# smzhHub Design Contract (V5)

Verbindliches Regelwerk fuer das visuelle System des smzhHub. Quelle der Wahrheit ist
der Style-Block `<style id="smzh-v5-css">` in `build/build_hub_v5.py`. Dieses Dokument
beschreibt, was dort gilt, was erlaubt ist und was verboten ist. Die Anwendung auf echte
Seiten macht der `builder` ueber `build/build_hub_v5.py` — nicht durch direktes
Seiten-Redesign.

Geltungsbereich: die von uns gebauten Hub-Seiten
(`site/smzh.ch/de/smzhub/`, `smzhub-immobilienanlagen/`, `smzhub-horizon/`,
`ratgeber-*/`). Die geklonte smzh.ch-Chrome (Header/Footer/Branding) wird NICHT
umgestaltet. Aeltere `smzhub-*`-Skripte (v2-v4, editorial, concepts) sind Legacy und
kein Vorbild.

---

## 1. Design-Tokens

Definiert auf `#ed-root` im v5-CSS. Token-Namen sind verbindlich; neue Werte werden NICHT
ad hoc eingefuehrt.

### 1.1 Farbe
| Token | Wert | Verwendung |
|---|---|---|
| `--navy` | `#03314B` | Primaerfarbe: Headlines, dunkle Flaechen (Hero, phead, Funnel-Band), Buttontext auf hell |
| `--teal` | `#185E7F` | Akzent: Links, Eyebrows/Kategorien, CTA-Pfeile, Hover-Kanten, 3px-Akzentlinien |
| `--lblue` | `#E9F4FC` | Helle Flaeche: Research-Band, Notes, Bild-Platzhalter, Tabellen-Header |
| `--ink` | `#1c2b36` | Fliesstext |
| `--muted` | `#5b6b7a` | Sekundaertext, Subtitles, Beschreibungen |
| `--faint` | `#8b9aa8` | Tertiaer: Meta, Datums-/Lese-Angaben, Label-Klassen wie `v5-dec-fresh` |
| `--line` | `#e5e7eb` | Rahmen, Trennlinien |

Zusatz-Werte, die im v5-CSS bereits etabliert sind und mitbenutzt werden duerfen
(NICHT erweitern): `#fff` (Kartenflaeche), Navy-Verlauf der CTA-Flaeche
`linear-gradient(152deg,#03314B,#0a3f5d,#16566f)`, Statuspunkt-Gruen `#28a745` / `#38c172`
(ausschliesslich als kleiner Aktualitaets-/Live-Punkt, nie als Flaeche/Badge).

Hex-Werte duerfen 1:1 statt Tokens auftauchen (das v5-CSS tut das auch, u. a. in den
`#ed-root`-Spezifitaets-Overrides gegen die Chrome-Link-Styles). Neue Komponenten nutzen
bevorzugt die Tokens.

### 1.2 Typografie
- Schrift: `Plus Jakarta Sans` (Fallback `-apple-system,'Segoe UI',Roboto,sans-serif`). Keine zweite Schriftfamilie.
- Gewichte: 400 / 500 / 600 / 700 / 800. Headlines 800, Sub-Headlines 700, Labels 700, Fliesstext 400.
- Headlines (`h1,h2,h3`): `color:var(--navy)`, `letter-spacing:-.02em` (Polish: `-.022em`), `text-wrap:balance`.
- Groessen-Skala (fluid, etabliert):
  - H1 (Hero/phead): `clamp(1.9rem,2.7vw,2.5rem)` / line-height 1.1-1.12
  - H2 (Section): `clamp(1.4rem,2.4vw,1.85rem)`, weight 800
  - Rubrik-Intro (h3): `clamp(1.2rem,1.9vw,1.55rem)`, weight 700
  - Karten-Titel: 1.02-1.22rem
  - Fliesstext: 1.05rem / line-height 1.7-1.72 (Lead 1.1-1.18rem)
  - Sub/Meta: .78-.92rem
  - Labels/Eyebrows: .69-.8rem

### 1.3 Spacing
- Section-Rhythmus: `.v5-sec` = `5rem` vertikal; Rubrik-Sektion `5.6rem`.
- Content-Breite: `.v5-wrap` / `.v5-*-in` = `max-width:1180px`, Seitenpadding `1.5rem`.
- Lesespalte Artikel: `max-width:760px` (`.art-body`).
- Karten-Innenpadding: 1.1-1.7rem. Grid-Gaps: 0.9-2.8rem.

### 1.4 Radius
- Grosse Flaechen (Hero-Bild, CTA, phead, dunkle Karten): 18-22px.
- Standard-Karten: 12-16px. Kleine Cover/Chips: 8px / 999px (Pille).
- Buttons/Pillen: `999px`.

