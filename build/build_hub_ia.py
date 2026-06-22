#!/usr/bin/env python3
"""Iteration 3 – Neue Informationsarchitektur fuer den smzhHub.
Baut aus der bestehenden, voll ausgestatteten Hub-Seite (Chrome: Nav, Mega-/Mobile-
Menue, Footer, Skripte) eine kuratierte Startseite + 4 Themen-Landingpages + Archiv.
Datengetrieben aus build/smzhhub-content.json. Echte Inhalte/Links (Existenz geprueft).
Kein Deploy/Push. Schreibt nur unter site/smzh.ch/de/.
"""
import json, os, re, html as H
from datetime import datetime

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch')
CHROME_SRC='build/backup/pre-ia/smzhub-index.html'   # stabile Chrome-Quelle
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
P='../../'  # alle neuen Seiten liegen unter /de/<slug>/  (Tiefe 2)

# ---------- Helpers ----------
MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli',
     'Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try:
        d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def page_link(path):  # path '/de/x/...' -> relativ
    segs=[s for s in path.strip('/').split('/') if s]; return P+'/'.join(segs)+'/index.html'
def exists(path): return os.path.exists(os.path.join(SMZH, path.strip('/'), 'index.html'))
def localimg(r):
    il=r.get('imageLocal')
    if not il: return None
    return P+il[len('smzh.ch/'):].replace('%','%25').replace('&','&amp;')

def by(hubtype=None, topics=None, series=None):
    out=[]
    for r in rows:
        if hubtype and r['hubType']!=hubtype: continue
        if series is not None and r.get('series')!=series: continue
        if topics and not (set(r.get('topics') or []) & set(topics)): continue
        out.append(r)
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)

# ---------- Curation config (echte Seiten) ----------
THEMES={
 'kapitalmaerkte':{'slug':'smzhub-kapitalmaerkte','title':'Kapitalmärkte & Anlegen',
   'intro':'Märkte einordnen, Strategie schärfen: Einschätzungen zu Zinsen, Aktien, Obligationen und Portfolio – plus unser monatlicher Investment Guide.',
   'topics':['Anlagen','Finanzen'],'series':['investment-guide'],
   'evergreen':[('Anlagestrategie verstehen','de/anlagestrategie/'),('Risikoprofil erstellen','de/risikoprofil-erstellen/'),
                ('Leitfaden Anlageberatung','de/leitfaden-zur-anlageberatung-in-der-schweiz/'),
                ('Kosten & Gebühren beim Investieren','de/kosten-and-gebuehren-beim-investieren/'),
                ('Investieren statt Sparen','de/investieren-ist-das-neue-sparen/')],
   'rechner':[('Sparrechner','de/sparrechner/')],'cta':('Anlagestrategie besprechen','de/terminvereinbaren/')},
 'immobilien':{'slug':'smzhub-immobilien','title':'Immobilien & Hypotheken',
   'intro':'Vom Eigenheim-Traum zur tragbaren Finanzierung: Hypothekarstrategie, Marktlage und Praxiswissen – mit Hypotheken-Radar und Immobilien-Outlook.',
   'topics':['Immobilien','Hypotheken'],'series':['hypothekenradar','immobilien-outlook'],
   'evergreen':[('Tragbarkeit optimieren','de/optimierung-der-tragbarkeit/'),('Hypothekenarten im Vergleich','de/hypothekenarten-im-vergleich/'),
                ('Wie kaufe ich eine Immobilie?','de/wie-kaufe-ich-eine-immobilie/'),('Eigenkapital fürs Eigenheim','de/artikel/immobilien-kaufen-eigenkapital/'),
                ('Wohneigentumsförderung','de/wohneigentumsfoerderung/'),('Hypotheken-Guide 2026','de/hypotheken-guide-2026/')],
   'rechner':[('Immobilienbewertung','de/immobilienbewertung-rechner/'),('Budgetrechner','de/budgetrechner/')],
   'cta':('Hypothek prüfen lassen','de/immobilienbewertung/')},
 'vorsorge':{'slug':'smzhub-vorsorge','title':'Vorsorge & Pensionierung',
   'intro':'AHV, Pensionskasse und Säule 3a verständlich gemacht – damit Ihre Pensionierung planbar wird, in jeder Lebensphase.',
   'topics':['Vorsorge'],'series':[],
   'evergreen':[('Das 3-Säulen-System','de/das-3-saeulensystem-der-schweiz/'),('Säule 3a optimal nutzen','de/altersvorsorge-optimierung-saeule-3a/'),
                ('Pensionsplanung','de/pensionsplanung/'),('Leistungen im Alter','de/leistungen-im-alter/'),
                ('Frauen & Finanzen','de/frauen-finanzen-wissen-chancen/')],
   'rechner':[],'cta':('Vorsorge analysieren','de/vorsorgeanalyse/')},
 'steuern':{'slug':'smzhub-steuern','title':'Steuern & Finanzplanung',
   'intro':'Steuern senken, Vermögen strukturieren: konkrete Tipps und Grundlagen zu Abzügen, Wohneigentum, Kapitalbezug und Finanzplanung.',
   'topics':['Steuern','Finanzen'],'series':[],
   'evergreen':[('Steuerabzüge optimal nutzen','de/steuerabzuege-optimal-nutzen/'),('Grundlagen Steuererklärung','de/grundlagen-zur-steuererklaerung/'),
                ('Steuern bei Wohneigentum','de/steuern-wohneigentum/'),('Steuern beim Kapitalbezug','de/steuern-beim-kapitalbezug/'),
                ('Finanzplan erstellen','de/finanzplan-erstellen/')],
   'rechner':[('Steuerrechner','de/steuerrechner/')],'cta':('Steuern optimieren','de/steuererklaerung/')},
}
THEME_ORDER=['kapitalmaerkte','immobilien','vorsorge','steuern']
THEME_DESC={'kapitalmaerkte':'Investment Guide, Marktkommentare, Anlagestrategie.',
 'immobilien':'Hypotheken-Radar, Immobilien-Outlook, Eigenheim & Tragbarkeit.',
 'vorsorge':'AHV, Pensionskasse, Säule 3a, Pensionierung.',
 'steuern':'Steuern sparen, Vorsorgebezüge, Finanzplanung.'}
