#!/usr/bin/env python3
"""Iteration 7 – smzhHub als Hybrid Hub (Editorial + Decision + Research).
Strategisches Beratungs-/Research-System mit redaktioneller Oberfläche.
Sichtbare Reiter: Aktuell · Eigenheim · Vermögen · Zukunft · Steuern · Research.
Startseite: Hero-Slider → Entscheidungs-Karussell → redaktionelle Rubriken mit
Flagship-Ankern und Lead-Pfaden → Steuern-Kompaktmodul → Research-Band → CTA.
Backend-Taxonomie (kanonische Rubrik je Beitrag) aus build/smzhhub-content.json;
klar markierte Platzhalter aus build/smzhub-placeholders.json.
Schreibt nur unter site/smzh.ch/de/.
"""
import json, os, re, html as H, urllib.parse
from datetime import datetime
import sys; sys.path.insert(0,'build')
import postprocess_all as P

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch')
CHROME_SRC='build/backup/pre-ia/smzhub-index.html'
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
PH=json.load(open('build/smzhub-placeholders.json',encoding='utf-8'))
PH_BY={p['id']:p for p in PH}
P_='../../'

MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def teaser(r,n=150):
    t=r.get('excerpt') or r.get('teaser') or ''
    return (t[:n].rsplit(' ',1)[0]+'…') if len(t)>n else t
def link(path):
    segs=[s for s in path.strip('/').split('/') if s]; return P_+'/'.join(segs)+'/index.html'
def exists(path): return os.path.exists(os.path.join(SMZH,path.strip('/'),'index.html'))

def opt_img(cms_path, w):
    if not cms_path: return None
    enc=urllib.parse.quote('https://cms.smzh.ch'+cms_path, safe='')
    dest=os.path.join(SMZH,'_next','image',f'index.html@url={enc}&w={w}&q=75')
    P.download(f'https://smzh.ch/_next/image/?url={enc}&w={w}&q=75', dest)
    if not os.path.exists(dest): return None
    return P_+'_next/image/index.html@url='+enc.replace('%','%25')+f'&amp;w={w}&amp;q=75'
def img_of(r,w): return opt_img(r.get('image'), w)

# ---- Datenauswahl ----
def komm_rubric(key):
    out=[r for r in rows if r.get('rubric')==key and r['hubType']=='kommentar' and r.get('hubEligible')]
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)
def lead_rubric(key):
    out=[r for r in rows if r.get('rubric')==key and r.get('leadEligible')]
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)
def series_items(key): return sorted([r for r in rows if r.get('series')==key], key=lambda r:r.get('date') or '', reverse=True)
def hero_picks():
    best=[]
    for key in ['kapitalmaerkte','immobilien','vorsorge','steuern']:
        ls=lead_rubric(key)
        if ls: best.append(ls[0])
    best.sort(key=lambda r:r.get('date') or '', reverse=True)
    return best[:3]

# ---- Konfiguration ----
THEMES=[
 ('aktuell','Aktuell','de/smzhub/'),
 ('eigenheim','Eigenheim','de/smzhub-eigenheim/'),
 ('vermoegen','Vermögen','de/smzhub-vermoegen/'),
 ('zukunft','Zukunft','de/smzhub-zukunft/'),
 ('steuern','Steuern','de/smzhub-steuern/'),
 ('research','Research','de/smzhub-research/'),
]
THEME_BY={k:(lbl,path) for k,lbl,path in THEMES}
TAB_RUBRIC={'eigenheim':'immobilien','vermoegen':'kapitalmaerkte','zukunft':'vorsorge','steuern':'steuern'}
# tab -> (Intro, Anker-Serien, (CTA-Label, CTA-Pfad))
TAB_META={
 'eigenheim':('Kaufen, finanzieren, halten – Hypothek, Tragbarkeit und Immobilienmarkt klar eingeordnet.',
              ['hypothekenradar','immobilien-outlook'], ('Hypothek prüfen lassen','de/immobilienbewertung/')),
 'vermoegen':('Märkte, Zinsen und Portfolios verständlich – ohne tägliches Börsenrauschen.',
              ['investment-guide'], ('Anlagestrategie besprechen','de/terminvereinbaren/')),
 'zukunft':('AHV, Pensionskasse und Säule 3a – damit aus Unsicherheit ein Plan wird.',
            [], ('Vorsorge analysieren','de/vorsorgeanalyse/')),
 'steuern':('Steuern senken und Vermögen klug strukturieren – konkret und planbar.',
            [], ('Steuern optimieren','de/steuererklaerung/')),
}
# Home-Rubriken: (tab, Sektionstitel, Lead-Kicker, Dossier-Platzhalter-id)
HOME_RUBRICS=[
 ('eigenheim','Eigenheim & Finanzierung','Leitartikel','ph-dossier-eigenheim'),
 ('vermoegen','Vermögen aufbauen','Markteinschätzung',None),
 ('zukunft','Zukunft planen','Dossier','ph-dossier-pensionierung'),
]
EVERGREEN={
 'kapitalmaerkte':[('Anlagestrategie verstehen','de/anlagestrategie/'),('Risikoprofil erstellen','de/risikoprofil-erstellen/'),('Leitfaden Anlageberatung','de/leitfaden-zur-anlageberatung-in-der-schweiz/'),('Kosten & Gebühren beim Investieren','de/kosten-and-gebuehren-beim-investieren/')],
 'immobilien':[('Tragbarkeit optimieren','de/optimierung-der-tragbarkeit/'),('Hypothekenarten im Vergleich','de/hypothekenarten-im-vergleich/'),('Wie kaufe ich eine Immobilie?','de/wie-kaufe-ich-eine-immobilie/'),('Wohneigentumsförderung','de/wohneigentumsfoerderung/')],
 'vorsorge':[('Das 3-Säulen-System','de/das-3-saeulensystem-der-schweiz/'),('Säule 3a optimal nutzen','de/altersvorsorge-optimierung-saeule-3a/'),('Pensionsplanung','de/pensionsplanung/'),('Leistungen im Alter','de/leistungen-im-alter/')],
 'steuern':[('Steuerabzüge optimal nutzen','de/steuerabzuege-optimal-nutzen/'),('Grundlagen Steuererklärung','de/grundlagen-zur-steuererklaerung/'),('Steuern bei Wohneigentum','de/steuern-wohneigentum/'),('Finanzplan erstellen','de/finanzplan-erstellen/')],
}
SERIES=[
 ('hypothekenradar','Hypotheken-Radar','Monatlich','smzhub-serie-hypotheken-radar','immobilien',
   'Monatliche Einschätzung zu Zinsen, Festhypotheken und Schweizer Hypothekarmarkt.'),
 ('investment-guide','Investment Guide','Monatlich','smzhub-serie-investment-guide','kapitalmaerkte',
   'Monatliche Anlageeinschätzung – Märkte, Strategie und Portfoliothemen.'),
 ('immobilien-outlook','Immobilien-Outlook','Quartalsweise','smzhub-serie-immobilien-outlook','immobilien',
   'Quartalsweise Analyse des Schweizer Immobilienmarkts.'),
]
SERIES_BY={k:(name,cad,slug,theme,desc) for k,name,cad,slug,theme,desc in SERIES}
SERIES_FOR={'immobilien':['hypothekenradar','immobilien-outlook'],'kapitalmaerkte':['investment-guide'],'vorsorge':[],'steuern':[]}
ITEM_BY_PATH={r['path']:r for r in rows}
# Kuratierte Dossiers (Storyline aus bestehenden, realen Seiten)
DOSSIERS={
 'eigenheim':{'tab':'eigenheim','title':'Eigenheim finanzieren','kicker':'Dossier · Immobilien',
   'intro':'Von der ersten Idee bis zur Bankzusage: Dieser Leitfaden bündelt die wichtigsten Schritte zu Kauf, Tragbarkeit, Eigenkapital und Hypothek – in der richtigen Reihenfolge.',
   'flagship':'hypothekenradar','rubric':'immobilien',
   'steps':[
     ('Einstieg','de/wie-kaufe-ich-eine-immobilie/','Wie kaufe ich eine Immobilie?','Der Ablauf vom Suchen bis zum Notariat – worauf es Schritt für Schritt ankommt.'),
     ('Tragbarkeit','de/optimierung-der-tragbarkeit/','Tragbarkeit optimieren','Wie die Bank Ihr Einkommen rechnet – und was Sie beeinflussen können.'),
     ('Finanzierung','de/hypothekenarten-im-vergleich/','Hypothekenarten im Vergleich','SARON oder Festhypothek: Laufzeit, Zins und Risiko abwägen.'),
     ('Eigenkapital','de/wohneigentumsfoerderung/','Wohneigentumsförderung','Säule 3a und Pensionskasse fürs Eigenheim einsetzen.'),
   ]},
 'pensionierung':{'tab':'zukunft','title':'Pensionierung planen','kicker':'Dossier · Vorsorge',
   'intro':'AHV, Pensionskasse und Säule 3a greifen ineinander. Dieser rote Faden führt von den Grundlagen bis zur grossen Entscheidung: Rente oder Kapital.',
   'flagship':None,'rubric':'vorsorge',
   'steps':[
     ('Grundlagen','de/das-3-saeulensystem-der-schweiz/','Das 3-Säulen-System','Wie die Schweizer Vorsorge aufgebaut ist und ineinandergreift.'),
     ('Säule 3a','de/altersvorsorge-optimierung-saeule-3a/','Säule 3a optimal nutzen','Steuern sparen und Vorsorgelücken frühzeitig schliessen.'),
     ('Planung','de/pensionsplanung/','Pensionsplanung','Rechtzeitig die Weichen für den Ruhestand stellen.'),
     ('Leistungen','de/leistungen-im-alter/','Leistungen im Alter','Was Sie aus AHV und Pensionskasse konkret erwarten können.'),
   ]},
}
DOSSIER_SLUG={'eigenheim':'smzhub-dossier-eigenheim','pensionierung':'smzhub-dossier-pensionierung'}