### 1.5 Schatten
Navy-getoente, weiche Schatten — keine harten/grauen Boxen:
- Karte ruhend: `0 8px 22px -18px rgba(3,49,75,.5)`
- Karte Hover: `0 18px 40px -22px rgba(3,49,75,.5)` (Translate `-3px` bis `-4px`)
- Grosse Flaeche/Hero-Bild: `0 26px 54px -30px` bis `0 34px 64px -28px rgba(3,49,75,.6)`
Transition-Standard: `.25s cubic-bezier(.2,.7,.2,1)` fuer Transform, `.25s ease` fuer Schatten/Border.

---

## 2. Erlaubte Komponenten

Nur diese Bausteine sind Teil des Systems. Reuse vor Neubau. Neue Muster brauchen eine
schriftliche Begruendung in diesem Dokument.

| Komponente | Wurzelklasse | Zweck |
|---|---|---|
| Hero (Landing) | `.v5-hero` / `.v5-hero-in` (+ Karussell `.v5-car`/`.h-slide*`/`.h-dot`) | Einstieg Startseite: Claim links, Karussell rechts |
| Page-Head (Themenwelt) | `.v5-phead` / `.v5-phead-in` (+ `.v5-eyebrow`, h1, p) | Navy-Kopf der Unterseiten |
| Themenwelten-Band | `.v5-funnels` / `.v5-fn-top` / `.v5-fgrid` / `.v5-funnel` | Funnel-Kacheln (5 Einstiege) |
| Decision-Cards | `.v5-dec-sec` / `.v5-dec-track` / `.v5-dec` (`.v5-dec-cat/-q/-d/-fresh/-shape`) | Karussell konkreter Entscheidungsfragen |
| Saison-Block | `.v5-season` / `.v5-se-hero` / `.v5-se-sub` | Ein grosser Saison-Aufmacher + Sub-Links |
| Rubrik-Block | `.v5-rub-sec` / `.v5-rub-grid` / `.v5-rub-hero` + `.v5-rub-side` (`.v5-sl`, `.v5-mid`) | Lead-Hero + Sub-Liste + Tool-Mid-Hero |
| Research-Band | `.v5-research` / `.v5-rs-row` / `.v5-rs` (`.v5-rs-cov/-n/-cad/-go`) | 3 wiederkehrende Serien als Cover-Karten |
| **Flagship-Research-Segment** | `.v5-flagship` / `.v5-fa` + Rail `.v5-rub-side` (siehe Abschnitt 6) | Ein vollbreites Premium-Segment je Reihe mit rechtem Kontext-Rail (Hypotheken-Radar, Immobilien-Outlook) |
| **Zins-Verlaufs-Chart** | `.v5-ratechart` / `.v5-rc-fig` (siehe Abschnitt 7) | Redaktionelle, statische Zeitreihen-Figur (Inline-SVG, 1 Datenreihe) |
| **LP-Download-Block** | `.v5-dl` / `.v5-dl-btn` (siehe Abschnitt 8) | Download der neuesten Ausgabe (PDF-Pille) + Fallback Artikel-Link |
| **LP-Archiv-Liste** | `.v5-arch` (`.v5-sl`/`.v5-rs`-Karten) (siehe Abschnitt 8) | Ausgaben-Liste mit Datum + Verweis auf die Serien-Seite |
| Section-Head | `.v5-head` (h2 + `.v5-sub` + optional `.v5-more`) | Ueberschrift-Zeile mit Beistrich-Link |
| Eyebrow/Label | siehe Abschnitt 3 | kleine Auszeichner |
| Artikel-Bausteine | `.art-body`, `.art-fig`/`.art-fig-tag`, `.art-cta*`, `.art-faq*`, `.art-related`/`.art-rel-card` | Ratgeber-Seiten |
| Karte allgemein | `.v5-sl`, `.v5-mid`, `.v5-rs`, `.art-rel-card` | Standardkarten/Listenzeilen |

Legacy-Hinweis: `.v5-flag*` (`flag_card`) existiert nur als ungestyltes Markup im Build
und ist NICHT Teil des Systems. Das Flagship-Segment (Abschnitt 6) ersetzt diese Idee
sauber und gestylt. `.v5-flag*` nicht weiterverwenden. Ebenso abgeloest: `.v5-fa-grid`
(`1fr 1fr`) als gleichwertiges Flagship-**Paar** — das Flagship ist jetzt ein vollbreites
Segment im Bestands-`.v5-rub-grid` + Rail (Abschnitt 6); `.v5-fa-grid` bleibt nur ein
generischer 2-Spalten-Container, nicht das Flagship-Muster.

---

## 3. Label- und Eyebrow-Regel (verbindlich, Pre-Deploy-geprueft)

