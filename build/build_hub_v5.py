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
def fquarter(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"Q{(d.month-1)//3+1} {d.year}"
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
def upload(f): return P_+'../cms.smzh.ch/uploads/'+f  # build-konsistenter PDF-Pfad (-> ../../../cms.smzh.ch/uploads/<file>)
def pdf_of(r):
    """Bevorzugt PDF mit _DE_-Marker, sonst erste; nur wenn die Datei real unter site/cms.smzh.ch/uploads/ liegt. Sonst None (Fallback Lese-Link)."""
    pdfs=r.get('pdfs') or []
    cand=next((f for f in pdfs if '_DE_' in f), pdfs[0] if pdfs else None)
    if cand and os.path.exists(os.path.join(SMZH,'..','cms.smzh.ch','uploads',cand)): return cand
    return None
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
    # Blog-CTA-Regel (PAGE_SCHEMA §8.2): Saison-Block als reiner Lese-Block fuehren – der werbliche
    # Conversion-CTA (cl) wird nicht ausgegeben; Hero und Sub-Links bleiben reine Lese-Links ("Beitrag lesen").
    # (Wird in home_inner derzeit nicht eingebunden; bei kuenftiger Nutzung §8-konform.)
    t,teaser,_cl,cp=SEASON_HERO
    subs=''
    for st,sp in SEASON_SUBS:
        subs+=f'<a class="v5-se-sub" href="{link(sp)}"><span class="v5-se-sub-t">{esc(st)}</span><span class="v5-se-sub-go">→</span></a>'
    hero=(f'<a class="v5-se-hero" href="{link(cp)}"><span class="v5-se-tag">Aktuell relevant</span>'
          f'<span class="v5-se-h">{esc(t)}</span><span class="v5-se-p">{esc(teaser)}</span>'
          f'<span class="v5-se-cta">Beitrag lesen →</span></a>')
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
    leadp=arts[0]
    lead=item(leadp); im=img_of(leadp,1080)
    rm=rmin(leadp); goline=(rm+' · ' if rm else '')+'Beitrag lesen'
    hero=(f'<a class="v5-rub-hero" href="{link(leadp)}"><span class="v5-rh-img">{imgt(im)}</span>'
          f'<span class="v5-rh-b"><span class="v5-rh-cat">{esc(rb["label"])}</span>'
          f'<span class="v5-rh-t">{esc(lead["title"])}</span>'
          f'<span class="v5-rh-p">{esc(teaser(leadp,170))}</span>'
          f'<span class="v5-rh-go">{esc(goline)}</span></span></a>')
    # Blog-CTA-Regel (PAGE_SCHEMA §8.2/§8.4): der Conversion-Tool-Slot (v5-mid mit Aktions-Label)
    # sass INNERHALB der redaktionellen Lese-Rubrik und wird hier entfernt. Das Rail traegt nur noch
    # reine Lese-Links; der vierte Beitrag (arts[4]) ersetzt den Tool-Slot als zusaetzlicher Lese-Teaser.
    leadsubs=arts[1:5]
    sub_html=''.join(f'<a class="v5-sl" href="{link(p)}"><span class="v5-sl-t">{esc(item(p)["title"])}</span>'
                     +(f'<span class="v5-sl-m">{esc(rmin(p))}</span>' if rmin(p) else '')+'</a>' for p in leadsubs)
    side=f'<div class="v5-rub-side"><div class="v5-sl-list">{sub_html}</div></div>'
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
.v5-eyebrow{font-size:.8rem;font-weight:700;letter-spacing:.01em;color:#7fb3cc;margin:0 0 .6rem}
.v5-phead h1{color:#fff;font-size:clamp(1.9rem,2.7vw,2.5rem);font-weight:800;line-height:1.12}
.v5-phead-cta{display:inline-flex;align-items:center;gap:.55em;font-weight:700;font-size:.95rem;line-height:1;color:var(--navy);background:#fff;padding:.85rem 1.4rem;border-radius:999px;transition:transform .2s cubic-bezier(.2,.7,.3,1),box-shadow .2s}
.v5-phead-cta .ar{transition:transform .22s cubic-bezier(.2,.7,.3,1)}
.v5-phead-cta:hover{transform:translateY(-2px);box-shadow:0 14px 28px -14px rgba(0,0,0,.5)}
.v5-phead-cta:hover .ar{transform:translateX(4px)}
.v5-phead p{color:#bcd3e2;font-size:1.08rem;line-height:1.6;margin:1rem 0 0;max-width:60ch}
.v5-lead{font-size:1.1rem;line-height:1.65;color:var(--ink);max-width:64ch}
.v5-note{background:var(--lblue);border:1px solid #d7e6f2;border-radius:12px;padding:1.2rem 1.4rem;color:var(--ink);line-height:1.6}
.v5-back{display:inline-flex;align-items:center;gap:.4em;font-weight:700;color:var(--teal)}
.v5-backsec{margin-top:3rem}
/* Entscheidungs-Karten: Aktualitäts-Chip */
.v5-dec-fresh{margin-top:auto;padding-top:.7rem;font-size:.72rem;font-weight:700;letter-spacing:.01em;color:var(--faint);display:inline-flex;align-items:center;gap:.45em}
.v5-dec-fresh::before{content:"";width:6px;height:6px;border-radius:50%;background:#28a745;box-shadow:0 0 0 3px rgba(40,167,69,.15)}
/* Ratgeber-Artikel (Lead-Gen + SEO) */
.art-bc{font-size:.8rem;color:var(--faint);margin:1.2rem 0 .2rem}
.art-bc a{color:var(--teal);font-weight:600}
.art-body{max-width:760px;margin:0 auto;padding-bottom:1rem}
.art-lead{font-size:1.18rem;line-height:1.65;color:var(--navy);font-weight:500;margin:1.4rem 0 1.2rem}
.art-fig{margin:1.7rem 0 2rem}
.art-figw{position:relative;border-radius:18px;overflow:hidden;background:var(--lblue);box-shadow:0 26px 54px -30px rgba(3,49,75,.6)}
.art-figw::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(3,49,75,0) 52%,rgba(3,49,75,.5));pointer-events:none}
.art-fig img{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;height:auto}
.art-fig-tag{position:absolute;z-index:2;left:15px;top:15px;font-size:.68rem;font-weight:700;letter-spacing:.01em;color:#fff;background:rgba(3,49,75,.5);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.28);padding:.42rem .75rem;border-radius:999px}
.art-fig figcaption{font-size:.82rem;color:var(--faint);margin:.7rem 0 0;padding-left:.9rem;border-left:2px solid var(--teal);line-height:1.45}
.art-body h2{font-size:clamp(1.3rem,2vw,1.6rem);font-weight:800;color:var(--navy);margin:2.4rem 0 .7rem;letter-spacing:-.01em}
.art-body h3{font-size:1.12rem;font-weight:700;color:var(--navy);margin:1.5rem 0 .4rem}
.art-body p{font-size:1.05rem;line-height:1.72;color:var(--ink);margin:.8rem 0}
.art-body ul,.art-body ol{font-size:1.05rem;line-height:1.7;color:var(--ink);padding-left:1.3rem;margin:.7rem 0}
.art-body li{margin:.4rem 0}
.art-body a{color:var(--teal);font-weight:600;text-decoration:underline;text-underline-offset:2px}
.art-table{width:100%;border-collapse:collapse;margin:1.3rem 0;font-size:.97rem}
.art-table th,.art-table td{border:1px solid var(--line);padding:.7rem .9rem;text-align:left;vertical-align:top}
.art-table th{background:var(--lblue);color:var(--navy);font-weight:700}
.art-cta{position:relative;overflow:hidden;color:#fff;border-radius:20px;padding:2.1rem 2.1rem 1.8rem;margin:2.6rem 0;background:linear-gradient(152deg,#03314B 0%,#0a3f5d 50%,#16566f 128%);box-shadow:0 32px 64px -36px rgba(3,49,75,.9)}
.art-cta::before{content:"";position:absolute;right:-70px;top:-90px;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(126,200,230,.32),rgba(126,200,230,0) 70%);pointer-events:none}
.art-cta::after{content:"";position:absolute;left:-50px;bottom:-100px;width:230px;height:230px;border-radius:50%;background:radial-gradient(circle,rgba(24,94,127,.55),rgba(24,94,127,0) 72%);pointer-events:none}
.art-cta>*{position:relative;z-index:1}
.art-cta-eyebrow{display:inline-flex;align-items:center;gap:.55em;font-size:.71rem;font-weight:700;letter-spacing:.02em;color:#a6d2e6;margin:0 0 .8rem}
.art-cta-eyebrow::before{content:"";width:7px;height:7px;border-radius:50%;background:#38c172;box-shadow:0 0 0 4px rgba(56,193,114,.2)}
.art-cta h3{color:#fff;font-size:clamp(1.3rem,2.2vw,1.55rem);font-weight:800;letter-spacing:-.01em;line-height:1.18;margin:0 0 .55rem}
.art-cta p{color:#cce1ed;margin:0 0 1.35rem;line-height:1.6;max-width:54ch}
.art-cta-row{display:flex;flex-wrap:wrap;gap:.8rem;align-items:center}
.art-cta-btn{display:inline-flex!important;align-items:center;gap:.55em;font-weight:700;font-size:1rem;line-height:1;padding:.95rem 1.55rem;border-radius:999px;text-decoration:none!important;transition:transform .2s cubic-bezier(.2,.7,.3,1),box-shadow .2s,background .2s,border-color .2s}
.art-cta-btn .ar{transition:transform .22s cubic-bezier(.2,.7,.3,1)}
.art-cta-btn:hover .ar{transform:translateX(4px)}
.art-cta-btn1{background:linear-gradient(135deg,#1f93c4,#136f97);color:#fff;box-shadow:0 16px 32px -16px rgba(19,111,151,.9)}
.art-cta-btn1:hover{transform:translateY(-2px);box-shadow:0 22px 42px -16px rgba(38,150,190,.95)}
.art-cta-btn2{background:rgba(255,255,255,.07);color:#fff;border:1px solid rgba(255,255,255,.42)}
.art-cta-btn2:hover{background:rgba(255,255,255,.15);border-color:rgba(255,255,255,.72);transform:translateY(-2px)}
.art-cta-trust{display:flex;flex-wrap:wrap;gap:.35rem 1.2rem;margin:1.15rem 0 0;font-size:.79rem;color:#9ec3d5}
.art-cta-trust span{display:inline-flex;align-items:center;gap:.4em}
.art-cta-trust span::before{content:"✓";color:#38c172;font-weight:800}
.art-faq{margin:2.6rem 0 1rem}
.art-faq-q{font-weight:700;color:var(--navy);font-size:1.08rem;margin:1.4rem 0 .25rem}
.art-faq-a{color:var(--ink);line-height:1.72;margin:0}
.art-related{margin:3.1rem 0 1rem;border-top:1px solid var(--line);padding-top:1.9rem}
.art-related-eyebrow{font-size:.74rem;font-weight:700;letter-spacing:.02em;color:var(--teal);margin:0 0 .35rem}
.art-related h2{font-size:1.3rem;font-weight:800;color:var(--navy);margin:0;letter-spacing:-.01em}
.art-rel-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:.9rem;margin-top:1.3rem}
.art-rel-card{position:relative;display:flex;flex-direction:column;gap:.55rem;min-height:150px;padding:1.15rem 1.2rem 1.2rem;border:1px solid var(--line);border-radius:15px;background:#fff;overflow:hidden;text-decoration:none!important;transition:transform .22s cubic-bezier(.2,.7,.3,1),box-shadow .22s,border-color .22s}
.art-rel-card::before{content:"";position:absolute;left:0;top:0;height:100%;width:3px;background:var(--teal);transform:scaleY(0);transform-origin:top;transition:transform .26s}
.art-rel-card:hover{transform:translateY(-3px);border-color:#cfe0ec;box-shadow:0 20px 38px -24px rgba(3,49,75,.5)}
.art-rel-card:hover::before{transform:scaleY(1)}
.art-rel-k{font-size:.69rem;font-weight:700;letter-spacing:.02em;color:var(--faint)}
.art-rel-t{font-size:1.02rem;font-weight:700;color:var(--navy);line-height:1.32}
.art-rel-go{margin-top:auto;font-size:.83rem;font-weight:700;color:var(--teal);display:inline-flex;align-items:center;gap:.4em}
.art-rel-go .ar{transition:transform .22s}
.art-rel-card:hover .art-rel-go .ar{transform:translateX(4px)}
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
/* Flagship-Research-Anker (gleichwertiges Premium-Paar; Spec: COMPONENT_LIBRARY.html) */
.v5-flagship{margin:5.6rem 0}
.v5-fa-grid{display:grid;grid-template-columns:1fr;gap:1.6rem}
@media(min-width:880px){.v5-fa-grid{grid-template-columns:1fr 1fr;gap:2rem}}
.v5-fa{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:18px;overflow:hidden;box-shadow:0 18px 44px -26px rgba(3,49,75,.55);transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s ease,border-color .25s ease}
.v5-fa:hover{transform:translateY(-4px);box-shadow:0 30px 60px -28px rgba(3,49,75,.55);border-color:#cdd6df}
.v5-fa-cov{position:relative;aspect-ratio:16/9;overflow:hidden;background:var(--lblue)}
.v5-fa-cov img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.v5-fa:hover .v5-fa-cov img{transform:scale(1.04)}
.v5-fa-badge{position:absolute;left:14px;top:14px;font-size:.7rem;font-weight:700;letter-spacing:.02em;color:#fff;background:rgba(3,49,75,.55);-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.28);padding:.4rem .75rem;border-radius:999px}
.v5-fa-body{display:flex;flex-direction:column;gap:.55rem;padding:1.5rem 1.6rem 1.3rem;flex:1}
.v5-fa-title{font-size:clamp(1.3rem,2vw,1.6rem);font-weight:800;color:var(--navy);line-height:1.2}
.v5-fa-sub{font-size:.95rem;color:var(--muted);line-height:1.5;margin:0}
.v5-fa-latest{display:flex;flex-direction:column;gap:.2rem;margin-top:.5rem;padding-top:.9rem;border-top:1px solid var(--line)}
.v5-fa-date{font-size:.74rem;font-weight:700;letter-spacing:.02em;color:var(--faint)}
.v5-fa-latest-t{font-size:1.04rem;font-weight:700;color:var(--navy);line-height:1.3}
.v5-fa-latest-t:hover{color:var(--teal)}
.v5-fa-foot{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;margin-top:auto;padding:1.1rem 1.6rem 1.5rem;background:var(--navy)}
.v5-fa-cta{display:inline-flex;align-items:center;gap:.55em;font-weight:700;font-size:.95rem;line-height:1;color:var(--navy);background:#fff;padding:.8rem 1.3rem;border-radius:999px;transition:transform .2s cubic-bezier(.2,.7,.3,1),box-shadow .2s}
.v5-fa-cta .ar{transition:transform .22s cubic-bezier(.2,.7,.3,1)}
.v5-fa-cta:hover{transform:translateY(-2px);box-shadow:0 14px 28px -14px rgba(0,0,0,.5)}
.v5-fa-cta:hover .ar{transform:translateX(4px)}
.v5-fa-archive{font-size:.86rem;font-weight:700;color:#9fd0ee;display:inline-flex;align-items:center;gap:.35em}
.v5-fa-archive:hover{color:#fff}
/* High-End-Variante Outlook-Segment (Contract §6.3) – nur Bestands-Tokens: Navy-Flaeche + Hellwerte exakt wie .v5-phead */
.v5-fa--feature{background:var(--navy);border-color:transparent}
.v5-fa--feature .v5-fa-title{color:#fff}
.v5-fa--feature .v5-fa-sub{color:#bcd3e2}
.v5-fa--feature .v5-fa-latest{border-top-color:rgba(255,255,255,.16)}
.v5-fa--feature .v5-fa-date{color:#9ec3d5}
.v5-fa--feature .v5-fa-latest-t{color:#fff}
.v5-fa--feature .v5-fa-latest-t:hover{color:#9fd0ee}
.v5-fa--feature .v5-fa-foot{background:transparent;padding-top:.2rem}
/* Zins-Verlaufs-Chart (Contract §7) – statisches Inline-SVG, EINE Datenreihe, keine JS-Lib */
.v5-ratechart{margin:5rem 0}
.v5-rc-fig{margin:1.6rem 0 0;position:relative;border-radius:18px;overflow:hidden;background:var(--lblue);box-shadow:0 26px 54px -30px rgba(3,49,75,.6)}
.v5-rc-svg{display:block;width:100%;height:auto;background:#fff}
.v5-rc-area{fill:var(--lblue);stroke:none}
.v5-rc-line{fill:none;stroke:var(--teal);stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}
.v5-rc-axis{stroke:var(--line);stroke-width:1}
.v5-rc-grid{stroke:var(--line);stroke-width:1;stroke-dasharray:3 4}
.v5-rc-dot{fill:var(--teal)}
.v5-rc-lbl{fill:var(--faint);font-family:'Plus Jakarta Sans',sans-serif;font-size:11px;font-weight:600}
.v5-rc-lbl.v5-rc-lbl-y{text-anchor:end}
.v5-rc-lbl.v5-rc-lbl-x{text-anchor:middle}
.v5-rc-fig figcaption{font-size:.82rem;color:var(--faint);margin:0;padding:.7rem .9rem .9rem;border-left:2px solid var(--teal);line-height:1.45;background:#fff}
/* LP: Download-Block der neuesten Ausgabe (Contract §8.2) */
.v5-dl{display:flex;flex-direction:column;gap:.5rem;background:#fff;border:1px solid var(--line);border-radius:16px;padding:1.5rem 1.6rem 1.6rem;box-shadow:0 8px 22px -18px rgba(3,49,75,.5);max-width:680px}
.v5-dl-meta{font-size:.74rem;font-weight:700;letter-spacing:.02em;color:var(--faint)}
.v5-dl-t{font-size:1.22rem;font-weight:800;color:var(--navy);line-height:1.25}
.v5-dl-p{font-size:.95rem;color:var(--muted);line-height:1.55;margin:0}
.v5-dl-act{margin-top:.7rem}
.v5-dl-btn{display:inline-flex;align-items:center;gap:.55em;font-weight:700;font-size:.95rem;line-height:1;color:#fff;background:var(--navy);padding:.85rem 1.4rem;border-radius:999px;transition:transform .2s cubic-bezier(.2,.7,.3,1),box-shadow .2s}
.v5-dl-btn .ar{transition:transform .22s cubic-bezier(.2,.7,.3,1)}
.v5-dl-btn:hover{transform:translateY(-2px);box-shadow:0 16px 30px -16px rgba(3,49,75,.6)}
.v5-dl-btn:hover .ar{transform:translateY(2px)}
.v5-dl-read{display:inline-flex;align-items:center;gap:.4em;font-weight:700;font-size:.95rem;color:var(--teal)}
.v5-dl-read .ar{transition:transform .22s}
.v5-dl-read:hover .ar{transform:translateX(4px)}
/* LP: Archiv-Liste (Contract §8.3) – nutzt Bestandskarten .v5-sl/.v5-rs */
.v5-arch{max-width:760px}
.v5-arch .v5-sl-list{margin-top:.4rem}
.v5-arch-all{display:inline-flex;align-items:center;gap:.4em;margin-top:1.1rem;font-weight:700;font-size:.9rem;color:var(--teal)}
.v5-arch-all .ar{transition:transform .22s}
.v5-arch-all:hover .ar{transform:translateX(4px)}
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
#ed-root .v5-phead h1{color:#fff!important}#ed-root .v5-phead p{color:#bcd3e2!important}#ed-root .v5-eyebrow{color:#7fb3cc!important}#ed-root .v5-back{color:#185E7F!important}#ed-root .v5-lead{color:#1c2b36!important}#ed-root .v5-phead-cta{color:#03314B!important}
#ed-root .v5-dec-fresh{color:#8b9aa8!important}
#ed-root .v5-fa-title,#ed-root .v5-fa-latest-t{color:#03314B!important}#ed-root .v5-fa-sub{color:#5b6b7a!important}#ed-root .v5-fa-date{color:#8b9aa8!important}#ed-root .v5-fa-cta{color:#03314B!important}#ed-root .v5-fa-archive{color:#9fd0ee!important}#ed-root .v5-fa-badge{color:#fff!important}
#ed-root .v5-fa--feature .v5-fa-title,#ed-root .v5-fa--feature .v5-fa-latest-t{color:#fff!important}#ed-root .v5-fa--feature .v5-fa-sub{color:#bcd3e2!important}#ed-root .v5-fa--feature .v5-fa-date{color:#9ec3d5!important}
#ed-root .v5-dl-t{color:#03314B!important}#ed-root .v5-dl-p{color:#5b6b7a!important}#ed-root .v5-dl-meta{color:#8b9aa8!important}#ed-root .v5-dl-btn{color:#fff!important}#ed-root .v5-dl-read{color:#185E7F!important}
#ed-root .v5-arch-all{color:#185E7F!important}
#ed-root .art-body a,#ed-root .art-bc a,#ed-root .art-related a{color:#185E7F!important}
#ed-root .art-body p,#ed-root .art-body li,#ed-root .art-faq-a{color:#1c2b36!important}
#ed-root .art-body h2,#ed-root .art-body h3,#ed-root .art-lead,#ed-root .art-faq-q,#ed-root .art-related a,#ed-root .art-related h2{color:#03314B!important}
#ed-root .art-cta h3{color:#fff!important}#ed-root .art-cta p{color:#cce1ed!important}#ed-root .art-cta-eyebrow{color:#a6d2e6!important}#ed-root .art-cta a.art-cta-btn1,#ed-root .art-cta a.art-cta-btn1 .ar{color:#fff!important}#ed-root .art-cta a.art-cta-btn2,#ed-root .art-cta a.art-cta-btn2 .ar{color:#fff!important}#ed-root .art-cta-trust{color:#9ec3d5!important}#ed-root .art-rel-k{color:#8b9aa8!important}#ed-root .art-rel-t{color:#03314B!important}#ed-root .art-rel-go{color:#185E7F!important}#ed-root .art-table th{color:#03314B!important}
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
/* Mobile: Touch-Ziele der Pillen-CTAs auf >=44px (vertikales Padding) */
@media(max-width:600px){.v5-fa-cta,.v5-phead-cta{padding-top:1.05rem;padding-bottom:1.05rem}}
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
    img=meta.get('image')
    if img:
        if '<meta property="og:image"' in before:
            before=re.sub(r'<meta property="og:image"[^>]*>',f'<meta property="og:image" content="{img}">',before,count=1)
        else: head_add+=f'<meta property="og:image" content="{img}">'
        if '<meta name="twitter:image"' in before:
            before=re.sub(r'<meta name="twitter:image"[^>]*>',f'<meta name="twitter:image" content="{img}">',before,count=1)
        else: head_add+=f'<meta name="twitter:image" content="{img}">'
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

# ===================== Themenwelt: Eigenheim & Hypothek (V5 + Flagship-Segmente) =====================
# Flagship-Segmente (PAGE_SCHEMA §1.4 Block 2+3, §3, Contract §6): zwei vollbreite Segmente
# (je Reihe ein .v5-rub-grid mit linker .v5-fa-Hauptspalte + rechtem .v5-rub-side-Rail).
# Aktuellste Ausgabe build-dynamisch aus series_items(key)[0]; Segment-CTA routet NEU auf die LP
# (PAGE_SCHEMA §2.1/§1.6); Archiv-Link zeigt im Eigenheim-Muster auf die LP (sie traegt den Archiv-Block, §3.2).
EIGENHEIM_FLAGSHIP=[
 {'key':'hypothekenradar','badge':'Research-Reihe · monatlich','title':'Hypotheken-Radar','feature':False,
  'sub':'Der monatliche Taktgeber zu Zinsen, SARON und Festhypothek – als Entscheidungshilfe, wenn Sie abschliessen, verlängern oder umschulden.',
  'cta':('Zum Hypotheken-Radar','/de/smzhub-hypotheken-radar/'),'lp':'/de/smzhub-hypotheken-radar/',
  'rail':[('SARON oder Festhypothek?','/de/ratgeber-saron-oder-festhypothek/'),
          ('Reicht mein Einkommen für die Bank?','/de/ratgeber-tragbarkeit-hypothek/'),
          ('Amortisieren oder investieren?','/de/ratgeber-amortisieren-oder-investieren/')],
  'tool':{'tag':'Rechner','t':'Tragbarkeit und Immobilienwert prüfen','go':'Zum Immobilienrechner','href':'/de/immobilienbewertung-rechner/','imgfrom':'/de/artikel/snb-zinsentscheid-juni/'}},
 {'key':'immobilien-outlook','badge':'Research-Reihe · quartalsweise','title':'Immobilien-Outlook','feature':True,
  'sub':'Der quartalsweise Marktkompass zu Preisen, Tragbarkeit und Regionen – Orientierung für grössere Kauf- und Eigentumsentscheidungen.',
  'cta':('Zum Immobilien-Outlook','/de/smzhub-immobilien-outlook/'),'lp':'/de/smzhub-immobilien-outlook/',
  'rail':[('Kaufen oder warten?','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
          ('Wie viel Eigenkapital brauche ich wirklich?','/de/ratgeber-eigenkapital-eigenheim/'),
          ('Wie kaufe ich eine Immobilie?','/de/wie-kaufe-ich-eine-immobilie/')],
  'tool':{'tag':'Rechner','t':'Immobilienwert einschätzen','go':'Zum Bewertungsrechner','href':'/de/immobilienbewertung-rechner/','imgfrom':'/de/artikel/zuercher-wohnungsinitiativen/'}}]
# Decision-Cards (PAGE_SCHEMA §1.6/§2.2): nur Rubrik Eigenheim/Hypothek, auf reale Ratgeber geroutet.
EIGENHEIM_DECISIONS=[
 ('Hypothek','SARON oder Festhypothek?','Welche Strategie 2026 trägt, wenn die SNB-Zinsen tief sind, aber Planungssicherheit zählt.','/de/ratgeber-saron-oder-festhypothek/'),
 ('Eigenheim','Reicht mein Einkommen für die Bank?','Wie Banken die Tragbarkeit 2026 rechnen – und was Sie daran heute beeinflussen können.','/de/ratgeber-tragbarkeit-hypothek/'),
 ('Vermögen','Amortisieren oder investieren?','Schulden tilgen oder anlegen: was sich bei den Zinsen von 2026 für Sie langfristig mehr lohnt.','/de/ratgeber-amortisieren-oder-investieren/'),
 ('Eigenheim','Kaufen oder warten?','Wie Preise, Eigenkapital und Tragbarkeit 2026 zusammenspielen – und worauf es jetzt ankommt.','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
 ('Eigenheim','Wie viel Eigenkapital brauche ich wirklich?','20 Prozent sind nur die halbe Wahrheit – worauf es 2026 zusätzlich ankommt.','/de/ratgeber-eigenkapital-eigenheim/')]
# Tools-Verweis-Slot (PAGE_SCHEMA §1.4 Block 5): schlanker Link, kein eigener Rechner.
EIGENHEIM_TOOL={'tag':'Rechner','t':'Immobilienwert und Tragbarkeit prüfen',
 'go':'Zum Immobilienrechner','href':'/de/immobilienbewertung-rechner/'}
# Vertiefung Grundlagen (PAGE_SCHEMA §1.4 Block 6a, §2.3) – aus EVERGREEN['immobilien'].
EIGENHEIM_EVERGREEN=[('Tragbarkeit optimieren','/de/optimierung-der-tragbarkeit/'),
 ('Hypothekenarten im Vergleich','/de/hypothekenarten-im-vergleich/'),
 ('Wie kaufe ich eine Immobilie?','/de/wie-kaufe-ich-eine-immobilie/'),
 ('Wohneigentumsförderung','/de/wohneigentumsfoerderung/')]
EIGENHEIM_DOSSIER=('/de/smzhub-dossier-eigenheim/','Eigenheim finanzieren')
# Ratgeber-Sektion (PAGE_SCHEMA §1.4 Block 6, §2.2): reale ratgeber-* als Lese-Einstiege (reine Lese-Links).
# Titel = reale Seiten-Titel der gerenderten ratgeber-*; Kategorie aus dem Themen-Cluster. Kein Conversion-CTA.
EIGENHEIM_RATGEBER=[
 ('Hypothek','SARON oder Festhypothek 2026: Was lohnt sich?','/de/ratgeber-saron-oder-festhypothek/'),
 ('Tragbarkeit','Tragbarkeit Hypothek 2026: Reicht mein Einkommen?','/de/ratgeber-tragbarkeit-hypothek/'),
 ('Eigenheim','Eigenkapital fürs Eigenheim 2026: Wie viel wirklich?','/de/ratgeber-eigenkapital-eigenheim/'),
 ('Markt','Eigenheim kaufen oder warten? Ratgeber 2026','/de/ratgeber-eigenheim-kaufen-oder-warten/'),
 ('Vermögen','Hypothek amortisieren oder investieren? 2026','/de/ratgeber-amortisieren-oder-investieren/')]
# Stories (PAGE_SCHEMA §1.4 Block 7, §2.5; Texte build-spec Abschnitt 3): anonymisierte Ausgangslagen,
# KEINE erfundenen Personen. Je Story ein reiner Lese-Link in den passenden Ratgeber.
EIGENHEIM_STORIES=[
 ('Erstkauf mit knappem Eigenkapital',
  'Das Wunschobjekt ist gefunden, doch die 20 Prozent Eigenkapital sind erst zur Hälfte beisammen – und ein Teil steckt in der Pensionskasse. Die Frage: Reicht es bereits, und welche Mittel darf die Bank überhaupt anrechnen?',
  '/de/ratgeber-eigenkapital-eigenheim/'),
 ('Festhypothek läuft aus – verlängern oder wechseln?',
  'In wenigen Monaten endet die Festhypothek. Verlängern, in eine SARON-Lösung wechseln oder auf mehrere Laufzeiten verteilen? Entscheidend ist weniger die Zinsprognose als die Frage, wie viel Schwankung das Budget verträgt.',
  '/de/ratgeber-saron-oder-festhypothek/'),
 ('Freies Kapital: amortisieren oder anlegen?',
  'Nach einigen Jahren ist Kapital frei geworden. Soll es in die Hypothek fliessen und die Schuld senken – oder breit angelegt werden? Die Antwort hängt von Zins, erwarteter Rendite und der eigenen Steuersituation ab.',
  '/de/ratgeber-amortisieren-oder-investieren/')]

def eigenheim_flagship():
    # Pro Reihe EIN vollbreites .v5-rub-grid: links .v5-fa (Outlook zusaetzlich .v5-fa--feature),
    # rechts .v5-rub-side (reine Lese-Links + ein Rechner-.v5-mid). Reihenfolge: Radar, dann Outlook.
    segs=''
    for fa in EIGENHEIM_FLAGSHIP:
        its=series_items(fa['key']); cur=its[0] if its else None
        im=opt_img(cur['image'],640) if cur else None
        cov=f'<span class="v5-fa-cov">{imgt(im)}<span class="v5-fa-badge">{esc(fa["badge"])}</span></span>'
        latest=''
        if cur:
            date=fquarter(cur.get('date')) if fa['key']=='immobilien-outlook' else fdate(cur.get('date'))
            datelbl='Aktuelle Ausgabe'+(f' · {date}' if date else '')
            latest=(f'<span class="v5-fa-latest"><span class="v5-fa-date">{esc(datelbl)}</span>'
                    f'<a class="v5-fa-latest-t" href="{link(cur["path"])}">{esc(cur["title"])}</a></span>')
        cl,cp=fa['cta']
        foot=(f'<div class="v5-fa-foot"><a class="v5-fa-cta" href="{link(cp)}">{esc(cl)} <span class="ar">→</span></a>'
              f'<a class="v5-fa-archive" href="{link(fa["lp"])}">Alle Ausgaben →</a></div>')
        facls='v5-fa v5-fa--feature' if fa.get('feature') else 'v5-fa'
        main=(f'<article class="{facls}">{cov}<div class="v5-fa-body">'
              f'<h3 class="v5-fa-title">{esc(fa["title"])}</h3>'
              f'<p class="v5-fa-sub">{esc(fa["sub"])}</p>{latest}</div>{foot}</article>')
        # Rechtes Kontext-Rail: reine Lese-Links (Meta = Min falls bekannt, sonst Pfeil) + ein Rechner-.v5-mid
        sl_html=''.join(f'<a class="v5-sl" href="{link(h)}"><span class="v5-sl-t">{esc(t)}</span>'
                        f'<span class="v5-sl-m">{esc(rmin(h)) if rmin(h) else "→"}</span></a>' for t,h in fa['rail'])
        tl=fa['tool']; tim=img_of(tl['imgfrom'],640)
        mid=(f'<a class="v5-mid" href="{link(tl["href"])}"><span class="v5-mid-img">{imgt(tim)}'
             f'<span class="v5-mid-tag">{esc(tl["tag"])}</span></span>'
             f'<span class="v5-mid-b"><span class="v5-mid-t">{esc(tl["t"])}</span>'
             f'<span class="v5-mid-go">{esc(tl["go"])}</span></span></a>')
        side=f'<div class="v5-rub-side"><div class="v5-sl-list">{sl_html}</div>{mid}</div>'
        segs+=f'<div class="v5-rub-grid" style="--cols:3fr 2fr;margin-bottom:2.8rem">{main}{side}</div>'
    head=('<div class="v5-head"><div><h2>Unsere Research-Reihen zu Eigenheim und Hypothek</h2>'
          '<p class="v5-sub">Zwei feste Formate, die wir regelmässig fortschreiben – kein loser '
          'Beitragsstrom, sondern eine verlässliche Grundlage für Finanzierungs- und Kaufentscheidungen.</p></div></div>')
    return f'<section class="v5-flagship">{head}{segs}</section>'

# Zins-Chart (PAGE_SCHEMA §1.4 Block 4, §2.6, Contract §7): EINE Datenreihe, statisches Inline-SVG.
# VERIFIZIERTE SNB-Leitzins-Reihe (build-spec Abschnitt 4) – resultierender Satz nach jeder Lagebeurteilung.
# Step-/Treppenbewegung: Wert gilt ab Entscheiddatum bis zum naechsten. KEINE erfundenen/interpolierten Werte.
SNB_SERIES=[  # (Perioden-Label, Jahr-fuer-X-Achse, Satz %)
 ('bis Jun 2022',2022,-0.75),('16.06.2022',2022,-0.25),('22.09.2022',2022,0.50),('15.12.2022',2022,1.00),
 ('23.03.2023',2023,1.50),('22.06.2023',2023,1.75),('21.03.2024',2024,1.50),('20.06.2024',2024,1.25),
 ('26.09.2024',2024,1.00),('12.12.2024',2024,0.50),('20.03.2025',2025,0.25),('19.06.2025',2025,0.00),
 ('Jun 2026',2026,0.00)]
def eigenheim_ratechart():
    n=len(SNB_SERIES)
    # Plot-Flaeche x 56..680 (Breite 624), y 28..272 (Hoehe 244). Y-Skala -0.75..+1.75 (Bereich 2.5).
    ppp=244/2.5
    X=lambda i:round(56+i*(624/(n-1)),1)
    Y=lambda v:round(272-(v-(-0.75))*ppp,1)
    pts=[(X(i),Y(v)) for i,(_,_,v) in enumerate(SNB_SERIES)]
    step=[pts[0]]
    for i in range(1,n):
        step.append((pts[i][0],pts[i-1][1])); step.append(pts[i])
    poly=' '.join(f'{a},{b}' for a,b in step)
    area='M'+' L'.join(f'{a},{b}' for a,b in step)+f' L{pts[-1][0]},272 L{pts[0][0]},272 Z'
    # Marker an den Entscheidpunkten; deckungsgleiche Endpunkte (gleicher Wert) nur einmal zeichnen
    seen=set(); dots=''
    for a,b in pts:
        if (a,b) in seen: continue
        seen.add((a,b)); dots+=f'<circle class="v5-rc-dot" cx="{a}" cy="{b}" r="3.5"></circle>'
    # horizontale Gitterlinien + Y-Labels (dezent): 1.75 / 1.0 / 0.0 / -0.75
    yticks=''.join(f'<line class="v5-rc-grid" x1="56" y1="{Y(t)}" x2="680" y2="{Y(t)}"></line>'
                   f'<text class="v5-rc-lbl v5-rc-lbl-y" x="46" y="{round(Y(t)+4,1)}">{lbl}</text>'
                   for t,lbl in [(1.75,'1,75 %'),(1.0,'1,0 %'),(0.0,'0,0 %'),(-0.75,'−0,75 %')])
    # X-Labels: erster Entscheid je Jahr (zeitlich korrekt verortet)
    xseen=set(); xlbl=''
    for i,(_,yr,_) in enumerate(SNB_SERIES):
        if yr in xseen: continue
        xseen.add(yr); xlbl+=f'<text class="v5-rc-lbl v5-rc-lbl-x" x="{X(i)}" y="292">{yr}</text>'
    svg=(f'<svg class="v5-rc-svg" viewBox="0 0 720 320" preserveAspectRatio="xMidYMid meet" role="img" '
         f'aria-labelledby="rc-t rc-d" style="aspect-ratio:720/320">'
         f'<title id="rc-t">SNB-Leitzins seit 2022</title>'
         f'<desc id="rc-d">Resultierender SNB-Leitzins nach jeder Lagebeurteilung, von −0,75 Prozent bis 1,75 Prozent und zurück auf 0,0 Prozent.</desc>'
         f'{yticks}<path class="v5-rc-area" d="{area}"></path>'
         f'<polyline class="v5-rc-line" points="{poly}"></polyline>{dots}'
         f'<line class="v5-rc-axis" x1="56" y1="272" x2="680" y2="272"></line>{xlbl}</svg>')
    cap='SNB-Leitzins in Prozent. Quelle: Schweizerische Nationalbank (data.snb.ch). Stand: Juni 2026.'
    head=('<div class="v5-head"><div><h2>Wie haben sich die Zinsen entwickelt?</h2>'
          '<p class="v5-sub">Der SNB-Leitzins ist die gemeinsame Achse hinter Hypotheken-Radar und Immobilien-Outlook: '
          'Er prägt die Konditionen für Festhypotheken ebenso wie die Bewegung am Immobilienmarkt.</p></div></div>')
    return (f'<section class="v5-sec v5-ratechart">{head}'
            f'<figure class="v5-rc-fig" style="max-width:760px">{svg}<figcaption>{esc(cap)}</figcaption></figure></section>')

def eigenheim_decisions():
    cards=''
    shapes=['#185E7F','#03314B','#185E7F','#03314B','#185E7F']
    for i,(cat,q,desc,p) in enumerate(EIGENHEIM_DECISIONS):
        cards+=(f'<a class="v5-dec" href="{link(p)}"><span class="v5-dec-cat">{esc(cat)}</span>'
                f'<span class="v5-dec-q">{esc(q)}</span><span class="v5-dec-d">{esc(desc)}</span>'
                f'<span class="v5-dec-fresh">Aktualisiert · 2026</span>'
                f'<span class="v5-dec-shape" style="background:{shapes[i%5]}"></span></a>')
    nav=('<div class="v5-dec-nav"><span class="v5-dec-arrow v5-dec-prev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
         '<span class="v5-dec-arrow v5-dec-next" role="button" tabindex="0" aria-label="Weiter">›</span></div>')
    return (f'<section class="v5-sec v5-dec-sec"><div class="v5-head"><div><h2>Ihre Entscheidung</h2>'
            f'<p class="v5-sub">Konkrete Fragen rund um Eigenheim und Hypothek – mit dem passenden Einstieg in den Ratgeber.</p></div>'
            f'{nav}</div><div class="v5-dec-vp"><div class="v5-dec-track">{cards}</div></div></section>')

def eigenheim_ratgeber():
    # Ratgeber-Sektion (Block 6): reine Lese-Links in reale ratgeber-* (kein Conversion-CTA, §8).
    cards=''.join(f'<a class="art-rel-card" href="{link(h)}"><span class="art-rel-k">Ratgeber · {esc(cat)}</span>'
                  f'<span class="art-rel-t">{esc(t)}</span>'
                  f'<span class="art-rel-go">Beitrag lesen <span class="ar">→</span></span></a>' for cat,t,h in EIGENHEIM_RATGEBER)
    return (f'<section class="v5-sec"><div class="v5-head"><div><h2>Ratgeber zu Eigenheim und Hypothek</h2>'
            f'<p class="v5-sub">Die wichtigsten Einstiege zum Nachlesen – fundierte Grundlagen statt loser Beitragsstrom.</p></div></div>'
            f'<div class="art-rel-grid">{cards}</div></section>')

def eigenheim_stories():
    # Stories (Block 7): anonymisierte Ausgangslagen, reine Lese-Links (build-spec Abschnitt 3).
    cards=''.join(f'<a class="art-rel-card" href="{link(h)}"><span class="art-rel-t">{esc(t)}</span>'
                  f'<span class="v5-rh-p" style="font-size:.92rem;line-height:1.5">{esc(teas)}</span>'
                  f'<span class="art-rel-go">Beitrag lesen <span class="ar">→</span></span></a>' for t,teas,h in EIGENHEIM_STORIES)
    return (f'<section class="v5-sec"><div class="v5-head"><div><h2>Typische Ausgangslagen</h2>'
            f'<p class="v5-sub">Drei Situationen, die in der Eigenheimberatung immer wiederkehren – anonymisiert dargestellt.</p></div></div>'
            f'<div class="art-rel-grid">{cards}</div></section>')

def eigenheim_tools():
    t=EIGENHEIM_TOOL; tim=img_of('/de/artikel/zuercher-wohnungsinitiativen/',640)
    mid=(f'<a class="v5-mid" href="{link(t["href"])}" style="max-width:420px;margin-top:0">'
         f'<span class="v5-mid-img">{imgt(tim)}<span class="v5-mid-tag">{esc(t["tag"])}</span></span>'
         f'<span class="v5-mid-b"><span class="v5-mid-t">{esc(t["t"])}</span>'
         f'<span class="v5-mid-go">{esc(t["go"])}</span></span></a>')
    return (f'<section class="v5-sec"><div class="v5-head"><div><h2>Rechner & Tools</h2>'
            f'<p class="v5-sub">Selbst einordnen, bevor Sie beraten lassen: Immobilienwert und Tragbarkeit in wenigen Minuten.</p></div></div>'
            f'{mid}</section>')

def eigenheim_depth():
    rows_html=''.join(f'<a class="v5-sl" href="{link(h)}"><span class="v5-sl-t">{esc(t)}</span>'
                      f'<span class="v5-sl-m">→</span></a>' for t,h in EIGENHEIM_EVERGREEN)
    grundlagen=(f'<div class="v5-head"><div><h2>Grundlagen vertiefen</h2>'
                f'<p class="v5-sub">Die wichtigsten Evergreen-Erklärungen rund um Kauf, Tragbarkeit und Finanzierung.</p></div></div>'
                f'<div class="v5-sl-list">{rows_html}</div>')
    dp,dt=EIGENHEIM_DOSSIER
    dossier=(f'<a class="v5-mid" href="{link(dp)}" style="max-width:420px">'
             f'<span class="v5-mid-b" style="padding:1.2rem 1.4rem">'
             f'<span class="v5-mid-tag" style="position:static;width:max-content;margin-bottom:.5rem">Dossier</span>'
             f'<span class="v5-mid-t">{esc(dt)}</span>'
             f'<span class="v5-mid-go">Dem roten Faden folgen</span></span></a>')
    return f'<section class="v5-sec">{grundlagen}{dossier}</section>'

# Schluss-CTA (PAGE_SCHEMA §1.4 Block 7): themenweiter Beratungs-/360°-CTA, terminorientiert.
# Wiederverwendung der .art-cta-Komponente (vgl. COMPONENT_LIBRARY „Artikel — CTA-Block"),
# genau ein Primaer-Button (btn1) auf /de/terminvereinbaren/, sekundaer auf den Finanzierungs-Erstkontakt.
def eigenheim_cta():
    return ('<div class="art-cta"><p class="art-cta-eyebrow">360° Check-Up</p>'
            '<h3>Wie tragfähig ist Ihre Eigenheim- und Hypothekenstrategie?</h3>'
            '<p>Im 360°-Finanzcheck ordnen wir Tragbarkeit, Zinsstrategie und Eigenkapital für Ihre '
            'Situation ein – und zeigen die nächsten Schritte, bevor Sie kaufen, verlängern oder umschulden.</p>'
            '<div class="art-cta-row">'
            f'<a class="art-cta-btn art-cta-btn1" href="{link("/de/terminvereinbaren/")}">360°-Finanzcheck vereinbaren<span class="ar">→</span></a>'
            f'<a class="art-cta-btn art-cta-btn2" href="{link("/de/finanzierungsberatung/")}">Finanzierungsberatung ansehen<span class="ar">→</span></a></div>'
            '<div class="art-cta-trust"><span>Unverbindlich</span><span>Persönlich beraten</span><span>Auf Ihre Situation</span></div>'
            '</div>')

def eigenheim_inner():
    hero=('<section class="v5-phead"><div class="v5-phead-in">'
          '<p class="v5-eyebrow">smzhHub · Themenwelt</p><h1>Eigenheim &amp; Hypothek</h1>'
          '<p>Kaufen, finanzieren, halten: die Entscheidungen rund um Wohneigentum, sachlich eingeordnet. '
          'Wir verbinden laufendes Research zu Zinsen, Hypotheken und Immobilienmarkt mit konkreten Schritten für Ihre Situation.</p>'
          f'<p style="margin-top:1.4rem"><a class="v5-phead-cta" href="{link("/de/terminvereinbaren/")}">Finanzierung besprechen <span class="ar">→</span></a></p>'
          '</div></section>')
    # Block-Reihenfolge VERBINDLICH nach PAGE_SCHEMA §1.4:
    # Hero → Flagship-Segmente (Radar+Outlook) → Zins-Chart → Entscheidungspfade → Ratgeber → Stories
    # → Rechner/Tools → Vertiefung (Grundlagen+Dossier) → Schluss-CTA → Back-Link.
    body=(eigenheim_flagship()+eigenheim_ratechart()+eigenheim_decisions()
          +eigenheim_ratgeber()+eigenheim_stories()+eigenheim_tools()+eigenheim_depth()
          +eigenheim_cta()
          +f'<section class="v5-sec v5-backsec"><a class="v5-back" href="{link("/de/smzhub/")}">← Zurück zum smzhHub</a></section>')
    return f'<div class="v5">{hero}<div class="v5-wrap">{body}</div></div>'

# ===================== Flagship-Landingpages (PAGE_SCHEMA §6/§7, Contract §8, build-spec 1/2) =====================
# Zwei LPs im V5-Bestandsraster: Hero (.v5-phead, 1 CTA) → Erklaerteil → Download (aktuell)
# → Archiv → Schluss-CTA (.art-cta) → Back-Link. Aktuelle Ausgabe build-dynamisch series_items(key)[0];
# PDF via pdf_of() (bevorzugt _DE_, Existenzpruefung) -> Download-Pille, sonst Fallback Lese-Link.
def _exists_slug(p): return os.path.isdir(os.path.join(SMZH,*[s for s in p.strip('/').split('/') if s]))

FLAGSHIP_LP={
 'hypothekenradar':{
  'slug':'smzhub-hypotheken-radar','key':'hypothekenradar','datefn':fdate,
  'eyebrow':'smzhHub · Research · monatlich','h1':'Hypotheken-Radar',
  'dek':'Unsere monatliche Einordnung zu Zinsen, SARON und Festhypotheken in der Schweiz. Der Hypotheken-Radar zeigt, wo die Hypothekarzinsen stehen, was die nächste SNB-Lagebeurteilung bedeutet und worauf es bei Abschluss, Verlängerung und Umschuldung ankommt.',
  'hero_cta':('Finanzierung besprechen','/de/terminvereinbaren/'),
  'about_h':'Was der Hypotheken-Radar leistet',
  'about_p':'Der Hypotheken-Radar erscheint monatlich und ordnet das Zinsumfeld für private Hypothekarnehmer ein — verständlich und ohne Verkaufslogik. Jede Ausgabe verfolgt die Erwartung an die nächste SNB-Lagebeurteilung, das Niveau der Festhypothekarsätze und die Frage, wann sich SARON oder eine feste Laufzeit aufdrängt. Die Reihe richtet sich an alle, die vor einem Abschluss, einer Verlängerung oder einer Umschuldung stehen und eine fundierte Grundlage suchen, statt Schlagzeilen. Wer wiederkehrend mitliest, erkennt Zinsbewegungen früh — und entscheidet auf Basis von Einordnung, nicht von Bauchgefühl.',
  'dl_h':'Neueste Ausgabe',
  'dl_p':'Die aktuelle Ausgabe als PDF — mit der Zinslage des Monats und unserer Einordnung für die kommenden Wochen.',
  'dl_btn':'Neueste Ausgabe lesen (PDF)','dl_read':'Zum aktuellen Beitrag','dl_secondary':'Zum Beitrag',
  'arch_h':'Frühere Ausgaben',
  'arch_p':'Jede Ausgabe hält die Zinslage ihres Monats fest. Im Verlauf wird sichtbar, wie sich das Umfeld für Hypotheken bewegt hat.',
  'arch_series':'/de/smzhub-serie-hypotheken-radar/',
  'cta_eyebrow':'360° Check-Up','cta_h':'Wie sicher steht Ihre Finanzierung im aktuellen Zinsumfeld?',
  'cta_p':'Ob Erstabschluss, auslaufende Festhypothek oder Umschuldung — wir ordnen Ihre Tragbarkeit, Zinsstrategie und Laufzeiten für Ihre Situation ein und zeigen die nächsten Schritte. Unabhängig, auf Basis des laufenden Research hinter dem Hypotheken-Radar.',
  'cta_btn1':('Finanzierung besprechen','/de/terminvereinbaren/'),
  'cta_btn2':('Finanzierungsberatung ansehen','/de/finanzierungsberatung/'),
  'title':'Hypotheken-Radar – monatliches Zins-Research | smzhHub'},
 'immobilien-outlook':{
  'slug':'smzhub-immobilien-outlook','key':'immobilien-outlook','datefn':fquarter,'feature':True,
  'eyebrow':'smzhHub · Research · quartalsweise','h1':'Immobilien-Outlook',
  'dek':'Unser quartalsweiser Marktkompass für den Schweizer Immobilienmarkt. Der Immobilien-Outlook bündelt Preisentwicklung, Tragbarkeit, regionale Unterschiede und die Faktoren hinter der Nachfrage — als Grundlage für grössere Eigentumsentscheidungen.',
  'hero_cta':('Eigenheimstrategie besprechen','/de/terminvereinbaren/'),
  'about_h':'Was der Immobilien-Outlook leistet',
  'about_p':'Der Immobilien-Outlook erscheint quartalsweise und ordnet den Schweizer Immobilienmarkt für Eigentümer und Kaufinteressierte ein. Jede Ausgabe verbindet Preisentwicklung und Tragbarkeit mit regionalen Unterschieden, demografischen Treibern und dem regulatorischen Umfeld — und übersetzt sie in eine Einschätzung des Marktausblicks. Die Reihe richtet sich an alle, die vor einem Kauf, einer Strategiefrage oder der Planung des Eigenkapitals stehen und mehr wollen als Schlagzeilen zur Preisentwicklung. Quartal für Quartal entsteht so ein belastbares Bild des Marktes statt einer Momentaufnahme.',
  'dl_h':'Aktuelle Ausgabe',
  'dl_p':'Der vollständige Marktausblick des Quartals als PDF — mit Datenlage, regionalen Einschätzungen und unserer Markteinordnung.',
  'dl_btn':'Aktuelle Ausgabe lesen (PDF)','dl_read':'Zum aktuellen Beitrag','dl_secondary':'Zum Beitrag',
  'arch_h':'Frühere Ausgaben',
  'arch_p':'Jedes Quartal hält den Stand des Marktes fest. In der Folge der Ausgaben wird die Entwicklung von Preisen, Nachfrage und Rahmenbedingungen nachvollziehbar.',
  'arch_series':'/de/smzhub-serie-immobilien-outlook/',
  'cta_eyebrow':'360° Check-Up','cta_h':'Passt Ihre Eigentumsstrategie zum aktuellen Markt?',
  'cta_p':'Ob Kaufentscheid, Eigenkapitalplanung oder die Frage, ob Sie halten oder umschichten — wir ordnen Ihre Situation vor dem Hintergrund von Marktlage und Tragbarkeit ein und zeigen die nächsten Schritte. Unabhängig, auf Basis des Research hinter dem Immobilien-Outlook.',
  'cta_btn1':('Eigenheimstrategie besprechen','/de/terminvereinbaren/'),
  'cta_btn2':('Immobilienberatung ansehen','/de/immobilienberatung/'),
  'title':'Immobilien-Outlook – quartalsweiser Marktkompass | smzhHub'}}

def flagship_lp_inner(cfg):
    its=series_items(cfg['key']); cur=its[0] if its else None
    df=cfg['datefn']
    # Hero (Block a): genau 1 Beratungs-CTA
    hl,hp=cfg['hero_cta']
    hero=('<section class="v5-phead"><div class="v5-phead-in">'
          f'<p class="v5-eyebrow">{esc(cfg["eyebrow"])}</p><h1>{esc(cfg["h1"])}</h1><p>{esc(cfg["dek"])}</p>'
          f'<p style="margin-top:1.4rem"><a class="v5-phead-cta" href="{link(hp)}">{esc(hl)} <span class="ar">→</span></a></p>'
          '</div></section>')
    # Erklaerteil (Block b): reiner Text, kein CTA
    about=(f'<section class="v5-sec"><div class="v5-head"><div><h2>{esc(cfg["about_h"])}</h2></div></div>'
           f'<p class="v5-lead">{esc(cfg["about_p"])}</p></section>')
    # Download (Block c): aktuelle Ausgabe; PDF -> Pille, Fallback -> Lese-Link
    if cur:
        date=df(cur.get('date')); meta='Aktuelle Ausgabe'+(f' · {date}' if date else '')
        pdf=pdf_of(cur)
        if pdf:
            act=f'<div class="v5-dl-act"><a class="v5-dl-btn" href="{upload(pdf)}" download>{esc(cfg["dl_btn"])} <span class="ar">↓</span></a></div>'
            read=f'<div class="v5-dl-act" style="margin-top:.4rem"><a class="v5-dl-read" href="{link(cur["path"])}">{esc(cfg["dl_secondary"])} <span class="ar">→</span></a></div>'
            act=act+read
        else:
            act=f'<div class="v5-dl-act"><a class="v5-dl-read" href="{link(cur["path"])}">{esc(cfg["dl_read"])} <span class="ar">→</span></a></div>'
        dl_card=(f'<div class="v5-dl"><span class="v5-dl-meta">{esc(meta)}</span>'
                 f'<span class="v5-dl-t">{esc(cur["title"])}</span>'
                 f'<p class="v5-dl-p">{esc(cfg["dl_p"])}</p>{act}</div>')
    else:
        dl_card='<div class="v5-dl"><p class="v5-dl-p">Derzeit ist keine aktuelle Ausgabe verfügbar.</p></div>'
    download=(f'<section class="v5-sec"><div class="v5-head"><div><h2>{esc(cfg["dl_h"])}</h2></div></div>{dl_card}</section>')
    # Archiv (Block d): Lese-Links + Verweis auf Serien-Seite
    rows_html=''.join(f'<a class="v5-sl" href="{link(r["path"])}"><span class="v5-sl-t">{esc(r["title"])}</span>'
                      f'<span class="v5-sl-m">{esc(df(r.get("date")))}</span></a>' for r in its)
    archive=(f'<section class="v5-sec v5-arch"><div class="v5-head"><div><h2>{esc(cfg["arch_h"])}</h2>'
             f'<p class="v5-sub">{esc(cfg["arch_p"])}</p></div></div>'
             f'<div class="v5-sl-list">{rows_html}</div>'
             f'<a class="v5-arch-all" href="{link(cfg["arch_series"])}">Alle Ausgaben ansehen <span class="ar">→</span></a></section>')
    # Schluss-CTA (Block e): .art-cta, 1 Primaer-Button; Sekundaer mit Existenz-Fallback
    b1l,b1p=cfg['cta_btn1']; b2l,b2p=cfg['cta_btn2']
    if not _exists_slug(b2p): b2p='/de/terminvereinbaren/'
    cta=('<div class="art-cta">'
         f'<p class="art-cta-eyebrow">{esc(cfg["cta_eyebrow"])}</p>'
         f'<h3>{esc(cfg["cta_h"])}</h3><p>{esc(cfg["cta_p"])}</p>'
         '<div class="art-cta-row">'
         f'<a class="art-cta-btn art-cta-btn1" href="{link(b1p)}">{esc(b1l)}<span class="ar">→</span></a>'
         f'<a class="art-cta-btn art-cta-btn2" href="{link(b2p)}">{esc(b2l)}<span class="ar">→</span></a></div>'
         '<div class="art-cta-trust"><span>Unverbindlich</span><span>Persönlich beraten</span><span>Auf Ihre Situation</span></div>'
         '</div>')
    back=f'<section class="v5-sec v5-backsec"><a class="v5-back" href="{link("/de/smzhub-eigenheim/")}">← Zurück zu Eigenheim & Hypothek</a></section>'
    return f'<div class="v5">{hero}<div class="v5-wrap">{about+download+archive+cta+back}</div></div>'

def flagship_lp_meta(cfg):
    return {'desc':cfg['dek'],
        'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':cfg['h1'],
                   'isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]}

ORG={'@type':'Organization','name':'smzh','url':'https://smzh.ch','logo':'https://smzh.ch/favicon.ico'}

def main():
    home_meta={'desc':'smzhHub ordnet Märkte, Eigenheim, Vorsorge und Steuern so ein, dass Sie Ihre nächste Finanzentscheidung 2026 sicherer treffen. Einordnungen, Ratgeber und Research.',
        'jsonld':[{'@context':'https://schema.org','@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/','publisher':ORG}]}
    build_page(('de','smzhub'),home_inner(),'smzhHub – Klarheit für Ihre Finanzentscheidungen',home_meta)
    build_page(('de','smzhub-eigenheim'),eigenheim_inner(),'Eigenheim & Hypothek einordnen | smzhHub',
        {'desc':'Eigenheim & Hypothek sachlich eingeordnet: Hypotheken-Radar und Immobilien-Outlook, Entscheidungspfade zu SARON, Tragbarkeit und Eigenkapital sowie der Weg zur Finanzierungsberatung.',
         'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':'Eigenheim & Hypothek','isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]})
    # Flagship-LPs (PAGE_SCHEMA §6/§7) – build-dynamische Download-/Archiv-Bloecke aus series_items.
    for k in ('hypothekenradar','immobilien-outlook'):
        cfg=FLAGSHIP_LP[k]
        build_page(('de',cfg['slug']),flagship_lp_inner(cfg),cfg['title'],flagship_lp_meta(cfg))
    build_page(('de','smzhub-immobilienanlagen'),immobilienanlagen_inner(),'Immobilienanlagen einordnen | smzhHub',
        {'desc':'Renditeobjekte und indirekte Immobilienanlagen verständlich eingeordnet: Rendite, Risiken, Regulierung und Finanzierung für Ihre Anlageentscheidung.',
         'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':'Immobilienanlagen','isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]})
    build_page(('de','smzhub-horizon'),horizon_inner(),'smzh horizon – Trends & Ausblick | smzhHub',
        {'desc':'smzh horizon bündelt den längeren Blick: makroökonomische Trends, strukturelle Entwicklungen und Ausblicke, die die Themenwelten des smzhHub verbinden.',
         'jsonld':[{'@context':'https://schema.org','@type':'CollectionPage','name':'smzh horizon','isPartOf':{'@type':'WebSite','name':'smzhHub','url':BASE+'/de/smzhub/'},'publisher':ORG}]})
    print('OK V5: Landing Page + Themenwelten (Eigenheim & Hypothek, Immobilienanlagen, smzh horizon) + Flagship-LPs (Hypotheken-Radar, Immobilien-Outlook) geschrieben.')

if __name__=='__main__':
    main()
