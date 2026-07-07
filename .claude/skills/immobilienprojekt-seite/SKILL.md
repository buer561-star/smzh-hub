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

**C · Die Wertstufen (phases)** → §3b/§1b — je Stufe Stichworte genügen; **Archetyp (§1b) zuerst
bestimmen** (er legt Phasenzahl, Werthebel-Kandidaten und ob 09 Exit oder 08 Zielstufe fest).
Grundfolge **Objektzugang · Machbarkeit · Nutzungskonzept · Struktur · Bewilligung · Kapital ·
Umsetzung · Vermietung/Verkauf [· Exit]** je:
13. Ausgangslage der Stufe · 14. **smzh-Entscheid** · 15. **Werthebel = die konkret
    ausgeführte Massnahme, die Wert/Finanzierbarkeit/Umsetzbarkeit/Ertrag/Verkaufbarkeit
    erhöht hat** (KEINE Admin-/Vorbereitungs-/Dokumentationstätigkeit!) · 16. Resultat.
17. Welche Stufen sind **Wertsprünge**? (projektspezifisch, §1b — nur echte Hebel; Achse ↔ Phasen-Badges identisch).

**D · Kontext der Lage (cmap)** → «Eine Lage, die viele als Problem gesehen hätten» o. ä.
18. Standort-Story in 2–3 Sätzen: was macht die Lage schwierig **und** wertvoll?

**E · Verlinkung & Karte** → `wref`, REA-Hauptseite
19. Welche **3** anderen Projekte in «Weitere Referenzobjekte» zeigen (genau 3)?
20. Pin-Koordinaten / Ort für die Schweizer Karte auf der REA-Hauptseite.

**F · Bilder / Files** → verlangen (für die REA-Karte **nicht** optional; bevorzugt **Google-Drive-
Ordner**, §3f-Pipeline; Chat-Anhänge sind nicht als Datei lesbar)
21. **1× starkes Hauptbild** — **fertiger Zustand / Rendering / Luftbild des Objekts, NIEMALS Innen/
    Detail/Baustelle** (§6). Es ist **dasselbe** Bild für proofband-Slide-1, REA-Karte, `refsel__img`
    **und** die `wref`-Karte (Bild-Identität §6).
22. **Aussen- + Interieur-Renderings** fürs proofband-Karussell (Aussen→Interieur, §6-Reihenfolge).
23. **Herausforderungs-Bilder fürs cmap** je Archetyp (§1b): Denkmal = geschützte Substanz; Neubau =
    Baustelle (Aushub/Hangsicherung/Kran/Drohnenbild). Baustellenbilder gehören **nur** hierhin, nie als Hauptbild.

**G · Meta/SEO** → `<title>`, og/twitter, JSON-LD
24. SEO-Titel + 1-Satz-Description — oder ich generiere aus A/B (Tonalität §1).

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

## 1a. Semantik-Regeln (verbindlich, projektspezifisch statt generisch)

Texte müssen **projektspezifisch, knapp und immobilienwirtschaftlich sauber** sein — keine
AI-Sprache, kein «Case», kein Eigenlob, **keine allgemeinen Immobilienweisheiten**. Jeder Text
zeigt: konkrete **Ausgangslage** → geführte **Herausforderung** → entstehendes **Resultat**.

1. **Die 3 Boxen strikt trennen:**
   - **Ausgangslage** = nur die **neutrale Ausgangssituation + das Potenzial**. **Keine** Probleme,
     Risiken oder Lösungen.
   - **Herausforderung** = die **echten Engpässe**: Denkmalschutz, Bestand, Nutzungsmix, Bewilligung,
     Kosten, Marktqualität, Vermietbarkeit.
   - **Resultat** = **konkret**, was entsteht/entstanden ist: Anzahl Wohnungen, Gewerbefläche,
     Sanierungsstandard, Vermietungsziel, Status. **Keine langen Prozesssätze.**