SERIES_META={'hypothekenradar':('Hypotheken-Radar','Monatlich'),'investment-guide':('Investment Guide','Monatlich'),
             'immobilien-outlook':('Immobilien-Outlook','Quartalsweise')}
ORIENT=[('Ich möchte ein Eigenheim kaufen','immobilien'),('Ich will meine Hypothek optimieren','immobilien'),
        ('Ich möchte mein Geld besser anlegen','kapitalmaerkte'),('Ich plane meine Pensionierung','vorsorge'),
        ('Ich will Steuern sparen','steuern'),('Ich suche aktuelle Markteinschätzungen','kapitalmaerkte')]
HOME_EVERGREEN=[('Das 3-Säulen-System','de/das-3-saeulensystem-der-schweiz/'),('Tragbarkeit optimieren','de/optimierung-der-tragbarkeit/'),
 ('Anlagestrategie verstehen','de/anlagestrategie/'),('Steuerabzüge optimal nutzen','de/steuerabzuege-optimal-nutzen/'),
 ('Wie kaufe ich eine Immobilie?','de/wie-kaufe-ich-eine-immobilie/'),('Frauen & Finanzen','de/frauen-finanzen-wissen-chancen/')]

# ---------- HTML-Bausteine ----------
def kommentar_card(r):
    chip=(r.get('topics') or [''])[0]
    img=localimg(r)
    cover=f'<a class="kc-img" href="{page_link(r["path"])}"><img loading="lazy" src="{img}" alt=""></a>' if img else ''
    rt=f'<span class="kc-rt">{r["readingTime"]} Min</span>' if r.get('readingTime') else ''
    return (f'<article class="kc">{cover}<div class="kc-b">'
            f'<div class="kc-meta"><span class="kc-chip">{esc(chip)}</span><time>{fdate(r.get("date"))}</time>{rt}</div>'
            f'<a class="kc-title" href="{page_link(r["path"])}">{esc(r["title"])}</a></div></article>')

def series_card(key):
    items=by(series=key)
    if not items: return ''
    n=items[0]; name,cad=SERIES_META[key]; img=localimg(n)
    cover=f'<a class="rs-cover" href="{page_link(n["path"])}"><img loading="lazy" src="{img}" alt=""></a>' if img else ''
    pdf=f'<a class="rs-pdf" href="{P}../cms.smzh.ch/uploads/{n["pdfs"][0]}" target="_blank" rel="noopener">PDF</a>' if n.get('pdfs') else ''
    return (f'<article class="rs-card"><div class="rs-badge">{cad}</div>{cover}<div class="rs-body">'
            f'<h3 class="rs-name">{esc(name)}</h3>'
            f'<div class="rs-latest"><span class="rs-latest-label">Aktuelle Ausgabe</span>'
            f'<a class="rs-latest-link" href="{page_link(n["path"])}">{esc(n["title"])}</a>'
            f'<time class="rs-date">{fdate(n.get("date"))}</time></div>'
            f'<div class="rs-actions"><a class="rs-primary" href="{page_link(n["path"])}">Lesen</a>{pdf}</div></div></article>')

