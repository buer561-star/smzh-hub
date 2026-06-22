#!/usr/bin/env python3
"""Iteration 4 – Editorial-Neubau des smzhHub.
Kuratierter, redaktioneller Wissens-Hub statt Kachelwand:
- Themen-Reiterleiste (oben)
- asymmetrischer Hero: Intro links + dominanter Slider (Top-3) rechts
- modulare Editorial-Sektionen (grosser Leitartikel + 3 kleinere)
- elegante Serien-Rubrik (Regelmaessige Publikationen) + eigene Serienseiten
- editoriale Evergreen/Grundlagen-Rubrik
Chrome (Nav/Menue/Footer/Skripte) wird aus dem bestehenden Hub wiederverwendet.
Daten aus build/smzhhub-content.json. Kein Dummy. Schreibt nur unter site/smzh.ch/de/.
"""
import json, os, re, html as H, urllib.parse
from datetime import datetime
import sys; sys.path.insert(0,'build')
import postprocess_all as P

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch')
CHROME_SRC='build/backup/pre-ia/smzhub-index.html'   # volle Chrome ohne IA-CSS
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
P_='../../'

MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def teaser(r,n=150):
    t=r.get('excerpt') or ''
    return (t[:n].rsplit(' ',1)[0]+'…') if len(t)>n else t
def link(path):
    segs=[s for s in path.strip('/').split('/') if s]; return P_+'/'.join(segs)+'/index.html'
def exists(path): return os.path.exists(os.path.join(SMZH,path.strip('/'),'index.html'))

def opt_img(cms_path, w):
    """Lokale Optimizer-Variante in Breite w; laedt bei Bedarf nach. None wenn kein Bild."""
    if not cms_path: return None
    enc=urllib.parse.quote('https://cms.smzh.ch'+cms_path, safe='')
    dest=os.path.join(SMZH,'_next','image',f'index.html@url={enc}&w={w}&q=75')
    P.download(f'https://smzh.ch/_next/image/?url={enc}&w={w}&q=75', dest)
    if not os.path.exists(dest): return None
    return P_+'_next/image/index.html@url='+enc.replace('%','%25')+f'&amp;w={w}&amp;q=75'
def img_of(r,w): return opt_img(r.get('image'), w)

def kommentare(topics=None):
    out=[r for r in rows if r['hubType']=='kommentar' and (not topics or set(r.get('topics') or [])&set(topics))]
    return sorted(out, key=lambda r:r.get('date') or '', reverse=True)
def series_items(key): return sorted([r for r in rows if r.get('series')==key], key=lambda r:r.get('date') or '', reverse=True)

# ---- Themen / Serien Konfiguration ----
THEMES=[
 ('alle','Alle','de/smzhub/',None),
 ('kapitalmaerkte','Kapitalmärkte & Anlegen','de/smzhub-kapitalmaerkte/',['Anlagen','Finanzen']),
 ('immobilien','Immobilien & Hypotheken','de/smzhub-immobilien/',['Immobilien','Hypotheken']),
 ('vorsorge','Vorsorge & Pensionierung','de/smzhub-vorsorge/',['Vorsorge']),
 ('steuern','Steuern & Finanzplanung','de/smzhub-steuern/',['Steuern','Finanzen']),
]
THEME_BY={k:(lbl,path,tp) for k,lbl,path,tp in THEMES}
THEME_INTRO={
 'kapitalmaerkte':'Märkte einordnen, Strategie schärfen – Einschätzungen zu Zinsen, Aktien, Obligationen und Portfolio.',
 'immobilien':'Vom Eigenheim zur tragbaren Finanzierung – Hypothekarstrategie, Marktlage und Praxiswissen.',
 'vorsorge':'AHV, Pensionskasse und Säule 3a verständlich – damit Ihre Pensionierung planbar wird.',
 'steuern':'Steuern senken, Vermögen strukturieren – konkrete Tipps und solide Grundlagen.'}
