#!/usr/bin/env python3
"""Erzeugt 3 eigenständige statische smzhHub-Konzepte (concept-a/b/c.html) unter
site/. Nutzt echte Inhalte aus build/smzhhub-content.json und lädt echte Bilder
nach site/concept-assets/ (saubere Dateinamen -> lokal per Doppelklick lauffähig).
Production (site/smzh.ch/de/smzhub*) wird NICHT verändert.
Referenzmuster: SS1 Flagship-Hero (Titel links, Spotlight rechts, gefilterte
Inhalte unten) · SS2 Topic-Sektion (grosser Lead links, kleine Items rechts) ·
SS3 Navy-Break (dunkler Research-/Signal-Block).
"""
import json, os, re, html as H
from datetime import datetime
import sys; sys.path.insert(0,'build')
import postprocess_all as P

SITE='site'; ASSETS=os.path.join(SITE,'concept-assets'); os.makedirs(ASSETS,exist_ok=True)
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso,short=False):
    if not iso: return ''
    try:
        d=datetime.fromisoformat(iso.replace('Z','+00:00'))
        return f"{d.day:02d}.{d.month:02d}.{d.year}" if short else f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def teaser(r,n=150):
    t=r.get('excerpt') or ''
    return (t[:n].rsplit(' ',1)[0]+'…') if len(t)>n else t
def alink(r):
    return 'smzh.ch/'+r['path'].strip('/')+'/index.html'
def komm(rk): return sorted([r for r in rows if r.get('rubric')==rk and r['hubType']=='kommentar' and r.get('hubEligible')],key=lambda r:r.get('date') or '',reverse=True)
def leads(rk): return sorted([r for r in rows if r.get('rubric')==rk and r.get('leadEligible')],key=lambda r:r.get('date') or '',reverse=True)
def series(k): return sorted([r for r in rows if r.get('series')==k],key=lambda r:r.get('date') or '',reverse=True)
def find(sub):
    for r in rows:
        if sub.lower() in (r['title'] or '').lower(): return r
    return None
def latest_month():
    ds=[r['date'] for r in rows if r.get('date')]
    return fdate(max(ds)) if ds else ''

def img_dl(r,_cache={}):
    if not r: return None
    img=r.get('image')
    if not img: return None
    if r['id'] in _cache: return _cache[r['id']]
    ext=os.path.splitext(img.split('?')[0])[1] or '.jpg'
    fn=f"{r['id']}{ext}"; dest=os.path.join(ASSETS,fn)
    if not os.path.exists(dest):
        try: P.download('https://cms.smzh.ch'+img, dest)
        except Exception: pass
    rel=f"concept-assets/{fn}" if os.path.exists(dest) else None
    _cache[r['id']]=rel; return rel
def imgt(r,cls='c-img'):
    rel=img_dl(r)
    return f'<img src="{rel}" alt="" class="{cls}">' if rel else f'<span class="{cls} c-img-ph"></span>'

CAT={'immobilien':'Eigenheim','kapitalmaerkte':'Vermögen','vorsorge':'Zukunft','steuern':'Steuern'}
SER={'hypothekenradar':('Hypotheken-Radar','Monatlich','Zinsen, Festhypotheken und der Schweizer Hypothekarmarkt.'),
 'investment-guide':('Investment Guide','Monatlich','Märkte, Strategie und Portfoliothemen.'),
 'immobilien-outlook':('Immobilien-Outlook','Quartalsweise','Analyse des Schweizer Immobilienmarkts.')}
DECISIONS=[('SARON oder Festhypothek?','Welche Laufzeit passt, wenn Zinsen tief bleiben, aber Sicherheit zählt?','Eigenheim','smzh.ch/de/hypothekenarten-im-vergleich/index.html'),
 ('Kaufen oder warten?','Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenspielen.','Eigenheim','smzh.ch/de/wie-kaufe-ich-eine-immobilie/index.html'),
 ('Rente oder Kapital?','Die Pensionierungsentscheidung, die selten sauber vorbereitet wird.','Zukunft','smzh.ch/de/leistungen-im-alter/index.html'),
 ('3a-Konto oder Wertschriften?','Warum Sparen allein über lange Zeiträume selten genügt.','Vermögen','smzh.ch/de/altersvorsorge-optimierung-saeule-3a/index.html')]