2. **Begrifflichkeit:** narrativ **«Gewerbefläche»** (nicht «Gastro/Gewerbe», nicht «Gastro-/Gewerbe-
   fläche»); im Faktenblock nur wenn konkret richtig «Restaurant inkl. Take-Away»; **«Gastronomie»**
   nur wenn der **Betrieb als Nutzung** gemeint ist; **«Totalsanierung» vermeiden** — bei Bestand/
   Denkmalschutz **«Grundsanierung»** bzw. **«denkmalgerechte Grundsanierung»**.
3. **Werthebel (`vnode--ws`):** nicht alle 9 Stufen künstlich gleich wichtig machen — **nur echte
   Hebel markieren**. Bei Denkmal-/Bestandsprojekten sind i. d. R. **Machbarkeit, Bewilligung,
   Umsetzung, Vermietung** wichtiger als Nutzungskonzept oder Exit. Werthebel-Texte = **konkrete
   Execution**, keine abstrakten Begriffe (§1 Werthebel-Prinzip).
4. **Claims projektspezifisch** — kein «Wert entsteht nicht linear» o. ä. ohne Projektbezug.
   Besser: «Denkmalschutz setzt Grenzen. Genau darin lag die Aufgabe.» / «Aus Bestand wird ein
   bewilligtes und vermietbares Ertragsobjekt.»
5. **Standardblock Projektführung (`orch`)** → §3d (fixe Links-/Label-/Claim-Texte, projektspezifisch
   nur Schnittstellen-Punkte + Schlusssatz, beide untere Sätze identisch gestylt).
6. **Textlänge:** Boxen **kurz** — **1–2 präzise Sätze**, nie ein Absatz. Lieber präzise als vollständig.
7. **Nicht dramatisieren, nicht abstrahieren.** Kein «teuerste-Entscheidung»-Ton, keine allgemeinen
   Immobilien-Weisheiten, **kein Preis-Prahlen**. Segment immer als **«gehobenes Wohnsegment»**, NIE
   «oberes Preissegment». Luxus/Hochwertigkeit über **Substanz, Lage und Positionierung** ausdrücken,
   nicht über den Preis (bei Villa/Einzelobjekt: «geschützte Substanz erhalten und neu positionieren»,
   nicht «Luxusobjekt»). **Anglizismen im Fliesstext vermeiden** (Asset/Share Deal, Core, Value-Add,
   Joint Venture nur, wo sie als Fachbegriff wirklich nötig sind — dann bewusst, nicht flächig).
8. **Hero-Titel = Transformationssatz:** «Aus <Ausgangslage> wird <Resultat>» bzw. «Vom <X> zum <Y>»
   — kurz, konkret, projektspezifisch (die Namenszeile §3 steht davor). Beispiele: «Vom Grundstück
   zur Kapitalanlage.» · «Aus geschützter Substanz wird eine Villa mit Seeblick.»

---

## 1b. Projekttyp-Archetypen (Semantik · Werthebel · Bilder · orch — zusammenhängend)

Der **Projekttyp** bestimmt **gemeinsam** Wortwahl, markierte Werthebel, orch-Punkte, cmap-Bilder und
facts-Schwerpunkt. Wähle **einen** Archetyp und mische seine Bausteine nicht wahllos:

**A · Entwicklung / Transaktion** — Grundstück → institutionelles Anlageobjekt (*Killwangen*)
- Hero: «Vom Grundstück zur Kapitalanlage.» · **9 Phasen inkl. 09 Exit**.
- Werthebel (Achse **=** Phasen-Badges): typ. 01 Objektzugang · 03 Nutzungskonzept · 05 Bewilligung · 06 Kapital · 09 Exit.
- orch-Punkte: **Markt & Nutzung · Planung & Bewilligung · Kapital & Banken · Vermietung & Verkauf**.
- cmap-Bilder: **Baustelle/Rohbau**. facts: Grundstück, Neubau, Einheiten, institutioneller Käufer.

