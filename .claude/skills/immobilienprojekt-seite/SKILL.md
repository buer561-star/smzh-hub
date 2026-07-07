---
name: immobilienprojekt-seite
description: Baut oder überarbeitet eine Referenzprojekt-/Projektdetail-Seite der smzh Real Estate Advisory (REA) nach dem KILLWANGEN-STANDARD und bindet sie auf der REA-Hauptseite ein. Nutze diese Skill, sobald ein Immobilienprojekt als eigene Landingpage angelegt, eine bestehende Projektseite auf den Killwangen-Standard umgebaut oder auf der REA-Seite als Referenzprojekt eingebunden werden soll. Enthält den Fragebogen (Intake), die exakte Seitenstruktur, Design-Tokens, Hintergrund-Rhythmus, Investoren-Tonalität, Verlinkungs- und Deploy-Ablauf.
---

# Immobilienprojekt-Seite — der «Killwangen-Standard»

Diese Skill kapselt das verbindliche Muster für eine **Projektdetail-/Referenzseite** der
smzh **Real Estate Advisory** (REA). Der **kanonische, fertig ausgearbeitete Referenzfall
ist Killwangen** — *jede* andere Projektseite (Bremgarten Drei Könige, Bremgarten Sonne,
Küsnacht-Villa, Küsnacht 5 Eigentumswohnungen) hat **exakt dieselbe Struktur, denselben
Hintergrund-Rhythmus und dieselbe Tonalität**; nur der **Inhalt** ist projektspezifisch.

> **Kanonische Vorlage:** `site/smzh.ch/de/killwangen/index.html`.
> Neue oder umzubauende Seiten werden **immer an Killwangen ausgerichtet** — Struktur,
> Chrome (Header/Mega-Menü/Footer), Reveal-Animationen und CSS werden übernommen;
> getauscht wird **nur der Inhalt**.

Dies ist ein **eigenes Prototyp-System**, NICHT das smzhHub-V5-System. `DESIGN_CONTRACT.md`
und `PAGE_SCHEMA.md` im Repo-Root gelten für die `smzhub-*`-Seiten (Plus Jakarta Sans,
`--navy #03314B`). Die REA-Projektseiten liegen auf der geklonten **smzh.ch-Chrome**
(Circular XX, `--navy #07314C`). Verwechsle die beiden Systeme nicht.

---

## 0. Fragebogen (Intake) — VOR dem Bau, immer zuerst

> **Ziel:** einmal alles einsammeln, dann die Seite **eloquent in einem Rutsch** befüllen.
> Stelle dem Nutzer diesen Fragebogen **kompakt, nummeriert, in EINER Nachricht**. Der
> Nutzer liefert Kontext (Stichworte genügen) — den **Fliesstext formuliere ich aus**
> (Tonalität §1). Erst bauen, wenn A, B, C und F beantwortet sind. **Fehlt eine Antwort
> → betroffene Sektion weglassen, nie als Platzhalter rendern** (harter Gate §7).
>
> **Ich kann keine lokalen Pfade / OneDrive öffnen** — Bilder **im Chat anhängen** oder ins
> Repo unter `site/cms.smzh.ch/uploads/` legen. Nie einen `C:\…`-Pfad annehmen.

**A · Stammdaten** → `facts` («Das Projekt in Zahlen»), Hero-Meta
1. Projektname (öffentlich) + gewünschter Slug.
2. Adresse: Strasse Nr., PLZ, Ort, Kanton.
3. Nutzung (Wohnen / Gewerbe / Gastronomie / Mischnutzung).
4. Einheiten konkret (z. B. «58 Wohneinheiten», «5 Mietwohnungen + 1 Restaurant»).
5. Eingriff (Neubau / Umbau / Kernsanierung / Totalsanierung; denkmalgerecht?).
6. Ausbau-Besonderheiten (Bodenheizung, Lift, zusätzliche UG, Minergie …).
7. Status (in Projektierung / bewilligt / in Ausführung / realisiert) + Fertigstellung (Jahr).
8. Käuferschaft & Transaktionsart, falls verkauft (z. B. «Schweizer Pensionskasse, Asset Deal»).
9. Dauer (Objektzugang → Übergabe), falls bekannt.