Betroffene Klassen (Lint-Liste): `art-cta-eyebrow`, `art-fig-tag`, `art-rel-k`,
`art-related-eyebrow`, `v5-eyebrow`, `v5-dec-fresh`. Dieselbe Regel gilt fuer alle
weiteren Label-/Kategorie-/Kadenz-/Badge-artigen Auszeichner im System
(`v5-dec-cat`, `v5-rh-cat`, `v5-rs-cad`, `h-slide-cat`, `v5-se-tag`, `v5-mid-tag`,
sowie die neue `v5-fa-badge`).

VERBINDLICH:
- KEIN `text-transform:uppercase` im v5-CSS. Der Pre-Deploy-Lint
  (`.claude/hooks/pre-deploy-lint.py`) blockt jeden Deploy, der das in der Quelle
  `build/build_hub_v5.py` oder im gerenderten `smzh-v5-css`-Block findet.
- KEINE literalen ALL-CAPS-Texte in Label-Klassen. Der Lint blockt
  `[A-ZAEOEUE]{4,}` im Textinhalt dieser Klassen. Labels in normaler Schreibung
  (z. B. "Hypotheken-Radar", "monatlich", "Aktualisiert 2026").
- Labels in Normalschrift mit dezentem `letter-spacing` zwischen `.01em` und `.02em`,
  `font-weight:700`, kleine `font-size` (.69-.8rem).
- Statt Versalien Differenzierung ueber Farbe (`--teal`/`--faint`), Gewicht und
  optionalen Statuspunkt.

Korrektur immer in der QUELLE `build/build_hub_v5.py` (die Label-Klasse dort aendern),
nicht nur im gerenderten HTML.

---

## 4. Sprache

- Deutsch, Schweizer Rechtschreibung: durchgehend "ss", niemals "ß"
  (z. B. "Fliesstext", "grosse", "Strasse", "schliessen").
- Konsistente Begriffe; Anglizismen sparsam und nur, wenn etabliert (z. B. "Research",
  "Outlook", "Hub" als Eigennamen). SEO-Keywords erhalten.
- Datumsformat: deutsche Monatskuerzel ("Jan", "Maerz", "Juni" ... "Dez") + Jahr,
  Lesezeit als "N Min". Trennzeichen Mittelpunkt " · ".

---

## 5. No-Gos (Rolle Design System Guardian)

Verboten — wird abgelehnt:
1. **Bunte Badges.** Keine farbigen Status-Chips (gruen/rot/orange/gelb als Flaeche).
   Auszeichner sind Text in `--teal`/`--faint`; der einzige Farbtupfer ist der kleine
   Statuspunkt (`--ok`-Gruen, max. ~7px) bei Aktualitaet/Kadenz.
2. **Zufaellige Icons.** Keine Icon-Sets, Emoji oder dekorativen Glyphen. Erlaubt sind
   ausschliesslich: Pfeil `→`/`‹`/`›` (Navigation), kleiner Rhombus `◆` als
   Platzhalter-Cover. Kein neuer Icon-Wildwuchs.
3. **PowerPoint-Diagramme.** Keine generischen Charts, Funnels-als-Pyramide, 3D-Balken,
   Tortendiagramme, Prozess-Pfeil-Ketten. Daten gehoeren in `.art-table` oder echte
   redaktionelle Bildfiguren (`.art-fig`).
4. **Generische SaaS-Komponenten.** Kein Pricing-Grid, keine Feature-Tick-Matrix, keine
   "Trusted by"-Logo-Wand, keine Testimonial-Slider-Klischees, keine Gradient-Hero-Blobs
   ausserhalb der definierten Hero/CTA-Flaechen.
5. **Freies Seiten-Redesign.** Der Guardian definiert nur das System (dieses Dokument +
   `COMPONENT_LIBRARY.html`). Seiten/Build-CSS aendert der `builder`. Keine ganzen Seiten
   neu erfinden, keine Inhalte strategisch umsortieren.
6. **Token-/Skalen-Drift.** Keine neuen Farben, Schriftgroessen ausserhalb der Skala,
   keine zweite Schriftfamilie, keine harten grauen Schatten.

---

## 6. Flagship-Research-Segment (geaendert: Vollbreiten-Segment + Kontext-Rail)

> **Geaendert mit PAGE_SCHEMA §3 (Entscheidung 3).** Das fruehere "gleichwertige
> 2er-Paar nebeneinander" (`.v5-fa-grid` als `1fr 1fr`) ist abgeloest. Neues Muster:
> **ein eigenstaendiges, vollbreites Segment je Flagship** (Hypotheken-Radar, dann
> Immobilien-Outlook) mit linker Hauptspalte (Flagship) und **rechtem Kontext-Rail**.
> Aufbau lehnt sich an den Bestands-Rubrik-Block (`.v5-rub-grid` + `.v5-rub-side`) an,
> wird aber als Premium-Flagship-Segment gefuehrt. Die `.v5-fa-*`-Klassen werden
> **wiederverwendet**, nur die Anordnung (Hauptspalte breit + Rail statt 2er-Grid)
> aendert sich. Legacy-Hinweis: `.v5-fa-grid` als `1fr 1fr`-Paar wird **nicht** mehr
> als Flagship-Muster verwendet (bleibt nur als generischer 2-Spalten-Grid-Container).