**B · Denkmal / Bestand** — geschützte Substanz → vermietbares/verkäufliches Ertragsobjekt (*Drei Könige, Sonne, MIRAGE*)
- Hero: «Aus historischer/geschützter Substanz wird belastbarer Ertrag / eine Villa.» · **8 Phasen (kein 09), 08 = Zielstufe**.
- Werthebel: typ. 01 Objektzugang · 02 Machbarkeit · 05 Bewilligung · 08 Vermietung/Verkauf.
- orch-Punkte: **Machbarkeit · Planung & Bewilligung · Umsetzung · Vermietung/Verkauf**.
- cmap-Bilder: **freigelegte Substanz, Bruchsteinmauerwerk, Gebälk, der geschützte Bestand im Umbau** (Handyfotos ok).
- Sprache: «denkmalgerechte Grundsanierung», Substanz/Positionierung statt Preis. facts: denkmalgeschützt, Grundsanierung/Erweiterung, Nutzung, «In Ausführung».

**C · Wohneigentum-Neubau** — Neubau → verkauftes Wohneigentum, **Verkauf = Endpunkt** (*HIDE*)
- Hero: «Fünf Eigentumswohnungen mit Seeblick – entwickelt mit den Käufern.» · **8 Phasen (kein 09), 08 Verkauf = Zielstufe**.
- Werthebel: typ. 01 Objektzugang · 03 Nutzungskonzept · 06 Kapital · 07 Umsetzung (+ 08 Zielstufe).
- orch-Punkte: **Markt & Nutzung · Planung & Bewilligung · Kapital & Banken · Verkauf**.
- cmap-Bilder: **Baustelle** (Aushub, Hangsicherung, Kran, **Drohnen-Luftbild der Baustelle**).
- facts: Eigentumswohnungen, Neubau, Segment («gehobenes Wohnsegment»), Aussicht, «In Ausführung».

> **Regel für alle:** Werthebel-Set **immer projektspezifisch** (nur echte Hebel markieren), **Achse ↔
> Phasen-Badges 1:1 identisch** (§3b). **Kein institutioneller Exit ⇒ 8 Phasen + 08 Zielstufe** (Achse
> & Phase synchron ohne 09). Die konkreten Nummern oben sind **Beispiele**, keine Pflicht — es zählt,
> dass sie die realen Wertsprünge des Projekts abbilden.

---

## 2. Seitenstruktur (Killwangen-Standard, normativ)

Alle Projektseiten teilen **dieses** Sektions-Skelett und **diesen Hintergrund-Rhythmus**.
Jede Sektion ist `<section class="…">` mit innen `<div class="wrap …">`.

