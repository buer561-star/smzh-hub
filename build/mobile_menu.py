#!/usr/bin/env python3
"""Baut ein funktionierendes Mobile-/Hamburger-Menue (das Original-Mobilmenue ist
JS-befuellt und im statischen Snapshot leer -> bei < 1024px fehlten alle Reiter).

Quelle: build/menus.json (4 Dropdowns) + feste Top-Links. Erzeugt ein Overlay-
Panel mit <details>-Akkordeons; der Hamburger oeffnet es per Mini-JS. Alle Links
pro Seitentiefe lokalisiert (kein Original-Verweis). Idempotent.
"""
import os, re, json, glob, html as H
import sys; sys.path.insert(0,'build')
import postprocess_all as P  # download() + Bild-Localisierung nicht noetig hier

SMZH = os.path.join('site','smzh.ch')
MENUS = json.load(open('build/menus.json',encoding='utf-8'))

def extract_links(html):
    out=[]; seen=set()
    for a in re.finditer(r'<a\b[^>]*href="([^"]+)"[^>]*>(.*?)</a>', html, re.S):
        href=a.group(1); text=H.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>','',a.group(2)))).strip()
        if text and href.startswith('/de') and (href,text) not in seen:
            seen.add((href,text)); out.append((text,href))
    return out

SECTIONS=[]
for m in MENUS:
    if m['html']:
        SECTIONS.append((m['label'], extract_links(m['html'])))

# feste Top-Links (Standalone-Reiter rechts in der Navbar)
TOPLINKS=[('smzHub','/de/smzhub/'),('Rechner','/de/rechner/'),
          ('smzh Markets','/de/markets/'),('Karriere','/de/karriere/')]
CTA=('Termin vereinbaren','/de/terminvereinbaren/')

def loc(tp, prefix):
    segs=[s for s in tp.strip('/').split('/') if s] or ['de']
    return prefix+'/'.join(segs)+'/index.html'

def build_panel(prefix):
    parts=['<div id="smzh-mobile-menu" role="dialog" aria-label="Menü">',
           '<button class="smzh-mm-close" aria-label="Menü schliessen">&times;</button>',
           '<nav class="smzh-mm-nav">']
    for label, links in SECTIONS:
        parts.append('<details class="smzh-mm-sec"><summary>'+H.escape(label)+'</summary><div class="smzh-mm-sub">')
        for t,h in links:
            parts.append('<a href="'+loc(h,prefix)+'">'+H.escape(t)+'</a>')
        parts.append('</div></details>')
    for t,h in TOPLINKS:
        parts.append('<a class="smzh-mm-top" href="'+loc(h,prefix)+'">'+H.escape(t)+'</a>')
    parts.append('<a class="smzh-mm-cta" href="'+loc(CTA[1],prefix)+'">'+H.escape(CTA[0])+'</a>')
    parts.append('</nav></div>')
    return ''.join(parts)

STYLE='''<style id="smzh-mobile-css">
#smzh-mobile-menu{position:fixed;inset:0;z-index:9999;background:#fff;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:1.1rem 1.25rem 3rem;display:none}
html.smzh-mm-open #smzh-mobile-menu{display:block}
html.smzh-mm-open{overflow:hidden}
#smzh-mobile-menu .smzh-mm-close{position:absolute;top:.6rem;right:1rem;font-size:2.2rem;line-height:1;background:none;border:none;color:#07314C;cursor:pointer}
#smzh-mobile-menu .smzh-mm-nav{margin-top:2.4rem;display:flex;flex-direction:column}
#smzh-mobile-menu a{display:block;padding:.7rem 0;color:#07314C;text-decoration:none;border-bottom:1px solid #eef1f4;font-size:1.05rem}
#smzh-mobile-menu details.smzh-mm-sec{border-bottom:1px solid #eef1f4}
#smzh-mobile-menu details>summary{padding:.85rem 0;font-weight:600;color:#07314C;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center}
#smzh-mobile-menu details>summary::-webkit-details-marker{display:none}
#smzh-mobile-menu details>summary::after{content:"+";font-size:1.3rem;color:#0050ff}
#smzh-mobile-menu details[open]>summary::after{content:"–"}
#smzh-mobile-menu .smzh-mm-sub{padding-bottom:.5rem}
#smzh-mobile-menu .smzh-mm-sub a{padding-left:.9rem;font-size:.98rem;color:#3a5a72;border-bottom:none;padding-top:.5rem;padding-bottom:.5rem}
#smzh-mobile-menu .smzh-mm-top{font-weight:600}
#smzh-mobile-menu .smzh-mm-cta{margin-top:1rem;background:#07314C;color:#fff;text-align:center;border-radius:.6rem;border:none;font-weight:600}
@media (min-width:1024px){#smzh-mobile-menu{display:none !important}html.smzh-mm-open{overflow:auto}}
</style>'''

SCRIPT='''<script id="smzh-mobile-js">
(function(){function ready(fn){if(document.readyState!=='loading'){fn();}else{document.addEventListener('DOMContentLoaded',fn);}}
ready(function(){var panel=document.getElementById('smzh-mobile-menu');if(!panel)return;
var root=document.documentElement;
function open(){root.classList.add('smzh-mm-open');}function close(){root.classList.remove('smzh-mm-open');}
document.querySelectorAll('.lucide-menu').forEach(function(ic){var btn=ic.closest('button')||ic.parentElement;if(btn&&!btn.__smzhmm){btn.__smzhmm=1;btn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();open();});}});
var c=panel.querySelector('.smzh-mm-close');if(c)c.addEventListener('click',close);
panel.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});});})();
</script>'''

PREFIXES={1:'../',2:'../../',3:'../../../'}
PANELS={d:build_panel(p) for d,p in PREFIXES.items()}

def inject(path):
    html=open(path,encoding='utf-8',errors='ignore').read()
    if 'id="smzh-mobile-menu"' in html: return False
    if 'lucide-menu' not in html: return False  # keine mobile Navbar
    rel=os.path.relpath(os.path.dirname(path),SMZH)
    depth=0 if rel=='.' else len([s for s in rel.split(os.sep) if s]); depth=min(max(depth,1),3)
    if '</head>' in html: html=html.replace('</head>', STYLE+'</head>',1)
    if '</body>' in html: html=html.replace('</body>', PANELS[depth]+SCRIPT+'</body>',1)
    open(path,'w',encoding='utf-8').write(html)
    return True

n=0
for f in glob.glob(SMZH+'/**/index.html',recursive=True):
    if inject(f): n+=1
print('Mobile-Menü injiziert in',n,'Seiten')