### 6.1 Zweck, Aufbau und Verhalten
Pro wiederkehrender Research-Reihe **ein vollbreites Segment**, das die Wertigkeit
"institutionelle Research-Basis" traegt und die Reihe in **einen** Beratungspfad
(neu: auf die jeweilige Flagship-LP) ueberleitet. Auf "Eigenheim & Hypothek" stehen
zwei solche Segmente direkt nach dem Hero: zuerst Hypotheken-Radar, dann Immobilien-Outlook.

Aufbau je Segment (zweispaltig, Bestands-Raster `.v5-rub-grid`):
1. **Linke Hauptspalte** (breit) — die Flagship-Karte `.v5-fa` mit:
   Cover/Visual, Format-Badge ("Research-Reihe · monatlich" / "· quartalsweise"),
   Titel, Erklaertext, Zeile "aktuelle Ausgabe", Archiv-Link und **genau einem**
   Beratungs-/Segment-CTA, der **neu auf die jeweilige LP** zeigt
   (`/de/smzhub-hypotheken-radar/` bzw. `/de/smzhub-immobilien-outlook/`).
2. **Rechtes Kontext-Rail** (`.v5-rub-side`) — reale, thematisch passende Beitraege als
   `.v5-sl`-Liste (reine Lese-Links) **plus optional ein** Rechner-`.v5-mid` (Tools-Slot,
   deklariertes Element, §8-Ausnahme in PAGE_SCHEMA). **Kein** zweiter Beratungs-CTA im Rail.

Verhalten:
- **Desktop (>= 880px):** Hauptspalte breit, Rail schmal — Spaltenverhaeltnis ueber die
  Bestands-Variable `--cols` (z. B. `3fr 2fr`, identisch zur Rubrik-Logik). Die zwei
  Segmente stehen **untereinander** (je ein voller `.v5-rub-grid`), nicht nebeneinander.
- **Mobil (< 880px):** eine Spalte — das **Rail rutscht unter** die Flagship-Hauptspalte
  desselben Segments (Bestandsverhalten von `.v5-rub-grid`). Reihenfolge der Segmente:
  Hypotheken-Radar zuerst, Immobilien-Outlook danach.

### 6.2 Pflicht-Anatomie je Segment
**Hauptspalte (`.v5-fa`, Klassen wiederverwendet):**
1. **Cover/Visual** — `v5-fa-cov` (Bild aus der aktuellsten Ausgabe `series_items(key)[0].image`; Ratio 16/9). Fallback: `--lblue`-Flaeche.
2. **Format-Badge** — `v5-fa-badge`, Normalschrift, KEINE Versalien (z. B. "Research-Reihe · monatlich"). Label-Regel (Abschnitt 3).
3. **Titel** — `v5-fa-title` (Reihen-Name, h3, weight 800, navy).
4. **Erklaertext** — `v5-fa-sub` (ein Satz, was die Reihe leistet; `--muted`).
5. **Zeile "aktuelle Ausgabe"** — `v5-fa-latest`: Datum (`v5-fa-date`, `--faint`) + Titel-Link (`v5-fa-latest-t`, navy/teal-hover; Lese-Link auf den Beitrag).
6. **Archiv-Link** — `v5-fa-archive` (sekundaerer Textlink "Alle Ausgaben"; im Eigenheim-Muster auf die **LP**, da diese den Archiv-Block traegt — PAGE_SCHEMA §3.2-Hinweis).
7. **Genau ein Segment-CTA** — `v5-fa-cta` (Pille, navy-Flaeche/weiss, Pfeil), **routet auf die jeweilige LP** (nicht mehr direkt auf die Serie). Kein zweiter Primaer-Button.

**Rechtes Rail (`.v5-rub-side`, Klassen wiederverwendet):**
8. **`.v5-sl`-Liste** mit 2-4 realen Lese-Links (aus `EIGENHEIM_DECISIONS`/`EIGENHEIM_EVERGREEN`), Titel + Meta (`.v5-sl-m`). Reine Lese-Links.
9. **Optional ein `.v5-mid`** als Rechner-Slot (Tools-Verweis), mit `.v5-mid-tag` "Rechner". Max. einer je Rail.

