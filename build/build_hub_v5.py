#!/usr/bin/env python3
"""smzhHub V5 – kuratierte editoriale Landing Page nach smzh Design System.
Navy #03314B · Teal #185E7F · Light Blue #E9F4FC · Plus Jakarta Sans.
Schreibt nur site/smzh.ch/de/smzhub/index.html. Sub-Seiten (Rubriken/Serien/
Research/Dossiers) bleiben bestehen und werden verlinkt.
Struktur: Hero+Karussell · Entscheidungen · Saison (Krankenkasse) · 3 Rubriken
(Eigenheim/Anlagen/Vorsorge) · Research Signals.
"""
import os, re, html as H, urllib.parse, json
from datetime import datetime
import sys; sys.path.insert(0,'build')
import postprocess_all as P

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch'); CHROME_SRC='build/backup/pre-ia/smzhub-index.html'
BASE='https://buer561-star.github.io/smzh-hub/smzh.ch'  # Canonical-/OG-Basis (GitHub Pages)
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
BYP={r['path']:r for r in rows}
P_='../../'
MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def teaser(p,n=120):
    r=item(p); t=(r.get('excerpt') or '') if r else ''
    return (t[:n].rsplit(' ',1)[0]+'…') if len(t)>n else t
def link(p): return P_+'/'.join(s for s in p.strip('/').split('/') if s)+'/index.html'
def item(p): return BYP.get(p) or BYP.get('/'+p.strip('/')+'/')
def opt_img(cms,w):
    if not cms: return None
    enc=urllib.parse.quote('https://cms.smzh.ch'+cms,safe='')
    dest=os.path.join(SMZH,'_next','image',f'index.html@url={enc}&w={w}&q=75')
    P.download(f'https://smzh.ch/_next/image/?url={enc}&w={w}&q=75',dest)
    return (P_+'_next/image/index.html@url='+enc.replace('%','%25')+f'&amp;w={w}&amp;q=75') if os.path.exists(dest) else None
def img_of(p,w):
    r=item(p); return opt_img(r.get('image'),w) if r else None
def imgt(src): return f'<img loading="lazy" src="{src}" alt="">' if src else ''
def series_items(k): return sorted([r for r in rows if r.get('series')==k],key=lambda r:r.get('date') or '',reverse=True)
def meta_of(p):
    r=item(p)
    if not r: return ''
    m=fdate(r.get('date'))
    if r.get('readingTime'): m+=f' · {r["readingTime"]} Min'
    return m
def rmin(p):
    r=item(p)
    return f'{r["readingTime"]} Min' if r and r.get('readingTime') else ''

