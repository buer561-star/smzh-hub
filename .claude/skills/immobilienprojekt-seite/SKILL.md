---
name: immobilienprojekt-seite
description: Baut eine neue Immobilienprojekt-/Referenzseite (Case-Page) für die smzh Real Estate Advisory (REA) – im Stil von Killwangen, Bremgarten, Küsnacht – und verlinkt sie sauber auf der REA-Hauptseite. Nutze diese Skill, sobald ein neues Immobilienprojekt als eigene Landingpage angelegt, eine bestehende Projektseite umgebaut oder auf der REA-Seite als Referenzprojekt eingebunden werden soll. Enthält Seitenstruktur, Design-Tokens, Investoren-Tonalität, Verlinkungs- und Deploy-Ablauf.
---

# Immobilienprojekt-Seite (REA Case-Page)

Diese Skill kapselt das etablierte Muster für eine **Immobilienprojekt-Seite** der
smzh **Real Estate Advisory** – die eigenständige Landingpage eines einzelnen
Projekts (Referenz/Case), plus die Einbindung auf der REA-Hauptseite.

> **Kanonische Vorlage:** `site/smzh.ch/de/killwangen/index.html`.
> Eine neue Projektseite entsteht **immer als Klon einer bestehenden** (Killwangen =
> Referenz), nicht auf der grünen Wiese. Struktur, Chrome (Header/Mega-Menü/Footer),
> Reveal-Animationen und CSS werden übernommen; getauscht wird **nur der Inhalt**.

Dies ist ein **eigenes Prototyp-System**, NICHT das smzhHub-V5-System. `DESIGN_CONTRACT.md`
und `PAGE_SCHEMA.md` im Repo-Root gelten für die `smzhub-*`-Seiten (Plus Jakarta Sans,
`--navy #03314B`). Die REA-Projektseiten liegen auf der geklonten **smzh.ch-Chrome**
(Circular XX, `--navy #07314C`). Verwechsle die beiden Systeme nicht.

---

## 0. Intake — Fragenkatalog & benötigte Files (VOR dem Bau, immer zuerst)

> **Ziel:** einmal alles einsammeln, dann die Seite in **einem Rutsch** befüllen.
> Startet ein neues Projekt (oder soll ein Platzhalter-Projekt wie Sonne/Küsnacht
> gefüllt werden), stelle dem Nutzer **diesen Katalog kompakt in EINER Nachricht**,
> nummeriert. Erst bauen, wenn A, B und F beantwortet sind (C/D/E/G darf ich aus A/B
> ausformulieren). **Fehlt eine Antwort → betroffene Sektion weglassen, nie als
> Platzhalter rendern** (harter Gate, §7). Offene Punkte kurz zurückmelden.
>
> **Ich kann keine lokalen Pfade / OneDrive öffnen** — Bilder **im Chat anhängen**
> oder ins Repo unter `site/cms.smzh.ch/uploads/` legen. Nie einen `C:\…`-Pfad annehmen.