### 6.3 High-End-Hervorhebung des Outlook-Segments (nur Bestands-Tokens)
Das Outlook-Segment darf zusaetzlich als **gehobene Publikation** hervorgehoben werden —
**ausschliesslich ueber bestehende Tokens, KEINE neuen Farben/Schriften/Schatten**. Zulaessig:
- **Staerkere Navy-Praesenz** der Hauptspalte ueber den Modifier `.v5-fa--feature` (siehe
  COMPONENT_LIBRARY): ganze Flagship-Karte auf `--navy`-Flaeche statt `#fff`, Titel/Erklaertext
  in den vorhandenen Hellwerten (`#fff` / `#bcd3e2` — dieselben Werte wie `.v5-phead`), Cover
  bleibt; das Segment liest sich wie ein kleiner, fokussierter "phead-Block".
- Der Segment-CTA bleibt die **eine** weisse Pille (`v5-fa-cta`), jetzt auf Navy = derselbe
  Kontrast wie der CTA im `.v5-fa-foot`. Archiv-Link in `#9fd0ee` (Bestandswert).
- Der `.v5-fa--feature`-Block ist — wie der `.v5-fa-foot` und Hero/phead/CTA — ein bewusst
  zugelassenes dunkles Flaechen-Element; **kein** drittes neues dunkles Muster, sondern die
  vorhandene Navy-Flaeche auf die Karte angewandt.
**Nicht erlaubt:** ein "Premium"-Goldton, eine zweite Akzentfarbe, ein groesserer Radius
ausserhalb 18-22px, eine Sonderschrift oder ein staerkerer Schatten als in §1.5 definiert.
Differenzierung laeuft ueber **Flaeche (Navy) + Luft + Reihenfolge**, nicht ueber neue Tokens.

### 6.4 Reuse vor Neubau
- **Wiederverwendete Muster/Klassen (kein Neubau):** das gesamte `.v5-rub-grid` +
  `.v5-rub-side` + `.v5-sl`/`.v5-sl-list` + `.v5-mid`-Geruest (inkl. `--cols`,
  `.rev`-Logik, Mobile-Stacking); saemtliche `.v5-fa-*`-Klassen aus der Vor-Iteration;
  Section-Head `.v5-head`/`.v5-sub`; Cover-Logik wie `.v5-rs-cov`; Pillen-/Pfeil-Logik
  wie `.art-cta-btn` (`gap:.55em`, Pfeil `translateX(4px)`); Schatten/Transition §1.5;
  Label-Regel §3.
- **Nur eine wirklich neue Klasse** (mit Begruendung): `v5-fa--feature` — Modifier fuer
  die High-End-Navy-Variante des Outlook-Segments. Begruendung: im Bestand existiert keine
  Flagship-Karte auf Navy-Vollflaeche; der Modifier setzt nur **bestehende** Token-Werte
  (`--navy`, `#fff`, `#bcd3e2`, `#9fd0ee`) neu zusammen, fuehrt keinen neuen Wert ein.
- Es entstehen **keine** neuen Layout-Klassen fuer das Segment selbst — es nutzt das
  Bestands-`.v5-rub-grid`-Geruest. `.v5-fa-grid` (`1fr 1fr`) wird fuer Flagships nicht
  mehr verwendet.

### 6.5 Regeln fuer das Flagship-Segment
- **Genau ein** Segment-CTA je Segment (Pille → LP). Archiv-Link und Ausgaben-Titel sind
  sekundaere Textlinks, kein zweiter Button. Rail-Links sind **reine Lese-Links**; der
  Rechner-`.v5-mid` ist ein deklariertes Tool, kein Blog-CTA (§8-Ausnahme).
- **Zwei** aufeinanderfolgende Segmente (Radar, dann Outlook) — kein drittes Flagship-Segment
  auf derselben Seite (weitere Reihen → `.v5-research`-Band).
- Badge folgt der Label-Regel: keine Versalien, `letter-spacing .01-.02em`, weight 700.
- High-End-Hervorhebung nur ueber Bestands-Tokens (§6.3) — keine neue Farbe/Schrift.
- Keine bunten Badges, keine Icons ausser dem CTA-/Listen-Pfeil, **kein Diagramm im Cover**
  (Cover ist ein Ausgaben-Bild, kein Chart).
- Texte (Titel, Erklaertext, Badge-Wortlaut, Ausgaben-Titel, Rail-Linktexte) liefert die
  Redaktion; dieses Dokument legt nur Struktur, Klassen und Stil fest.

Vollstaendige Markup-/CSS-Spezifikation: siehe `COMPONENT_LIBRARY.html`, Abschnitt
"Flagship-Research-Segment". Den Block baut der `builder` nach dieser Spec in
`build/build_hub_v5.py` und auf die Subpage/LP ein — nicht der Guardian.

---

## 7. Zins-Verlaufs-Chart (neue Komponente — redaktionelle Datenfigur)