# ---- kuratierte Inhalte ----
ig=series_items('investment-guide'); io=series_items('immobilien-outlook'); hr=series_items('hypothekenradar')
HERO=[  # (path-or-row, kategorie)
 ('/de/artikel/snb-zinsentscheid-juni/','Eigenheim'),
 ('/de/artikel/neue-aera-fed/','Anlagen'),
 ('/de/artikel/ahv-2030-pensionierung-planungsfrage/','Vorsorge'),
 ('/de/artikel/zuercher-wohnungsinitiativen/','Eigenheim'),
 (ig[0]['path'] if ig else None,'Anlagen'),
 (io[0]['path'] if io else None,'Eigenheim'),
]
DECISIONS=[('Hypothek','SARON oder Festhypothek?','Welche Strategie 2026 trägt, wenn die SNB-Zinsen tief sind, aber Planungssicherheit zählt.','/de/ratgeber-saron-oder-festhypothek/'),
 ('Eigenheim','Kaufen oder warten?','Wie Preise, Eigenkapital und Tragbarkeit 2026 zusammenspielen – und worauf es jetzt ankommt.','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
 ('Vorsorge','Rente oder Kapital?','Die Pensionierungsentscheidung 2026 – mit Folgen für Steuern, Sicherheit und Flexibilität.','/de/ratgeber-rente-oder-kapitalbezug/'),
 ('Anlegen','3a Konto oder Wertschriften?','Warum die Anlageform der Säule 3a über Jahrzehnte mehr bewirkt als die Einzahlung – Stand 2026.','/de/ratgeber-saeule-3a-konto-oder-wertschriften/'),
 ('Eigenheim','Reicht mein Einkommen für die Bank?','Wie Banken die Tragbarkeit 2026 rechnen – und was Sie daran heute beeinflussen können.','/de/ratgeber-tragbarkeit-hypothek/'),
 ('Vermögen','Amortisieren oder investieren?','Schulden tilgen oder anlegen: was sich bei den Zinsen von 2026 für Sie langfristig mehr lohnt.','/de/ratgeber-amortisieren-oder-investieren/'),
 ('Vorsorge','Früher pensionieren oder weiterarbeiten?','Was ein früherer Ausstieg 2026 kostet – und wie er finanzierbar bleibt.','/de/ratgeber-frueher-pensionieren/'),
 ('Steuern','Wo verschenke ich jedes Jahr Steuern?','Welche Abzüge und Einzahlungen Sie für das Steuerjahr 2026 jetzt noch nutzen können.','/de/ratgeber-steuern-sparen/'),
 ('Eigenheim','Wie viel Eigenkapital brauche ich wirklich?','20 Prozent sind nur die halbe Wahrheit – worauf es 2026 zusätzlich ankommt.','/de/ratgeber-eigenkapital-eigenheim/'),
 ('Vorsorge','Lohnt sich die Säule 3a für mich?','Wann sich 3a 2026 wirklich lohnt – und wann Ihr Geld anderswo besser aufgehoben ist.','/de/ratgeber-lohnt-sich-saeule-3a/')]
RUBRICS=[
 {'label':'Eigenheim','intro':'Eigenheim & Hypothek','desc':'Für alle, die kaufen, verlängern oder ihre Finanzierung neu ausrichten wollen.','more':'/de/smzhub-eigenheim/',
  'arts':['/de/artikel/snb-zinsentscheid-juni/','/de/artikel/zuercher-wohnungsinitiativen/','/de/artikel/abstimmung-keine-10-millionen-schweiz/','/de/artikel/eigenmietwert-sanierung-bundesrat-2029/'],
  'tool':{'imgfrom':'/de/artikel/zuercher-wohnungsinitiativen/','href':'/de/immobilienbewertung-rechner/','tag':'Rechner','t':'Tragbarkeit in zwei Minuten prüfen','go':'Tragbarkeit berechnen'}},
 {'label':'Vermögen','intro':'Vermögen & Anlegen','desc':'Märkte, Zinsen und Portfolios verständlich eingeordnet – ohne tägliches Börsenrauschen.','more':'/de/smzhub-vermoegen/',
  'arts':['/de/artikel/neue-aera-fed/','/de/artikel/usa-iran-deal/','/de/artikel/boersengang-spacex/','/de/artikel/sell-in-may/'],
  'tool':{'imgfrom':'/de/artikel/boersengang-spacex/','href':'/de/risikoprofil-erstellen/','tag':'Check','t':'Welche Anlagestrategie passt zu Ihnen?','go':'Anlagestrategie einordnen'}},
 {'label':'Vorsorge','intro':'Vorsorge & Pensionierung','desc':'AHV, BVG, 3a und Pensionierung als Lebensplanung – nicht als Produktliste.','more':'/de/smzhub-zukunft/',
  'arts':['/de/artikel/ahv-2030-pensionierung-planungsfrage/','/de/artikel/kapitalbezug-steuerentscheid/','/de/artikel/fruehpensionierung-unter-druck/','/de/artikel/gender-pension-gap/'],
  'tool':{'imgfrom':'/de/artikel/fruehpensionierung-unter-druck/','href':'/de/vorsorgeanalyse/','tag':'Analyse','t':'Reicht Ihr Geld bis in die Pensionierung?','go':'Vorsorge analysieren'}}]
FLAGMETA={'hypothekenradar':('Hypotheken-Radar','monatlich'),'investment-guide':('Investment Guide','monatlich'),
 'immobilien-outlook':('Immobilien-Outlook','quartalsweise'),'dossier':('Pensionierung planen','Dossier · Storyline')}
RESEARCH=[('Hypotheken-Radar','monatlich · 9 Ausgaben','/de/smzhub-serie-hypotheken-radar/','hypothekenradar'),
 ('Investment Guide','monatlich · 16 Ausgaben','/de/smzhub-serie-investment-guide/','investment-guide'),
 ('Immobilien-Outlook','quartalsweise · 7 Ausgaben','/de/smzhub-serie-immobilien-outlook/','immobilien-outlook')]
# Saison (Krankenkasse) – kuratiertes Saisonthema, Links auf reale Seiten
SEASON_HERO=('Krankenkasse 2027: prüfen, bevor die Police automatisch weiterläuft','Prämie, Franchise und Modellwahl wirken jedes Jahr direkt auf Ihr Budget. Der richtige Moment zu prüfen ist, bevor die neue Police automatisch weiterläuft.','Prämien vergleichen','/de/krankenkasse-vergleichen/')
SEASON_SUBS=[('Prämien optimieren ohne Leistungsverlust','/de/krankenkassen-praemienoptimierung/'),
 ('Welche Franchise passt zu Ihrem Profil?','/de/krankenkasse-vergleichen/'),
 ('Budget für 2027 durchrechnen','/de/budgetrechner/')]

# ---- Render ----
def hero():
    slides=''; dots=''
    its=[(p,c) for p,c in HERO if p]
    for i,(p,cat) in enumerate(its):
        im=img_of(p,1080); r=item(p)
        if not r: continue
        slides+=(f'<a class="h-slide{" on" if i==0 else ""}" href="{link(p)}">'
                 f'<span class="h-slide-img">{imgt(im)}</span>'
                 f'<span class="h-slide-c"><span class="h-slide-cat">{esc(cat)}</span>'
                 f'<span class="h-slide-t">{esc(r["title"])}</span>'
                 f'<span class="h-slide-p">{esc(teaser(p,110))}</span>'
                 f'<span class="h-slide-go">Beitrag lesen →</span></span></a>')
        dots+=f'<span class="h-dot{" on" if i==0 else ""}" role="button" tabindex="0" data-i="{i}" aria-label="Beitrag {i+1}"></span>'
    return (f'<section class="v5-hero"><div class="v5-hero-in">'
            f'<div class="v5-hero-l"><h1>Klarheit für Ihre nächste Finanzentscheidung.</h1>'
            f'<p>smzhHub ordnet Märkte, Eigenheim, Vorsorge und Steuern so ein, dass Sie Ihre nächste Entscheidung sicherer treffen.</p></div>'
            f'<div class="v5-hero-r v5-car"><div class="h-slides">{slides}</div><div class="h-dots">{dots}</div></div>'
            f'</div></section>')

def decisions():
    cards=''
    shapes=['#185E7F','#03314B','#185E7F','#03314B']
    for i,(cat,q,desc,p) in enumerate(DECISIONS):
        cards+=(f'<a class="v5-dec" href="{link(p)}"><span class="v5-dec-cat">{esc(cat)}</span>'
                f'<span class="v5-dec-q">{esc(q)}</span><span class="v5-dec-d">{esc(desc)}</span>'
                f'<span class="v5-dec-fresh">Aktualisiert · 2026</span>'
                f'<span class="v5-dec-shape" style="background:{shapes[i%4]}"></span></a>')
    nav=('<div class="v5-dec-nav"><span class="v5-dec-arrow v5-dec-prev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
         '<span class="v5-dec-arrow v5-dec-next" role="button" tabindex="0" aria-label="Weiter">›</span></div>')
    return (f'<section class="v5-sec v5-dec-sec"><div class="v5-head"><div><h2>Entscheiden statt nur informieren</h2>'
            f'<p class="v5-sub">Konkrete Einordnungen zu den Finanzfragen, die 2026 anstehen – laufend aktualisiert.</p></div>'
            f'{nav}</div>'
            f'<div class="v5-dec-vp"><div class="v5-dec-track">{cards}</div></div></section>')

def season():
    t,teaser,cl,cp=SEASON_HERO
    subs=''
    for st,sp in SEASON_SUBS:
        subs+=f'<a class="v5-se-sub" href="{link(sp)}"><span class="v5-se-sub-t">{esc(st)}</span><span class="v5-se-sub-go">→</span></a>'
    hero=(f'<a class="v5-se-hero" href="{link(cp)}"><span class="v5-se-tag">Aktuell relevant</span>'
          f'<span class="v5-se-h">{esc(t)}</span><span class="v5-se-p">{esc(teaser)}</span>'
          f'<span class="v5-se-cta">{esc(cl)} →</span></a>')
    return f'<section class="v5-sec"><div class="v5-season">{hero}<div class="v5-se-subs">{subs}</div></div></section>'

def flag_card(key,path):
    name,cad=FLAGMETA[key]
    cov=''
    if key!='dossier':
        its=series_items(key); im=opt_img(its[0]['image'],640) if its else None
        cov=f'<span class="v5-flag-cov">{imgt(im)}</span>'
    else:
        cov='<span class="v5-flag-cov v5-flag-cov-dos"><span class="v5-flag-dos-i">◆</span></span>'
    return (f'<a class="v5-flag" href="{link(path)}">{cov}<span class="v5-flag-b">'
            f'<span class="v5-flag-cad">{esc(cad)}</span><span class="v5-flag-n">{esc(name)}</span>'
            f'<span class="v5-flag-go">{"Dossier öffnen" if key=="dossier" else "Zur Serie"} →</span></span></a>')

FLAGCAD={'hypothekenradar':'monatlich','investment-guide':'monatlich','immobilien-outlook':'quartalsweise','dossier':'Dossier'}
FLAGNM={'hypothekenradar':'Hypotheken-Radar','investment-guide':'Investment Guide','immobilien-outlook':'Immobilien-Outlook','dossier':'Pensionierung planen'}
def rubric(rb, idx):
    arts=[p for p in rb['arts'] if item(p)]
    leadp=arts[0]; subs=arts[1:4]
    lead=item(leadp); im=img_of(leadp,1080)
    rm=rmin(leadp); goline=(rm+' · ' if rm else '')+'Beitrag lesen'
    hero=(f'<a class="v5-rub-hero" href="{link(leadp)}"><span class="v5-rh-img">{imgt(im)}</span>'
          f'<span class="v5-rh-b"><span class="v5-rh-cat">{esc(rb["label"])}</span>'
          f'<span class="v5-rh-t">{esc(lead["title"])}</span>'
          f'<span class="v5-rh-p">{esc(teaser(leadp,170))}</span>'
          f'<span class="v5-rh-go">{esc(goline)}</span></span></a>')
    sub_html=''.join(f'<a class="v5-sl" href="{link(p)}"><span class="v5-sl-t">{esc(item(p)["title"])}</span>'
                     +(f'<span class="v5-sl-m">{esc(rmin(p))}</span>' if rmin(p) else '')+'</a>' for p in subs)
    # Mid-Hero / subtiler CTA: highlighted Tool/Check/Analyse mit Bild (Platzhalter-Slot)
    t=rb['tool']; tim=img_of(t['imgfrom'],640)
    mid=(f'<a class="v5-mid" href="{link(t["href"])}"><span class="v5-mid-img">{imgt(tim)}'
         f'<span class="v5-mid-tag">{esc(t["tag"])}</span></span>'
         f'<span class="v5-mid-b"><span class="v5-mid-t">{esc(t["t"])}</span>'
         f'<span class="v5-mid-go">{esc(t["go"])}</span></span></a>')
    side=f'<div class="v5-rub-side"><div class="v5-sl-list">{sub_html}</div>{mid}</div>'
    rev = idx%2==1
    cols = '1fr 1.45fr' if rev else '1.45fr 1fr'
    cls = 'v5-rub-grid rev' if rev else 'v5-rub-grid'
    desc=f'<p class="v5-rub-desc">{esc(rb["desc"])}</p>' if rb.get('desc') else ''
    return (f'<section class="v5-sec v5-rub-sec"><div class="v5-rub-head"><h3 class="v5-rub-intro">{esc(rb["intro"])}</h3>{desc}</div>'
            f'<div class="{cls}" style="--cols:{cols}">{hero+side}</div></section>')

def research():
    cols=''
    for name,cad,path,key in RESEARCH:
        its=series_items(key); im=opt_img(its[0]['image'],640) if its else None
        cols+=(f'<a class="v5-rs" href="{link(path)}"><span class="v5-rs-cov">{imgt(im)}</span>'
               f'<span class="v5-rs-n">{esc(name)}</span><span class="v5-rs-cad">{esc(cad)}</span>'
               f'<span class="v5-rs-go">Serie ansehen →</span></a>')
    return (f'<section class="v5-research"><div class="v5-rs-in"><div class="v5-head"><div>'
            f'<h2>Wiederkehrende Einschätzungen von smzh</h2></div>'
            f'<a class="v5-more" href="{link("/de/smzhub-research/")}">Alle Publikationen →</a></div>'
            f'<div class="v5-rs-row">{cols}</div></div></section>')

# ---- Themenwelten als Funnel-Kacheln (3 oben, 2 unten) – je eigene Hub-Seite ----
FUNNELS=[
 ('Eigenheim & Hypothek','Kaufen, finanzieren oder die Hypothek neu ausrichten.','/de/smzhub-eigenheim/'),
 ('Immobilienanlagen','Renditeobjekte und indirekte Immobilienanlagen einordnen.','/de/smzhub-immobilienanlagen/'),
 ('Kapitalmärkte & Anlagen','Märkte, Portfolios und die passende Anlagestrategie.','/de/smzhub-vermoegen/'),
 ('Vorsorge & Pensionierung','AHV, BVG, 3a und der Weg in die Pensionierung.','/de/smzhub-zukunft/'),
 ('smzh horizon','Perspektiven, Trends und Ausblick von smzh.','/de/smzhub-horizon/'),
]

def funnels():
    cards=''
    for i,(t,d,href) in enumerate(FUNNELS):
        wide=' wide' if i>=3 else ''
        cards+=(f'<a class="v5-funnel{wide}" href="{link(href)}">'
                f'<span class="v5-funnel-n">{i+1:02d}</span>'
                f'<span class="v5-funnel-t">{esc(t)}</span>'
                f'<span class="v5-funnel-d">{esc(d)}</span>'
                f'<span class="v5-funnel-go">Bereich öffnen</span></a>')
    return ('<section class="v5-funnels">'
            '<div class="v5-fn-top"><div class="v5-fn-in">'
            '<h2 class="v5-fn-h">Ihre Themenwelten</h2>'
            '<p class="v5-fn-sub">Fünf Einstiege in den smzhHub – wählen Sie Ihren Schwerpunkt.</p>'
            '</div></div>'
            f'<div class="v5-fn-body"><div class="v5-fn-in"><div class="v5-fgrid">{cards}</div></div></div>'
            '</section>')

def home_inner():
    return ('<div class="v5">'+hero()+funnels()+'<div class="v5-wrap">'
            +decisions()+''.join(rubric(r,i) for i,r in enumerate(RUBRICS))+'</div></div>')

FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
CSS='''<style id="smzh-v5-css">
#ed-root{--navy:#03314B;--teal:#185E7F;--lblue:#E9F4FC;--ink:#1c2b36;--muted:#5b6b7a;--faint:#8b9aa8;--line:#e5e7eb;max-width:none;padding:0 !important;gap:0 !important}
#ed-root,.v5,.v5 *{font-family:'Plus Jakarta Sans',-apple-system,'Segoe UI',Roboto,sans-serif;box-sizing:border-box}
.v5{color:var(--ink)}
.v5-wrap{max-width:1180px;margin:0 auto;padding:0 1.5rem}
.v5 h1,.v5 h2,.v5 h3{letter-spacing:-.02em;color:var(--navy);margin:0}
.v5 a{text-decoration:none;color:inherit}
.v5-sec{margin:5rem 0}
.v5-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;margin-bottom:1.4rem}
.v5-head h2{font-size:clamp(1.4rem,2.4vw,1.85rem);font-weight:800}
.v5-sub{color:var(--muted);font-size:.92rem;margin:.35rem 0 0}
.v5-more{color:var(--teal);font-weight:700;font-size:.9rem;white-space:nowrap}
.v5-more:hover{color:var(--navy)}
/* Themenwelten – Funnel-Band: setzt das Navy des Hero fort, Kacheln schweben über der Naht */
.v5-funnels{position:relative}
.v5-fn-top{background:var(--navy);padding:2.6rem 1.5rem 3.6rem}
.v5-fn-in{max-width:1180px;margin:0 auto}
.v5-fn-h{color:#fff;font-size:clamp(1.4rem,2.4vw,1.85rem);font-weight:800;line-height:1.15}
.v5-fn-sub{color:#bcd3e2;font-size:.95rem;line-height:1.5;margin:.45rem 0 0;max-width:60ch}
.v5-fn-body{background:linear-gradient(180deg,#e7f0f8 0%,#f3f9fd 55%,#fff 100%);padding:0 1.5rem 3rem}
.v5-fn-body .v5-fgrid{margin-top:-2.6rem}
.v5-wrap>.v5-sec:first-child{margin-top:3.6rem}
.v5-fgrid{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:760px){.v5-fgrid{grid-template-columns:repeat(6,1fr)}
 .v5-funnel{grid-column:span 2}.v5-funnel.wide{grid-column:span 3}}
.v5-funnel{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:.5rem;min-height:172px;background:#fff;border:1px solid #e2e9f0;border-radius:16px;padding:1.6rem 1.7rem;box-shadow:0 18px 40px -22px rgba(3,49,75,.5);transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s ease,border-color .25s ease}
.v5-funnel::before{content:"";position:absolute;left:0;top:0;height:100%;width:3px;background:var(--teal);transform:scaleY(0);transform-origin:top;transition:transform .3s ease}
.v5-funnel:hover{transform:translateY(-4px);box-shadow:0 28px 52px -24px rgba(3,49,75,.5);border-color:#cdd6df}
.v5-funnel:hover::before{transform:scaleY(1)}
.v5-funnel-n{position:absolute;top:1.1rem;right:1.4rem;font-size:1.35rem;font-weight:800;color:#e3ebf2;letter-spacing:-.02em;transition:color .25s ease}
.v5-funnel:hover .v5-funnel-n{color:var(--teal)}
.v5-funnel-t{font-size:1.22rem;font-weight:800;color:var(--navy);line-height:1.2;max-width:82%}
.v5-funnel-d{font-size:.92rem;color:var(--muted);line-height:1.5;flex:1}
.v5-funnel-go{display:inline-flex;align-items:center;gap:.3em;font-size:.86rem;font-weight:700;color:var(--teal);margin-top:.2rem}
.v5-funnel-go::after{content:"\\2192";transition:transform .25s ease}
.v5-funnel:hover .v5-funnel-go::after{transform:translateX(4px)}
/* Themenwelt-Seiten (Kategorie-Stubs) */
.v5-phead{background:var(--navy);color:#fff;border-radius:0 0 22px 22px;padding:3.4rem 1.5rem 3.6rem}
.v5-phead-in{max-width:1180px;margin:0 auto}
.v5-eyebrow{font-size:.8rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#7fb3cc;margin:0 0 .6rem}
.v5-phead h1{color:#fff;font-size:clamp(1.9rem,2.7vw,2.5rem);font-weight:800;line-height:1.12}
.v5-phead p{color:#bcd3e2;font-size:1.08rem;line-height:1.6;margin:1rem 0 0;max-width:60ch}
.v5-lead{font-size:1.1rem;line-height:1.65;color:var(--ink);max-width:64ch}
.v5-note{background:var(--lblue);border:1px solid #d7e6f2;border-radius:12px;padding:1.2rem 1.4rem;color:var(--ink);line-height:1.6}
.v5-back{display:inline-flex;align-items:center;gap:.4em;font-weight:700;color:var(--teal)}
.v5-backsec{margin-top:3rem}
/* Entscheidungs-Karten: Aktualitäts-Chip */
.v5-dec-fresh{margin-top:auto;padding-top:.7rem;font-size:.72rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;color:var(--faint);display:inline-flex;align-items:center;gap:.45em}
.v5-dec-fresh::before{content:"";width:6px;height:6px;border-radius:50%;background:#28a745;box-shadow:0 0 0 3px rgba(40,167,69,.15)}
/* Ratgeber-Artikel (Lead-Gen + SEO) */
.art-bc{font-size:.8rem;color:var(--faint);margin:1.2rem 0 .2rem}
.art-bc a{color:var(--teal);font-weight:600}
.art-body{max-width:760px;margin:0 auto;padding-bottom:1rem}
.art-lead{font-size:1.18rem;line-height:1.65;color:var(--navy);font-weight:500;margin:1.4rem 0 1.2rem}
.art-fig{margin:1.4rem 0 1.6rem}
.art-fig img{width:100%;height:auto;border-radius:14px;display:block;box-shadow:0 18px 40px -24px rgba(3,49,75,.5)}
.art-fig figcaption{font-size:.82rem;color:var(--faint);margin-top:.5rem;text-align:center}
.art-body h2{font-size:clamp(1.3rem,2vw,1.6rem);font-weight:800;color:var(--navy);margin:2.4rem 0 .7rem;letter-spacing:-.01em}
.art-body h3{font-size:1.12rem;font-weight:700;color:var(--navy);margin:1.5rem 0 .4rem}
.art-body p{font-size:1.05rem;line-height:1.72;color:var(--ink);margin:.8rem 0}
.art-body ul,.art-body ol{font-size:1.05rem;line-height:1.7;color:var(--ink);padding-left:1.3rem;margin:.7rem 0}
.art-body li{margin:.4rem 0}
.art-body a{color:var(--teal);font-weight:600;text-decoration:underline;text-underline-offset:2px}
.art-table{width:100%;border-collapse:collapse;margin:1.3rem 0;font-size:.97rem}
.art-table th,.art-table td{border:1px solid var(--line);padding:.7rem .9rem;text-align:left;vertical-align:top}
.art-table th{background:var(--lblue);color:var(--navy);font-weight:700}
.art-cta{background:linear-gradient(135deg,var(--navy),var(--teal));color:#fff;border-radius:16px;padding:1.8rem 1.9rem;margin:2.2rem 0}
.art-cta h3{color:#fff;font-size:1.3rem;font-weight:800;margin:0 0 .5rem}
.art-cta p{color:#dbe9f1;margin:0 0 1.1rem;line-height:1.55}
.art-cta-row{display:flex;flex-wrap:wrap;gap:.7rem}
.art-cta-btn{display:inline-block;background:#fff;color:var(--navy);font-weight:700;padding:.8rem 1.3rem;border-radius:10px;transition:.15s}
.art-cta-btn:hover{transform:translateY(-2px);box-shadow:0 12px 26px -14px rgba(0,0,0,.5)}
.art-cta-btn2{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.55)}
.art-faq{margin:2.6rem 0 1rem}
.art-faq-q{font-weight:700;color:var(--navy);font-size:1.08rem;margin:1.4rem 0 .25rem}
.art-faq-a{color:var(--ink);line-height:1.72;margin:0}
.art-related{margin-top:2.4rem;border-top:1px solid var(--line);padding-top:1.3rem}
.art-related h2{font-size:1.15rem;font-weight:800;color:var(--navy);margin:0 0 .6rem}
.art-related ul{list-style:none;padding:0;margin:0}
.art-related li{padding:.5rem 0;border-bottom:1px solid var(--line)}
.art-related a{color:var(--navy);font-weight:700}
.art-related a:hover{color:var(--teal)}
/* Hero */
.v5-hero{background:var(--navy);color:#fff}
.v5-hero-in{max-width:1180px;margin:0 auto;display:grid;grid-template-columns:1fr;gap:2rem;padding:3rem 1.5rem 3.4rem}
@media(min-width:960px){.v5-hero-in{grid-template-columns:35fr 65fr;gap:2.5rem;padding:4.5rem 1.5rem 4.8rem;align-items:center}}
.v5-hero-l{max-width:none}
.v5-hero-l h1{color:#fff;font-size:clamp(1.9rem,2.7vw,2.5rem);font-weight:800;line-height:1.1;hyphens:auto;overflow-wrap:break-word}
.v5-hero-l p{color:#bcd3e2;font-size:1.08rem;line-height:1.6;margin:1.2rem 0 0;max-width:42ch}
.v5-hero-r{position:relative}
.h-slides{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:16/10;background:#06283b;box-shadow:0 34px 64px -28px rgba(0,0,0,.6)}
.h-slide{position:absolute;inset:0;opacity:0;transition:opacity .7s ease;pointer-events:none}
.h-slide.on{opacity:1;pointer-events:auto}
.h-slide-img{position:absolute;inset:0;overflow:hidden}
.h-slide-img img{width:100%;height:100%;object-fit:cover;transform-origin:62% 38%;animation:kbzoom 14s ease-in-out infinite alternate}
@keyframes kbzoom{from{transform:scale(1.015)}to{transform:scale(1.11)}}
@media(prefers-reduced-motion:reduce){.h-slide-img img{animation:none}}
.h-slide-c{position:absolute;left:1.1rem;right:1.1rem;bottom:1.1rem;display:flex;flex-direction:column;gap:.4rem;padding:1.25rem 1.45rem;border-radius:14px;background:rgba(255,255,255,.76);backdrop-filter:blur(14px) saturate(125%);-webkit-backdrop-filter:blur(14px) saturate(125%);box-shadow:0 12px 34px -18px rgba(3,49,75,.55)}
.h-slide-cat{font-size:.82rem;font-weight:600;color:var(--teal)}
.h-slide-t{font-size:1.3rem;font-weight:700;color:var(--navy);line-height:1.22;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.h-slide-p{font-size:.9rem;color:var(--muted);line-height:1.45;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.h-slide-go{font-size:.86rem;font-weight:700;color:var(--teal);margin-top:.1rem}
.h-dots{display:flex;gap:.5rem;justify-content:center;margin-top:1.1rem}
.h-dot{width:9px;height:9px;border-radius:50%;background:rgba(255,255,255,.3);cursor:pointer;transition:.2s}
.h-dot.on{background:#fff;width:26px;border-radius:5px}
/* Decisions */
.v5-dec-nav{display:flex;gap:.5rem;flex:0 0 auto}
.v5-dec-arrow{width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:#fff;color:var(--navy);font-size:1.45rem;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s;user-select:none}
.v5-dec-arrow:hover{border-color:var(--teal);color:var(--teal);box-shadow:0 8px 18px -12px rgba(3,49,75,.5)}
.v5-dec-vp{overflow:hidden}
.v5-dec-track{display:flex;gap:1.1rem;align-items:stretch}
.v5-dec-track .v5-dec{flex:0 0 86%}
@media(min-width:560px){.v5-dec-track .v5-dec{flex:0 0 calc((100% - 1.1rem)/2)}}
@media(min-width:980px){.v5-dec-track .v5-dec{flex:0 0 calc((100% - 3.3rem)/4)}}
.v5-dec{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:.5rem;background:#fff;border:1px solid var(--line);border-radius:12px;padding:1.4rem;box-shadow:0 8px 22px -18px rgba(3,49,75,.5);transition:.15s}
.v5-dec:hover{transform:translateY(-3px);box-shadow:0 18px 36px -20px rgba(3,49,75,.45);border-color:#cdd6df}
.v5-dec-cat{font-size:.8rem;font-weight:600;color:var(--teal)}
.v5-dec-q{font-size:1.22rem;font-weight:800;color:var(--navy);line-height:1.18}
.v5-dec-d{font-size:.9rem;color:var(--muted);line-height:1.45;position:relative;z-index:1}
.v5-dec-shape{position:absolute;right:-26px;bottom:-26px;width:74px;height:74px;border-radius:20px;opacity:.10;transform:rotate(18deg)}
/* Season */
.v5-season{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:880px){.v5-season{grid-template-columns:1.5fr 1fr}}
.v5-se-hero{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:.6rem;background:linear-gradient(135deg,var(--navy),var(--teal));color:#fff;border-radius:16px;padding:2rem 2.1rem;min-height:230px;justify-content:flex-end}
.v5-se-tag{font-size:.82rem;font-weight:600;color:#bfe2f1}
.v5-se-h{font-size:clamp(1.4rem,2.2vw,1.85rem);font-weight:800;line-height:1.15;color:#fff}
.v5-se-p{color:#d3e6f1;line-height:1.5;max-width:48ch}
.v5-se-cta{margin-top:.4rem;font-weight:700;color:#fff}
.v5-se-subs{display:flex;flex-direction:column;gap:1.1rem}
.v5-se-sub{display:flex;align-items:center;justify-content:space-between;gap:1rem;background:#fff;border:1px solid var(--line);border-radius:12px;padding:1.15rem 1.3rem;flex:1;transition:.15s}
.v5-se-sub:hover{border-color:var(--teal);box-shadow:0 12px 26px -20px rgba(3,49,75,.5)}
.v5-se-sub-t{font-weight:700;color:var(--navy);line-height:1.3}
.v5-se-sub-go{color:var(--teal);font-weight:800}
/* Rubric */
.v5-rub-sec{margin:5.6rem 0}
.v5-rub-head{border-top:1px solid var(--line);padding-top:2.4rem;margin-bottom:2rem}
.v5-rub-intro{font-size:clamp(1.2rem,1.9vw,1.55rem);font-weight:700;color:var(--navy);max-width:none}
.v5-rub-desc{color:var(--muted);font-size:1rem;line-height:1.5;margin:.45rem 0 0;max-width:62ch}
.v5-rub-grid{display:grid;grid-template-columns:1fr;gap:1.6rem}
@media(min-width:880px){.v5-rub-grid{grid-template-columns:var(--cols,3fr 2fr);gap:2.8rem;align-items:stretch}
 .v5-rub-grid.rev .v5-rub-hero{order:2}.v5-rub-grid.rev .v5-rub-side{order:1}}
/* Lead-Hero (60%): Bild oben, Titel + Text unten */
.v5-rub-hero{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;text-decoration:none;transition:.15s}
.v5-rub-hero:hover{box-shadow:0 18px 42px -26px rgba(3,49,75,.55)}
.v5-rh-img{aspect-ratio:16/9;overflow:hidden;background:var(--lblue)}
.v5-rh-img img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.v5-rub-hero:hover .v5-rh-img img{transform:scale(1.04)}
.v5-rh-b{display:flex;flex-direction:column;gap:.5rem;padding:1.4rem 1.6rem 1.6rem}
.v5-rh-cat{font-size:.82rem;font-weight:600;color:var(--teal)}
.v5-rh-t{font-size:clamp(1.3rem,2vw,1.65rem);font-weight:800;color:var(--navy);line-height:1.22}
.v5-rh-p{color:var(--muted);line-height:1.5}
.v5-rh-go{font-size:.86rem;font-weight:700;color:var(--teal);margin-top:.1rem}
/* Sub-Content rechts (ohne Bild), füllt Rechteck, bündig unten */
.v5-rub-side{display:flex;flex-direction:column;justify-content:space-between;gap:1.4rem}
.v5-sl-list{display:flex;flex-direction:column}
.v5-sl{display:flex;align-items:baseline;justify-content:space-between;gap:1.2rem;padding:.95rem 0;border-bottom:1px solid var(--line);text-decoration:none}
.v5-sl:first-child{padding-top:0}
.v5-sl-t{font-size:1.04rem;font-weight:700;color:var(--navy);line-height:1.3}
.v5-sl:hover .v5-sl-t{color:var(--teal)}
.v5-sl-m{font-size:.78rem;color:var(--faint);white-space:nowrap}
.v5-fl-list{display:flex;flex-direction:column;gap:.6rem}
.v5-fl-row{display:flex;align-items:center;gap:.8rem;padding:.7rem .95rem;border:1px solid var(--line);border-left:3px solid var(--teal);border-radius:10px;background:var(--lblue);text-decoration:none}
.v5-fl-row:hover{box-shadow:0 10px 24px -18px rgba(3,49,75,.5)}
.v5-fl-k{font-size:.74rem;color:var(--muted);min-width:78px}
.v5-fl-n{font-weight:700;color:var(--navy);flex:1}
.v5-fl-go{font-size:.78rem;color:var(--teal);font-weight:700;white-space:nowrap}
.v5-cta{display:block;text-align:center;background:var(--navy);color:#fff;font-weight:700;padding:.9rem 1.2rem;border-radius:10px}
.v5-cta:hover{background:var(--teal)}
/* Mid-Hero (subtiler CTA: Rechner/Check/Analyse mit Bild) */
.v5-mid{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:#fff;text-decoration:none;transition:.15s;margin-top:1.4rem}
.v5-mid:hover{box-shadow:0 18px 40px -24px rgba(3,49,75,.55);transform:translateY(-2px)}
.v5-mid-img{position:relative;aspect-ratio:16/9;overflow:hidden;background:var(--lblue)}
.v5-mid-img img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.v5-mid:hover .v5-mid-img img{transform:scale(1.05)}
.v5-mid-tag{position:absolute;top:.7rem;left:.7rem;font-size:.7rem;font-weight:700;color:#fff;background:var(--teal);padding:.22rem .6rem;border-radius:999px}
.v5-mid-b{display:flex;flex-direction:column;gap:.3rem;padding:1rem 1.2rem 1.15rem}
.v5-mid-t{font-weight:700;color:var(--navy);line-height:1.25;font-size:1.08rem}
.v5-mid-go{font-size:.84rem;font-weight:700;color:var(--teal)}
/* Research */
.v5-research{background:var(--lblue);padding:3rem 1.5rem;margin-top:1rem}
.v5-rs-in{max-width:1180px;margin:0 auto}
.v5-rs-row{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:760px){.v5-rs-row{grid-template-columns:repeat(3,1fr)}}
.v5-rs{display:flex;flex-direction:column;gap:.4rem;background:#fff;border:1px solid #d7e6f2;border-radius:12px;padding:1.1rem;transition:.15s}
.v5-rs:hover{box-shadow:0 16px 34px -22px rgba(3,49,75,.5);transform:translateY(-2px)}
.v5-rs-cov{aspect-ratio:16/10;border-radius:8px;overflow:hidden;background:var(--lblue);margin-bottom:.4rem}
.v5-rs-cov img{width:100%;height:100%;object-fit:cover}
.v5-rs-n{font-size:1.15rem;font-weight:800;color:var(--navy)}
.v5-rs-cad{font-size:.84rem;color:var(--muted)}
.v5-rs-go{font-size:.84rem;font-weight:700;color:var(--teal);margin-top:.3rem}
/* Spezifitäts-Overrides gegen Chrome-Link-Styles */
#ed-root .v5-cta,#ed-root .v5-cta:hover{color:#fff!important}
#ed-root .v5-se-cta,#ed-root .v5-se-tag,#ed-root .v5-se-h,#ed-root .v5-se-p{color:#fff!important}
#ed-root .h-slide-t{color:#03314B!important}#ed-root .h-slide-cat{color:#185E7F!important}#ed-root .h-slide-go{color:#185E7F!important}#ed-root .h-slide-p{color:#5b6b7a!important}
#ed-root .v5-hero-l h1{color:#fff!important}
#ed-root .v5-more,#ed-root .v5-rh-cat,#ed-root .v5-rh-go,#ed-root .v5-fl-go,#ed-root .v5-rs-go,#ed-root .v5-se-sub-go{color:#185E7F!important}
#ed-root .v5-dec-q,#ed-root .v5-rh-t,#ed-root .v5-sl-t,#ed-root .v5-mid-t,#ed-root .v5-rs-n,#ed-root .v5-se-sub-t,#ed-root .v5-rub-intro,#ed-root .v5 h2{color:#03314B!important}
#ed-root .v5-mid-go{color:#185E7F!important}#ed-root .v5-mid-tag{color:#fff!important}
#ed-root .v5-rh-p,#ed-root .v5-sl-m,#ed-root .v5-fl-k{color:#5b6b7a!important}
#ed-root .v5-dec-cat{color:#185E7F!important}
#ed-root .v5-funnel-t{color:#03314B!important}#ed-root .v5-funnel-d{color:#5b6b7a!important}#ed-root .v5-funnel-go{color:#185E7F!important}
#ed-root .v5-funnel-n{color:#e3ebf2!important}#ed-root .v5-funnel:hover .v5-funnel-n{color:#185E7F!important}
#ed-root .v5-fn-h{color:#fff!important}#ed-root .v5-fn-sub{color:#bcd3e2!important}
#ed-root .v5-phead h1{color:#fff!important}#ed-root .v5-phead p{color:#bcd3e2!important}#ed-root .v5-eyebrow{color:#7fb3cc!important}#ed-root .v5-back{color:#185E7F!important}#ed-root .v5-lead{color:#1c2b36!important}
#ed-root .v5-dec-fresh{color:#8b9aa8!important}
#ed-root .art-body a,#ed-root .art-bc a,#ed-root .art-related a{color:#185E7F!important}
#ed-root .art-body p,#ed-root .art-body li,#ed-root .art-faq-a{color:#1c2b36!important}
#ed-root .art-body h2,#ed-root .art-body h3,#ed-root .art-lead,#ed-root .art-faq-q,#ed-root .art-related a,#ed-root .art-related h2{color:#03314B!important}
#ed-root .art-cta h3{color:#fff!important}#ed-root .art-cta p{color:#dbe9f1!important}#ed-root .art-cta-btn{color:#03314B!important}#ed-root .art-cta-btn2{color:#fff!important}#ed-root .art-table th{color:#03314B!important}
/* === frontend-design polish (rein visuell) === */
html{scroll-behavior:smooth}
.v5 h1,.v5 h2,.v5 h3{letter-spacing:-.022em;text-wrap:balance}
.v5 ::selection{background:rgba(24,94,127,.18);color:var(--navy)}
.v5 a:focus-visible,.v5 [role="button"]:focus-visible{outline:2px solid var(--teal);outline-offset:3px;border-radius:6px}
/* Wärmere Tiefe statt flacher Flächen */
.v5-hero{position:relative;overflow:hidden}
.v5-hero::before{content:"";position:absolute;inset:0;background:radial-gradient(120% 90% at 88% -10%,rgba(24,94,127,.55),transparent 60%),radial-gradient(80% 70% at -10% 110%,rgba(24,94,127,.32),transparent 55%);pointer-events:none}
.v5-hero-in{position:relative;z-index:1}
.v5-dec,.v5-rub-hero,.v5-mid,.v5-se-sub,.v5-rs{transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s ease,border-color .25s ease}
.v5-rub-hero:hover{transform:translateY(-3px)}
.v5-rh-go,.v5-mid-go{display:inline-flex;align-items:center;gap:.3em}
.v5-rh-go::after,.v5-mid-go::after{content:"\\2192";transition:transform .25s ease}
.v5-rub-hero:hover .v5-rh-go::after,.v5-mid:hover .v5-mid-go::after{transform:translateX(4px)}
.v5-sl{position:relative;transition:padding-left .2s ease}
.v5-sl::before{content:"";position:absolute;left:-.85rem;top:50%;width:3px;height:0;background:var(--teal);border-radius:2px;transform:translateY(-50%);transition:height .25s ease}
.v5-sl:hover{padding-left:.85rem}
.v5-sl:hover::before{height:62%}
/* Page-Load: gestaffelte Hero-Reveal */
@media(prefers-reduced-motion:no-preference){
 @keyframes v5up{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:none}}
 .v5-hero-l h1{animation:v5up .7s both cubic-bezier(.2,.7,.2,1)}
 .v5-hero-l p{animation:v5up .7s .12s both cubic-bezier(.2,.7,.2,1)}
 .v5-hero-r{animation:v5up .8s .22s both cubic-bezier(.2,.7,.2,1)}
 /* Scroll-Reveal (JS fügt .v5-reveal hinzu; ohne JS bleibt alles sichtbar) */
 .v5-reveal{opacity:0;transform:translateY(22px)}
 .v5-reveal.r-in{opacity:1;transform:none;transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.2,1)}
}
</style>'''
JS='''<script id="smzh-v5-js">
(function(){function r(f){if(document.readyState!=='loading')f();else document.addEventListener('DOMContentLoaded',f);}
r(function(){document.querySelectorAll('.v5-car').forEach(function(c){
var sl=c.querySelectorAll('.h-slide'),dt=c.querySelectorAll('.h-dot'),i=0,n=sl.length,t=null;if(n<2)return;
function go(k){i=(k+n)%n;sl.forEach(function(e,j){e.classList.toggle('on',j===i)});dt.forEach(function(d,j){d.classList.toggle('on',j===i)})}
function au(){t=setInterval(function(){go(i+1)},5000)}function rs(){clearInterval(t);au()}
dt.forEach(function(d,j){d.addEventListener('click',function(){go(j);rs()});d.addEventListener('keydown',function(e){if(e.key==='Enter'){go(j);rs()}})});
c.addEventListener('mouseenter',function(){clearInterval(t)});c.addEventListener('mouseleave',au);go(0);au();});
document.querySelectorAll('.v5-dec-sec').forEach(function(sec){
var track=sec.querySelector('.v5-dec-track'),prev=sec.querySelector('.v5-dec-prev'),next=sec.querySelector('.v5-dec-next');
if(!track||track.children.length<2)return;var busy=false;
function step(){var c=track.children[0],cs=getComputedStyle(track),g=parseFloat(cs.columnGap||cs.gap||0)||0;return c.getBoundingClientRect().width+g;}
function fwd(){if(busy)return;busy=true;var s=step();track.style.transition='transform .45s ease';track.style.transform='translateX(-'+s+'px)';
 var d=function(e){if(e.target!==track||e.propertyName!=='transform')return;track.style.transition='none';track.appendChild(track.firstElementChild);track.style.transform='translateX(0)';track.removeEventListener('transitionend',d);busy=false;};
 track.addEventListener('transitionend',d);}
function back(){if(busy)return;busy=true;var s=step();track.style.transition='none';track.insertBefore(track.lastElementChild,track.firstElementChild);track.style.transform='translateX(-'+s+'px)';
 requestAnimationFrame(function(){track.style.transition='transform .45s ease';track.style.transform='translateX(0)';});
 setTimeout(function(){busy=false;},480);}
if(next){next.addEventListener('click',fwd);next.addEventListener('keydown',function(e){if(e.key==='Enter')fwd();});}
if(prev){prev.addEventListener('click',back);prev.addEventListener('keydown',function(e){if(e.key==='Enter')back();});}
});
/* Scroll-Reveal: rein visuell, ohne IO/Reduced-Motion bleibt alles sichtbar */
try{var rm=window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches;
if('IntersectionObserver' in window && !rm){
 var els=document.querySelectorAll('.v5-wrap .v5-sec');
 els.forEach(function(el){el.classList.add('v5-reveal');});
 var io=new IntersectionObserver(function(ents){ents.forEach(function(en){if(en.isIntersecting){en.target.classList.add('r-in');io.unobserve(en.target);}});},{rootMargin:'0px 0px -8% 0px',threshold:.08});
 els.forEach(function(el){io.observe(el);});
}}catch(e){}
});})();
</script>'''

# Schluss-CTA-Umtextung (nur Beschriftung; Links/Routing/Layout unverändert)
CTA_COPY=[
 ('Nutzen Sie unseren 360° Check-Up','Wissen ist der Einstieg. Entscheidend ist, was es für Ihre Situation bedeutet.'),
 ('Unser 360° Check-Up ist eine Analyse Ihrer aktuellen Ausgangslage. Mit ihr finden wir heraus, wie Ihre individuelle Situation optimiert werden könnte.',
  'smzh hilft, Marktinformationen, Vorsorge, Eigenheim, Steuern und Vermögen in eine konkrete Finanzentscheidung zu übersetzen.'),
 ('<span>Unverbindlichen Termin vereinbaren</span>','<span>Nächsten Schritt klären</span>'),
]

def balanced_div_end(s,start):
    depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>',s[start:]):
        depth+=1 if m.group(1)=='' else -1
        if depth==0: return start+m.end()
    return -1

def build_page(slug_parts, inner, title, meta=None):
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*"',html)
    o=html.index('>',m.start())+1; c=balanced_div_end(html,m.start())
    before=html[:o]; after=html[c-6:]
    if 'id="smzh-v5-css"' not in before: before=before.replace('</head>',FONTS+CSS+'</head>',1)
    before=re.sub(r'(<div class="content-hub[^"]*")',r'\1 id="ed-root"',before,count=1)
    if 'id="smzh-v5-js"' not in after: after=after.replace('</body>',JS+'</body>',1)
    # Schluss-CTA (360°-Band im Chrome) konsumentenorientiert umtexten – seitenscharf, Routing unverändert
    for old,new in CTA_COPY:
        after=after.replace(old,new,1)
    # --- SEO-Head: Description, Canonical, Open Graph/Twitter, JSON-LD (verhindert Duplicate-Tags des geklonten Chrome) ---
    meta=meta or {}
    before=re.sub(r'<meta property="og:title"[^>]*>',f'<meta property="og:title" content="{esc(title)}">',before,count=1)
    before=re.sub(r'<meta name="twitter:title"[^>]*>',f'<meta name="twitter:title" content="{esc(title)}">',before,count=1)
    desc=meta.get('desc')
    if desc:
        before=re.sub(r'<meta name="description"[^>]*>',f'<meta name="description" content="{esc(desc)}">',before,count=1)
        before=re.sub(r'<meta property="og:description"[^>]*>',f'<meta property="og:description" content="{esc(desc)}">',before,count=1)
        before=re.sub(r'<meta name="twitter:description"[^>]*>',f'<meta name="twitter:description" content="{esc(desc)}">',before,count=1)
    url=BASE+'/'+'/'.join(slug_parts)+'/'
    head_add=f'<link rel="canonical" href="{url}">'
    if '<meta property="og:url"' in before:
        before=re.sub(r'<meta property="og:url"[^>]*>',f'<meta property="og:url" content="{url}">',before,count=1)
    else:
        head_add+=f'<meta property="og:url" content="{url}">'
    for blob in meta.get('jsonld',[]):
        head_add+='<script type="application/ld+json">'+json.dumps(blob,ensure_ascii=False)+'</script>'
    before=before.replace('</head>',head_add+'</head>',1)
    full=before+inner+after
    full=re.sub(r'<title>.*?</title>',f'<title>{esc(title)}</title>',full,count=1,flags=re.S)
    d=os.path.join(SMZH,*slug_parts); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)