NAV=['Alle','Entscheiden','Eigenheim','Vermögen','Zukunft','Research']
TOPIC=[('Eigenheim & Finanzierung','immobilien','Kann ich mir mein Eigenheim leisten – und zu welchen Konditionen?',['hypothekenradar','immobilien-outlook'],('Hypothek prüfen lassen','smzh.ch/de/immobilienbewertung/index.html')),
 ('Vermögen aufbauen','kapitalmaerkte','Wie lege ich mein Vermögen sinnvoll und ruhig an?',['investment-guide'],('Anlagestrategie besprechen','smzh.ch/de/terminvereinbaren/index.html')),
 ('Zukunft planen','vorsorge','Reicht mein Geld bis zur und in der Pensionierung?',[],('Vorsorge analysieren','smzh.ch/de/vorsorgeanalyse/index.html'))]

# ---------- gemeinsame Render-Bausteine ----------
def chip(rk): return f'<span class="c-chip c-chip-{rk}">{esc(CAT.get(rk,"smzh"))}</span>'
def meta(r):
    m=fdate(r.get('date'))
    if r.get('readingTime'): m+=f' · {r["readingTime"]} Min'
    return m

def topbar(active='Alle'):
    tabs=''.join(f'<a class="c-tab{" is-on" if t==active else ""}" href="#">{t}</a>' for t in NAV)
    return (f'<header class="c-top"><div class="c-top-in"><a class="c-logo" href="#">smzh<b>Hub</b></a>'
            f'<nav class="c-tabs">{tabs}</nav><a class="c-top-cta" href="smzh.ch/de/terminvereinbaren/index.html">Termin vereinbaren</a></div></header>')

def lead_big(r, kicker='Im Fokus'):
    return (f'<a class="c-lead" href="{alink(r)}"><span class="c-lead-img">{imgt(r,"c-img")}</span>'
            f'<span class="c-lead-b"><span class="c-ey">{esc(kicker)}</span>'
            f'<span class="c-lead-h">{esc(r["title"])}</span>'
            f'<span class="c-lead-p">{esc(teaser(r,160))}</span>'
            f'<span class="c-lead-m">{chip(r.get("rubric"))}<span class="c-date">{meta(r)}</span></span></span></a>')

def list_row(r):
    return (f'<a class="c-row" href="{alink(r)}"><span class="c-row-th">{imgt(r,"c-img")}</span>'
            f'<span class="c-row-b"><span class="c-row-h">{esc(r["title"])}</span>'
            f'<span class="c-row-m">{esc(CAT.get(r.get("rubric"),"smzh"))} · {fdate(r.get("date"))}</span></span></a>')

def link_row(r):
    return (f'<a class="c-lrow" href="{alink(r)}"><span class="c-lrow-h">{esc(r["title"])}</span>'
            f'<span class="c-lrow-m">{esc(CAT.get(r.get("rubric"),"smzh"))} · {fdate(r.get("date"))}</span></a>')

def flag_card(skey, big=False):
    name,cad,desc=SER[skey]; its=series(skey)
    if not its: return ''
    cur=its[0]
    return (f'<a class="c-flag{" c-flag-big" if big else ""}" href="{alink(cur)}">'
            f'<span class="c-flag-cov">{imgt(cur,"c-img")}<span class="c-flag-badge">{esc(cad)}</span></span>'
            f'<span class="c-flag-b"><span class="c-flag-k">Flagship-Research · {len(its)} Ausgaben</span>'
            f'<span class="c-flag-n">{esc(name)}</span><span class="c-flag-d">{esc(desc)}</span>'
            f'<span class="c-flag-cur">Aktuell: {esc(cur["title"])}</span>'
            f'<span class="c-go">Ausgabe ansehen →</span></span></a>')

