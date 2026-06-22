#!/usr/bin/env python3
"""Wandelt die gerenderten Snapshots in statische, lokal verlinkte Mirror-Seiten um.
- entfernt alle <script>-Tags (verhindert Re-Hydration, die den Inhalt wieder leert)
- schreibt Asset-URLs auf die lokalen Mirror-Pfade um (wie der wget-Mirror)
- laedt fehlende Bild-/Asset-Dateien vom Original-Server nach
- Fallback: laesst sich eine Datei nicht laden, bleibt die absolute Original-URL stehen
"""
import os, re, ssl, sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

SITE = 'site'
SMZH = os.path.join(SITE, 'smzh.ch')
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE
UA = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36'}

# key -> (rendered file, output index.html path, relative prefix to smzh.ch root)
PAGES = {
  'home':                     (os.path.join(SMZH,'de','index.html'), '../'),
  'smzhub':                   (os.path.join(SMZH,'de','smzhub','index.html'), '../../'),
  'rechner':                  (os.path.join(SMZH,'de','rechner','index.html'), '../../'),
  'markets':                  (os.path.join(SMZH,'de','markets','index.html'), '../../'),
  'karriere':                 (os.path.join(SMZH,'de','karriere','index.html'), '../../'),
  'terminvereinbaren':        (os.path.join(SMZH,'de','terminvereinbaren','index.html'), '../../'),
  'steuererklaerung':         (os.path.join(SMZH,'de','steuererklaerung','index.html'), '../../'),
  'vorsorgeanalyse':          (os.path.join(SMZH,'de','vorsorgeanalyse','index.html'), '../../'),
  'immobilienbewertung':      (os.path.join(SMZH,'de','immobilienbewertung','index.html'), '../../'),
  'preise-fuer-privatkunden': (os.path.join(SMZH,'de','preise-fuer-privatkunden','index.html'), '../../'),
  'preise-fuer-firmenkunden': (os.path.join(SMZH,'de','preise-fuer-firmenkunden','index.html'), '../../'),
  'uber-uns':                 (os.path.join(SMZH,'de','uber-uns','index.html'), '../../'),
  'geschaftspartner':         (os.path.join(SMZH,'de','geschaftspartner','index.html'), '../../'),
  'impressum':                (os.path.join(SMZH,'de','impressum','index.html'), '../../'),
  'datenschutz':              (os.path.join(SMZH,'de','datenschutz','index.html'), '../../'),
  'email-korrespondenz':      (os.path.join(SMZH,'de','email-korrespondenz','index.html'), '../../'),
}

dl_cache = {}
def download(url, dest):
    """Laedt url nach dest, wenn noch nicht vorhanden. True bei Erfolg/vorhanden."""
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return True
    if url in dl_cache:
        ok = dl_cache[url]
        return ok
    try:
        req = Request(url, headers=UA)
        data = urlopen(req, context=CTX, timeout=40).read()
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, 'wb') as f:
            f.write(data)
        dl_cache[url] = True
        return True
    except (URLError, HTTPError, Exception) as e:
        dl_cache[url] = False
        return False

stats = {'img':0, 'img_dl':0, 'img_fail':0, 'static':0, 'cms':0, 'asset_dl':0}

