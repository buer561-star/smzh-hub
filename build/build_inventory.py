#!/usr/bin/env python3
"""Iteration 1 – Content-Inventar fuer den smzhHub.
Baut build/smzhhub-content.json aus: CMS-API (Typ, Kategorien, Excerpt, Bild,
Datum) + lokalen HTML-Snapshots (PDF-Verknuepfung, Lesezeit). Reine Datenarbeit,
kein UI. Anschliessend Validierung + Qualitaetsbericht.
Es wird NICHTS am site/ veraendert (nur gelesen) und nur build/ geschrieben.
"""
import json, os, re, ssl, html as H, sys, urllib.parse
from urllib.request import urlopen, Request

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch'); UPLOADS=os.path.join(SITE,'cms.smzh.ch','uploads')
CTX=ssl.create_default_context(); CTX.check_hostname=False; CTX.verify_mode=ssl.CERT_NONE
UA={'User-Agent':'Mozilla/5.0'}

def api(start):
    u=('https://cms.smzh.ch/api/web/content-hub?locale=de&types=artikel%2Cnew%2Cflash-talk%2Cpodcast%2Cedu-talk'
       f'&categories=&pagination%5Bstart%5D={start}&pagination%5Blimit%5D=100')
    return json.load(urlopen(Request(u,headers=UA),context=CTX,timeout=60))['data']

TYPESEG={'artikel':'artikel','new':'news','news':'news','flash-talk':'flash-talk','edu-talk':'edu-talk','podcast':'podcast'}
GENERIC_PDF=('smzh_datenschutz','smzh_impressum','smzh_e_mail','e_mail_korrespondenz')

# ---- Erkennungs-Heuristiken -------------------------------------------------
def detect_series(title, slug, pdfs):
    """Titelbasiert (robust gegen Blogs, die eine Publikation nur verlinken)."""
    s=(slug or '').lower(); t=(title or '').lower()
    if re.search(r'hypotheken[\s-]?radar', t) or 'hypotheken-radar' in s:
        return 'hypothekenradar'
    if re.search(r'investment[\s-]?guide', t) or 'investment-guide' in s:
        return 'investment-guide'
    if re.search(r'(aktuelle beurteilung des immobilienmarkt|beurteilung des immobilienmarkt|'
                 r'ausblick immobilienmarkt|immobilien[\s-]?outlook|einsch[äa]tzung immobilienmarkt|'
                 r'q\d[\s/]*\d{4}.*immobilienmarkt)', t):
        return 'immobilien-outlook'
    return None

EVERGREEN_RE=re.compile(r'(^\d+\s|grundlagen|ratgeber|einmaleins|3[- ]?s[äa]ulen|s[äa]ule\s?3a|schritt f[üu]r schritt|'
                        r'was ist|so funktioniert|guide|leitfaden|wie (kaufe|erstelle|funktioniert))', re.I)

def detect_contenttype(seg, title, slug, series):
    if seg=='news': return 'news'
    if seg in ('flash-talk','edu-talk'): return 'talk'
    if seg=='podcast': return 'podcast'
    # artikel
    if series: return 'publication'
    if EVERGREEN_RE.search((title or '')+' '+(slug or '')): return 'evergreen'
    return 'blog'

def cadence_for(series, ctype):
    if series in ('hypothekenradar','investment-guide'): return 'monthly'
    if series=='immobilien-outlook': return 'quarterly'
    if ctype=='evergreen': return 'evergreen'
    return 'adhoc'

TOPIC_KW={
 'Hypotheken':['hypothek','snb','zins','tragbarkeit','amortis','saron'],
 'Anlagen':['anlage','aktien','invest','portfolio','gold','etf','b[öo]rse','fed','rendite','obligation','krypto','bitcoin'],
 'Vorsorge':['vorsorge','pension','s[äa]ule','ahv','bvg','3a','pensionskasse','rente'],
 'Immobilien':['immobilie','eigenheim','wohneigentum','wohnen','liegenschaft','bauen','renovier'],
 'Steuern':['steuer'],
 'Recht':['erb','testament','nachlass','recht','g[üu]ter','ehe','scheidung','vorsorgeauftrag'],
 'Versicherungen':['versicher','krankenkasse','vvg','kvg'],
 'KMU':['kmu','unternehm','firma','gesch[äa]ft','lohn','dividende'],
 'Finanzen':['finanzplan','budget','sparen','finanzierung','verm[öo]gen'],
}
def detect_topics(api_cats, title, slug, pdfs):
    topics=[c for c in api_cats if c and c!='Events']
    blob=' '.join([title or '', slug or '']+pdfs).lower()
    for topic,kws in TOPIC_KW.items():
        if topic in topics: continue
        if any(re.search(k,blob) for k in kws): topics.append(topic)
    return topics

def detect_audience(topics, title):
    t=(title or '').lower(); aud=set()
    if 'Immobilien' in topics or 'eigenheim' in t or 'kaufen' in t: aud.add('Eigenheimkäufer')
    if 'Anlagen' in topics: aud.add('Anleger')
    if 'Vorsorge' in topics: aud.add('Pensionierungsplanung')
    if re.search(r'\b40\b|über 40|ü40',t): aud.add('40plus')
    if 'KMU' in topics: aud.add('Unternehmer')
    if re.search(r'famil|kind|heirat|scheidung|konkubinat',t): aud.add('Familien')
    return sorted(aud)