def decision_card(d):
    q,prob,cat,href=d
    return (f'<a class="c-dec" href="{href}"><span class="c-dec-cat">{esc(cat)}</span>'
            f'<span class="c-dec-q">{esc(q)}</span><span class="c-dec-p">{esc(prob)}</span>'
            f'<span class="c-go">Einstieg finden →</span></a>')

def sec_head(title, sub='', more='', kicker=''):
    k=f'<span class="c-ey">{esc(kicker)}</span>' if kicker else ''
    s=f'<p class="c-sub">{esc(sub)}</p>' if sub else ''
    m=f'<a class="c-more" href="#">{esc(more)}</a>' if more else ''
    return f'<div class="c-head">{k}<div class="c-head-row"><h2 class="c-h2">{esc(title)}</h2>{m}</div>{s}</div>'

# SS2 Topic-Sektion: grosser Lead links + kleine Items rechts (Artikel/Guides/Flagship)
def topic_section(title, rk, question, flags, cta, navy=False):
    ld=leads(rk)
    if not ld: return ''
    lead=ld[0]; side=ld[1:4]
    sideitems=''.join(list_row(r) for r in side)
    flagrefs=''.join(f'<a class="c-ref" href="{alink(series(s)[0])}"><span class="c-ref-k">Flagship · {esc(SER[s][1])}</span><span class="c-ref-n">{esc(SER[s][0])} →</span></a>' for s in flags if series(s))
    cl,ch=cta
    cls='c-topic'+(' c-topic-navy' if navy else '')
    return (f'<section class="{cls}">'
            f'<div class="c-topic-head"><div><span class="c-ey">{esc(title)}</span>'
            f'<h2 class="c-h2">{esc(question)}</h2></div><a class="c-btn" href="{ch}">{esc(cl)} →</a></div>'
            f'<div class="c-topic-grid"><div class="c-topic-main">{lead_big(lead, kicker=esc(title))}</div>'
            f'<aside class="c-topic-side"><span class="c-side-k">Aktuell &amp; passend</span>{sideitems}{flagrefs}</aside></div></section>')

# SS3 Navy-Break: dunkler Signal/Research-Block (grosser Lead + Items rechts)
def navy_signals(title, kicker, lead, items, more=('Alle Einschätzungen','smzh.ch/de/smzhub-archiv/index.html')):
    si=''.join(f'<a class="c-nrow" href="{alink(r)}"><span class="c-nrow-h">{esc(r["title"])}</span>'
               f'<span class="c-nrow-m">{esc(CAT.get(r.get("rubric"),"smzh"))} · {fdate(r.get("date"))}</span></a>' for r in items)
    cl,ch=more
    return (f'<section class="c-navy"><div class="c-navy-head"><div><span class="c-ey c-ey-l">{esc(kicker)}</span>'
            f'<h2 class="c-h2 c-h2-l">{esc(title)}</h2></div><a class="c-btn c-btn-ghost" href="{ch}">{esc(cl)} →</a></div>'
            f'<div class="c-navy-grid"><a class="c-nlead" href="{alink(lead)}"><span class="c-nlead-img">{imgt(lead,"c-img")}</span>'
            f'<span class="c-nlead-b"><span class="c-ey c-ey-l">{esc(CAT.get(lead.get("rubric"),"smzh"))} · {fdate(lead.get("date"))}</span>'
            f'<span class="c-nlead-h">{esc(lead["title"])}</span><span class="c-nlead-p">{esc(teaser(lead,150))}</span>'
            f'<span class="c-go c-go-l">Beitrag lesen →</span></span></a><div class="c-nlist">{si}</div></div></section>')