| # | Sektion (`class`) | Hintergrund | Funktion | Heading |
|---|---|---|---|---|
| 1 | `archsec` | **hell** (`--paper`) | Hero-Titel **+ 3 Boxen** (Ausgangslage·Herausforderung·Ergebnis) **+ Wertachse** (§3) | **h1** (genau 1) |
| 2 | `facts` | **weiss** | Eckdaten, mit Zwischentitel **«Das Projekt in Zahlen.»** (§3a) | – |
| 3 | `proofband` | **navy** | Beleg-Band: grosser Claim + **grosses Bild-Karussell** (Hauptbild→Aussen→Interieur — §3f/§6, Bild-Identität) | – |
| 4 | `cmap` | **hell** (`--paper`) | Herausforderung: **Volltext (h2+p, volle Breite) + Herausforderungs-Karussell darunter** (§3f/§1b), **kein** rechtes Einzelbild | h2 |
| 5 | `proof` | **hell** (`--paper`) | 3 `pcard` — **projektspezifische** Synthese-Claims (§3c/§1a Regel 4), nicht die fixe Killwangen-Trias | h2 |
| 6 | `phases` (`main.phases`) ⊃ `phase` ×**8–9** | **hell** (`--paper`) | die Wertstufen **projektspezifisch** (§3b/§1b: 9 mit Exit *oder* 8 + Zielstufe), Sub-Titel projektadaptiert | (Sub-Titel) |
| 7 | `orch` | **navy** | «Eine Stelle, die den roten Faden hält» — Rolle smzh, Karte mit **smzh-Logo** (§3d) | h2 |
| 8 | `rea-cta` (`id="kontakt"`) | hellblau | Entscheidungs-CTA (§4), **VOR** «Weitere Projekte», **direkt an `orch` anschliessend** | h2 |
| 9 | `wref` | hell | Titel **«Weitere Referenzobjekte»** (`wref__h`, site-weit identisch) — **genau 3** Referenzkarten, 3-spaltig | h3 |

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
4. **Wertachse `.vaxis`** — horizontale Linie mit Knoten (`.vnode`), nur Nummer + Name;
   die **Wertsprung-Stufen** (`.vnode--ws`) sind gefüllt/blau hervorgehoben, die übrigen ruhig.
   **Kein Fliesstext/Punchline in der Achse, kein Kicker.** **Knotenzahl & Werthebel sind
   projektspezifisch** (§3b): Reine Wohneigentums-/Bestandsprojekte ohne institutionellen Exit
   führen **8 Knoten (01–08, kein 09 Exit)**; die `--ws`-Markierung nur auf die **realen**
   Werthebel des Projekts setzen (z. B. HIDE 01/03/06/07/08; MIRAGE 01/02/05/08). Die Achse
   muss **exakt** mit den Phasen-Badges (§3b) übereinstimmen.

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

## 3b. Die Wertstufen `phases` (verbindlich)

Grundfolge (Entwicklungs-/Transaktionsprojekt, Killwangen), fortlaufend 01–09:
```
01 Objektzugang · 02 Machbarkeit · 03 Nutzungskonzept · 04 Struktur ·
05 Bewilligung · 06 Kapital · 07 Umsetzung · 08 Vermietung/Verkauf · 09 Exit
```
- **09 Exit ist projektspezifisch, nicht Pflicht.** Bei Wohneigentums-/Bestandsprojekten, bei
  denen der Verkauf selbst der Endpunkt ist (kein institutioneller Exit), **entfällt Stufe 09
  komplett** — dann **8 Phasen (01–08)** und **08 = Zielstufe** (`<div class="wertspr wertspr--ziel">Zielstufe</div>`).
  09 restlos entfernen: Phasen-Section **und** den Achsen-Knoten 09 (§3) **und** evtl. „Exit“-Reste
  im Fliesstext (rea-cta ist geteilter Boilerplate → dort nur bei ausdrücklichem Wunsch anpassen).
- **Werthebel sind projektspezifisch.** Nur die realen Werthebel bekommen `phase phase--lever`
  **und** `<div class="wertspr">Wertsprung</div>`; die übrigen Phasen bleiben schmucklos. Diese
  Menge muss **1:1** der `--ws`-Markierung der Wertachse (§3) entsprechen (Achse ↔ Badges konsistent).
  Beispiele: HIDE 01/03/06/07 (+08 Zielstufe); MIRAGE 01/02/05 (+08 Zielstufe).
- Wrapper `main.phases > .wrap`, mit **Sub-Titel `.phases__t`** (projektadaptierbar, Aktiv-/Ergebnissatz),
  darüber die Spine/Cursor-JS (baut Timeline dynamisch aus `.phase[data-node]` — Phasenzahl egal).
- Jeder `phase`-Block: `data-phase="NN" data-label="…"`, `phase__num`, `phase__cat`,
  `phase__q` (**Aktiv-Satz «Wir …»**, kein Frage/Passiv), `phase__aha`, dann `raster` mit
  **vier** Zeilen: `Ausgangslage` · `smzh-Entscheid` · **`Werthebel`** (konkrete Handlung, §1)
  · `Resultat`.
- `data-phase`/`phase__num` konsistent mit DOM-Reihenfolge (Spine-/Scroll-JS liest `data-phase`).

## 3c. `proof` — Synthese direkt vor den Phasen (projektspezifisch)