**B · Die drei Boxen (archsec)** → Ausgangslage · Herausforderung · Ergebnis (§3)
10. **Ausgangslage:** Kennzahl + 1 Satz (z. B. «10 Bestandseinheiten — kleinteilige Nutzung …»).
11. **Herausforderung:** was hätte das Projekt stoppen können? (Auflagen, Lage, Substanz, Risiken)
12. **Ergebnis:** Kennzahl + 1 Satz (z. B. «58 neue Wohneinheiten — institutionell investierbar …»).
    → Die Wertachse zeigt aus diesen beiden Kennzahlen den Sprung **Ausgangswert → Ergebnis**.

**C · Die 9 Wertstufen (phases)** → §3b — je Stufe Stichworte genügen
Für **Objektzugang · Machbarkeit · Nutzungskonzept · Struktur · Bewilligung · Kapital ·
Umsetzung · Vermietung · Exit** je:
13. Ausgangslage der Stufe · 14. **smzh-Entscheid** · 15. **Werthebel = die konkret
    ausgeführte Massnahme, die Wert/Finanzierbarkeit/Umsetzbarkeit/Ertrag/Verkaufbarkeit
    erhöht hat** (KEINE Admin-/Vorbereitungs-/Dokumentationstätigkeit!) · 16. Resultat.
17. Welche Stufen sind **Wertsprünge**? (Killwangen: 01, 03, 05, 06, 09.)

**D · Kontext der Lage (cmap)** → «Eine Lage, die viele als Problem gesehen hätten» o. ä.
18. Standort-Story in 2–3 Sätzen: was macht die Lage schwierig **und** wertvoll?

**E · Verlinkung & Karte** → `wref`, REA-Hauptseite
19. Welche **3** anderen Projekte in «Weitere Projekte» zeigen (genau 3)?
20. Pin-Koordinaten / Ort für die Schweizer Karte auf der REA-Hauptseite.

**F · Bilder / Files** → verlangen (für die REA-Karte **nicht** optional)
21. **1× starkes Präsentationsbild** — **fertiger Zustand ODER Visualisierung/Rendering.
    NIEMALS Baustelle/Rohbau** (§6). Für REA-Referenzkarte, Auswahl-Panel **und** Projekt-Hero.
22. Optional: 2–4 Galerie-/Karussell-Bilder (Innenausbau/Prozess — Baustellenbilder hier ok).

**G · Meta/SEO** → `<title>`, og/twitter, JSON-LD
23. SEO-Titel + 1-Satz-Description — oder ich generiere aus A/B (Tonalität §1).

---

## 1. Zielgruppe & Tonalität (verbindlich)

**Zielgruppe:** institutionelle und semiprofessionelle Investoren, Entwickler, Eigentümer
**grösserer** Immobilienpositionen. **NICHT** Privat-/Familienvermögen, Erbschaft/Nachfolge.

**Sprache:** präzise, sachlich, projektbezogen; Schweizer Hochdeutsch, durchgehend **«ss»,
niemals «ß»**. smzh **klein**. Keine Floskeln (`ganzheitlich`, `massgeschneidert`,
`Ihr Partner`, `innovativ`, `Potenziale entfalten`, `Weitblick`, `A bis Z`).

**Aktiv-Prinzip (Phasen):** Die 9 Schritte sind aus smzh-Sicht als **ausgeführte Handlung**
formuliert («Wir sicherten …», «Wir schufen …», «Wir führten …»), nicht als Frage/Passiv.
**Resultat** immer als Ergebnis dieser Handlung.

**Werthebel-Prinzip (hart):** Der «Werthebel» jeder Stufe ist **echte Execution** — was
konkret getan wurde, um Wert, Finanzierbarkeit, Umsetzbarkeit, Ertrag oder Verkaufbarkeit
zu erhöhen. **«Datenraum vorbereitet» ist kein Werthebel** (nur Verkaufsinfrastruktur),
sondern z. B. «Vermietung stabilisiert, Objektqualität belegt, Käuferlogik geschärft».