### 7.1 Zweck und Abgrenzung zum No-Go §5.3
Die Block-4-Sektion "Wie haben sich die Zinsen entwickelt?" (PAGE_SCHEMA §1.4/§2.6)
braucht eine **echte Zeitreihen-Figur** (SNB-Leitzins / SARON / repraesentative
Festhypothek). Sie wird als **statisches Inline-SVG-Linien-/Flaechen-Chart OHNE
JS-Bibliothek** umgesetzt und ist **ausdruecklich von §5.3 abgegrenzt**: §5.3 verbietet
*generische* Charts, 3D-Balken, Tortendiagramme, Funnel-Pyramiden und
Prozess-Pfeil-Ketten. Erlaubt — und hier gemeint — ist eine **reduzierte, redaktionelle
Datenfigur** im Stil einer `.art-fig`: eine einzige Zeitreihe, dezente Achsen, klare
Quellenangabe. Sie zaehlt damit zu den in §5.3 ausdruecklich zugelassenen "echten
redaktionellen Bildfiguren (`.art-fig`)", nur als Vektor statt Pixelbild.

### 7.2 Pflicht-Anatomie
1. **Figur-Rahmen** — `figure.v5-rc-fig` (Geometrie wie `.art-fig`/`.art-figw`:
   Radius 18px, `--lblue`-Grund, weicher Navy-Schatten §1.5). Optional ein Label oben
   links wie `.art-fig-tag` (Normalschrift, z. B. "Zinsentwicklung").
2. **Inline-SVG** — `svg.v5-rc-svg` mit fester `viewBox` (Koordinatenraum, nicht Pixel),
   `preserveAspectRatio="xMidYMid meet"`, `role="img"` + `<title>`/`<desc>` fuer A11y.
   Ratio 16/9 bis 2/1 (responsiv ueber `width:100%;height:auto`).
3. **Eine Datenreihe** — genau **eine** `polyline`/`path`-Linie in `--teal` (Stroke) ueber
   einer `--lblue`-Flaeche (`path` mit `fill`, zur Achse geschlossen, leicht transparent
   oder `--lblue` voll). KEINE zweite Serie im selben Chart.
4. **Dezente Achsen** — X/Y-Grundlinie und wenige Hilfslinien in `--line`; Achsen-Ticks
   und Wertlabels als kleine `text`-Elemente (`--faint`, Schriftgroesse ~10-12px im
   SVG-Raum). Jahre auf der X-Achse, Zins-% auf der Y-Achse.
5. **Datenpunkt-Marker (optional, dezent)** — kleine Kreise (`r` ~3-4) in `--teal` an den
   Stuetzpunkten; KEINE gefuellten "Bubble"-Flaechen.
6. **Bildunterschrift** — `figcaption` exakt wie `.art-fig figcaption` (links `--teal`-
   Strich, `--faint`, .82rem) **mit Quellenangabe** (z. B. "Quelle: SNB / SARON, Stand …").

### 7.3 Reuse vor Neubau
- Wiederverwendet: `.art-fig`-Rahmenlogik (Radius, `--lblue`, Schatten), `.art-fig-tag`
  fuer das optionale Label, `.art-fig figcaption` 1:1 fuer die Quellen-Caption; alle Farben
  aus den Tokens (`--teal` Linie, `--lblue` Flaeche, `--line` Achsen, `--faint`/`--navy`
  Labels). Keine neue Farbe, keine zweite Schrift, keine Chart-Lib.
- Neue Klassen, nur die Huelle (mit Begruendung — eine Vektor-Datenfigur existiert im
  Bestand nicht): `v5-ratechart` (Section-Wrapper), `v5-rc-fig` (Figur), `v5-rc-svg`
  (SVG), `v5-rc-line`, `v5-rc-area`, `v5-rc-axis`, `v5-rc-tick`, `v5-rc-dot`, `v5-rc-lbl`
  (SVG-Teilklassen fuer Stil/Farbe). Geometrie/Skalierung/`viewBox` sind in
  COMPONENT_LIBRARY mit Beispiel hinterlegt.

### 7.4 Regeln fuer den Zins-Chart
- **Genau eine Datenreihe** — keine Multi-Serien-Ueberlagerung, keine Legende mit mehreren
  Farben. Sollen Radar (Finanzierung) und Outlook (Markt) je eine eigene Reihe zeigen,
  sind das **zwei getrennte Figuren**, nicht ein Multi-Linien-Chart.
- **Statisch, kein JS, keine externe Lib** — reines Inline-SVG; keine Interaktivitaet,
  keine Tooltips, keine Animation ausser dezentem CSS (optional `stroke-dasharray`-Aufbau,
  kein Muss).
