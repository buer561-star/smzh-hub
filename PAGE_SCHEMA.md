# PAGE_SCHEMA.md — Informationsarchitektur smzhHub

> **Quelle der Wahrheit für die Seitenstruktur des smzhHub.**
> Gepflegt vom Product Architect. Definiert Block-Reihenfolge, Sektionsfunktion, Nutzerpfade und CTA-Logik je Hub-Seite.
> Dieses Dokument beschreibt **Struktur und Logik**, nicht Gestaltung (→ `design-system`), nicht Texte (→ `editorial`), nicht Code (→ `builder`).
> Verbindlich: Wer eine Hub-Seite (um-)baut, hält sich an die hier festgelegte Block-Reihenfolge und Pflicht-Elemente.

---

## 0. Zweck des Dokuments

- **Was es ist:** Das persistente Schema aller smzhHub-Seiten — Startseite, Themenwelten (Subpages) und die geplante Erweiterung um Flagship-Research-Anker.
- **Wozu:** Damit Build-Skripte (`build/build_hub_v5.py`), Design und Redaktion gegen *eine* verbindliche Struktur arbeiten. Reihenfolge der Blöcke, Funktion jeder Sektion und CTA-Ziele sind hier festgehalten, nicht in den Skripten verstreut.
- **Geltungsbereich:** smzhHub-Seiten unter `site/smzh.ch/de/smzhub*`. Ratgeber-Artikel (`ratgeber-*`) und Serien-Seiten (`smzhub-serie-*`) sind eigene Templates und werden hier nur als Ziele/Quellen referenziert.
- **Status-Konvention:** `VERBINDLICH` = umzusetzen in dieser Iteration · `MUSTER` = wiederverwendbares Schema für künftige Seiten · `OUT OF SCOPE` = bewusst auf Folge-Iteration verschoben.
- **Pflege:** Bei jeder Struktur-Entscheidung wird der betroffene Eintrag aktualisiert. Block-Reihenfolge ist normativ; konkrete Pfade/Slugs sind dokumentiert, aber im Build die Quelle der Implementierung.

### Bestätigter Ist-Zustand (Basis dieser Iteration)

- **V5-System** (`build/build_hub_v5.py`) rendert heute: `smzhub` (Startseite, voll), `smzhub-eigenheim` (voll, via `eigenheim_inner`), `smzhub-immobilienanlagen` und `smzhub-horizon` (schlanke Themenwelt-Stubs via `category_inner` → `v5-phead`-Hero + `v5-wrap`-Body + Back-Link).
- **Ist-Block-Reihenfolge `smzhub-eigenheim` (V5, vor dieser Iteration):** `v5-phead-Hero (1 CTA) → eigenheim_flagship() [Radar + Outlook als gleichwertiges 2-Spalten-Kartenpaar v5-fa-grid] → eigenheim_decisions() → eigenheim_tools() → eigenheim_depth() (Grundlagen + Dossier) → eigenheim_cta() (Schluss) → Back-Link`.
- **Editorial-System** (`build/build_hub_editorial.py`) rendert heute noch `smzhub-vermoegen` und `smzhub-zukunft` via `theme_inner(...)`. Diese sind **nicht** auf V5 migriert (siehe §4.4, Backlog §5.4).
- **Reale Inhalte bestätigt** (alle Seiten existieren): 10 × `ratgeber-*`; `smzhub-serie-hypotheken-radar` (monatlich); `smzhub-serie-immobilien-outlook` (quartalsweise); `smzhub-dossier-eigenheim`. Datenquelle für Serien-Ausgaben inkl. PDFs: `build/smzhhub-content.json` (`series_items(key)` → sortiert nach Datum absteigend; Feld `pdfs` mit Dateinamen, `_DE_`-Marker für deutsche Ausgabe).

### Bestätigte Entscheidungen dieser Iteration (Auftraggeber, nicht zu diskutieren)

1. **Zwei neue Flagship-Landingpages** (eigene Slugs, eigene Beratungspfade): `/de/smzhub-hypotheken-radar/` und `/de/smzhub-immobilien-outlook/`. Lösen den §1.7-/Backlog-Punkt „eigenständige Flagship-LP" auf. Volle Schemata → §6 und §7. Die bestehenden Serien-Seiten `smzhub-serie-hypotheken-radar` / `smzhub-serie-immobilien-outlook` **bleiben** und sind das Archiv-Ziel der LPs.
2. **Routing-Änderung:** Der Flagship-Anker auf `smzhub-eigenheim` zeigt künftig auf die jeweilige neue LP (statt direkt auf die Serien-Seite). Verankert in §1.6 und §2.1.
3. **Subpage-Restruktur `smzhub-eigenheim`:** Die zwei Flagships werden vom gleichwertigen 2-Spalten-Kartenpaar zu **zwei vollen Vollbreiten-Einzel-Segmenten mit rechtem Kontext-Rail** umgebaut (Muster Home-`rubric` `v5-rub-grid` + Side-Rail). Outlook zusätzlich als High-End-Publikation hervorgehoben. Aktualisiert §1.4 und §3.
4. **Neue Inhalts-Sektionen auf `smzhub-eigenheim`:** Ratgeber-Sektion, Rechner-/Tools-Sektion (kuratierter Verweis, kein Inline-Rechner), Stories-Sektion (Fallbeispiele/Use-Cases, keine erfundenen Personen) und „Wie haben sich die Zinsen entwickelt?"-Sektion (echter Daten-Chart). Finale Block-Reihenfolge → §1.4.
5. **Blog-CTA-Regel:** In redaktionellen Lese-/Blog-Rubriken der Startseite und der 5 Funnel-Themenwelten **keine** Conversion-CTAs; Blog-Teaser sind reine Lese-Links. Globaler Abschnitt → §8.

---

## 1. SCHEMA: `smzhub-eigenheim` (Eigenheim & Hypothek) — V5 — `VERBINDLICH`

**Slug/Pfad:** `site/smzh.ch/de/smzhub-eigenheim/`
**Build:** `build/build_hub_v5.py` (neue Funktion, Muster `category_inner` erweitert um Flagship-Anker; **Ablösung** von `theme_inner('eigenheim')`)
**Typ:** Themenwelt-Subpage mit Research-Schwerpunkt (nicht reiner Stub)

### 1.1 Ziel der Seite
Eigenheim-Interessierte und Eigentümer von der Frage in einen qualifizierten Beratungspfad führen — und dabei über zwei wiederkehrende, prominent verankerte Research-Formate (Hypotheken-Radar, Immobilien-Outlook) Glaubwürdigkeit und Wiederkehr-Anlass aufbauen. Lead-Generierung mit Research als Vertrauensanker.