**A. Stammdaten** → `facts`, Hero-Meta
1. Projektname (öffentlich, z. B. „Bremgarten, Drei Könige") + gewünschter Slug.
2. Adresse: Strasse Nr., PLZ, Ort, Kanton.
3. Ausgangslage in 1 Zeile (z. B. „denkmalgeschützte Altstadtliegenschaft").
4. Nutzung (Wohnen / Gewerbe / Gastronomie / Mischnutzung).
5. Einheiten konkret (z. B. „5 Mietwohnungen", „1 Restaurant inkl. Take-Away").
6. Eingriff (Neubau / Umbau / Kernsanierung / Totalsanierung; denkmalgerecht?).
7. Besonderheiten Ausbau (Bodenheizung, Lift, zusätzliche UG, Minergie …).
8. Status (in Projektierung / bewilligt / in Ausführung / realisiert).
9. Fertigstellung (Jahr). 10. Flächen (m², Grundstück/Entwicklung) — falls relevant.

**B. Investment-Story** → Hero-Claim, Wertschöpfungskette (`archsec`), `proof`
11. Ausgangslage/Problem: Was war unter Potenzial? (leerstehend, schwache Qualität, Nutzungsmix …)
12. Opportunität: Was hat smzh erkannt? 13. Wertstrategie: Was wurde konkret gemacht?
14. Ergebnis/Zielbild: Was entsteht?
15. Zwei Kennzahlen für die Wertachse: **Ausgangswert → Ergebnis**
    (z. B. „10 Bestandseinheiten → 58 Wohneinheiten" oder „1 denkmalgeschützte Liegenschaft → 5 Wohnungen + 1 Restaurant").

**C. Die 9 Wertstufen** → `phase`-Blöcke + Spine (§3b) — je Stufe stichwortartig genügt
Für **Objektzugang, Machbarkeit, Nutzungskonzept, Struktur, Bewilligung, Kapital,
Umsetzung, Vermietung, Exit** je: 16. Ausgangslage · 17. smzh-Entscheid (der Hebel) ·
18. Resultat (falls offen: „offen bis Fertigstellung"). Welche Stufen sind **Wertsprünge**?
> Stichworte reichen — den Fliesstext (Ausgangslage/smzh-Entscheid/Entscheidender Hebel/Resultat)
> formuliere ich aus. Unbekannte Stufen bekommen einen knappen, kanonischen Standardsatz.

**D. Das 4-Kreis-Wertsystem** → `comp` (§3c) — je Bereich 1 Satz + 1–2 Bullets
19. Strategische Immobilienberatung · 20. Projektentwicklung & Bauherrenvertretung ·
21. Finanzierungsberatung · 22. Transaktionsmanagement. **Auf den Punkt, was smzh tat.**

**E. Verlinkung & Karte** → `wref`, REA-Hauptseite
23. Welche **3** anderen Projekte in „Weitere Projekte" zeigen (max. 3)?
24. Neuer Standort? Pin-Koordinaten auf der Schweizer Karte (SVG viewBox `0 0 1000 643.7`)
    oder Ort nennen, den ich verorte.

**F. Bilder / Files** → verlangen (für die REA-Karte **nicht** optional)
25. **1× starkes Präsentationsbild** (Fassade/Lage/Innenausbau, fertiger Zustand) — für
    REA-Referenzkarte, Auswahl-Panel **und** Projekt-Hero. **KEIN Baustellenbild** (§6).
26. Optional: 2–4 **Galerie-/Karussell-Bilder** (Innenausbau/Prozess — Baustellenbilder hier ok).
27. Optional: Grundriss/Schema. Format: JPG/PNG, quer, ~1600 px+.

**G. Meta/SEO** → `<title>`, og/twitter, JSON-LD
28. SEO-Titel + 1-Satz-Description — oder ich generiere aus A/B (Tonalität §1).

---

## 1. Zielgruppe & Tonalität (verbindlich)

**Zielgruppe:** institutionelle und semiprofessionelle Investoren, Entwickler,
Eigentümer **grösserer** Immobilienpositionen. **NICHT** Privatvermögen, Familien­vermögen,
Erbschaft/Nachfolge.

**Verbotene Begriffe** (dürfen im REA-Eigencontent NICHT vorkommen):
`Gesamtvermögen`, `Familienvermögen`, `Familienbesitz`, `Unternehmerfamilien`,
`Nachfolge`, `Vermögensstruktur`, `ganzheitlich`, `massgeschneidert`, `A bis Z`,
`Methode` (als Marke), `in wenigen Minuten`, `Schnellbewertung` (als Substantiv-Marke),
generische `Werthebel`.

> Ausnahme: `Gesamtvermögen`/`massgeschneidert` tauchen im **globalen Mega-Menü/Footer**
> der geklonten smzh.ch-Chrome auf (Nav-Links `gesamtvermoegensanalyse`,
> `massgeschneiderte-versicherungsloesungen`). Das ist Original-Site-Chrome, kein
> REA-Eigencontent – hier **nicht** anfassen. Der Tonalitäts-Check gilt für den
> **selbst geschriebenen** Inhalt.

**Erwünschte Tonalität:** Investment Case, Ausgangslage, Potenzial, Struktur, Kapital,
Exit, Umsetzbarkeit, Marktgängigkeit, Ertrag, Risiko.

**Sprache:** Schweizer Hochdeutsch, durchgehend **„ss", niemals „ß"**.

**Labels:** „**Projekt**", nie „**Case**" als Label (Buttons, Eyebrows, Breadcrumbs,
E-Mail-Betreff). Einzige erlaubte Ausnahme: der feststehende Fachbegriff
**„Investment Case"** im Fliesstext (Investment-These), z. B. „Ein Bestand ist noch kein
Investment Case."

---

## 2. Seitenstruktur einer Projektseite (Block-Reihenfolge, normativ)

Alle Projektseiten teilen dasselbe Sektions-Skelett (Reihenfolge identisch; nur die
Zahl der `phase`-Blöcke variiert je nach Projekt). Jede Sektion ist `<section
class="…">` mit innen `<div class="wrap …">`.

| # | Sektion (`class`) | Funktion | Heading |
|---|---|---|---|
| 1 | `archsec` | Hero (Projektname + Claim) **+ Wertschöpfungskette**: Ausgangslage→Zielbild links, Spine der **kanonischen 9 Wertstufen** rechts (§3b) | **h1** (genau 1 pro Seite) |
| 2 | `facts` | Eckdaten-Band (Lage, Nutzung, Einheiten, Status …) — **Stil V5, §3a** | – |
| 3 | `proofband` | schmales Beleg-/Kontext-Band (Claim; optional grosses Bild-Karussell) | – |
| 4 | `cmap` | Kontext/Ausgangslage der Lage | h2 |
| 5 | `phase` ×**9** | die **9 kanonischen Wertstufen** (§3b); `phase--lever` = Wertsprung, letzte = `--ziel` | – |
| 6 | `proof` | „Was &lt;Projekt&gt; zeigt" (3 `pcard`) | h2 |
| 7 | `orch` | „Die Rolle von smzh" (Orchestrierung) | h2 |
| 8 | `comp` | **4-Kreis-Wertsystem** (§3c), projektspezifisch, **transparent (ohne Hintergrund)** | h2 |
| 9 | `rea-cta` (`id="kontakt"`) | heller **Entscheidungs-CTA** (§4), **VOR** „Weitere Projekte" | h2 |
| 10 | `wref` | „Weitere Projekte" — **genau 3** Referenzkarten (`rc`), **3-spaltig** | h3 |
| — | smzh-Footer | geklonte Chrome, unverändert | – |

Vor `archsec` und nach `wref` steht die geklonte Chrome (`firstRow`/`secondRow`
Header, Mega-Menü, Footer). **Nie** ein zweites `h1` einbauen.

**Entfernt (früher vorhanden, heute NICHT mehr aufnehmen):**
- `thesis` (dunkles Textband unter dem Bild-Karussell) — **weg**.
- `team` („Das Team hinter …") — **weg**; das Team wird zentral auf der REA-Hauptseite
  vorgestellt, nicht je Projektseite.
- `frame` (dunkler navy CTA-Block) — **ersetzt** durch den hellen `rea-cta` (§4).
- **Eyebrow-Kicker** vor Titeln (Hero-Breadcrumb „Projekt · …", Sektions-Labels
  wie „Die Ausgangslage" / „Was … zeigt" / „Die Rolle von smzh" **und** der
  Wertschöpfungsketten-Kicker `.wsa__head` „Die Wertschöpfungskette") — **alle weg**,
  konsistent mit der Startseite. Generell: keine kleinen Kicker-Titel oben links über
  Überschriften.

---

## 3a. Eckdaten-Band `facts` — Stil V5 (verbindlich, editorial)

Das Eckdaten-Band ist **nicht** das alte dunkle Vollbreiten-Band (`--navy-ink`,
full-bleed) — das wirkte zu ausreisserisch. Standard ist die **editoriale Variante V5**:
weiss, im Content eingefasst, jede Kennzahl mit feiner Teal-Akzentlinie oben.

Markup bleibt: `<section class="facts"><div class="facts__grid">` mit
`<div class="fact"><div class="k">Label</div><div class="v">Wert</div></div>` je Kennzahl.

Verbindliche CSS-Regeln:
```
.facts{background:#fff;color:var(--ink)}
.facts__grid{display:grid;grid-template-columns:repeat(4,1fr);max-width:1180px;margin:44px auto;padding:0 28px;gap:26px 24px}
.fact{padding:13px 0 0;border-top:2px solid var(--blue)}
.fact .k{font-size:11px;font-weight:700;letter-spacing:.09em;color:var(--muted);margin-bottom:6px}
.fact .v{font-size:17px;font-weight:700;line-height:1.25;overflow-wrap:break-word;hyphens:auto;color:var(--navy)}
```
Mobil (bestehender `@media`-Block): `.facts__grid{grid-template-columns:repeat(2,1fr)}`,
`.fact .v{font-size:16px}`. Labels **nicht** in Versalien setzen (Text wie „Standort").

---

## 3b. Die kanonischen 9 Wertstufen (verbindlich, site-weit identisch)

Die Wertachse ist **überall dieselbe 9er-Reihenfolge** – auf der REA-Startseite
(`.wsys`-Timeline) **und** auf jeder Projektseite (`.wsa__steps`-Spine + `phase`-Blöcke):

```
01 Objektzugang · 02 Machbarkeit · 03 Nutzungskonzept · 04 Struktur ·
05 Bewilligung · 06 Kapital · 07 Umsetzung · 08 Vermietung · 09 Exit
```

- **Keine** projektspezifischen Labels mehr (früher: Grundstück/Produkt/Substanz/
  Nutzungsmix/Potenzial/Entscheid/Ertrag). Immer diese 9 Begriffe, in dieser Folge.
- Jeder `phase`-Block: `data-phase="NN" data-label="<kanonisch>"`, `phase__num`,
  `phase__cat`, `phase__q` (Frage), `phase__aha`, dann `raster` mit **vier** Zeilen:
  `Ausgangslage` · `smzh-Entscheid` · `Entscheidender Hebel` (Label **nie** „Werthebel")
  · `Resultat`. Wertsprung-Stufen: `phase phase--lever` + `<div class="wertspr">Wertsprung</div>`;
  die Zielstufe (Exit/Ertrag): `wertspr wertspr--ziel">Zielstufe`.
- `data-phase`/`phase__num`/`wsa__nr` **fortlaufend 01–09** und mit der DOM-Reihenfolge
  konsistent (die Spine-/Scroll-JS liest `data-phase`).
- Die `comp`-Chips referenzieren Stufen als `<span>NN Label</span>` – bei Umbau
  mit-nummerieren.

---

## 3c. Das 4-Kreis-Wertsystem (`comp`, projektspezifisch)

Die `comp`-Sektion zeigt **nicht** mehr 4 statische Karten, sondern die **interaktive
4-Kreis-Grafik der Startseite** (`.wm`-Komponente, „Vier Leistungsbereiche"):

- Markup: `wmx__grid` = SVG links (`.wm-svg`, **verbatim** von der REA-Startseite
  kopieren, 4 `.wm-seg` mit `data-key` a/b/c/d) + `wmx__box` rechts (`#wmBox`, füllt
  `#wmK/#wmT/#wmD/#wmList` per JS). Klick auf einen Kreis rendert den Bereich.
- Die **4 Bereiche sind fix** (an die SVG-Icons gebunden), Reihenfolge/Farben:
  `a` Strategische Immobilienberatung `#07314C` · `b` Transaktionsmanagement `#6AA9D2` ·
  `c` Projektentwicklung & Bauherrenvertretung `#115A8A` · `d` Finanzierungsberatung `#3681B2`.
- **Inhalt pro Bereich ist projektspezifisch**: je `t` (kurzer Titel, was gemacht wurde),
  `d` (1 knapper Satz), `b` (1–2 Bullets). **Weniger blabla, auf den Punkt.**
- H2 kurz + **projektspezifischer Ein-Satz-Lead** (kein generisches „Drei/Vier
  deklarierte Beiträge"). **Sektion transparent**: `.comp{background:transparent;padding:64px 0}`
  (keine Hintergrundfarbe).

---

## 3. Design-Tokens (Prototyp-System der Projektseiten)

Im letzten `<style>`-Block der Seite (nach den `smzh-*`-Chrome-Styles) definiert:

```
--navy:   #07314C   /* Headlines, dunkle Flächen, CTA-Buttons (.frame__btn) */
--blue:   #3681B2   /* Akzent: Links, Eyebrows, Pfeile */
--ink:    #111827   /* Fliesstext */
--muted:  #5B6B7A   /* Sekundärtext, Beschreibungen, Rollen */
--paper:  #FBFCFD   /* heller Seitengrund */
--powder: #8FC4EB   /* helle Akzentfläche */
--sans:   "Circular XX","CircularXX","Hanken Grotesk",system-ui,… /* smzh-Brand-Font */
```

**Container:** `.wrap{width:100%;max-width:1180px;margin:0 auto;padding:0 28px}`.

**CTA-Button:** `.frame__btn` – navy Fläche, weisser Text, `font-weight:700`,
`font-size:16px`, `padding:16px 32px`, `border-radius:9px`. Die drei Buttons im
`.frame__ctas` sind **gleich breit** ("gliich dick").

**Reveal-Animation:** Elemente mit `class="reveal-el"` faden beim Scrollen ein
(IntersectionObserver-Skript ist Teil der geklonten Seite – beim Klonen mitnehmen).

**Radius/Schatten/Spacing** aus der Vorlage übernehmen; keine neuen Farben, keine
zweite Schriftfamilie, keine bunten Badges, keine dekorativen Icons (nur Pfeil `→`).

---

## 4. Der geteilte Entscheidungs-CTA (`.rea-cta`) – identisch auf allen Seiten

Alle Projektseiten **und** die REA-Hauptseite tragen denselben **hellen** CTA-Block
mit **drei gleich breiten** CTAs. Auf den Projektseiten steht er als
`<section class="rea-cta" id="kontakt">` **direkt vor** `wref` („Weitere Projekte").
Der frühere dunkle `frame`-Block ist **abgelöst** (nicht mehr verwenden).

| Button-Text | Ziel (relativ, Projektseite) |
|---|---|
| Projekt einordnen | `../projekt-einordnen/index.html` |
| Anlageprofil prüfen | `../anlageprofil/index.html` |
| Verkauf prüfen | `../liegenschaft-verkaufen/index.html` |

Fixe Inhalte des Blocks (identisch überall):
- H2: „Welche Entscheidung steht bei Ihrem Immobilienprojekt an?"
- Lead: „Ob Bestand, Entwicklung, Finanzierung, Vermietung oder Verkauf: Wir ordnen
  Ihre Ausgangslage ein und zeigen, welche nächsten Schritte für Struktur, Kapital,
  Umsetzung oder Exit zählen."
- (Keine Fussnote/Zielgruppen-Zeile mehr unter den CTAs.)

> **Stehende Regel (verbindlich):** Der CTA-Text ist **überall identisch** — Startseite
> (`.cta`) **und** alle Projektseiten (`.rea-cta`). Wird der CTA irgendwo geändert,
> **immer synchron auf ALLE** CTAs übertragen, ausser der Nutzer sagt ausdrücklich etwas
> anderes. Analog: „kein Flattern in der Mitte" — Lead-/Intro-Texte ohne enge `max-width`,
> volle Breite nutzen.

Der Block ist **selbsttragend gestylt** (eigener `<style>` mit fest verdrahteten
REA-Farbwerten `#03314B`/`#185E7F`, Hintergrund `#EEF6FC`), damit er unabhängig von
den Projekt-Tokens (`--navy #07314C`) **exakt** wie auf der Startseite rendert. Er
trägt `id="kontakt"`, damit der Nav-Link „Projekt einordnen lassen" (`href="#kontakt"`)
auflöst. **Nie** nur einen einzelnen CTA – immer die drei gleichgewichteten.

---

## 5. Neues Projekt anlegen – Ablauf

1. **Klonen:** `site/smzh.ch/de/killwangen/index.html` → neuer Slug
   `site/smzh.ch/de/<slug>/index.html`. Chrome, `<style>`, Reveal-Skript und
   Sektions-Skelett bleiben.
2. **Inhalt tauschen** je Sektion (§2) mit Investoren-Tonalität (§1). Projektbezogene
   Bilder als base64 einbetten (wie in der Vorlage) oder über `_next/image`-Pfade –
   analog zu bestehenden Projekten.
3. **Hero/Meta:** `h1`, `<title>`, `og:*`/`twitter:*`-Description und ggf. JSON-LD auf
   das neue Projekt setzen – **und dabei ebenfalls die Tonalitäts-Regeln einhalten**
   (die verbotenen Begriffe stecken oft auch in den Meta-Descriptions, nicht nur im
   sichtbaren Text).
4. **Keine Eyebrow-Kicker** vor Titeln (weder Hero-Breadcrumb noch Sektions-Labels) —
   entfernt (§2). Der Nav-Trail (`nav__tag` „Real Estate Advisory · Projekt <Ort>")
   in der Sticky-Nav bleibt; er ist kein Eyebrow.
5. **`wref`-Sektion:** **genau 3** Referenzkarten auf **andere** Projekte (nicht auf
   sich selbst), **3-spaltig** (`.wgrid{grid-template-columns:repeat(3,1fr)}`). Auf den
   bestehenden Projektseiten die neue Seite in deren `wref` gegenseitig ergänzen.
6. **E-Mail-CTAs:** mailto-Betreff „Projekt-Einordnung (<Ort>)" – ohne das Wort „Case".

---

## 6. Auf der REA-Hauptseite einbinden

`site/smzh.ch/de/real-estate-advisory/index.html`:

- **Referenzkarten-Grid (`.refs` / `.rc`):** neue Karte im Stil der bestehenden
  Karten (grösseres Bild `.rc__img`, Titel, Beschreibungstext, Button
  „**Projekt ansehen** →" via `.rc__go` → `../<slug>/index.html`). Karten sind
  **gleich gross** (flex `calc()`), Buttons unten via `margin-top:auto` gepinnt.
- **Bildwahl (verbindlich):** Das Bild der REA-Referenzkarte (`.rc__img`) **und**
  das Bild im Auswahl-Panel (`refsel__img`) müssen das Projekt **repräsentativ und
  attraktiv** zeigen (fertiger/hochwertiger Zustand, Fassade/Lage/Innenausbau) — das
  Bild verkauft den Case. **Niemals ein Baustellen-/Rohbaubild** als Karten- oder
  Panel-Bild verwenden. Baustellen-/Prozessbilder gehören höchstens in eine
  Galerie/Phasen-Sektion der Projektseite, nie in die REA-Übersicht. Gilt sinngemäss
  auch für das Hero-Bild (`archsec`) der Projektseite selbst.
- **Karten-Auswahlbox neben der Karte (`refsel`)** und Platzhalter haben **dieselbe
  Struktur** wie die Referenzkarten.
- Reihenfolge/Anzahl konsistent halten; „Weitere Projekte anzeigen" endet nach
  **max. 2 zusätzlichen Zeilen**, dann verschwindet der Button (keine endlose Ausgabe).

Die REA-Hauptseite nutzt einen **breiteren** Container (Tailwind-Scale bis
`max-width:1536px`) als die Projektseiten (`1180px`) – das ist bewusst so, weil die
REA-Seite gespiegelte Next.js-Sektionen enthält. Beim Kopieren von Karten-Markup
zwischen den Seiten die jeweilige Container-Breite beachten.

---

## 7. Verifikation vor dem Commit (Pflicht-Checks)

Aus `/home/user/smzh-hub` laufen lassen (Slug einsetzen):

```bash
P=site/smzh.ch/de/<slug>/index.html
# 1) verbotene Tonalität im Eigencontent (Treffer im Mega-Menü/Footer ignorieren)
for t in Familienvermögen Familienbesitz Unternehmerfamilie Nachfolge \
         Vermögensstruktur Eigentümerfamilie Familienprojekt Werthebel \
         ganzheitlich "in wenigen Minuten" Schnellbewertung; do
  echo "$t = $(grep -o "$t" "$P" | wc -l)"; done   # alle 0 im Eigencontent
# 2) SICHTBARE REDAKTIONS-PLATZHALTER — muss 0 sein (sonst BLOCKER, wird ausgeliefert!)
for t in "Inhalt fehlt" "Name offen" "Rolle offen" "Slot bewusst leer" "TODO" "Platzhalter"; do
  echo "PH $t = $(grep -o "$t" "$P" | wc -l)"; done
# 3) kein „ß“
grep -o 'ß' "$P" | wc -l          # muss 0 sein
# 4) kein „Case“ als Label (nur „Investment Case“ im Fliesstext erlaubt)
grep -o '· Case \|>Case ·\|Case ansehen\|Case Study\|(Case ' "$P"
# 5) genau ein h1
grep -oc '<h1' "$P"
# 6) interne Links auflösen (Python-Check aus §Audit nutzen)
```

> **Kritisch (aus Audit gelernt):** Bremgarten und Küsnacht wurden mit sichtbaren
> `.miss`-Badges („Inhalt fehlt") und leeren `.nm`/`.ro`-Team-Karten
> („Name offen / Rolle offen") deployt — diese Klassen sind **nicht** versteckt,
> sondern gestylt sichtbar. Ein leerer Slot wird **weggelassen**, nie als Platzhalter
> gerendert. Check 2 ist ein harter Gate vor jedem Commit.
>
> **`Werthebel`** ist als Feld-Label im Wertstufen-Detailtemplate (`.rk--hebel`) ein
> verbotener generischer Begriff — durch neutraleres Label ersetzen
> (z. B. „Entscheidender Hebel" / „smzh-Beitrag"), wirkt auf alle Projektseiten.

**Rendern/Screenshot** mit dem vorinstallierten Chromium (Playwright):

```js
const {chromium}=require('/opt/node22/lib/node_modules/playwright');
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
// file://$PWD/site/smzh.ch/de/<slug>/index.html laden, Sektionen prüfen/shooten
```

Das avendo-Embed („Schnelle Erstbewertung Ihrer Immobilie") ist ein Cross-Origin-iframe
auf `avendo.ch` und im Sandbox **blockiert** – dessen interne Darstellung lässt sich
lokal nicht verifizieren; nur am Live-Deploy prüfen.

---

## 8. Deploy (zwei-Branch-Ablauf)

Entwickelt wird auf `claude/branch-tree-verification-ojmemp`; deployt wird über
`claude/inspiring-dirac-2ioa4s` (GitHub-Pages-Workflow `.github/workflows/deploy-pages.yml`
triggert nur auf Push dieses Branches).

```bash
git add -A && git commit -m "…"          # Trailer: Co-Authored-By + Claude-Session
git push -u origin claude/branch-tree-verification-ojmemp
git branch -f claude/inspiring-dirac-2ioa4s <commit>
git push origin claude/inspiring-dirac-2ioa4s
```

**Bekannte Flakiness:** Der Pages-Deploy schlägt zeitweise mit
`syncing_files` → „Deployment failed, try again later." fehl (GitHub-seitig, nicht
inhaltlich). Der Upload-Step gelingt dabei, nur der finale Step „Deploy to GitHub
Pages" scheitert beim `syncing_files`-Polling. Nicht am Code suchen.
**Fix: immer ein frischer `workflow_dispatch`-Lauf** (`run_workflow` auf
`deploy-pages.yml`, ref = Deploy-Branch). **NICHT `rerun_failed_jobs`** benutzen —
der wiederholt im selben Run den Upload-Step und erzeugt ein **zweites** Artefakt
`github-pages`; der Deploy bricht dann mit „Multiple artifacts named 'github-pages'
were unexpectedly found" ab. Ein frischer Dispatch hat einen sauberen Artefakt-Space.
Nach grünem Lauf den Nutzer hart neu laden lassen (Cmd/Ctrl+Shift+R).

---

## 9. Definition of Done

- [ ] Intake (§0) beantwortet; Präsentationsbild vorhanden (kein Baustellenbild).
- [ ] Seite als Klon der Vorlage, Sektions-Skelett **nach §2** (kein `thesis`/`team`/
      `frame`; `rea-cta` vor `wref`; `comp` = 4-Kreis, transparent), genau **1 h1**.
- [ ] **Kanonische 9 Wertstufen** (§3b) in Reihenfolge Objektzugang→Exit — Spine,
      `phase`-Blöcke und `comp`-Chips fortlaufend 01–09.
- [ ] Investoren-Tonalität (§1); Tonalitäts-Grep **sauber** (auch in Meta-Tags:
      `<title>`, og/twitter-Description, JSON-LD — nicht nur sichtbarer Text).
- [ ] **Keine sichtbaren Platzhalter** (`Inhalt fehlt`, `Name offen`, `Rolle offen`) —
      harter Gate; leere Slots weglassen.
- [ ] Kein „ß"; kein „Case"-Label (nur „Investment Case" im Fliesstext); kein „Werthebel"
      (Hebel-Label = „Entscheidender Hebel"); **keine Eyebrow-Kicker** vor Titeln.
- [ ] Ein Begriff site-weit: **Anlageprofil** vs. Anlegerprofil, **ein** Titel-Trennzeichen.
- [ ] Heller `rea-cta` (§4, `id="kontakt"`) vor `wref`, drei gleich breite CTAs.
- [ ] `wref` = **genau 3** andere Projekte, 3-spaltig; bestehende Projekte gegenseitig ergänzt.
- [ ] 4-Kreis-`comp` (§3c) projektspezifisch + transparent; SVG rendert, 4 Kreise klickbar.
- [ ] Auf der REA-Hauptseite als gleich grosse Referenzkarte „Projekt ansehen" **und**
      als Pin auf der Karte eingebunden (richtiger `data-id`).
- [ ] Alle internen Links lösen auf; Screenshot geprüft; 0 Page-Errors.
- [ ] Auf beide Branches gepusht, Deploy grün (frischer `workflow_dispatch`, §8).