- **Kein generischer/3D-/Torten-/Balken-/Funnel-Chart** (§5.3 bleibt voll gueltig).
- **Achsen dezent**, nie dominanter als die Datenlinie; Gitter nur so viel wie noetig.
- **Quellenangabe Pflicht** in der `figcaption`.
- **Datenpunkte liefert die Redaktion (WP2/editorial).** Dieses Dokument und die
  COMPONENT_LIBRARY definieren **nur** Huelle, Skalierung, Achsen und ein
  Demonstrations-`viewBox` — **keine erfundenen Werte** in der finalen Figur. Bis reale
  Daten vorliegen, bleibt die Figur ein deklarierter Platzhalter.
- Label-Texte (Jahre, %-Werte) folgen der Label-Regel: keine Versalien.

Vollstaendige Markup-/CSS-Spezifikation inkl. Beispiel-`viewBox`/Skalierung: siehe
`COMPONENT_LIBRARY.html`, Abschnitt "Zins-Verlaufs-Chart".

---

## 8. Flagship-Landingpages — Download-/Archiv-Bausteine und LP-Gesamtlayout

> Bezug: PAGE_SCHEMA §6 (Radar-LP) und §7 (Outlook-LP). Die LP ist **keine** neue
> Seitenarchitektur, sondern eine **V5-Seite im Bestandsraster** (Hero `.v5-phead`,
> Body `.v5-sec`/`.v5-wrap`, Schluss-CTA `.art-cta`, Back-Link). Nur die zwei
> LP-spezifischen Bausteine (Download, Archiv) werden hier ergaenzt.

### 8.1 LP-Gesamtlayout (Reuse, kein Neubau)
- **Hero:** `.v5-phead`/`.v5-phead-in` mit `.v5-eyebrow` (Format + Cadence, Normalschrift),
  H1 (Format-Name), Lead und **genau einem** Beratungs-CTA `.v5-phead-cta` (Pille).
- **Erklaerteil "Was diese Publikation leistet":** reiner Text in `.v5-sec` (`.v5-lead`/
  Absaetze), kein CTA.
- **Download-Block:** `.v5-sec` mit `.v5-dl` (§8.2).
- **Archiv-Block:** `.v5-sec` mit `.v5-arch` (§8.3).
- **Schluss-CTA:** `.art-cta` (genau ein Primaer-Button `art-cta-btn1`), Richtung
  Finanzierung (Radar) bzw. Eigenheimstrategie (Outlook).
- **Back-Link:** `.v5-back`/`.v5-backsec` wie im `category_inner`.
- Keine neuen Layout-/Sektionsklassen fuer die LP ausser `.v5-dl*` und `.v5-arch*`.

### 8.2 Download-Block der neuesten Ausgabe (`.v5-dl`)
- **Datenquelle:** `series_items(key)[0]` (neuestes Datum). PDF aus Feld `pdfs`,
  **bevorzugt die Datei mit `_DE_`-Marker** (PAGE_SCHEMA §2.1).
- **Aufbau:** Karte `.v5-dl` (weisser Card-Stil, `--line`, Radius 14-16px, Schatten §1.5)
  mit: Datums-/Cadence-Label `.v5-dl-meta` (`--faint`, Label-Regel), Titel `.v5-dl-t`
  (navy, weight 700/800), kurzer Beschreibung `.v5-dl-p` (`--muted`), und der Aktion.
- **Download-Button** `.v5-dl-btn` — **wiederverwendet die Pillen-Geometrie von
  `.v5-fa-cta`/`.art-cta-btn`** (`border-radius:999px`, navy-Flaeche, weisser Text,
  `gap:.55em`, Hover `translateY(-2px)`, Pfeil `.ar` `translateX(4px)`). Label z. B.
  "Aktuelle Ausgabe herunterladen (PDF)". Der Pfeil ist der einzige zulaessige Glyph
  (Download-Pfeil als `↓` zulaessig, sonst `→`; **kein** Icon-Set).
- **Fallback (kein PDF):** hat die neueste Ausgabe **kein** `pdfs`-File →
  **KEIN** Download-Button. Stattdessen nur der **Artikel-Lese-Link** `.v5-dl-read`
  ("Ausgabe lesen" → `cur['path']`), Textlink in `--teal`. Es wird **nie** ein
  Download-Button gerendert, der auf eine nicht existierende PDF zeigt.
- Genau **eine** Aktion je Download-Block: entweder Download-Pille **oder** (Fallback)
  Lese-Link. Kein zusaetzlicher Beratungs-CTA in diesem Block (Wertabgabe, PAGE_SCHEMA §6.6/§7.6).

### 8.3 Archiv-Liste (`.v5-arch`)
- **Aufbau:** Liste der Ausgaben (`series_items(key)` absteigend) als **Karten im
  Bestandsstil** — wahlweise `.v5-sl`-Listenzeilen (kompakt: Titel + Datum `.v5-sl-m`)
  oder `.v5-rs`-Cover-Karten (mit Ausgaben-Cover). Beide existieren bereits; **keine neue
  Kartenklasse**. Empfehlung: `.v5-sl`-Liste fuer die letzten N Ausgaben.