def evergreen_list(pairs):
    lis=''
    for label,tail in pairs:
        if exists(tail):
            lis+=f'<a class="eg-item" href="{page_link(tail)}"><span>{esc(label)}</span><i>→</i></a>'
    return lis

def sec_head(title, sub=''):
    s=f'<p class="hub-sub">{esc(sub)}</p>' if sub else ''
    return f'<div class="hub-h"><h2>{esc(title)}</h2>{s}</div>'

# ---------- Seiteninhalte ----------
def home_inner():
    orient=''.join(f'<a class="or-item" href="{page_link("de/"+THEMES[t]["slug"]+"/")}"><span>{esc(lbl)}</span><i>→</i></a>' for lbl,t in ORIENT)
    themecards=''
    for t in THEME_ORDER:
        th=THEMES[t]; cnt=len(by(topics=th['topics']))
        themecards+=(f'<a class="tw-card tw-{t}" href="{page_link("de/"+th["slug"]+"/")}">'
                     f'<h3>{esc(th["title"])}</h3><p>{esc(THEME_DESC[t])}</p>'
                     f'<span class="tw-link">{cnt} Beiträge ansehen →</span></a>')
    stream=''.join(kommentar_card(r) for r in by(hubtype='kommentar')[:5])
    research=''.join(series_card(k) for k in ['hypothekenradar','investment-guide','immobilien-outlook'])
    evergreen=evergreen_list(HOME_EVERGREEN)
    return (
    '<section class="hub-hero"><h1>Finanzwissen, das Entscheidungen einfacher macht.</h1>'
    '<p>Analysen, Ratgeber und Einschätzungen zu Hypotheken, Immobilien, Anlagen, Vorsorge und Steuern – ruhig und auf den Punkt.</p></section>'
    f'<section class="hub-orient">{sec_head("Was beschäftigt Sie gerade?")}<div class="or-grid">{orient}</div></section>'
    f'<section class="hub-themes">{sec_head("Themenwelten","Vier Welten, ein Ziel: bessere finanzielle Entscheidungen.")}<div class="tw-grid">{themecards}</div></section>'
    f'<section class="hub-stream">{sec_head("Aktuelle Einschätzungen","Kuratiert – nicht chronologisch.")}<div class="kc-grid">{stream}</div>'
    f'<a class="hub-more" href="{page_link("de/smzhub-archiv/")}">Alle Inhalte ansehen →</a></section>'
    f'<section id="smzh-research" aria-label="Research">{sec_head("Research & Publikationen","Unsere wiederkehrenden Einschätzungen.")}<div class="rs-grid">{research}</div></section>'
    f'<section class="hub-eg">{sec_head("Evergreen-Guides","Zeitlose Orientierung für grundsätzliche Entscheidungen.")}<div class="eg-grid">{evergreen}</div></section>'
    f'<section class="hub-cta"><div><h2>Persönliche Beratung?</h2><p>Wir begleiten Sie bei Hypotheken, Vorsorge, Anlagen und Steuern.</p></div>'
    f'<a class="hub-cta-btn" href="{page_link("de/terminvereinbaren/")}">Beratung vereinbaren</a></section>')

def theme_inner(key):
    th=THEMES[key]
    komm=''.join(kommentar_card(r) for r in by(hubtype='kommentar', topics=th['topics'])[:6])
    series=''.join(series_card(k) for k in th['series'])
    series_block=(f'<section id="smzh-research">{sec_head("Relevante Serien")}<div class="rs-grid">{series}</div></section>') if series else ''
    eg=evergreen_list(th['evergreen'])
    rech=''.join(f'<a class="eg-item" href="{page_link(p)}"><span>{esc(l)}</span><i>→</i></a>' for l,p in th['rechner'] if exists(p))
    rech_block=(f'<section class="hub-eg">{sec_head("Rechner & Tools")}<div class="eg-grid">{rech}</div></section>') if rech else ''
    cta_l,cta_p=th['cta']
    crumb=f'<nav class="hub-crumb"><a href="{page_link("de/smzhub/")}">smzHub</a> <span>/</span> {esc(th["title"])}</nav>'
    return (
    f'{crumb}<section class="hub-hero hub-hero-theme"><h1>{esc(th["title"])}</h1><p>{esc(th["intro"])}</p></section>'
    f'<section class="hub-stream">{sec_head("Aktuelle Einschätzungen")}<div class="kc-grid">{komm}</div></section>'
    f'{series_block}'
    f'<section class="hub-eg">{sec_head("Evergreen-Guides")}<div class="eg-grid">{eg}</div></section>'
    f'{rech_block}'
    f'<section class="hub-cta"><div><h2>{esc(cta_l)}?</h2><p>Sprechen Sie mit unseren Expertinnen und Experten.</p></div>'
    f'<a class="hub-cta-btn" href="{page_link(cta_p)}">{esc(cta_l)}</a></section>')