SERIES=[
 ('hypothekenradar','Hypotheken-Radar','Monatlich','smzhub-serie-hypotheken-radar','immobilien',
   'Monatliche Einschätzung zu Zinsen, Festhypotheken und Schweizer Hypothekarmarkt.'),
 ('investment-guide','Investment Guide','Monatlich','smzhub-serie-investment-guide','kapitalmaerkte',
   'Monatliche Anlageeinschätzung – Märkte, Strategie und Portfoliothemen.'),
 ('immobilien-outlook','Immobilien-Outlook','Quartalsweise','smzhub-serie-immobilien-outlook','immobilien',
   'Quartalsweise Analyse des Schweizer Immobilienmarkts.'),
]
SERIES_BY={k:(name,cad,slug,theme,desc) for k,name,cad,slug,theme,desc in SERIES}
EVERGREEN={ # echte Seiten
 'kapitalmaerkte':[('Anlagestrategie verstehen','de/anlagestrategie/'),('Risikoprofil erstellen','de/risikoprofil-erstellen/'),('Leitfaden Anlageberatung','de/leitfaden-zur-anlageberatung-in-der-schweiz/'),('Kosten & Gebühren beim Investieren','de/kosten-and-gebuehren-beim-investieren/')],
 'immobilien':[('Tragbarkeit optimieren','de/optimierung-der-tragbarkeit/'),('Hypothekenarten im Vergleich','de/hypothekenarten-im-vergleich/'),('Wie kaufe ich eine Immobilie?','de/wie-kaufe-ich-eine-immobilie/'),('Wohneigentumsförderung','de/wohneigentumsfoerderung/')],
 'vorsorge':[('Das 3-Säulen-System','de/das-3-saeulensystem-der-schweiz/'),('Säule 3a optimal nutzen','de/altersvorsorge-optimierung-saeule-3a/'),('Pensionsplanung','de/pensionsplanung/'),('Leistungen im Alter','de/leistungen-im-alter/')],
 'steuern':[('Steuerabzüge optimal nutzen','de/steuerabzuege-optimal-nutzen/'),('Grundlagen Steuererklärung','de/grundlagen-zur-steuererklaerung/'),('Steuern bei Wohneigentum','de/steuern-wohneigentum/'),('Finanzplan erstellen','de/finanzplan-erstellen/')],
}
EVERGREEN_HOME=[('Das 3-Säulen-System','de/das-3-saeulensystem-der-schweiz/'),('Tragbarkeit optimieren','de/optimierung-der-tragbarkeit/'),('Anlagestrategie verstehen','de/anlagestrategie/'),('Steuerabzüge optimal nutzen','de/steuerabzuege-optimal-nutzen/'),('Wie kaufe ich eine Immobilie?','de/wie-kaufe-ich-eine-immobilie/'),('Säule 3a optimal nutzen','de/altersvorsorge-optimierung-saeule-3a/'),('Risikoprofil erstellen','de/risikoprofil-erstellen/'),('Finanzplan erstellen','de/finanzplan-erstellen/')]
THEME_CTA={'kapitalmaerkte':('Anlagestrategie besprechen','de/terminvereinbaren/'),'immobilien':('Hypothek prüfen lassen','de/immobilienbewertung/'),'vorsorge':('Vorsorge analysieren','de/vorsorgeanalyse/'),'steuern':('Steuern optimieren','de/steuererklaerung/')}

# ---- Komponenten ----
def themebar(active):
    items=''
    for k,lbl,path,tp in THEMES:
        cls='tb-link'+(' tb-active' if k==active else '')
        items+=f'<a class="{cls}" href="{link(path)}">{esc(lbl)}</a>'
    return f'<nav class="ed-themebar" aria-label="Themenwelten"><div class="tb-inner">{items}</div></nav>'

