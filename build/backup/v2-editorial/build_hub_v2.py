#!/usr/bin/env python3
"""smzhHub V2 – Editorial Redesign.
Eigenständige redaktionelle Designsprache (Magazin-Masthead, Serif-Display,
Cream/Ink/Gold-Palette, dunkler Decision-Layer, drei unterschiedliche Rubrik-
Kompositionen, institutionelles Research-Band). Ersetzt den alten Karten-Hub.
Daten: build/smzhhub-content.json + build/smzhub-placeholders.json.
Schreibt unter site/smzh.ch/de/.
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

MON={'Jan':'Jan.','Feb':'Feb.','Mar':'März','Apr':'Apr.','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug.','Sep':'Sep.','Oct':'Okt.','Nov':'Nov.','Dec':'Dez.'}
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
def imgt(im): return f'<img loading="lazy" src="{im}" alt="">' if im else ''

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

# ---- Konfig ----
NAV=[('aktuell','Aktuell','de/smzhub/'),('eigenheim','Eigenheim','de/smzhub-eigenheim/'),
     ('vermoegen','Vermögen','de/smzhub-vermoegen/'),('zukunft','Zukunft','de/smzhub-zukunft/'),
     ('steuern','Steuern','de/smzhub-steuern/'),('research','Research','de/smzhub-research/')]
NAV_BY={k:(l,p) for k,l,p in NAV}
TAB_RUBRIC={'eigenheim':'immobilien','vermoegen':'kapitalmaerkte','zukunft':'vorsorge','steuern':'steuern'}
TAB_INTRO={'eigenheim':'Kaufen, finanzieren, halten – Hypothek, Tragbarkeit und Immobilienmarkt klar eingeordnet.',
 'vermoegen':'Märkte, Zinsen und Portfolios verständlich – ohne tägliches Börsenrauschen.',
 'zukunft':'AHV, Pensionskasse und Säule 3a – damit aus Unsicherheit ein Plan wird.',
 'steuern':'Steuern senken und Vermögen klug strukturieren – konkret und planbar.'}
TAB_CTA={'eigenheim':('Hypothek prüfen lassen','de/immobilienbewertung/'),
 'vermoegen':('Anlagestrategie besprechen','de/terminvereinbaren/'),
 'zukunft':('Vorsorge analysieren','de/vorsorgeanalyse/'),
 'steuern':('Steuern optimieren','de/steuererklaerung/')}
SERIES=[('hypothekenradar','Hypotheken-Radar','Monatlich','smzhub-serie-hypotheken-radar','immobilien','Zinsen, Festhypotheken und Schweizer Hypothekarmarkt.'),
 ('investment-guide','Investment Guide','Monatlich','smzhub-serie-investment-guide','kapitalmaerkte','Märkte, Strategie und Portfoliothemen.'),
 ('immobilien-outlook','Immobilien-Outlook','Quartalsweise','smzhub-serie-immobilien-outlook','immobilien','Analyse des Schweizer Immobilienmarkts.')]
SERIES_BY={k:(name,cad,slug,theme,desc) for k,name,cad,slug,theme,desc in SERIES}
DECISIONS=[('Hypothek','SARON oder Festhypothek?','de/hypothekenarten-im-vergleich/'),
 ('Eigenheim','Kaufen oder warten?','de/wie-kaufe-ich-eine-immobilie/'),
 ('Vorsorge','Rente oder Kapital?','de/leistungen-im-alter/'),
 ('Anlegen','3a-Konto oder Wertschriften?','de/altersvorsorge-optimierung-saeule-3a/'),
 ('Eigenheim','Reicht mein Einkommen für die Bank?','de/optimierung-der-tragbarkeit/'),
 ('Steuern','Wie senke ich meine Steuern?','de/steuerabzuege-optimal-nutzen/')]
CTA_PATH={'vorsorgeanalyse':'de/vorsorgeanalyse/','immobilienbewertung':'de/immobilienbewertung/',
 'steuererklaerung':'de/steuererklaerung/','terminvereinbaren':'de/terminvereinbaren/'}
DOSSIER_OF={'immobilien':'ph-dossier-eigenheim','vorsorge':'ph-dossier-pensionierung'}

# ---- Komponenten (V2) ----
def cat_of(r):
    rub=r.get('rubric')
    return {'immobilien':'Eigenheim','kapitalmaerkte':'Vermögen','vorsorge':'Zukunft','steuern':'Steuern'}.get(rub, (r.get('topics') or ['smzh'])[0])

def rubricnav(active):
    items=''
    for i,(k,l,p) in enumerate(NAV):
        cls='v2-nav-link'+(' is-active' if k==active else '')
        items+=f'<a class="{cls}" href="{link(p)}"><span class="v2-nav-num">{i:02d}</span>{esc(l)}</a>'
    return f'<nav class="v2-nav" aria-label="smzhHub Rubriken"><div class="v2-nav-in">{items}</div></nav>'

def mast():
    return (f'<div class="v2-mast"><span class="v2-word">smzh<em>Hub</em></span>'
            f'<span class="v2-mast-tag">Research &amp; Orientierung</span>'
            f'<span class="v2-mast-ed">Ausgabe {esc(latest_month())}</span></div>')

def hero(slides):
    big=''; dots=''
    for i,r in enumerate(slides):
        im=img_of(r,1200)
        big+=(f'<a class="v2-hslide{" is-on" if i==0 else ""}" href="{link(r["path"])}">'
              f'<div class="v2-hslide-img">{imgt(im)}</div>'
              f'<div class="v2-hslide-cap"><span class="v2-kicker v2-kicker-light">{esc(cat_of(r))} · {esc(fdate(r.get("date")))}</span>'
              f'<h3>{esc(r["title"])}</h3><span class="v2-read">Beitrag lesen →</span></div></a>')
        dots+=f'<span class="v2-hdot{" is-on" if i==0 else ""}" role="button" tabindex="0" aria-label="Beitrag {i+1}">{i+1:02d}</span>'
    return (f'<header class="v2-hero">'
            f'<div class="v2-hero-l"><span class="v2-kicker">Der Finanz- und Beratungshub von smzh</span>'
            f'<h1 class="v2-hero-h1">Wissen, das Ihre <em>nächste Entscheidung</em> einfacher macht.</h1>'
            f'<p class="v2-hero-sub">Einordnungen, Ratgeber und wiederkehrendes Research zu Eigenheim, Vermögen, '
            f'Vorsorge und Steuern – ruhig, fundiert und auf den Punkt.</p>'
            f'<div class="v2-hero-cta"><a class="v2-btn" href="#v2-decide">Entscheidung finden</a>'
            f'<a class="v2-btn-ghost" href="#v2-rubrics">Themen entdecken</a></div></div>'
            f'<div class="v2-hero-r v2-slider"><div class="v2-hslides">{big}</div>'
            f'<div class="v2-hdots">{dots}</div></div></header>')

def decision_layer():
    rowsh=''
    for i,(cat,q,tail) in enumerate(DECISIONS):
        if not exists(tail): continue
        rowsh+=(f'<a class="v2-dec-row" href="{link(tail)}"><span class="v2-dec-n">{i+1:02d}</span>'
                f'<span class="v2-dec-q">{esc(q)}</span><span class="v2-dec-cat">{esc(cat)}</span>'
                f'<span class="v2-dec-go">→</span></a>')
    return (f'<section class="v2-decide" id="v2-decide"><div class="v2-decide-in">'
            f'<div class="v2-decide-l"><span class="v2-kicker v2-kicker-gold">Decision Layer</span>'
            f'<h2 class="v2-decide-h">Entscheiden statt nur informieren.</h2>'
            f'<p>Die wichtigsten Finanzfragen sind selten Wissensfragen, sondern Entscheidungen unter '
            f'Unsicherheit. Wählen Sie Ihre Frage – wir liefern den Einstieg.</p></div>'
            f'<div class="v2-decide-list">{rowsh}</div></div></section>')

def art_teaser(r, big=False):
    im=img_of(r, 1080 if big else 640)
    img=f'<span class="v2-te-img">{imgt(im)}</span>'
    return (f'<a class="v2-te{" v2-te-big" if big else ""}" href="{link(r["path"])}">{img}'
            f'<span class="v2-te-txt"><span class="v2-te-cat">{esc(cat_of(r))}</span>'
            f'<span class="v2-te-h">{esc(r["title"])}</span>'
            f'<span class="v2-te-meta">{esc(fdate(r.get("date")))}'
            +(f' · {r["readingTime"]} Min' if r.get("readingTime") else '')+'</span></span></a>')

def index_item(r, n):
    return (f'<a class="v2-ix-row" href="{link(r["path"])}"><span class="v2-ix-n">{n:02d}</span>'
            f'<span class="v2-ix-txt"><span class="v2-ix-h">{esc(r["title"])}</span>'
            f'<span class="v2-ix-meta">{esc(cat_of(r))} · {esc(fdate(r.get("date")))}</span></span></a>')

def edition(skey, vertical=False):
    name,cad,slug,theme,desc=SERIES_BY[skey]
    its=series_items(skey)
    if not its: return ''
    cur=its[0]; im=img_of(cur,640)
    cls='v2-ed'+(' v2-ed-v' if vertical else '')
    cover=f'<span class="v2-ed-cover">{imgt(im)}</span>'
    return (f'<a class="{cls}" href="{link("de/"+slug+"/")}">{cover}<span class="v2-ed-body">'
            f'<span class="v2-ed-tag">Edition · {esc(cad)}</span><span class="v2-ed-name">{esc(name)}</span>'
            f'<span class="v2-ed-cur">Aktuell: {esc(cur["title"])}</span>'
            f'<span class="v2-ed-go">Zur Serie →</span></span></a>')

def leadpath(tab, dossier_id=None):
    cl,cp=TAB_CTA[tab]
    dos=''
    if dossier_id and dossier_id in PH_BY:
        ph=PH_BY[dossier_id]
        if ph.get('status')=='real' and ph.get('url'):
            dos=f'<a class="v2-lp-dos" href="{link(ph["url"])}"><span class="v2-lp-tag">Dossier</span>{esc(ph["title"])} →</a>'
    return (f'<div class="v2-lp"><span class="v2-lp-k">Nächster Schritt</span>'
            f'<a class="v2-lp-cta" href="{link(cp)}">{esc(cl)} →</a>{dos}</div>')

def rub_head(num, tab, more=True):
    lbl=NAV_BY[tab][0]
    m=f'<a class="v2-rub-more" href="{link(NAV_BY[tab][1])}">Ganze Rubrik →</a>' if more else ''
    return (f'<header class="v2-rub-head"><span class="v2-secnum">{num}</span>'
            f'<div class="v2-rub-hh"><span class="v2-kicker v2-kicker-gold">Rubrik</span>'
            f'<h2 class="v2-h2">{esc(lbl)}</h2><p class="v2-lede">{esc(TAB_INTRO[tab])}</p></div>{m}</header>')

# Komposition A – Eigenheim: grosses Feature + nummerierter Index + Editionen
def rubric_eigenheim(num):
    rk='immobilien'; pool=lead_rubric(rk)
    if not pool: return ''
    lead=pool[0]; idx=pool[1:5]
    idxh=''.join(index_item(r,i+1) for i,r in enumerate(idx))
    eds=f'<div class="v2-ed-row">{edition("hypothekenradar")}{edition("immobilien-outlook")}</div>'
    return (f'<section class="v2-rub v2-rub-a">{rub_head(num,"eigenheim")}'
            f'<div class="v2-a-grid">{art_teaser(lead,big=True)}<ol class="v2-index">{idxh}</ol></div>'
            f'{eds}{leadpath("eigenheim",DOSSIER_OF["immobilien"])}</section>')

# Komposition B – Vermögen: Dispatch-Kolumne + vertikale Edition
def rubric_vermoegen(num):
    rk='kapitalmaerkte'; pool=lead_rubric(rk)
    if not pool: return ''
    lead=pool[0]; disp=pool[1:6]
    disph=''.join(
        f'<a class="v2-disp" href="{link(r["path"])}"><span class="v2-disp-h">{esc(r["title"])}</span>'
        f'<span class="v2-disp-meta">{esc(fdate(r.get("date")))}</span></a>' for r in disp)
    return (f'<section class="v2-rub v2-rub-b">{rub_head(num,"vermoegen")}'
            f'<div class="v2-b-grid"><div class="v2-b-feat">{art_teaser(lead,big=True)}</div>'
            f'<div class="v2-dispatches"><span class="v2-disp-k">Markteinschätzungen</span>{disph}</div>'
            f'<div class="v2-b-anchor">{edition("investment-guide",vertical=True)}</div></div>'
            f'{leadpath("vermoegen")}</section>')

# Komposition C – Zukunft: Feature + Storyline-Timeline (Dossier)
DOSSIER_STEPS={'pensionierung':[
   ('Grundlagen','de/das-3-saeulensystem-der-schweiz/','Das 3-Säulen-System'),
   ('Säule 3a','de/altersvorsorge-optimierung-saeule-3a/','Säule 3a optimal nutzen'),
   ('Planung','de/pensionsplanung/','Pensionsplanung'),
   ('Leistungen','de/leistungen-im-alter/','Leistungen im Alter')]}
def rubric_zukunft(num):
    rk='vorsorge'; pool=lead_rubric(rk)
    if not pool: return ''
    lead=pool[0]
    steps=DOSSIER_STEPS['pensionierung']
    tl=''
    n=0
    for kicker,path,fallback in steps:
        if not exists(path): continue
        n+=1
        it={r['path']:r for r in rows}.get('/'+path.strip('/')+'/')
        title=it['title'] if it else fallback
        tl+=(f'<a class="v2-tl-step" href="{link(path)}"><span class="v2-tl-n">{n}</span>'
             f'<span class="v2-tl-k">{esc(kicker)}</span><span class="v2-tl-h">{esc(title)}</span></a>')
    return (f'<section class="v2-rub v2-rub-c">{rub_head(num,"zukunft")}'
            f'<div class="v2-c-grid"><div class="v2-c-feat">{art_teaser(lead,big=True)}</div>'
            f'<div class="v2-tl"><span class="v2-tl-cap">Dossier · Pensionierung planen</span>'
            f'<div class="v2-tl-steps">{tl}</div>'
            f'<a class="v2-tl-go" href="{link("de/smzhub-dossier-pensionierung/")}">Ganzes Dossier öffnen →</a></div></div>'
            f'{leadpath("zukunft",DOSSIER_OF["vorsorge"])}</section>')

def flagship_band():
    cols=''
    for skey,name,cad,slug,theme,desc in SERIES:
        its=series_items(skey)
        if not its: continue
        cur=its[0]; im=img_of(cur,640)
        cols+=(f'<a class="v2-fl-col" href="{link("de/"+slug+"/")}">'
               f'<span class="v2-fl-cover">{imgt(im)}</span>'
               f'<span class="v2-fl-cad">{esc(cad)} · {len(its)} Ausgaben</span>'
               f'<span class="v2-fl-name">{esc(name)}</span><span class="v2-fl-desc">{esc(desc)}</span>'
               f'<span class="v2-fl-cur">Aktuell: {esc(cur["title"])}</span>'
               f'<span class="v2-fl-go">Zur Serie →</span></a>')
    return (f'<section class="v2-research"><div class="v2-research-head">'
            f'<span class="v2-kicker v2-kicker-light v2-kicker-gold">Research</span>'
            f'<h2 class="v2-research-h">Wiederkehrende Einschätzungen von smzh</h2>'
            f'<p>Drei Flagship-Formate – fundiert, regelmässig, mit eigener Serienidentität.</p></div>'
            f'<div class="v2-editions">{cols}</div>'
            f'<a class="v2-research-more" href="{link("de/smzhub-research/")}">Alle Publikationen →</a></section>')

def big_cta(label='Persönliche Beratung', path='de/terminvereinbaren/'):
    return (f'<section class="v2-cta"><div class="v2-cta-in">'
            f'<h2 class="v2-cta-h">Ihre Situation verdient mehr als einen Standardrat.</h2>'
            f'<p>Wir begleiten Sie persönlich – unabhängig, diskret und auf Ihre Situation zugeschnitten.</p>'
            f'<a class="v2-btn v2-btn-gold" href="{link(path)}">{esc(label)} →</a></div></section>')

# ---- Seiten ----
def home_inner():
    used=set()
    hp=[]
    for key in ['immobilien','kapitalmaerkte','vorsorge']:
        ls=lead_rubric(key)
        if ls: hp.append(ls[0])
    hp.sort(key=lambda r:r.get('date') or '', reverse=True); hp=hp[:3]
    return (mast()+rubricnav('aktuell')+hero(hp)+decision_layer()
            +'<div id="v2-rubrics">'+rubric_eigenheim('01')+rubric_vermoegen('02')+rubric_zukunft('03')+'</div>'
            +flagship_band()+big_cta())

def rubric_page(tab):
    rk=TAB_RUBRIC[tab]; lbl,path=NAV_BY[tab]
    pool=lead_rubric(rk); komm=komm_rubric(rk)
    crumb=f'<nav class="v2-crumb"><a href="{link("de/smzhub/")}">smzhHub</a> / {esc(lbl)}</nav>'
    cl,cp=TAB_CTA[tab]
    hero=(f'<header class="v2-phero"><span class="v2-kicker v2-kicker-gold">Rubrik</span>'
          f'<h1 class="v2-phero-h">{esc(lbl)}</h1><p class="v2-phero-sub">{esc(TAB_INTRO[tab])}</p>'
          f'<a class="v2-btn" href="{link(cp)}">{esc(cl)} →</a></header>')
    body=''
    if tab=='eigenheim': body=rubric_eigenheim('01')
    elif tab=='vermoegen': body=rubric_vermoegen('01')
    elif tab=='zukunft': body=rubric_zukunft('01')
    else:
        if pool:
            lead=pool[0]; idx=pool[1:7]
            idxh=''.join(index_item(r,i+1) for i,r in enumerate(idx))
            body=(f'<section class="v2-rub v2-rub-a"><div class="v2-a-grid">{art_teaser(lead,big=True)}'
                  f'<ol class="v2-index">{idxh}</ol></div>{leadpath(tab)}</section>')
    # weitere Beiträge als Editorial-Teaser-Reihe (kein Kartenraster)
    used_ids={r['id'] for r in pool[:7]}
    more=[r for r in komm if r['id'] not in used_ids][:6]
    moreh=''
    if more:
        moreh=('<section class="v2-more"><span class="v2-kicker v2-kicker-gold">Weiterlesen</span>'
               '<div class="v2-more-grid">'+''.join(art_teaser(r) for r in more)+'</div></section>')
    return rubricnav(tab)+crumb+hero+body+moreh+big_cta(cl,cp)

def research_page():
    crumb=f'<nav class="v2-crumb"><a href="{link("de/smzhub/")}">smzhHub</a> / Research</nav>'
    hero=('<header class="v2-phero"><span class="v2-kicker v2-kicker-gold">Research &amp; Publikationen</span>'
          '<h1 class="v2-phero-h">Das smzh-Research</h1><p class="v2-phero-sub">Drei wiederkehrende '
          'Flagship-Formate liefern regelmässig fundierte Einschätzungen – mit aktueller Ausgabe und Archiv.</p></header>')
    return rubricnav('research')+crumb+hero+flagship_band()+big_cta('Beratung vereinbaren','de/terminvereinbaren/')

def series_page(skey):
    name,cad,slug,theme,desc=SERIES_BY[skey]; its=series_items(skey); cur=its[0] if its else None
    tab={'immobilien':'eigenheim','kapitalmaerkte':'vermoegen'}.get(theme,'research')
    crumb=(f'<nav class="v2-crumb"><a href="{link("de/smzhub/")}">smzhHub</a> / '
           f'<a href="{link("de/smzhub-research/")}">Research</a> / {esc(name)}</nav>')
    hero=(f'<header class="v2-phero"><span class="v2-kicker v2-kicker-gold">{esc(cad)} · Serie</span>'
          f'<h1 class="v2-phero-h">{esc(name)}</h1><p class="v2-phero-sub">{esc(desc)}</p></header>')
    cur_html=''
    if cur:
        im=img_of(cur,1200); cover=f'<span class="v2-te-img">{imgt(im)}</span>'
        pdf=f'<a class="v2-pdf" href="{P_}../cms.smzh.ch/uploads/{cur["pdfs"][0]}" target="_blank" rel="noopener">PDF ansehen</a>' if cur.get('pdfs') else ''
        cur_html=(f'<section class="v2-rub"><span class="v2-kicker v2-kicker-gold">Aktuelle Ausgabe</span>'
                  f'<a class="v2-te v2-te-big" href="{link(cur["path"])}">{cover}<span class="v2-te-txt">'
                  f'<span class="v2-te-cat">{esc(fdate(cur.get("date")))}</span>'
                  f'<span class="v2-te-h">{esc(cur["title"])}</span>'
                  f'<span class="v2-te-meta">{esc(teaser(cur,160))}</span></span></a>'
                  f'<div class="v2-lp"><a class="v2-lp-cta" href="{link(cur["path"])}">Ausgabe lesen →</a>{pdf}</div></section>')
    arch=''
    for r in its[1:]:
        pdf=f'<a class="v2-pdf" href="{P_}../cms.smzh.ch/uploads/{r["pdfs"][0]}" target="_blank" rel="noopener">PDF</a>' if r.get('pdfs') else ''
        arch+=(f'<a class="v2-arch-row" href="{link(r["path"])}"><span class="v2-arch-t">{esc(fdate(r.get("date")))}</span>'
               f'<span class="v2-arch-h">{esc(r["title"])}</span>{pdf}</a>')
    arch_html=(f'<section class="v2-rub"><span class="v2-kicker v2-kicker-gold">Archiv · {len(its)-1} Ausgaben</span>'
               f'<div class="v2-arch">{arch}</div></section>') if len(its)>1 else ''
    return rubricnav('research')+crumb+hero+cur_html+arch_html+big_cta('Beratung vereinbaren','de/terminvereinbaren/')

def dossier_page(dkey):
    cfg={'eigenheim':{'tab':'eigenheim','rk':'immobilien','title':'Eigenheim finanzieren','kicker':'Dossier · Immobilien',
            'intro':'Von der ersten Idee bis zur Bankzusage: der rote Faden zu Kauf, Tragbarkeit, Eigenkapital und Hypothek.',
            'flag':'hypothekenradar','steps':[('Einstieg','de/wie-kaufe-ich-eine-immobilie/','Wie kaufe ich eine Immobilie?'),
              ('Tragbarkeit','de/optimierung-der-tragbarkeit/','Tragbarkeit optimieren'),
              ('Finanzierung','de/hypothekenarten-im-vergleich/','Hypothekenarten im Vergleich'),
              ('Eigenkapital','de/wohneigentumsfoerderung/','Wohneigentumsförderung')]},
          'pensionierung':{'tab':'zukunft','rk':'vorsorge','title':'Pensionierung planen','kicker':'Dossier · Vorsorge',
            'intro':'AHV, Pensionskasse und Säule 3a greifen ineinander – von den Grundlagen bis zur Entscheidung Rente oder Kapital.',
            'flag':None,'steps':DOSSIER_STEPS['pensionierung']}}[dkey]
    tab=cfg['tab']; cl,cp=TAB_CTA[tab]
    crumb=(f'<nav class="v2-crumb"><a href="{link("de/smzhub/")}">smzhHub</a> / '
           f'<a href="{link(NAV_BY[tab][1])}">{esc(NAV_BY[tab][0])}</a> / Dossier</nav>')
    hero=(f'<header class="v2-phero v2-phero-dos"><span class="v2-kicker v2-kicker-gold">{esc(cfg["kicker"])}</span>'
          f'<h1 class="v2-phero-h">{esc(cfg["title"])}</h1><p class="v2-phero-sub">{esc(cfg["intro"])}</p>'
          f'<a class="v2-btn" href="{link(cp)}">{esc(cl)} →</a></header>')
    steps=list(cfg['steps']); lr=lead_rubric(cfg['rk'])
    if lr: steps=steps+[('Aktuell', lr[0]['path'].strip('/'), lr[0]['title'])]
    big=''; n=0
    for kicker,path,fb in steps:
        if not exists(path): continue
        n+=1
        it={r['path']:r for r in rows}.get('/'+path.strip('/')+'/')
        title=it['title'] if it else fb; tz=teaser(it,120) if it else ''
        big+=(f'<a class="v2-dos-step" href="{link(path)}"><span class="v2-dos-n">{n}</span>'
              f'<span class="v2-dos-txt"><span class="v2-tl-k">{esc(kicker)}</span>'
              f'<span class="v2-dos-h">{esc(title)}</span><span class="v2-dos-p">{esc(tz)}</span></span>'
              f'<span class="v2-dos-go">→</span></a>')
    story=f'<section class="v2-rub"><span class="v2-kicker v2-kicker-gold">Storyline · Der rote Faden</span><div class="v2-dos-steps">{big}</div></section>'
    band=flagship_band() if cfg.get('flag') else ''
    return rubricnav(tab)+crumb+hero+story+band+big_cta(cl,cp)

def archiv_inner(orig_inner):
    body=re.sub(r'<section id="smzh-research".*?</section>','',orig_inner,flags=re.S)
    crumb=f'<nav class="v2-crumb"><a href="{link("de/smzhub/")}">smzhHub</a> / Alle Inhalte</nav>'
    hero=('<header class="v2-phero"><span class="v2-kicker v2-kicker-gold">Archiv</span>'
          '<h1 class="v2-phero-h">Alle Inhalte</h1><p class="v2-phero-sub">Das vollständige Verzeichnis aller '
          'Beiträge, Publikationen, Talks und Podcasts.</p></header>')
    return rubricnav(None)+crumb+hero+body

# ---- CSS / JS ----
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,700&display=swap" rel="stylesheet">')

V2_CSS = '''<style id="smzh-v2-css">
#ed-root{--ink:#0e1f30;--ink2:#10243a;--paper:#f7f3eb;--paper2:#efe7d7;--gold:#b07d1e;--gold2:#caa44e;--rule:#ddd2bd;--muted:#6b6256;--body:#2c2f33;max-width:1280px}
#ed-root{--serif:'Fraunces','Iowan Old Style','Palatino Linotype',Palatino,Georgia,serif}
#ed-root{gap:0 !important;background:var(--paper);color:var(--body);padding-top:0 !important}
#ed-root *{box-sizing:border-box}
#ed-root section,#ed-root header{margin:0}
#ed-root .v2-kicker{display:inline-block;font-size:.7rem;letter-spacing:.22em;text-transform:uppercase;font-weight:700;color:var(--muted)}
#ed-root .v2-kicker-gold{color:var(--gold)}
#ed-root .v2-kicker-light{color:#cdbb8e}
#ed-root em{font-style:italic}
/* Masthead */
#ed-root .v2-mast{display:flex;align-items:baseline;gap:1.2rem;padding:1.4rem 0 1rem;border-bottom:2px solid var(--ink)}
#ed-root .v2-word{font-family:var(--serif);font-weight:600;font-size:1.7rem;color:var(--ink);letter-spacing:-.01em}
#ed-root .v2-word em{font-style:italic;color:var(--gold)}
#ed-root .v2-mast-tag{font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);font-weight:700}
#ed-root .v2-mast-ed{margin-left:auto;font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}
/* Rubriknav */
#ed-root .v2-nav{position:sticky;top:0;z-index:30;background:var(--paper);border-bottom:1px solid var(--rule);margin-bottom:2.6rem}
#ed-root .v2-nav-in{display:flex;gap:2.2rem;overflow-x:auto;padding:.9rem 0}
#ed-root .v2-nav-link{display:inline-flex;align-items:baseline;gap:.45rem;white-space:nowrap;text-decoration:none;color:var(--ink);font-weight:600;font-size:1rem;padding-bottom:.2rem;border-bottom:2px solid transparent}
#ed-root .v2-nav-num{font-size:.62rem;color:var(--gold);font-weight:800;letter-spacing:.05em}
#ed-root .v2-nav-link.is-active{border-bottom-color:var(--gold)}
#ed-root .v2-nav-link:hover{color:var(--gold)}
/* Hero */
#ed-root .v2-hero{display:grid;grid-template-columns:1fr;gap:2.4rem;padding:1.5rem 0 4rem;border-bottom:1px solid var(--rule);margin-bottom:4rem}
@media(min-width:920px){#ed-root .v2-hero{grid-template-columns:1.02fr 1.18fr;gap:3.4rem;align-items:stretch}}
#ed-root .v2-hero-l{display:flex;flex-direction:column;justify-content:center}
#ed-root .v2-hero-h1{font-family:var(--serif);font-weight:500;font-size:clamp(2.4rem,5vw,4.1rem);line-height:1.02;letter-spacing:-.02em;color:var(--ink);margin:1rem 0 1.2rem}
#ed-root .v2-hero-h1 em{color:var(--gold);font-style:italic}
#ed-root .v2-hero-sub{font-size:clamp(1.05rem,1.5vw,1.2rem);color:var(--muted);max-width:44ch;line-height:1.55;margin:0 0 1.8rem}
#ed-root .v2-hero-cta{display:flex;gap:1rem;flex-wrap:wrap}
#ed-root .v2-btn{display:inline-block;background:var(--ink);color:#fff;font-weight:600;text-decoration:none;padding:.9rem 1.7rem;border-radius:2px;font-size:.98rem;transition:.15s}
#ed-root .v2-btn:hover{background:var(--gold);color:var(--ink)}
#ed-root .v2-btn-gold{background:var(--gold);color:var(--ink)}
#ed-root .v2-btn-gold:hover{background:#fff}
#ed-root .v2-btn-ghost{display:inline-block;color:var(--ink);text-decoration:none;font-weight:600;padding:.9rem .4rem;border-bottom:2px solid var(--gold);align-self:center}
/* Hero-Slider (grosse Bühne) */
#ed-root .v2-hero-r{position:relative;min-height:420px;border:1px solid var(--rule);background:var(--ink2);overflow:hidden}
#ed-root .v2-hslides{position:absolute;inset:0}
#ed-root .v2-hslide{position:absolute;inset:0;opacity:0;transition:opacity .7s ease;text-decoration:none;pointer-events:none}
#ed-root .v2-hslide.is-on{opacity:1;pointer-events:auto}
#ed-root .v2-hslide-img,#ed-root .v2-hslide-img img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#ed-root .v2-hslide:after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(8,18,30,.95) 0%,rgba(8,18,30,.45) 45%,rgba(8,18,30,.05) 75%)}
#ed-root .v2-hslide-cap{position:absolute;left:0;right:0;bottom:0;z-index:2;padding:2.2rem 2.4rem;color:#fff}
#ed-root .v2-hslide-cap h3{font-family:var(--serif);font-weight:500;font-size:clamp(1.5rem,2.6vw,2.3rem);line-height:1.12;margin:.6rem 0 .7rem;max-width:20ch}
#ed-root .v2-read{font-size:.82rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-weight:700}
#ed-root .v2-hdots{position:absolute;top:1.4rem;right:1.6rem;z-index:3;display:flex;gap:.5rem}
#ed-root .v2-hdot{font-size:.66rem;font-weight:800;letter-spacing:.05em;color:rgba(255,255,255,.5);cursor:pointer;border-bottom:2px solid transparent;padding-bottom:2px}
#ed-root .v2-hdot.is-on{color:#fff;border-bottom-color:var(--gold)}
/* Decision Layer (dunkel, editorial) */
#ed-root .v2-decide{background:var(--ink);color:#fff;margin:0 0 4.5rem;border-radius:3px}
#ed-root .v2-decide-in{display:grid;grid-template-columns:1fr;gap:2rem;padding:3rem 2.4rem}
@media(min-width:920px){#ed-root .v2-decide-in{grid-template-columns:0.8fr 1.2fr;gap:3.5rem;padding:3.6rem 3rem}}
#ed-root .v2-decide-h{font-family:var(--serif);font-weight:500;font-size:clamp(1.8rem,3vw,2.6rem);line-height:1.08;color:#fff;margin:.7rem 0 1rem}
#ed-root .v2-decide-l p{color:#aebccb;line-height:1.6;margin:0;max-width:40ch}
#ed-root .v2-decide-list{display:flex;flex-direction:column}
#ed-root .v2-dec-row{display:grid;grid-template-columns:auto 1fr auto auto;align-items:center;gap:1.2rem;padding:1.15rem .2rem;border-top:1px solid rgba(255,255,255,.16);text-decoration:none;color:#fff;transition:.15s}
#ed-root .v2-dec-row:last-child{border-bottom:1px solid rgba(255,255,255,.16)}
#ed-root .v2-dec-n{font-size:.78rem;font-weight:800;color:var(--gold2)}
#ed-root .v2-dec-q{font-family:var(--serif);font-size:clamp(1.15rem,1.8vw,1.5rem);font-weight:500;line-height:1.15}
#ed-root .v2-dec-cat{font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:#8fa1b3;font-weight:700;white-space:nowrap}
#ed-root .v2-dec-go{color:var(--gold2);font-size:1.3rem;transform:translateX(0);transition:.2s}
#ed-root .v2-dec-row:hover{padding-left:.8rem}
#ed-root .v2-dec-row:hover .v2-dec-q{color:var(--gold2)}
#ed-root .v2-dec-row:hover .v2-dec-go{transform:translateX(6px)}
/* Rubrik-Kopf */
#ed-root .v2-rub{margin:0 0 4.5rem}
#ed-root .v2-rub-head{display:grid;grid-template-columns:auto 1fr auto;gap:1.4rem;align-items:end;border-bottom:2px solid var(--ink);padding-bottom:1.1rem;margin-bottom:2rem}
#ed-root .v2-secnum{font-family:var(--serif);font-size:clamp(2.4rem,5vw,3.6rem);line-height:.8;color:var(--gold);font-weight:600}
#ed-root .v2-h2{font-family:var(--serif);font-weight:500;font-size:clamp(1.7rem,3vw,2.5rem);line-height:1.05;color:var(--ink);margin:.3rem 0 .2rem}
#ed-root .v2-lede{color:var(--muted);margin:.2rem 0 0;max-width:54ch;line-height:1.5}
#ed-root .v2-rub-more{color:var(--ink);font-weight:700;text-decoration:none;white-space:nowrap;border-bottom:2px solid var(--gold);padding-bottom:2px;font-size:.92rem}
/* Editorial-Teaser (keine Box) */
#ed-root .v2-te{display:flex;flex-direction:column;gap:.8rem;text-decoration:none;color:inherit}
#ed-root .v2-te-img{display:block;overflow:hidden;background:var(--paper2);aspect-ratio:3/2}
#ed-root .v2-te-big .v2-te-img{aspect-ratio:4/3}
#ed-root .v2-te-img img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
#ed-root .v2-te:hover .v2-te-img img{transform:scale(1.04)}
#ed-root .v2-te-cat{display:block;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:800}
#ed-root .v2-te-h{display:block;font-family:var(--serif);font-weight:500;color:var(--ink);line-height:1.14;font-size:1.4rem;margin:.25rem 0}
#ed-root .v2-te-big .v2-te-h{font-size:clamp(1.7rem,2.6vw,2.4rem)}
#ed-root .v2-te:hover .v2-te-h{color:var(--gold)}
#ed-root .v2-te-meta{display:block;font-size:.82rem;color:var(--muted)}
/* Komposition A: Feature + Index */
#ed-root .v2-a-grid{display:grid;grid-template-columns:1fr;gap:2.4rem}
@media(min-width:920px){#ed-root .v2-a-grid{grid-template-columns:1.5fr 1fr;gap:3rem}}
#ed-root .v2-index{list-style:none;margin:0;padding:0;border-top:1px solid var(--rule)}
#ed-root .v2-ix-row{display:grid;grid-template-columns:auto 1fr;gap:1rem;padding:1.05rem 0;border-bottom:1px solid var(--rule);text-decoration:none}
#ed-root .v2-ix-n{font-family:var(--serif);font-size:1.2rem;color:var(--gold);font-weight:600}
#ed-root .v2-ix-h{display:block;font-family:var(--serif);font-weight:500;color:var(--ink);line-height:1.2;font-size:1.12rem}
#ed-root .v2-ix-row:hover .v2-ix-h{color:var(--gold)}
#ed-root .v2-ix-meta{display:block;font-size:.74rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;margin-top:.25rem}
/* Editionen-Reihe (Serien-Anker) */
#ed-root .v2-ed-row{display:grid;grid-template-columns:1fr;gap:1.2rem;margin-top:2.4rem}
@media(min-width:720px){#ed-root .v2-ed-row{grid-template-columns:1fr 1fr}}
#ed-root .v2-ed{display:flex;gap:1.1rem;align-items:stretch;text-decoration:none;background:var(--ink);color:#fff;border-radius:2px;overflow:hidden;border-left:3px solid var(--gold)}
#ed-root .v2-ed-v{flex-direction:column}
#ed-root .v2-ed-cover{flex:0 0 116px;background:#0a1a2a;overflow:hidden}
#ed-root .v2-ed-v .v2-ed-cover{flex-basis:auto;aspect-ratio:16/9}
#ed-root .v2-ed-cover img{width:100%;height:100%;object-fit:cover;opacity:.92}
#ed-root .v2-ed-body{display:flex;flex-direction:column;gap:.2rem;padding:1.1rem 1.2rem}
#ed-root .v2-ed-tag{font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-weight:800}
#ed-root .v2-ed-name{font-family:var(--serif);font-size:1.3rem;font-weight:500}
#ed-root .v2-ed-cur{font-size:.82rem;color:#9fb0c0;line-height:1.35}
#ed-root .v2-ed-go{font-size:.78rem;color:var(--gold2);font-weight:700;margin-top:.3rem}
/* Lead-Pfad */
#ed-root .v2-lp{display:flex;flex-wrap:wrap;align-items:center;gap:1.4rem;margin-top:2rem;padding-top:1.2rem;border-top:1px solid var(--rule)}
#ed-root .v2-lp-k{font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;color:var(--muted);font-weight:800}
#ed-root .v2-lp-cta{font-family:var(--serif);font-size:1.2rem;color:var(--ink);text-decoration:none;font-weight:600;border-bottom:2px solid var(--gold)}
#ed-root .v2-lp-cta:hover{color:var(--gold)}
#ed-root .v2-lp-dos{margin-left:auto;color:var(--muted);text-decoration:none;font-weight:600;font-size:.9rem;display:inline-flex;align-items:center;gap:.5rem}
#ed-root .v2-lp-tag{font-size:.6rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--gold);background:#efe2c6;padding:.14rem .5rem;border-radius:2px}
#ed-root .v2-pdf{color:var(--gold);font-weight:700;text-decoration:none;font-size:.86rem}
/* Komposition B: Dispatch-Kolumne */
#ed-root .v2-b-grid{display:grid;grid-template-columns:1fr;gap:2.4rem}
@media(min-width:920px){#ed-root .v2-b-grid{grid-template-columns:1.4fr 1fr .9fr;gap:2.6rem}}
#ed-root .v2-disp-k{display:block;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:800;margin-bottom:.6rem}
#ed-root .v2-disp{display:block;padding:.95rem 0 .95rem 1.1rem;border-left:2px solid var(--rule);text-decoration:none;transition:.15s}
#ed-root .v2-disp:hover{border-left-color:var(--gold)}
#ed-root .v2-disp-h{display:block;font-family:var(--serif);font-weight:500;color:var(--ink);line-height:1.2;font-size:1.08rem}
#ed-root .v2-disp:hover .v2-disp-h{color:var(--gold)}
#ed-root .v2-disp-meta{font-size:.74rem;color:var(--muted);text-transform:uppercase;letter-spacing:.05em}
/* Komposition C: Timeline */
#ed-root .v2-c-grid{display:grid;grid-template-columns:1fr;gap:2.4rem}
@media(min-width:920px){#ed-root .v2-c-grid{grid-template-columns:1.3fr 1fr;gap:3rem}}
#ed-root .v2-tl{background:var(--paper2);border-radius:3px;padding:1.8rem}
#ed-root .v2-tl-cap{display:block;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);font-weight:800;margin-bottom:1rem}
#ed-root .v2-tl-steps{display:flex;flex-direction:column;position:relative}
#ed-root .v2-tl-steps:before{content:"";position:absolute;left:15px;top:18px;bottom:18px;width:2px;background:var(--rule)}
#ed-root .v2-tl-step{display:grid;grid-template-columns:auto 1fr;gap:1rem;align-items:baseline;padding:.7rem 0;text-decoration:none;position:relative;z-index:1}
#ed-root .v2-tl-n{width:32px;height:32px;border-radius:50%;background:var(--ink);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;font-size:.9rem;grid-row:span 2}
#ed-root .v2-tl-k{font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);font-weight:800}
#ed-root .v2-tl-h{font-family:var(--serif);font-weight:500;color:var(--ink);font-size:1.1rem;line-height:1.2}
#ed-root .v2-tl-step:hover .v2-tl-h{color:var(--gold)}
#ed-root .v2-tl-go{display:inline-block;margin-top:1rem;font-weight:700;color:var(--ink);text-decoration:none;border-bottom:2px solid var(--gold);padding-bottom:2px;font-size:.9rem}
/* Research-Band (dunkel, institutionell) */
#ed-root .v2-research{background:var(--ink);color:#fff;border-radius:3px;padding:3rem 2.4rem;margin:0 0 4.5rem}
@media(min-width:920px){#ed-root .v2-research{padding:3.6rem 3rem}}
#ed-root .v2-research-head{max-width:60ch;margin-bottom:2.4rem}
#ed-root .v2-research-h{font-family:var(--serif);font-weight:500;font-size:clamp(1.7rem,3vw,2.5rem);line-height:1.08;color:#fff;margin:.7rem 0 .6rem}
#ed-root .v2-research-head p{color:#aebccb;margin:0;line-height:1.55}
#ed-root .v2-editions{display:grid;grid-template-columns:1fr;gap:2rem}
@media(min-width:760px){#ed-root .v2-editions{grid-template-columns:1fr 1fr 1fr;gap:2.4rem}}
#ed-root .v2-fl-col{display:flex;flex-direction:column;gap:.5rem;text-decoration:none;color:#fff;padding-top:1.4rem;border-top:2px solid var(--gold)}
#ed-root .v2-fl-cover{aspect-ratio:16/10;overflow:hidden;background:#0a1a2a;margin-bottom:.4rem}
#ed-root .v2-fl-cover img{width:100%;height:100%;object-fit:cover;opacity:.9;transition:.5s}
#ed-root .v2-fl-col:hover .v2-fl-cover img{opacity:1;transform:scale(1.03)}
#ed-root .v2-fl-cad{font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold2);font-weight:800}
#ed-root .v2-fl-name{font-family:var(--serif);font-size:1.45rem;font-weight:500}
#ed-root .v2-fl-desc{color:#9fb0c0;font-size:.86rem;line-height:1.4}
#ed-root .v2-fl-cur{color:#7e90a1;font-size:.8rem;margin-top:.2rem}
#ed-root .v2-fl-go{color:var(--gold2);font-weight:700;font-size:.84rem;margin-top:.4rem}
#ed-root .v2-research-more{display:inline-block;margin-top:2.2rem;color:#fff;font-weight:700;text-decoration:none;border-bottom:2px solid var(--gold);padding-bottom:2px}
/* CTA */
#ed-root .v2-cta{border-top:2px solid var(--ink);padding:3rem 0 1rem;margin-bottom:2rem}
#ed-root .v2-cta-h{font-family:var(--serif);font-weight:500;font-size:clamp(1.7rem,3.4vw,2.7rem);line-height:1.05;color:var(--ink);max-width:24ch;margin:0 0 .7rem}
#ed-root .v2-cta p{color:var(--muted);margin:0 0 1.5rem;max-width:52ch;line-height:1.55}
/* Rubrikseiten */
#ed-root .v2-crumb{font-size:.8rem;color:var(--muted);margin:.4rem 0 1.4rem;letter-spacing:.04em}
#ed-root .v2-crumb a{color:var(--gold);text-decoration:none}
#ed-root .v2-phero{border-bottom:1px solid var(--rule);padding-bottom:2.2rem;margin-bottom:3rem}
#ed-root .v2-phero-h{font-family:var(--serif);font-weight:500;font-size:clamp(2.4rem,5.5vw,4.2rem);line-height:1;color:var(--ink);letter-spacing:-.02em;margin:.8rem 0 1rem}
#ed-root .v2-phero-sub{font-size:1.15rem;color:var(--muted);max-width:50ch;line-height:1.5;margin:0 0 1.6rem}
#ed-root .v2-more{margin-bottom:4rem}
#ed-root .v2-more-grid{display:grid;grid-template-columns:1fr;gap:2.4rem;margin-top:1.4rem}
@media(min-width:640px){#ed-root .v2-more-grid{grid-template-columns:1fr 1fr}}
@media(min-width:980px){#ed-root .v2-more-grid{grid-template-columns:1fr 1fr 1fr}}
/* Dossier */
#ed-root .v2-dos-steps{display:flex;flex-direction:column;border-top:1px solid var(--rule);margin-top:1.2rem}
#ed-root .v2-dos-step{display:grid;grid-template-columns:auto 1fr auto;gap:1.4rem;align-items:center;padding:1.4rem .3rem;border-bottom:1px solid var(--rule);text-decoration:none}
#ed-root .v2-dos-n{font-family:var(--serif);font-size:2rem;font-weight:600;color:var(--gold);line-height:1}
#ed-root .v2-dos-h{display:block;font-family:var(--serif);font-size:1.4rem;font-weight:500;color:var(--ink);line-height:1.15;margin:.1rem 0}
#ed-root .v2-dos-step:hover .v2-dos-h{color:var(--gold)}
#ed-root .v2-dos-p{display:block;color:var(--muted);font-size:.9rem;line-height:1.45}
#ed-root .v2-dos-go{color:var(--gold);font-size:1.4rem}
/* Archiv */
#ed-root .v2-arch{display:flex;flex-direction:column;border-top:1px solid var(--rule);margin-top:1rem}
#ed-root .v2-arch-row{display:grid;grid-template-columns:auto 1fr auto;gap:1.2rem;align-items:baseline;padding:1rem .2rem;border-bottom:1px solid var(--rule);text-decoration:none}
#ed-root .v2-arch-t{font-size:.78rem;color:var(--muted);text-transform:uppercase;letter-spacing:.06em;min-width:84px}
#ed-root .v2-arch-h{font-family:var(--serif);font-size:1.12rem;color:var(--ink);font-weight:500}
#ed-root .v2-arch-row:hover .v2-arch-h{color:var(--gold)}
</style>'''

V2_JS = '''<script id="smzh-v2-js">
(function(){function r(f){if(document.readyState!=='loading')f();else document.addEventListener('DOMContentLoaded',f);}
r(function(){document.querySelectorAll('.v2-slider').forEach(function(s){
var sl=s.querySelectorAll('.v2-hslide'),dt=s.querySelectorAll('.v2-hdot'),i=0,n=sl.length,t=null;if(n<2)return;
function go(k){i=(k+n)%n;sl.forEach(function(e,j){e.classList.toggle('is-on',j===i)});dt.forEach(function(d,j){d.classList.toggle('is-on',j===i)})}
function au(){t=setInterval(function(){go(i+1)},6000)}function rs(){clearInterval(t);au()}
dt.forEach(function(d,j){d.addEventListener('click',function(e){e.preventDefault();go(j);rs()})});
s.addEventListener('mouseenter',function(){clearInterval(t)});s.addEventListener('mouseleave',au);go(0);au();});});})();
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
    o=html.index('>',m.start())+1; c=balanced_div_end(html,m.start())
    before=html[:o]; after=html[c-6:]; orig=html[o:c-6]
    if 'id="smzh-v2-css"' not in before:
        before=before.replace('</head>', FONTS+V2_CSS+'</head>',1)
    before=re.sub(r'(<div class="content-hub[^"]*")', r'\1 id="ed-root"', before, count=1)
    if 'id="smzh-v2-js"' not in after:
        after=after.replace('</body>', V2_JS+'</body>',1)
    def write(path, inner, title):
        full=before+inner+after
        full=re.sub(r'<title>.*?</title>','<title>'+H.escape(title)+'</title>',full,count=1,flags=re.S)
        d=os.path.join(SMZH,path.strip('/')); os.makedirs(d,exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)
    write('de/smzhub/', home_inner(), 'smzhHub – Finanzwissen für Ihre Entscheidungen')
    for tab in ['eigenheim','vermoegen','zukunft','steuern']:
        write(NAV_BY[tab][1], rubric_page(tab), f'{NAV_BY[tab][0]} – smzhHub')
    write('de/smzhub-research/', research_page(), 'Research & Publikationen – smzhHub')
    for dk in ['eigenheim','pensionierung']:
        write('de/smzhub-dossier-'+dk+'/', dossier_page(dk), f'Dossier – smzhHub')
    for skey,*_ in SERIES:
        write('de/'+SERIES_BY[skey][2]+'/', series_page(skey), f'{SERIES_BY[skey][0]} – smzhHub')
    write('de/smzhub-archiv/', archiv_inner(orig), 'Alle Inhalte – smzhHub')
    print('OK V2: Home, 4 Rubriken, Research, 2 Dossiers, 3 Serien, Archiv.')

if __name__=='__main__':
    main()