CTA_PATH={'vorsorgeanalyse':'de/vorsorgeanalyse/','immobilienbewertung':'de/immobilienbewertung/',
          'steuererklaerung':'de/steuererklaerung/','terminvereinbaren':'de/terminvereinbaren/'}

# Entscheidungs-Einstiege (Kategorie, Frage, Kurztext, Ziel, Backend-Rubrik)
DECISIONS=[
 ('Hypothek','SARON oder Festhypothek?','Welche Laufzeit passt, wenn Zinsen tief bleiben, aber Planungssicherheit zählt?','de/hypothekenarten-im-vergleich/','immobilien'),
 ('Eigenheim','Kaufen oder warten?','Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenhängen.','de/wie-kaufe-ich-eine-immobilie/','immobilien'),
 ('Eigenheim','Reicht mein Einkommen?','Tragbarkeit verstehen, bevor die Bank Nein sagt.','de/optimierung-der-tragbarkeit/','immobilien'),
 ('Anlegen','3a-Konto oder Wertschriften?','Warum Sparen allein über lange Zeiträume oft nicht genügt.','de/altersvorsorge-optimierung-saeule-3a/','kapitalmaerkte'),
 ('Anlegen','Wie lege ich richtig an?','Vom Risikoprofil zur passenden Anlagestrategie.','de/anlagestrategie/','kapitalmaerkte'),
 ('Vorsorge','Rente oder Kapital?','Die Pensionierungsentscheidung, die selten sauber vorbereitet wird.','de/leistungen-im-alter/','vorsorge'),
 ('Vorsorge','Vorsorgelücke mit 40+?','Wie Sie Lücken früh erkennen und rechtzeitig schliessen.','de/pensionsplanung/','vorsorge'),
 ('Steuern','Wie senke ich meine Steuern?','Welche Abzüge und Vorsorgebezüge wirklich etwas bringen.','de/steuerabzuege-optimal-nutzen/','steuern'),
]

# ---- Bausteine ----
def section(inner, cls='ed-sec'): return f'<section class="{cls}">{inner}</section>'

def sec_head(title, more_path=None, kicker=None, sub=None, more_label='Zur Rubrik →', extra=''):
    k=f'<span class="ed-kicker">{esc(kicker)}</span>' if kicker else ''
    subh=f'<p class="sh-sub">{esc(sub)}</p>' if sub else ''
    more=f'<a class="ed-sec-more" href="{link(more_path)}">{esc(more_label)}</a>' if more_path else ''
    return f'<div class="ed-sec-head"><div class="ed-sh-l">{k}<h2>{esc(title)}</h2>{subh}</div>{more}{extra}</div>'

def themebar(active):
    items=''
    for k,lbl,path in THEMES:
        cls='tb-link'+(' tb-active' if k==active else '')
        items+=f'<a class="{cls}" href="{link(path)}">{esc(lbl)}</a>'
    return f'<nav class="ed-themebar" aria-label="smzhHub Rubriken"><div class="tb-inner">{items}</div></nav>'