def hero(slider_items):
    slides=''; dots=''
    for i,r in enumerate(slider_items):
        im=img_of(r,1200);
        bg=f'<img src="{im}" alt="">' if im else ''
        chip=(r.get('topics') or [''])[0]
        slides+=(f'<a class="hslide{" active" if i==0 else ""}" href="{link(r["path"])}">'
                 f'<div class="hslide-img">{bg}</div><div class="hslide-grad"></div>'
                 f'<div class="hslide-txt"><span class="hslide-chip">{esc(chip)}</span>'
                 f'<h3>{esc(r["title"])}</h3><p>{esc(teaser(r,120))}</p>'
                 f'<span class="hslide-meta">{fdate(r.get("date"))}</span></div></a>')
        dots+=f'<span class="hdot{" active" if i==0 else ""}" role="button" tabindex="0" aria-label="Beitrag {i+1}"></span>'
    return (f'<section class="ed-hero"><div class="hero-intro">'
            f'<h1>Finanzwissen, das Entscheidungen einfacher macht.</h1>'
            f'<p>Analysen, Ratgeber und Einschätzungen zu Hypotheken, Immobilien, Anlagen, Vorsorge und Steuern – ruhig und auf den Punkt.</p>'
            f'<a class="hero-scroll" href="#ed-sections">Themen entdecken ↓</a></div>'
            f'<div class="hero-feature hslider"><div class="hslides">{slides}</div>'
            f'<span class="harrow hprev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
            f'<span class="harrow hnext" role="button" tabindex="0" aria-label="Weiter">›</span>'
            f'<div class="hdots">{dots}</div></div></section>')

def side_item(r):
    im=img_of(r,640); thumb=f'<span class="es-thumb"><img loading="lazy" src="{im}" alt=""></span>' if im else '<span class="es-thumb es-thumb-empty"></span>'
    return (f'<a class="es-item" href="{link(r["path"])}">{thumb}<span class="es-it-txt">'
            f'<span class="es-h4">{esc(r["title"])}</span>'
            f'<span class="es-p">{esc(teaser(r,80))}</span></span></a>')

def editorial_section(theme_key, items, more_path):
    if len(items)<1: return ''
    lead=items[0]; side=items[1:4]
    lbl=THEME_BY[theme_key][0]
    im=img_of(lead,1200); chip=(lead.get('topics') or [''])[0]
    leadimg=f'<div class="el-img"><img loading="lazy" src="{im}" alt=""></div>' if im else ''
    leadcard=(f'<a class="ed-lead" href="{link(lead["path"])}">{leadimg}'
              f'<div class="el-txt"><span class="es-chip">{esc(chip)}</span>'
              f'<h3>{esc(lead["title"])}</h3><p>{esc(teaser(lead,180))}</p>'
              f'<span class="el-meta">{fdate(lead.get("date"))}'
              + (f' · {lead["readingTime"]} Min' if lead.get("readingTime") else '') + '</span></div></a>')
    sidehtml=''.join(side_item(r) for r in side)
    return (f'<section class="ed-sec"><div class="ed-sec-head">'
            f'<h2>{esc(lbl)}</h2><a class="ed-sec-more" href="{link(more_path)}">Alle ansehen →</a></div>'
            f'<div class="ed-sec-body"><div class="ed-lead-wrap">{leadcard}</div>'
            f'<div class="ed-side">{sidehtml}</div></div></section>')

def series_rubric():
    rowshtml=''
    for key,name,cad,slug,theme,desc in SERIES:
        items=series_items(key)
        if not items: continue
        cur=items[0]
        rowshtml+=(f'<a class="ser-row ser-{theme}" href="{link("de/"+slug+"/")}">'
                   f'<span class="ser-cad">{esc(cad)}</span>'
                   f'<span class="ser-main"><span class="ser-name">{esc(name)}</span>'
                   f'<span class="ser-cur">Aktuell: {esc(cur["title"])}</span></span>'
                   f'<span class="ser-go">Zur Serie →</span></a>')
    return (f'<section class="ed-rubric ser-rubric"><div class="ed-rub-head">'
            f'<span class="ed-kicker">Research</span><h2>Regelmässige Publikationen</h2>'
            f'<p>Wiederkehrende Einschätzungen mit eigener Serienidentität.</p></div>'
            f'<div class="ser-list">{rowshtml}</div></section>')

def evergreen_rubric(pairs, title='Grundlagen & Evergreen-Guides'):
    lis=''
    n=0
    for lbl,tail in pairs:
        if not exists(tail): continue
        n+=1
        lis+=(f'<a class="eg-row" href="{link(tail)}"><span class="eg-num">{n:02d}</span>'
              f'<span class="eg-lbl">{esc(lbl)}</span><i>→</i></a>')
    return (f'<section class="ed-rubric eg-rubric"><div class="ed-rub-head">'
            f'<span class="ed-kicker">Grundlagen</span><h2>{esc(title)}</h2>'
            f'<p>Zeitlose Orientierung für grundsätzliche Entscheidungen.</p></div>'
            f'<div class="eg-list">{lis}</div></section>')

