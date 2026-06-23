#!/usr/bin/env python3
"""smzhHub V4 – Advisory-Interface mit Navy-Hero-Karussell + Empfehlungs-Rail.
Baut auf V3 (digitales Advisory-Interface) auf und ersetzt die Production-Home:
- Voller Navy-Hero mit dezent animiertem Hintergrund + Karussell mit 6 kuratierten
  Aktuell-Inhalten.
- Decision Layer (Matrix), Advisory Journeys, Empfehlungs-Rail ("Beliebt bei …"),
  institutionelles Research Signal Band, CTA.
Sub-Seiten (Rubriken, Research, Dossiers, Serien, Archiv) werden aus V3
wiederverwendet, mit identischer Chrome-Injektion (V3-CSS + V4-CSS + V4-JS).
"""
import os, re, html as H
import sys; sys.path.insert(0,'build')
import build_hub_v3 as v3
from build_hub_v3 import (rows, link, img_of, imgt, fdate, esc, teaser, lead_rubric,
  komm_rubric, series_items, SERIES, SERIES_BY, NAV, NAV_BY, CAT, SMZH, CHROME_SRC,
  latest_month, hubbar, rubricnav, research_band, advisory_journey, cta_panel,
  rubric_page, research_page, series_page, dossier_page, archiv_inner, V3_CSS, balanced_div_end)

def find(sub):
    for r in rows:
        if sub.lower() in (r['title'] or '').lower(): return r
    return None

# Decisions (6, prompt-orientiert, alle mit realen Zielen)
v3.DECISIONS=[
 ('SARON oder Festhypothek?','Welche Laufzeit passt, wenn Zinsen tief bleiben, aber Sicherheit zählt?','eigenheim','de/hypothekenarten-im-vergleich/'),
 ('Kaufen oder warten?','Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenspielen.','eigenheim','de/wie-kaufe-ich-eine-immobilie/'),
 ('Amortisieren oder investieren?','Schulden tilgen oder das Geld anlegen – was sich für Sie mehr lohnt.','vermoegen','de/finanzplan-erstellen/'),
 ('Rente oder Kapital?','Die Pensionierungsentscheidung, die selten sauber vorbereitet wird.','zukunft','de/leistungen-im-alter/'),
 ('3a-Konto oder Wertschriften?','Warum Sparen allein über lange Zeiträume selten genügt.','vermoegen','de/altersvorsorge-optimierung-saeule-3a/'),
 ('Frühpensionierung oder weiterarbeiten?','Was ein früherer Ausstieg kostet – und wie man ihn finanziert.','zukunft','de/pensionsplanung/'),
]

# ---- 6 kuratierte Hero-Inhalte ----
def hero_items():
    picks=[]
    seen=set()
    def add(r):
        if r and r['id'] not in seen: picks.append(r); seen.add(r['id'])
    add(find('SNB hält am Nullzins'))
    add(find('neue Ära an der Fed'))
    add(find('AHV 2030'))
    add(find('Wohninitiativen'))
    igs=series_items('investment-guide'); add(igs[0] if igs else None)
    ios=series_items('immobilien-outlook'); add(ios[0] if ios else None)
    # auffüllen falls nötig
    for key in ['immobilien','kapitalmaerkte','vorsorge']:
        for r in lead_rubric(key):
            if len(picks)>=6: break
            add(r)
    return picks[:6]