**Labels:** «**Projekt**», nie «**Case**» als Label. Das Wort «Case» **gar nicht** verwenden.

---

## 2. Seitenstruktur (Killwangen-Standard, normativ)

Alle Projektseiten teilen **dieses** Sektions-Skelett und **diesen Hintergrund-Rhythmus**.
Jede Sektion ist `<section class="…">` mit innen `<div class="wrap …">`.

| # | Sektion (`class`) | Hintergrund | Funktion | Heading |
|---|---|---|---|---|
| 1 | `archsec` | **hell** (`--paper`) | Hero-Titel **+ 3 Boxen** (Ausgangslage·Herausforderung·Ergebnis) **+ Wertachse** (§3) | **h1** (genau 1) |
| 2 | `facts` | **weiss** | Eckdaten, mit Zwischentitel **«Das Projekt in Zahlen.»** (§3a) | – |
| 3 | `proofband` | **navy** | Beleg-Band: grosser Claim + **grosses Bild-Karussell** (2× Aussen, dann Innenräume — §3f) | – |
| 4 | `cmap` | **hell** (`--paper`) | Herausforderung der Lage: **Volltext (h2+p, volle Breite) + Karussell darunter** (§3f), **kein** rechtes Einzelbild | h2 |
| 5 | `proof` | **hell** (`--paper`) | «Wert entsteht selten linear …» — 3 `pcard` (Intro zum Wertverlauf) | h2 |
| 6 | `phases` (`main.phases`) ⊃ `phase` ×**9** | **hell** (`--paper`) | die **9 Wertstufen** (§3b), Titel **«So wurde aus Potenzial ein umsetzbares Projekt.»** | (Sub-Titel) |
| 7 | `orch` | **navy** | «Eine Stelle, die den roten Faden hält» — Rolle smzh, Karte mit **smzh-Logo** (§3d) | h2 |
| 8 | `rea-cta` (`id="kontakt"`) | hellblau | Entscheidungs-CTA (§4), **VOR** «Weitere Projekte», **direkt an `orch` anschliessend** | h2 |
| 9 | `wref` | hell | «Weitere Projekte» — **genau 3** Referenzkarten, 3-spaltig | h3 |

**Hintergrund-Rhythmus (verbindlich):** Dunkel = **Statement/emotionaler Beat**
(Hero, `proofband`, `orch`); Hell = **detaillierter Inhalt** (`archsec`, `facts`, `cmap`,
`proof`, `phases` — ein **zusammenhängender heller Lauf**, damit `proof`+`phases` als ein
Block lesen). **Kein** willkürliches Hell/Dunkel-Wechseln Sektion für Sektion.

**Reihenfolge = Erzählbogen:** Hero → Summary (`archsec`+`facts`) → Bilder (`proofband`) →
Herausforderung (`cmap`) → Wertverlauf (`proof`+`phases`) → Rolle smzh (`orch`) → CTA.

**Entfernt / heute NICHT mehr aufnehmen:**
- `comp` (4-Kreis-Wertsystem) — **komplett weg** (inkl. zugehörigem `#wmBox`-Script).
- `thesis`, `team`, `frame` — weg (Team steht zentral auf der REA-Hauptseite).
- **Eyebrow-/Kicker-Titel** über Überschriften (auch `.wsa__head`) — alle weg.
- Keine **Grossbuchstaben-Labels** (kein `text-transform:uppercase` an Box-/Fakten-Labels).

**Titelgrössen (vereinheitlicht):** Sektions-H2/Hero-Titel `clamp(24px,3.4vw,38px)`;
Phasen-Sub-Titel `clamp(20px,2.6vw,26px)`. Der geteilte `rea-cta` behält seine eigene Grösse.

