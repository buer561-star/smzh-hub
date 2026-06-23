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

- **V5-System** (`build/build_hub_v5.py`) rendert heute: `smzhub` (Startseite, voll), `smzhub-immobilienanlagen` und `smzhub-horizon` (schlanke Themenwelt-Stubs via `category_inner` → `v5-phead`-Hero + `v5-wrap`-Body + Back-Link).
- **Editorial-System** (`build/build_hub_editorial.py`) rendert heute u. a. `smzhub-eigenheim` via `theme_inner('eigenheim')`. Ist-Block-Reihenfolge dort: `themebar → crumb → hero → decision_carousel (DECISIONS, Rubrik=immobilien) → "Im Fokus" (rubric_body) → Dossier ("Roter Faden") → research_band ("Relevantes Research") → "Weitere Beiträge" → guides_band ("Guides & Evergreens") → "In Vorbereitung" → CTA`.
- **Reale Inhalte bestätigt** (alle Seiten existieren): 10 × `ratgeber-*`; `smzhub-serie-hypotheken-radar` (monatlich, 8 Ausgaben); `smzhub-serie-immobilien-outlook` (quartalsweise, 8 Ausgaben); `smzhub-dossier-eigenheim`.
- **Entscheidung 1:** `smzhub-eigenheim` migriert auf V5 (künftig gebaut in `build/build_hub_v5.py`, **nicht** mehr `build_hub_editorial.py`) und wird dabei um die zwei Flagship-Formate restrukturiert.

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

### 1.4 Seitenstruktur mit Sections — VERBINDLICHE Block-Reihenfolge

| # | Block | Status | Quelle/Ziel |
|---|-------|--------|-------------|
| 1 | **Hero (Themenwelt-Kopf)** | VERBINDLICH | `v5-phead`: Eyebrow „smzhHub · Themenwelt", H1 „Eigenheim & Hypothek", Einordnungs-Lead. Genau **ein** Hero-CTA (kontextarm, Richtung Beratung). |
| 2 | **Flagship-Anker A — Hypotheken-Radar** | VERBINDLICH | Anker-Block nach Muster §3. → `smzhub-serie-hypotheken-radar` |
| 3 | **Flagship-Anker B — Immobilien-Outlook** | VERBINDLICH | Anker-Block nach Muster §3. → `smzhub-serie-immobilien-outlook` |
| 4 | **Entscheidungspfade (nach Nutzerproblem)** | VERBINDLICH | Decision-Cards, **nur Rubrik Eigenheim/Hypothek**. Übernahme aus `DECISIONS`, neu auf reale `ratgeber-*` geroutet (siehe §1.6). |
| 5 | **Rechner & Tools (Verweis-Slot)** | VERBINDLICH (schlank) | Ein Verweis-Element auf bestehenden Tragbarkeits-/Bewertungs-Pfad. **Kein** eigener Rechner-Block (→ OUT OF SCOPE §1.7). |
| 6 | **Vertiefende Inhalte** | VERBINDLICH | Zweiteilig: (a) Grundlagen/Evergreens (aus `EVERGREEN['immobilien']`), (b) optional Dossier-Verweis „Eigenheim finanzieren" → `smzhub-dossier-eigenheim`. |
| 7 | **Beratungs-/Schluss-CTA** | VERBINDLICH | Themenweiter Abschluss-CTA Richtung 360°-Check-up / Termin. |
| — | Back-Link „Zurück zum smzhHub" | VERBINDLICH | Wie V5-`category_inner`. |

> **Reihenfolge ist normativ.** Die zwei Flagship-Anker stehen **direkt nach dem Hero** und **vor** allen Entscheidungspfaden/Tools — als gleichwertiges, prominentes Block-Paar (Position 2 + 3).

