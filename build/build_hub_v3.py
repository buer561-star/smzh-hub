#!/usr/bin/env python3
"""smzhHub V3 – modernes digitales Advisory- & Research-Interface.
Kein Magazin/Serif/Creme. Weiss + Navy, Sans, klare Linien, funktionale Module:
Intelligence Hero (Current-Signals-Panel) · Decision Matrix · Advisory Journeys
· Research Signal Band · CTA Panel. Daten aus build/smzhhub-content.json.
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
def fdate(iso, short=False):
    if not iso: return ''
    try:
        d=datetime.fromisoformat(iso.replace('Z','+00:00'))
        return (f"{d.day:02d}.{d.month:02d}.{d.year}" if short else f"{MON[d.strftime('%b')]} {d.year}")
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
def imgt(im,cls=''): return f'<img loading="lazy" src="{im}" alt="" class="{cls}">' if im else ''

def komm_rubric(key):
    out=[r for r in rows if r.get('rubric')==key and r['hubType']=='kommentar' and r.get('hubEligible')]
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)
def lead_rubric(key):
    out=[r for r in rows if r.get('rubric')==key and r.get('leadEligible')]
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)
def series_items(key): return sorted([r for r in rows if r.get('series')==key], key=lambda r:r.get('date') or '', reverse=True)
def latest_month():
    ds=[r['date'] for r in rows if r.get('date')]
    return fdate(max(ds)) if ds else ''
def signals():
    best=[]
    for key in ['immobilien','kapitalmaerkte','vorsorge']:
        ls=lead_rubric(key)
        if ls: best.append(ls[0])
    best.sort(key=lambda r:r.get('date') or '', reverse=True)
    return best[:3]

# ---- Konfig ----
NAV=[('aktuell','Aktuell','de/smzhub/'),('eigenheim','Eigenheim','de/smzhub-eigenheim/'),
     ('vermoegen','Vermögen','de/smzhub-vermoegen/'),('zukunft','Zukunft','de/smzhub-zukunft/'),
     ('steuern','Steuern','de/smzhub-steuern/'),('research','Research','de/smzhub-research/')]
NAV_BY={k:(l,p) for k,l,p in NAV}
TAB_RUBRIC={'eigenheim':'immobilien','vermoegen':'kapitalmaerkte','zukunft':'vorsorge','steuern':'steuern'}
CAT={'immobilien':'Eigenheim','kapitalmaerkte':'Vermögen','vorsorge':'Zukunft','steuern':'Steuern'}
TAB_INTRO={'eigenheim':'Kaufen, finanzieren und halten – Hypothek, Tragbarkeit und Immobilienmarkt klar eingeordnet.',
 'vermoegen':'Märkte, Zinsen und Portfolios verständlich – ohne tägliches Börsenrauschen.',
 'zukunft':'AHV, Pensionskasse und Säule 3a – damit aus Unsicherheit ein konkreter Plan wird.',
 'steuern':'Steuern senken und Vermögen klug strukturieren – konkret und planbar.'}
TAB_CTA={'eigenheim':('Hypothek prüfen lassen','de/immobilienbewertung/'),
 'vermoegen':('Anlagestrategie besprechen','de/terminvereinbaren/'),
 'zukunft':('Vorsorge analysieren','de/vorsorgeanalyse/'),
 'steuern':('Steuern optimieren','de/steuererklaerung/')}
JQ={'eigenheim':'Kann ich mir mein Eigenheim leisten – und zu welchen Konditionen?',
 'vermoegen':'Wie lege ich mein Vermögen sinnvoll und ruhig an?',
 'zukunft':'Reicht mein Geld bis zur und in der Pensionierung?',
 'steuern':'Wo lasse ich jedes Jahr unnötig Steuern liegen?'}
JFLAG={'eigenheim':['hypothekenradar','immobilien-outlook'],'vermoegen':['investment-guide'],'zukunft':[],'steuern':[]}
JDOSSIER={'eigenheim':'ph-dossier-eigenheim','zukunft':'ph-dossier-pensionierung'}
SERIES=[('hypothekenradar','Hypotheken-Radar','Monatlich','smzhub-serie-hypotheken-radar','immobilien','Zinsen, Festhypotheken und Schweizer Hypothekarmarkt.'),
 ('investment-guide','Investment Guide','Monatlich','smzhub-serie-investment-guide','kapitalmaerkte','Märkte, Strategie und Portfoliothemen.'),
 ('immobilien-outlook','Immobilien-Outlook','Quartalsweise','smzhub-serie-immobilien-outlook','immobilien','Analyse des Schweizer Immobilienmarkts.')]
SERIES_BY={k:(name,cad,slug,theme,desc) for k,name,cad,slug,theme,desc in SERIES}
DECISIONS=[('SARON oder Festhypothek?','Welche Laufzeit passt, wenn Zinsen tief bleiben, aber Sicherheit zählt?','eigenheim','de/hypothekenarten-im-vergleich/'),
 ('Kaufen oder warten?','Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenspielen.','eigenheim','de/wie-kaufe-ich-eine-immobilie/'),
 ('Reicht mein Einkommen?','Tragbarkeit verstehen, bevor die Bank Nein sagt.','eigenheim','de/optimierung-der-tragbarkeit/'),
 ('Rente oder Kapital?','Die Pensionierungsentscheidung, die selten sauber vorbereitet wird.','zukunft','de/leistungen-im-alter/'),
 ('3a-Konto oder Wertschriften?','Warum Sparen allein über lange Zeiträume selten genügt.','vermoegen','de/altersvorsorge-optimierung-saeule-3a/'),
 ('Wie senke ich meine Steuern?','Welche Abzüge und Vorsorgebezüge wirklich etwas bringen.','steuern','de/steuerabzuege-optimal-nutzen/')]
CTA_PATH={'vorsorgeanalyse':'de/vorsorgeanalyse/','immobilienbewertung':'de/immobilienbewertung/',
 'steuererklaerung':'de/steuererklaerung/','terminvereinbaren':'de/terminvereinbaren/'}
ITEM_BY_PATH={r['path']:r for r in rows}

# ---- Module ----
def hubbar():
    return (f'<div class="v3-bar"><span class="v3-brand">smzhHub</span>'
            f'<span class="v3-brand-tag">Research &amp; Advisory</span>'
            f'<span class="v3-bar-upd"><i class="v3-pulse"></i>Aktualisiert {esc(latest_month())}</span></div>')

def rubricnav(active):
    items=''
    for k,l,p in NAV:
        cls='v3-tab'+(' is-active' if k==active else '')
        items+=f'<a class="{cls}" href="{link(p)}">{esc(l)}</a>'
    return f'<nav class="v3-nav" aria-label="smzhHub Rubriken"><div class="v3-nav-in">{items}</div></nav>'

def signal_row(r):
    return (f'<a class="v3-sig-row" href="{link(r["path"])}">'
            f'<span class="v3-sig-date">{esc(fdate(r.get("date"),short=True))}</span>'
            f'<span class="v3-sig-body"><span class="v3-chip v3-chip-{r.get("rubric") or "x"}">{esc(CAT.get(r.get("rubric"),"smzh"))}</span>'
            f'<span class="v3-sig-t">{esc(r["title"])}</span></span><span class="v3-sig-arr">→</span></a>')

def intelligence_hero():
    sigs=signals()
    sg=''.join(signal_row(r) for r in sigs)
    total=len(rows); nser=len(SERIES)
    return (f'<section class="v3-hero">'
            f'<div class="v3-hero-l"><span class="v3-eyebrow">Der Finanz- &amp; Beratungshub von smzh</span>'
            f'<h1 class="v3-hero-h1">Klarheit für Ihre nächste Finanzentscheidung.</h1>'
            f'<p class="v3-hero-sub">smzhHub bündelt Einschätzungen, Ratgeber und wiederkehrendes Research zu '
            f'Eigenheim, Vermögen, Vorsorge und Steuern – strukturiert nach Ihren Fragen, nicht nach Fachabteilung.</p>'
            f'<div class="v3-hero-cta"><a class="v3-btn" href="#v3-decide">Entscheidung finden</a>'
            f'<a class="v3-btn-2" href="#v3-journeys">Themen ansehen</a></div>'
            f'<div class="v3-hero-stats"><span><b>{total}</b> Beiträge</span><span><b>{nser}</b> Research-Reihen</span>'
            f'<span><b>monatlich</b> aktualisiert</span></div></div>'
            f'<aside class="v3-signals"><div class="v3-signals-head"><span class="v3-live"><i class="v3-pulse"></i>Aktuelle Einschätzungen</span>'
            f'<span class="v3-signals-stand">{esc(latest_month())}</span></div>'
            f'<div class="v3-signals-list">{sg}</div>'
            f'<a class="v3-signals-more" href="{link("de/smzhub-archiv/")}">Alle Beiträge ansehen →</a></aside></section>')

def decision_matrix():
    body=''
    for q,prob,tab,tail in DECISIONS:
        if not exists(tail): continue
        body+=(f'<a class="v3-mx-row" href="{link(tail)}">'
               f'<span class="v3-mx-q">{esc(q)}</span>'
               f'<span class="v3-mx-prob">{esc(prob)}</span>'
               f'<span class="v3-chip v3-chip-{TAB_RUBRIC.get(tab,"x")}">{esc(NAV_BY[tab][0])}</span>'
               f'<span class="v3-mx-step">Einstieg <i>→</i></span></a>')
    return (f'<section class="v3-block" id="v3-decide"><div class="v3-sec-head">'
            f'<div><span class="v3-eyebrow">Decision Matrix</span><h2 class="v3-h2">Entscheiden statt nur informieren</h2>'
            f'<p class="v3-sec-sub">Die wichtigsten Finanzfragen sind Entscheidungen unter Unsicherheit. '
            f'Wählen Sie Ihre Frage – wir liefern den passenden Einstieg.</p></div></div>'
            f'<div class="v3-matrix"><div class="v3-mx-head"><span>Entscheidungsfrage</span><span>Worum es geht</span>'
            f'<span>Rubrik</span><span></span></div>{body}</div></section>')

def jr_item(r):
    return (f'<a class="v3-jr-item" href="{link(r["path"])}"><span class="v3-jr-it-t">{esc(r["title"])}</span>'
            f'<span class="v3-jr-it-m">{esc(fdate(r.get("date")))}'
            +(f' · {r["readingTime"]} Min' if r.get("readingTime") else '')+'</span></a>')

def anchor_chip(skey):
    name,cad,slug,theme,desc=SERIES_BY[skey]
    return (f'<a class="v3-anchor" href="{link("de/"+slug+"/")}"><span class="v3-anchor-k">Flagship · {esc(cad)}</span>'
            f'<span class="v3-anchor-n">{esc(name)} <i>→</i></span></a>')

def dossier_chip(ph_id):
    ph=PH_BY.get(ph_id)
    if not ph or ph.get('status')!='real' or not ph.get('url'): return ''
    return (f'<a class="v3-anchor v3-anchor-dos" href="{link(ph["url"])}"><span class="v3-anchor-k">Dossier · Storyline</span>'
            f'<span class="v3-anchor-n">{esc(ph["title"])} <i>→</i></span></a>')

def advisory_journey(tab):
    rk=TAB_RUBRIC[tab]; lbl,path=NAV_BY[tab]; cl,cp=TAB_CTA[tab]
    pool=lead_rubric(rk)
    if not pool: return ''
    items=''.join(jr_item(r) for r in pool[:4])
    anchors=''.join(anchor_chip(s) for s in JFLAG.get(tab,[]))
    if tab in JDOSSIER: anchors+=dossier_chip(JDOSSIER[tab])
    anchor_html=f'<div class="v3-anchors">{anchors}</div>' if anchors else ''
    return (f'<section class="v3-journey v3-acc-{tab}">'
            f'<div class="v3-jr-rail"><span class="v3-jr-label">{esc(lbl)}</span>'
            f'<h3 class="v3-jr-q">{esc(JQ[tab])}</h3>'
            f'<p class="v3-jr-intro">{esc(TAB_INTRO[tab])}</p>{anchor_html}'
            f'<a class="v3-jr-cta" href="{link(cp)}">{esc(cl)} <i>→</i></a></div>'
            f'<div class="v3-jr-content"><div class="v3-jr-c-head"><span class="v3-eyebrow">Wichtigste Inhalte</span>'
            f'<a class="v3-jr-all" href="{link(path)}">Ganze Rubrik →</a></div>'
            f'<div class="v3-jr-list">{items}</div></div></section>')

def sig_card(skey):
    name,cad,slug,theme,desc=SERIES_BY[skey]
    its=series_items(skey)
    if not its: return ''
    cur=its[0]; im=img_of(cur,640)
    cover=f'<span class="v3-sc-cover">{imgt(im)}</span>' if im else '<span class="v3-sc-cover"></span>'
    return (f'<a class="v3-sc" href="{link("de/"+slug+"/")}">'
            f'<div class="v3-sc-top">{cover}<div class="v3-sc-meta"><span class="v3-badge">{esc(cad)}</span>'
            f'<span class="v3-sc-count">{len(its)} Ausgaben</span></div></div>'
            f'<span class="v3-sc-name">{esc(name)}</span><span class="v3-sc-desc">{esc(desc)}</span>'
            f'<span class="v3-sc-latest"><span class="v3-sc-lk">Aktuelle Ausgabe</span>{esc(cur["title"])}</span>'
            f'<span class="v3-sc-go">Serie ansehen <i>→</i></span></a>')

def research_band():
    cards=''.join(sig_card(s[0]) for s in SERIES)
    return (f'<section class="v3-block v3-research"><div class="v3-sec-head">'
            f'<div><span class="v3-eyebrow">Research Signals</span><h2 class="v3-h2">Wiederkehrende Einschätzungen von smzh</h2>'
            f'<p class="v3-sec-sub">Drei institutionelle Flagship-Formate – regelmässig, fundiert, mit eigener Serienidentität.</p></div>'
            f'<a class="v3-sec-more" href="{link("de/smzhub-research/")}">Alle Publikationen →</a></div>'
            f'<div class="v3-sig-cards">{cards}</div></section>')

def cta_panel(label='Persönliche Beratung', path='de/terminvereinbaren/'):
    return (f'<section class="v3-cta"><div class="v3-cta-l"><h2 class="v3-cta-h">Ihre Situation verdient mehr als einen Standardrat.</h2>'
            f'<p>Wir begleiten Sie persönlich – unabhängig, diskret und auf Ihre Situation zugeschnitten.</p></div>'
            f'<a class="v3-btn v3-btn-light" href="{link(path)}">{esc(label)} →</a></section>')

# ---- Seiten ----
def home_inner():
    return (hubbar()+rubricnav('aktuell')+intelligence_hero()+decision_matrix()
            +'<div id="v3-journeys">'+advisory_journey('eigenheim')+advisory_journey('vermoegen')+advisory_journey('zukunft')+'</div>'
            +research_band()+cta_panel())

def teaser_card(r):
    im=img_of(r,640)
    cov=f'<span class="v3-tc-img">{imgt(im)}</span>' if im else ''
    return (f'<a class="v3-tc" href="{link(r["path"])}">{cov}<span class="v3-tc-b">'
            f'<span class="v3-chip v3-chip-{r.get("rubric") or "x"}">{esc(CAT.get(r.get("rubric"),"smzh"))}</span>'
            f'<span class="v3-tc-t">{esc(r["title"])}</span>'
            f'<span class="v3-tc-m">{esc(fdate(r.get("date")))}'
            +(f' · {r["readingTime"]} Min' if r.get("readingTime") else '')+'</span></span></a>')

def rubric_page(tab):
    rk=TAB_RUBRIC[tab]; lbl,path=NAV_BY[tab]; cl,cp=TAB_CTA[tab]
    crumb=f'<nav class="v3-crumb"><a href="{link("de/smzhub/")}">smzhHub</a><span>/</span>{esc(lbl)}</nav>'
    head=(f'<header class="v3-phead"><div><span class="v3-eyebrow">Rubrik</span>'
          f'<h1 class="v3-phead-h">{esc(lbl)}</h1><p class="v3-phead-sub">{esc(TAB_INTRO[tab])}</p></div>'
          f'<a class="v3-btn" href="{link(cp)}">{esc(cl)} →</a></header>')
    jr=advisory_journey(tab)
    decs=[d for d in DECISIONS if d[2]==tab]
    decmod=''
    if decs:
        body=''.join(f'<a class="v3-mx-row" href="{link(t)}"><span class="v3-mx-q">{esc(q)}</span>'
                     f'<span class="v3-mx-prob">{esc(pr)}</span><span class="v3-chip v3-chip-{rk}">{esc(lbl)}</span>'
                     f'<span class="v3-mx-step">Einstieg <i>→</i></span></a>' for q,pr,tb,t in decs if exists(t))
        decmod=f'<section class="v3-block"><div class="v3-sec-head"><div><span class="v3-eyebrow">Decision Matrix</span><h2 class="v3-h2">Ihre Entscheidungen</h2></div></div><div class="v3-matrix">{body}</div></section>'
    used={r['id'] for r in lead_rubric(rk)[:4]}
    more=[r for r in komm_rubric(rk) if r['id'] not in used][:6]
    moreh=''
    if more:
        moreh=('<section class="v3-block"><div class="v3-sec-head"><div><span class="v3-eyebrow">Weiterlesen</span>'
               '<h2 class="v3-h2">Weitere Beiträge</h2></div></div><div class="v3-tc-grid">'+''.join(teaser_card(r) for r in more)+'</div></section>')
    band=research_band() if JFLAG.get(tab) else ''
    return hubbar()+rubricnav(tab)+crumb+head+decmod+jr+band+moreh+cta_panel(cl,cp)

def research_page():
    crumb=f'<nav class="v3-crumb"><a href="{link("de/smzhub/")}">smzhHub</a><span>/</span>Research</nav>'
    head=('<header class="v3-phead"><div><span class="v3-eyebrow">Research &amp; Publikationen</span>'
          '<h1 class="v3-phead-h">Das smzh-Research</h1><p class="v3-phead-sub">Drei wiederkehrende Flagship-Formate '
          'liefern regelmässig fundierte Einschätzungen – mit aktueller Ausgabe und vollständigem Archiv.</p></div></header>')
    return hubbar()+rubricnav('research')+crumb+head+research_band()+cta_panel('Beratung vereinbaren','de/terminvereinbaren/')

def series_page(skey):
    name,cad,slug,theme,desc=SERIES_BY[skey]; its=series_items(skey); cur=its[0] if its else None
    crumb=(f'<nav class="v3-crumb"><a href="{link("de/smzhub/")}">smzhHub</a><span>/</span>'
           f'<a href="{link("de/smzhub-research/")}">Research</a><span>/</span>{esc(name)}</nav>')
    head=(f'<header class="v3-phead"><div><span class="v3-eyebrow">{esc(cad)} · Serie</span>'
          f'<h1 class="v3-phead-h">{esc(name)}</h1><p class="v3-phead-sub">{esc(desc)}</p></div></header>')
    cur_html=''
    if cur:
        im=img_of(cur,640); cov=f'<span class="v3-cur-img">{imgt(im)}</span>' if im else ''
        pdf=f'<a class="v3-pdf" href="{P_}../cms.smzh.ch/uploads/{cur["pdfs"][0]}" target="_blank" rel="noopener">PDF ansehen</a>' if cur.get('pdfs') else ''
        cur_html=(f'<section class="v3-block"><div class="v3-sec-head"><div><span class="v3-eyebrow">Aktuelle Ausgabe</span>'
                  f'<h2 class="v3-h2">{esc(cur["title"])}</h2></div></div>'
                  f'<a class="v3-cur" href="{link(cur["path"])}">{cov}<span class="v3-cur-b"><span class="v3-cur-date">{esc(fdate(cur.get("date")))}</span>'
                  f'<p>{esc(teaser(cur,180))}</p><span class="v3-cur-go">Ausgabe lesen →</span></span></a>'
                  +(f'<div class="v3-cur-actions">{pdf}</div>' if pdf else '')+'</section>')
    arch=''
    for r in its[1:]:
        pdf=f'<a class="v3-pdf" href="{P_}../cms.smzh.ch/uploads/{r["pdfs"][0]}" target="_blank" rel="noopener">PDF</a>' if r.get('pdfs') else ''
        arch+=(f'<a class="v3-arch-row" href="{link(r["path"])}"><span class="v3-arch-d">{esc(fdate(r.get("date")))}</span>'
               f'<span class="v3-arch-t">{esc(r["title"])}</span>{pdf}</a>')
    arch_html=(f'<section class="v3-block"><div class="v3-sec-head"><div><span class="v3-eyebrow">Archiv</span>'
               f'<h2 class="v3-h2">Frühere Ausgaben ({len(its)-1})</h2></div></div><div class="v3-arch">{arch}</div></section>') if len(its)>1 else ''
    return hubbar()+rubricnav('research')+crumb+head+cur_html+arch_html+cta_panel('Beratung vereinbaren','de/terminvereinbaren/')

DOSSIER_STEPS={'eigenheim':[('Einstieg','de/wie-kaufe-ich-eine-immobilie/','Wie kaufe ich eine Immobilie?'),
   ('Tragbarkeit','de/optimierung-der-tragbarkeit/','Tragbarkeit optimieren'),
   ('Finanzierung','de/hypothekenarten-im-vergleich/','Hypothekenarten im Vergleich'),
   ('Eigenkapital','de/wohneigentumsfoerderung/','Wohneigentumsförderung')],
 'pensionierung':[('Grundlagen','de/das-3-saeulensystem-der-schweiz/','Das 3-Säulen-System'),
   ('Säule 3a','de/altersvorsorge-optimierung-saeule-3a/','Säule 3a optimal nutzen'),
   ('Planung','de/pensionsplanung/','Pensionsplanung'),
   ('Leistungen','de/leistungen-im-alter/','Leistungen im Alter')]}
def dossier_page(dkey):
    cfg={'eigenheim':('eigenheim','immobilien','Eigenheim finanzieren','Von der ersten Idee bis zur Bankzusage: der strukturierte Pfad zu Kauf, Tragbarkeit, Eigenkapital und Hypothek.',['hypothekenradar']),
         'pensionierung':('zukunft','vorsorge','Pensionierung planen','AHV, Pensionskasse und Säule 3a greifen ineinander – vom Grundlagenwissen bis zur Entscheidung Rente oder Kapital.',[])}[dkey]
    tab,rk,title,intro,flags=cfg; cl,cp=TAB_CTA[tab]
    crumb=(f'<nav class="v3-crumb"><a href="{link("de/smzhub/")}">smzhHub</a><span>/</span>'
           f'<a href="{link(NAV_BY[tab][1])}">{esc(NAV_BY[tab][0])}</a><span>/</span>Dossier</nav>')
    head=(f'<header class="v3-phead"><div><span class="v3-eyebrow">Dossier · Storyline</span>'
          f'<h1 class="v3-phead-h">{esc(title)}</h1><p class="v3-phead-sub">{esc(intro)}</p></div>'
          f'<a class="v3-btn" href="{link(cp)}">{esc(cl)} →</a></header>')
    steps=list(DOSSIER_STEPS[dkey]); lr=lead_rubric(rk)
    if lr: steps=steps+[('Aktuell', lr[0]['path'].strip('/'), lr[0]['title'])]
    body=''; n=0
    for kicker,pth,fb in steps:
        if not exists(pth): continue
        n+=1
        it=ITEM_BY_PATH.get('/'+pth.strip('/')+'/'); title2=it['title'] if it else fb; tz=teaser(it,120) if it else ''
        body+=(f'<a class="v3-step" href="{link(pth)}"><span class="v3-step-n">{n}</span>'
               f'<span class="v3-step-b"><span class="v3-step-k">{esc(kicker)}</span>'
               f'<span class="v3-step-t">{esc(title2)}</span><span class="v3-step-p">{esc(tz)}</span></span>'
               f'<span class="v3-step-arr">→</span></a>')
    story=f'<section class="v3-block"><div class="v3-sec-head"><div><span class="v3-eyebrow">Der Pfad</span><h2 class="v3-h2">Schritt für Schritt</h2></div></div><div class="v3-steps">{body}</div></section>'
    band=research_band() if flags else ''
    return hubbar()+rubricnav(tab)+crumb+head+story+band+cta_panel(cl,cp)

def archiv_inner(orig_inner):
    body=re.sub(r'<section id="smzh-research".*?</section>','',orig_inner,flags=re.S)
    crumb=f'<nav class="v3-crumb"><a href="{link("de/smzhub/")}">smzhHub</a><span>/</span>Alle Inhalte</nav>'
    head=('<header class="v3-phead"><div><span class="v3-eyebrow">Archiv</span>'
          '<h1 class="v3-phead-h">Alle Inhalte</h1><p class="v3-phead-sub">Das vollständige Verzeichnis aller '
          'Beiträge, Publikationen, Talks und Podcasts.</p></div></header>')
    return hubbar()+rubricnav(None)+crumb+head+body

V3_CSS = '''<style id="smzh-v3-css">
#ed-root{--brand:#07314C;--ink:#0f2231;--blue:#0050ff;--muted:#5b6b7a;--faint:#8b9aa8;--line:#e4e9ee;--surf:#f5f8fb;--surf2:#eef3f8;--ok:#1f9d7a;--eh:#07314C;--ve:#0050ff;--zu:#1f7a6b;--st:#9a6b18;max-width:1240px}
#ed-root{gap:0 !important;padding-top:0 !important;color:var(--ink)}
#ed-root *{box-sizing:border-box}
#ed-root section,#ed-root header{margin:0}
#ed-root .v3-eyebrow{display:inline-block;font-size:.7rem;letter-spacing:.13em;text-transform:uppercase;font-weight:700;color:var(--blue)}
#ed-root .v3-h2{font-size:clamp(1.4rem,2.4vw,1.85rem);font-weight:700;color:var(--brand);margin:.4rem 0 .3rem;letter-spacing:-.01em}
#ed-root .v3-sec-sub{color:var(--muted);margin:0;max-width:62ch;line-height:1.5;font-size:.98rem}
/* Bar */
#ed-root .v3-bar{display:flex;align-items:center;gap:.8rem;padding:1rem 0 .9rem;border-bottom:1px solid var(--line)}
#ed-root .v3-brand{font-weight:800;font-size:1.15rem;color:var(--brand);letter-spacing:-.02em}
#ed-root .v3-brand-tag{font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);font-weight:700;border-left:1px solid var(--line);padding-left:.8rem}
#ed-root .v3-bar-upd{margin-left:auto;font-size:.74rem;color:var(--muted);font-weight:600;display:inline-flex;align-items:center;gap:.5rem}
#ed-root .v3-pulse{width:7px;height:7px;border-radius:50%;background:var(--ok);box-shadow:0 0 0 0 rgba(31,157,122,.5);animation:v3p 2.4s infinite}
@keyframes v3p{0%{box-shadow:0 0 0 0 rgba(31,157,122,.45)}70%{box-shadow:0 0 0 7px rgba(31,157,122,0)}100%{box-shadow:0 0 0 0 rgba(31,157,122,0)}}
/* Nav */
#ed-root .v3-nav{position:sticky;top:0;z-index:30;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);margin-bottom:2.4rem}
#ed-root .v3-nav-in{display:flex;gap:.3rem;overflow-x:auto}
#ed-root .v3-tab{padding:.95rem 1.1rem;color:var(--muted);text-decoration:none;font-weight:600;font-size:.96rem;white-space:nowrap;border-bottom:2px solid transparent;transition:.12s}
#ed-root .v3-tab:hover{color:var(--brand);background:var(--surf)}
#ed-root .v3-tab.is-active{color:var(--brand);border-bottom-color:var(--blue)}
/* Intelligence Hero */
#ed-root .v3-hero{display:grid;grid-template-columns:1fr;gap:2rem;padding:1.4rem 0 3rem;margin-bottom:3rem;border-bottom:1px solid var(--line)}
@media(min-width:920px){#ed-root .v3-hero{grid-template-columns:1.05fr .95fr;gap:3.4rem;align-items:start}}
#ed-root .v3-hero-h1{font-size:clamp(1.9rem,3.6vw,2.9rem);font-weight:800;line-height:1.08;letter-spacing:-.02em;color:var(--brand);margin:.9rem 0 1rem}
#ed-root .v3-hero-sub{font-size:clamp(1.02rem,1.4vw,1.15rem);color:var(--muted);max-width:50ch;line-height:1.55;margin:0 0 1.6rem}
#ed-root .v3-hero-cta{display:flex;gap:.8rem;flex-wrap:wrap}
#ed-root .v3-btn{display:inline-block;background:var(--brand);color:#fff;font-weight:600;text-decoration:none;padding:.8rem 1.5rem;border-radius:8px;font-size:.96rem;transition:.15s}
#ed-root .v3-btn:hover{background:#0b4569}
#ed-root .v3-btn-2{display:inline-block;color:var(--brand);font-weight:600;text-decoration:none;padding:.8rem 1.2rem;border:1px solid var(--line);border-radius:8px;font-size:.96rem}
#ed-root .v3-btn-2:hover{border-color:var(--brand)}
#ed-root .v3-hero-stats{display:flex;gap:1.8rem;margin-top:1.8rem;padding-top:1.4rem;border-top:1px solid var(--line)}
#ed-root .v3-hero-stats span{font-size:.84rem;color:var(--muted)}
#ed-root .v3-hero-stats b{display:block;font-size:1.3rem;color:var(--brand);font-weight:800;font-variant-numeric:tabular-nums}
/* Current Signals panel */
#ed-root .v3-signals{border:1px solid var(--line);border-radius:14px;background:#fff;box-shadow:0 14px 40px -22px rgba(7,49,76,.35);overflow:hidden}
#ed-root .v3-signals-head{display:flex;align-items:center;justify-content:space-between;padding:1rem 1.2rem;background:var(--surf);border-bottom:1px solid var(--line)}
#ed-root .v3-live{display:inline-flex;align-items:center;gap:.5rem;font-size:.74rem;text-transform:uppercase;letter-spacing:.1em;font-weight:800;color:var(--brand)}
#ed-root .v3-signals-stand{font-size:.74rem;color:var(--faint);font-weight:600}
#ed-root .v3-signals-list{display:flex;flex-direction:column}
#ed-root .v3-sig-row{display:grid;grid-template-columns:auto 1fr auto;gap:.9rem;align-items:center;padding:1rem 1.2rem;border-bottom:1px solid var(--line);text-decoration:none;transition:.12s}
#ed-root .v3-sig-row:hover{background:var(--surf)}
#ed-root .v3-sig-date{font-size:.74rem;color:var(--faint);font-variant-numeric:tabular-nums;font-weight:600;white-space:nowrap}
#ed-root .v3-sig-body{min-width:0}
#ed-root .v3-sig-t{display:block;color:var(--ink);font-weight:600;line-height:1.3;font-size:.96rem;margin-top:.3rem}
#ed-root .v3-sig-row:hover .v3-sig-t{color:var(--blue)}
#ed-root .v3-sig-arr{color:var(--faint);font-size:1.1rem}
#ed-root .v3-signals-more{display:block;padding:.9rem 1.2rem;color:var(--blue);font-weight:700;text-decoration:none;font-size:.88rem}
/* Chips */
#ed-root .v3-chip{display:inline-block;font-size:.64rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:.2rem .5rem;border-radius:5px;background:var(--surf2);color:var(--brand)}
#ed-root .v3-chip-immobilien{background:#e6eef4;color:#07314C}
#ed-root .v3-chip-kapitalmaerkte{background:#e7ecff;color:#1c3bd6}
#ed-root .v3-chip-vorsorge{background:#e2f2ee;color:#15705f}
#ed-root .v3-chip-steuern{background:#f4ecd9;color:#8a5e12}
/* Blocks */
#ed-root .v3-block{margin:0 0 3.4rem}
#ed-root .v3-sec-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1.2rem;margin-bottom:1.4rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
#ed-root .v3-sec-more{color:var(--blue);font-weight:700;text-decoration:none;white-space:nowrap;font-size:.9rem}
/* Decision Matrix */
#ed-root .v3-matrix{border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
#ed-root .v3-mx-head{display:grid;grid-template-columns:1.3fr 1.7fr auto auto;gap:1.2rem;padding:.7rem 1.3rem;background:var(--surf);font-size:.66rem;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);font-weight:800}
#ed-root .v3-mx-row{display:grid;grid-template-columns:1.3fr 1.7fr auto auto;gap:1.2rem;align-items:center;padding:1.05rem 1.3rem;border-top:1px solid var(--line);text-decoration:none;transition:.12s}
#ed-root .v3-mx-row:hover{background:var(--surf)}
#ed-root .v3-mx-q{font-weight:700;color:var(--brand);font-size:1.02rem}
#ed-root .v3-mx-row:hover .v3-mx-q{color:var(--blue)}
#ed-root .v3-mx-prob{color:var(--muted);font-size:.9rem;line-height:1.4}
#ed-root .v3-mx-step{color:var(--blue);font-weight:700;font-size:.88rem;white-space:nowrap}
#ed-root .v3-mx-step i{font-style:normal;transition:.15s;display:inline-block}
#ed-root .v3-mx-row:hover .v3-mx-step i{transform:translateX(4px)}
@media(max-width:760px){#ed-root .v3-mx-head{display:none}
 #ed-root .v3-mx-row{grid-template-columns:1fr;gap:.4rem;padding:1rem 1.1rem}
 #ed-root .v3-mx-prob{order:3}#ed-root .v3-mx-step{order:4}}
/* Advisory Journey */
#ed-root .v3-journey{display:grid;grid-template-columns:1fr;gap:0;border:1px solid var(--line);border-radius:14px;overflow:hidden;margin:0 0 1.6rem;background:#fff}
@media(min-width:880px){#ed-root .v3-journey{grid-template-columns:.95fr 1.05fr}}
#ed-root .v3-jr-rail{padding:1.8rem;background:var(--surf);border-top:3px solid var(--brand);border-right:1px solid var(--line)}
#ed-root .v3-acc-eigenheim .v3-jr-rail{border-top-color:var(--eh)}
#ed-root .v3-acc-vermoegen .v3-jr-rail{border-top-color:var(--ve)}
#ed-root .v3-acc-zukunft .v3-jr-rail{border-top-color:var(--zu)}
#ed-root .v3-acc-steuern .v3-jr-rail{border-top-color:var(--st)}
#ed-root .v3-jr-label{font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;font-weight:800;color:var(--brand)}
#ed-root .v3-jr-q{font-size:1.35rem;font-weight:700;color:var(--brand);line-height:1.18;margin:.5rem 0 .6rem;letter-spacing:-.01em}
#ed-root .v3-jr-intro{color:var(--muted);font-size:.94rem;line-height:1.5;margin:0 0 1.2rem}
#ed-root .v3-anchors{display:flex;flex-direction:column;gap:.6rem;margin-bottom:1.3rem}
#ed-root .v3-anchor{display:block;padding:.7rem .9rem;background:#fff;border:1px solid var(--line);border-radius:9px;text-decoration:none;transition:.12s}
#ed-root .v3-anchor:hover{border-color:var(--blue);box-shadow:0 6px 16px -10px rgba(7,49,76,.4)}
#ed-root .v3-anchor-k{display:block;font-size:.62rem;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);font-weight:800}
#ed-root .v3-anchor-n{display:block;font-weight:700;color:var(--brand);font-size:.96rem;margin-top:.15rem}
#ed-root .v3-anchor i{font-style:normal;color:var(--blue)}
#ed-root .v3-anchor-dos{border-style:dashed}
#ed-root .v3-jr-cta{display:inline-block;color:#fff;background:var(--brand);font-weight:600;text-decoration:none;padding:.7rem 1.3rem;border-radius:8px;font-size:.92rem}
#ed-root .v3-jr-cta:hover{background:#0b4569}#ed-root .v3-jr-cta i{font-style:normal}
#ed-root .v3-jr-content{padding:1.8rem}
#ed-root .v3-jr-c-head{display:flex;align-items:baseline;justify-content:space-between;margin-bottom:.4rem;padding-bottom:.8rem;border-bottom:1px solid var(--line)}
#ed-root .v3-jr-all{color:var(--blue);font-weight:700;text-decoration:none;font-size:.84rem}
#ed-root .v3-jr-list{display:flex;flex-direction:column}
#ed-root .v3-jr-item{display:flex;flex-direction:column;gap:.15rem;padding:.85rem 0;border-bottom:1px solid var(--line);text-decoration:none}
#ed-root .v3-jr-item:last-child{border-bottom:none}
#ed-root .v3-jr-it-t{font-weight:600;color:var(--ink);line-height:1.3;font-size:1rem}
#ed-root .v3-jr-item:hover .v3-jr-it-t{color:var(--blue)}
#ed-root .v3-jr-it-m{font-size:.76rem;color:var(--faint);text-transform:uppercase;letter-spacing:.04em}
/* Research Signal cards */
#ed-root .v3-sig-cards{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:760px){#ed-root .v3-sig-cards{grid-template-columns:1fr 1fr 1fr}}
#ed-root .v3-sc{display:flex;flex-direction:column;gap:.4rem;border:1px solid var(--line);border-radius:12px;padding:1.1rem;text-decoration:none;background:#fff;transition:.15s}
#ed-root .v3-sc:hover{border-color:var(--blue);box-shadow:0 14px 34px -20px rgba(7,49,76,.5);transform:translateY(-2px)}
#ed-root .v3-sc-top{display:flex;align-items:center;gap:.8rem;margin-bottom:.3rem}
#ed-root .v3-sc-cover{flex:0 0 52px;width:52px;height:52px;border-radius:8px;overflow:hidden;background:var(--surf2)}
#ed-root .v3-sc-cover img{width:100%;height:100%;object-fit:cover}
#ed-root .v3-sc-meta{display:flex;flex-direction:column;gap:.25rem}
#ed-root .v3-badge{display:inline-block;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--ok);background:#e2f2ee;padding:.18rem .5rem;border-radius:5px;width:max-content}
#ed-root .v3-sc-count{font-size:.74rem;color:var(--faint);font-weight:600}
#ed-root .v3-sc-name{font-weight:800;color:var(--brand);font-size:1.15rem;letter-spacing:-.01em}
#ed-root .v3-sc-desc{color:var(--muted);font-size:.86rem;line-height:1.45}
#ed-root .v3-sc-latest{display:block;margin-top:.4rem;padding-top:.7rem;border-top:1px solid var(--line);font-size:.84rem;color:var(--ink);font-weight:600;line-height:1.35}
#ed-root .v3-sc-lk{display:block;font-size:.64rem;text-transform:uppercase;letter-spacing:.07em;color:var(--faint);font-weight:800;margin-bottom:.2rem}
#ed-root .v3-sc-go{color:var(--blue);font-weight:700;font-size:.86rem;margin-top:.6rem}
#ed-root .v3-sc-go i{font-style:normal}
/* Teaser cards (rubric "weiterlesen") */
#ed-root .v3-tc-grid{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:640px){#ed-root .v3-tc-grid{grid-template-columns:1fr 1fr}}
@media(min-width:980px){#ed-root .v3-tc-grid{grid-template-columns:1fr 1fr 1fr}}
#ed-root .v3-tc{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;background:#fff;transition:.15s}
#ed-root .v3-tc:hover{border-color:var(--blue);box-shadow:0 14px 34px -20px rgba(7,49,76,.5)}
#ed-root .v3-tc-img{display:block;aspect-ratio:16/9;overflow:hidden;background:var(--surf2)}
#ed-root .v3-tc-img img{width:100%;height:100%;object-fit:cover}
#ed-root .v3-tc-b{display:flex;flex-direction:column;gap:.4rem;padding:1rem 1.1rem 1.2rem}
#ed-root .v3-tc-t{font-weight:700;color:var(--brand);line-height:1.3;font-size:1.02rem}
#ed-root .v3-tc:hover .v3-tc-t{color:var(--blue)}
#ed-root .v3-tc-m{font-size:.76rem;color:var(--faint);text-transform:uppercase;letter-spacing:.04em}
/* CTA Panel */
#ed-root .v3-cta{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1.4rem;background:var(--brand);border-radius:14px;padding:2.2rem 2.4rem;margin-bottom:2rem}
#ed-root .v3-cta-h{color:#fff;font-size:clamp(1.3rem,2.4vw,1.7rem);font-weight:700;margin:0 0 .4rem;max-width:26ch;letter-spacing:-.01em}
#ed-root .v3-cta p{color:#bcd0df;margin:0;max-width:48ch;line-height:1.5}
#ed-root .v3-btn-light{background:#fff;color:var(--brand)}
#ed-root .v3-btn-light:hover{background:#eaf1f6}
/* Rubrik-/Detailseiten */
#ed-root .v3-crumb{font-size:.8rem;color:var(--faint);margin:.2rem 0 1.4rem}
#ed-root .v3-crumb a{color:var(--blue);text-decoration:none}#ed-root .v3-crumb span{margin:0 .45rem}
#ed-root .v3-phead{display:flex;flex-wrap:wrap;align-items:flex-end;justify-content:space-between;gap:1.4rem;padding-bottom:1.8rem;margin-bottom:2.6rem;border-bottom:1px solid var(--line)}
#ed-root .v3-phead-h{font-size:clamp(2rem,4vw,3rem);font-weight:800;color:var(--brand);letter-spacing:-.02em;margin:.6rem 0 .7rem;line-height:1.02}
#ed-root .v3-phead-sub{font-size:1.1rem;color:var(--muted);max-width:52ch;line-height:1.5;margin:0}
/* Dossier steps */
#ed-root .v3-steps{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
#ed-root .v3-step{display:grid;grid-template-columns:auto 1fr auto;gap:1.2rem;align-items:center;padding:1.2rem 1.3rem;border-top:1px solid var(--line);text-decoration:none;transition:.12s}
#ed-root .v3-step:first-child{border-top:none}
#ed-root .v3-step:hover{background:var(--surf)}
#ed-root .v3-step-n{width:34px;height:34px;border-radius:8px;background:var(--surf2);color:var(--brand);font-weight:800;display:flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
#ed-root .v3-step-k{display:block;font-size:.64rem;text-transform:uppercase;letter-spacing:.08em;color:var(--blue);font-weight:800}
#ed-root .v3-step-t{display:block;font-weight:700;color:var(--brand);font-size:1.05rem;margin:.1rem 0}
#ed-root .v3-step:hover .v3-step-t{color:var(--blue)}
#ed-root .v3-step-p{display:block;color:var(--muted);font-size:.86rem;line-height:1.4}
#ed-root .v3-step-arr{color:var(--faint);font-size:1.15rem}
/* Series current + archive */
#ed-root .v3-cur{display:grid;grid-template-columns:1fr;gap:1.2rem;text-decoration:none;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
@media(min-width:640px){#ed-root .v3-cur{grid-template-columns:.5fr 1fr}}
#ed-root .v3-cur-img{background:var(--surf2);overflow:hidden;min-height:160px}
#ed-root .v3-cur-img img{width:100%;height:100%;object-fit:cover}
#ed-root .v3-cur-b{padding:1.4rem 1.5rem}
#ed-root .v3-cur-date{font-size:.72rem;text-transform:uppercase;letter-spacing:.07em;color:var(--faint);font-weight:800}
#ed-root .v3-cur-b p{color:var(--muted);line-height:1.5;margin:.5rem 0 .8rem}
#ed-root .v3-cur-go{color:var(--blue);font-weight:700}
#ed-root .v3-cur-actions{margin-top:.9rem}
#ed-root .v3-pdf{color:var(--blue);font-weight:700;text-decoration:none;font-size:.86rem}
#ed-root .v3-arch{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff}
#ed-root .v3-arch-row{display:grid;grid-template-columns:auto 1fr auto;gap:1.2rem;align-items:center;padding:1rem 1.3rem;border-top:1px solid var(--line);text-decoration:none}
#ed-root .v3-arch-row:first-child{border-top:none}
#ed-root .v3-arch-row:hover{background:var(--surf)}
#ed-root .v3-arch-d{font-size:.78rem;color:var(--faint);font-variant-numeric:tabular-nums;min-width:84px}
#ed-root .v3-arch-t{font-weight:600;color:var(--brand)}
#ed-root .v3-arch-row:hover .v3-arch-t{color:var(--blue)}
</style>'''

def balanced_div_end(s, start):
    depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>', s[start:]):
        depth+= 1 if m.group(1)=='' else -1
        if depth==0: return start+m.end()
    return -1

def main():
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*"', html)
    o=html.index('>',m.start())+1; c=balanced_div_end(html,m.start())
    before=html[:o]; after=html[c-6:]; orig=html[o:c-6]
    if 'id="smzh-v3-css"' not in before:
        before=before.replace('</head>', V3_CSS+'</head>',1)
    before=re.sub(r'(<div class="content-hub[^"]*")', r'\1 id="ed-root"', before, count=1)
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
    print('OK V3: Home, 4 Rubriken, Research, 2 Dossiers, 3 Serien, Archiv.')

if __name__=='__main__':
    main()
