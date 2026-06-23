#!/usr/bin/env python3
"""Phase 7 (V3) – Artikel-Detailseiten als Teil des Advisory-Hubs aufwerten.
Fügt OHNE Fliesstext-Eingriff hinzu:
  - smzhHub-Rubrik-Chip + Lesedauer unter der H1
  - Brief-Karte: "Darum geht es" (Excerpt) + "Das erfahren Sie" (Abschnitte als
    Anker, aus den eigenen H2/H3 – Boilerplate gefiltert)
  - End-Block: "Was bedeutet das für mich?" (kontextbezogener Beratungs-CTA),
    Flagship-Serie, 3 Related-Beiträge der Rubrik, Zurück-zum-Hub.
V3-Designsprache (weiss/navy/sans). Idempotent.
"""
import json, os, re, html as H
from datetime import datetime

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch')
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))
REL='../../../'
MON={'Jan':'Jan','Feb':'Feb','Mar':'März','Apr':'Apr','May':'Mai','Jun':'Juni','Jul':'Juli','Aug':'Aug','Sep':'Sep','Oct':'Okt','Nov':'Nov','Dec':'Dez'}
def fdate(iso):
    if not iso: return ''
    try: d=datetime.fromisoformat(iso.replace('Z','+00:00')); return f"{MON[d.strftime('%b')]} {d.year}"
    except Exception: return ''
def esc(s): return H.escape(s or '')
def lk(path): return REL+'/'.join(s for s in path.strip('/').split('/') if s)+'/index.html'

RUBRIC_INFO={
 'immobilien':('Eigenheim','de/smzhub-eigenheim/','hypothekenradar','Ob Kauf, Tragbarkeit oder Anschlussfinanzierung – wir ordnen Ihre Hypothekarsituation unabhängig ein.'),
 'kapitalmaerkte':('Vermögen','de/smzhub-vermoegen/','investment-guide','Von der Anlagestrategie bis zur Portfolioüberprüfung – wir schauen mit Ihnen auf Ihre Situation.'),
 'vorsorge':('Zukunft','de/smzhub-zukunft/',None,'AHV, Pensionskasse und Säule 3a: Wir machen Ihre Pensionierung planbar.'),
 'steuern':('Steuern','de/smzhub-steuern/',None,'Steuern senken und Vermögen strukturieren – konkret auf Ihre Situation bezogen.'),
}
SERIES_NAME={'hypothekenradar':('Hypotheken-Radar','de/smzhub-serie-hypotheken-radar/','Monatliches Hypotheken-Research'),
 'investment-guide':('Investment Guide','de/smzhub-serie-investment-guide/','Monatliche Anlageeinschätzung'),
 'immobilien-outlook':('Immobilien-Outlook','de/smzhub-serie-immobilien-outlook/','Quartalsweiser Immobilienmarkt-Ausblick')}
LEAD_PATH={'Hypothekenberatung':'de/immobilienbewertung/','Vorsorgeanalyse':'de/vorsorgeanalyse/',
 'Anlageberatung':'de/terminvereinbaren/','Steuerberatung':'de/steuererklaerung/','Immobilienberatung':'de/immobilienbewertung/',
 'KMU-Beratung':'de/terminvereinbaren/','Nachlassberatung':'de/terminvereinbaren/','Versicherungsberatung':'de/terminvereinbaren/','360-Check-Up':'de/terminvereinbaren/'}

def related(item):
    rub=item.get('rubric')
    pool=[r for r in rows if r.get('rubric')==rub and r['id']!=item['id'] and r.get('hubEligible')] if rub \
         else [r for r in rows if r.get('hubEligible') and r['id']!=item['id']]
    pool.sort(key=lambda r:r.get('date') or '', reverse=True)
    return pool[:3]