# SS1 Flagship-Hero: Titel links + Spotlight rechts
def flagship_hero(spotlight_series):
    name,cad,desc=SER[spotlight_series]; cur=series(spotlight_series)[0]
    return (f'<section class="c-fhero"><div class="c-fhero-l"><span class="c-ey">smzhHub · Research &amp; Advisory</span>'
            f'<h1 class="c-h1">Klarheit für Ihre nächste Finanzentscheidung.</h1>'
            f'<p class="c-hero-sub">Einschätzungen, Ratgeber und wiederkehrendes Research zu Eigenheim, Vermögen, '
            f'Vorsorge und Steuern – strukturiert nach Ihren Fragen.</p>'
            f'<div class="c-hero-cta"><a class="c-btn" href="#decide">Entscheidung finden</a>'
            f'<a class="c-btn-2" href="#topics">Themen ansehen</a></div></div>'
            f'<aside class="c-spot"><span class="c-spot-k">Flagship-Spotlight · {esc(cad)}</span>'
            f'<span class="c-spot-cov">{imgt(cur,"c-img")}</span>'
            f'<span class="c-spot-n">{esc(name)}</span><span class="c-spot-d">{esc(desc)}</span>'
            f'<a class="c-spot-go" href="{alink(cur)}">Aktuelle Ausgabe ansehen →</a></aside></section>')

def decision_strip(big=False):
    cards=''.join(decision_card(d) for d in DECISIONS)
    return (f'<section class="c-decsec{" c-decsec-big" if big else ""}" id="decide">'
            f'{sec_head("Entscheiden statt nur informieren","Die wichtigsten Finanzfragen sind Entscheidungen unter Unsicherheit. Wählen Sie Ihre Frage.","","Decision Layer")}'
            f'<div class="c-dec-grid">{cards}</div></section>')

def research_band(big=False):
    cards=''.join(flag_card(s,big=big) for s in ['hypothekenradar','investment-guide','immobilien-outlook'])
    return (f'<section class="c-research">{sec_head("Wiederkehrende Einschätzungen von smzh","Drei institutionelle Flagship-Formate – regelmässig, fundiert, mit eigener Serienidentität.","Alle Publikationen →","Research Signals")}'
            f'<div class="c-flag-grid{" c-flag-grid-big" if big else ""}">{cards}</div></section>')

def cta_panel():
    return ('<section class="c-cta"><div><h2 class="c-cta-h">Ihre Situation verdient mehr als einen Standardrat.</h2>'
            '<p>Wir begleiten Sie persönlich – unabhängig, diskret und auf Ihre Situation zugeschnitten.</p></div>'
            '<a class="c-btn c-btn-light" href="smzh.ch/de/terminvereinbaren/index.html">Persönliche Beratung →</a></section>')

