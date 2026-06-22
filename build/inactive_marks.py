#!/usr/bin/env python3
"""Markiert nicht-funktionale (JS-/Backend-abhaengige) Bedienelemente sichtbar als
inaktiv und neutralisiert Formular-Submits – ohne die funktionierenden Elemente
(Desktop-Mega-Menue-Trigger sind <span>, Akkordeon ist <details>, der Hamburger
und das Mobile-Menue werden ausgenommen) zu beeintraechtigen.

Zusaetzlich: /de/smzh_ste/ -Links -> /de/steuererklaerung/ (Original-Redirectziel).
Idempotent.
"""
import os, re, glob

SMZH = os.path.join('site','smzh.ch')

CSS = ('<style id="smzh-inactive-css">'
       '.smzh-inactive{opacity:.55 !important;cursor:not-allowed !important}'
       '.smzh-inactive:hover{opacity:.55 !important}'
       '</style>')

JS = ('<script id="smzh-inactive-js">'
      '(function(){function ready(f){if(document.readyState!=="loading"){f();}else{document.addEventListener("DOMContentLoaded",f);}}'
      'ready(function(){'
      'var TITLE="Funktion im statischen Archiv-Mirror nicht verfügbar";'
      # alle Buttons ausser Hamburger + Mobile-Menue inaktiv markieren
      'document.querySelectorAll("button").forEach(function(b){'
      'if(b.closest("#smzh-mobile-menu"))return;'
      'if(b.querySelector(".lucide-menu"))return;'
      'b.classList.add("smzh-inactive");b.setAttribute("aria-disabled","true");if(!b.title)b.title=TITLE;'
      'b.addEventListener("click",function(e){e.preventDefault();e.stopPropagation();});});'
      # Formulare nicht absenden lassen
      'document.querySelectorAll("form").forEach(function(f){f.addEventListener("submit",function(e){e.preventDefault();});});'
      # Sprachwahl-/Suche-Trigger, die als <a> oder <div role=button> kommen koennten
      'document.querySelectorAll(".lucide-search").forEach(function(ic){var el=ic.closest("a,button,[role=button]")||ic.parentElement;if(el){el.classList.add("smzh-inactive");if(!el.title)el.title=TITLE;el.addEventListener("click",function(e){e.preventDefault();e.stopPropagation();});}});'
      '});})();'
      '</script>')

smzh_ste = re.compile(r'href="((?:\.\./)*)de/smzh_ste/index\.html"')

inj=0; remap=0
for f in glob.glob(SMZH+'/**/index.html', recursive=True):
    html=open(f,encoding='utf-8',errors='ignore').read()
    orig=html
    html, n = smzh_ste.subn(lambda m:'href="'+m.group(1)+'de/steuererklaerung/index.html"', html)
    if n: remap+=1
    if 'id="smzh-inactive-css"' not in html and '</head>' in html:
        html=html.replace('</head>', CSS+'</head>',1)
    if 'id="smzh-inactive-js"' not in html and '</body>' in html:
        html=html.replace('</body>', JS+'</body>',1); inj+=1
    if html!=orig:
        open(f,'w',encoding='utf-8').write(html)
print(f'inaktiv-markiert injiziert: {inj} Seiten; smzh_ste->steuererklaerung remap: {remap} Seiten')