CSS='''<style id="smzh-art-css">
.smzha{--brand:#07314C;--blue:#0050ff;--ink:#0f2231;--muted:#5b6b7a;--faint:#8b9aa8;--line:#e4e9ee;--surf:#f5f8fb}
.smzh-hubchip{display:inline-flex;align-items:center;gap:.5rem;margin:.3rem 0 1rem;padding:.34rem .8rem;border:1px solid #e4e9ee;border-radius:999px;background:#f5f8fb;color:#07314C;text-decoration:none;font-size:.78rem;font-weight:600}
.smzh-hubchip b{color:#0050ff;font-weight:800}
.smzh-hubchip:hover{border-color:#0050ff}
.smzha-brief{border:1px solid #e4e9ee;border-radius:12px;background:#fff;margin:0 0 1.8rem;overflow:hidden}
.smzha-brief-s{padding:1.1rem 1.3rem}
.smzha-brief-s+.smzha-brief-s{border-top:1px solid #e4e9ee;background:#f5f8fb}
.smzha-k{display:block;font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;font-weight:800;color:#0050ff;margin-bottom:.5rem}
.smzha-darum{color:#2c2f33;line-height:1.55;margin:0;font-size:1.02rem}
.smzha-toc{margin:0;padding:0;list-style:none;display:grid;grid-template-columns:1fr;gap:.4rem}
@media(min-width:620px){.smzha-toc{grid-template-columns:1fr 1fr}}
.smzha-toc li{counter-increment:tc}
.smzha-toc a{display:flex;gap:.6rem;color:#07314C;text-decoration:none;font-weight:600;font-size:.92rem;align-items:baseline}
.smzha-toc a:before{content:counter(tc,decimal-leading-zero);color:#8b9aa8;font-weight:800;font-size:.72rem}
.smzha-toc a:hover{color:#0050ff}
.smzha-toc{counter-reset:tc}
.smzha-toc li.lvl3 a{font-weight:500;color:#3a5a72;padding-left:1.3rem}
#smzh-art-enh{margin:3.2rem 0 0;border-top:1px solid #e4e9ee}
#smzh-art-enh .sae-wrap{max-width:1080px;margin:0 auto;padding:2.4rem 1.4rem 1rem;display:flex;flex-direction:column;gap:1.6rem}
#smzh-art-enh .sae-cta{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:1.2rem;background:#07314C;border-radius:12px;padding:1.7rem 1.9rem}
#smzh-art-enh .sae-k{display:block;font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#9fc0d6;font-weight:800;margin-bottom:.35rem}
#smzh-art-enh .sae-cta p{color:#c7d6e2;margin:0;max-width:58ch;line-height:1.5}
#smzh-art-enh .sae-btn{background:#fff;color:#07314C;font-weight:700;text-decoration:none;padding:.8rem 1.5rem;border-radius:8px;white-space:nowrap}
#smzh-art-enh .sae-flag{display:flex;align-items:center;gap:1rem;border:1px solid #e4e9ee;border-radius:10px;padding:1rem 1.2rem;text-decoration:none;background:#fff}
#smzh-art-enh .sae-flag-tag{font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#1f9d7a;background:#e2f2ee;padding:.2rem .55rem;border-radius:5px;white-space:nowrap}
#smzh-art-enh .sae-flag-main{flex:1;display:flex;flex-direction:column;gap:.1rem}
#smzh-art-enh .sae-flag-name{font-weight:700;color:#07314C}
#smzh-art-enh .sae-flag-desc{color:#5b6b7a;font-size:.84rem}
#smzh-art-enh .sae-flag-go{color:#0050ff;font-weight:700;font-size:.86rem;white-space:nowrap}
#smzh-art-enh .sae-related h3{font-size:.7rem;letter-spacing:.1em;text-transform:uppercase;color:#0050ff;margin:0 0 1rem;font-weight:800}
#smzh-art-enh .sae-rel-grid{display:grid;grid-template-columns:1fr;gap:.7rem}
@media(min-width:720px){#smzh-art-enh .sae-rel-grid{grid-template-columns:1fr 1fr 1fr}}
#smzh-art-enh .sae-rel{display:flex;flex-direction:column;gap:.3rem;border:1px solid #e4e9ee;border-radius:10px;padding:1rem 1.1rem;text-decoration:none;background:#fff;transition:.15s}
#smzh-art-enh .sae-rel:hover{border-color:#0050ff;box-shadow:0 10px 24px -16px rgba(7,49,76,.5)}
#smzh-art-enh .sae-rel-cat{font-size:.62rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;color:#0050ff}
#smzh-art-enh .sae-rel-t{font-weight:700;color:#07314C;line-height:1.3;font-size:.96rem}
#smzh-art-enh .sae-rel-d{color:#8b9aa8;font-size:.76rem}
#smzh-art-enh .sae-back{display:inline-block;color:#0050ff;text-decoration:none;font-weight:700;font-size:.9rem}
</style>'''