def hero(slider_items):
    slides=''; dots=''
    for i,r in enumerate(slider_items):
        im=img_of(r,1200)
        bg=f'<img src="{im}" alt="">' if im else ''
        chip=(r.get('topics') or [''])[0]
        slides+=(f'<a class="hslide{" active" if i==0 else ""}" href="{link(r["path"])}">'
                 f'<div class="hslide-img">{bg}</div><div class="hslide-grad"></div>'
                 f'<div class="hslide-txt"><span class="hslide-chip">{esc(chip)}</span>'
                 f'<h3>{esc(r["title"])}</h3><p>{esc(teaser(r,120))}</p>'
                 f'<span class="hslide-meta">{fdate(r.get("date"))}</span></div></a>')
        dots+=f'<span class="hdot{" active" if i==0 else ""}" role="button" tabindex="0" aria-label="Beitrag {i+1}"></span>'
    return (f'<section class="ed-hero"><div class="hero-intro">'
            f'<span class="hero-eyebrow">smzhHub · Research & Orientierung</span>'
            f'<h1>Finanzwissen, das Entscheidungen einfacher macht.</h1>'
            f'<p>Einordnungen, Ratgeber und wiederkehrendes Research von smzh zu Eigenheim, '
            f'Vermögen, Vorsorge und Steuern – damit Sie wissen, was Ihre nächste Entscheidung wirklich bedeutet.</p>'
            f'<div class="hero-cta"><a class="hero-btn" href="#ed-decisions">Entscheidung finden</a>'
            f'<a class="hero-link" href="#ed-sections">Themen entdecken ↓</a></div></div>'
            f'<div class="hero-feature hslider"><div class="hslides">{slides}</div>'
            f'<span class="harrow hprev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
            f'<span class="harrow hnext" role="button" tabindex="0" aria-label="Weiter">›</span>'
            f'<div class="hdots">{dots}</div></div></section>')

def decision_carousel(decs=None, title='Entscheiden statt nur informieren',
                      sub='Die wichtigsten Finanzfragen sind selten Wissensfragen, sondern Entscheidungen unter Unsicherheit. Hier finden Sie den passenden Einstieg.'):
    decs=decs or DECISIONS
    cards=''
    for cat,q,desc,tail,rub in decs:
        if not exists(tail): continue
        cards+=(f'<a class="dc-card" href="{link(tail)}"><span class="dc-cat">{esc(cat)}</span>'
                f'<span class="dc-q">{esc(q)}</span><span class="dc-d">{esc(desc)}</span>'
                f'<span class="dc-go">Einstieg →</span><span class="dc-deco"></span></a>')
    nav=('<div class="dc-nav"><span class="dc-arrow dc-prev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
         '<span class="dc-arrow dc-next" role="button" tabindex="0" aria-label="Weiter">›</span></div>')
    head=sec_head(title, sub=sub, kicker='Entscheiden', extra=nav)
    return (f'<section class="ed-sec dc-sec" id="ed-decisions">{head}'
            f'<div class="dc-carousel"><div class="dc-viewport"><div class="dc-track">{cards}</div></div></div></section>')

def side_item(r, tag=None):
    im=img_of(r,640)
    thumb=f'<span class="es-thumb"><img loading="lazy" src="{im}" alt=""></span>' if im else '<span class="es-thumb es-thumb-empty"></span>'
    tagh=f'<span class="es-tag">{esc(tag)}</span>' if tag else ''
    cls='es-item'+(' es-serie' if tag else '')
    return (f'<a class="{cls}" href="{link(r["path"])}">{thumb}<span class="es-it-txt">'
            f'{tagh}<span class="es-h4">{esc(r["title"])}</span>'
            f'<span class="es-p">{esc(teaser(r,80))}</span></span></a>')

def ph_item(ph):
    if ph.get('status')=='real' and ph.get('url'):
        href=link(ph['url']); tag=f'{esc(ph["contentType"])}'; tagcls='es-tag'; thumb='⤳'
    else:
        href=link(CTA_PATH.get(ph.get('ctaType'),'de/terminvereinbaren/'))
        tag=f'In Vorbereitung · {esc(ph["contentType"])}'; tagcls='es-tag es-tag-ph'; thumb='→'
    cls='es-item'+('' if ph.get('status')=='real' else ' es-ph')
    return (f'<a class="{cls}" href="{href}"><span class="es-thumb es-thumb-ph">{thumb}</span>'
            f'<span class="es-it-txt"><span class="{tagcls}">{tag}</span>'
            f'<span class="es-h4">{esc(ph["title"])}</span>'
            f'<span class="es-p">{esc(teaser(ph,80))}</span></span></a>')

def meta_label(r):
    if r.get('series') in SERIES_BY:
        nm=SERIES_BY[r['series']][0]
        return nm+(f' · {r["readingTime"]} Min' if r.get('readingTime') else '')
    parts=[fdate(r.get('date'))]
    if r.get('readingTime'): parts.append(f'{r["readingTime"]} Min')
    return ' · '.join(p for p in parts if p)

def lead_card(lead, kicker):
    im=img_of(lead,1200)
    leadimg=f'<div class="el-img"><img loading="lazy" src="{im}" alt=""></div>' if im else ''
    return (f'<a class="ed-lead" href="{link(lead["path"])}">{leadimg}<div class="el-txt">'
            f'<span class="es-chip">{esc(kicker)}</span><h3>{esc(lead["title"])}</h3>'
            f'<p>{esc(teaser(lead,190))}</p><span class="el-meta">{esc(meta_label(lead))}</span></div></a>')

def rubric_footer(cta, ph_id=None):
    cl,cp=cta
    extra=''
    if ph_id and ph_id in PH_BY:
        ph=PH_BY[ph_id]
        if ph.get('status')=='real' and ph.get('url'):
            extra=(f'<a class="rub-dossier" href="{link(ph["url"])}">'
                   f'<span class="rub-dossier-tag rub-dossier-real">Dossier</span>{esc(ph["title"])} →</a>')
        else:
            extra=(f'<a class="rub-dossier" href="{link(CTA_PATH.get(ph.get("ctaType"),"de/terminvereinbaren/"))}">'
                   f'<span class="rub-dossier-tag">In Vorbereitung</span>{esc(ph["title"])} →</a>')
    return (f'<div class="rub-foot"><span class="rub-foot-l"><span class="rub-foot-k">Nächster Schritt</span>'
            f'<a class="rub-cta" href="{link(cp)}">{esc(cl)} →</a></span>{extra}</div>')

def home_rubric(tab, title, kicker, ph_id, used):
    rkey=TAB_RUBRIC[tab]; intro,anchors,cta=TAB_META[tab]
    pool=[r for r in lead_rubric(rkey) if r['id'] not in used]
    if not pool: return ''
    lead=pool[0]; used.add(lead['id'])
    sides=[]
    for s in anchors[:1]:
        its=series_items(s)
        if its and its[0]['id'] not in used:
            sides.append((its[0], f'{SERIES_BY[s][1]} · Serie')); used.add(its[0]['id'])
    for r in pool[1:]:
        if len(sides)>=3: break
        used.add(r['id']); sides.append((r,None))
    body=(f'<div class="ed-sec-body"><div class="ed-lead-wrap">{lead_card(lead,kicker)}</div>'
          f'<div class="ed-side">{"".join(side_item(r,t) for r,t in sides)}</div></div>')
    head=sec_head(title, THEME_BY[tab][1], sub=intro, more_label='Zur Rubrik →')
    return section(head+body+rubric_footer(cta,ph_id))