# ---------- CSS (gemeinsame Basis, smzh navy/weiss/blau, Sans) ----------
BASE_CSS='''
*{box-sizing:border-box}
:root{--brand:#07314C;--ink:#0f2231;--blue:#0050ff;--muted:#5b6b7a;--faint:#8b9aa8;--line:#e4e9ee;--surf:#f5f8fb;--surf2:#eef3f8;--ok:#1f9d7a}
html,body{margin:0;background:#fff;color:var(--ink);font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
a{color:inherit}
.c-wrap{max-width:1180px;margin:0 auto;padding:0 1.5rem}
.c-ey{display:inline-block;font-size:.7rem;letter-spacing:.12em;text-transform:uppercase;font-weight:800;color:var(--blue)}
.c-ey-l{color:#7fb0d6}
.c-h1{font-size:clamp(2rem,4vw,3rem);font-weight:800;line-height:1.06;letter-spacing:-.02em;color:var(--brand);margin:.8rem 0 1rem}
.c-h2{font-size:clamp(1.35rem,2.4vw,1.85rem);font-weight:800;color:var(--brand);margin:.3rem 0;letter-spacing:-.01em}
.c-h2-l{color:#fff}
.c-sub{color:var(--muted);margin:.5rem 0 0;max-width:64ch;line-height:1.5}
.c-go{color:var(--blue);font-weight:700;font-size:.88rem}
.c-go-l{color:#7fb0d6}
.c-chip{display:inline-block;font-size:.62rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:.2rem .5rem;border-radius:5px;background:var(--surf2);color:var(--brand)}
.c-chip-immobilien{background:#e6eef4;color:#07314C}.c-chip-kapitalmaerkte{background:#e7ecff;color:#1c3bd6}
.c-chip-vorsorge{background:#e2f2ee;color:#15705f}.c-chip-steuern{background:#f4ecd9;color:#8a5e12}
.c-img{width:100%;height:100%;object-fit:cover;display:block}
.c-img-ph{background:repeating-linear-gradient(135deg,#eef3f8,#eef3f8 10px,#e6edf4 10px,#e6edf4 20px)}
.c-btn{display:inline-block;background:var(--brand);color:#fff;font-weight:600;text-decoration:none;padding:.8rem 1.4rem;border-radius:8px;font-size:.95rem}
.c-btn:hover{background:#0b4569}
.c-btn-2{display:inline-block;color:var(--brand);font-weight:600;text-decoration:none;padding:.8rem 1.1rem;border:1px solid var(--line);border-radius:8px}
.c-btn-ghost{background:transparent;border:1px solid rgba(255,255,255,.4);color:#fff}
.c-btn-light{background:#fff;color:var(--brand)}
.c-more{color:var(--blue);font-weight:700;text-decoration:none;font-size:.9rem;white-space:nowrap}
/* topbar */
.c-top{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.97);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.c-top-in{max-width:1180px;margin:0 auto;padding:.7rem 1.5rem;display:flex;align-items:center;gap:1.4rem}
.c-logo{font-weight:800;font-size:1.15rem;color:var(--brand);text-decoration:none;letter-spacing:-.02em}.c-logo b{color:var(--blue);font-weight:800}
.c-tabs{display:flex;gap:.2rem;overflow-x:auto}
.c-tab{padding:.5rem .8rem;color:var(--muted);text-decoration:none;font-weight:600;font-size:.92rem;white-space:nowrap;border-radius:6px}
.c-tab:hover{background:var(--surf);color:var(--brand)}.c-tab.is-on{color:var(--brand);background:var(--surf2)}
.c-top-cta{margin-left:auto;background:var(--brand);color:#fff;text-decoration:none;font-weight:600;font-size:.86rem;padding:.55rem 1rem;border-radius:7px;white-space:nowrap}
section{margin:0 0 3.4rem}
.c-head{margin-bottom:1.4rem;padding-bottom:1rem;border-bottom:1px solid var(--line)}
.c-head-row{display:flex;align-items:baseline;justify-content:space-between;gap:1rem}
/* flagship hero (SS1) */
.c-fhero{display:grid;grid-template-columns:1fr;gap:2rem;padding:2.4rem 0 2.6rem;border-bottom:1px solid var(--line);margin-bottom:3rem}
@media(min-width:900px){.c-fhero{grid-template-columns:1.1fr .9fr;gap:3.2rem;align-items:center}}
.c-hero-sub{color:var(--muted);font-size:1.1rem;line-height:1.55;max-width:48ch;margin:0 0 1.5rem}
.c-hero-cta{display:flex;gap:.7rem;flex-wrap:wrap}
.c-spot{display:flex;flex-direction:column;gap:.4rem;border:1px solid var(--line);border-radius:14px;padding:1.2rem;background:var(--surf);box-shadow:0 20px 50px -30px rgba(7,49,76,.5)}
.c-spot-k{font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;color:var(--ok)}
.c-spot-cov{display:block;aspect-ratio:16/10;border-radius:9px;overflow:hidden;background:var(--surf2);margin:.3rem 0 .5rem}
.c-spot-n{font-size:1.4rem;font-weight:800;color:var(--brand)}
.c-spot-d{color:var(--muted);font-size:.9rem;line-height:1.4}
.c-spot-go{margin-top:.6rem;color:var(--blue);font-weight:700;text-decoration:none;font-size:.92rem}
/* decision */
.c-dec-grid{display:grid;grid-template-columns:1fr;gap:1rem}
@media(min-width:620px){.c-dec-grid{grid-template-columns:1fr 1fr}}
.c-decsec-big .c-dec-grid{gap:1.2rem}
@media(min-width:980px){.c-decsec-big .c-dec-grid{grid-template-columns:1fr 1fr}}
.c-dec{display:flex;flex-direction:column;gap:.4rem;border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:10px;padding:1.3rem 1.4rem;text-decoration:none;background:#fff;transition:.15s}
.c-dec:hover{box-shadow:0 16px 36px -22px rgba(7,49,76,.55);transform:translateY(-2px)}
.c-dec-cat{font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;color:var(--faint)}
.c-dec-q{font-size:1.3rem;font-weight:800;color:var(--brand);line-height:1.15}
.c-decsec-big .c-dec-q{font-size:1.55rem}
.c-dec-p{color:var(--muted);font-size:.92rem;line-height:1.45;flex:1}
/* topic (SS2) */
.c-topic-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;border-bottom:2px solid var(--brand);padding-bottom:1rem;margin-bottom:1.6rem}
.c-topic-grid{display:grid;grid-template-columns:1fr;gap:2rem}
@media(min-width:880px){.c-topic-grid{grid-template-columns:1.45fr 1fr;gap:2.6rem}}
.c-lead{display:block;text-decoration:none}
.c-lead-img{display:block;aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:var(--surf2);margin-bottom:1rem}
.c-lead-h{display:block;font-size:clamp(1.3rem,2.2vw,1.7rem);font-weight:800;color:var(--brand);line-height:1.18;margin:.4rem 0 .5rem}
.c-lead:hover .c-lead-h{color:var(--blue)}
.c-lead-p{display:block;color:var(--muted);line-height:1.5;margin-bottom:.6rem}
.c-lead-m{display:flex;align-items:center;gap:.7rem}.c-date{color:var(--faint);font-size:.82rem}
.c-topic-side{display:flex;flex-direction:column;gap:.2rem}
.c-side-k{font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.08em;color:var(--faint);margin-bottom:.6rem}
.c-row{display:flex;gap:.9rem;align-items:center;padding:.85rem 0;border-bottom:1px solid var(--line);text-decoration:none}
.c-row-th{flex:0 0 76px;width:76px;height:54px;border-radius:7px;overflow:hidden;background:var(--surf2)}
.c-row-h{display:block;font-weight:700;color:var(--brand);line-height:1.3;font-size:.96rem}
.c-row:hover .c-row-h{color:var(--blue)}
.c-row-m{display:block;font-size:.74rem;color:var(--faint);text-transform:uppercase;letter-spacing:.04em;margin-top:.2rem}
.c-ref{display:flex;flex-direction:column;gap:.1rem;margin-top:.8rem;padding:.8rem .95rem;border:1px solid var(--line);border-radius:9px;text-decoration:none;background:var(--surf)}
.c-ref-k{font-size:.6rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--ok)}
.c-ref-n{font-weight:700;color:var(--brand);font-size:.95rem}
/* navy (SS3) */
.c-navy{background:var(--brand);border-radius:16px;padding:2.4rem;color:#fff}
@media(min-width:900px){.c-navy{padding:3rem}}
.c-navy-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;margin-bottom:1.8rem;padding-bottom:1.2rem;border-bottom:1px solid rgba(255,255,255,.16)}
.c-navy-grid{display:grid;grid-template-columns:1fr;gap:2rem}
@media(min-width:880px){.c-navy-grid{grid-template-columns:1.3fr 1fr;gap:2.8rem}}
.c-nlead{text-decoration:none;color:#fff}
.c-nlead-img{display:block;aspect-ratio:16/9;border-radius:12px;overflow:hidden;background:#0a1a2a;margin-bottom:1rem}
.c-nlead-h{display:block;font-size:clamp(1.4rem,2.4vw,1.9rem);font-weight:800;line-height:1.16;margin:.4rem 0 .5rem}
.c-nlead-p{display:block;color:#aebccb;line-height:1.5;margin-bottom:.6rem}
.c-nlist{display:flex;flex-direction:column}
.c-nrow{padding:1rem 0;border-top:1px solid rgba(255,255,255,.14);text-decoration:none;color:#fff;display:block}
.c-nrow:first-child{border-top:none}
.c-nrow-h{display:block;font-weight:700;line-height:1.3}
.c-nrow:hover .c-nrow-h{color:#9fd0ee}
.c-nrow-m{display:block;font-size:.74rem;color:#7e96aa;text-transform:uppercase;letter-spacing:.04em;margin-top:.25rem}
/* research / flagship cards */
.c-flag-grid{display:grid;grid-template-columns:1fr;gap:1.2rem}
@media(min-width:760px){.c-flag-grid{grid-template-columns:1fr 1fr 1fr}}
.c-flag{display:flex;flex-direction:column;border:1px solid var(--line);border-radius:12px;overflow:hidden;text-decoration:none;background:#fff;transition:.15s}
.c-flag:hover{border-color:var(--blue);box-shadow:0 18px 40px -24px rgba(7,49,76,.55);transform:translateY(-2px)}
.c-flag-cov{position:relative;aspect-ratio:16/10;overflow:hidden;background:var(--surf2)}
.c-flag-badge{position:absolute;top:10px;left:10px;background:var(--ok);color:#fff;font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;padding:.2rem .55rem;border-radius:5px}
.c-flag-b{padding:1.1rem 1.2rem;display:flex;flex-direction:column;gap:.35rem}
.c-flag-k{font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:var(--faint)}
.c-flag-n{font-size:1.25rem;font-weight:800;color:var(--brand)}
.c-flag-d{color:var(--muted);font-size:.86rem;line-height:1.4}
.c-flag-cur{font-size:.82rem;color:var(--ink);border-top:1px solid var(--line);padding-top:.6rem;margin-top:.2rem;font-weight:600}
.c-flag-grid-big .c-flag-cov{aspect-ratio:16/9}
/* cta */
.c-cta{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1.4rem;background:var(--surf);border:1px solid var(--line);border-radius:14px;padding:2rem 2.2rem}
.c-cta-h{font-size:clamp(1.3rem,2.2vw,1.6rem);font-weight:800;color:var(--brand);margin:0 0 .4rem;max-width:26ch}
.c-cta p{color:var(--muted);margin:0;max-width:46ch;line-height:1.5}
.c-foot{border-top:1px solid var(--line);padding:1.6rem 0 3rem;color:var(--faint);font-size:.82rem}
'''

