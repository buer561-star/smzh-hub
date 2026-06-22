# smzhHub – Redesign Audit-Log

Strategischer Neuaufbau als simuliertes Multi-Agent-Team (Product Strategist,
Editorial Director, UX/IA, Visual Designer, Conversion Strategist, Content
Librarian, Frontend Engineer, Mobile UX Auditor). Lead Architect entscheidet.

**Ziele (alles gleichzeitig maximieren):** Thought Leadership · Lead Generation ·
Institutional Appearance · Entertainment & Problem Solving.

## Backup
- Pre-Redesign-Stand: Commit `782ac2a` + `build/backup/karussell-3rubriken/`.
- Zweites Referenz-Backup: `build/backup/radikale-vereinfachung/` (`d908058`).
- Übersicht: `docs/smzhub-snapshots.md`.

## Phase 1 – Content-Inventar
- `build/build_inventory.py` → `build/smzhhub-content.json` (346 reale Inhalte,
  kanonische Rubrik je Beitrag, hubEligible/leadEligible).
- `build/smzhub-placeholders.json` → 4 klar markierte Platzhalter (Dossiers,
  Guide, Tool) für dünne Rubriken.
- Taxonomie-Doku: `docs/smzhub-content-taxonomy.md`.

## Phase 3 – Konzeptvarianten (Bewertung 1–10)

| Dimension | A Editorial | B Decision | C Research | **D Hybrid** |
|---|--:|--:|--:|--:|
| Thought Leadership | 8 | 6 | 9 | **9** |
| Lead Generation | 6 | 9 | 6 | **9** |
| Institutional Appearance | 7 | 5 | 9 | **9** |
| Entertainment & Problem Solving | 8 | 9 | 5 | **9** |
| Nutzerklarheit | 7 | 9 | 6 | **8** |
| Redaktionelle Stärke | 9 | 6 | 7 | **9** |
| Visuelles Potenzial | 9 | 6 | 7 | **9** |
| Technische Umsetzbarkeit | 8 | 8 | 7 | **7** |
| Pflegebarkeit | 8 | 8 | 7 | **7** |
| Mobile UX | 7 | 8 | 6 | **8** |
| **Schnitt** | 7.7 | 7.4 | 6.9 | **8.4** |

**Entscheidung (Lead Architect): Variante D – Hybrid Hub.** Begründung: Nur die
Kombination aus redaktioneller Dramaturgie (Editorial), konkreter
Entscheidungsführung (Decision) und institutioneller Flagship-Verankerung
(Research) bedient alle vier Ziele gleichzeitig. Editorial liefert Wertigkeit &
Thought Leadership, Decision liefert Lead-Pfade & „das betrifft mich", Research
liefert institutionelle Glaubwürdigkeit.

## Navigation (Phase 2) – sichtbare Reiter
Bewusst nutzerwertig statt Fachabteilung:
`Aktuell · Eigenheim · Vermögen · Zukunft · Steuern · Research`
- Backend-Taxonomie bleibt (immobilien/kapitalmaerkte/vorsorge/steuern), aber die
  sichtbaren Labels sind kurz und bedürfnisorientiert.
- „Eigenheim" statt „Immobilien & Hypotheken", „Vermögen" statt „Kapitalmärkte &
  Anlegen", „Zukunft" statt „Vorsorge & Pensionierung".

## Iterationen

### Iteration 1 – Hybrid-Grundgerüst
- **Ziel:** Kachelwand/Archivgefühl ersetzen durch Hero + Decision + Editorial + Research.
- **Agenten:** Product Strategist, Editorial Director, UX/IA, Frontend.
- **Schwächen vorher:** (1) Hub erklärt sich nicht in 5 Sek; (2) keine
  Entscheidungslogik; (3) Flagships wie normale Artikel.
- **Umsetzung:** Neuer Hero mit Eyebrow + Doppel-CTA, Entscheidungs-Karussell,
  3 Editorial-Rubriken (Leitartikel + Begleitung + Flagship-Anker), Research-Band.
- **Geändert:** `build/build_hub_editorial.py` (komplett), `site/.../smzhub*`.

### Iteration 2 – Lead-Pfade & Conversion
- **Agenten:** Conversion Strategist, Product Strategist.
- **Schwäche:** Rubriken zeigten Inhalt, aber keine glaubwürdige nächste Handlung.
- **Umsetzung:** `rubric_footer` (ruhiges „Nächster Schritt"-Band mit
  kontextbezogenem Beratungs-CTA) unter jeder Rubrik; Decision-Karten mit
  „Einstieg →"; Hero-CTA „Entscheidung finden".

### Iteration 3 – Flagship-Verankerung & Institutionalität
- **Agenten:** Product Strategist, Visual Designer, Content Librarian.
- **Schwäche:** Research wirkte wie PDF-Lager.
- **Umsetzung:** Research-Band mit Cover, Frequenz + Ausgabenzahl, Beschreibung,
  aktueller Ausgabe; eigene Research-Seite + Serienseiten (aktuelle Ausgabe +
  Archiv + PDF). Flagships als Gold-Anker auch innerhalb der Rubriken.

