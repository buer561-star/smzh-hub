#!/usr/bin/env python3
"""Phase 7 – Artikel-Detailseiten strukturell aufwerten (ohne Fliesstext-Eingriff).
Fügt je Artikelseite ein:
  - smzhHub-Rubrik-Chip + Lesedauer direkt nach der H1 (Einordnung + Navigation)
  - End-Block vor dem Footer: "Was bedeutet das für Sie?" (kontextbezogener
    Beratungs-CTA), Flagship-Verknüpfung, Related-Beiträge der gleichen Rubrik,
    Zurück-zum-Hub.
Verändert KEINEN Artikeltext. Nur Navigations-/Lead-Chrome wird ergänzt.
Idempotent: bestehende Injektionen werden vorher entfernt.
"""
import json, os, re, html as H
from datetime import datetime

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch')
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
BY_ID={r['id']:r for r in rows}
REL='../../../'   # von de/<seg>/<slug>/ zum smzh.ch-Root

MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def lk(path): return REL+'/'.join(s for s in path.strip('/').split('/') if s)+'/index.html'

# Rubrik -> (Label, Hub-Rubrikseite, Flagship-Serie, Beratungssatz)
RUBRIC_INFO={
 'immobilien':('Eigenheim','de/smzhub-eigenheim/','hypothekenradar',
   'Ob Kauf, Tragbarkeit oder Anschlussfinanzierung – wir ordnen Ihre Hypothekarsituation unabhängig ein.'),
 'kapitalmaerkte':('Vermögen','de/smzhub-vermoegen/','investment-guide',
   'Von der Anlagestrategie bis zur Portfolioüberprüfung – wir schauen mit Ihnen auf Ihre Situation.'),
 'vorsorge':('Zukunft','de/smzhub-zukunft/',None,
   'AHV, Pensionskasse und Säule 3a: Wir machen Ihre Pensionierung planbar.'),
 'steuern':('Steuern','de/smzhub-steuern/',None,
   'Steuern senken und Vermögen strukturieren – konkret auf Ihre Situation bezogen.'),
}
SERIES_NAME={'hypothekenradar':('Hypotheken-Radar','de/smzhub-serie-hypotheken-radar/','Monatliches Hypotheken-Research'),
 'investment-guide':('Investment Guide','de/smzhub-serie-investment-guide/','Monatliche Anlageeinschätzung'),
 'immobilien-outlook':('Immobilien-Outlook','de/smzhub-serie-immobilien-outlook/','Quartalsweiser Immobilienmarkt-Ausblick')}
LEAD_PATH={'Hypothekenberatung':'de/immobilienbewertung/','Vorsorgeanalyse':'de/vorsorgeanalyse/',
 'Anlageberatung':'de/terminvereinbaren/','Steuerberatung':'de/steuererklaerung/',
 'Immobilienberatung':'de/immobilienbewertung/','KMU-Beratung':'de/terminvereinbaren/',
 'Nachlassberatung':'de/terminvereinbaren/','Versicherungsberatung':'de/terminvereinbaren/',
 '360-Check-Up':'de/terminvereinbaren/'}

def related(item):
    rub=item.get('rubric')
    if rub:
        pool=[r for r in rows if r.get('rubric')==rub and r['id']!=item['id'] and r.get('hubEligible')]
    else:
        pool=[r for r in rows if r.get('hubEligible') and r['id']!=item['id']]
    pool.sort(key=lambda r:r.get('date') or '', reverse=True)
    return pool[:3]

CSS='''<style id="smzh-art-css">
.smzh-hubchip{display:inline-flex;align-items:center;gap:.5rem;margin:.2rem 0 .4rem;padding:.32rem .8rem;border:1px solid #e7ebef;border-radius:999px;background:#f4f7fa;color:#07314C;text-decoration:none;font-size:.78rem;font-weight:600}
.smzh-hubchip b{color:#0050ff;font-weight:800}
.smzh-hubchip:hover{border-color:#0050ff}
#smzh-art-enh{margin:3.5rem 0 0;border-top:1px solid #e7ebef;background:#fff}
#smzh-art-enh .sae-wrap{max-width:1120px;margin:0 auto;padding:2.6rem 1.5rem 1rem;display:flex;flex-direction:column;gap:2rem}
#smzh-art-enh .sae-cta{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1.2rem;background:#07314C;border-radius:16px;padding:1.8rem 2rem}
#smzh-art-enh .sae-k{display:block;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:#e6b15e;font-weight:800;margin-bottom:.4rem}
#smzh-art-enh .sae-cta p{color:#cfe;margin:0;color:#c7d6e2;max-width:60ch;line-height:1.5}
#smzh-art-enh .sae-cta h3{display:none}
#smzh-art-enh .sae-btn{background:#fff;color:#07314C;font-weight:700;text-decoration:none;padding:.85rem 1.6rem;border-radius:10px;white-space:nowrap}
#smzh-art-enh .sae-flag{display:flex;align-items:center;gap:1rem;border:1px solid #e7ebef;border-left:3px solid #b07d1e;border-radius:12px;padding:1rem 1.3rem;text-decoration:none;background:#fff}
#smzh-art-enh .sae-flag-tag{font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#b07d1e;background:#f6ead2;padding:.18rem .5rem;border-radius:4px;white-space:nowrap}
#smzh-art-enh .sae-flag-main{flex:1;display:flex;flex-direction:column;gap:.15rem}
#smzh-art-enh .sae-flag-name{font-weight:700;color:#07314C;display:block}
#smzh-art-enh .sae-flag-desc{color:#5b6b7a;font-size:.86rem;display:block}
#smzh-art-enh .sae-flag-go{color:#0050ff;font-weight:700;font-size:.9rem;white-space:nowrap}
#smzh-art-enh .sae-related h3{font-size:1.15rem;color:#07314C;margin:0 0 1rem;font-weight:700}
#smzh-art-enh .sae-rel-grid{display:grid;grid-template-columns:1fr;gap:.8rem}
@media(min-width:720px){#smzh-art-enh .sae-rel-grid{grid-template-columns:1fr 1fr 1fr}}
#smzh-art-enh .sae-rel{display:flex;flex-direction:column;gap:.35rem;border:1px solid #e7ebef;border-radius:12px;padding:1.1rem 1.2rem;text-decoration:none;background:#fff;transition:.15s}
#smzh-art-enh .sae-rel:hover{border-color:#0050ff;box-shadow:0 8px 20px rgba(7,49,76,.06)}
#smzh-art-enh .sae-rel-cat{font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#0050ff}
#smzh-art-enh .sae-rel-t{font-weight:650;color:#07314C;line-height:1.3}
#smzh-art-enh .sae-rel-d{color:#9aa7b2;font-size:.78rem}
#smzh-art-enh .sae-back{display:inline-block;color:#0050ff;text-decoration:none;font-weight:600;font-size:.92rem}
</style>'''