def home_steuern():
    rkey='steuern'; intro,anchors,cta=TAB_META['steuern']
    leads=lead_rubric(rkey)[:1]; komm=komm_rubric(rkey)
    if not leads and not komm: return ''
    lead=leads[0] if leads else komm[0]
    rest=[r for r in komm if r['id']!=lead['id']][:3]
    guides=''.join(f'<a class="cg-pill" href="{link(t)}">{esc(l)}</a>' for l,t in EVERGREEN['steuern'][:4] if exists(t))
    resthtml=''.join(side_item(r) for r in rest)
    ph=PH_BY.get('ph-guide-steuern-pensionierung')
    phh=ph_item(ph) if ph else ''
    head=sec_head('Steuern & Planung', THEME_BY['steuern'][1], sub=intro, kicker='Kompakt', more_label='Zur Rubrik →')
    body=(f'<div class="cg-wrap"><div class="cg-main">{lead_card(lead,"Analyse")}'
          f'<div class="cg-pills">{guides}</div></div>'
          f'<div class="ed-side">{resthtml}{phh}</div></div>')
    return section(head+body+rubric_footer(cta,None))

def research_band(keys=None, heading='Flagship-Research', thumbs=True, more_path='de/smzhub-research/'):
    keys=[k for k in (keys or [s[0] for s in SERIES]) if k in SERIES_BY]
    if not keys: return ''
    rr=''
    for key in keys:
        name,cad,slug,theme,desc=SERIES_BY[key]
        its=series_items(key)
        if not its: continue
        cur=its[0]; im=img_of(cur,640)
        cover=''
        if thumbs and im:
            cover=f'<span class="rsb-cover"><img loading="lazy" src="{im}" alt=""></span>'
        elif thumbs:
            cover='<span class="rsb-cover"></span>'
        rr+=(f'<a class="rsb-row" href="{link("de/"+slug+"/")}">{cover}'
             f'<span class="rsb-cad">{esc(cad)} · {len(its)} Ausgaben</span>'
             f'<span class="rsb-main"><span class="rsb-name">{esc(name)}</span>'
             f'<span class="rsb-desc">{esc(desc)}</span>'
             f'<span class="rsb-cur">Aktuell: {esc(cur["title"])}</span></span>'
             f'<span class="rsb-go">Zur Serie →</span></a>')
    more=f'<a class="ed-sec-more" href="{link(more_path)}">Alle Publikationen →</a>' if more_path else ''
    head=(f'<div class="ed-sec-head"><div class="ed-sh-l"><span class="ed-kicker">Research</span>'
          f'<h2>{esc(heading)}</h2><p class="sh-sub">Wiederkehrende Einschätzungen mit eigener Serienidentität – '
          f'fundiert, ruhig und auf den Punkt.</p></div>{more}</div>')
    return section(head+f'<div class="rsb-list rsb-thumbs">{rr}</div>', cls='ed-sec rsb-sec')

def cta(label, path, big=True):
    return (f'<section class="ed-cta"><div><h2>{esc(label)}?</h2>'
            f'<p>Wir begleiten Sie persönlich – unabhängig, diskret und auf Ihre Situation zugeschnitten.</p></div>'
            f'<a class="ed-cta-btn" href="{link(path)}">{esc(label)}</a></section>')

# ---- Seiten ----
def home_inner():
    hero_items=hero_picks()
    used=set(r['id'] for r in hero_items)
    out=[themebar('aktuell'), hero(hero_items), decision_carousel(), '<div id="ed-sections">']
    for tab,title,kicker,ph_id in HOME_RUBRICS:
        out.append(home_rubric(tab,title,kicker,ph_id,used))
    out.append(home_steuern())
    out.append('</div>')
    out.append(research_band())
    out.append(cta('Persönliche Beratung','de/terminvereinbaren/'))
    return ''.join(out)

def rubric_body(rkey, kicker, anchors, used, n_anchors):
    pool=[r for r in lead_rubric(rkey) if r['id'] not in used]
    if not pool: return ''
    lead=pool[0]; used.add(lead['id'])
    sides=[]
    for s in anchors[:n_anchors]:
        its=series_items(s)
        if its and its[0]['id'] not in used:
            sides.append((its[0], f'{SERIES_BY[s][1]} · Serie')); used.add(its[0]['id'])
    for r in pool[1:]:
        if len(sides)>=3: break
        used.add(r['id']); sides.append((r,None))
    return (f'<div class="ed-sec-body"><div class="ed-lead-wrap">{lead_card(lead,kicker)}</div>'
            f'<div class="ed-side">{"".join(side_item(r,t) for r,t in sides)}</div></div>')

def guides_band(rkey):
    pills=''.join(f'<a class="cg-pill" href="{link(t)}">{esc(l)}</a>' for l,t in EVERGREEN.get(rkey,[]) if exists(t))
    if not pills: return ''
    return section('<div class="ed-sec-head"><div class="ed-sh-l"><span class="ed-kicker">Grundlagen</span>'
                   '<h2>Guides & Evergreens</h2></div></div>'+f'<div class="cg-pills cg-pills-lg">{pills}</div>')

def theme_inner(tab):
    lbl,path=THEME_BY[tab]; rkey=TAB_RUBRIC[tab]
    intro,anchors,cta_pair=TAB_META[tab]
    used=set()
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>{esc(lbl)}</nav>'
    hero=(f'<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
          f'<span class="ed-kicker">Rubrik</span><h1>{esc(lbl)}</h1><p>{esc(intro)}</p>'
          f'<div class="hero-cta"><a class="hero-btn" href="{link(cta_pair[1])}">{esc(cta_pair[0])}</a></div></div></section>')
    # themenspezifische Entscheidungen
    decs=[d for d in DECISIONS if d[4]==rkey]
    decmod=decision_carousel(decs, title='Ihre Entscheidung', sub='Konkrete Fragen, konkrete Einstiege.') if len(decs)>=1 else ''
    body=rubric_body(rkey,'Leitartikel',anchors,used,n_anchors=len(anchors) or 1)
    mod=section(sec_head('Im Fokus',kicker='Redaktion')+body+rubric_footer(cta_pair,None)) if body else ''
    band=research_band(anchors, heading='Relevantes Research', more_path='de/smzhub-research/') if anchors else ''
    rest=[r for r in komm_rubric(rkey) if r['id'] not in used][:8]
    morehtml=(section(sec_head('Weitere Beiträge')+'<div class="es-grid">'+''.join(side_item(r) for r in rest)+'</div>')
              if rest else '')
    guides=guides_band(rkey)
    # echte Dossiers dieser Rubrik
    dos=[p for p in PH if p.get('primaryRubric')==rkey and p.get('status')=='real']
    doshtml=''
    if dos:
        doshtml=section('<div class="ed-sec-head"><div class="ed-sh-l"><span class="ed-kicker">Dossier</span>'
                        '<h2>Roter Faden zum Thema</h2></div></div><div class="es-grid">'+''.join(ph_item(p) for p in dos)+'</div>')
    # Platzhalter dieser Rubrik
    phs=[p for p in PH if p.get('primaryRubric')==rkey and p.get('status')!='real']
    phhtml=''
    if phs:
        phhtml=section('<div class="ed-sec-head"><div class="ed-sh-l"><span class="ed-kicker">Demnächst</span>'
                       '<h2>In Vorbereitung</h2></div></div><div class="es-grid">'+''.join(ph_item(p) for p in phs)+'</div>')
    return themebar(tab)+crumb+hero+decmod+mod+doshtml+band+morehtml+guides+phhtml+cta(cta_pair[0],cta_pair[1])

