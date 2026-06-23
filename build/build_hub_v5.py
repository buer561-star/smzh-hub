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
DECISIONS=[('Hypothek','SARON oder Festhypothek?','Welche Laufzeit passt, wenn Zinsen tief bleiben, aber Planungssicherheit zählt?','/de/hypothekenarten-im-vergleich/'),
 ('Eigenheim','Kaufen oder warten?','Wie Preisentwicklung, Eigenkapital und Lebensplanung zusammenhängen.','/de/wie-kaufe-ich-eine-immobilie/'),
 ('Vorsorge','Rente oder Kapital?','Die Pensionierungsentscheidung, die selten sauber vorbereitet wird.','/de/leistungen-im-alter/'),
 ('Anlegen','3a Konto oder Wertschriften?','Warum Sparen allein über lange Zeiträume oft nicht genügt.','/de/altersvorsorge-optimierung-saeule-3a/'),
 ('Eigenheim','Reicht mein Einkommen für die Bank?','Wie Banken die Tragbarkeit rechnen – und was Sie daran beeinflussen können.','/de/optimierung-der-tragbarkeit/'),
 ('Vermögen','Amortisieren oder investieren?','Hypothek tilgen oder das Geld anlegen – was sich für Sie langfristig mehr lohnt.','/de/finanzplan-erstellen/'),
 ('Vorsorge','Früher pensionieren oder weiterarbeiten?','Was ein früherer Ausstieg kostet – und wie er finanzierbar bleibt.','/de/pensionsplanung/'),
 ('Steuern','Wo verschenke ich jedes Jahr Steuern?','Welche Abzüge und Vorsorgebezüge wirklich einen Unterschied machen.','/de/steuerabzuege-optimal-nutzen/'),
 ('Eigenheim','Wie viel Eigenkapital brauche ich wirklich?','20 Prozent sind nur die halbe Wahrheit – worauf es zusätzlich ankommt.','/de/wohneigentumsfoerderung/'),
 ('Vorsorge','Lohnt sich die Säule 3a für mich?','Wann 3a wirklich zählt – und wann Ihr Geld anderswo besser aufgehoben ist.','/de/das-3-saeulensystem-der-schweiz/')]
RUBRICS=[
 {'intro':'Kann ich mir mein Eigenheim leisten – und zu welchen Konditionen?','more':'/de/smzhub-eigenheim/',
  'arts':['/de/artikel/snb-zinsentscheid-juni/','/de/artikel/zuercher-wohnungsinitiativen/','/de/artikel/abstimmung-keine-10-millionen-schweiz/','/de/artikel/eigenmietwert-sanierung-bundesrat-2029/'],
  'flags':[('hypothekenradar','/de/smzhub-serie-hypotheken-radar/'),('immobilien-outlook','/de/smzhub-serie-immobilien-outlook/')],
  'cta':('Hypothek prüfen lassen','/de/immobilienbewertung/')},
 {'intro':'Wie lege ich mein Vermögen sinnvoll und ruhig an?','more':'/de/smzhub-vermoegen/',
  'arts':['/de/artikel/neue-aera-fed/','/de/artikel/usa-iran-deal/','/de/artikel/boersengang-spacex/','/de/artikel/sell-in-may/'],
  'flags':[('investment-guide','/de/smzhub-serie-investment-guide/')],
  'cta':('Anlagestrategie besprechen','/de/terminvereinbaren/')},
 {'intro':'Reicht mein Geld bis zur – und in der – Pensionierung?','more':'/de/smzhub-zukunft/',
  'arts':['/de/artikel/ahv-2030-pensionierung-planungsfrage/','/de/artikel/kapitalbezug-steuerentscheid/','/de/artikel/fruehpensionierung-unter-druck/','/de/artikel/gender-pension-gap/'],
  'flags':[('dossier','/de/smzhub-dossier-pensionierung/')],
  'cta':('Vorsorge analysieren','/de/vorsorgeanalyse/')}]