def archiv_inner(orig_inner):
    # Research-Sektion aus dem alten Inner entfernen -> nur Filter + Grid behalten
    body=re.sub(r'<section id="smzh-research".*?</section>','',orig_inner,flags=re.S)
    crumb=f'<nav class="hub-crumb"><a href="{page_link("de/smzhub/")}">smzHub</a> <span>/</span> Alle Inhalte</nav>'
    intro=('<section class="hub-hero hub-hero-theme"><h1>Alle Inhalte</h1>'
           '<p>Das vollständige Archiv aller Beiträge, Publikationen, Talks und Podcasts.</p></section>')
    return crumb+intro+body

IA_STYLE='''<style id="smzh-ia-css">
#smzh-ia-root .hub-hero{padding:2.2rem 0 1.4rem}
#smzh-ia-root .hub-hero h1{font-size:clamp(1.9rem,4.2vw,3rem);font-weight:700;color:#07314C;line-height:1.12;margin:0 0 .7rem;max-width:18ch}
#smzh-ia-root .hub-hero p{font-size:clamp(1rem,1.6vw,1.2rem);color:#5b6b7a;margin:0;max-width:60ch}
#smzh-ia-root .hub-hero-theme h1{max-width:24ch}
#smzh-ia-root section{margin-bottom:2.8rem}
#smzh-ia-root .hub-h{margin:0 0 1.1rem}
#smzh-ia-root .hub-h h2{font-size:clamp(1.35rem,2.4vw,1.8rem);font-weight:700;color:#07314C;margin:0}
#smzh-ia-root .hub-sub{color:#7a8893;margin:.25rem 0 0}
#smzh-ia-root .or-grid{display:grid;gap:.7rem;grid-template-columns:1fr}
@media(min-width:640px){#smzh-ia-root .or-grid{grid-template-columns:1fr 1fr}}
@media(min-width:1024px){#smzh-ia-root .or-grid{grid-template-columns:1fr 1fr 1fr}}
#smzh-ia-root .or-item{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:1rem 1.2rem;border:1px solid #e7ebef;border-radius:12px;background:#fff;color:#07314C;text-decoration:none;font-weight:600;transition:.15s}
#smzh-ia-root .or-item:hover{border-color:#0050ff;box-shadow:0 4px 18px rgba(7,49,76,.07)}
#smzh-ia-root .or-item i{color:#0050ff;font-style:normal}
#smzh-ia-root .tw-grid{display:grid;gap:1rem;grid-template-columns:1fr}
@media(min-width:768px){#smzh-ia-root .tw-grid{grid-template-columns:1fr 1fr}}
#smzh-ia-root .tw-card{display:block;padding:1.6rem;border-radius:14px;text-decoration:none;background:#f4f7fa;border:1px solid #e7ebef;transition:.15s}
#smzh-ia-root .tw-card:hover{transform:translateY(-2px);box-shadow:0 10px 28px rgba(7,49,76,.10)}
#smzh-ia-root .tw-card h3{margin:0 0 .4rem;color:#07314C;font-size:1.3rem}
#smzh-ia-root .tw-card p{margin:0 0 .9rem;color:#5b6b7a;font-size:.95rem}
#smzh-ia-root .tw-link{color:#0050ff;font-weight:600;font-size:.9rem}
#smzh-ia-root .kc-grid{display:grid;gap:1.1rem;grid-template-columns:1fr}
@media(min-width:640px){#smzh-ia-root .kc-grid{grid-template-columns:1fr 1fr}}
@media(min-width:1024px){#smzh-ia-root .kc-grid{grid-template-columns:1fr 1fr 1fr}}
#smzh-ia-root .kc{border:1px solid #e7ebef;border-radius:12px;overflow:hidden;background:#fff;display:flex;flex-direction:column}
#smzh-ia-root .kc-img{display:block;aspect-ratio:16/10;overflow:hidden;background:#eef2f6}
#smzh-ia-root .kc-img img{width:100%;height:100%;object-fit:cover}
#smzh-ia-root .kc-b{padding:.9rem 1rem 1.1rem;display:flex;flex-direction:column;gap:.45rem}
#smzh-ia-root .kc-meta{display:flex;align-items:center;gap:.6rem;font-size:.75rem;color:#9aa7b2}
#smzh-ia-root .kc-chip{background:#eaf0f6;color:#0050ff;font-weight:600;padding:.15rem .5rem;border-radius:999px;text-transform:uppercase;letter-spacing:.02em;font-size:.68rem}
#smzh-ia-root .kc-title{color:#07314C;font-weight:600;text-decoration:none;line-height:1.32}
#smzh-ia-root .kc-title:hover{text-decoration:underline}
#smzh-ia-root .hub-more{display:inline-block;margin-top:1.1rem;color:#0050ff;font-weight:600;text-decoration:none}
#smzh-ia-root .eg-grid{display:grid;gap:.7rem;grid-template-columns:1fr}
@media(min-width:640px){#smzh-ia-root .eg-grid{grid-template-columns:1fr 1fr}}
@media(min-width:1024px){#smzh-ia-root .eg-grid{grid-template-columns:1fr 1fr 1fr}}
#smzh-ia-root .eg-item{display:flex;justify-content:space-between;align-items:center;gap:1rem;padding:.9rem 1.1rem;border:1px solid #eef1f4;border-radius:10px;background:#fff;color:#07314C;text-decoration:none;font-weight:500}
#smzh-ia-root .eg-item:hover{border-color:#0050ff}
#smzh-ia-root .eg-item i{color:#0050ff;font-style:normal}
#smzh-ia-root .hub-cta{display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;justify-content:space-between;background:#07314C;border-radius:16px;padding:2rem}
#smzh-ia-root .hub-cta h2{color:#fff;margin:0 0 .3rem;font-size:1.5rem}
#smzh-ia-root .hub-cta p{color:#c7d6e2;margin:0}
#smzh-ia-root .hub-cta-btn{background:#fff;color:#07314C;font-weight:700;text-decoration:none;padding:.85rem 1.6rem;border-radius:10px;white-space:nowrap}
#smzh-ia-root .hub-crumb{font-size:.85rem;color:#9aa7b2;padding-top:1.2rem}
#smzh-ia-root .hub-crumb a{color:#0050ff;text-decoration:none}
#smzh-ia-root .hub-crumb span{margin:0 .3rem}
</style>'''

