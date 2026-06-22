# smzh.ch – lokaler 1:1 Mirror (komplette deutsche Site)

Ein originalgetreuer, offline lauffähiger Nachbau der **gesamten deutschen
smzh.ch** – alle **663 Seiten** unter `/de/` (Startseite, Services, smzHub,
smzh Markets, alle Artikel, News, Flash/Edu Talks, Podcasts, Team-, Event- und
Rechtsseiten). Jede Seite wurde im Headless-Browser gerendert, sodass der per
API nachgeladene Inhalt als statischer Snapshot eingefroren ist; alle Assets
(CSS, Bilder, Schriften, PDFs) wurden lokal gespiegelt.

**Wichtig – keine Verlinkung zum Original:** Sämtliche internen Links und
Asset-Verweise zeigen ausschließlich auf lokale Kopien. Es existiert **kein
einziger Verweis** mehr auf `smzh.ch` / `www.smzh.ch` / `cms.smzh.ch`. Nur
externe Links (Social Media, YouTube etc.) bleiben unverändert.

> Hinweis: Die ältere Tabelle unten listet die 16 zuerst gespiegelten Kernseiten
> – inzwischen ist die **komplette** deutsche Site enthalten.

## Schnellstart

```bash
./serve.sh            # startet einen lokalen Webserver auf Port 8099
# danach im Browser oeffnen:
#   http://localhost:8099/
```

> **Wichtig:** Der Mirror muss über **HTTP** ausgeliefert werden (das macht
> `serve.sh`), **nicht** per `file://`-Doppelklick. Die von Next.js optimierten
> Bilder (`/_next/image`) liegen unter Dateinamen mit URL-kodierten Zeichen, die
> erst ein HTTP-Server korrekt auflöst.

Eigener Port: `./serve.sh 3000`

## Gespiegelte Seiten

| Seite | Pfad im Mirror |
|-------|----------------|
| **smzHub** (Hauptseite) | `site/smzh.ch/de/smzhub/index.html` |
| Startseite | `site/smzh.ch/de/index.html` |
| Rechner | `site/smzh.ch/de/rechner/index.html` |
| smzh Markets | `site/smzh.ch/de/markets/index.html` |
| Karriere | `site/smzh.ch/de/karriere/index.html` |
| Termin vereinbaren | `site/smzh.ch/de/terminvereinbaren/index.html` |
| Steuererklärung | `site/smzh.ch/de/steuererklaerung/index.html` |
| Vorsorgeanalyse | `site/smzh.ch/de/vorsorgeanalyse/index.html` |
| Immobilienbewertung | `site/smzh.ch/de/immobilienbewertung/index.html` |
| Preise für Privatkunden | `site/smzh.ch/de/preise-fuer-privatkunden/index.html` |
| Preise für Firmenkunden | `site/smzh.ch/de/preise-fuer-firmenkunden/index.html` |
| Über uns | `site/smzh.ch/de/uber-uns/index.html` |
| Geschäftspartner | `site/smzh.ch/de/geschaftspartner/index.html` |
| Impressum | `site/smzh.ch/de/impressum/index.html` |
| Datenschutz | `site/smzh.ch/de/datenschutz/index.html` |
| E-Mail-Korrespondenz | `site/smzh.ch/de/email-korrespondenz/index.html` |

Die Navigation (Mega-Menü, Footer) zwischen diesen Seiten ist funktionsfähig und
führt auf die lokalen Kopien.

## Verzeichnisstruktur

```
site/
├── index.html              # Einstiegsseite mit Links + Redirect auf smzHub
├── smzh.ch/
│   ├── de/<seite>/index.html   # die gespiegelten Seiten
│   ├── _next/static/...        # CSS- und JS-Chunks
│   ├── _next/image/...         # optimierte Bilder (Next.js Image)
│   ├── fonts/...               # CircularXX Web-Fonts
│   ├── logo/  favicon/...      # Logos und Favicons
└── cms.smzh.ch/uploads/...     # CMS-Bilder (Logos von Partnern etc.)
```

## Mirror aktualisieren

Die komplette deutsche Site entsteht über diese Pipeline:

```bash
# URL-Liste stammt aus build/de-urls.txt (aus den smzh.ch-Sitemaps abgeleitet)
node   build/crawl.cjs            # 1) alle 663 /de/-Seiten im Headless-Browser rendern
                                  #    (Playwright, parallel, resuemierbar, 3x Retry)
python3 build/postprocess_all.py  # 2) Inhalt einfrieren, Skripte entfernen,
                                  #    Assets + interne Links lokal verlinken, Bilder nachladen
python3 build/fixlinks.py         # 3) Nachzieh-Pass: letzte Original-/Root-Links lokalisieren
```

Für nur die 16 Kernseiten existiert weiterhin der ältere Zweistufen-Weg
(`build/snapshot-all.cjs` + `build/postprocess.py`).

**Warum zwei Stufen?** smzh.ch ist eine Next.js-App; der eigentliche
smzHub-Inhalt (Artikel, News, Flash Talks, Edu Talks, Podcasts) wird erst im
Browser per API nachgeladen. `mirror.sh` allein liefert daher nur das Geruest
mit einem „Loading…"-Platzhalter. Stufe 2 lädt jede Seite in Chromium
(Playwright), wartet bis der Inhalt vollständig da ist, friert das gerenderte
HTML ein, entfernt die Skripte (sonst würde die Re-Hydration den Inhalt wieder
leeren) und schreibt alle Asset- und Navigations-Links auf die lokalen
Mirror-Pfade um (fehlende Bildvarianten werden nachgeladen).

Build-Artefakte liegen unter `build/` (`wget.log`, gerenderte Rohseiten in
`build/rendered/`).

## Bekannte Einschränkungen

- **Dynamische Inhalte (eingefroren):** Der smzHub-Wissens-Content (Artikel,
  News, Flash Talks, Edu Talks, Podcasts) wird im Original per API nachgeladen.
  Über den Headless-Render (siehe „Mirror aktualisieren") ist dieser Inhalt als
  **statischer Snapshot eingefroren** und sichtbar – er entspricht dem Stand zum
  Render-Zeitpunkt und aktualisiert sich nicht von selbst. Echtzeit-Funktionen
  (z. B. Live-Marktdaten in smzh Markets, Filter-Interaktionen) sind als
  Momentaufnahme enthalten, aber nicht interaktiv.
- **Formulare** (Termin, Newsletter, Datei-Upload) senden im Original an
  Backend-APIs und funktionieren im Mirror nicht.
- **Schriftschnitt `CircularXXWeb-RegularItalic.woff2`** liefert auf dem
  Original-Server konstant HTTP 500 und fehlt daher. Der Browser synthetisiert
  diese Kursive aus dem Regular-Schnitt – optisch nicht relevant.
- **Tracking** (Google Tag Manager) wurde bewusst nicht mitgespiegelt.
- Externe Links (Social Media, YouTube etc.) zeigen weiterhin auf die
  Original-URLs im Web.

## Hinweis

Inhalte und Marken gehören smzh (Swiss Management Zürich). Dieser Mirror dient
ausschließlich der lokalen, originalgetreuen Reproduktion zu Archiv-/Testzwecken.