def process(key):
    rendered = os.path.join('build','rendered', key + '.html')
    out, prefix = PAGES[key]
    if not os.path.exists(rendered):
        print(f'  SKIP {key}: kein Render'); return
    html = open(rendered, encoding='utf-8', errors='ignore').read()

    # 1) alle <script> entfernen (inkl. Inhalt) + script-preloads
    html = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S|re.I)
    html = re.sub(r'<script\b[^>]*/>', '', html, flags=re.I)
    html = re.sub(r'<link\b[^>]*rel="(?:modulepreload|preload)"[^>]*as="script"[^>]*>', '', html, flags=re.I)
    html = re.sub(r'<link\b[^>]*rel="modulepreload"[^>]*>', '', html, flags=re.I)

    # 2) /_next/image/?url=A&w=W&q=Q  ->  lokale optimierte Datei (ggf. nachladen)
    #    Parameter koennen als & oder &amp; serialisiert sein.
    def repl_img(m):
        A, W, Q = m.group('a'), m.group('w'), m.group('q')
        fname = f'index.html@url={A}&w={W}&q={Q}'
        dest = os.path.join(SMZH, '_next', 'image', fname)
        origin = f'https://smzh.ch/_next/image/?url={A}&w={W}&q={Q}'
        stats['img'] += 1
        existed = os.path.exists(dest)
        if download(origin, dest):
            if not existed: stats['img_dl'] += 1
            return (prefix + '_next/image/index.html@url=' + A.replace('%','%25')
                    + f'&amp;w={W}&amp;q={Q}')
        stats['img_fail'] += 1
        return origin  # Fallback: Original-URL
    img_re = re.compile(
        r'/_next/image/?\?url=(?P<a>[^"\'\s,)&]+)&(?:amp;)?w=(?P<w>\d+)&(?:amp;)?q=(?P<q>\d+)')
    html = img_re.sub(repl_img, html)

    # 3) /_next/static/... (oder mit Host) -> lokal (CSS vorhanden; sonst nachladen)
    def repl_static(m):
        path = m.group('p')  # beginnt mit _next/static/...
        dest = os.path.join(SMZH, path)
        origin = 'https://smzh.ch/' + path
        stats['static'] += 1
        if os.path.exists(dest) or download(origin, dest):
            if not os.path.exists(os.path.join(SMZH, path)):
                pass
            return prefix + path
        return origin
    html = re.sub(r'(?:https://smzh\.ch)?/(?P<p>_next/static/[^"\'\s,)]+)', repl_static, html)

    # 4) /logo /favicon /fonts -> lokal (vorhanden; sonst nachladen)
    def repl_asset(m):
        path = m.group('p')
        dest = os.path.join(SMZH, path)
        origin = 'https://smzh.ch/' + path
        if os.path.exists(dest) or download(origin, dest):
            return prefix + path
        return origin
    html = re.sub(r'(?:https://smzh\.ch)?/(?P<p>(?:logo|favicon|fonts)/[^"\'\s,)]+)', repl_asset, html)

    # 5) cms.smzh.ch direkt referenziert -> lokal (nachladen)
    def repl_cms(m):
        path = m.group('p')  # uploads/...
        dest = os.path.join(SITE, 'cms.smzh.ch', path)
        origin = 'https://cms.smzh.ch/' + path
        stats['cms'] += 1
        if os.path.exists(dest) or download(origin, dest):
            # cms liegt parallel zu smzh.ch: ein Verzeichnis hoeher als smzh.ch-root
            return prefix + '../cms.smzh.ch/' + path
        return origin
    html = re.sub(r'https://cms\.smzh\.ch/(?P<p>uploads/[^"\'\s,)]+)', repl_cms, html)

    # 6) interne Seiten-Links (/de/...) -> lokal fuer die 16 gespiegelten Seiten,
    #    sonst absolut auf die Live-Site (damit Klicks nicht ins Leere laufen).
    PATHKEY = {
      '/de/': 'home', '/de/smzhub/': 'smzhub', '/de/rechner/': 'rechner',
      '/de/markets/': 'markets', '/de/karriere/': 'karriere',
      '/de/terminvereinbaren/': 'terminvereinbaren', '/de/steuererklaerung/': 'steuererklaerung',
      '/de/vorsorgeanalyse/': 'vorsorgeanalyse', '/de/immobilienbewertung/': 'immobilienbewertung',
      '/de/preise-fuer-privatkunden/': 'preise-fuer-privatkunden',
      '/de/preise-fuer-firmenkunden/': 'preise-fuer-firmenkunden', '/de/uber-uns/': 'uber-uns',
      '/de/geschaftspartner/': 'geschaftspartner', '/de/impressum/': 'impressum',
      '/de/datenschutz/': 'datenschutz', '/de/email-korrespondenz/': 'email-korrespondenz',
    }
    to_de = '' if key == 'home' else '../'
    def local_link(k):
        return to_de + ('index.html' if k == 'home' else k + '/index.html')
    def repl_link(m):
        path = m.group('p')
        norm = path if path.endswith('/') else path + '/'
        k = PATHKEY.get(norm)
        if k:
            return 'href="' + local_link(k) + '"'
        return 'href="https://smzh.ch' + path + '"'  # nicht gespiegelt -> Live
    html = re.sub(r'href="(?:https://smzh\.ch)?(?P<p>/de/[^"#?]*)"', repl_link, html)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  {key:28s} -> {out}  ({len(html)} bytes)')

if __name__ == '__main__':
    keys = sys.argv[1:] or list(PAGES.keys())
    for k in keys:
        process(k)
    print('STATS', stats)