def dossier_inner(dkey):
    d=DOSSIERS[dkey]; tab=d['tab']; rkey=d['rubric']
    lbl=THEME_BY[tab][1]
    cta_pair=TAB_META[tab][2]
    crumb=(f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>'
           f'<a href="{link(THEME_BY[tab][1])}">{esc(THEME_BY[tab][0])}</a><span>/</span>Dossier</nav>')
    hero=(f'<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
          f'<span class="ed-kicker">{esc(d["kicker"])}</span><h1>{esc(d["title"])}</h1><p>{esc(d["intro"])}</p>'
          f'<div class="hero-cta"><a class="hero-btn" href="{link(cta_pair[1])}">{esc(cta_pair[0])}</a></div></div></section>')
    # Storyline-Schritte (kuratierte reale Seiten)
    steps=list(d['steps'])
    # dynamischer Abschluss-Schritt: aktuellster Kommentar der Rubrik
    lr=lead_rubric(rkey)
    if lr:
        cur=lr[0]
        steps=steps+[('Aktuell', cur['path'].strip('/'), cur['title'], teaser(cur,110))]
    items=''
    n=0
    for kicker,path,fallback_title,fallback_teaser in steps:
        if not exists(path): continue
        n+=1
        it=ITEM_BY_PATH.get('/'+path.strip('/')+'/')
        title=it['title'] if it else fallback_title
        tz=teaser(it,120) if it else fallback_teaser
        items+=(f'<a class="dos-step" href="{link(path)}"><span class="dos-num">{n}</span>'
                f'<span class="dos-txt"><span class="dos-kicker">{esc(kicker)}</span>'
                f'<span class="dos-h">{esc(title)}</span><span class="dos-p">{esc(tz)}</span></span>'
                f'<span class="dos-go">→</span></a>')
    story=section(sec_head('Der rote Faden',kicker='Storyline')+f'<div class="dos-steps">{items}</div>')
    band=research_band([d['flagship']], heading='Vertiefendes Research', more_path='de/smzhub-research/') if d.get('flagship') else ''
    return themebar(tab)+crumb+hero+story+band+cta(cta_pair[0],cta_pair[1])

def research_inner():
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>Research</nav>'
    hero=('<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
          '<span class="ed-kicker">Research & Publikationen</span><h1>Das smzh-Research</h1>'
          '<p>Drei wiederkehrende Flagship-Formate liefern regelmässig fundierte Einschätzungen zu '
          'Hypotheken, Märkten und dem Schweizer Immobilienmarkt – mit aktueller Ausgabe und vollständigem Archiv.</p></div></section>')
    band=research_band(heading='Unsere Flagship-Formate', more_path=None)
    return themebar('research')+crumb+hero+band+cta('Beratung vereinbaren','de/terminvereinbaren/')

def series_inner(key):
    name,cad,slug,theme,desc=SERIES_BY[key]
    items=series_items(key); cur=items[0] if items else None
    crumb=(f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>'
           f'<a href="{link("de/smzhub-research/")}">Research</a><span>/</span>{esc(name)}</nav>')
    hero=(f'<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
          f'<span class="ed-kicker">{esc(cad)} · Serie</span><h1>{esc(name)}</h1><p>{esc(desc)}</p></div></section>')
    cur_html=''
    if cur:
        im=img_of(cur,1200); cover=f'<div class="el-img"><img src="{im}" alt=""></div>' if im else ''
        pdf=f'<a class="rs-pdf" href="{P_}../cms.smzh.ch/uploads/{cur["pdfs"][0]}" target="_blank" rel="noopener">PDF ansehen</a>' if cur.get('pdfs') else ''
        cur_html=(f'<section class="ed-sec"><div class="ed-sec-head"><div class="ed-sh-l"><span class="ed-kicker">Aktuelle Ausgabe</span><h2>{esc(cur["title"])}</h2></div></div>'
                  f'<a class="ed-lead" href="{link(cur["path"])}">{cover}<div class="el-txt">'
                  f'<span class="es-chip">{esc(fdate(cur.get("date")))}</span>'
                  f'<p>{esc(teaser(cur,220))}</p><span class="el-actions"><span class="ed-cta-btn ed-cta-inline">Lesen</span>{pdf}</span></div></a></section>')
    arch=''
    for r in items[1:]:
        pdf=f'<a class="arch-pdf" href="{P_}../cms.smzh.ch/uploads/{r["pdfs"][0]}" target="_blank" rel="noopener">PDF</a>' if r.get('pdfs') else ''
        arch+=(f'<a class="arch-row" href="{link(r["path"])}"><time>{esc(fdate(r.get("date")))}</time>'
               f'<span class="arch-title">{esc(r["title"])}</span>{pdf}</a>')
    arch_html=(f'<section class="ed-rubric"><div class="ed-rub-head"><span class="ed-kicker">Archiv</span>'
               f'<h2>Frühere Ausgaben ({len(items)-1})</h2></div><div class="arch-list">{arch}</div></section>') if len(items)>1 else ''
    return themebar('research')+crumb+hero+cur_html+arch_html+cta('Beratung vereinbaren','de/terminvereinbaren/')

def archiv_inner(orig_inner):
    body=re.sub(r'<section id="smzh-research".*?</section>','',orig_inner,flags=re.S)
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>Alle Inhalte</nav>'
    intro='<section class="ed-hero ed-hero-theme"><div class="hero-intro"><span class="ed-kicker">Archiv</span><h1>Alle Inhalte</h1><p>Das vollständige Verzeichnis aller Beiträge, Publikationen, Talks und Podcasts.</p></div></section>'
    return themebar(None)+crumb+intro+body