Steht **direkt vor `phases`**, **heller** Hintergrund (`--paper`, gleiche Farbe wie `phases`,
damit beide als ein Block lesen). h2 = **projektspezifischer Synthesesatz** (Ausgangslage→Resultat,
z. B. «Aus geschützter Substanz wird eine marktfähige Villa.»). 3 `pcard` (weisse Karten, blaue
Icon-Box, navy h3, muted Text): je **h3 (2–4 Wörter) + 1 konkreter Satz**, die die **drei tragenden
Werthebel dieses Projekts** benennen — **nicht** die fixe Killwangen-Trias, sondern projektbezogen.
Beispiele: MIRAGE «Potenzial im Bestand geklärt» · «Zur Villa weiterentwickelt» · «Käuferkreis gezielt
geführt». Killwangen war «Wert entsteht nicht linear» · «Ein Grundstück hat mehrere Werte» · «Der Exit
wird früh vorbereitet» — nur als **eine** mögliche Variante, nicht als Vorlage zum Kopieren.

## 3d. `orch` — Zentrale Projektführung (Statement, navy) — **standardisiert, auf allen Seiten identisch**

Der dunkle Projektführungs-Abschnitt ist **strukturell auf jeder Projektseite gleich**.
**Projektspezifisch sind NUR** die Schnittstellen-Punkte rechts (`.role__step`) und der
**letzte Satz unten** (`.role__sub`). Alles andere ist fixer Standardtext:

- **Links Titel (`h2`), immer:** «Eine Stelle, die den roten Faden hält.»
- **Links Fliesstext (`p`), immer:** «smzh war nicht einfach ein weiterer Spezialist im
  Projekt. smzh führte die zentralen Schnittstellen.» (kein «: Produkt, Planung …»-Anhang).
- **Rechts Kopf:** smzh-**Logo** (`.role__logo`, s. u.) + Label (`.role__label`), immer
  «Zentrale Projektführung». **Nie** «Deklarierter Wertbeitrag» / «Wertbeitrag von smzh» /
  «Wir zeigen offen …» als Titel.
- **Rechts Punkte (`.role__step`, projektspezifisch, i. d. R. 4):**
  - Entwicklungs-/Transaktionsprojekte (Killwangen-Typ): **Markt & Nutzung · Planung & Bewilligung
    · Kapital & Banken · Vermietung & Verkauf**.
  - Denkmal-/Bestandsprojekte (Bremgarten-Typ): **Machbarkeit · Planung & Bewilligung · Umsetzung
    · Vermietung**.
- **Unten erster Satz (`.role__claim`), immer:** «Nicht jede Aufgabe selbst. Aber jede
  Schnittstelle im Blick.»
- **Unten zweiter Satz (`.role__sub`, projektspezifisch):** konkret zur Wertschöpfung des Projekts
  (z. B. Killwangen «So entstand der durchgängige Weg vom Grundstück bis zum institutionellen Käufer.»,
  Bremgarten «So entsteht der durchgängige Weg vom denkmalgeschützten Bestand zum vermietbaren
  Ertragsobjekt.»). **Keine generische Eigenlob-Sprache, kein «Case».**
- **Beide unteren Sätze visuell GLEICH:** `.role__claim` und `.role__sub` haben **identische**
  Schriftgrösse, Font-Weight, Farbe und Zeilenhöhe (`font-size:15px;font-weight:700;color:#fff;
  line-height:1.45`; `.role__sub` nur zusätzlich `margin-top:9px`). **Kein Satz fett/grösser/heller
  als der andere.**
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

**Proofband-Karussell (gross, navy):** Reihenfolge (§6): Hauptbild (Objekt/Luftbild) zuerst, dann
weitere Aussen-Renderings, dann Interieur. **Slide 1 = Hauptbild** und **exakt dasselbe Bild wie
REA-`rc__img`-Karte, `refsel__img` und `wref`-Karte** (Bild-Identität §6 — bei Änderung überall synchron).