**TEXT IMMER VON LINKS NACH RECHTS — EGAL WO (hart, verbindlich):** Titel **UND** Fliesstext
nutzen die **volle Container-Breite** und laufen von links nach rechts. **NIE eine enge
`max-width` an Überschriften oder Absätzen** (kein `max-width:48ch`, kein `…ch`/schmales `px`),
die Text in eine **schmale, links «abgehackte» Spalte** zwingt. In Volltext-Sektionen (z. B.
`cmap`) hat `p` **keine** `max-width`. (Ausnahme nur echte Mehrspalten-Karten wie `pcard`, wo
die Kartenbreite die Zeile bestimmt.) Beim Klonen/Anpassen solche `max-width` an Textknoten aktiv entfernen.

---

## 3. `archsec` — 3 Boxen + Wertachse (Variante B, verbindlich)

Aufbau innerhalb `archsec > .wrap`:

1. **Kein archsec-Titel** — die 3 Boxen beginnen **direkt** (kein `.wsa__lead`/`.wsa__intro`).
   Der **Projektname steht im Hero-h1** (`<header class="hero">`) im **Format «Projektname: <Titel>»**
   (z. B. «Killwangen AG, 2 Mehrfamilienhäuser: Vom Grundstück zur Kapitalanlage.»,
   «Bremgarten AG, Drei Könige: Aus historischer Substanz wird belastbarer Ertrag.»).
   **Umbruch:** Der Projektname steht auf einer **eigenen Zeile** über dem Titel — Markup
   `<h1><span class="hero__name">Projektname:</span>Titel</h1>` mit `.hero__name{display:block}`.
   Der Name hat **dieselbe Grösse/Farbe/Gewichtung wie der Titel** (KEIN kleiner Eyebrow/Kicker,
   nicht powderfarben verkleinern) — nur der Zeilenumbruch nach dem Doppelpunkt trennt Name und Titel.
   **Projektname = «Gemeinde Kantonskürzel[, Objektname]»** — immer Gemeinde + Kantonskürzel
   (Killwangen AG, Bremgarten AG, Küsnacht ZH), und falls das Objekt einen Namen/eine Kurzbe-
   schreibung hat, danach mit Komma (…, Drei Könige / …, Sonne / …, Villa / …, 2 Mehrfamilienhäuser).
   Dieser **exakt gleiche Projektname** steht überall gleich: Hero-h1, `<title>`, die `wref`-Karten
   auf den anderen Projektseiten, die `rc`-Referenzkarten und die Karten-Pins auf `real-estate-advisory`.
2. **Triptychon `.vtrip`** — drei gleich hohe Boxen nebeneinander:
   - `.vbox.vbox--aus` (rosé `#FBF4F9`/`#EAD4E5`): Label «Ausgangslage» · grosse Kennzahl · Einheit · 1 Satz.
   - `.vbox.vbox--her` (amber `#FFF7EE`/`#F0DEC4`): Label «Herausforderung» · 1–2 Sätze (was hätte stoppen können).
   - `.vbox.vbox--erg` (navy): Label «Ergebnis» · grosse Kennzahl · Einheit · 1 Satz.
   - Box-Labels **normale Schreibweise** (kein Uppercase), `letter-spacing:.14em`.
3. **Achsen-Titel** `.vaxis__t` = **«Die grössten Werthebel bei <Ort>.»**
4. **Wertachse `.vaxis`** — horizontale Linie mit **9 Knoten** (`.vnode`), nur Nummer + Name;
   die **Wertsprung-Stufen** (`.vnode--ws`, Killwangen 01/03/05/06/09) sind gefüllt/blau
   hervorgehoben, die übrigen ruhig. **Kein Fliesstext/Punchline in der Achse, kein Kicker.**

Danach folgt `facts` mit Zwischentitel **«Das Projekt in Zahlen.»** (`.facts__t`) und
etwas Luft (nicht «zerquetscht»).

Referenz-CSS-Klassen (aus Killwangen übernehmen): `.vtrip .vbox .vbox__k/.vbox__big/.vbox__u/.vbox__tx`,
`.vaxis .vaxis__line .vnode .vnode__d/.vnode__n/.vnode__m`, `.vaxis__t`, `.facts__t`.