### Iteration 4 – Content-Sauberkeit & Platzhalter
- **Agenten:** Content Librarian / Taxonomy Specialist.
- **Schwäche:** Dünne Rubriken (Steuern/Zukunft), Gefahr von Fremdfüllung.
- **Umsetzung:** Kanonische Rubrik je Beitrag (keine Themenvermischung);
  4 klar markierte Platzhalter (`build/smzhub-placeholders.json`) mit
  „In Vorbereitung"-Badge in dünnen Rubriken; Steuern als Kompaktmodul statt
  gestreckt; Guides als Pill-Reihe.

### Iteration 5 – UX/Mobile & Sticky-Navigation
- **Agenten:** UX/IA, Mobile UX Auditor, Frontend.
- **Schwäche:** Orientierung beim Scrollen; Karussell-Bug (Pfeile ausserhalb
  Carousel-Container nicht gebunden).
- **Umsetzung:** Sticky Reiterleiste; Karussell-JS an `.dc-sec` gebunden (Fix),
  responsive 1/2/4 sichtbar; eigene Rubrikseiten mit themenspezifischem
  Decision-Modul; mobile Stapelung statt endloser Kartenliste.

## Nutzerszenarien (Phase 9)

| Szenario | Ergebnis |
|---|---|
| 1 Erstbesucher (5-Sek-Test) | Hero + Eyebrow erklären Zweck; „Entscheidung finden" als Einstieg. ✔ |
| 2 Eigenheim-Interessent | Reiter „Eigenheim" + Rubrik + Decisions (Kaufen/Tragbarkeit) + Hypotheken-Radar. ✔ |
| 3 Hypothekarkunde | Decision „SARON oder Festhypothek?" + Hypotheken-Radar-Serie. ✔ |
| 4 Anleger | Reiter „Vermögen" + Investment Guide + Marktkommentare. ✔ |
| 5 Person 40+ Vorsorge | Decision „Vorsorgelücke mit 40+?" + Zukunft-Rubrik + Dossier-Platzhalter. ✔ |
| 6 Steueroptimierer | „Steuern"-Modul + Guide-Pills + Platzhalter-Guide. ✔ (dünn) |
| 7 Wiederkehrender Leser | Research-Band + Serienarchive zeigen neueste Ausgaben. ✔ |
| 8 smzh-Berater | Klare URLs je Rubrik/Serie zum Weiterleiten. ✔ |
| 9 Skeptiker | Reales Research, Quellen, ruhige Optik → substanziell. ✔ |
| 10 Mobile | Sticky-Reiter + gestapelte Module + 1-up-Karussell statt Endlosliste. ✔ |

## Scores (1–10) – vorher (Karussell-Stand 782ac2a) → nachher (Hybrid Hub)

| Dimension | Vorher | Nachher |
|---|--:|--:|
| Thought Leadership | 6 | 8 |
| Lead Generation | 6 | 8 |
| Institutional Appearance | 6 | 9 |
| Entertainment & Problem Solving | 7 | 8 |
| Orientierung in 5 Sekunden | 6 | 8 |
| Rubrikenlogik | 7 | 9 |
| Content-Zuordnung | 8 | 9 |
| Redaktionelle Dramaturgie | 6 | 8 |
| Visuelle Wertigkeit | 7 | 8 |
| Flagship-Verankerung | 5 | 9 |
| Mobile UX | 7 | 8 |
| Pflegebarkeit | 8 | 8 |
| Vermeidung Kachelwand/Archiv | 7 | 9 |

**Kein zentraler Score < 7.** Schwächster Bereich Entertainment/Visuell (8) –
bewusst ruhig gehalten (institutionell statt verspielt).

## Offene Schwächen (Top 5)
1. Blogartikel-/Detailtemplate (Phase 7) noch nicht umgebaut – Key-Takeaways,
   „Was bedeutet das für mich?", Related/CTA fehlen auf Artikelebene.
2. Steuern- und Zukunft-Rubrik inhaltlich dünn – mehr echte Evergreens nötig
   (aktuell teils Platzhalter).
3. Decision-Platzhalter sind Evergreen-Links, noch keine eigenständigen
   Decision-Detailseiten.
4. Kein echter Rechner/Tool (nur Platzhalter) – starker Lead-Hebel offen.
5. Dossier-Storylines noch als Platzhalter, nicht als kuratierte Mehrteiler.

## Nächster sinnvoller Schritt
Artikel-Detailtemplate aufwerten (Hero, Lesedauer, Key-Takeaways, „Was bedeutet
das für mich?", Related-Serie/Dossier, kontextbezogener CTA) – grösster offener
Lead- und Thought-Leadership-Hebel.