def cta(label, path):
    return (f'<section class="ed-cta"><div><h2>{esc(label)}?</h2>'
            f'<p>Wir begleiten Sie persönlich – unabhängig und auf Ihre Situation zugeschnitten.</p></div>'
            f'<a class="ed-cta-btn" href="{link(path)}">{esc(label)}</a></section>')

# ---- Seiteninhalte ----
def home_inner():
    used=set()
    hero_items=[r for r in kommentare() if r.get('image')][:3]
    for r in hero_items: used.add(r['id'])
    secs=''
    for key in ['kapitalmaerkte','immobilien','vorsorge','steuern']:
        pool=[r for r in kommentare(THEME_BY[key][2]) if r['id'] not in used]
        pick=pool[:4]
        for r in pick: used.add(r['id'])
        secs+=editorial_section(key, pick, THEME_BY[key][1])
    return (themebar('alle')+hero(hero_items)
            +'<div id="ed-sections">'+secs+'</div>'
            +series_rubric()
            +evergreen_rubric(EVERGREEN_HOME)
            +cta('Persönliche Beratung','de/terminvereinbaren/'))

def theme_inner(key):
    lbl,path,tp=THEME_BY[key]
    komm=kommentare(tp)
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>{esc(lbl)}</nav>'
    intro=(f'<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
           f'<span class="ed-kicker">Themenwelt</span><h1>{esc(lbl)}</h1><p>{esc(THEME_INTRO[key])}</p></div></section>')
    # Leitartikel + 3, dann ein zweiter Editorial-Block mit weiteren
    sec1=editorial_section(key, komm[:4], 'de/smzhub-archiv/')
    more=komm[4:10]
    morehtml=''
    if more:
        morehtml='<section class="ed-sec"><div class="ed-sec-head"><h2>Weitere Einschätzungen</h2></div><div class="es-grid">'+''.join(side_item(r) for r in more)+'</div></section>'
    # relevante Serien (als kompakte Rubrik, nur die zum Thema)
    rel=[s for s in SERIES if s[4]==key]
    serhtml=''
    if rel:
        rr=''
        for k2,name,cad,slug,theme,desc in rel:
            its=series_items(k2)
            if not its: continue
            rr+=(f'<a class="ser-row ser-{theme}" href="{link("de/"+slug+"/")}"><span class="ser-cad">{esc(cad)}</span>'
                 f'<span class="ser-main"><span class="ser-name">{esc(name)}</span><span class="ser-cur">Aktuell: {esc(its[0]["title"])}</span></span>'
                 f'<span class="ser-go">Zur Serie →</span></a>')
        serhtml=f'<section class="ed-rubric ser-rubric"><div class="ed-rub-head"><span class="ed-kicker">Research</span><h2>Relevante Serien</h2></div><div class="ser-list">{rr}</div></section>'
    eg=evergreen_rubric(EVERGREEN.get(key,[]), 'Evergreen-Guides')
    cl,cp=THEME_CTA[key]
    return themebar(key)+crumb+intro+sec1+morehtml+serhtml+eg+cta(cl,cp)

