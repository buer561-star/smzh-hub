#!/usr/bin/env python3
"""Baut die 4 Mega-Menue-Panels (aus build/menus.json) in jede Seite ein und
macht sie ohne JavaScript per CSS (Hover/Focus) bedienbar.

- Panels werden als Kind des jeweiligen .group-Triggers eingefuegt.
- Alle Panel-Links/-Assets werden pro Seitentiefe lokalisiert (kein Original-Link).
- Ein injiziertes <style> blendet das Panel beim Hover des Triggers ein; die
  verschachtelte Spalten-Logik nutzt das vorhandene Tailwind-group-hover-CSS.
Idempotent: bereits injizierte Seiten werden uebersprungen.
"""
import os, re, json, sys
sys.path.insert(0, 'build')
import postprocess_all as P  # fuer download() + gleiche Lokalisierungslogik

SMZH = os.path.join('site', 'smzh.ch')
MENUS = json.load(open('build/menus.json', encoding='utf-8'))

def target_local(tp, prefix):
    tp = tp.split('#')[0].split('?')[0]
    segs = [s for s in tp.strip('/').split('/') if s]
    if not segs: segs = ['de']
    return prefix + '/'.join(segs) + '/index.html'

def localize(frag, prefix):
    # /_next/image
    def ri(m):
        A,W,Q=m.group('a'),m.group('w'),m.group('q')
        dest=os.path.join(SMZH,'_next','image',f'index.html@url={A}&w={W}&q={Q}')
        P.download(f'https://smzh.ch/_next/image/?url={A}&w={W}&q={Q}', dest)
        return prefix+'_next/image/index.html@url='+A.replace('%','%25')+f'&amp;w={W}&amp;q={Q}'
    frag=re.sub(r'/_next/image/?\?url=(?P<a>[^"\'\s,)&]+)&(?:amp;)?w=(?P<w>\d+)&(?:amp;)?q=(?P<q>\d+)', ri, frag)
    # /_next/static
    def rs(m):
        p=m.group('p'); P.download('https://smzh.ch/'+p, os.path.join(SMZH,p)); return prefix+p
    frag=re.sub(r'(?:https://smzh\.ch)?/(?P<p>_next/static/[^"\'\s,)]+)', rs, frag)
    # logo/favicon/fonts
    def ra(m):
        p=m.group('p'); P.download('https://smzh.ch/'+p, os.path.join(SMZH,p)); return prefix+p
    frag=re.sub(r'(?:https://smzh\.ch)?/(?P<p>(?:logo|favicon|fonts)/[^"\'\s,)]+)', ra, frag)
    # cms
    def rc(m):
        p=m.group('p'); P.download('https://cms.smzh.ch/'+p, os.path.join('site','cms.smzh.ch',p))
        return prefix+'../cms.smzh.ch/'+p
    frag=re.sub(r'https://cms\.smzh\.ch/(?P<p>uploads/[^"\'\s,)]+)', rc, frag)
    # interne Links
    frag=re.sub(r'href="(?:https://(?:www\.)?smzh\.ch)?(?P<p>/(?:de|en)/[^"#?]*)"',
                lambda m:'href="'+target_local(m.group('p'),prefix)+'"', frag)
    frag=re.sub(r'href="https?://(?:www\.)?smzh\.ch/?"','href="'+target_local('/',prefix)+'"', frag)
    frag=re.sub(r'href="/"','href="'+target_local('/',prefix)+'"', frag)
    return frag

STYLE = """<style id="smzh-megamenu-fix">
nav.smzh-navbar .group{position:relative}
nav.smzh-navbar .group>.dropdown-navigation-wrapper{display:none !important}
nav.smzh-navbar .group:hover>.dropdown-navigation-wrapper,
nav.smzh-navbar .group:focus-within>.dropdown-navigation-wrapper{display:flex !important}
</style>"""

# Panels pro Tiefe (1,2,3) vorbereiten
PREFIXES = {1:'../', 2:'../../', 3:'../../../'}
PANELS = {d:{} for d in PREFIXES}
for d,pref in PREFIXES.items():
    for m in MENUS:
        if m['html']:
            PANELS[d][m['label']] = localize(m['html'], pref)

def inject(path):
    html = open(path, encoding='utf-8', errors='ignore').read()
    if 'dropdown-navigation-wrapper' in html or 'smzh-navbar' not in html:
        return False  # schon injiziert oder keine Navbar
    rel_dir = os.path.relpath(os.path.dirname(path), SMZH)
    depth = 0 if rel_dir=='.' else len([s for s in rel_dir.split(os.sep) if s])
    depth = min(max(depth,1),3)
    panels = PANELS[depth]
    changed = False
    for label, panel in panels.items():
        # Trigger-Span mit genau diesem Label finden und Panel direkt dahinter einfuegen
        pat = re.compile(r'(<span data-dropdown-trigger="true"[^>]*>'+re.escape(label)+r'<svg.*?</svg></span>)', re.S)
        new, n = pat.subn(lambda m: m.group(1)+panel, html, count=1)
        if n:
            html = new; changed = True
    if changed:
        if '<style id="smzh-megamenu-fix">' not in html:
            html = html.replace('</head>', STYLE+'</head>', 1)
        with open(path,'w',encoding='utf-8') as f:
            f.write(html)
    return changed

def main():
    import glob
    files = glob.glob(SMZH+'/**/index.html', recursive=True)
    done=0
    for f in files:
        if inject(f): done+=1
    print(f'injiziert in {done}/{len(files)} Seiten')

if __name__=='__main__':
    main()