ED_CSS = '''<style id="smzh-ed-css">
#ed-root{--brand:#07314C;--accent:#0050ff;--gold:#b07d1e;--muted:#5b6b7a;--faint:#9aa7b2;--line:#e7ebef;--bg:#f4f7fa}
#ed-root{gap:0 !important}
#ed-root section{margin:0 0 4rem}
#ed-root .ed-kicker{display:inline-block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:.4rem}
/* Sticky Reiter */
#ed-root .ed-themebar{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.96);backdrop-filter:blur(8px);margin:0 0 2.4rem;border-bottom:1px solid var(--line)}
#ed-root .tb-inner{display:flex;gap:2rem;min-width:max-content;padding:.2rem 0}
#ed-root .tb-link{padding:.9rem 0;color:var(--muted);text-decoration:none;font-weight:500;font-size:1.02rem;white-space:nowrap;border-bottom:2px solid transparent;transition:.15s}
#ed-root .tb-link:hover{color:var(--brand)}
#ed-root .tb-active{color:var(--brand);font-weight:700;border-bottom-color:var(--accent)}
@media(max-width:760px){#ed-root .ed-themebar{overflow-x:auto}}
/* Hero */
#ed-root .ed-hero{display:grid;grid-template-columns:1fr;gap:2rem;align-items:center;margin-bottom:4rem}
@media(min-width:900px){#ed-root .ed-hero{grid-template-columns:0.86fr 1.14fr;gap:3rem}}
#ed-root .hero-eyebrow{display:inline-block;font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:800;margin-bottom:.8rem}
#ed-root .hero-intro h1{font-size:clamp(2rem,4.4vw,3.4rem);font-weight:700;color:var(--brand);line-height:1.07;margin:0 0 1rem;letter-spacing:-.01em}
#ed-root .hero-intro p{font-size:clamp(1.05rem,1.6vw,1.22rem);color:var(--muted);margin:0 0 1.6rem;max-width:48ch;line-height:1.55}
#ed-root .hero-cta{display:flex;align-items:center;gap:1.3rem;flex-wrap:wrap}
#ed-root .hero-btn{background:var(--brand);color:#fff;font-weight:700;text-decoration:none;padding:.85rem 1.6rem;border-radius:10px}
#ed-root .hero-btn:hover{background:#0b4366}
#ed-root .hero-link{color:var(--accent);font-weight:600;text-decoration:none}
#ed-root .ed-hero-theme{display:block;margin-bottom:3rem;padding-top:.5rem}
#ed-root .ed-hero-theme h1{max-width:20ch}
#ed-root .hero-feature{position:relative;border-radius:18px;overflow:hidden;aspect-ratio:16/11;box-shadow:0 24px 60px rgba(7,49,76,.18);background:#dfe6ec}
#ed-root .hslides,#ed-root .hslide{position:absolute;inset:0}
#ed-root .hslide{display:block;opacity:0;transition:opacity .6s ease;text-decoration:none;pointer-events:none}
#ed-root .hslide.active{opacity:1;pointer-events:auto}
#ed-root .hslide-img,#ed-root .hslide-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#ed-root .hslide-grad{position:absolute;inset:0;background:linear-gradient(to top,rgba(4,22,38,.92) 0%,rgba(4,22,38,.45) 38%,rgba(4,22,38,0) 68%)}
#ed-root .hslide-txt{position:absolute;left:0;right:0;bottom:0;padding:2rem 2.2rem;color:#fff}
#ed-root .hslide-chip{display:inline-block;background:rgba(255,255,255,.18);backdrop-filter:blur(4px);color:#fff;font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;padding:.3rem .7rem;border-radius:999px;margin-bottom:.7rem}
#ed-root .hslide-txt h3{font-size:clamp(1.3rem,2.4vw,1.95rem);font-weight:700;margin:0 0 .5rem;line-height:1.18}
#ed-root .hslide-txt p{margin:0 0 .5rem;color:#dce6ee;font-size:.98rem;max-width:48ch}
#ed-root .hslide-meta{font-size:.8rem;color:#aebecb}
#ed-root .harrow{position:absolute;top:50%;transform:translateY(-50%);z-index:4;width:42px;height:42px;border-radius:50%;border:none;background:rgba(255,255,255,.85);color:var(--brand);font-size:1.4rem;line-height:1;cursor:pointer;display:flex;align-items:center;justify-content:center;opacity:0;transition:.2s}
#ed-root .hero-feature:hover .harrow{opacity:1}
#ed-root .hprev{left:14px}#ed-root .hnext{right:14px}
#ed-root .hdots{position:absolute;bottom:1.1rem;right:1.4rem;z-index:4;display:flex;gap:.45rem}
#ed-root .hdot{width:8px;height:8px;border-radius:50%;border:none;background:rgba(255,255,255,.45);cursor:pointer;padding:0}
#ed-root .hdot.active{background:#fff;width:22px;border-radius:5px}
/* Section-Head */
#ed-root .ed-sec-head{display:flex;align-items:flex-start;justify-content:space-between;gap:1.4rem;margin-bottom:1.6rem;border-top:1px solid var(--line);padding-top:1.4rem}
#ed-root .ed-sh-l{display:flex;flex-direction:column;gap:.15rem}
#ed-root .ed-sec-head h2{font-size:clamp(1.5rem,2.6vw,2.05rem);font-weight:700;color:var(--brand);margin:0}
#ed-root .sh-sub{color:var(--muted);margin:.4rem 0 0;font-size:1rem;max-width:64ch;line-height:1.5}
#ed-root .ed-sec-more{color:var(--accent);font-weight:600;text-decoration:none;white-space:nowrap;font-size:.95rem;padding-top:.3rem}
/* Entscheidungs-Karussell */
#ed-root .dc-nav{display:flex;gap:.55rem;align-items:center;flex:0 0 auto}
#ed-root .dc-arrow{width:46px;height:46px;border-radius:50%;border:1px solid var(--line);background:#fff;color:var(--brand);font-size:1.5rem;line-height:1;display:flex;align-items:center;justify-content:center;cursor:pointer;transition:.15s;user-select:none}
#ed-root .dc-arrow:hover{border-color:var(--accent);color:var(--accent);box-shadow:0 6px 16px rgba(7,49,76,.08)}
#ed-root .dc-viewport{overflow:hidden}
#ed-root .dc-track{display:flex;gap:1.1rem;transition:transform .45s ease;will-change:transform}
#ed-root .dc-card{position:relative;overflow:hidden;display:flex;flex-direction:column;gap:.5rem;background:#fff;border:1px solid var(--line);border-radius:14px;padding:1.5rem 1.4rem 1.6rem;text-decoration:none;transition:.18s;flex:0 0 100%}
@media(min-width:560px){#ed-root .dc-card{flex-basis:calc((100% - 1.1rem)/2)}}
@media(min-width:980px){#ed-root .dc-card{flex-basis:calc((100% - 3.3rem)/4)}}
#ed-root .dc-card:hover{box-shadow:0 16px 36px rgba(7,49,76,.10);transform:translateY(-3px);border-color:#d4dde4}
#ed-root .dc-cat{font-size:.68rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--accent)}
#ed-root .dc-q{font-size:1.2rem;font-weight:800;color:var(--brand);line-height:1.2}
#ed-root .dc-d{font-size:.86rem;color:var(--muted);line-height:1.5;flex:1}
#ed-root .dc-go{font-size:.8rem;font-weight:700;color:var(--accent);margin-top:.3rem}
#ed-root .dc-deco{position:absolute;right:-24px;bottom:-24px;width:74px;height:74px;border-radius:50%;background:linear-gradient(135deg,rgba(0,80,255,.10),rgba(7,49,76,.04))}
/* Rubrik: Leitartikel + Begleitung */
#ed-root .ed-sec-body,#ed-root .cg-wrap{display:grid;grid-template-columns:1fr;gap:1.8rem}
@media(min-width:900px){#ed-root .ed-sec-body,#ed-root .cg-wrap{grid-template-columns:1.45fr 1fr;gap:2.4rem}}
#ed-root .ed-lead{display:block;text-decoration:none;color:inherit}
#ed-root .el-img{aspect-ratio:4/3;border-radius:14px;overflow:hidden;background:var(--bg);margin-bottom:1.1rem}
#ed-root .el-img img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
#ed-root .ed-lead:hover .el-img img{transform:scale(1.03)}
#ed-root .es-chip{display:inline-block;color:var(--accent);font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.5rem}
#ed-root .el-txt h3{font-size:clamp(1.4rem,2.4vw,1.95rem);font-weight:700;color:var(--brand);margin:0 0 .6rem;line-height:1.18}
#ed-root .el-txt p{color:var(--muted);margin:0 0 .6rem;line-height:1.55}
#ed-root .el-meta{color:var(--faint);font-size:.82rem;font-weight:600}
#ed-root .ed-side{display:flex;flex-direction:column;gap:1rem}
#ed-root .es-item{display:flex;gap:1rem;align-items:center;padding:.9rem;border:1px solid var(--line);border-radius:12px;text-decoration:none;color:inherit;background:#fff;transition:.15s}
#ed-root .es-item:hover{border-color:#d4dde4;box-shadow:0 8px 20px rgba(7,49,76,.06)}
#ed-root .es-serie{border-left:3px solid var(--gold)}
#ed-root .es-ph{border-style:dashed;background:#fbfcfd}
#ed-root .es-thumb{flex:0 0 96px;width:96px;height:72px;border-radius:8px;overflow:hidden;background:var(--bg)}
#ed-root .es-thumb img{width:100%;height:100%;object-fit:cover}
#ed-root .es-thumb-ph{display:flex;align-items:center;justify-content:center;color:var(--faint);font-size:1.5rem;background:#eef2f6}
#ed-root .es-it-txt{display:flex;flex-direction:column;gap:.22rem}
#ed-root .es-tag{display:inline-block;font-size:.6rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--gold);background:#f6ead2;padding:.13rem .45rem;border-radius:4px;width:max-content}
#ed-root .es-tag-ph{color:#6b7785;background:#e7edf2}
#ed-root .es-h4{font-weight:650;color:var(--brand);line-height:1.3;font-size:1rem}
#ed-root .es-item:hover .es-h4{color:var(--accent)}
#ed-root .es-p{color:var(--muted);font-size:.85rem;line-height:1.45}
#ed-root .es-grid{display:grid;grid-template-columns:1fr;gap:1rem}
@media(min-width:640px){#ed-root .es-grid{grid-template-columns:1fr 1fr}}
/* Rubrik-Footer (Lead-Pfad) */
#ed-root .rub-foot{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1rem;margin-top:1.6rem;padding:1.1rem 1.4rem;background:var(--bg);border-radius:12px}
#ed-root .rub-foot-l{display:flex;align-items:center;gap:1rem}
#ed-root .rub-foot-k{font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);font-weight:800}
#ed-root .rub-cta{color:var(--brand);font-weight:700;text-decoration:none;font-size:1rem}
#ed-root .rub-cta:hover{color:var(--accent)}
#ed-root .rub-dossier{color:var(--muted);text-decoration:none;font-size:.88rem;font-weight:600;display:inline-flex;align-items:center;gap:.5rem}
#ed-root .rub-dossier:hover{color:var(--brand)}
#ed-root .rub-dossier-tag{font-size:.6rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#6b7785;background:#e7edf2;padding:.13rem .45rem;border-radius:4px}
#ed-root .rub-dossier-real{color:var(--gold);background:#f6ead2}
/* Dossier-Storyline */
#ed-root .dos-steps{display:flex;flex-direction:column;position:relative}
#ed-root .dos-steps:before{content:"";position:absolute;left:21px;top:28px;bottom:28px;width:2px;background:var(--line)}
#ed-root .dos-step{display:flex;gap:1.2rem;align-items:flex-start;padding:1rem 1.1rem;text-decoration:none;position:relative;z-index:1;border:1px solid transparent;border-radius:12px;transition:.15s}
#ed-root .dos-step:hover{border-color:var(--line);background:#fff;box-shadow:0 8px 20px rgba(7,49,76,.05)}
#ed-root .dos-num{flex:0 0 44px;width:44px;height:44px;border-radius:50%;background:var(--brand);color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:1.05rem}
#ed-root .dos-txt{flex:1;display:flex;flex-direction:column;gap:.2rem;padding-top:.15rem}
#ed-root .dos-kicker{font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--accent)}
#ed-root .dos-h{font-weight:700;color:var(--brand);font-size:1.1rem;line-height:1.25}
#ed-root .dos-step:hover .dos-h{color:var(--accent)}
#ed-root .dos-p{color:var(--muted);font-size:.88rem;line-height:1.45}
#ed-root .dos-go{color:var(--accent);font-weight:800;font-size:1.2rem;align-self:center}
/* Kompakt-Guides (Steuern) */
#ed-root .cg-main{display:flex;flex-direction:column;gap:1rem}
#ed-root .cg-pills{display:flex;flex-wrap:wrap;gap:.6rem}
#ed-root .cg-pill{display:inline-block;padding:.5rem .9rem;border:1px solid var(--line);border-radius:999px;color:var(--brand);text-decoration:none;font-size:.86rem;font-weight:600;background:#fff;transition:.15s}
#ed-root .cg-pill:hover{border-color:var(--accent);color:var(--accent)}
#ed-root .cg-pills-lg .cg-pill{padding:.7rem 1.2rem;font-size:.95rem}
/* Research-Band */
#ed-root .rsb-list{display:flex;flex-direction:column;gap:.8rem}
#ed-root .rsb-row{display:flex;align-items:center;gap:1.3rem;padding:1.1rem 1.4rem;border:1px solid var(--line);border-radius:14px;text-decoration:none;background:#fff;transition:.15s}
#ed-root .rsb-row:hover{border-color:var(--accent);box-shadow:0 10px 26px rgba(7,49,76,.07)}
#ed-root .rsb-cover{flex:0 0 100px;width:100px;height:68px;border-radius:8px;overflow:hidden;background:var(--bg)}
#ed-root .rsb-cover img{width:100%;height:100%;object-fit:cover}
#ed-root .rsb-cad{flex:0 0 150px;font-size:.66rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:var(--faint)}
#ed-root .rsb-main{flex:1;display:flex;flex-direction:column;gap:.18rem}
#ed-root .rsb-name{font-weight:800;color:var(--brand);font-size:1.15rem}
#ed-root .rsb-desc{color:var(--muted);font-size:.85rem;line-height:1.4}
#ed-root .rsb-cur{color:var(--faint);font-size:.82rem;margin-top:.1rem}
#ed-root .rsb-go{color:var(--accent);font-weight:700;white-space:nowrap;font-size:.92rem}
@media(max-width:760px){#ed-root .rsb-cad{display:none}#ed-root .rsb-cover{flex-basis:74px;width:74px;height:56px}}
/* Serien-Archiv */
#ed-root .ed-rubric{background:var(--bg);border-radius:18px;padding:2.2rem}
#ed-root .ed-rub-head{margin-bottom:1.2rem}
#ed-root .ed-rub-head h2{font-size:clamp(1.3rem,2.2vw,1.7rem);font-weight:700;color:var(--brand);margin:0}
#ed-root .arch-list{display:flex;flex-direction:column}
#ed-root .arch-row{display:flex;align-items:center;gap:1.2rem;padding:1rem .2rem;border-bottom:1px solid var(--line);text-decoration:none;color:var(--brand)}
#ed-root .arch-row time{flex:0 0 88px;color:var(--faint);font-size:.85rem}
#ed-root .arch-title{flex:1;font-weight:600}
#ed-root .arch-row:hover .arch-title{color:var(--accent)}
#ed-root .arch-pdf,#ed-root .rs-pdf{color:var(--accent);font-weight:600;text-decoration:none;font-size:.85rem}
/* CTA */
#ed-root .ed-cta{display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;justify-content:space-between;background:var(--brand);border-radius:18px;padding:2.6rem}
#ed-root .ed-cta h2{color:#fff;margin:0 0 .3rem;font-size:1.7rem}
#ed-root .ed-cta p{color:#c7d6e2;margin:0;max-width:54ch}
#ed-root .ed-cta-btn{background:#fff;color:var(--brand);font-weight:700;text-decoration:none;padding:.95rem 1.8rem;border-radius:10px;white-space:nowrap}
#ed-root .el-actions{display:flex;align-items:center;gap:1.2rem;margin-top:.4rem}
#ed-root .ed-cta-inline{display:inline-block;padding:.7rem 1.4rem}
#ed-root .ed-crumb{font-size:.85rem;color:var(--faint);margin:1rem 0 .5rem}
#ed-root .ed-crumb a{color:var(--accent);text-decoration:none}#ed-root .ed-crumb span{margin:0 .4rem}
</style>'''

