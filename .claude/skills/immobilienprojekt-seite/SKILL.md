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
| 1 | `archsec` | Hero: Projektname + Leit-Claim „Vom Grundstück zur Kapitalanlage" | **h1** (genau 1 pro Seite) |
| 2 | `facts` | Eckdaten-Band (Lage, Nutzung, Fläche, Status …) — **Stil V5, siehe §3a** | – |
| 3 | `proofband` | schmales Beleg-/Kontext-Band | – |
| 4 | `thesis` | Kernthese: „Wert entsteht vor dem Verkauf. Und oft lange davor." | h2 |
| 5 | `cmap` | Kontext/Ausgangslage der Lage | h2 |
| 6 | `phase` ×N | Wertachse als Phasen; `phase--lever` markiert die Hebel-Phasen | – |
| 7 | `proof` | Beleg, dass Wert nicht linear entsteht | h2 |
| 8 | `orch` | „Eine Stelle, die den roten Faden hält" (Orchestrierung) | h2 |
| 9 | `team` | „Das Team hinter <Projekt>" (Bauherrenvertretung/Projektleitung) | h2 |
| 10 | `comp` | „Nicht vier Dienstleistungen. Ein durchgängiges Wertsystem." | h2 |
| 11 | `frame` (`id="kontakt"`) | **CTA-Block** (projektspezifisches Heading + 3 CTAs) | h2 |
| 12 | `wref` | „Weitere Projekte" – Referenzkarten (`rc`) auf andere Projekte | h3 |
| — | smzh-Footer | geklonte Chrome, unverändert | – |

Vor `archsec` und nach `wref` steht die geklonte Chrome (`firstRow`/`secondRow`
Header, Mega-Menü, Footer). **Nie** ein zweites `h1` einbauen.

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

## 4. Der geteilte CTA-Block (`.frame`) – identisch auf allen Seiten

Alle Projektseiten **und** die REA-Hauptseite tragen dieselben **drei** CTAs
(gleich breit). Nur das **Heading** ist auf den Projektseiten projektspezifisch;
die Buttons sind überall gleich:

| Button-Text | Ziel |
|---|---|
| Projekt einordnen | `../projekt-einordnen/index.html` |
| Anlegerprofil erstellen | `../anlageprofil/index.html` |
| Verkauf prüfen | `../liegenschaft-verkaufen/index.html` |

Auf den Projektseiten liegt der Block als `<section class="frame" id="kontakt">` in
navy; auf der REA-Hauptseite als `<section class="cta">` auf hellblauem Grund
(`background:#EEF6FC`). **Nie** nur „Projekt einordnen lassen" allein – immer die
drei gleichgewichteten CTAs.

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
4. **Eyebrow/Breadcrumb:** „Projekt · <Ort>" (nie „Case · …"). Nav-Trail
   „Real Estate Advisory · Projekt <Ort>".
5. **`wref`-Sektion:** Referenzkarten auf **andere** Projekte setzen (nicht auf sich
   selbst). Auf den bestehenden Projektseiten die neue Seite in deren `wref`
   gegenseitig ergänzen.
6. **E-Mail-CTAs:** mailto-Betreff „Projekt-Einordnung (<Ort>)" – ohne das Wort „Case".

---

## 6. Auf der REA-Hauptseite einbinden

`site/smzh.ch/de/real-estate-advisory/index.html`:

- **Referenzkarten-Grid (`.refs` / `.rc`):** neue Karte im Stil der bestehenden
  Karten (grösseres Bild `.rc__img`, Titel, Beschreibungstext, Button
  „**Projekt ansehen** →" via `.rc__go` → `../<slug>/index.html`). Karten sind
  **gleich gross** (flex `calc()`), Buttons unten via `margin-top:auto` gepinnt.
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
inhaltlich). Fix: **`rerun_failed_jobs`** oder ein frischer **`workflow_dispatch`**-Lauf
(`run_workflow` auf `deploy-pages.yml`, ref = Deploy-Branch). Nicht am Code suchen,
wenn der Fehler im Step „Deploy to GitHub Pages" beim `syncing_files`-Polling auftritt.
Nach grünem Lauf den Nutzer hart neu laden lassen (Cmd/Ctrl+Shift+R).

---

## 9. Definition of Done

- [ ] Seite als Klon der Vorlage, volles Sektions-Skelett (§2), genau **1 h1**.
- [ ] Investoren-Tonalität (§1); Tonalitäts-Grep **sauber** (auch in Meta-Tags:
      `<title>`, og/twitter-Description, JSON-LD — nicht nur sichtbarer Text).
- [ ] **Keine sichtbaren Platzhalter** (`Inhalt fehlt`, `Name offen`, `Rolle offen`,
      leere `?`-Team-Karten) — harter Gate.
- [ ] Kein „ß"; kein „Case"-Label (nur „Investment Case" im Fliesstext); kein „Werthebel".
- [ ] Ein Begriff site-weit: **Anlageprofil** vs. Anlegerprofil, **ein** Titel-Trennzeichen.
- [ ] Geteilter 3-CTA-Block (gleich breit), korrekte Ziele (§4).
- [ ] `wref` verweist auf andere Projekte; bestehende Projekte gegenseitig ergänzt.
- [ ] Auf der REA-Hauptseite als gleich grosse Referenzkarte „Projekt ansehen"
      eingebunden.
- [ ] Alle internen Links lösen auf; Screenshot geprüft.
- [ ] Auf beide Branches gepusht, Deploy grün (nötigenfalls Rerun/Dispatch).
