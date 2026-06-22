#!/usr/bin/env python3
"""Fuellt die smzHub-Seite mit ALLEN 346 Beitragskarten (statt nur 12 + kaputtem
"Mehr anzeigen"). Karten werden im Original-Design (.blog-card) generiert; Daten
aus build/content-all.json (CMS-API). Bilder werden ueber den Next.js-Optimizer
lokal nachgeladen. "Mehr anzeigen" wird entfernt. Reihenfolge: neueste zuerst.
"""
import os, re, json, urllib.parse, html as H
import sys; sys.path.insert(0,'build')
import postprocess_all as P

HUB='site/smzh.ch/de/smzhub/index.html'
PREFIX='../../'
rows=json.load(open('build/content-all.json',encoding='utf-8'))
h=open(HUB,encoding='utf-8',errors='ignore').read()

# ICON (pen-tool) + CHEVRON aus dem Original extrahieren
icon_m=re.search(r'(<svg[^>]*lucide-pen-tool.*?</svg>)', h, re.S)
ICON=icon_m.group(1) if icon_m else ''
chev_m=re.search(r'<span>Mehr lesen</span>(<svg.*?</svg>)', h, re.S)
CHEV=chev_m.group(1) if chev_m else ''

WRAP=('<div class="blog-card flex h-full flex-col overflow-hidden rounded-xl border '
      'border-neutral-50 bg-white text-brand-700 !w-max-full" data-component-id="C023" variant="blog">')
TYPELABEL={'artikel':'artikel','news':'news','flash-talk':'flash-talk','edu-talk':'edu-talk','podcast':'podcast'}

def img_ref(cms_path):
    if not cms_path: return None
    cms='https://cms.smzh.ch'+cms_path
    enc=urllib.parse.quote(cms, safe='')
    fname=f'index.html@url={enc}&w=640&q=75'
    dest=os.path.join('site','smzh.ch','_next','image',fname)
    P.download(f'https://smzh.ch/_next/image/?url={enc}&w=640&q=75', dest)
    return PREFIX+'_next/image/index.html@url='+enc.replace('%','%25')+'&amp;w=640&amp;q=75'

CELL='<div class="break-inside-avoid col-span-4 block h-full">'

def card(r):
    seg=r['seg']; slug=r['path'].strip('/').split('/')[-1]
    link=PREFIX+'de/'+seg+'/'+slug+'/index.html'
    title=H.escape(r['title'] or '')
    typ=TYPELABEL.get(seg, seg)
    ref=img_ref(r.get('img'))
    img=(f'<div class="relative flex w-full flex-shrink-0"><div class="w-full overflow-hidden">'
         f'<figure data-component-id="C007" class="smzh-image flex flex-col gap-2 object-center h-full w-full">'
         f'<img alt="Article Image" aria-label="Article Image" decoding="async" data-nimg="1" '
         f'class="w-full h-full object-cover object-top aspect-[16/10]" '
         f'src="{ref}" srcset="{ref}"></figure></div></div>') if ref else ''
    body=(f'<div class="flex h-full flex-col justify-between gap-4 p-6"><div class="flex flex-col gap-4">'
          f'<span class="tag flex items-center gap-1 text-xs font-medium uppercase text-neutral-400">{ICON}<span>{typ}</span></span>'
          f'<span class="text-brand-70 text-base font-medium md:text-xl">{title}</span></div>'
          f'<div class="flex self-end"><a target="_self" aria-disabled="false" data-component-id="C011" '
          f'class="smzh-link rounded-lg flex flex-row items-center gap-2 text-left bg-transparent border-none '
          f'text-neutral-900 !p-0.5 hover:underline hover:underline-offset-4 hover:text-neutral-700 px-[18px] py-3" '
          f'href="{link}"><span>Mehr lesen</span>{CHEV}</a></div></div>')
    return CELL+WRAP+img+body+'</div></div>'

def match_div(s, start):
    """Index nach dem schliessenden </div> des bei start (<div) geoeffneten Elements."""
    depth=0; i=start
    for m in re.finditer(r'<(/?)div\b', s[start:]):
        if m.group(1)=='': depth+=1
        else:
            depth-=1
            if depth==0:
                end=start+m.end()
                end=s.find('>',end-4)  # zur schliessenden Klammer von </div>
                return s.find('>', start+m.start())+1 if False else (start+m.end()+ (s[start+m.end():start+m.end()+1]=='>' and 1 or 0))
    return -1

# robusteres Matching: zaehle <div / </div>
def card_end(s, start):
    depth=0; pos=start
    for m in re.finditer(r'<(/?)div\b[^>]*>', s[start:]):
        if m.group(1)=='': depth+=1
        else: depth-=1
        if depth==0: return start+m.end()
    return -1

# erste Karten-Zelle finden und alle Zellen ueberspannen
first=h.find(CELL)
assert first>0, 'keine Karten-Zelle gefunden'
pos=first
while True:
    e=card_end(h,pos)
    nxt=h.find(CELL, e)
    if nxt<0 or (nxt-e)>10:
        last_end=e; break
    pos=nxt
cards_html=''.join(card(r) for r in rows)
new_h=h[:first]+cards_html+h[last_end:]
# "Mehr anzeigen"-Link entfernen
new_h=re.sub(r'<a[^>]*aria-label="Mehr anzeigen"[^>]*>.*?</a>', '', new_h, flags=re.S)
open(HUB,'w',encoding='utf-8').write(new_h)
print('Karten generiert:',len(rows),'| Bytes Hub:',len(new_h),'| Bild-Downloads:',P.stats['img_dl'])