SLIDER_JS = '''<script id="smzh-ed-js">
(function(){function ready(f){if(document.readyState!=='loading'){f();}else{document.addEventListener('DOMContentLoaded',f);}}
ready(function(){
document.querySelectorAll('.hslider').forEach(function(s){
var sl=s.querySelectorAll('.hslide'),dt=s.querySelectorAll('.hdot'),i=0,n=sl.length,t=null;
if(n<2){return;}
function go(k){i=(k+n)%n;sl.forEach(function(e,j){e.classList.toggle('active',j===i);});dt.forEach(function(d,j){d.classList.toggle('active',j===i);});}
function auto(){t=setInterval(function(){go(i+1);},6500);}function reset(){clearInterval(t);auto();}
var nx=s.querySelector('.hnext'),pv=s.querySelector('.hprev');
if(nx)nx.addEventListener('click',function(e){e.preventDefault();go(i+1);reset();});
if(pv)pv.addEventListener('click',function(e){e.preventDefault();go(i-1);reset();});
dt.forEach(function(d,j){d.addEventListener('click',function(e){e.preventDefault();go(j);reset();});});
s.addEventListener('mouseenter',function(){clearInterval(t);});s.addEventListener('mouseleave',auto);
go(0);auto();});
document.querySelectorAll('.dc-sec').forEach(function(c){
var track=c.querySelector('.dc-track');if(!track)return;var cards=track.children,n=cards.length,i=0;
var prev=c.querySelector('.dc-prev'),next=c.querySelector('.dc-next');
function vis(){var w=c.clientWidth;return w<560?1:(w<980?2:4);}
function maxI(){return Math.max(0,n-vis());}
function step(){if(!n)return 0;var cs=getComputedStyle(track);var g=parseFloat(cs.columnGap||cs.gap||0)||0;return cards[0].getBoundingClientRect().width+g;}
function go(k){var m=maxI();i=k<0?m:(k>m?0:k);track.style.transform='translateX('+(-i*step())+'px)';}
if(next)next.addEventListener('click',function(e){e.preventDefault();go(i+1);});
if(prev)prev.addEventListener('click',function(e){e.preventDefault();go(i-1);});
var rt;window.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(function(){go(Math.min(i,maxI()));},150);});
go(0);});
});})();
</script>'''