def chip(item):
    rub=item.get('rubric')
    href,lbl=(lk('/'+RUBRIC_INFO[rub][1]),RUBRIC_INFO[rub][0]) if rub in RUBRIC_INFO else (lk('/de/smzhub/'),'smzhHub')
    rt=f' · {item["readingTime"]} Min Lesezeit' if item.get('readingTime') else ''
    return f'<a class="smzh-hubchip" href="{href}"><b>smzhHub</b> · {esc(lbl)}{rt}</a>'

def slugify(t):
    t=(t or '').lower().replace('ä','ae').replace('ö','oe').replace('ü','ue').replace('ß','ss')
    return (re.sub(r'[^a-z0-9]+','-',t).strip('-')[:50]) or 'abschnitt'

def headings(h):
    mh=re.search(r'</h1>',h)
    if not mh: return h,[]
    start=mh.end(); foot=h.find('<footer',start); end=foot if foot>0 else len(h)
    region=h[start:end]; entries=[]; used=set()
    def repl(m):
        tag,attrs,inner=m.group(1),m.group(2),m.group(3)
        text=re.sub(r'<[^>]+>','',inner).strip()
        if not text or len(text)>90: return m.group(0)
        idm=re.search(r'\sid="([^"]*)"',attrs)
        if idm and idm.group(1).strip(): sid=idm.group(1)
        else:
            sid='sec-'+slugify(text); base=sid; i=2
            while sid in used: sid=f'{base}-{i}'; i+=1
            attrs=(attrs[:idm.start()]+f' id="{sid}"'+attrs[idm.end():]) if idm else attrs+f' id="{sid}"'
        used.add(sid); entries.append((tag,sid,text))
        return f'<{tag}{attrs}>{inner}</{tag}>'
    newregion=re.sub(r'<(h[23])\b([^>]*)>(.*?)</\1>',repl,region,flags=re.S)
    h=h[:start]+newregion+h[end:]
    STOP={'die smzh für sie','kontaktieren sie uns','verwandte inhalte','das könnte sie auch interessieren',
          'newsletter','häufige fragen','termin vereinbaren','das könnte dich auch interessieren'}
    cut=len(entries)
    for i,(t,s,x) in enumerate(entries):
        if x.lower().strip() in STOP: cut=i; break
    entries=[e for e in entries[:cut] if e[2].lower().strip() not in STOP][:8]
    return h,entries

def brief(item, entries):
    parts=''
    ex=item.get('excerpt')
    if ex and len(ex)>60:
        parts+=f'<div class="smzha-brief-s"><span class="smzha-k">Darum geht es</span><p class="smzha-darum">{esc(ex[:320])}</p></div>'
    if len(entries)>=3:
        lis=''.join(f'<li class="{("lvl3" if t=="h3" else "lvl2")}"><a href="#{s}">{esc(x)}</a></li>' for t,s,x in entries)
        parts+=f'<div class="smzha-brief-s"><span class="smzha-k">Das erfahren Sie</span><ul class="smzha-toc">{lis}</ul></div>'
    return f'<!--smzha-brief--><div class="smzha smzha-brief">{parts}</div><!--/smzha-brief-->' if parts else ''

