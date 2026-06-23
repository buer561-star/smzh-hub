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
| **Flagship-Research-Anker** | `.v5-flagship` / `.v5-fa` (siehe Abschnitt 6) | Gleichwertiges Premium-Paar (Hypotheken-Radar + Immobilien-Outlook) |
| Section-Head | `.v5-head` (h2 + `.v5-sub` + optional `.v5-more`) | Ueberschrift-Zeile mit Beistrich-Link |
| Eyebrow/Label | siehe Abschnitt 3 | kleine Auszeichner |
| Artikel-Bausteine | `.art-body`, `.art-fig`/`.art-fig-tag`, `.art-cta*`, `.art-faq*`, `.art-related`/`.art-rel-card` | Ratgeber-Seiten |
| Karte allgemein | `.v5-sl`, `.v5-mid`, `.v5-rs`, `.art-rel-card` | Standardkarten/Listenzeilen |

Legacy-Hinweis: `.v5-flag*` (`flag_card`) existiert nur als ungestyltes Markup im Build
und ist NICHT Teil des Systems. Der neue Flagship-Anker (Abschnitt 6) ersetzt diese Idee
sauber und gestylt. `.v5-flag*` nicht weiterverwenden.

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

## 6. Flagship-Research-Anker (neue Komponente)

### 6.1 Zweck und Abgrenzung
Ein **gleichwertiges, prominentes Paar** aus zwei institutionellen Research-Reihen —
**Hypotheken-Radar** und **Immobilien-Outlook** — das die Wertigkeit "institutionelle
Research-Basis" traegt. Es steht ueber den Decision-Cards/Standardkarten und hebt sich
klar von ihnen ab durch: groessere Cover, dunkler Navy-Footer-Block je Anker,
zweispaltiges, exakt gleichwertiges Desktop-Layout (kein Lead/Sub-Gefaelle), mehr
vertikale Luft. Auf der Subpage "Eigenheim & Hypothek" ist dies der obere Anker.

Verhalten:
- Desktop (>= 880px): zwei gleich grosse Spalten (`1fr 1fr`), beide Anker identisch
  aufgebaut, keiner dominiert.
- Mobil: gestapelt (eine Spalte), Reihenfolge Hypotheken-Radar zuerst.

### 6.2 Pflicht-Anatomie je Anker
1. **Cover/Visual** — `v5-fa-cov` (Bild aus der jeweils aktuellsten Ausgabe; Ratio 16/9, Radius wie grosse Flaeche). Fallback: `--lblue`-Flaeche.
2. **Format-Badge** — `v5-fa-badge`, Normalschrift, KEINE Versalien (z. B. "Research-Reihe · monatlich"). Faellt unter die Label-Regel (Abschnitt 3).
3. **Headline** — `v5-fa-title` (Name der Reihe, h-Ebene als `<span>`/h3, weight 800, navy).
4. **Subtitle** — `v5-fa-sub` (ein Satz, was die Reihe leistet; `--muted`).
5. **Zeile "aktuellste Ausgabe"** — `v5-fa-latest` mit Datum (`v5-fa-date`, `--faint`) + Titel-Link (`v5-fa-latest-t`, navy/teal-hover).
6. **Archiv-Einstieg** — `v5-fa-archive` (sekundaerer Textlink zu allen Ausgaben, `--teal`).
7. **Primaerer CTA-Button** — `v5-fa-cta` (Pille, navy-Flaeche, weiss; fuehrt zur Reihe/zum Abo). Genau EIN Primaer-Button je Anker.

### 6.3 Reuse vor Neubau
- Wiederverwendete Tokens/Muster (keine neuen Werte): `--navy`, `--teal`, `--lblue`,
  `--muted`, `--faint`, `--line`; Section-Head `.v5-head`/`.v5-sub`; Cover-Behandlung
  wie `.v5-rs-cov` (object-fit cover, Radius); Pillen-Geometrie und Hover-Pfeil-Logik wie
  `.art-cta-btn` (`gap:.55em`, Pfeil `transform:translateX(4px)` on hover); Schatten- und
  Transition-Standards aus Abschnitt 1.5; Eyebrow-Regel aus Abschnitt 3.
- Nur wirklich neue Klassen (weil ein gleichwertiges, prominenteres 2er-Layout im
  Bestand fehlt): `v5-flagship`, `v5-fa-grid`, `v5-fa`, `v5-fa-cov`, `v5-fa-badge`,
  `v5-fa-body`, `v5-fa-title`, `v5-fa-sub`, `v5-fa-latest`, `v5-fa-date`,
  `v5-fa-latest-t`, `v5-fa-foot`, `v5-fa-archive`, `v5-fa-cta`.

### 6.4 Regeln fuer den Flagship-Anker
- Genau zwei Anker, visuell exakt gleichwertig. Kein dritter Anker in diesem Block
  (weitere Reihen gehoeren ins normale `.v5-research`-Band).
- Genau ein Primaer-CTA je Anker; Archiv-Einstieg ist sekundaerer Textlink, kein zweiter Button.
- Badge folgt der Label-Regel: keine Versalien, `letter-spacing .01-.02em`.
- Der dunkle Footer-Block je Anker nutzt die Navy-Flaeche; er ist das einzige zusaetzlich
  zulaessige dunkle Element ausserhalb von Hero/phead/CTA und dient der Abhebung von den
  Standardkarten.
- Keine bunten Badges, keine Icons ausser dem CTA-Pfeil, kein Diagramm im Cover.
- Texte (Headline, Subtitle, Badge-Wortlaut, Ausgaben-Titel) liefert die Redaktion —
  dieses Dokument legt nur Struktur, Klassen und Stil fest.

Vollstaendige Markup-/CSS-Spezifikation: siehe `COMPONENT_LIBRARY.html`, Abschnitt
"Flagship-Research-Anker". Den Block baut der `builder` nach dieser Spec in
`build/build_hub_v5.py` und auf die Subpage ein — nicht der Guardian.