def series_inner(key):
    name,cad,slug,theme,desc=SERIES_BY[key]
    items=series_items(key); cur=items[0] if items else None
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>{esc(name)}</nav>'
    intro=(f'<section class="ed-hero ed-hero-theme"><div class="hero-intro">'
           f'<span class="ed-kicker">{esc(cad)} · Serie</span><h1>{esc(name)}</h1><p>{esc(desc)}</p></div></section>')
    cur_html=''
    if cur:
        im=img_of(cur,1200); cover=f'<div class="el-img"><img src="{im}" alt=""></div>' if im else ''
        pdf=f'<a class="rs-pdf" href="{P_}../cms.smzh.ch/uploads/{cur["pdfs"][0]}" target="_blank" rel="noopener">PDF ansehen</a>' if cur.get('pdfs') else ''
        cur_html=(f'<section class="ed-sec"><div class="ed-sec-head"><h2>Aktuelle Ausgabe</h2></div>'
                  f'<a class="ed-lead" href="{link(cur["path"])}">{cover}<div class="el-txt">'
                  f'<span class="es-chip">{esc(fdate(cur.get("date")))}</span><h3>{esc(cur["title"])}</h3>'
                  f'<p>{esc(teaser(cur,200))}</p><span class="el-actions"><span class="ed-cta-btn ed-cta-inline">Lesen</span>{pdf}</span></div></a></section>')
    arch=''
    for r in items[1:]:
        pdf=f'<a class="arch-pdf" href="{P_}../cms.smzh.ch/uploads/{r["pdfs"][0]}" target="_blank" rel="noopener">PDF</a>' if r.get('pdfs') else ''
        arch+=(f'<a class="arch-row" href="{link(r["path"])}"><time>{esc(fdate(r.get("date")))}</time>'
               f'<span class="arch-title">{esc(r["title"])}</span>{pdf}</a>')
    arch_html=f'<section class="ed-rubric"><div class="ed-rub-head"><span class="ed-kicker">Archiv</span><h2>Frühere Ausgaben ({len(items)-1})</h2></div><div class="arch-list">{arch}</div></section>' if len(items)>1 else ''
    return themebar(theme)+crumb+intro+cur_html+arch_html+cta('Beratung vereinbaren','de/terminvereinbaren/')

def archiv_inner(orig_inner):
    body=re.sub(r'<section id="smzh-research".*?</section>','',orig_inner,flags=re.S)
    crumb=f'<nav class="ed-crumb"><a href="{link("de/smzhub/")}">smzHub</a><span>/</span>Alle Inhalte</nav>'
    intro='<section class="ed-hero ed-hero-theme"><div class="hero-intro"><span class="ed-kicker">Archiv</span><h1>Alle Inhalte</h1><p>Das vollständige Verzeichnis aller Beiträge, Publikationen, Talks und Podcasts.</p></div></section>'
    return themebar(None)+crumb+intro+body