### 1.5 Funktion jeder Section
1. **Hero** — Verortung und Erwartung setzen: „Dies ist der Eigenheim-Bereich." Kein Content-Wettbewerb mit den Ankern; ein einziger ruhiger CTA.
2. **Hypotheken-Radar** — Finanzierungs-/Zinsseite. Macht das monatliche Format zum Wiederkehr-Anlass und leitet Verlängerer/Käufer in den Finanzierungs-Beratungspfad.
3. **Immobilien-Outlook** — Marktseite. Macht das quartalsweise Format greifbar und leitet Kauf-/Strategie-Interessierte in den Eigenheimstrategie-Pfad.
4. **Entscheidungspfade** — Übersetzt Lebensfragen in konkrete Einstiege; fängt Nutzer ab, die nicht über die Research-Anker einsteigen, und routet sie in den passenden Ratgeber.
5. **Rechner & Tools** — Niedrigschwelliger Selbst-Einstieg (Tragbarkeit/Bewertung); Brücke von „informieren" zu „rechnen lassen" zu „beraten lassen".
6. **Vertiefende Inhalte** — Bedient Nutzer mit Grundlagenbedarf und gibt dem Dossier (Storyline) einen Platz, ohne die Anker zu verdrängen.
7. **Beratungs-CTA** — Sammelt die Restnachfrage themenweit; letzter Konversionspunkt.

