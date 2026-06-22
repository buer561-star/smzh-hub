#!/usr/bin/env python3
"""Iteration 2 – Research-/Publikationsreihen-Sektion in den echten Hub einbauen.
Datengetrieben aus build/smzhhub-content.json. Fuegt oben im .content-hub-Container
einen ruhigen, hochwertigen Block fuer die 3 Reihen ein (neueste Ausgabe + Archiv).
Idempotent. Kein Deploy/Push. Aendert nur die Hub-Datei.
"""
import json, os, re, html as H
from datetime import datetime

HUB='site/smzh.ch/de/smzhub/index.html'
P='../../'            # de/smzhub/ -> smzh.ch-root
CMS='../../../cms.smzh.ch/uploads/'   # de/smzhub/ -> site/ -> cms uploads
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))

SERIES=[
 ('hypothekenradar','Hypotheken-Radar','Monatliche Einschätzung zu Zinsen, Festhypotheken und Schweizer Hypothekarmarkt.','Monatlich','Hypothekenberatung','de/steuererklaerung/'),
 ('investment-guide','Investment Guide','Monatliche Anlageeinschätzung – Märkte, Strategie und Portfoliothemen.','Monatlich','Anlageberatung','de/vorsorgeanalyse/'),
 ('immobilien-outlook','Immobilien-Outlook','Quartalsweise Analyse des Schweizer Immobilienmarkts.','Quartalsweise','Immobilienberatung','de/immobilienbewertung/'),
]

def fmt_date(iso):
    if not iso: return ''
    try: return datetime.fromisoformat(iso.replace('Z','+00:00')).strftime('%b %Y').replace('Jan','Jan').replace('Mar','März').replace('Oct','Okt').replace('Dec','Dez')
    except Exception: return ''

def localimg(r):
    il=r.get('imageLocal')
    if not il: return None
    # imageLocal ist einfach-kodiert (Dateiname); fuer HTTP muss '%' verdoppelt
    # und '&' als &amp; ausgegeben werden (gleiches Schema wie die Hub-Karten).
    rel=il[len('smzh.ch/'):].replace('%','%25').replace('&','&amp;')
    return P+rel

def art_link(r):
    return P+r['path'].strip('/').split('/',0)[0] and P+'/'.join(r['path'].strip('/').split('/'))+'/index.html'

def link_for(r):
    segs=[s for s in r['path'].strip('/').split('/') if s]
    return P+'/'.join(segs)+'/index.html'

def card_html(s):
    key,name,desc,cadence,cta,ctapath=s
    items=sorted([r for r in rows if r.get('series')==key], key=lambda r:r.get('date') or '', reverse=True)
    if not items: return ''
    newest=items[0]; archive=items[1:]
    img=localimg(newest)
    cover=(f'<a class="rs-cover" href="{link_for(newest)}">'
           f'<img loading="lazy" src="{img}" alt="{H.escape(newest["title"])}"></a>') if img else ''
    pdf=''
    if newest.get('pdfs'):
        pdf=f'<a class="rs-pdf" href="{CMS}{newest["pdfs"][0]}" target="_blank" rel="noopener">PDF ansehen</a>'
    arch=''
    if archive:
        lis=''.join(f'<li><a href="{link_for(r)}"><span>{H.escape(r["title"])}</span><time>{fmt_date(r.get("date"))}</time></a></li>' for r in archive[:24])
        arch=(f'<details class="rs-archive"><summary>Frühere Ausgaben ({len(archive)})</summary>'
              f'<ul>{lis}</ul></details>')
    return (f'<article class="rs-card"><div class="rs-badge">{cadence}</div>'
            f'{cover}'
            f'<div class="rs-body"><h3 class="rs-name">{H.escape(name)}</h3>'
            f'<p class="rs-desc">{H.escape(desc)}</p>'
            f'<div class="rs-latest"><span class="rs-latest-label">Aktuelle Ausgabe</span>'
            f'<a class="rs-latest-link" href="{link_for(newest)}">{H.escape(newest["title"])}</a>'
            f'<time class="rs-date">{fmt_date(newest.get("date"))}</time></div>'
            f'<div class="rs-actions"><a class="rs-primary" href="{link_for(newest)}">Lesen</a>{pdf}</div>'
            f'{arch}</div></article>')

SECTION=('<section id="smzh-research" aria-label="Research und Publikationen"><div class="rs-head">'
         '<h2>Research &amp; Publikationen</h2>'
         '<p>Unsere wiederkehrenden Einschätzungen – fundiert, ruhig, auf den Punkt.</p></div>'
         '<div class="rs-grid">'+''.join(card_html(s) for s in SERIES)+'</div></section>')