def end_block(item):
    rub=item.get('rubric'); info=RUBRIC_INFO.get(rub)
    lead=item.get('leadCta') or '360-Check-Up'; cta_path=LEAD_PATH.get(lead,'de/terminvereinbaren/')
    advis=info[3] if info else 'Sprechen Sie mit uns – unabhängig, diskret und auf Ihre Situation zugeschnitten.'
    cta=(f'<div class="sae-cta"><div><span class="sae-k">Was bedeutet das für mich?</span>'
         f'<p>{esc(advis)}</p></div><a class="sae-btn" href="{lk("/"+cta_path)}">{esc(lead)} →</a></div>')
    flag=''; skey=info[2] if info else None
    if skey and item.get('series')!=skey and skey in SERIES_NAME:
        nm,path,desc=SERIES_NAME[skey]
        flag=(f'<a class="sae-flag" href="{lk("/"+path)}"><span class="sae-flag-tag">Research-Serie</span>'
              f'<span class="sae-flag-main"><span class="sae-flag-name">{esc(nm)}</span>'
              f'<span class="sae-flag-desc">{esc(desc)} – jetzt vertiefen.</span></span>'
              f'<span class="sae-flag-go">Zur Serie →</span></a>')
    rcards=''
    for r in related(item):
        cat=RUBRIC_INFO.get(r.get('rubric'),(None,))[0] or 'smzhHub'
        rcards+=(f'<a class="sae-rel" href="{lk(r["path"])}"><span class="sae-rel-cat">{esc(cat)}</span>'
                 f'<span class="sae-rel-t">{esc(r["title"])}</span><span class="sae-rel-d">{esc(fdate(r.get("date")))}</span></a>')
    rel=f'<div class="sae-related"><h3>Weiterlesen im smzhHub</h3><div class="sae-rel-grid">{rcards}</div></div>' if rcards else ''
    back=lk('/'+info[1]) if info else lk('/de/smzhub/')
    return f'<section id="smzh-art-enh"><div class="sae-wrap smzha">{cta}{flag}{rel}<a class="sae-back" href="{back}">← Zurück zum smzhHub</a></div></section>'

def enhance(path, item):
    f=os.path.join(SMZH, path.strip('/'), 'index.html')
    if not os.path.exists(f): return False
    h=open(f,encoding='utf-8',errors='ignore').read()
    h=re.sub(r'<style id="smzh-art-css">.*?</style>','',h,flags=re.S)
    h=re.sub(r'<a class="smzh-hubchip".*?</a>','',h,flags=re.S,count=1)
    h=re.sub(r'<!--smzha-brief-->.*?<!--/smzha-brief-->','',h,flags=re.S)
    h=re.sub(r'<nav class="smzh-toc".*?</nav>','',h,flags=re.S,count=1)
    h=re.sub(r'<section id="smzh-art-enh">.*?</section>','',h,flags=re.S)
    if '</head>' in h: h=h.replace('</head>', CSS+'</head>',1)
    h, entries = headings(h)
    inject=chip(item)+brief(item, entries)
    if '</h1>' in h: h=h.replace('</h1>', '</h1>'+inject,1)
    blk=end_block(item)
    if '<footer' in h: h=h.replace('<footer', blk+'<footer',1)
    elif '</body>' in h: h=h.replace('</body>', blk+'</body>',1)
    else: h=h+blk
    open(f,'w',encoding='utf-8').write(h)
    return True

def main():
    n=0; skip=0
    for r in rows:
        if r.get('originalType') in ('flash-talk','edu-talk','podcast'): skip+=1; continue
        if enhance(r['path'], r): n+=1
        else: skip+=1
    print(f'OK: {n} Artikelseiten aufgewertet (V3), {skip} übersprungen.')

if __name__=='__main__':
    main()
