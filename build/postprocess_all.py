#!/usr/bin/env python3
"""Wandelt ALLE gerenderten Seiten (build/rendered2/**/index.html) in statische,
vollstaendig lokal verlinkte Mirror-Seiten um.

Strikte Regel: NICHTS verweist auf das Original smzh.ch / cms.smzh.ch.
- alle <script> werden entfernt (verhindert Re-Hydration, die Inhalt leert)
- Assets (CSS/JS-Reste/Bilder/Fonts) -> lokale Mirror-Pfade (fehlende werden geladen)
- alle internen Seiten-Links (/de/, /en/, smzh.ch-absolut) -> lokale relative Pfade
- schlaegt ein Download fehl oder ist ein Ziel nicht gespiegelt, bleibt der Link
  trotzdem LOKAL (ggf. lokaler 404) -- niemals die Original-URL.
Externe Links (Social Media, YouTube etc.) bleiben unveraendert.
"""
import os, re, ssl, sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

RENDERED = 'build/rendered2'
SITE = 'site'
SMZH = os.path.join(SITE, 'smzh.ch')
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}

dl_cache = {}
def download(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return True
    if url in dl_cache:
        return dl_cache[url]
    try:
        data = urlopen(Request(url, headers=UA), context=CTX, timeout=40).read()
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'wb') as f:
            f.write(data)
        dl_cache[url] = True
        return True
    except (URLError, HTTPError, Exception):
        dl_cache[url] = False
        return False

stats = dict(pages=0, img=0, img_dl=0, img_fail=0, static=0, static_fail=0, cms=0, cms_fail=0, links=0)

def page_paths(rel):
    """rel = '/de/foo/' -> (output index.html, prefix zum smzh.ch-root)."""
    segs = [s for s in rel.strip('/').split('/') if s]
    out = os.path.join(SMZH, *segs, 'index.html')
    prefix = '../' * len(segs)
    return out, prefix

def target_local(target_path, prefix):
    """'/de/foo/' -> prefix + 'de/foo/index.html'."""
    segs = [s for s in target_path.strip('/').split('/') if s]
    if not segs:
        segs = ['de']  # '/' -> Startseite de
    return prefix + '/'.join(segs) + '/index.html'

def process(rel, html):
    out, prefix = page_paths(rel)

    # 1) Skripte + Script-Preloads entfernen
    html = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S|re.I)
    html = re.sub(r'<script\b[^>]*/>', '', html, flags=re.I)
    html = re.sub(r'<link\b[^>]*rel="(?:modulepreload|preload)"[^>]*as="script"[^>]*>', '', html, flags=re.I)
    html = re.sub(r'<link\b[^>]*rel="modulepreload"[^>]*>', '', html, flags=re.I)

    # 2) /_next/image/?url=A&w=W&q=Q -> lokale optimierte Datei
    def repl_img(m):
        A, W, Q = m.group('a'), m.group('w'), m.group('q')
        dest = os.path.join(SMZH, '_next', 'image', f'index.html@url={A}&w={W}&q={Q}')
        origin = f'https://smzh.ch/_next/image/?url={A}&w={W}&q={Q}'
        stats['img'] += 1
        if not (os.path.exists(dest) or download(origin, dest)):
            stats['img_fail'] += 1
        else:
            if dl_cache.get(origin): stats['img_dl'] += 1
        return prefix + '_next/image/index.html@url=' + A.replace('%','%25') + f'&amp;w={W}&amp;q={Q}'
    html = re.sub(r'/_next/image/?\?url=(?P<a>[^"\'\s,)&]+)&(?:amp;)?w=(?P<w>\d+)&(?:amp;)?q=(?P<q>\d+)',
                  repl_img, html)

    # 3) /_next/static/... -> lokal
    def repl_static(m):
        p = m.group('p')
        dest = os.path.join(SMZH, p)
        stats['static'] += 1
        if not (os.path.exists(dest) or download('https://smzh.ch/' + p, dest)):
            stats['static_fail'] += 1
        return prefix + p
    html = re.sub(r'(?:https://smzh\.ch)?/(?P<p>_next/static/[^"\'\s,)]+)', repl_static, html)

    # 4) /logo /favicon /fonts -> lokal
    def repl_asset(m):
        p = m.group('p')
        dest = os.path.join(SMZH, p)
        if not (os.path.exists(dest) or download('https://smzh.ch/' + p, dest)):
            pass
        return prefix + p
    html = re.sub(r'(?:https://smzh\.ch)?/(?P<p>(?:logo|favicon|fonts)/[^"\'\s,)]+)', repl_asset, html)

    # 5) cms.smzh.ch -> lokal
    def repl_cms(m):
        p = m.group('p')
        dest = os.path.join(SITE, 'cms.smzh.ch', p)
        stats['cms'] += 1
        if not (os.path.exists(dest) or download('https://cms.smzh.ch/' + p, dest)):
            stats['cms_fail'] += 1
        return prefix + '../cms.smzh.ch/' + p
    html = re.sub(r'https://cms\.smzh\.ch/(?P<p>uploads/[^"\'\s,)]+)', repl_cms, html)

    # 6) interne Seiten-Links (/de/.., /en/.., smzh.ch-absolut, "/") -> lokal
    def repl_link(m):
        tp = m.group('p') or '/'
        stats['links'] += 1
        return 'href="' + target_local(tp, prefix) + '"'
    # smzh.ch-absolute oder root-relative Links auf /de/ oder /en/
    html = re.sub(r'href="(?:https://smzh\.ch)?(?P<p>/(?:de|en)/[^"#?]*)"', repl_link, html)
    # blanke Startseiten-Links
    html = re.sub(r'href="https://smzh\.ch/?"', 'href="' + target_local('/', prefix) + '"', html)
    html = re.sub(r'href="/"', 'href="' + target_local('/', prefix) + '"', html)
    # evtl. verbliebene smzh.ch-Wurzel-Links (Sicherheitsnetz, keine Original-Verweise)
    html = re.sub(r'(href|src)="https://smzh\.ch(/[^"]*)"',
                  lambda m: f'{m.group(1)}="' + prefix + m.group(2).lstrip('/') + '"', html)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    stats['pages'] += 1

def main():
    files = []
    for root, _, names in os.walk(RENDERED):
        for n in names:
            if n == 'index.html':
                full = os.path.join(root, n)
                rel = '/' + os.path.relpath(os.path.dirname(full), RENDERED).replace(os.sep, '/') + '/'
                if rel == '/./': rel = '/'
                files.append((rel, full))
    files.sort()
    print(f'{len(files)} Seiten zu verarbeiten')
    for i, (rel, full) in enumerate(files, 1):
        html = open(full, encoding='utf-8', errors='ignore').read()
        process(rel, html)
        if i % 50 == 0:
            print(f'  [{i}/{len(files)}] {stats}')
    print('FERTIG', stats)

if __name__ == '__main__':
    main()