def chip(item):
    rub=item.get('rubric')
    if not rub or rub not in RUBRIC_INFO:
        href=lk('/de/smzhub/'); lbl='smzhHub'
    else:
        href=lk('/'+RUBRIC_INFO[rub][1]); lbl=RUBRIC_INFO[rub][0]
    rt=f' · {item["readingTime"]} Min Lesezeit' if item.get('readingTime') else ''
    return f'<a class="smzh-hubchip" href="{href}"><b>smzhHub</b> · {esc(lbl)}{rt}</a>'

def end_block(item):
    rub=item.get('rubric')
    info=RUBRIC_INFO.get(rub)
    # CTA
    lead=item.get('leadCta') or '360-Check-Up'
    cta_path=LEAD_PATH.get(lead,'de/terminvereinbaren/')
    advis=info[3] if info else 'Sprechen Sie mit uns – unabhängig, diskret und auf Ihre Situation zugeschnitten.'
    cta=(f'<div class="sae-cta"><div><span class="sae-k">Was bedeutet das für Sie?</span>'
         f'<p>{esc(advis)}</p></div><a class="sae-btn" href="{lk("/"+cta_path)}">{esc(lead)} →</a></div>')
    # Flagship
    flag=''
    skey=info[2] if info else None
    if skey and item.get('series')!=skey and skey in SERIES_NAME:
        nm,path,desc=SERIES_NAME[skey]
        flag=(f'<a class="sae-flag" href="{lk("/"+path)}"><span class="sae-flag-tag">Research-Serie</span>'
              f'<span class="sae-flag-main"><span class="sae-flag-name">{esc(nm)}</span>'
              f'<span class="sae-flag-desc">{esc(desc)} – jetzt vertiefen.</span></span>'
              f'<span class="sae-flag-go">Zur Serie →</span></a>')
    # Related
    rels=related(item); rcards=''
    for r in rels:
        cat=RUBRIC_INFO.get(r.get('rubric'),(None,))[0] or 'smzhHub'
        rcards+=(f'<a class="sae-rel" href="{lk(r["path"])}"><span class="sae-rel-cat">{esc(cat)}</span>'
                 f'<span class="sae-rel-t">{esc(r["title"])}</span>'
                 f'<span class="sae-rel-d">{esc(fdate(r.get("date")))}</span></a>')
    related_html=f'<div class="sae-related"><h3>Weiterlesen im smzhHub</h3><div class="sae-rel-grid">{rcards}</div></div>' if rcards else ''
    back=lk('/'+info[1]) if info else lk('/de/smzhub/')
    back_html=f'<a class="sae-back" href="{back}">← Zurück zum smzhHub</a>'
    return (f'<section id="smzh-art-enh"><div class="sae-wrap">{cta}{flag}{related_html}{back_html}</div></section>')

def enhance(path, item):
    f=os.path.join(SMZH, path.strip('/'), 'index.html')
    if not os.path.exists(f): return False
    h=open(f,encoding='utf-8',errors='ignore').read()
    # idempotent: alte Injektionen entfernen
    h=re.sub(r'<style id="smzh-art-css">.*?</style>','',h,flags=re.S)
    h=re.sub(r'<a class="smzh-hubchip".*?</a>','',h,flags=re.S,count=1)
    h=re.sub(r'<section id="smzh-art-enh">.*?</section>','',h,flags=re.S)
    # CSS in head
    if '</head>' in h: h=h.replace('</head>', CSS+'</head>',1)
    # Chip nach erster </h1>
    if '</h1>' in h: h=h.replace('</h1>', '</h1>'+chip(item),1)
    # End-Block vor Footer
    blk=end_block(item)
    if '<footer' in h: h=h.replace('<footer', blk+'<footer',1)
    elif '</body>' in h: h=h.replace('</body>', blk+'</body>',1)
    else: h=h+blk
    open(f,'w',encoding='utf-8').write(h)
    return True

def main():
    n=0; skip=0
    for r in rows:
        # Nur Text-Artikel/Kommentare/Publikationen/Evergreens (keine Talks/Podcasts)
        if r.get('originalType') in ('flash-talk','edu-talk','podcast'):
            skip+=1; continue
        if enhance(r['path'], r): n+=1
        else: skip+=1
    print(f'OK: {n} Artikelseiten aufgewertet, {skip} übersprungen (Talks/Podcasts/fehlend).')

if __name__=='__main__':
    main()