def sl_row(t,h): return f'<a class="v5-sl" href="{link(h)}"><span class="v5-sl-t">{esc(t)}</span><span class="v5-sl-m">→</span></a>'

def category_inner(eyebrow,title,intro,body):
    return ('<div class="v5"><section class="v5-phead"><div class="v5-phead-in">'
            f'<p class="v5-eyebrow">{esc(eyebrow)}</p><h1>{esc(title)}</h1><p>{esc(intro)}</p></div></section>'
            f'<div class="v5-wrap">{body}'
            f'<section class="v5-sec v5-backsec"><a class="v5-back" href="{link("/de/smzhub/")}">← Zurück zum smzhHub</a></section>'
            '</div></div>')

def immobilienanlagen_inner():
    arts=[p for p in ['/de/artikel/zuercher-wohnungsinitiativen/','/de/artikel/eigenmietwert-sanierung-bundesrat-2029/','/de/artikel/abstimmung-keine-10-millionen-schweiz/'] if item(p)]
    rows_html=sl_row('Immobilien-Outlook – quartalsweises Research','/de/smzhub-serie-immobilien-outlook/')
    rows_html+=''.join(sl_row(item(p)['title'],p) for p in arts)
    body=('<section class="v5-sec"><p class="v5-lead">Immobilien als Kapitalanlage folgen anderen Regeln als das selbstbewohnte '
          'Eigenheim: Rendite, Leerstandsrisiko, Regulierung und Finanzierung entscheiden über den Erfolg. Dieser Bereich '
          'ordnet Renditeobjekte und indirekte Immobilienanlagen für Anlegerinnen und Anleger ein.</p></section>'
          f'<section class="v5-sec"><div class="v5-head"><div><h2>Relevante Einschätzungen</h2></div></div><div class="v5-sl-list">{rows_html}</div></section>')
    return category_inner('smzhHub · Themenwelt','Immobilienanlagen',
        'Renditeobjekte und indirekte Immobilienanlagen – eingeordnet für Ihre Anlageentscheidung.',body)