ED_CSS = '''<style id="smzh-ed-css">
#ed-root{--brand:#07314C;--accent:#0050ff;--muted:#5b6b7a;--faint:#9aa7b2;--line:#e7ebef;--bg:#f4f7fa}
#ed-root{gap:0 !important}
#ed-root section{margin:0 0 4rem}
#ed-root .ed-kicker{display:inline-block;font-size:.72rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700;margin-bottom:.5rem}
/* Themenreiter */
#ed-root .ed-themebar{margin:0 0 2.2rem;border-bottom:1px solid var(--line);overflow-x:auto}
#ed-root .tb-inner{display:flex;gap:1.8rem;min-width:max-content}
#ed-root .tb-link{padding:0 0 .9rem;color:var(--muted);text-decoration:none;font-weight:500;font-size:1rem;white-space:nowrap;border-bottom:2px solid transparent;transition:.15s}
#ed-root .tb-link:hover{color:var(--brand)}
#ed-root .tb-active{color:var(--brand);font-weight:700;border-bottom-color:var(--accent)}
/* Hero */
#ed-root .ed-hero{display:grid;grid-template-columns:1fr;gap:2rem;align-items:center;margin-bottom:4.5rem}
@media(min-width:900px){#ed-root .ed-hero{grid-template-columns:0.82fr 1.18fr;gap:3rem}}
#ed-root .hero-intro h1{font-size:clamp(2rem,4.4vw,3.3rem);font-weight:700;color:var(--brand);line-height:1.08;margin:0 0 1rem;letter-spacing:-.01em}
#ed-root .hero-intro p{font-size:clamp(1.05rem,1.6vw,1.25rem);color:var(--muted);margin:0 0 1.4rem;max-width:46ch;line-height:1.5}
#ed-root .hero-scroll{color:var(--accent);font-weight:600;text-decoration:none}
#ed-root .ed-hero-theme{display:block;margin-bottom:3rem;padding-top:.5rem}
#ed-root .ed-hero-theme h1{max-width:22ch}
/* Hero-Slider */
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
/* Editorial-Sektion */
#ed-root .ed-sec-head{display:flex;align-items:baseline;justify-content:space-between;gap:1rem;margin-bottom:1.3rem;border-top:2px solid var(--brand);padding-top:1rem}
#ed-root .ed-sec-head h2{font-size:clamp(1.4rem,2.4vw,1.9rem);font-weight:700;color:var(--brand);margin:0}
#ed-root .ed-sec-more{color:var(--accent);font-weight:600;text-decoration:none;white-space:nowrap;font-size:.92rem}
#ed-root .ed-sec-body{display:grid;grid-template-columns:1fr;gap:1.8rem}
@media(min-width:900px){#ed-root .ed-sec-body{grid-template-columns:1.45fr 1fr;gap:2.4rem}}
#ed-root .ed-lead{display:block;text-decoration:none;color:inherit;group:lead}
#ed-root .el-img{aspect-ratio:16/10;border-radius:14px;overflow:hidden;background:var(--bg);margin-bottom:1.1rem}
#ed-root .el-img img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
#ed-root .ed-lead:hover .el-img img{transform:scale(1.03)}
#ed-root .es-chip{display:inline-block;color:var(--accent);font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:.5rem}
#ed-root .el-txt h3{font-size:clamp(1.35rem,2.2vw,1.8rem);font-weight:700;color:var(--brand);margin:0 0 .6rem;line-height:1.2}
#ed-root .el-txt p{color:var(--muted);margin:0 0 .6rem;line-height:1.55}
#ed-root .el-meta{color:var(--faint);font-size:.82rem}
#ed-root .ed-side{display:flex;flex-direction:column}
#ed-root .es-item{display:flex;gap:1rem;padding:1.1rem 0;border-bottom:1px solid var(--line);text-decoration:none;color:inherit}
#ed-root .ed-side .es-item:first-child{padding-top:0}
#ed-root .es-thumb{flex:0 0 92px;width:92px;height:68px;border-radius:9px;overflow:hidden;background:var(--bg)}
#ed-root .es-thumb img{width:100%;height:100%;object-fit:cover}
#ed-root .es-it-txt{display:flex;flex-direction:column;gap:.25rem}
#ed-root .es-h4{font-weight:650;color:var(--brand);line-height:1.3;font-size:1rem}
#ed-root .es-item:hover .es-h4{color:var(--accent)}
#ed-root .es-p{color:var(--muted);font-size:.85rem;line-height:1.45}
#ed-root .es-grid{display:grid;grid-template-columns:1fr;gap:0}
@media(min-width:640px){#ed-root .es-grid{grid-template-columns:1fr 1fr;gap:0 2.4rem}}
/* Rubriken */
#ed-root .ed-rubric{background:var(--bg);border-radius:18px;padding:2.2rem}
#ed-root .ed-rub-head{margin-bottom:1.4rem}
#ed-root .ed-rub-head h2{font-size:clamp(1.4rem,2.4vw,1.9rem);font-weight:700;color:var(--brand);margin:0}
#ed-root .ed-rub-head p{color:var(--muted);margin:.3rem 0 0}
#ed-root .ser-list{display:flex;flex-direction:column;gap:.7rem}
#ed-root .ser-row{display:flex;align-items:center;gap:1.2rem;background:#fff;border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:1.1rem 1.4rem;text-decoration:none;color:inherit;transition:.15s}
#ed-root .ser-row:hover{box-shadow:0 8px 24px rgba(7,49,76,.08);transform:translateX(2px)}
#ed-root .ser-immobilien{border-left-color:#1b8a7a}#ed-root .ser-kapitalmaerkte{border-left-color:#0050ff}
#ed-root .ser-cad{flex:0 0 auto;font-size:.7rem;text-transform:uppercase;letter-spacing:.05em;color:var(--faint);font-weight:700;min-width:92px}
#ed-root .ser-main{flex:1;display:flex;flex-direction:column;gap:.15rem}
#ed-root .ser-name{font-weight:700;color:var(--brand);font-size:1.15rem}
#ed-root .ser-cur{color:var(--muted);font-size:.88rem}
#ed-root .ser-go{color:var(--accent);font-weight:600;white-space:nowrap;font-size:.9rem}
/* Evergreen */
#ed-root .eg-list{display:grid;grid-template-columns:1fr;gap:0 2.6rem}
@media(min-width:760px){#ed-root .eg-list{grid-template-columns:1fr 1fr}}
#ed-root .eg-row{display:flex;align-items:center;gap:1rem;padding:1rem .2rem;border-bottom:1px solid var(--line);text-decoration:none;color:var(--brand)}
#ed-root .eg-num{color:var(--faint);font-weight:700;font-size:.85rem;font-variant-numeric:tabular-nums}
#ed-root .eg-lbl{flex:1;font-weight:600}
#ed-root .eg-row i{color:var(--accent);font-style:normal}
#ed-root .eg-row:hover .eg-lbl{color:var(--accent)}
/* Archiv-Liste (Serienseite) */
#ed-root .arch-list{display:flex;flex-direction:column}
#ed-root .arch-row{display:flex;align-items:center;gap:1.2rem;padding:1rem .2rem;border-bottom:1px solid var(--line);text-decoration:none;color:var(--brand)}
#ed-root .arch-row time{flex:0 0 88px;color:var(--faint);font-size:.85rem}
#ed-root .arch-title{flex:1;font-weight:600}
#ed-root .arch-row:hover .arch-title{color:var(--accent)}
#ed-root .arch-pdf,#ed-root .rs-pdf{color:var(--accent);font-weight:600;text-decoration:none;font-size:.85rem}
/* CTA */
#ed-root .ed-cta{display:flex;flex-wrap:wrap;gap:1.2rem;align-items:center;justify-content:space-between;background:var(--brand);border-radius:18px;padding:2.4rem}
#ed-root .ed-cta h2{color:#fff;margin:0 0 .3rem;font-size:1.6rem}
#ed-root .ed-cta p{color:#c7d6e2;margin:0;max-width:52ch}
#ed-root .ed-cta-btn{background:#fff;color:var(--brand);font-weight:700;text-decoration:none;padding:.9rem 1.7rem;border-radius:10px;white-space:nowrap}
#ed-root .el-actions{display:flex;align-items:center;gap:1.2rem;margin-top:.4rem}
#ed-root .ed-cta-inline{display:inline-block;padding:.7rem 1.4rem}
#ed-root .ed-crumb{font-size:.85rem;color:var(--faint);margin:1rem 0 .5rem}
#ed-root .ed-crumb a{color:var(--accent);text-decoration:none}#ed-root .ed-crumb span{margin:0 .4rem}
</style>'''