- **Datum** je Ausgabe als `--faint`-Meta (`.v5-sl-m`/`.v5-rs-cad`), deutsches
  Format/Quartal (§4).
- **"Alle Ausgaben"-Verweis** auf die **Serien-Seite** (`smzhub-serie-*`) als sekundaerer
  Textlink (`.v5-more` oder `.v5-back`-Stil, `--teal`). Das ist der einzige Pflicht-
  Verweis; reine Lese-Links sonst, **kein** Beratungs-CTA im Archiv.
- Reuse-only: `.v5-sl`/`.v5-sl-list`/`.v5-rs`/`.v5-rs-row`/`.v5-more`. `.v5-arch` ist nur
  ein duenner Wrapper/Section-Marker, kein neues Kartendesign.

### 8.4 Regeln fuer die LP-Bausteine
- **Kein Download-Button ohne real existierende PDF** — Fallback ist Pflicht (§8.2).
- **Aktuelle Ausgabe vor Archiv** (Reihenfolge normativ, PAGE_SCHEMA §6.4/§7.4).
- **Ein Beratungs-CTA im Hero, einer im Schluss-CTA** — **keiner** im Download- oder
  Archiv-Block (PAGE_SCHEMA §6.6/§7.6). Download = Wertabgabe, Archiv = Lese-Pfad.
- Download-/Archiv-Labels folgen der Label-Regel (keine Versalien).
- Keine neue Seitenarchitektur, kein neues Kartendesign — Bestandsraster + Bestandskarten.

Vollstaendige Markup-/CSS-Spezifikation: siehe `COMPONENT_LIBRARY.html`, Abschnitte
"LP — Download-Block" und "LP — Archiv-Liste".

---

## 9. Neue No-Gos (aus den Komponenten §6-§8)

Ergaenzen die No-Go-Liste §5; gleicher Verbindlichkeitsgrad (werden abgelehnt):

1. **Flagship als 2er-Karten-Paar.** Das fruehere `.v5-fa-grid` (`1fr 1fr`) als
   gleichwertiges Flagship-Paar ist **abgeloest** und wird nicht mehr als Flagship-Muster
   gebaut. Flagships sind **vollbreite Segmente mit rechtem Rail** (§6).
2. **Zweiter Conversion-CTA im Flagship-Segment, Download- oder Archiv-Block.** Pro
   Flagship-Segment **genau ein** Segment-CTA (→ LP); im Download/Archiv **kein**
   Beratungs-CTA. Rail-Links und Ausgaben-Titel sind reine Lese-Links.
3. **Outlook-Hervorhebung ueber neue Tokens.** Die High-End-Anmutung des Outlook-Segments
   entsteht **nur** ueber Bestands-Tokens (Navy-Flaeche `.v5-fa--feature` + Luft +
   Reihenfolge). **Kein** Goldton, keine zweite Akzentfarbe, kein Sonder-Radius/-Schatten,
   keine Sonderschrift.
4. **Zins-Chart als Multi-Serien-Spaghetti.** Genau **eine** Datenreihe je Figur. Keine
   ueberlagerten Mehrfach-Linien, keine Mehrfarben-Legende; mehrere Reihen ⇒ mehrere
   getrennte Figuren.
5. **Generischer/3D-/Torten-/Balken-Chart oder Chart-JS-Lib.** Der Zins-Chart ist eine
   statische, reduzierte Inline-SVG-Datenfigur; §5.3 bleibt fuer alle anderen Diagrammtypen
   voll gueltig. Keine Chart-Bibliothek, kein Tooltip-/3D-/Tortendiagramm.
6. **Erfundene Daten im Zins-Chart.** Keine ausgedachten Zinswerte in der finalen Figur —
   Datenpunkte kommen vom editorial; bis dahin deklarierter Platzhalter.
7. **Download-Button ohne reale PDF.** Nie eine Download-Pille rendern, wenn die neueste
   Ausgabe kein `pdfs`-File hat — dann nur Artikel-Lese-Link (§8.2-Fallback).
8. **Neue Seitenarchitektur / neues Kartendesign fuer die LP.** Die LP ist eine V5-Seite
   im Bestandsraster (`.v5-phead`/`.v5-sec`/`.art-cta`); Archiv nutzt Bestandskarten
   (`.v5-sl`/`.v5-rs`). Keine LP-eigene Sektions-/Kartenfamilie ausser `.v5-dl*`/`.v5-arch*`.
9. **Diagramm im Flagship-Cover.** Das Cover ist ein Ausgaben-Bild (oder `--lblue`-Fallback),
   nie ein eingebettetes Chart.