def navy_hero():
    items=hero_items()
    slides=''; dots=''
    for i,r in enumerate(items):
        im=img_of(r,1200)
        cat=CAT.get(r.get('rubric'),'Aktuell')
        slides+=(f'<a class="v4-slide{" is-on" if i==0 else ""}" href="{link(r["path"])}">'
                 f'<span class="v4-slide-img">{imgt(im)}</span><span class="v4-slide-grad"></span>'
                 f'<span class="v4-slide-cap"><span class="v4-slide-chip">{esc(cat)} · {esc(fdate(r.get("date")))}</span>'
                 f'<span class="v4-slide-h">{esc(r["title"])}</span>'
                 f'<span class="v4-slide-p">{esc(teaser(r,120))}</span>'
                 f'<span class="v4-slide-go">Beitrag lesen →</span></span></a>')
        dots+=(f'<span class="v4-dot{" is-on" if i==0 else ""}" role="button" tabindex="0" '
               f'data-i="{i}" aria-label="Beitrag {i+1}"><b>{i+1:02d}</b>{esc(CAT.get(r.get("rubric"),"Aktuell"))}</span>')
    return (f'<header class="v4-hero"><div class="v4-hero-bg" aria-hidden="true"></div>'
            f'<div class="v4-hero-in">'
            f'<div class="v4-hero-l"><span class="v4-eyebrow">smzhHub · Research &amp; Advisory</span>'
            f'<h1 class="v4-hero-h1">Klarheit für Ihre nächste Finanzentscheidung.</h1>'
            f'<p class="v4-hero-sub">Einordnungen, Research und Ratgeber zu Eigenheim, Vermögen, Vorsorge '
            f'und Steuern – kuratiert nach Ihren Fragen, nicht nach Fachabteilung.</p>'
            f'<div class="v4-hero-cta"><a class="v4-btn" href="#v3-decide">Entscheidung finden</a>'
            f'<a class="v4-btn-g" href="#v4-journeys">Themen ansehen</a></div>'
            f'<div class="v4-hero-meta"><span><b>{len(rows)}</b> Beiträge</span><span><b>3</b> Research-Reihen</span>'
            f'<span><b>monatlich</b> aktualisiert</span></div></div>'
            f'<div class="v4-hero-stage v4-car"><div class="v4-slides">{slides}</div>'
            f'<div class="v4-dots">{dots}</div></div></div></header>')

def rail_card(r):
    im=img_of(r,640)
    return (f'<a class="v4-rc" href="{link(r["path"])}"><span class="v4-rc-img">{imgt(im)}</span>'
            f'<span class="v4-rc-b"><span class="v4-chip v3-chip-{r.get("rubric") or "x"}">{esc(CAT.get(r.get("rubric"),"smzh"))}</span>'
            f'<span class="v4-rc-t">{esc(r["title"])}</span>'
            f'<span class="v4-rc-m">{esc(fdate(r.get("date")))}'+(f' · {r["readingTime"]} Min' if r.get("readingTime") else '')+'</span></span></a>')

def recommendation_rail():
    # "Beliebt bei Eigenheim-Interessierten" – Eigenheim-lastig + Querbezug
    pool=[]
    seen=set()
    for r in lead_rubric('immobilien'):
        if r['id'] not in seen: pool.append(r); seen.add(r['id'])
    for key in ['kapitalmaerkte','vorsorge']:
        ls=lead_rubric(key)
        if ls and ls[0]['id'] not in seen: pool.append(ls[0]); seen.add(ls[0]['id'])
    cards=''.join(rail_card(r) for r in pool[:9])
    return (f'<section class="v4-rail"><div class="v4-rail-head"><div>'
            f'<span class="v3-eyebrow">Empfohlen</span><h2 class="v3-h2">Beliebt bei Eigenheim-Interessierten</h2></div>'
            f'<a class="v3-sec-more" href="{link("de/smzhub-eigenheim/")}">Mehr zu Eigenheim →</a></div>'
            f'<div class="v4-rail-track">{cards}</div></section>')

def home_inner():
    return (hubbar()+rubricnav('aktuell')+navy_hero()+v3.decision_matrix()
            +'<div id="v4-journeys">'+advisory_journey('eigenheim')+advisory_journey('vermoegen')+advisory_journey('zukunft')+'</div>'
            +recommendation_rail()+research_band()+cta_panel())