### 1.6 CTA-Logik
- **Hero-CTA (1×):** ruhiger Primär-CTA Richtung Beratung/Check-up (z. B. „Finanzierung besprechen"). Bewusst nur einer, um die Anker nicht zu überstrahlen.
- **Radar-Anker-CTA (Pflicht, 1 Beratungspfad):** Richtung **Finanzierung** — „Hypothek prüfen" / „Finanzierung besprechen" / „Verlängerung planen". Sekundäraktionen (nicht-CTA): „Aktuelle Ausgabe lesen", „Alle Ausgaben" (Archiv → Serie).
- **Outlook-Anker-CTA (Pflicht, 1 Beratungspfad):** Richtung **Strategie** — „Eigenheimstrategie besprechen" / „Kaufentscheid besprechen". Sekundär: „Aktuelle Ausgabe lesen", „Alle Ausgaben".
- **Decision-Cards:** jede Karte verlinkt in **einen realen Ratgeber** (kein Beratungs-CTA — das ist der Lese-/SEO-Pfad). Routing:
  - Hypothek/Finanzierung-nah → `ratgeber-saron-oder-festhypothek`, `ratgeber-tragbarkeit-hypothek`, `ratgeber-amortisieren-oder-investieren`
  - Markt/Kaufentscheid → `ratgeber-eigenheim-kaufen-oder-warten`, `ratgeber-eigenkapital-eigenheim`
- **Tools-Slot:** ein Aktions-Link (Tragbarkeit/Bewertung), low-commitment.
- **Schluss-CTA:** themenweiter Beratungs-/360°-CTA (höchstes Commitment), terminorientiert.
- **CTA-Hierarchie:** pro Flagship-Anker **genau ein** primärer Beratungspfad-CTA. Nie zwei konkurrierende Primär-CTAs in einem Anker.

### 1.7 Was bewusst weggelassen wird (diese Iteration)
- **Eigenständige Flagship-Landingpages** mit vollen, eigenen Beratungspfaden (Radar-LP, Outlook-LP). Hier nur Anker-Blöcke, die auf die bestehenden Serien-Seiten zeigen. → **Folge-Iteration.**
- **Dedizierter Tragbarkeits-/Hypothekenrechner-Block** (interaktiv, mehrteilig). Diese Iteration: nur schlanker Verweis-Slot (Position 5). → **Folge-Iteration.**
- **Bidirektionale Ratgeber ↔ Subpage-Verlinkung** (Rückverlinkung aus den `ratgeber-*` auf diese Subpage / Anker). Diese Iteration ist einseitig: Subpage → Ratgeber. → **Folge-Iteration.**
- **Investment-Guide-Anker** — gehört thematisch zu Anlagen, nicht Eigenheim; hier nicht aufgenommen.
- **Vollständiges Beitrags-/Artikelarchiv** der Rubrik (das Editorial-„Weitere Beiträge"/„In Vorbereitung"). Nachrangig zu den Ankern; entfällt zugunsten der klareren Funnel-Struktur.
- **Sticky Rubriken-Themebar** (Editorial-`themebar`) — im V5-Subpage-Muster nicht vorgesehen.

### 1.8 Migrationszuordnung Editorial → V5 (was bleibt, was fällt)

| Editorial-Block (Ist) | Entscheidung | V5-Ziel |
|---|---|---|
| `decision_carousel` (DECISIONS, Rubrik immobilien) | **ÜBERNEHMEN**, neu auf reale `ratgeber-*` geroutet | Block 4 |
| `research_band` (Hypotheken-Radar + Immobilien-Outlook) | **ERSETZEN/AUFWERTEN** durch zwei eigenständige Flagship-Anker | Block 2 + 3 |
| Dossier „Roter Faden" (`smzhub-dossier-eigenheim`) | **ÜBERNEHMEN** als Verweis | Block 6b |
| `guides_band` / `EVERGREEN['immobilien']` | **ÜBERNEHMEN** (schlanker) | Block 6a |
| „Im Fokus" (`rubric_body`, Leitartikel + Begleitung) | **WEGFALL** (nachrangig zu Ankern) | — |
| „Weitere Beiträge" / „In Vorbereitung" | **WEGFALL** | — |
| Editorial-Hero + sticky `themebar` | **ERSETZEN** durch V5-`v5-phead`-Hero | Block 1 |
| Schluss-CTA | **ÜBERNEHMEN** (V5-Schluss-CTA) | Block 7 |

---

## 2. Reale Inhalts-Zuordnung (Eigenheim) — `VERBINDLICH`

### 2.1 Flagship-Quellen
| Anker | Serie (Slug) | Cadence | Ausgaben (Ist) | Aktuellste Ausgabe | Archiv-Ziel |
|---|---|---|---|---|---|
| Hypotheken-Radar | `smzhub-serie-hypotheken-radar` | monatlich | 9 | jeweils neueste (build-dynamisch, `series_items('hypothekenradar')[0]`) | Serien-Seite |
| Immobilien-Outlook | `smzhub-serie-immobilien-outlook` | quartalsweise | 7 | jeweils neueste (`series_items('immobilien-outlook')[0]`) | Serien-Seite |

> Aktuellste Ausgabe wird **dynamisch** aus den Serien-Items gezogen (neuestes Datum), nicht hartkodiert.

### 2.2 Ratgeber-Zuordnung (Decision-Cards & vertiefende Inhalte)
| Thematischer Anker | Ratgeber (real) | Rolle |
|---|---|---|
| **Radar** (Finanzierung/Zinsen) | `ratgeber-saron-oder-festhypothek` | Kern-Entscheidung Hypothekenstrategie |
| **Radar** | `ratgeber-tragbarkeit-hypothek` | Tragbarkeit (Bank-Sicht) |
| **Radar** (hypothekennah) | `ratgeber-amortisieren-oder-investieren` | Kapitalverwendung bei Hypothek |
| **Outlook** (Markt/Kaufentscheid) | `ratgeber-eigenheim-kaufen-oder-warten` | Timing-/Marktentscheid |
| **Outlook** | `ratgeber-eigenkapital-eigenheim` | Eigenkapital für den Kauf |

### 2.3 Grundlagen/Evergreen (Block 6a) — aus `EVERGREEN['immobilien']`
`Tragbarkeit optimieren` · `Hypothekenarten im Vergleich` · `Wie kaufe ich eine Immobilie?` · `Wohneigentumsförderung` (bestehende Evergreen-Seiten).

### 2.4 Dossier (Block 6b)
`smzhub-dossier-eigenheim` — „Eigenheim finanzieren" (Storyline), als Verweis-Element.

---

## 3. MUSTER: „Flagship-Research-Anker" — `MUSTER` (wiederverwendbar)

> Wiederverwendbares Sektions-Muster für jede Themenwelt mit wiederkehrendem Research-Format
> (Eigenheim heute; künftig z. B. Vorsorge, Steuern, Anlagen). Definiert die **Pflicht-Elemente** eines Anker-Blocks.

### 3.1 Platzierung
- **Immer direkt nach dem Hero**, vor Entscheidungspfaden/Tools.
- Bei **zwei** Flagship-Formaten je Themenwelt: als **gleichwertiges, prominentes Block-Paar** (z. B. Eigenheim: Radar + Outlook). Keine Hierarchie zwischen den beiden Ankern.
- Bei **einem** Format: einzelner Anker, gleiche Pflicht-Elemente.

### 3.2 Pflicht-Elemente je Anker (alle obligatorisch)
1. **Format-Name** (z. B. „Hypotheken-Radar").
2. **Cadence-Label** (monatlich / quartalsweise) — sichtbar, da Wiederkehr-Versprechen.
3. **Aktuellste Ausgabe**, verlinkt auf den jeweiligen Beitrag (Titel + Datum; build-dynamisch neueste).
4. **Archiv-Einstieg** auf die jeweilige Serien-Seite (`smzhub-serie-*`), Beschriftung Richtung „Alle Ausgaben".
5. **Genau ein primärer Beratungspfad-CTA**, thematisch passend zum Format (siehe §3.3).

### 3.3 CTA-Richtung je Format-Typ
| Format-Typ | Beratungspfad-CTA Richtung |
|---|---|
| Zins-/Finanzierungs-Radar (z. B. Hypotheken-Radar) | „Hypothek prüfen" / „Finanzierung besprechen" / „Verlängerung planen" |
| Markt-/Strategie-Outlook (z. B. Immobilien-Outlook) | „Eigenheimstrategie besprechen" / „Kaufentscheid besprechen" |
| (künftig) Vorsorge-Format | „Vorsorge analysieren" / „Pensionierung planen" |
| (künftig) Steuer-Format | „Steuern optimieren" / „Steuersituation besprechen" |

### 3.4 Regeln
- **Ein** Primär-CTA pro Anker — keine konkurrierenden Primär-CTAs.
- Anker zeigt auf **bestehende** Serien-Seite; **keine** eigene Flagship-Landingpage in der ersten Iteration (das ist die definierte Folge-Iteration).
- Cadence-Label und „aktuellste Ausgabe" sind **nicht optional** — sie tragen das Wiederkehr- und Aktualitäts-Versprechen.
- Reihenfolge der Pflicht-Elemente innerhalb des Ankers ist logisch (Name → Cadence → aktuelle Ausgabe → Archiv → CTA); konkrete visuelle Anordnung entscheidet `design-system`.

### 3.5 Anwendungsregel für künftige Subpages
Eine neue Themenwelt-Subpage übernimmt das Block-Raster aus §1.4 (Hero → Anker → Entscheidungspfade → Tools → Vertiefung → CTA). Hat sie kein wiederkehrendes Research-Format, entfällt der Anker-Block ersatzlos und sie bleibt ein V5-`category_inner`-Stub (wie heute `smzhub-horizon`).

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

### 4.4 `smzhub-vermoegen` · `smzhub-zukunft` · `smzhub-steuern` — `EDITORIAL (noch nicht migriert)`
**Pfade:** `de/smzhub-vermoegen/`, `de/smzhub-zukunft/`, `de/smzhub-steuern/` · **Build:** aktuell `build_hub_editorial.py` (`theme_inner`).
Noch auf dem Editorial-System. Migration auf V5 + ggf. Flagship-Anker-Muster (§3) in Folge-Iterationen — Eigenheim ist der Pilot.

### 4.5 Research & Serien — `BESTEHEND` (Ziele der Anker)
- `de/smzhub-research/` — Übersicht der Flagship-Formate.
- `de/smzhub-serie-hypotheken-radar/` — Archiv-Ziel Radar (Eigenheim-Anker A).
- `de/smzhub-serie-immobilien-outlook/` — Archiv-Ziel Outlook (Eigenheim-Anker B).
- `de/smzhub-serie-investment-guide/` — Anlagen-Format (nicht Eigenheim).
- `de/smzhub-dossier-eigenheim/` — Storyline „Eigenheim finanzieren" (Block 6b).

---

## 5. Backlog / Folge-Iterationen (aus §1.7 abgeleitet)

1. **Flagship-Landingpages** mit eigenen, vollen Beratungspfaden (Radar-LP, Outlook-LP).
2. **Dedizierter Tragbarkeits-/Hypothekenrechner-Block** (interaktiv) statt Verweis-Slot.
3. **Bidirektionale Verlinkung** Ratgeber ↔ Subpage/Anker.
4. **V5-Migration** der übrigen Editorial-Subpages (Vermögen, Zukunft, Steuern) + Prüfung Flagship-Anker je Themenwelt.
5. **Immobilienanlagen** vom Stub auf Anker-Muster heben (Outlook geteilt mit Eigenheim).
