# smzHub – lokaler 1:1 Asset-Mirror

Ein originalgetreuer, offline lauffähiger Mirror der Seite
[`https://smzh.ch/de/smzhub/`](https://smzh.ch/de/smzhub/) **und aller direkt
darauf verlinkten Seiten**. Alle Seiten-Assets (HTML, CSS, JavaScript, Bilder,
Schriften) wurden vom Original-Server heruntergeladen und sämtliche Links auf
lokale, relative Pfade umgeschrieben.

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

```bash
./mirror.sh
```

Das Skript lädt alle Seiten aus `build/urls.txt` neu. Das Build-Log liegt unter
`build/wget.log`.

## Bekannte Einschränkungen

- **Dynamische Inhalte:** smzh.ch ist eine Next.js-Anwendung. Der Wissens-Content
  des smzHub (Blogartikel, News, Flash Talks, Podcasts) sowie Live-Marktdaten
  werden zur Laufzeit per API/JavaScript nachgeladen und sind in einem statischen
  Mirror nicht vollständig reproduzierbar. Das vorgerenderte Layout, Texte und
  Bilder sind originalgetreu vorhanden.
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