V4_CSS='''<style id="smzh-v4-css">
#ed-root .v4-eyebrow{display:inline-block;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;font-weight:800;color:#7fb0d6}
/* Navy Hero – full bleed innerhalb des Containers */
#ed-root .v4-hero{position:relative;background:#07314C;border-radius:16px;overflow:hidden;margin:.4rem 0 3rem;isolation:isolate}
#ed-root .v4-hero-bg{position:absolute;inset:0;z-index:0;background:
  radial-gradient(60% 80% at 12% 18%,rgba(0,80,255,.28),transparent 60%),
  radial-gradient(50% 70% at 90% 12%,rgba(31,157,122,.20),transparent 60%),
  radial-gradient(70% 90% at 80% 100%,rgba(0,80,255,.16),transparent 60%);
  background-size:160% 160%;animation:v4drift 24s ease-in-out infinite alternate}
#ed-root .v4-hero-bg:after{content:"";position:absolute;inset:0;opacity:.5;
  background-image:radial-gradient(rgba(255,255,255,.06) 1px,transparent 1px);background-size:26px 26px}
@keyframes v4drift{0%{background-position:0% 0%}100%{background-position:100% 100%}}
@media(prefers-reduced-motion:reduce){#ed-root .v4-hero-bg{animation:none}}
#ed-root .v4-hero-in{position:relative;z-index:1;display:grid;grid-template-columns:1fr;gap:2rem;padding:2.4rem}
@media(min-width:940px){#ed-root .v4-hero-in{grid-template-columns:1fr 1.05fr;gap:3rem;padding:3.2rem 3rem;align-items:center}}
#ed-root .v4-hero-l{color:#fff}
#ed-root .v4-hero-h1{font-size:clamp(2rem,3.8vw,3rem);font-weight:800;line-height:1.07;letter-spacing:-.02em;color:#fff;margin:.9rem 0 1rem}
#ed-root .v4-hero-sub{color:#c4d4e2;font-size:clamp(1.02rem,1.4vw,1.18rem);line-height:1.55;max-width:46ch;margin:0 0 1.6rem}
#ed-root .v4-hero-cta{display:flex;gap:.8rem;flex-wrap:wrap}
#ed-root .v4-btn{display:inline-block;background:#fff;color:#07314C;font-weight:700;text-decoration:none;padding:.8rem 1.5rem;border-radius:8px;font-size:.96rem}
#ed-root .v4-btn:hover{background:#e7eff6}
#ed-root .v4-btn-g{display:inline-block;color:#fff;font-weight:600;text-decoration:none;padding:.8rem 1.2rem;border:1px solid rgba(255,255,255,.35);border-radius:8px}
#ed-root .v4-btn-g:hover{border-color:#fff}
#ed-root .v4-hero-meta{display:flex;gap:1.8rem;margin-top:1.8rem;padding-top:1.3rem;border-top:1px solid rgba(255,255,255,.18)}
#ed-root .v4-hero-meta span{font-size:.82rem;color:#9fb6c8}
#ed-root .v4-hero-meta b{display:block;font-size:1.25rem;color:#fff;font-weight:800;font-variant-numeric:tabular-nums}
/* Hero-Karussell */
#ed-root .v4-hero-stage{position:relative}
#ed-root .v4-slides{position:relative;border-radius:12px;overflow:hidden;aspect-ratio:16/11;background:#0a1f31;box-shadow:0 30px 60px -30px rgba(0,0,0,.6)}
#ed-root .v4-slide{position:absolute;inset:0;opacity:0;transition:opacity .7s ease;text-decoration:none;pointer-events:none}
#ed-root .v4-slide.is-on{opacity:1;pointer-events:auto}
#ed-root .v4-slide-img,#ed-root .v4-slide-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#ed-root .v4-slide-grad{position:absolute;inset:0;background:linear-gradient(to top,rgba(6,20,33,.96) 8%,rgba(6,20,33,.45) 45%,rgba(6,20,33,0) 75%)}
#ed-root .v4-slide-cap{position:absolute;left:0;right:0;bottom:0;padding:1.6rem 1.7rem;color:#fff;display:block}
#ed-root .v4-slide-chip{display:inline-block;font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:#9fd0ee;background:rgba(255,255,255,.12);padding:.22rem .6rem;border-radius:5px}
#ed-root .v4-slide-h{display:block;font-size:clamp(1.25rem,2vw,1.7rem);font-weight:800;line-height:1.16;margin:.6rem 0 .4rem}
#ed-root .v4-slide-p{display:block;color:#c8d6e3;font-size:.92rem;line-height:1.45;max-width:46ch}
#ed-root .v4-slide-go{display:inline-block;margin-top:.6rem;font-size:.8rem;font-weight:800;letter-spacing:.04em;color:#9fd0ee}
#ed-root .v4-dots{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin-top:.8rem}
@media(min-width:520px){#ed-root .v4-dots{grid-template-columns:repeat(6,1fr)}}
#ed-root .v4-dot{display:flex;flex-direction:column;gap:.15rem;font-size:.6rem;text-transform:uppercase;letter-spacing:.04em;color:#8aa3b8;cursor:pointer;padding:.45rem .2rem .35rem;border-top:2px solid rgba(255,255,255,.18);transition:.15s}
#ed-root .v4-dot b{font-size:.78rem;font-weight:800;color:#c4d4e2}
#ed-root .v4-dot.is-on{border-top-color:#9fd0ee;color:#cfe3f1}
#ed-root .v4-dot.is-on b{color:#fff}
#ed-root .v4-dot:hover{color:#cfe3f1}
/* Empfehlungs-Rail (horizontal) */
#ed-root .v4-rail{margin:0 0 3.4rem}
#ed-root .v4-rail-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;margin-bottom:1.2rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
#ed-root .v4-rail-track{display:grid;grid-auto-flow:column;grid-auto-columns:78%;gap:1rem;overflow-x:auto;scroll-snap-type:x mandatory;padding-bottom:.6rem;scrollbar-width:thin}
@media(min-width:680px){#ed-root .v4-rail-track{grid-auto-columns:38%}}
@media(min-width:1000px){#ed-root .v4-rail-track{grid-auto-columns:23.5%}}
#ed-root .v4-rc{scroll-snap-align:start;display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;background:#fff;transition:.15s}
#ed-root .v4-rc:hover{border-color:var(--blue);box-shadow:0 16px 36px -22px rgba(7,49,76,.55)}
#ed-root .v4-rc-img{display:block;aspect-ratio:16/10;overflow:hidden;background:var(--surf2)}
#ed-root .v4-rc-img img{width:100%;height:100%;object-fit:cover}
#ed-root .v4-rc-b{padding:.9rem 1rem 1.1rem;display:flex;flex-direction:column;gap:.4rem}
#ed-root .v4-chip{display:inline-block;font-size:.62rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:.18rem .5rem;border-radius:5px;background:var(--surf2);color:var(--brand);width:max-content}
#ed-root .v4-rc-t{font-weight:700;color:var(--brand);line-height:1.3;font-size:1rem}
#ed-root .v4-rc:hover .v4-rc-t{color:var(--blue)}
#ed-root .v4-rc-m{font-size:.76rem;color:var(--faint);text-transform:uppercase;letter-spacing:.04em}
</style>'''