def balanced_div_end(s, start):
    depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>', s[start:]):
        depth+= 1 if m.group(1)=='' else -1
        if depth==0: return start+m.end()
    return -1

def main():
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*"', html)
    openTagEnd=html.index('>',m.start())+1
    closeEnd=balanced_div_end(html, m.start())
    chrome_before=html[:openTagEnd]; chrome_after=html[closeEnd-6:]
    orig_inner=html[openTagEnd:closeEnd-6]
    if 'id="smzh-ed-css"' not in chrome_before:
        chrome_before=chrome_before.replace('</head>', ED_CSS+'</head>',1)
    chrome_before=re.sub(r'(<div class="content-hub[^"]*")', r'\1 id="ed-root"', chrome_before, count=1)
    if 'id="smzh-ed-js"' not in chrome_after:
        chrome_after=chrome_after.replace('</body>', SLIDER_JS+'</body>',1)

    def write(path, inner, title):
        full=chrome_before+inner+chrome_after
        full=re.sub(r'<title>.*?</title>', '<title>'+H.escape(title)+'</title>', full, count=1, flags=re.S)
        d=os.path.join(SMZH,path.strip('/')); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)

    import shutil
    for old in ['smzhub-kapitalmaerkte','smzhub-immobilien','smzhub-vorsorge']:
        shutil.rmtree(os.path.join(SMZH,'de',old), ignore_errors=True)

    write('de/smzhub/', home_inner(), 'smzHub – Finanzwissen für Ihre Entscheidungen')
    write('de/smzhub-eigenheim/', theme_inner('eigenheim'), 'Eigenheim – smzHub')
    write('de/smzhub-vermoegen/', theme_inner('vermoegen'), 'Vermögen – smzHub')
    write('de/smzhub-zukunft/', theme_inner('zukunft'), 'Zukunft – smzHub')
    write('de/smzhub-steuern/', theme_inner('steuern'), 'Steuern – smzHub')
    write('de/smzhub-research/', research_inner(), 'Research & Publikationen – smzHub')
    for dkey,slug in DOSSIER_SLUG.items():
        write('de/'+slug+'/', dossier_inner(dkey), f'{DOSSIERS[dkey]["title"]} – smzHub Dossier')
    for k,name,cad,slug,theme,desc in SERIES:
        write('de/'+slug+'/', series_inner(k), f'{name} – smzHub')
    write('de/smzhub-archiv/', archiv_inner(orig_inner), 'Alle Inhalte – smzHub')
    print('OK: Hybrid Hub – Home, 4 Rubriken, Research, 3 Serien, Archiv.')

if __name__=='__main__':
    main()
