#!/usr/bin/env python3
"""Repariert die injizierten Mega-Menues:
 (1) ersetzt den alten <style>-Fix durch eine Version mit fester Panelbreite
     (behebt die Verzerrung / das char-weise Umbrechen der linken Spalte)
 (2) fuegt ein kleines Vanilla-JS ein, das die 2. Ebene umsetzt: beim Hover
     einer linken Kategorie wird der zugehoerige rechte Block gezeigt
     (Mapping linkes Item i -> rechter Block i+1), per Toggle der 'hidden'-Klasse
     – genau wie im Original. Kein React, nur Menue-Interaktion.
Idempotent.
"""
import os, re, glob

SMZH = os.path.join('site', 'smzh.ch')

STYLE = """<style id="smzh-megamenu-fix">
nav.smzh-navbar .group{position:relative}
nav.smzh-navbar .group>.dropdown-navigation-wrapper{display:none !important}
nav.smzh-navbar .group:hover>.dropdown-navigation-wrapper,
nav.smzh-navbar .group:focus-within>.dropdown-navigation-wrapper{display:flex !important}
.dropdown-navigation-wrapper{width:760px !important;max-width:94vw !important;left:0 !important}
.dropdown-navigation-wrapper>div{width:100% !important}
</style>"""

SCRIPT = """<script id="smzh-menu-js">
(function(){function init(){document.querySelectorAll('.dropdown-navigation-wrapper').forEach(function(w){
var inner=w.firstElementChild;if(!inner)return;var left=inner.firstElementChild;
var right=w.querySelector('.dropdown-nav-right');if(!left||!right)return;
var items=[].slice.call(left.children),blocks=[].slice.call(right.children);
function setActive(k){blocks.forEach(function(b,i){if(i===k){b.classList.remove('hidden');}else if(i!==0||k!==0){b.classList.add('hidden');}});if(k!==0&&blocks[0])blocks[0].classList.add('hidden');if(k===0&&blocks[0])blocks[0].classList.remove('hidden');}
setActive(0);
items.forEach(function(it,idx){it.addEventListener('mouseenter',function(){var t=idx+1,blk=blocks[t];if(blk&&blk.textContent.trim().length>0){setActive(t);}else{setActive(0);}});});
w.addEventListener('mouseleave',function(){setActive(0);});});}
if(document.readyState!=='loading'){init();}else{document.addEventListener('DOMContentLoaded',init);}})();
</script>"""

OLD_STYLE = re.compile(r'<style id="smzh-megamenu-fix">.*?</style>', re.S)

patched = 0
for f in glob.glob(SMZH + '/**/index.html', recursive=True):
    html = open(f, encoding='utf-8', errors='ignore').read()
    if 'dropdown-navigation-wrapper' not in html:
        continue
    orig = html
    if OLD_STYLE.search(html):
        html = OLD_STYLE.sub(STYLE, html, count=1)
    elif '</head>' in html:
        html = html.replace('</head>', STYLE + '</head>', 1)
    if 'id="smzh-menu-js"' not in html and '</body>' in html:
        html = html.replace('</body>', SCRIPT + '</body>', 1)
    if html != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        patched += 1
print('gepatcht:', patched)