# ---------- Chrome extrahieren + Seiten schreiben ----------
def balanced_div_end(s, start):
    depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>', s[start:]):
        depth+= 1 if m.group(1)=='' else -1
        if depth==0: return start+m.end()
    return -1

def main():
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*">', html)
    openEnd=m.end(); closeEnd=balanced_div_end(html, m.start())
    chrome_before=html[:openEnd]
    chrome_after=html[closeEnd-6:]              # ab '</div>' der content-hub
    orig_inner=html[openEnd:closeEnd-6]
    # IA-Style in <head> + Root-Wrapper-Klasse fuer scoping
    if 'id="smzh-ia-css"' not in chrome_before:
        chrome_before=chrome_before.replace('</head>', IA_STYLE+'</head>',1)
    # content-hub bekommt zusaetzlich id=smzh-ia-root (fuer CSS-Scope)
    chrome_before=re.sub(r'(<div class="content-hub[^"]*")>', r'\1 id="smzh-ia-root">', chrome_before, count=1)

    def write(path, inner, title):
        full=chrome_before+inner+chrome_after
        full=re.sub(r'<title>.*?</title>', '<title>'+H.escape(title)+'</title>', full, count=1, flags=re.S)
        d=os.path.join(SMZH, path.strip('/')); os.makedirs(d, exist_ok=True)
        open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)

    write('de/smzhub/', home_inner(), 'smzHub – Finanzwissen für Ihre Entscheidungen')
    for key in THEME_ORDER:
        th=THEMES[key]; write('de/'+th['slug']+'/', theme_inner(key), f'{th["title"]} – smzHub')
    write('de/smzhub-archiv/', archiv_inner(orig_inner), 'Alle Inhalte – smzHub')

    pages=['de/smzhub/','de/smzhub-archiv/']+['de/'+THEMES[k]['slug']+'/' for k in THEME_ORDER]
    print('Seiten geschrieben:'); [print('  /'+p) for p in pages]

if __name__=='__main__':
    main()