def horizon_inner():
    body=('<section class="v5-sec"><p class="v5-lead">smzh horizon bündelt den längeren Blick: makroökonomische Trends, '
          'strukturelle Entwicklungen und Ausblicke, die einzelne Themenwelten miteinander verbinden.</p></section>'
          '<section class="v5-sec"><div class="v5-note">Dieser Bereich wird derzeit aufgebaut. Bis dahin finden Sie '
          f'aktuelle Einschätzungen und Publikationen im <a class="v5-back" href="{link("/de/smzhub-research/")}">Research-Bereich</a>.</div></section>')
    return category_inner('smzhHub · Themenwelt','smzh horizon',
        'Perspektiven, Trends und Ausblick von smzh.',body)

ORG={'@type':'Organization','name':'smzh','url':'https://smzh.ch','logo':'https://smzh.ch/favicon.ico'}

def main():
    home_meta={'desc':'smzhHub ordnet Märkte, Eigenheim, Vorsorge und Steuern so ein, dass Sie Ihre nächste Finanzentscheidung 2026 sicherer treffen. Einordnungen, Ratgeber und Research.',
        'jsonld':[{'@context':'https://schema.org','@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/','publisher':ORG}]}
    build_page(('de','smzhub'),home_inner(),'smzhHub – Klarheit für Ihre Finanzentscheidungen',home_meta)
    build_page(('de','smzhub-immobilienanlagen'),immobilienanlagen_inner(),'Immobilienanlagen einordnen | smzhHub',
        {'desc':'Renditeobjekte und indirekte Immobilienanlagen verständlich eingeordnet: Rendite, Risiken, Regulierung und Finanzierung für Ihre Anlageentscheidung.',
         'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':'Immobilienanlagen','isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]})
    build_page(('de','smzhub-horizon'),horizon_inner(),'smzh horizon – Trends & Ausblick | smzhHub',
        {'desc':'smzh horizon bündelt den längeren Blick: makroökonomische Trends, strukturelle Entwicklungen und Ausblicke, die die Themenwelten des smzhHub verbinden.',
         'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':'smzh horizon','isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]})
    print('OK V5: Landing Page + Themenwelten-Seiten (Immobilienanlagen, smzh horizon) geschrieben.')

if __name__=='__main__':
    main()