---

## 3a. Eckdaten-Band `facts` (editorial V5)

Weiss, im Content eingefasst, jede Kennzahl mit feiner blauer Akzentlinie oben; **mit
Zwischentitel** «Das Projekt in Zahlen.». Markup: `.facts__t` + `.facts__grid` mit
`.fact > .k/.v`. Labels **nicht** in Versalien. Referenz-CSS aus Killwangen.

---

## 3b. Die 9 Wertstufen `phases` (verbindlich, site-weit identisch)

Immer diese 9er-Folge, fortlaufend 01–09:
```
01 Objektzugang · 02 Machbarkeit · 03 Nutzungskonzept · 04 Struktur ·
05 Bewilligung · 06 Kapital · 07 Umsetzung · 08 Vermietung · 09 Exit
```
- Wrapper `main.phases > .wrap`, mit **Sub-Titel `.phases__t`** «So wurde aus Potenzial ein
  umsetzbares Projekt.» (projektadaptierbar), darüber die Spine/Cursor-JS.
- Jeder `phase`-Block: `data-phase="NN" data-label="…"`, `phase__num`, `phase__cat`,
  `phase__q` (**Aktiv-Satz «Wir …»**, kein Frage/Passiv), `phase__aha`, dann `raster` mit
  **vier** Zeilen: `Ausgangslage` · `smzh-Entscheid` · **`Werthebel`** (konkrete Handlung, §1)
  · `Resultat`. Wertsprung: `phase phase--lever` + `<div class="wertspr">Wertsprung</div>`.
- `data-phase`/`phase__num` konsistent mit DOM-Reihenfolge (Spine-/Scroll-JS liest `data-phase`).

## 3c. `proof` — «Wert entsteht selten linear» (Intro zum Wertverlauf)

Steht **direkt vor `phases`**, **heller** Hintergrund (`--paper`, gleiche Farbe wie `phases`,
damit beide als ein Block lesen). 3 `pcard` (weisse Karten, blaue Icon-Box, navy h3, muted
Text): kurze, konkrete Sätze, **wenig AI-Sprache**. Killwangen-Karten: «Wert entsteht nicht
linear» · «Ein Grundstück hat mehrere Werte» · «Der Exit wird früh vorbereitet».

## 3d. `orch` — Rolle smzh (Statement, navy)

«Eine Stelle, die den roten Faden hält.» Links Aussage + Lead, rechts Karte `.role__card`
mit den zentralen Schnittstellen (Markt & Produkt · Planung & Bewilligung · Kapital & Banken
· Vermietung & Exit) + Claim «Nicht jede Aufgabe selbst. Aber jede Schnittstelle im Blick.».
- **Wo «smzh» als Wortmarke steht, das echte Logo verwenden**, nicht Text: `.role__logo`
  = `brand__logo`-Data-URI (aus der geklonten Chrome) mit `filter:brightness(0) invert(1)`
  (weiss auf navy). Gilt sinngemäss überall, wo die Marke als Logo gemeint ist (nicht im Fliesstext).
- Oben etwas Luft (`padding-top`), unten **nur so viel Abstand, dass die Karte den hellen
  `rea-cta` nicht berührt** — keine grosse Lücke, keine Kollision.

---

## 3e. Design-Tokens (Prototyp-System der Projektseiten)

```
--navy:#07314C  --navy2:#041F32  --blue:#3681B2  --powder:#BFE0F5
--mauve:#8A5A80  --ink:#16222E  --muted:#5B6B7A  --line:#E1E9F0  --paper:#FBFCFD
--sans:"Circular XX",…   /* smzh-Brand-Font */
```
Container `.wrap{max-width:1180px;margin:0 auto;padding:0 28px}`. Reveal-Elemente
(`reveal-el`) faden per IntersectionObserver ein (beim Klonen mitnehmen). Keine neuen
Farben, keine zweite Schriftfamilie, keine bunten Badges, nur Pfeil `→` als Icon.

---

## 3f. Bild-Karussells (proofband + cmap) — Komponente, Ausschnitt, Pipeline