LEADCTA={'Hypotheken':'Hypothekenberatung','Vorsorge':'Vorsorgeanalyse','Anlagen':'Anlageberatung',
         'Finanzen':'Anlageberatung','Steuern':'Steuerberatung','Immobilien':'Immobilienberatung',
         'KMU':'KMU-Beratung','Recht':'Nachlassberatung','Versicherungen':'Versicherungsberatung'}
def lead_cta(topics):
    for t in ['Hypotheken','Vorsorge','Immobilien','Anlagen','Steuern','KMU','Recht','Versicherungen','Finanzen']:
        if t in topics: return LEADCTA[t]
    return '360-Check-Up'

def hub_type(seg, ctype, series, topics):
    """Redaktioneller Typ fuer den Hub."""
    if series: return 'serie'
    if ctype=='evergreen': return 'evergreen'
    if seg=='news': return 'kommentar'
    if seg in ('flash-talk','edu-talk'): return 'talk'
    if seg=='podcast': return 'podcast'
    # artikel
    if topics: return 'kommentar'
    return 'blog'

def flatten_excerpt(rich):
    if not isinstance(rich,list): return ''
    out=[]
    for blk in rich:
        for ch in (blk.get('children') or []):
            if ch.get('text'): out.append(ch['text'])
    return re.sub(r'\s+',' ',' '.join(out)).strip()

def best_img(mi):
    if not mi: return None
    f=mi.get('formats') or {}
    for k in ('medium','small','large','thumbnail'):
        if f.get(k) and f[k].get('url'): return f[k]['url']
    return mi.get('url')

def image_local(img):
    """Pfad (relativ zu site/) der lokal vorhandenen Optimizer-Variante, sonst None."""
    if not img: return None
    enc=urllib.parse.quote('https://cms.smzh.ch'+img, safe='')
    rel=os.path.join('smzh.ch','_next','image',f'index.html@url={enc}&w=640&q=75')
    return rel if os.path.exists(os.path.join(SITE, rel)) else None

def snapshot_pdfs_and_reading(path):
    f=os.path.join(SMZH, path.strip('/'), 'index.html')
    pdfs=[]; reading=None; lead=''
    if os.path.exists(f):
        html=open(f,encoding='utf-8',errors='ignore').read()
        for m in re.findall(r'uploads/([^"\']+\.pdf)', html):
            low=m.lower()
            if any(g in low for g in GENERIC_PDF): continue
            if m not in pdfs: pdfs.append(m)
        mh=re.search(r'<h1', html)
        if mh:
            seg=html[mh.start():]
            cut=seg.find('Termin vereinbaren')
            body=seg[:cut] if cut>0 else seg
            text=re.sub(r'<[^>]+>',' ', body)
            words=len(re.findall(r'\w+', text))
            if 60<words<8000: reading=max(1,round(words/200))
            # Lead-Absatz als Excerpt-Fallback (erster sinnvoller <p>, ohne Cookie-Text)
            for pm in re.findall(r'<p[^>]*>(.*?)</p>', body, re.S):
                txt=H.unescape(re.sub(r'<[^>]+>','',pm)).strip()
                if len(txt)>80 and 'Cookies' not in txt and 'Wir verwenden' not in txt:
                    lead=re.sub(r'\s+',' ',txt)[:320]; break
    return pdfs, reading, lead

# ---- Build ------------------------------------------------------------------
def build():
    items=[]
    for s in (0,100,200,300): items+=api(s)
    rows=[]; seen=set()
    for it in items:
        seg=TYPESEG.get(it.get('type')); slug=it.get('slug')
        if not seg or not slug: continue
        path=f"/de/{seg}/{slug}/"
        if path in seen: continue
        seen.add(path)
        title=it.get('title') or ''
        api_cats=[ (c.get('title')) for c in (it.get('categories') or []) if c.get('title') ]
        pdfs, reading, lead = snapshot_pdfs_and_reading(path)
        series=detect_series(title, slug, pdfs)
        ctype=detect_contenttype(seg, title, slug, series)
        topics=detect_topics(api_cats, title, slug, pdfs)
        img=best_img(it.get('mainImage'))
        excerpt=flatten_excerpt(it.get('shortExcerpt')) or lead
        rows.append({
            'id': it.get('id'),
            'title': title,
            'slug': slug,
            'path': path,
            'localUrl': f"smzh.ch{path}index.html",
            'originalType': seg,
            'contentType': ctype,
            'hubType': hub_type(seg, ctype, series, topics),
            'series': series,
            'cadence': cadence_for(series, ctype),
            'topics': topics,
            'audience': detect_audience(topics, title),
            'date': it.get('publishedDate') or it.get('publishedAt'),
            'excerpt': excerpt,
            'image': img,
            'imageLocal': image_local(img),
            'pdfs': pdfs,
            'readingTime': reading,
            'leadCta': lead_cta(topics),
        })
    rows.sort(key=lambda r: r.get('date') or '', reverse=True)
    json.dump(rows, open('build/smzhhub-content.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    return rows

if __name__=='__main__':
    rows=build()
    print('GEBAUT: build/smzhhub-content.json |', len(rows),'Eintraege')
