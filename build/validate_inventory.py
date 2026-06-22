#!/usr/bin/env python3
"""Validiert build/smzhhub-content.json gegen die lokalen Dateien und gibt einen
Qualitaetsbericht aus. Reine Lese-/Pruefarbeit."""
import json, os, re, urllib.parse, collections

SITE='site'; SMZH=os.path.join(SITE,'smzh.ch'); UPLOADS=os.path.join(SITE,'cms.smzh.ch','uploads')
rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))

miss_url=[]; miss_pdf=[]; no_img=[]; no_local_img=[]; no_excerpt=[]; no_topic=[]; no_date=[]
for r in rows:
    if not os.path.exists(os.path.join(SITE, r['localUrl'])): miss_url.append(r['slug'])
    for p in r['pdfs']:
        if not os.path.exists(os.path.join(UPLOADS, p)): miss_pdf.append((r['slug'],p))
    if not r['image']: no_img.append(r['slug'])
    elif not r.get('imageLocal') or not os.path.exists(os.path.join(SITE, r['imageLocal'])): no_local_img.append(r['slug'])
    if not r['excerpt']: no_excerpt.append(r['slug'])
    if not r['topics']: no_topic.append(r['slug'])
    if not r['date']: no_date.append(r['slug'])

# Dubletten
paths=collections.Counter(r['path'] for r in rows)
dupes=[p for p,c in paths.items() if c>1]

def dist(key):
    c=collections.Counter()
    for r in rows:
        v=r[key]
        if isinstance(v,list):
            for x in v: c[x]+=1
        else: c[v if v is not None else '∅']+=1
    return c

print("====== INVENTAR-QUALITAETSBERICHT ======")
print("Total Inhalte:", len(rows))
print("\n-- originalType --"); [print(f"  {k:12} {v}") for k,v in dist('originalType').most_common()]
print("\n-- contentType --"); [print(f"  {k:12} {v}") for k,v in dist('contentType').most_common()]
print("\n-- series --"); [print(f"  {str(k):16} {v}") for k,v in dist('series').most_common()]
print("\n-- cadence --"); [print(f"  {k:12} {v}") for k,v in dist('cadence').most_common()]
print("\n-- topics --"); [print(f"  {k:16} {v}") for k,v in dist('topics').most_common()]
print("\n-- audience --"); [print(f"  {k:22} {v}") for k,v in dist('audience').most_common()]
print("\n-- leadCta --"); [print(f"  {k:22} {v}") for k,v in dist('leadCta').most_common()]
print("\nInhalte mit PDF:", sum(1 for r in rows if r['pdfs']))
print("Inhalte mit readingTime:", sum(1 for r in rows if r['readingTime']))
print("\n====== DATENLUECKEN ======")
print("ohne Bild (image=null):", len(no_img), no_img[:6])
print("Bild referenziert, aber lokal NICHT vorhanden:", len(no_local_img), no_local_img[:6])
print("ohne Excerpt:", len(no_excerpt), no_excerpt[:6])
print("ohne Thema:", len(no_topic), no_topic[:10])
print("ohne Datum:", len(no_date))
print("\n====== LINK-/DATEI-PRUEFUNG ======")
print("localUrl FEHLT (Seite nicht vorhanden):", len(miss_url), miss_url[:6])
print("PDF-Pfad FEHLT:", len(miss_pdf), miss_pdf[:6])
print("Dubletten (gleicher path):", len(dupes), dupes[:6])
print("\n====== DUMMY-CHECK ======")
fabricated=[r['slug'] for r in rows if not os.path.exists(os.path.join(SITE,r['localUrl']))]
print("Eintraege ohne reale lokale Seite (=erfunden?):", len(fabricated))
print("JSON valide: JA (geladen)")