Beide Karussells nutzen **dieselbe `.carousel`-Komponente**; das JS initialisiert per
`document.querySelectorAll('.carousel')` **alle** Karussells der Seite (ein zweites Karussell
funktioniert automatisch). Aufbau:
- `<figure class="carousel reveal-el" data-caps="Cap1||Cap2||…">` — **eine Caption je REALEM
  Slide**, mit `||` getrennt.
- `.carousel__count` = «1 / N», **N = Anzahl realer Slides** (NICHT die vom JS erzeugten Clone-Slides).
- `.carousel__track` mit `.carousel__slide > img.carousel__img`, danach Prev/Next-Buttons,
  `.carousel__dots`, `.carousel__cap` (Startwert = Cap1).
- Das JS klont beim Init ersten/letzten Slide (Endlos-Loop) → im DOM erscheinen **N+2** Slides
  und die Spur startet auf `translateX(-1 Slide)`. **Beim Hinzufügen/Entfernen von Slides IMMER
  `data-caps`, `count /N` und `.carousel__cap` gemeinsam nachziehen**, sonst laufen Bild, Caption
  und Zähler auseinander. (Zum Prüfen die Track-Transform NICHT per `*{transform:none}` überschreiben
  — das zeigt sonst den Clone-Slide.)

**Proofband-Karussell (gross, navy):** Reihenfolge fix (§6): 2× Aussen, dann Terrasse (falls),
Küche, Wohnzimmer, Schlafzimmer, Bad. **Slide 1 = Hauptbild** (= Hero/REA-Karte/wref).

**cmap-Karussell (hell):** **kein** rechtes Einzelbild — der Text (h2 + p) läuft **volle Breite**,
darunter ein **eigenes** Karussell mit den **Herausforderungs-/Denkmal-Bildern** (freigelegte
Substanz, Bruchsteinmauerwerk, Gebälk, Treppen, Baustelle). Wrapper wie Killwangen:
`<div class="wrap" style="margin-top:36px"><figure class="carousel …">…</figure></div>`.