def page(concept_label, title, body, extra_css=''):
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{esc(title)}</title><style>{BASE_CSS}{extra_css}</style></head>'
            f'<body><div class="c-concept-flag">{esc(concept_label)}</div>{body}'
            f'<div class="c-wrap"><div class="c-foot">smzhHub – statisches Konzept · echte Inhalte, reale Bilder · {esc(latest_month())}</div></div>'
            f'</body></html>')

FLAGBAR='.c-concept-flag{background:#07314C;color:#fff;text-align:center;font-size:.74rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;padding:.4rem}'

# ---------- Concept A: Advisory Interface ----------
def concept_a():
    css=FLAGBAR+'.c-fhero{padding-top:2rem}'
    topics=''.join(topic_section(t,rk,q,fl,cta) for t,rk,q,fl,cta in TOPIC)
    body=(topbar('Alle')+'<div class="c-wrap">'+flagship_hero('investment-guide')
          +decision_strip()
          +'<div id="topics"></div>'+topics
          +research_band()+cta_panel()+'</div>')
    return page('Concept A · Advisory Interface','smzhHub – Concept A',body,css)

# ---------- Concept B: Research Signal Hub ----------
def concept_b():
    css=(FLAGBAR
         +'.c-bhero{display:grid;grid-template-columns:1fr;gap:1.4rem;padding:2.2rem 0 2rem}'
         +'@media(min-width:900px){.c-bhero{grid-template-columns:1.3fr .7fr;align-items:end}}'
         +'.c-bhero .c-hero-sub{margin-bottom:0}')
    # Hero (kompakt) – Authority
    hero=(f'<section class="c-bhero"><div><span class="c-ey">smzhHub · Research &amp; Advisory</span>'
          f'<h1 class="c-h1">Das Research, das Schweizer Finanzentscheidungen einordnet.</h1>'
          f'<p class="c-hero-sub">Wiederkehrende Einschätzungen zu Hypotheken, Märkten und dem Immobilienmarkt – '
          f'plus Orientierung zu Eigenheim, Vermögen und Vorsorge.</p></div>'
          f'<div><a class="c-btn" href="#research">Research ansehen</a></div></section>')
    # Navy signal centerpiece: aktuelle Marktsignale (Fed/SNB/Vermögen)
    lead=find('neue Ära an der Fed') or leads('kapitalmaerkte')[0]
    items=[r for r in (find('SNB hält am Nullzins fest'),find('Iran'),find('Sell in May'),find('SpaceX')) if r][:4]
    if len(items)<4: items=(items+leads('kapitalmaerkte'))[:4]
    navy=navy_signals('Marktsignale & Zinsumfeld','Aktuell · Märkte', lead, items)
    research=research_band(big=True)
    topics=''.join(topic_section(t,rk,q,fl,cta) for t,rk,q,fl,cta in TOPIC[:2])
    body=(topbar('Research')+'<div class="c-wrap">'+hero
          +'<div id="research"></div>'+research
          +navy
          +decision_strip()
          +topics+cta_panel()+'</div>')
    return page('Concept B · Research Signal Hub','smzhHub – Concept B',body,css)

