#!/usr/bin/env python3
"""Originalgetreues mobiles Drilldown-Menue (ersetzt das fruehere flache Menue).
Struktur wie im Original-Mobilmenue:
  Hauptebene: Privatkunden→, Firmenkunden→, smzh Welt→, Über smzh→ (Drilldown)
              + smzHub, Rechner, smzh Markets, Karriere (Direktlinks)
  je Reiter:  Übersicht-/Direktlinks + Kategorien→ (Drilldown)
  je Kategorie: deren Links
Navigation per Zurueck-Pfeil; kleines Vanilla-JS (kein React). Links lokalisiert.
Idempotent (Marker smzh-mm-v2). Entfernt das alte flache Menue.
"""
import os, re, json, glob, html as H

SMZH=os.path.join('site','smzh.ch')
STRUCT={ (m['label']): {c['name']:c['links'] for c in m['cats']} for m in json.load(open('build/menu-structure.json',encoding='utf-8')) }

# Aufbau gemaess Original-Mobilmenue (aus build/mobile-tree.json ermittelt)
MENUS=[
 ('Privatkunden',('Privatkunden Übersicht','/de/privatkunden/'),[],
   ['Anlagen','Finanzen','Hypotheken','Immobilien','Recht','Steuern','Versicherungen','Vorsorge']),
 ('Firmenkunden',('Firmenkunden Übersicht','/de/firmenkunden/'),[('Real Estate Advisory','/de/real-estate-advisory/')],
   ['Finanzierung','Vorsorge','Versicherungen','Steuern']),
 ('smzh Welt',None,[('smzh Impact Storys','/de/impact-storys/'),('smzh Finanzfritiig','/de/finanzfriitig/'),
                    ('smzh Ambassadors','/de/ambassadors/'),('Unsere GewinnerInnen','/de/gewinnerinnen/')],
   ['smzh Partnerschaften']),
 ('Über smzh',None,[('Über uns','/de/uber-uns/'),('Vision & Mission','/de/vision-und-mission/'),
                    ('Geschäftspartner','/de/geschaftspartner/'),('Mitgliedschaften','/de/mitgliedschaften/'),
                    ('Kontakt','/de/kontakt/')],[]),
]
TOPLINKS=[('smzHub','/de/smzhub/'),('Rechner','/de/rechner/'),('smzh Markets','/de/markets/'),('Karriere','/de/karriere/')]

def loc(tp,prefix):
    segs=[s for s in tp.strip('/').split('/') if s] or ['de']
    return prefix+'/'.join(segs)+'/index.html'
def esc(s): return H.escape(s)

def build(prefix):
    screens=[]
    # Hauptebene
    root=['<div class="smzh-mm-screen" data-screen="root">']
    for mi,(label,ov,directs,cats) in enumerate(MENUS):
        root.append(f'<button class="smzh-mm-drill" data-target="m{mi}" data-title="{esc(label)}">{esc(label)}</button>')
    for t,h in TOPLINKS:
        root.append(f'<a class="smzh-mm-top" href="{loc(h,prefix)}">{esc(t)}</a>')
    root.append('</div>')
    screens.append(''.join(root))
    # je Reiter
    for mi,(label,ov,directs,cats) in enumerate(MENUS):
        s=[f'<div class="smzh-mm-screen" data-screen="m{mi}" hidden>']
        if ov: s.append(f'<a href="{loc(ov[1],prefix)}">{esc(ov[0])}</a>')
        for t,h in directs: s.append(f'<a href="{loc(h,prefix)}">{esc(t)}</a>')
        for ci,cat in enumerate(cats):
            links=STRUCT.get(label,{}).get(cat,[])
            if links:
                s.append(f'<button class="smzh-mm-drill" data-target="m{mi}c{ci}" data-title="{esc(cat)}">{esc(cat)}</button>')
            else:
                s.append(f'<span class="smzh-mm-head-lbl">{esc(cat)}</span>')
        s.append('</div>')
        screens.append(''.join(s))
        # je Kategorie
        for ci,cat in enumerate(cats):
            links=STRUCT.get(label,{}).get(cat,[])
            if not links: continue
            cs=[f'<div class="smzh-mm-screen" data-screen="m{mi}c{ci}" hidden>']
            for l in links:
                cs.append(f'<a href="{loc(l["href"],prefix)}">{esc(l["text"])}</a>')
            cs.append('</div>')
            screens.append(''.join(cs))
    panel=('<div id="smzh-mobile-menu" data-v="smzh-mm-v2" role="dialog" aria-label="Menü">'
           '<div class="smzh-mm-bar"><button class="smzh-mm-back" aria-label="Zurück" hidden>&#8592;</button>'
           '<span class="smzh-mm-title">Menu</span>'
           '<button class="smzh-mm-close" aria-label="Menü schliessen">&times;</button></div>'
           '<div class="smzh-mm-screens">'+''.join(screens)+'</div>'
           f'<div class="smzh-mm-foot"><a class="smzh-mm-cta" href="{loc("/de/terminvereinbaren/",prefix)}">Termin vereinbaren</a>'
           '<span class="smzh-mm-de">DE</span></div></div>')
    return panel