**cmap-Karussell (hell):** **kein** rechtes Einzelbild — der Text (h2 + p) läuft **volle Breite**,
darunter ein **eigenes** Karussell mit den **Herausforderungs-Bildern** je Archetyp (§1b): Denkmal =
freigelegte/geschützte Substanz (Bruchstein, Gebälk, Altbau im Umbau); Neubau = Baustelle (Aushub,
Hangsicherung, Kran, Drohnen-Baustellenbild). **Nie fertige Renderings** hier. Wrapper wie Killwangen:
`<div class="wrap" style="margin-top:36px"><figure class="carousel …">…</figure></div>`.

**Fenstergrösse = wie Killwangen (verbindlich):** Das Karussell-«Fenster» ist **gleich gross
wie bei Killwangen** — **volle Container-Breite**, Basishöhe `.carousel__img{height:clamp(280px,40vw,440px)}`
(proofband höher). **Das Karussell NICHT verschmälern** (kein `max-width` am `.carousel`, nicht
zentrieren). Beschnitt der ~3:2-Fotos wird **ausschliesslich über `object-position`** gesteuert,
nicht über die Rahmengrösse: heikle/**Hochformat-Bilder** mit `style="object-position:center <Y>%"`
so ausrichten, dass das bildwichtige Motiv (z. B. das Bruchsteinmauerwerk) im Ausschnitt bleibt.

**Slides hinzufügen/entfernen (verbindlicher 4-Punkt-Sync):** Beim Ändern der Slide-Zahl **immer
gemeinsam** nachziehen: (1) `data-caps` (`||`-Liste, genau eine Caption je realem Slide), (2)
`.carousel__count` «/ N», (3) die `.carousel__slide`-Divs im `.carousel__track`, (4) `.carousel__cap`
(= Caption Slide 1). Danach visuell prüfen (mind. Slide 1 + der neue Slide), sonst laufen Bild/Caption/Zähler auseinander.

**Bild-Pipeline (Google Drive):**
- **Chat-/PDF-Anhänge sind NICHT als Datei lesbar** (nicht im Container gespeichert). Einziger
  verlässlicher Weg: **Google Drive** (oder bereits eingebettetes Base64 in früher hochgeladenen HTMLs).
- **Ordner-Link → Datei-IDs:** die Ordner-HTML ziehen (`curl -sL "https://drive.google.com/drive/folders/<FID>"`)
  und die 28–44-stelligen IDs regexen. Titel/Reihenfolge über `mcp__Google_Drive__get_file_metadata`
  (`title`, `createdTime`). **Upload-Reihenfolge = `createdTime`** (der Nutzer meint mit „das erste
  hochgeladene“ genau das). Dateinamen verraten Rolle: `…Aussen…/…Luft…` (Renderings, Hauptkarussell),
  `…Innen…/…Bad/…Zimmer` (Interieur), kleine `Bild*.jpg`/Handyfotos (Baustelle/Bestand → **cmap**).
- **Web-Grössen** über den Thumbnail-Endpoint `…/thumbnail?id=<ID>&sz=w<Breite>` — **Hero/Hauptkarussell
  `w1600–1800`**, **Karten `w900`** — dann als Base64 einbetten.
- **Quadratische Thumbnails** (Picasa liefert manche `NxN`): für Querformat-Rahmen per Chromium-Canvas
  auf 3:2 mittig zuschneiden (`drawImage`), nicht verzerren. Kein PIL im Container → Canvas nutzen.
- Bilder **inhaltlich der Caption zuordnen** (Kontaktabzug rendern, visuell matchen), nicht raten.

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
- **Hauptbild = immer das Objekt in Aussen-/Kontextansicht** (Fassade/Aussen-Rendering **oder ein
  Luftbild/Drohnenbild des fertigen Objekts** — das Objekt + Umgebung zeigend). **Nie** ein Innenraum-,
  Detail- oder Baustellen-/Rohbaubild als Hauptbild. Gibt es keine solche Aufnahme → beim Nutzer
  verlangen, nicht ersatzweise ein Innenbild nehmen.
- **Bild-Identität (verbindlich, überall dasselbe Hauptbild):** Das **proofband-Slide-1-Hauptbild**
  ist **exakt dasselbe Bild** wie die **REA-`rc__img`-Referenzkarte**, das **Auswahl-Panel
  (`refsel__img`)** und die **`wref`-Karte** dieses Projekts auf anderen Seiten. **Ändert sich das
  Hauptbild, ziehe alle Vorkommen synchron nach** (proofband ↔ REA-Karte/Pin ↔ wref auf den anderen
  Seiten). Ein Auseinanderlaufen (REA zeigt ein anderes Bild als das Projekt-Karussell) ist ein Fehler.
- **Grosses Karussell (proofband) — Reihenfolge:** Hauptbild zuerst (Objekt/Luftbild), dann weitere
  **Aussen-Renderings** (Terrasse/Pool/Strasse/Weg), dann **Interieur** (Wohnen/Essen/Küche, Schlaf, Bad).
  Mechanik/Ausschnitt → §3f.
- **`cmap` = eigenes Karussell unter dem Volltext** (kein rechtes Einzelbild) = die **Herausforderungs-
  Bilder**, passend zum Archetyp (§1b): bei **Denkmal/Bestand** die geschützte/freigelegte Substanz
  (Bruchsteinmauerwerk, Gebälk, der Altbau im Umbau); bei **Neubau/Entwicklung** die **Baustelle**
  (Aushub, Hangsicherung, Kran, Drohnen-Baustellenbild). Immer die eher **prozesshaften/rohen** Fotos —
  nie die fertigen Renderings (die gehören ins proofband). Rahmen ans Foto-Format angleichen (§3f).

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
- [ ] Bild-Karussells (§3f): 4-Punkt-Sync (`data-caps` · `count /N` · Slide-Divs · `.carousel__cap`);
      volle Breite, Hochformat/Quadrat via `object-position`/Canvas-Crop.
- [ ] **Bild-Identität (§6):** proofband Slide 1 = REA-`rc__img` = `refsel__img` = `wref`-Karte (dasselbe
      Bild); Hauptbild ist Aussen/Luftbild (nie Innen/Detail/Baustelle); cmap = Herausforderungsbilder je Archetyp.
- [ ] **Archetyp konsistent (§1b):** Werthebel-Set, orch-Punkte, cmap-Bilder, facts-Schwerpunkt und
      Sprache passen zum **einen** gewählten Typ (A/B/C); kein Bausteine-Mix.
- [ ] Wertstufen aktiv («Wir …»); **jeder Werthebel = konkrete ausgeführte Massnahme** (§1).
      Werthebel projektspezifisch; **Achsen-`--ws` ↔ Phasen-`wertspr` identisch**; 09 Exit nur wo
      sinnvoll, sonst 8 Phasen + 08 Zielstufe (Achse & Phase synchron entfernt).
- [ ] `orch` **standardisiert (§3d)**: fixer Links-Titel/-Text, Label «Zentrale Projektführung»,
      Standard-Claim unten; projektspezifisch nur `.role__step` + `.role__sub`; **beide unteren Sätze
      identisch gestylt**; **smzh-Logo** statt Text; Karte berührt den CTA nicht (keine Lücke/Kollision).
- [ ] Tonalität §1; kein «ß»; kein «Case»; smzh klein; keine Kicker/Uppercase-Labels.
- [ ] Titelgrössen vereinheitlicht (§2); Titel volle Breite.
- [ ] Heller `rea-cta` (§4, `id="kontakt"`) vor `wref`; `wref` = genau 3 andere Projekte, 3-spaltig.
- [ ] Auf REA-Hauptseite als gleich grosse Referenzkarte + Karten-Pin (Bildregel §6).
- [ ] Screenshot geprüft, interne Links lösen auf; auf beide Branches gepusht, Deploy grün (§8).