V4_JS='''<script id="smzh-v4-js">
(function(){function r(f){if(document.readyState!=='loading')f();else document.addEventListener('DOMContentLoaded',f);}
r(function(){document.querySelectorAll('.v4-car').forEach(function(c){
var sl=c.querySelectorAll('.v4-slide'),dt=c.querySelectorAll('.v4-dot'),i=0,n=sl.length,t=null;if(n<2)return;
function go(k){i=(k+n)%n;sl.forEach(function(e,j){e.classList.toggle('is-on',j===i)});dt.forEach(function(d,j){d.classList.toggle('is-on',j===i)})}
function au(){t=setInterval(function(){go(i+1)},5500)}function rs(){clearInterval(t);au()}
dt.forEach(function(d,j){d.addEventListener('click',function(){go(j);rs()});d.addEventListener('keydown',function(e){if(e.key==='Enter'){go(j);rs()}})});
c.addEventListener('mouseenter',function(){clearInterval(t)});c.addEventListener('mouseleave',au);go(0);au();});});})();
</script>'''

def main():
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*"', html)
    o=html.index('>',m.start())+1; c=balanced_div_end(html,m.start())
    before=html[:o]; after=html[c-6:]; orig=html[o:c-6]
    if 'id="smzh-v3-css"' not in before: before=before.replace('</head>', V3_CSS+'</head>',1)
    if 'id="smzh-v4-css"' not in before: before=before.replace('</head>', V4_CSS+'</head>',1)
    before=re.sub(r'(<div class="content-hub[^"]*")', r'\1 id="ed-root"', before, count=1)
    if 'id="smzh-v4-js"' not in after: after=after.replace('</body>', V4_JS+'</body>',1)
    def write(path, inner, title):
        full=before+inner+after
        full=re.sub(r'<title>.*?</title>','<title>'+H.escape(title)+'</title>',full,count=1,flags=re.S)
        d=os.path.join(SMZH,path.strip('/')); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)
    write('de/smzhub/', home_inner(), 'smzhHub – Klarheit für Ihre Finanzentscheidungen')
    for tab in ['eigenheim','vermoegen','zukunft','steuern']:
        write(NAV_BY[tab][1], rubric_page(tab), f'{NAV_BY[tab][0]} – smzhHub')
    write('de/smzhub-research/', research_page(), 'Research & Publikationen – smzhHub')
    for dk in ['eigenheim','pensionierung']:
        write('de/smzhub-dossier-'+dk+'/', dossier_page(dk), 'Dossier – smzhHub')
    for skey,*_ in SERIES:
        write('de/'+SERIES_BY[skey][2]+'/', series_page(skey), f'{SERIES_BY[skey][0]} – smzhHub')
    write('de/smzhub-archiv/', archiv_inner(orig), 'Alle Inhalte – smzhHub')
    print('OK V4: Navy-Hero-Karussell + Rail + Journeys + Research. Home, 4 Rubriken, Research, 2 Dossiers, 3 Serien, Archiv.')

if __name__=='__main__':
    main()