STYLE='''<style id="smzh-research-css">
#smzh-research{margin-bottom:3.5rem}
#smzh-research .rs-head h2{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;color:#07314C;margin:0 0 .4rem}
#smzh-research .rs-head p{color:#5b6b7a;margin:0 0 1.6rem;font-size:1.05rem}
#smzh-research .rs-grid{display:grid;gap:1.25rem;grid-template-columns:1fr}
@media(min-width:768px){#smzh-research .rs-grid{grid-template-columns:repeat(3,1fr)}}
#smzh-research .rs-card{display:flex;flex-direction:column;border:1px solid #e7ebef;border-radius:14px;overflow:hidden;background:#fff;position:relative}
#smzh-research .rs-badge{position:absolute;top:12px;left:12px;z-index:2;background:#07314C;color:#fff;font-size:.7rem;font-weight:600;letter-spacing:.03em;text-transform:uppercase;padding:.3rem .6rem;border-radius:999px}
#smzh-research .rs-cover{display:block;aspect-ratio:16/10;overflow:hidden;background:#f2f5f8}
#smzh-research .rs-cover img{width:100%;height:100%;object-fit:cover}
#smzh-research .rs-body{display:flex;flex-direction:column;gap:.55rem;padding:1.1rem 1.2rem 1.3rem}
#smzh-research .rs-name{margin:0;font-size:1.25rem;font-weight:700;color:#07314C}
#smzh-research .rs-desc{margin:0;color:#5b6b7a;font-size:.93rem;line-height:1.45}
#smzh-research .rs-latest{display:flex;flex-direction:column;gap:.15rem;margin-top:.4rem;padding-top:.7rem;border-top:1px solid #eef1f4}
#smzh-research .rs-latest-label{font-size:.7rem;text-transform:uppercase;letter-spacing:.04em;color:#9aa7b2}
#smzh-research .rs-latest-link{color:#07314C;font-weight:600;text-decoration:none;line-height:1.3}
#smzh-research .rs-latest-link:hover{text-decoration:underline}
#smzh-research .rs-date{color:#9aa7b2;font-size:.8rem}
#smzh-research .rs-actions{display:flex;gap:.6rem;margin-top:.6rem}
#smzh-research .rs-primary{background:#07314C;color:#fff;text-decoration:none;font-weight:600;padding:.55rem 1.1rem;border-radius:8px;font-size:.9rem}
#smzh-research .rs-pdf{color:#0050ff;text-decoration:none;font-weight:600;padding:.55rem .4rem;font-size:.9rem}
#smzh-research .rs-archive{margin-top:.7rem;border-top:1px solid #eef1f4;padding-top:.5rem}
#smzh-research .rs-archive summary{cursor:pointer;color:#0050ff;font-weight:600;font-size:.88rem;list-style:none}
#smzh-research .rs-archive summary::-webkit-details-marker{display:none}
#smzh-research .rs-archive ul{list-style:none;margin:.5rem 0 0;padding:0;max-height:260px;overflow:auto}
#smzh-research .rs-archive li a{display:flex;justify-content:space-between;gap:1rem;padding:.45rem 0;border-bottom:1px solid #f1f4f7;color:#3a5a72;text-decoration:none;font-size:.88rem}
#smzh-research .rs-archive li a:hover{color:#07314C}
#smzh-research .rs-archive time{color:#9aa7b2;white-space:nowrap;font-size:.78rem}
</style>'''

def main():
    html=open(HUB,encoding='utf-8',errors='ignore').read()
    # alte Version entfernen (idempotent)
    html=re.sub(r'<section id="smzh-research".*?</section>','',html,flags=re.S)
    html=re.sub(r'<style id="smzh-research-css">.*?</style>','',html,flags=re.S)
    # Style in <head>
    if '</head>' in html: html=html.replace('</head>',STYLE+'</head>',1)
    # Section am Anfang des .content-hub-Containers einfuegen
    anchor=re.search(r'(<div class="content-hub[^"]*">)', html)
    if not anchor:
        raise SystemExit('content-hub Container nicht gefunden')
    pos=anchor.end()
    html=html[:pos]+SECTION+html[pos:]
    open(HUB,'w',encoding='utf-8').write(html)
    # kleine Bilanz
    for key,name,*_ in SERIES:
        n=len([r for r in rows if r.get('series')==key])
        print(f'  {name}: {n} Ausgaben')
    print('Research-Sektion eingefügt in', HUB)

if __name__=='__main__':
    main()
