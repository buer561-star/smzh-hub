#!/usr/bin/env python3
"""Behebt nicht-funktionale (JS-abhaengige) Elemente im statischen Mirror:
 (1) Cookie-Consent-Banner ausblenden (laesst sich ohne JS nicht wegklicken und
     ueberdeckt Inhalt) -> per CSS .rrc-container + dessen fixe Huelle.
 (2) "Mehr anzeigen" (Load-More, JS) -> Link auf die Artikel-Uebersicht.
Idempotent.
"""
import os, re, glob

SMZH = os.path.join('site', 'smzh.ch')

COOKIE_STYLE = ('<style id="smzh-static-fix">'
    '.rrc-container{display:none !important}'
    'div.fixed.bottom-0.left-0.z-50:has(.rrc-container){display:none !important}'
    '</style>')

btn_re = re.compile(
    r'<button\b[^>]*aria-label="smzh-Mehr anzeigen"[^>]*>(?P<inner>.*?)</button>', re.S)

def prefix_for(path):
    rel_dir = os.path.relpath(os.path.dirname(path), SMZH)
    depth = 0 if rel_dir == '.' else len([s for s in rel_dir.split(os.sep) if s])
    return '../' * max(depth, 1)

cookie=0; more=0
for f in glob.glob(SMZH + '/**/index.html', recursive=True):
    html = open(f, encoding='utf-8', errors='ignore').read()
    orig = html
    # (1) Cookie-Banner ausblenden
    if 'rrc-container' in html and 'id="smzh-static-fix"' not in html and '</head>' in html:
        html = html.replace('</head>', COOKIE_STYLE + '</head>', 1)
        cookie += 1
    # (2) "Mehr anzeigen" -> Link auf Artikel-Uebersicht
    if 'smzh-Mehr anzeigen' in html:
        pref = prefix_for(f)
        def repl(m):
            return ('<a href="'+pref+'de/artikel/index.html" '
                    'class="smzh-btn flex items-center gap-2 rounded-lg border border-border-400 '
                    'bg-white text-neutral-900 hover:bg-powder-blue px-[18px] py-3" '
                    'aria-label="Mehr anzeigen">'+m.group('inner')+'</a>')
        html, n = btn_re.subn(repl, html)
        if n: more += 1
    if html != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
print(f'Cookie-Banner ausgeblendet: {cookie} Seiten; "Mehr anzeigen" verlinkt: {more} Seiten')