SLIDER_JS = '''<script id="smzh-ed-js">
(function(){function ready(f){if(document.readyState!=='loading'){f();}else{document.addEventListener('DOMContentLoaded',f);}}
ready(function(){document.querySelectorAll('.hslider').forEach(function(s){
var sl=s.querySelectorAll('.hslide'),dt=s.querySelectorAll('.hdot'),i=0,n=sl.length,t=null;
if(n<2){return;}
function go(k){i=(k+n)%n;sl.forEach(function(e,j){e.classList.toggle('active',j===i);});dt.forEach(function(d,j){d.classList.toggle('active',j===i);});}
function auto(){t=setInterval(function(){go(i+1);},6500);}function reset(){clearInterval(t);auto();}
var nx=s.querySelector('.hnext'),pv=s.querySelector('.hprev');
if(nx)nx.addEventListener('click',function(e){e.preventDefault();go(i+1);reset();});
if(pv)pv.addEventListener('click',function(e){e.preventDefault();go(i-1);reset();});
dt.forEach(function(d,j){d.addEventListener('click',function(e){e.preventDefault();go(j);reset();});});
s.addEventListener('mouseenter',function(){clearInterval(t);});s.addEventListener('mouseleave',auto);
go(0);auto();});});})();
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
    chrome_before=html[:openTagEnd]
    chrome_after=html[closeEnd-6:]
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

    write('de/smzhub/', home_inner(), 'smzHub – Finanzwissen für Ihre Entscheidungen')
    for key in ['kapitalmaerkte','immobilien','vorsorge','steuern']:
        write(THEME_BY[key][1], theme_inner(key), f'{THEME_BY[key][0]} – smzHub')
    for k,name,cad,slug,theme,desc in SERIES:
        write('de/'+slug+'/', series_inner(k), f'{name} – smzHub')
    write('de/smzhub-archiv/', archiv_inner(orig_inner), 'Alle Inhalte – smzHub')
    print('OK: Home, 4 Themenseiten, 3 Serienseiten, Archiv geschrieben.')

if __name__=='__main__':
    main()