# ---------- Concept C: Decision Journey Hub ----------
def concept_c():
    css=(FLAGBAR
         +'.c-chero{padding:2.4rem 0 1.4rem;max-width:30ch}'
         +'.c-chero .c-h1{margin-top:.6rem}'
         +'.c-decsec-big .c-dec{border-left-width:4px}')
    hero=(f'<section class="c-chero"><span class="c-ey">smzhHub · Entscheiden</span>'
          f'<h1 class="c-h1">Welche Finanzentscheidung steht bei Ihnen an?</h1></section>')
    dec=decision_strip(big=True)
    # follow-up topics (SS2) for the decision themes
    topics=''.join(topic_section(t,rk,q,fl,cta) for t,rk,q,fl,cta in TOPIC)
    research=research_band()
    body=(topbar('Entscheiden')+'<div class="c-wrap">'+hero+dec
          +'<div id="topics"></div>'+topics+research+cta_panel()+'</div>')
    return page('Concept C · Decision Journey Hub','smzhHub – Concept C',body,css)

def main():
    open(os.path.join(SITE,'concept-a.html'),'w',encoding='utf-8').write(concept_a())
    open(os.path.join(SITE,'concept-b.html'),'w',encoding='utf-8').write(concept_b())
    open(os.path.join(SITE,'concept-c.html'),'w',encoding='utf-8').write(concept_c())
    n=len([f for f in os.listdir(ASSETS) if not f.startswith('.')])
    print(f'OK: concept-a/b/c.html geschrieben · {n} Bilder in site/concept-assets/')

if __name__=='__main__':
    main()