FLAGMETA={'hypothekenradar':('Hypotheken-Radar','monatlich'),'investment-guide':('Investment Guide','monatlich'),
 'immobilien-outlook':('Immobilien-Outlook','quartalsweise'),'dossier':('Pensionierung planen','Dossier · Storyline')}
RESEARCH=[('Hypotheken-Radar','monatlich · 9 Ausgaben','/de/smzhub-serie-hypotheken-radar/','hypothekenradar'),
 ('Investment Guide','monatlich · 16 Ausgaben','/de/smzhub-serie-investment-guide/','investment-guide'),
 ('Immobilien-Outlook','quartalsweise · 7 Ausgaben','/de/smzhub-serie-immobilien-outlook/','immobilien-outlook')]
# Saison (Krankenkasse) – kuratiertes Saisonthema, Links auf reale Seiten
SEASON_HERO=('Krankenkasse 2027: jetzt vergleichen statt automatisch zahlen','Prämien steigen erneut – wer Grundversicherung, Franchise und Modell prüft, spart oft mehrere Hundert Franken pro Jahr.','Prämien vergleichen','/de/krankenkasse-vergleichen/')
SEASON_SUBS=[('Prämien optimieren ohne Leistungsverlust','/de/krankenkassen-praemienoptimierung/'),
 ('Welche Franchise passt zu Ihrem Profil?','/de/krankenkasse-vergleichen/'),
 ('Budgetrechner nutzen','/de/budgetrechner/')]

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
    return (f'<section class="v5-hero"><div class="v5-hero-l"><h1>Klarheit für Ihre nächste Finanzentscheidung.</h1>'
            f'<p>Einordnungen, Research und Ratgeber zu Eigenheim, Vermögen, Vorsorge und Steuern – kuratiert nach Ihren Fragen.</p></div>'
            f'<div class="v5-hero-r v5-car"><div class="h-slides">{slides}</div><div class="h-dots">{dots}</div></div></section>')

def decisions():
    cards=''
    shapes=['#185E7F','#03314B','#185E7F','#03314B']
    for i,(cat,q,desc,p) in enumerate(DECISIONS):
        cards+=(f'<a class="v5-dec" href="{link(p)}"><span class="v5-dec-cat">{esc(cat)}</span>'
                f'<span class="v5-dec-q">{esc(q)}</span><span class="v5-dec-d">{esc(desc)}</span>'
                f'<span class="v5-dec-shape" style="background:{shapes[i%4]}"></span></a>')
    nav=('<div class="v5-dec-nav"><span class="v5-dec-arrow v5-dec-prev" role="button" tabindex="0" aria-label="Zurück">‹</span>'
         '<span class="v5-dec-arrow v5-dec-next" role="button" tabindex="0" aria-label="Weiter">›</span></div>')
    return (f'<section class="v5-sec v5-dec-sec"><div class="v5-head"><div><h2>Entscheiden statt nur informieren</h2>'
            f'<p class="v5-sub">Wichtige Finanzfragen sollten nicht unter Unsicherheit entschieden werden.</p></div>'
            f'{nav}</div>'
            f'<div class="v5-dec-vp"><div class="v5-dec-track">{cards}</div></div></section>')