CSS='''<style id="smzh-mm-css">
#smzh-mobile-menu{position:fixed;inset:0;z-index:9999;background:#fff;display:none;flex-direction:column}
html.smzh-mm-open #smzh-mobile-menu{display:flex}html.smzh-mm-open{overflow:hidden}
#smzh-mobile-menu .smzh-mm-bar{display:flex;align-items:center;gap:.5rem;padding:1rem 1.1rem;border-bottom:1px solid #eef1f4}
#smzh-mobile-menu .smzh-mm-title{font-weight:700;font-size:1.3rem;color:#07314C;flex:1}
#smzh-mobile-menu .smzh-mm-back,#smzh-mobile-menu .smzh-mm-close{background:none;border:none;font-size:1.6rem;line-height:1;color:#07314C;cursor:pointer;padding:.2rem .4rem}
#smzh-mobile-menu .smzh-mm-screens{flex:1;overflow-y:auto;-webkit-overflow-scrolling:touch;padding:.5rem 1.1rem 1rem}
#smzh-mobile-menu .smzh-mm-screen[hidden]{display:none}
#smzh-mobile-menu a,#smzh-mobile-menu .smzh-mm-drill{display:flex;justify-content:space-between;align-items:center;width:100%;text-align:left;padding:.85rem .2rem;color:#07314C;text-decoration:none;border:none;background:none;border-bottom:1px solid #eef1f4;font-size:1.05rem;cursor:pointer;font-family:inherit}
#smzh-mobile-menu .smzh-mm-drill::after{content:"\\2192";color:#0050ff;font-size:1.1rem}
#smzh-mobile-menu .smzh-mm-head-lbl{display:block;padding:.85rem .2rem;color:#07314C;border-bottom:1px solid #eef1f4;font-size:1.05rem}
#smzh-mobile-menu .smzh-mm-foot{border-top:1px solid #eef1f4;padding:1rem 1.1rem;display:flex;align-items:center;gap:1rem}
#smzh-mobile-menu .smzh-mm-cta{flex:1;justify-content:center;background:#07314C;color:#fff;border-radius:.6rem;font-weight:600;padding:.8rem;border-bottom:none}
#smzh-mobile-menu .smzh-mm-de{color:#07314C;font-weight:600;opacity:.55}
@media(min-width:1024px){#smzh-mobile-menu{display:none !important}html.smzh-mm-open{overflow:auto}}
</style>'''

JS='''<script id="smzh-mm-js">
(function(){function ready(f){if(document.readyState!=='loading'){f();}else{document.addEventListener('DOMContentLoaded',f);}}
ready(function(){var menu=document.getElementById('smzh-mobile-menu');if(!menu)return;var root=document.documentElement;
var screens=menu.querySelectorAll('.smzh-mm-screen'),titleEl=menu.querySelector('.smzh-mm-title'),back=menu.querySelector('.smzh-mm-back');
var stack=[{id:'root',t:'Menu'}];
function render(){var top=stack[stack.length-1];screens.forEach(function(s){s.hidden=(s.getAttribute('data-screen')!==top.id);});titleEl.textContent=top.t;back.hidden=stack.length<2;menu.querySelector('.smzh-mm-screens').scrollTop=0;}
function open(){root.classList.add('smzh-mm-open');stack=[{id:'root',t:'Menu'}];render();}
function close(){root.classList.remove('smzh-mm-open');}
menu.querySelectorAll('.smzh-mm-drill').forEach(function(b){b.addEventListener('click',function(){stack.push({id:b.getAttribute('data-target'),t:b.getAttribute('data-title')});render();});});
back.addEventListener('click',function(){if(stack.length>1){stack.pop();render();}});
menu.querySelector('.smzh-mm-close').addEventListener('click',close);
menu.querySelectorAll('a').forEach(function(a){a.addEventListener('click',close);});
document.querySelectorAll('.lucide-menu').forEach(function(ic){var btn=ic.closest('button')||ic.parentElement;if(btn&&!btn.__mm){btn.__mm=1;btn.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();open();});}});
document.addEventListener('keydown',function(e){if(e.key==='Escape')close();});render();});})();
</script>'''

# alte (flache) Mobile-Menue-Bestandteile entfernen
OLD_PANEL=re.compile(r'<div id="smzh-mobile-menu".*?<script id="smzh-mobile-js">.*?</script>', re.S)
OLD_CSS=re.compile(r'<style id="smzh-mobile-css">.*?</style>', re.S)

PREFIX={1:'../',2:'../../',3:'../../../'}
PANELS={d:build(p) for d,p in PREFIX.items()}

n=0
for f in glob.glob(SMZH+'/**/index.html',recursive=True):
    html=open(f,encoding='utf-8',errors='ignore').read()
    if 'lucide-menu' not in html: continue
    if 'data-v="smzh-mm-v2"' in html: continue
    html=OLD_PANEL.sub('', html)
    html=OLD_CSS.sub('', html)
    rel=os.path.relpath(os.path.dirname(f),SMZH)
    depth=0 if rel=='.' else len([s for s in rel.split(os.sep) if s]); depth=min(max(depth,1),3)
    if '</head>' in html: html=html.replace('</head>', CSS+'</head>',1)
    if '</body>' in html: html=html.replace('</body>', PANELS[depth]+JS+'</body>',1)
    open(f,'w',encoding='utf-8').write(html)
    n+=1
print('neues Drilldown-Mobilmenü injiziert in',n,'Seiten')
