#!/usr/bin/env python3
"""Erzeugt docs/smzhub-content-taxonomy.md aus build/smzhhub-content.json.
Dokumentiert je Beitrag: Titel, Content-Typ, Hauptthema, Nebenthemen,
Zielgruppe, Hub-Startseite erlaubt?, Lead-geeignet?, Rubrik und WARUM.
Reine Doku-Arbeit, aendert site/ nicht.
"""
import json, collections
from datetime import datetime

rows=json.load(open('build/smzhhub-content.json',encoding='utf-8'))

RUBRIC_TITLE={
 'kapitalmaerkte':'Kapitalmärkte & Anlegen',
 'immobilien':'Immobilien & Hypotheken',
 'vorsorge':'Vorsorge & Pensionierung',
 'steuern':'Steuern & Finanzplanung',
 None:'— (keine Themenwelt)',
}
CTYPE_LABEL={
 'serie':'Serie/Publikation','kommentar':'Kommentar','evergreen':'Evergreen/Guide',
 'talk':'Talk','podcast':'Podcast','blog':'Meldung/Blog',
}
RUBRIC_REASON={
 'kapitalmaerkte':'CMS-Kategorie „Anlagen" → Anlegerperspektive (Märkte, Strategie, Portfolio).',
 'immobilien':'CMS-Kategorie „Immobilien"/„Hypotheken" → Eigenheim, Tragbarkeit, Hypothekarmarkt, Immobilienregulierung.',
 'vorsorge':'CMS-Kategorie „Vorsorge" → AHV/BVG/Säule 3a, Pensionierung, Vorsorgelücken.',
 'steuern':'CMS-Kategorie „Steuern"/„Finanzen" → Steueroptimierung & Finanzplanung.',
 None:'Thema (Recht/Versicherungen/KMU/PR-Meldung) gehört in keine der 4 Hub-Themenwelten.',
}
SERIES_NOTE={
 'investment-guide':'Flagship-Anker in **Kapitalmärkte & Anlegen** (Doppelfunktion: eigene Reihe + Rubrik-Anker).',
 'hypothekenradar':'Flagship-Anker in **Immobilien & Hypotheken**.',
 'immobilien-outlook':'Flagship-Anker in **Immobilien & Hypotheken**.',
}

def fmt(iso):
    if not iso: return '–'
    try: return datetime.fromisoformat(iso.replace('Z','+00:00')).strftime('%Y-%m')
    except Exception: return '–'

def yn(b): return '✅ ja' if b else '— nein'

def reason_for(r):
    base=RUBRIC_REASON.get(r['rubric'],'')
    if r['series'] in SERIES_NOTE:
        return SERIES_NOTE[r['series']]
    return base

lines=[]
A=lines.append
A('# smzhHub – Content-Taxonomie & Rubriken-Zuordnung\n')
A(f'_Generiert aus `build/smzhhub-content.json` ({len(rows)} Beiträge)._\n')
A('Grundregel: **Kein Artikel erscheint in einer Rubrik, nur weil dort Platz frei ist.** '
  'Jeder Beitrag hat genau eine kanonische Themenwelt (oder keine). Die Zuordnung folgt '
  'den redaktionell gesetzten CMS-Kategorien mit fester Priorität: '
  '`Immobilien/Hypotheken > Vorsorge > Steuern > Anlagen/Finanzen`. '
  'Serien sind in ihrer Themenwelt verankert.\n')

# --- Überblick ---
A('## 1. Überblick\n')
A('### Verteilung auf Themenwelten (alle Beiträge)\n')
A('| Themenwelt | Beiträge gesamt | davon Hub-fähig | davon Lead-fähig |')
A('|---|--:|--:|--:|')
rc=collections.Counter(r['rubric'] for r in rows)
he=collections.Counter(r['rubric'] for r in rows if r['hubEligible'])
le=collections.Counter(r['rubric'] for r in rows if r['leadEligible'])
for k in ['kapitalmaerkte','immobilien','vorsorge','steuern',None]:
    A(f"| {RUBRIC_TITLE[k]} | {rc.get(k,0)} | {he.get(k,0)} | {le.get(k,0)} |")
A('')
A('### Content-Typen\n')
A('| Typ | Anzahl |')
A('|---|--:|')
for k,v in collections.Counter(r['hubType'] for r in rows).most_common():
    A(f"| {CTYPE_LABEL.get(k,k)} | {v} |")
A('')

# --- Flagship-Anker ---
A('## 2. Flagship-Anker (Serien mit Doppelfunktion)\n')
A('| Serie | Ausgaben | Verankert in | Takt |')
A('|---|--:|---|---|')
for s,note in SERIES_NOTE.items():
    items=[r for r in rows if r['series']==s]
    if not items: continue
    rub=RUBRIC_TITLE[items[0]['rubric']]
    cad=items[0].get('cadence','')
    A(f"| {items[0]['series']} | {len(items)} | {rub} | {cad} |")
A('')

# --- Pro Rubrik die Beiträge ---
A('## 3. Beiträge je Themenwelt\n')
for k in ['kapitalmaerkte','immobilien','vorsorge','steuern']:
    items=sorted([r for r in rows if r['rubric']==k],
                 key=lambda r:r.get('date') or '', reverse=True)
    A(f'### {RUBRIC_TITLE[k]}  ({len(items)} Beiträge)\n')
    A('| Titel | Typ | Hauptthema | Nebenthemen | Zielgruppe | Hub | Lead | Datum |')
    A('|---|---|---|---|---|:-:|:-:|---|')
    for r in items:
        topics=r['topics'] or []
        main=topics[0] if topics else '–'
        sec=', '.join(topics[1:]) or '–'
        aud=', '.join(r['audience']) or '–'
        title=r['title'].replace('|','/')[:80]
        A(f"| {title} | {CTYPE_LABEL.get(r['hubType'],r['hubType'])} | {main} | {sec} | {aud} | "
          f"{'✅' if r['hubEligible'] else '—'} | {'✅' if r['leadEligible'] else '—'} | {fmt(r.get('date'))} |")
    A('')
    A(f"**Begründung der Zuordnung:** {RUBRIC_REASON[k]}\n")

# --- Ohne Rubrik ---
none_items=[r for r in rows if r['rubric'] is None]
A(f'## 4. Bewusst ohne Themenwelt  ({len(none_items)} Beiträge)\n')
A('Diese Beiträge erscheinen **nicht** in den 4 Hub-Themenwelten – meist PR-/Unternehmens-'
  'meldungen oder Themen (Recht, Versicherungen, KMU), für die der Hub keine eigene '
  'Themenwelt führt. Sie bleiben über das Gesamtarchiv erreichbar.\n')
A('| Titel | Typ | Themen | Grund |')
A('|---|---|---|---|')
for r in sorted(none_items,key=lambda r:r.get('date') or '',reverse=True):
    title=r['title'].replace('|','/')[:80]
    tp=', '.join(r['topics']) or '–'
    grund='PR/Meldung ohne Finanzthema' if not r['topics'] else 'Thema ausserhalb der Hub-Welten'
    A(f"| {title} | {CTYPE_LABEL.get(r['hubType'],r['hubType'])} | {tp} | {grund} |")
A('')

open('docs/smzhub-content-taxonomy.md','w',encoding='utf-8').write('\n'.join(lines))
print('GEBAUT: docs/smzhub-content-taxonomy.md |', len(rows), 'Beitraege dokumentiert')