### 1.2 Zielgruppe
Schweizer Privatpersonen rund um Wohneigentum: Ersterwerbende (Kauf, Eigenkapital, Tragbarkeit), bestehende Eigentümer vor Hypothekenverlängerung (SARON/Fest), Eigentümer mit freiem Kapital (amortisieren vs. investieren), Marktbeobachter (kaufen oder warten).

### 1.3 Primärer Nutzerpfad
Hero (Verortung „Eigenheim & Hypothek") → **Research-Anker wählen** (Radar = Finanzierung/Zinsen *oder* Outlook = Markt/Kaufentscheid) → aktuellste Ausgabe lesen ODER über Entscheidungspfad zur konkreten Frage → vertiefen (Ratgeber/Grundlagen) → **Beratungs-CTA** (kontextspezifisch: Hypothek prüfen / Finanzierung besprechen / Eigenheimstrategie). Sekundärpfad: direkt über Entscheidungspfade (Decision-Cards) in den passenden Ratgeber.

### 1.4 Seitenstruktur mit Sections — VERBINDLICHE Block-Reihenfolge (nach Entscheidung 2–4)

| # | Block | Status | Quelle/Ziel |
|---|-------|--------|-------------|
| 1 | **Hero (Themenwelt-Kopf)** | VERBINDLICH | `v5-phead`: Eyebrow „smzhHub · Themenwelt", H1 „Eigenheim & Hypothek", Einordnungs-Lead. Genau **ein** Hero-CTA (kontextarm, Richtung Beratung). |
| 2 | **Flagship-Segment A — Hypotheken-Radar** (Vollbreite + rechtes Kontext-Rail) | VERBINDLICH | Eigenständiges Vollbreiten-Segment nach Muster §3 (nicht mehr halbe Karte). **Haupt-CTA des Segments routet auf die neue LP** `/de/smzhub-hypotheken-radar/`. Rail-Inhalte → §1.4a. |
| 3 | **Flagship-Segment B — Immobilien-Outlook** (Vollbreite + rechtes Kontext-Rail, zusätzlich als High-End-Publikation hervorgehoben) | VERBINDLICH | Eigenständiges Vollbreiten-Segment nach Muster §3. **Haupt-CTA des Segments routet auf die neue LP** `/de/smzhub-immobilien-outlook/`. Rail-Inhalte → §1.4a. |
| 4 | **„Wie haben sich die Zinsen entwickelt?" — Zins-Zeitreihe (Daten-Chart)** | VERBINDLICH (NEU, Entsch. 4d) | Echter Daten-Chart einer Zeitreihe (SNB-Leitzins / SARON / Festhypothek). Faktischer Anker, der die beiden Flagship-Segmente inhaltlich verklammert (Zins = gemeinsame Achse von Radar & Outlook). Kein Conversion-Element — neutrale Datensektion. |
| 5 | **Entscheidungspfade (nach Nutzerproblem)** | VERBINDLICH | Decision-Cards, **nur Rubrik Eigenheim/Hypothek**. Aus `EIGENHEIM_DECISIONS`, auf reale `ratgeber-*` geroutet (§1.6, §2.2). |
| 6 | **Ratgeber-Sektion** | VERBINDLICH (NEU, Entsch. 4a) | Kuratierte Liste der Eigenheim-/Hypothek-`ratgeber-*` als Lese-Einstiege (SEO-/Lead-Gen-Artikel). Reine Lese-Links. Löst §1.7-Punkt „Beitragsstrom" konstruktiv: nicht voller Artikel-Stream, sondern fokussierte Ratgeber-Auswahl. |
| 7 | **Stories — Fallbeispiele / Use-Cases** | VERBINDLICH (NEU, Entsch. 4c) | Typische Eigenheim-Situationen als anonymisierte Use-Cases (z. B. „Erstkauf mit knappem Eigenkapital", „Verlängerung bei auslaufender Festhypothek", „freies Kapital: amortisieren oder anlegen"). **Keine erfundenen Einzelpersonen / keine fiktiven Namen** — nur Situations-Muster. Jede Story verweist in den passenden Ratgeber/das passende Flagship. |
| 8 | **Rechner & Tools (kuratierte Sektion)** | VERBINDLICH (NEU/erweitert, Entsch. 4b) | Eigenständige, deklarierte Tools-Sektion mit Verweis(en) auf bestehende Rechner (Tragbarkeit/Immobilienbewertung). **Kein** neu gebauter interaktiver Inline-Rechner (→ Backlog §5.2). Als deklarierte Tools-Sektion **von der Blog-CTA-Regel ausgenommen** (§8). |
| 9 | **Vertiefende Inhalte (Grundlagen + Dossier)** | VERBINDLICH | (a) Grundlagen/Evergreens (`EIGENHEIM_EVERGREEN`), (b) Dossier-Verweis „Eigenheim finanzieren" → `smzhub-dossier-eigenheim`. |
| 10 | **Beratungs-/Schluss-CTA** | VERBINDLICH | Themenweiter Abschluss-CTA Richtung 360°-Check-up / Termin. |
| — | Back-Link „Zurück zum smzhHub" | VERBINDLICH | Wie V5-`category_inner`. |

> **Reihenfolge ist normativ.** Die zwei Flagship-Segmente stehen **direkt nach dem Hero** (Position 2 + 3) — nicht mehr als halbes Karten-Paar, sondern als zwei **eigenständige Vollbreiten-Segmente mit rechtem Kontext-Rail**. Der Zins-Chart (4) folgt unmittelbar als faktische Klammer. Erst danach kommen Entscheidungspfade, Ratgeber, Stories, Tools, Vertiefung, Schluss-CTA.

### 1.4a Rail-Inhalte je Flagship-Segment (Entscheidung 3) — VERBINDLICH

> Muster: wie Home-`rubric` (`v5-rub-grid` + Side-Rail). Links das breite Flagship-Segment (Format, aktuelle Ausgabe, Beschreibung, Segment-CTA auf LP), rechts ein Kontext-Rail mit realen, thematisch passenden Inhalten.

- **Rail Segment A (Hypotheken-Radar / Finanzierung-nah):**
  - Reale Beiträge aus `EIGENHEIM_DECISIONS` (Finanzierungs-Cluster): `ratgeber-saron-oder-festhypothek`, `ratgeber-tragbarkeit-hypothek`, `ratgeber-amortisieren-oder-investieren` — als reine Lese-Links.
  - Tools-Slot: Verweis auf Tragbarkeits-/Bewertungsrechner (`EIGENHEIM_TOOL`, `/de/immobilienbewertung-rechner/`). Dieser Tools-Slot ist ein deklariertes Rechner-Element, kein Blog-CTA (§8-Ausnahme).
- **Rail Segment B (Immobilien-Outlook / Markt & Kaufentscheid):**
  - Reale Beiträge aus `EIGENHEIM_DECISIONS` (Markt-Cluster) + `EIGENHEIM_EVERGREEN`: `ratgeber-eigenheim-kaufen-oder-warten`, `ratgeber-eigenkapital-eigenheim`, dazu Evergreen `Wie kaufe ich eine Immobilie?` / `Wohneigentumsförderung` — reine Lese-Links.
  - Tools-Slot: Verweis auf Immobilienbewertungs-/Marktwert-Pfad (deklariertes Rechner-Element, §8-Ausnahme).
- **Reine Lese-Links im Rail** tragen ausschliesslich „Beitrag lesen"-Charakter; **kein** Beratungs-CTA im Rail. Der einzige Conversion-Punkt je Segment ist der **eine** Segment-CTA (Richtung LP), siehe §1.6.

### 1.5 Funktion jeder Section
1. **Hero** — Verortung und Erwartung setzen: „Dies ist der Eigenheim-Bereich." Kein Content-Wettbewerb mit den Segmenten; ein einziger ruhiger CTA.
2. **Hypotheken-Radar (Segment + Rail)** — Finanzierungs-/Zinsseite. Macht das monatliche Format greifbar, zeigt im Rail die passenden Entscheidungs-Ratgeber + Rechner und leitet über **einen** Segment-CTA auf die **Radar-LP** (dort der volle Beratungspfad).
3. **Immobilien-Outlook (Segment + Rail, High-End)** — Marktseite, visuell/inhaltlich als gehobene Publikation positioniert. Rail mit Markt-Ratgebern + Rechner; **ein** Segment-CTA auf die **Outlook-LP**.
4. **Zins-Zeitreihe** — Liefert den faktischen Beleg hinter beiden Formaten (warum Radar/Outlook überhaupt relevant sind). Schafft Research-Glaubwürdigkeit ohne Verkaufsdruck; neutraler Daten-Block.
5. **Entscheidungspfade** — Übersetzt Lebensfragen in konkrete Einstiege; fängt Nutzer ab, die nicht über die Flagships einsteigen, und routet sie in den passenden Ratgeber.
6. **Ratgeber-Sektion** — Bündelt die Eigenheim-/Hypothek-Ratgeber als Lese-/SEO-Pfad; bedient Informationssuchende, die noch nicht beraten werden wollen.
7. **Stories** — Macht abstrakte Entscheidungen anhand typischer Situationen anschlussfähig („so jemand wie ich"); Brücke zwischen Information und Beratungsbereitschaft. Keine erfundenen Personen.
8. **Rechner & Tools** — Niedrigschwelliger Selbst-Einstieg (Tragbarkeit/Bewertung); deklarierte Tools-Sektion, Brücke von „informieren" zu „rechnen" zu „beraten lassen".
9. **Vertiefende Inhalte** — Bedient Grundlagenbedarf und gibt dem Dossier (Storyline) einen Platz, ohne die Flagships zu verdrängen.
10. **Beratungs-CTA** — Sammelt die Restnachfrage themenweit; letzter Konversionspunkt.

### 1.6 CTA-Logik
- **Hero-CTA (1×):** ruhiger Primär-CTA Richtung Beratung/Check-up (z. B. „Finanzierung besprechen"). Bewusst nur einer, um die Segmente nicht zu überstrahlen.
- **Radar-Segment-CTA (Pflicht, 1 CTA):** **routet neu auf die LP** `/de/smzhub-hypotheken-radar/` (statt direkt auf die Serien-Seite — Routing-Änderung Entscheidung 2). Beschriftung Richtung **Finanzierung/Radar** (z. B. „Zum Hypotheken-Radar"). Der volle Beratungspfad (Beratungs-CTA Richtung Finanzierung) liegt **auf der LP**. Sekundäraktionen im Segment (nicht-CTA): „Aktuelle Ausgabe lesen". Das Archiv („Alle Ausgaben") erreicht der Nutzer über die LP.
- **Outlook-Segment-CTA (Pflicht, 1 CTA):** **routet neu auf die LP** `/de/smzhub-immobilien-outlook/`. Beschriftung Richtung **Markt/Outlook** (z. B. „Zum Immobilien-Outlook"). Voller Beratungspfad (Richtung Eigenheimstrategie/Kaufentscheid) auf der LP. Sekundär: „Aktuelle Ausgabe lesen".
- **Zins-Chart-Sektion:** **kein CTA** — neutrale Datensektion.
- **Decision-Cards:** jede Karte verlinkt in **einen realen Ratgeber** (kein Beratungs-CTA — Lese-/SEO-Pfad). Routing:
  - Hypothek/Finanzierung-nah → `ratgeber-saron-oder-festhypothek`, `ratgeber-tragbarkeit-hypothek`, `ratgeber-amortisieren-oder-investieren`
  - Markt/Kaufentscheid → `ratgeber-eigenheim-kaufen-oder-warten`, `ratgeber-eigenkapital-eigenheim`
- **Ratgeber-Sektion:** reine Lese-Links („Beitrag lesen") in die `ratgeber-*`. **Kein** Conversion-CTA (Blog-CTA-Regel §8).
- **Stories-Sektion:** jede Story verlinkt als Lese-Link in den passenden Ratgeber / das passende Flagship. **Kein** eigener Beratungs-CTA je Story (Blog-CTA-Regel §8); die Konversion läuft über den Schluss-CTA.
- **Rechner & Tools (deklarierte Sektion):** ein/mehrere Aktions-Link(s) auf bestehende Rechner (Tragbarkeit/Bewertung), low-commitment. **Ausdrücklich erlaubt** als deklarierte Tools-Sektion (§8-Ausnahme), kein „in den Blog geschmuggelter" CTA.
- **Schluss-CTA:** themenweiter Beratungs-/360°-CTA (höchstes Commitment), terminorientiert.
- **CTA-Hierarchie:** pro Flagship-Segment **genau ein** CTA (auf die LP). Nie zwei konkurrierende Primär-CTAs in einem Segment. Innerhalb der Lese-Rubriken (Ratgeber, Stories, Rail-Lese-Links) **keine** Conversion-CTAs (§8).

### 1.7 Was bewusst weggelassen wird (diese Iteration)
- **Neu gebauter interaktiver Inline-Rechner** auf der Eigenheim-Seite (mehrteilig, mit Eingabe/Ergebnis). Diese Iteration: kuratierte Tools-Sektion mit Verweis auf bestehende Rechner (§1.4 Block 8). → **Backlog §5.2.**
- **Bidirektionale Ratgeber ↔ Subpage-Verlinkung** (Rückverlinkung aus den `ratgeber-*` auf diese Subpage / Segmente). Diese Iteration einseitig: Subpage → Ratgeber. → **Backlog §5.3.**
- **Investment-Guide-Anker** — gehört thematisch zu Anlagen, nicht Eigenheim; hier nicht aufgenommen.
- **Vollständiges Beitrags-/Artikelarchiv** der Rubrik (Editorial-„Weitere Beiträge"/„In Vorbereitung"). Die fokussierte Ratgeber-Sektion (§1.4 Block 6) ersetzt den losen Beitragsstrom bewusst.
- **Sticky Rubriken-Themebar** (Editorial-`themebar`) — im V5-Subpage-Muster nicht vorgesehen.

> **Hinweis (aufgelöst gegenüber Vor-Iteration):** Die früher hier als OUT-OF-SCOPE geführten Punkte „eigenständige Flagship-Landingpages" und „dedizierter Rechner-Block" sind durch die Entscheidungen 1 und 4 teilweise aufgelöst: die **LPs werden gebaut** (§6/§7), die **Tools-Sektion wird deklariert** gebaut (Verweis-Variante). Der voll-interaktive Rechner bleibt Backlog (§5.2).

### 1.8 Migrationszuordnung Editorial → V5 (was bleibt, was fällt)

| Editorial-Block (Ist) | Entscheidung | V5-Ziel (neue Block-Nr. §1.4) |
|---|---|---|
| `decision_carousel` (DECISIONS, Rubrik immobilien) | **ÜBERNEHMEN**, neu auf reale `ratgeber-*` geroutet | Block 5 |
| `research_band` (Hypotheken-Radar + Immobilien-Outlook) | **ERSETZEN/AUFWERTEN** durch zwei Flagship-**Vollbreiten-Segmente** (Routing → LP) | Block 2 + 3 |
| Dossier „Roter Faden" (`smzhub-dossier-eigenheim`) | **ÜBERNEHMEN** als Verweis | Block 9b |
| `guides_band` / `EVERGREEN['immobilien']` | **ÜBERNEHMEN** (schlanker) | Block 9a |
| „Im Fokus" (`rubric_body`, Leitartikel + Begleitung) | **WEGFALL** (nachrangig; Ratgeber-/Stories-Sektion treten an die Stelle) | — |
| „Weitere Beiträge" / „In Vorbereitung" | **WEGFALL** (ersetzt durch fokussierte Ratgeber-Sektion Block 6) | — |
| Editorial-Hero + sticky `themebar` | **ERSETZEN** durch V5-`v5-phead`-Hero | Block 1 |
| Schluss-CTA | **ÜBERNEHMEN** (V5-Schluss-CTA) | Block 10 |
| *(neu, kein Editorial-Pendant)* Zins-Zeitreihe-Chart | **NEU** (Entsch. 4d) | Block 4 |
| *(neu)* Ratgeber-Sektion · Stories · Tools-Sektion · Flagship-Rails | **NEU** (Entsch. 3+4) | Block 6 · 7 · 8 · 1.4a |

---

## 2. Reale Inhalts-Zuordnung (Eigenheim) — `VERBINDLICH`

### 2.1 Flagship-Quellen & Routing (nach Entscheidung 1+2)
| Format | Serie (Slug, Archiv) | Cadence | Aktuellste Ausgabe | Neue LP (Slug) | Eigenheim-Segment-CTA → |
|---|---|---|---|---|---|
| Hypotheken-Radar | `smzhub-serie-hypotheken-radar` | monatlich | `series_items('hypothekenradar')[0]` (neuestes Datum, build-dynamisch) | `/de/smzhub-hypotheken-radar/` | **LP** (nicht mehr direkt Serie) |
| Immobilien-Outlook | `smzhub-serie-immobilien-outlook` | quartalsweise | `series_items('immobilien-outlook')[0]` | `/de/smzhub-immobilien-outlook/` | **LP** (nicht mehr direkt Serie) |

> **Routing-Kette (Entscheidung 2):** Eigenheim-Segment-CTA → **LP** → (LP-Archiv-Block) → **Serien-Seite** `smzhub-serie-*`. Die Serien-Seite bleibt das finale Archiv-Ziel, ist aber nicht mehr das direkte Ziel des Eigenheim-Ankers.
> Aktuellste Ausgabe wird überall **dynamisch** aus `series_items(key)[0]` gezogen (neuestes Datum), nicht hartkodiert. PDF der Ausgabe: Feld `pdfs` (bevorzugt Datei mit `_DE_`-Marker).

### 2.2 Ratgeber-Zuordnung (Decision-Cards & vertiefende Inhalte)
| Thematischer Anker | Ratgeber (real) | Rolle |
|---|---|---|
| **Radar** (Finanzierung/Zinsen) | `ratgeber-saron-oder-festhypothek` | Kern-Entscheidung Hypothekenstrategie |
| **Radar** | `ratgeber-tragbarkeit-hypothek` | Tragbarkeit (Bank-Sicht) |
| **Radar** (hypothekennah) | `ratgeber-amortisieren-oder-investieren` | Kapitalverwendung bei Hypothek |
| **Outlook** (Markt/Kaufentscheid) | `ratgeber-eigenheim-kaufen-oder-warten` | Timing-/Marktentscheid |
| **Outlook** | `ratgeber-eigenkapital-eigenheim` | Eigenkapital für den Kauf |

### 2.3 Grundlagen/Evergreen (Block 9a) — aus `EIGENHEIM_EVERGREEN`
`Tragbarkeit optimieren` · `Hypothekenarten im Vergleich` · `Wie kaufe ich eine Immobilie?` · `Wohneigentumsförderung` (bestehende Evergreen-Seiten). Auch als Lese-Links in den Flagship-Rails verwendbar (§1.4a, Markt-Cluster).

### 2.4 Dossier (Block 9b)
`smzhub-dossier-eigenheim` — „Eigenheim finanzieren" (Storyline), als Verweis-Element.

### 2.5 Stories — reale Situations-Muster (Block 7) — `VERBINDLICH`
Anonymisierte Eigenheim-Situationen entlang typischer Entscheidungen, **keine erfundenen Einzelpersonen**. Mindest-Set (je Story → Lese-Link in passenden Ratgeber/Flagship):
- „Erstkauf mit knappem Eigenkapital" → `ratgeber-eigenkapital-eigenheim` / Outlook
- „Festhypothek läuft aus — verlängern oder wechseln?" → `ratgeber-saron-oder-festhypothek` / Radar
- „Reicht das Einkommen für die Bank?" → `ratgeber-tragbarkeit-hypothek` / Radar
- „Freies Kapital: amortisieren oder anlegen?" → `ratgeber-amortisieren-oder-investieren` / Radar
- „Kaufen oder noch warten?" → `ratgeber-eigenheim-kaufen-oder-warten` / Outlook

### 2.6 Zins-Zeitreihe (Block 4) — `VERBINDLICH`
Echte Zeitreihe als Daten-Chart: SNB-Leitzins / SARON / repräsentative Festhypothek (z. B. 10 Jahre). Faktischer Block, kein CTA. Datenquelle/Aktualisierung → Backlog §5.6 (Abhängigkeit, kein IA-Thema).

---

## 3. MUSTER: „Flagship-Research-Segment" — `MUSTER` (wiederverwendbar)

> Wiederverwendbares Sektions-Muster für jede Themenwelt mit wiederkehrendem Research-Format
> (Eigenheim heute; künftig z. B. Vorsorge, Steuern, Anlagen). Definiert die **Pflicht-Elemente** eines Flagship-Segments.
> **Geändert mit Entscheidung 3:** Das Muster ist **nicht mehr** „gleichwertiges Karten-Paar nebeneinander", sondern **„eigenständiges Vollbreiten-Segment je Flagship mit rechtem Kontext-Rail"** (Aufbau analog Home-`rubric` / `v5-rub-grid` + Side-Rail).

### 3.1 Platzierung & Layout-Logik
- **Immer direkt nach dem Hero**, vor Entscheidungspfaden/Tools.
- Bei **zwei** Flagship-Formaten je Themenwelt: **zwei aufeinanderfolgende Vollbreiten-Segmente** (je Flagship eines), nicht ein 2-Spalten-Kartenpaar. Jedes Segment besteht aus **Hauptspalte (Flagship)** + **rechtem Kontext-Rail** (reale Beiträge + Tools-Slot, §1.4a).
- Reihenfolge der Segmente folgt der Nutzerlogik (Eigenheim: Radar = Finanzierung zuerst, Outlook = Markt danach); eine der Publikationen darf als High-End-Format zusätzlich hervorgehoben werden (Eigenheim: Outlook).
- Bei **einem** Format: ein Vollbreiten-Segment, gleiche Pflicht-Elemente.

### 3.2 Pflicht-Elemente je Segment (alle obligatorisch)
1. **Format-Name** (z. B. „Hypotheken-Radar").
2. **Cadence-Label** (monatlich / quartalsweise) — sichtbar, da Wiederkehr-Versprechen.
3. **Aktuellste Ausgabe**, verlinkt (Titel + Datum; build-dynamisch `series_items(key)[0]`).
4. **Kontext-Rail** rechts: reale, thematisch passende Lese-Links (aus Decisions/Evergreen) + ein Tools-Slot. Reine Lese-Links, kein Beratungs-CTA im Rail (§1.4a).
5. **Genau ein Segment-CTA**, der auf die zugehörige **Flagship-LP** routet (§3.3). Der volle Beratungspfad liegt auf der LP, nicht im Segment.

> Hinweis: Der **Archiv-Einstieg** liegt im Eigenheim-Subpage-Muster **auf der LP** (nicht mehr im Segment), da das Segment auf die LP routet und die LP den Archiv-Block trägt (§6/§7). In Themenwelten **ohne** eigene LP zeigt das Segment direkt auf die Serien-Seite (Fallback-Muster).

### 3.3 CTA-/Routing-Richtung je Format-Typ
| Format-Typ | Segment-CTA routet auf | LP-Beratungspfad Richtung |
|---|---|---|
| Zins-/Finanzierungs-Radar (Hypotheken-Radar) | LP `/de/smzhub-hypotheken-radar/` | „Hypothek prüfen" / „Finanzierung besprechen" / „Verlängerung planen" |
| Markt-/Strategie-Outlook (Immobilien-Outlook) | LP `/de/smzhub-immobilien-outlook/` | „Eigenheimstrategie besprechen" / „Kaufentscheid besprechen" |
| (künftig) Vorsorge-Format | eigene LP oder Serie | „Vorsorge analysieren" / „Pensionierung planen" |
| (künftig) Steuer-Format | eigene LP oder Serie | „Steuern optimieren" / „Steuersituation besprechen" |

### 3.4 Regeln
- **Ein** CTA pro Segment — keine konkurrierenden Primär-CTAs; Rail-Links sind reine Lese-Links.
- Segment routet auf die **Flagship-LP** (Entscheidung 2); die LP trägt den vollen Beratungspfad + Archiv. Ohne LP (andere Themenwelten) zeigt das Segment direkt auf die Serien-Seite.
- Cadence-Label und „aktuellste Ausgabe" sind **nicht optional** — sie tragen das Wiederkehr- und Aktualitäts-Versprechen.
- Reihenfolge der Pflicht-Elemente innerhalb des Segments ist logisch (Name → Cadence → aktuelle Ausgabe → Rail → Segment-CTA); konkrete visuelle Anordnung entscheidet `design-system`.

### 3.5 Anwendungsregel für künftige Subpages
Eine neue Themenwelt-Subpage übernimmt das Block-Raster aus §1.4 (Hero → Flagship-Segment(e) → ggf. Daten-Sektion → Entscheidungspfade → Ratgeber → Stories → Tools → Vertiefung → CTA). Hat sie kein wiederkehrendes Research-Format, entfällt das Flagship-Segment ersatzlos und sie bleibt ein V5-`category_inner`-Stub (wie heute `smzhub-horizon`).

---

## 4. Übrige Hub-Seiten — Referenz

> Nur referenziert/abgegrenzt. Volle Schemata folgen in eigenen Iterationen.

### 4.1 `smzhub` (Startseite) — `BESTEHEND`
**Pfad:** `de/smzhub/` · **Build:** `build_hub_v5.py` (`home_inner`).
Block-Reihenfolge (Ist): Hero+Karussell → Themenwelten-Funnel (5 Kacheln) → Entscheidungen (`DECISIONS`, alle Rubriken) → 3 Rubrik-Sektionen (Eigenheim/Vermögen/Vorsorge, je Lead + Sub-Links + Tool-Slot) → Research-Band (3 Serien) → Schluss-CTA. **Bleibt** Einstiegs-Hub und verlinkt auf alle Themenwelten inkl. `smzhub-eigenheim`.

### 4.2 `smzhub-immobilienanlagen` — `BESTEHEND (Stub)`
**Pfad:** `de/smzhub-immobilienanlagen/` · **Build:** `build_hub_v5.py` (`immobilienanlagen_inner` → `category_inner`).
Heute: Lead-Text + Liste „Relevante Einschätzungen" (inkl. Verweis Immobilien-Outlook) + Back-Link. Kandidat, später auf das Flagship-Anker-Muster (§3) gehoben zu werden (Outlook teilbar mit Eigenheim).

### 4.3 `smzhub-horizon` — `BESTEHEND (Stub)`
**Pfad:** `de/smzhub-horizon/` · **Build:** `build_hub_v5.py` (`horizon_inner` → `category_inner`).
Heute: Lead + Hinweis „im Aufbau" + Verweis auf Research. Bleibt Stub bis eigene Inhalte vorliegen.

### 4.4 `smzhub-vermoegen` · `smzhub-zukunft` — `EDITORIAL (noch nicht migriert)`
**Pfade:** `de/smzhub-vermoegen/`, `de/smzhub-zukunft/` · **Build:** aktuell `build_hub_editorial.py` (`theme_inner`).
Noch auf dem Editorial-System (V5-`rubric`-Tool-Slots und `v5-season`-Block existieren dort nicht in dieser Form). **Die Blog-CTA-Regel (§8) gilt auch für diese Seiten**, ihre **technische Umsetzung erfolgt aber erst mit der V5-Migration** (Backlog §5.4) — in dieser Iteration **kein Code-Eingriff** auf `smzhub-vermoegen`/`smzhub-zukunft`. Eigenheim ist der V5-Pilot; Migration + ggf. Flagship-Segment-Muster (§3) in Folge-Iterationen.

### 4.5 Research & Serien — `BESTEHEND` (Ziele der LPs/Segmente)
- `de/smzhub-research/` — Übersicht der Flagship-Formate.
- `de/smzhub-serie-hypotheken-radar/` — Archiv-Ziel Radar (jetzt erreicht über die Radar-LP §6).
- `de/smzhub-serie-immobilien-outlook/` — Archiv-Ziel Outlook (jetzt erreicht über die Outlook-LP §7).
- `de/smzhub-serie-investment-guide/` — Anlagen-Format (nicht Eigenheim).
- `de/smzhub-dossier-eigenheim/` — Storyline „Eigenheim finanzieren" (Block 9b).

---

## 5. Backlog / Folge-Iterationen

> Aktualisiert nach Entscheidungen 1–5. Erledigte Punkte gestrichen; offene neu nummeriert (Nummern sind referenzstabil).

1. ~~Flagship-Landingpages mit eigenen, vollen Beratungspfaden~~ → **erledigt mit Entscheidung 1** (Schemata §6/§7).
2. **Dedizierter, interaktiver Tragbarkeits-/Hypothekenrechner** (Eingabe → Ergebnis, mehrteilig) statt kuratiertem Verweis. Betrifft die Eigenheim-Tools-Sektion (§1.4 Block 8) und ggf. die LP-Tools.
3. **Bidirektionale Verlinkung** Ratgeber ↔ Subpage/Flagship-Segment/LP (Rückverlinkung aus `ratgeber-*`).
4. **V5-Migration** der übrigen Editorial-Subpages (`smzhub-vermoegen`, `smzhub-zukunft`) — **inklusive technischer Umsetzung der Blog-CTA-Regel (§8) dort** (in dieser Iteration bewusst kein Code-Eingriff, vgl. §4.4). Dabei Prüfung Flagship-Segment-Muster je Themenwelt.
5. **Immobilienanlagen** vom Stub auf das Flagship-Segment-Muster (§3) heben (Outlook geteilt mit Eigenheim, ggf. via Outlook-LP).
6. **Datenpflege Zins-Zeitreihe** (§1.4 Block 4): Quelle/Aktualisierungsweg der SNB-Leitzins-/SARON-/Festhypothek-Reihe definieren (Verantwortung Datenquelle, kein IA-Thema — hier nur als Abhängigkeit notiert).

---

## 6. SCHEMA: `smzhub-hypotheken-radar` (Flagship-LP Hypotheken-Radar) — V5 — `VERBINDLICH`

**Slug/Pfad:** `site/smzh.ch/de/smzhub-hypotheken-radar/`
**Build:** `build/build_hub_v5.py` (neue Funktion, eigenes LP-Inner)
**Typ:** Flagship-Landingpage für ein wiederkehrendes Research-Format (Zins-/Finanzierungs-Radar)
**Quelle Ausgaben:** `series_items('hypothekenradar')` · aktuellste = `[0]` · PDF aus Feld `pdfs` (bevorzugt `_DE_`)

### 6.1 Ziel der Seite
Den Hypotheken-Radar als eigenständiges, glaubwürdiges Format inszenieren und Finanzierungs-Interessierte (Abschluss / Verlängerung / Umschuldung) in **einen** klaren Hypotheken-/Finanzierungs-Beratungspfad führen. Doppelziel: Download/Lektüre der aktuellen Ausgabe (Research-Glaubwürdigkeit) **und** qualifizierter Finanzierungs-Lead.

### 6.2 Zielgruppe
Schweizer Privatpersonen mit konkretem Finanzierungsbezug: Käufer vor Abschluss, Eigentümer vor auslaufender Festhypothek, Umschuldungs-/Verlängerungs-Interessierte, zins-sensible Beobachter (SARON vs. Fest). Sekundär: Stamm-Leser, die monatlich wiederkehren.

### 6.3 Primärer Nutzerpfad
Hero (Format-Versprechen + 1 Beratungs-CTA) → „Was diese Publikation leistet" verstehen → **aktuelle Ausgabe herunterladen/lesen** → ggf. Archiv prüfen (frühere Ausgaben) → **Schluss-CTA** (Finanzierung/Hypothek besprechen). Sekundärpfad: direkt vom Hero-CTA in die Beratung.

### 6.4 Seitenstruktur mit Sections — VERBINDLICHE Block-Reihenfolge

| # | Block | Status | Inhalt/Logik |
|---|-------|--------|--------------|
| a | **Hero / `phead`** | VERBINDLICH | Format-Name „Hypotheken-Radar", Cadence „monatlich", Einordnungs-Lead. **Genau 1 Beratungs-CTA** Richtung Finanzierung/Hypothek. |
| b | **„Was diese Publikation leistet"** (Erklärteil, Text) | VERBINDLICH | Erklärt Nutzen, Frequenz, Themenfokus (Zinsen, SARON, Festhypothek, Verlängerung). Reiner Text, kein CTA. |
| c | **Download der neuesten Ausgabe** | VERBINDLICH | Build-dynamisch `series_items('hypothekenradar')[0]`. **PDF aus Feld `pdfs`, bevorzugt Datei mit `_DE_`-Marker** → Download-Button. **Fallback:** hat die neueste Ausgabe **kein** PDF → nur Artikel-Link auf den Beitrag, **kein** Download-Button. Zeigt Titel + Datum der Ausgabe. |
| d | **Archiv / Alle Ausgaben** | VERBINDLICH | Liste der letzten Ausgaben (`series_items` absteigend) als Lese-Links **plus** Verweis auf die bestehende Serien-Seite `smzhub-serie-hypotheken-radar` („Alle Ausgaben ansehen"). |
| e | **Schluss-CTA** | VERBINDLICH | Beratungs-/360°-CTA Richtung **Finanzierung/Hypothek** (terminorientiert). |
| — | Back-Link | VERBINDLICH | Zurück zu `smzhub-eigenheim` (Herkunfts-Kontext) bzw. smzhHub. |

> **Reihenfolge normativ:** Hero → Erklärteil → Download (aktuell) → Archiv → Schluss-CTA. Der Download der **aktuellen** Ausgabe steht **vor** dem Archiv (Aktualität priorisiert).

### 6.5 Funktion jeder Section
- **a Hero** — Format als „das" Finanzierungs-Research positionieren; ein ruhiger Beratungs-CTA.
- **b Erklärteil** — Erwartung/Nutzen klären, bevor Download/Beratung gefragt wird; baut Vertrauen.
- **c Download aktuelle Ausgabe** — Kern-Asset: niedrigschwellige Wertabgabe (PDF) als Vertrauens- und Wiederkehr-Anker.
- **d Archiv** — Tiefe/Kontinuität belegen; Lese-Pfad für Stöbernde; Brücke zur Serien-Seite.
- **e Schluss-CTA** — Konversionspunkt Richtung Finanzierungsberatung.

### 6.6 CTA-Logik
- **Hero-CTA (1×):** Finanzierung/Hypothek besprechen (Richtung Beratung). Genau einer.
- **Download-Block:** Aktionsziel ist der **PDF-Download** (bzw. Fallback Artikel-Link) — kein Beratungs-CTA, das ist Wertabgabe.
- **Archiv-Block:** reine Lese-Links + 1 Verweis auf die Serien-Seite. Kein Beratungs-CTA.
- **Schluss-CTA:** einziger weiterer Beratungs-CTA; Richtung Finanzierung/Hypothek, terminorientiert.
- **CTA-Richtung gesamte LP: Finanzierung/Hypothek** (nie Markt-/Kaufstrategie — das ist die Outlook-LP).

### 6.7 Was bewusst weggelassen wird
- **Voller Markt-/Kaufentscheid-Pfad** (gehört auf die Outlook-LP §7).
- **Mehr als 1 Beratungs-CTA im Hero** und **CTAs im Archiv/Download** (würden die Wertabgabe verwässern).
- **Interaktiver Inline-Rechner** (Backlog §5.2).
- **Newsletter-/Abo-Mechanik** für die Ausgabe (nicht Teil dieser Iteration; Download ist der Wiederkehr-Anlass).

---

## 7. SCHEMA: `smzhub-immobilien-outlook` (Flagship-LP Immobilien-Outlook) — V5 — `VERBINDLICH`

**Slug/Pfad:** `site/smzh.ch/de/smzhub-immobilien-outlook/`
**Build:** `build/build_hub_v5.py` (neue Funktion, eigenes LP-Inner)
**Typ:** Flagship-Landingpage für ein wiederkehrendes High-End-Research-Format (Markt-/Strategie-Outlook)
**Quelle Ausgaben:** `series_items('immobilien-outlook')` · aktuellste = `[0]` · PDF aus Feld `pdfs` (bevorzugt `_DE_`)

### 7.1 Ziel der Seite
Den Immobilien-Outlook als gehobene, quartalsweise Marktpublikation positionieren und Kauf-/Eigentums-Interessierte in **einen** klaren Eigenheimstrategie-/Kaufentscheid-Beratungspfad führen. Doppelziel: Download/Lektüre der aktuellen Ausgabe (Markt-Autorität) **und** qualifizierter Strategie-Lead.

### 7.2 Zielgruppe
Schweizer Privatpersonen mit grösseren Eigentumsentscheidungen: Kaufinteressierte (Timing, Region, Preisniveau), Eigentümer mit Strategiefragen (halten/verkaufen/umschichten), Eigenkapital-Planer. Sekundär: anspruchsvolle Stamm-Leser (quartalsweise Wiederkehr).

### 7.3 Primärer Nutzerpfad
Hero (Format-Versprechen, High-End-Anmutung + 1 Beratungs-CTA) → „Was diese Publikation leistet" → **aktuelle Ausgabe herunterladen/lesen** → ggf. Archiv prüfen → **Schluss-CTA** (Eigenheimstrategie/Kaufentscheid besprechen). Sekundärpfad: direkt vom Hero-CTA in die Beratung.

### 7.4 Seitenstruktur mit Sections — VERBINDLICHE Block-Reihenfolge

| # | Block | Status | Inhalt/Logik |
|---|-------|--------|--------------|
| a | **Hero / `phead`** | VERBINDLICH | Format-Name „Immobilien-Outlook", Cadence „quartalsweise", Einordnungs-Lead; als High-End-Publikation positioniert. **Genau 1 Beratungs-CTA** Richtung Eigenheimstrategie/Kaufentscheid. |
| b | **„Was diese Publikation leistet"** (Erklärteil, Text) | VERBINDLICH | Erklärt Nutzen, Frequenz, Fokus (Preise, Tragbarkeit, Regionen, Marktausblick). Reiner Text, kein CTA. |
| c | **Download der neuesten Ausgabe** | VERBINDLICH | Build-dynamisch `series_items('immobilien-outlook')[0]`. **PDF aus `pdfs`, bevorzugt `_DE_`** → Download-Button. **Fallback** ohne PDF → nur Artikel-Link, kein Download-Button. Titel + Datum (Quartal). |
| d | **Archiv / Alle Ausgaben** | VERBINDLICH | Liste der letzten Ausgaben als Lese-Links **plus** Verweis auf `smzhub-serie-immobilien-outlook`. |
| e | **Schluss-CTA** | VERBINDLICH | Beratungs-/360°-CTA Richtung **Eigenheimstrategie/Kaufentscheid** (terminorientiert). |
| — | Back-Link | VERBINDLICH | Zurück zu `smzhub-eigenheim` bzw. smzhHub. |

> **Reihenfolge normativ:** identisch zur Radar-LP (Hero → Erklärteil → Download aktuell → Archiv → Schluss-CTA). Konsistentes LP-Muster für beide Flagships.

### 7.5 Funktion jeder Section
- **a Hero** — Format als gehobene Marktpublikation positionieren; ein ruhiger Strategie-CTA.
- **b Erklärteil** — Nutzen/Erwartung klären; trägt die High-End-Positionierung inhaltlich.
- **c Download aktuelle Ausgabe** — Kern-Asset; Wertabgabe + Wiederkehr-Anlass.
- **d Archiv** — Kontinuität/Markt-Autorität belegen; Lese-Pfad; Brücke zur Serien-Seite.
- **e Schluss-CTA** — Konversionspunkt Richtung Eigenheimstrategie/Kaufentscheid.

### 7.6 CTA-Logik
- **Hero-CTA (1×):** Eigenheimstrategie/Kaufentscheid besprechen. Genau einer.
- **Download-Block:** PDF-Download (bzw. Fallback Artikel-Link); kein Beratungs-CTA.
- **Archiv-Block:** reine Lese-Links + 1 Verweis auf die Serien-Seite.
- **Schluss-CTA:** einziger weiterer Beratungs-CTA; Richtung Eigenheimstrategie/Kaufentscheid.
- **CTA-Richtung gesamte LP: Eigenheimstrategie/Kaufentscheid** (nie Finanzierung/Hypothek-Detail — das ist die Radar-LP).

### 7.7 Was bewusst weggelassen wird
- **Voller Finanzierungs-/Zinspfad** (gehört auf die Radar-LP §6).
- **Mehr als 1 Beratungs-CTA im Hero**, CTAs im Archiv/Download.
- **Interaktiver Inline-Rechner** (Backlog §5.2).
- **Newsletter-/Abo-Mechanik**.

---

## 8. GLOBAL: Blog-CTA-Regel — `VERBINDLICH` (dauerhaft)

> Verbindliche, dauerhafte Platzierungsregel für **alle** smzhHub-Seiten. Verhindert, dass Conversion-CTAs in redaktionelle Lese-Strecken eindringen und deren Lese-/Research-Charakter (und damit die Glaubwürdigkeit) verwässern.

### 8.1 Regel
Innerhalb der **redaktionellen Lese-/Blog-Rubriken** auf der **Hub-Startseite (`smzhub`)** und den **5 Funnel-Themenwelten** (`smzhub-eigenheim`, `smzhub-immobilienanlagen`, `smzhub-vermoegen`, `smzhub-zukunft`, `smzhub-horizon`) dürfen **keine Conversion-CTA-Elemente** platziert werden. **Blog-/Beitrags-Teaser sind reine Lese-Links** mit Lese-Charakter („Beitrag lesen").

### 8.2 Konkret betroffen in V5 (umzusetzen in dieser Iteration)
- **Home-`rubric()` Tool-Slots (`v5-mid`)** — die als „Rechner/Check/Analyse"-Karte in den Lese-Rubriken sitzenden Conversion-Slots (`build_hub_v5.py`: Daten in den `tool`-Feldern Z. 77 / 80 / 83, gerendert in `rubric()` Z. ~166–172). Diese sind aus den redaktionellen Rubriken **zu entfernen** bzw. in reine Lese-Teaser umzuwandeln.
- **`v5-season`-Block (`season()`)** — der Saison-Block mit `v5-se-cta` und werblichen Sub-Links (`build_hub_v5.py` Z. ~130–138). Sein Conversion-Charakter ist aufzulösen: als redaktioneller Lese-Block ohne Conversion-CTA führen (Teaser → „Beitrag lesen").

### 8.3 Ausnahmen (bleiben ausdrücklich erlaubt)
1. **Je Flagship-Anker/-Segment genau 1 Beratungs-CTA** (Eigenheim-Segmente → LP; auf den LPs der eine Hero-CTA). Das ist kein „Blog-CTA", sondern der definierte Funnel-Übergang.
2. **Der seitenweite Schluss-CTA jeder Seite** (ein Konversionspunkt am Seitenende).
3. **Deklarierte, eigenständige Rechner-/Tools-Sektionen** — z. B. die neue Eigenheim-Rechner-/Tools-Sektion (§1.4 Block 8) und Tools-Slots in den Flagship-Rails (§1.4a). Diese sind **als Tools deklariert** und liegen nicht „in den Blog geschmuggelt" innerhalb einer Lese-Strecke.

### 8.4 Abgrenzung „Blog-CTA" vs. „erlaubtes Element"
- **Verboten:** ein Conversion-/Beratungs-/„Rechner"-CTA, der **innerhalb** einer redaktionellen Beitrags-/Lese-Liste sitzt und wie ein Beitrag aussieht, aber in einen Funnel/ein Tool führt (z. B. der heutige `v5-mid`-Slot in `rubric()`).
- **Erlaubt:** ein CTA/Tool in einer **eigenen, klar deklarierten Sektion** mit eigener Überschrift (Flagship-Segment-CTA, Schluss-CTA, Tools-Sektion) — räumlich und semantisch von der Lese-Strecke getrennt.
- **Faustregel:** Steht das Element **in** einer Beitragsliste/Lese-Rubrik? → verboten. Ist es eine **eigene** Sektion (Flagship / Tools / Schluss-CTA)? → erlaubt.

### 8.5 Geltung & Umsetzungsstand
- **Gilt für alle 6 Seiten** (Startseite + 5 Themenwelten) **dauerhaft**, auch für künftige Seiten/Rubriken.
- **V5-Seiten** (`smzhub`, `smzhub-eigenheim`, `smzhub-immobilienanlagen`, `smzhub-horizon`): technische Umsetzung **in dieser Iteration** (§8.2).
- **`smzhub-vermoegen` / `smzhub-zukunft`** laufen noch auf dem **Editorial-Build**: die Regel **gilt** dort, ihre **technische Umsetzung erfolgt erst mit der V5-Migration** (Backlog §5.4). In dieser Iteration **kein Code-Eingriff** dort.