def season():
    t,teaser,cl,cp=SEASON_HERO
    subs=''
    for st,sp in SEASON_SUBS:
        subs+=f'<a class="v5-se-sub" href="{link(sp)}"><span class="v5-se-sub-t">{esc(st)}</span><span class="v5-se-sub-go">→</span></a>'
    hero=(f'<a class="v5-se-hero" href="{link(cp)}"><span class="v5-se-tag">Saisonthema</span>'
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

def rubric(rb):
    arts=''
    for p in rb['arts']:
        r=item(p)
        if not r: continue
        arts+=f'<a class="v5-al" href="{link(p)}"><span class="v5-al-t">{esc(r["title"])}</span><span class="v5-al-m">{esc(meta_of(p))}</span></a>'
    flags=''.join(flag_card(k,pp) for k,pp in rb['flags'])
    cl,cp=rb['cta']
    return (f'<section class="v5-sec"><div class="v5-head v5-head-sm"><h3 class="v5-rub-intro">{esc(rb["intro"])}</h3>'
            f'<a class="v5-more" href="{link(rb["more"])}">Ganze Rubrik →</a></div>'
            f'<div class="v5-rub-grid"><div class="v5-al-list">{arts}</div>'
            f'<div class="v5-rub-side">{flags}<a class="v5-cta" href="{link(cp)}">{esc(cl)} →</a></div></div></section>')

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

def home_inner():
    return '<div class="v5">'+hero()+'<div class="v5-wrap">'+decisions()+season()+''.join(rubric(r) for r in RUBRICS)+'</div>'+research()+'</div>'

FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">')
CSS='''<style id="smzh-v5-css">
#ed-root{--navy:#03314B;--teal:#185E7F;--lblue:#E9F4FC;--ink:#1c2b36;--muted:#5b6b7a;--faint:#8b9aa8;--line:#e5e7eb;max-width:none;padding:0 !important;gap:0 !important}
#ed-root,.v5,.v5 *{font-family:'Plus Jakarta Sans',-apple-system,'Segoe UI',Roboto,sans-serif;box-sizing:border-box}
.v5{color:var(--ink)}
.v5-wrap{max-width:1180px;margin:0 auto;padding:0 1.5rem}
.v5 h1,.v5 h2,.v5 h3{letter-spacing:-.02em;color:var(--navy);margin:0}
.v5 a{text-decoration:none;color:inherit}
.v5-sec{margin:3.4rem 0}
.v5-head{display:flex;align-items:flex-end;justify-content:space-between;gap:1rem;margin-bottom:1.4rem}
.v5-head h2{font-size:clamp(1.4rem,2.4vw,1.85rem);font-weight:800}
.v5-sub{color:var(--muted);font-size:.92rem;margin:.35rem 0 0}
.v5-more{color:var(--teal);font-weight:700;font-size:.9rem;white-space:nowrap}
.v5-more:hover{color:var(--navy)}
/* Hero */
.v5-hero{display:grid;grid-template-columns:1fr;gap:2rem;background:var(--navy);color:#fff;border-radius:0 0 22px 22px;padding:3rem 1.5rem 3.4rem}
@media(min-width:960px){.v5-hero{grid-template-columns:1fr minmax(300px,400px);gap:4.5rem;padding:5rem 5rem 5.4rem;align-items:center}}
.v5-hero-l{max-width:46ch}
.v5-hero-l h1{color:#fff;font-size:clamp(2rem,3.6vw,3rem);font-weight:800;line-height:1.08}
.v5-hero-l p{color:#bcd3e2;font-size:1.1rem;line-height:1.6;margin:1.2rem 0 0;max-width:44ch}
.v5-hero-r{position:relative}
.h-slides{position:relative;border-radius:16px;overflow:hidden;aspect-ratio:4/5;background:#fff;box-shadow:0 34px 64px -30px rgba(0,0,0,.55)}
.h-slide{position:absolute;inset:0;display:flex;flex-direction:column;opacity:0;transition:opacity .6s ease;pointer-events:none}
.h-slide.on{opacity:1;pointer-events:auto}
.h-slide-img{flex:0 0 47%;overflow:hidden;background:#06283b}
.h-slide-img img{width:100%;height:100%;object-fit:cover}
.h-slide-c{flex:1;display:flex;flex-direction:column;gap:.5rem;padding:1.3rem 1.4rem;background:#fff}
.h-slide-cat{font-size:.82rem;font-weight:600;color:var(--teal)}
.h-slide-t{font-size:1.2rem;font-weight:700;color:var(--navy);line-height:1.24;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.h-slide-p{font-size:.9rem;color:var(--muted);line-height:1.45;flex:1;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.h-slide-go{font-size:.86rem;font-weight:700;color:var(--teal);margin-top:.2rem}
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
.v5-head-sm{border-top:1px solid var(--line);padding-top:1.5rem}
.v5-rub-intro{font-size:clamp(1.15rem,1.9vw,1.5rem);font-weight:700;color:var(--navy);max-width:30ch}
.v5-rub-grid{display:grid;grid-template-columns:1fr;gap:1.6rem}
@media(min-width:880px){.v5-rub-grid{grid-template-columns:1.6fr 1fr;gap:2.4rem}}
.v5-al-list{display:flex;flex-direction:column}
.v5-al{display:flex;align-items:baseline;justify-content:space-between;gap:1.2rem;padding:1.05rem 0;border-bottom:1px solid var(--line)}
.v5-al:first-child{padding-top:0}
.v5-al-t{font-size:1.08rem;font-weight:700;color:var(--navy);line-height:1.3}
.v5-al:hover .v5-al-t{color:var(--teal)}
.v5-al-m{font-size:.8rem;color:var(--faint);white-space:nowrap}
.v5-rub-side{display:flex;flex-direction:column;gap:.9rem}
.v5-flag{display:flex;gap:.9rem;align-items:stretch;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#fff;transition:.15s}
.v5-flag:hover{border-color:var(--teal);box-shadow:0 14px 30px -22px rgba(3,49,75,.55)}
.v5-flag-cov{flex:0 0 84px;background:var(--lblue);overflow:hidden}
.v5-flag-cov img{width:100%;height:100%;object-fit:cover}
.v5-flag-cov-dos{display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,var(--navy),var(--teal))}
.v5-flag-dos-i{color:#fff;font-size:1.5rem;opacity:.85}
.v5-flag-b{display:flex;flex-direction:column;gap:.15rem;padding:.85rem .95rem}
.v5-flag-cad{font-size:.76rem;color:var(--muted)}
.v5-flag-n{font-size:1.05rem;font-weight:800;color:var(--navy)}
.v5-flag-go{font-size:.8rem;font-weight:700;color:var(--teal);margin-top:.2rem}
.v5-cta{display:block;text-align:center;background:var(--navy);color:#fff;font-weight:700;padding:.85rem 1.2rem;border-radius:10px;margin-top:.3rem}
.v5-cta:hover{background:var(--teal)}
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
#ed-root .v5-more,#ed-root .v5-flag-go,#ed-root .v5-rs-go,#ed-root .v5-se-sub-go{color:#185E7F!important}
#ed-root .v5-dec-q,#ed-root .v5-al-t,#ed-root .v5-flag-n,#ed-root .v5-rs-n,#ed-root .v5-se-sub-t,#ed-root .v5-rub-intro,#ed-root .v5 h2{color:#03314B!important}
#ed-root .v5-dec-cat{color:#185E7F!important}
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
});});})();
</script>'''

def balanced_div_end(s,start):
    depth=0
    for m in re.finditer(r'<(/?)div\b[^>]*>',s[start:]):
        depth+=1 if m.group(1)=='' else -1
        if depth==0: return start+m.end()
    return -1

def main():
    html=open(CHROME_SRC,encoding='utf-8',errors='ignore').read()
    m=re.search(r'<div class="content-hub[^"]*"',html)
    o=html.index('>',m.start())+1; c=balanced_div_end(html,m.start())
    before=html[:o]; after=html[c-6:]
    if 'id="smzh-v5-css"' not in before: before=before.replace('</head>',FONTS+CSS+'</head>',1)
    before=re.sub(r'(<div class="content-hub[^"]*")',r'\1 id="ed-root"',before,count=1)
    if 'id="smzh-v5-js"' not in after: after=after.replace('</body>',JS+'</body>',1)
    full=before+home_inner()+after
    full=re.sub(r'<title>.*?</title>','<title>smzhHub – Klarheit für Ihre Finanzentscheidungen</title>',full,count=1,flags=re.S)
    d=os.path.join(SMZH,'de','smzhub'); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,'index.html'),'w',encoding='utf-8').write(full)
    print('OK V5: Landing Page geschrieben (Hero+Karussell · Entscheidungen · Saison · 3 Rubriken · Research).')

if __name__=='__main__':
    main()