**Fenstergrösse = wie Killwangen (verbindlich):** Das Karussell-«Fenster» ist **gleich gross
wie bei Killwangen** — **volle Container-Breite**, Basishöhe `.carousel__img{height:clamp(280px,40vw,440px)}`
(proofband höher). **Das Karussell NICHT verschmälern** (kein `max-width` am `.carousel`, nicht
zentrieren). Beschnitt der ~3:2-Fotos wird **ausschliesslich über `object-position`** gesteuert,
nicht über die Rahmengrösse: heikle/**Hochformat-Bilder** mit `style="object-position:center <Y>%"`
so ausrichten, dass das bildwichtige Motiv (z. B. das Bruchsteinmauerwerk) im Ausschnitt bleibt.

**Bild-Pipeline (Google Drive):** Web-Grössen über den Thumbnail-Endpoint
`https://drive.google.com/thumbnail?id=<ID>&sz=w<Breite>` ziehen — **Hero `w1800`**,
**Karussell-Slides `w1200`**, **Karten (`rc__img`/`wref`) `w900`** — dann als Base64 einbetten.
Bilder inhaltlich der Caption zuordnen (Kontaktabzug rendern, visuell matchen), nicht raten.

---

## 4. Geteilter Entscheidungs-CTA (`.rea-cta`) — identisch überall

Heller CTA-Block, **drei gleich breite** CTAs, `<section class="rea-cta" id="kontakt">`
**direkt vor** `wref` (und auf der Projektseite **direkt an `orch` anschliessend**, ohne
grosse Lücke). Selbsttragend gestylt (feste REA-Farben `#03314B`/`#185E7F`, BG `#EEF6FC`).

- H2: «Welche Entscheidung steht bei Ihrem Immobilienprojekt an?»
- Lead: «Ob Bestand, Entwicklung, Finanzierung, Vermietung oder Verkauf: Wir ordnen Ihre
  Ausgangslage ein und zeigen, welche nächsten Schritte für Struktur, Kapital, Umsetzung
  oder Exit zählen.»
- Buttons → `../projekt-einordnen/`, `../anlageprofil/`, `../liegenschaft-verkaufen/`.

> **Stehende Regel:** Der CTA-Text ist **überall identisch** (Startseite `.cta` **und** alle
> `.rea-cta`). Änderung → **immer synchron auf ALLE** übertragen, ausser ausdrücklich anders.

---

## 5. Neues / umzubauendes Projekt — Ablauf

1. **Fragebogen (§0)** stellen und Antworten abwarten (mind. A, B, C, F).
2. **Klonen/Angleichen an Killwangen:** Struktur, Chrome, `<style>`, Reveal-Skript,
   Sektions-Skelett **nach §2** übernehmen; nur Inhalt tauschen.
3. **Inhalt befüllen** je Sektion mit Investoren-Tonalität (§1): 3 Boxen (§3), Wertachse,
   `facts`, `proofband`, `cmap`, 9 Phasen aktiv (§3b), `orch` mit Logo (§3d).
4. **Hero/Meta:** `h1`, `<title>`, og/twitter, JSON-LD — Tonalität auch hier einhalten.
5. **`wref`:** genau 3 andere Projekte, 3-spaltig; bestehende Seiten gegenseitig ergänzen.
6. **REA-Hauptseite (§6):** Referenzkarte + Karten-Pin einbinden — **Präsentationsbild
   (fertig/Visualisierung), nie Baustelle**.

---

## 6. REA-Hauptseite & Bildwahl (verbindlich)

`site/smzh.ch/de/real-estate-advisory/index.html`: neue Karte im Stil der bestehenden
(`.rc__img`, Titel, Text, «Projekt ansehen →» → `../<slug>/`), Karten gleich gross, plus
Karten-Pin (richtiger `data-id`).

**Bildregeln (hart):**
- **Hauptbild = immer eine Aussenaufnahme** (Fassade/Aussen). Gilt für das Projekt-Hero,
  die REA-Referenzkarte (`.rc__img`) **und** das Auswahl-Panel (`refsel__img`). **Nie** ein
  Innenraum- oder Baustellen-/Rohbaubild als Hauptbild; alternativ eine Aussen-Visualisierung/
  Rendering. Gibt es keine Aussenaufnahme → beim Nutzer verlangen, nicht ersatzweise ein
  Innenbild als Hauptbild nehmen.
- **Grosses Karussell (proofband) — feste Reihenfolge:** 2× Aussen, dann Terrasse (falls
  vorhanden), Küche, Wohnzimmer, Schlafzimmer, Bad. Mechanik/Ausschnitt → §3f.
- **`cmap` = eigenes Karussell unter dem Volltext** (kein rechtes Einzelbild): die eher
  **prozesshaften/Baustellen**-Fotos — bzw. bei denkmalgeschützten Objekten (z. B. Bremgarten)
  die Bilder, die die **historische Substanz / freigelegte Holzelemente / Bruchsteinmauerwerk**
  zeigen. Rahmen ans Foto-Format angleichen (§3f), damit nichts stark beschnitten wird.

---

## 7. Verifikation vor dem Commit (Pflicht-Checks)

```bash
P=site/smzh.ch/de/<slug>/index.html
grep -o 'ß' "$P" | wc -l                 # 0
grep -o 'Case' "$P" | wc -l              # 0 (Wort gar nicht verwenden)
for t in "Inhalt fehlt" "Name offen" "Rolle offen" "TODO" "Platzhalter"; do
  echo "PH $t = $(grep -o "$t" "$P" | wc -l)"; done   # alle 0 (harter Gate)
grep -oc '<h1' "$P"                       # genau 1
# Werthebel-Review: jede .rv--hebel-Zeile = konkrete ausgeführte Massnahme, keine Admin/Doku
```
Sichtbare Redaktions-Platzhalter (`.miss` «Inhalt fehlt», leere Team-Slots) sind ein
**Blocker** — leere Slots weglassen, nie rendern. Rendern/Screenshot mit vorinstalliertem
Chromium (`/opt/pw-browsers/chromium-1194/chrome-linux/chrome` via
`/opt/node22/lib/node_modules/playwright`); `reveal-el` zum Prüfen sichtbar schalten
(`.reveal-el{opacity:1!important;transform:none!important}`). Das avendo-Embed ist ein
Cross-Origin-iframe und lokal nicht prüfbar.

---

## 8. Deploy (zwei-Branch-Ablauf)

Entwickelt wird auf `claude/branch-tree-verification-ojmemp`; deployt über
`claude/inspiring-dirac-2ioa4s` (GitHub-Pages-Workflow `.github/workflows/deploy-pages.yml`).

```bash
git add -A && git commit -m "…"          # Trailer: Co-Authored-By + Claude-Session
git push -u origin claude/branch-tree-verification-ojmemp
git checkout claude/inspiring-dirac-2ioa4s && git merge --ff-only claude/branch-tree-verification-ojmemp
git push -u origin claude/inspiring-dirac-2ioa4s && git checkout claude/branch-tree-verification-ojmemp
```
Danach **frischer `workflow_dispatch`** (`run_workflow` auf `deploy-pages.yml`, ref =
Deploy-Branch). **NIE `rerun_failed_jobs`** (erzeugt ein zweites `github-pages`-Artefakt →
«Multiple artifacts named 'github-pages'»). Bei `syncing_files`-Flakiness: neuer Dispatch,
nicht am Code suchen. Nach grünem Lauf hart neu laden lassen (Cmd/Ctrl+Shift+R).

---

## 9. Definition of Done

- [ ] Fragebogen (§0) beantwortet; Präsentationsbild fertig/Visualisierung (kein Baustellenbild).
- [ ] Struktur **exakt nach §2** (archsec = 3 Boxen + Wertachse; `proof` vor `phases`;
      kein `comp`/`thesis`/`team`/`frame`; `rea-cta` direkt an `orch`), genau **1 h1**.
- [ ] Hintergrund-Rhythmus §2 (heller Lauf archsec→phases; navy nur Hero/proofband/orch).
- [ ] 3 Boxen (Ausgangslage·Herausforderung·Ergebnis) + Achsen-Titel «Die grössten Werthebel …».
- [ ] Hero-h1: Projektname auf **eigener Zeile** (`.hero__name`, gleiche Grösse/Farbe wie Titel),
      Name-Format «Gemeinde Kantonskürzel[, Objektname]» überall identisch (Hero/`<title>`/wref/rc/Pins).
- [ ] `facts` mit Zwischentitel «Das Projekt in Zahlen.»; Labels normal (kein Uppercase);
      Zahlen in der Fakten-Tabelle als Ziffer, im Fliesstext ausgeschrieben.
- [ ] `cmap` = Volltext (volle Breite) + **Karussell darunter** (kein rechtes Einzelbild).
- [ ] Bild-Karussells (§3f): `data-caps`, `count /N` und `.carousel__cap` konsistent; Slide 1 proofband
      = Hauptbild; Rahmen ans Foto-Format angeglichen (kein starker Beschnitt), Hochformat via `object-position`.
- [ ] 9 Wertstufen aktiv («Wir …»); **jeder Werthebel = konkrete ausgeführte Massnahme** (§1).
- [ ] `orch`: **smzh-Logo** statt Text, Karte berührt den CTA nicht (keine Lücke, keine Kollision).
- [ ] Tonalität §1; kein «ß»; kein «Case»; smzh klein; keine Kicker/Uppercase-Labels.
- [ ] Titelgrössen vereinheitlicht (§2); Titel volle Breite.
- [ ] Heller `rea-cta` (§4, `id="kontakt"`) vor `wref`; `wref` = genau 3 andere Projekte, 3-spaltig.
- [ ] Auf REA-Hauptseite als gleich grosse Referenzkarte + Karten-Pin (Bildregel §6).
- [ ] Screenshot geprüft, interne Links lösen auf; auf beide Branches gepusht, Deploy grün (§8).
