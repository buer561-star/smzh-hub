# smzhHub – Snapshots & Wiederherstellungspunkte

Übersicht aller gespeicherten Design-Stände der smzhHub-Startseite. **Alle
Commits sind nach `origin/claude/inspiring-dirac-2ioa4s` gepusht** und damit
dauerhaft – auch wenn der Container neu startet. Backup-Ordner unter
`build/backup/` sind zusätzlich als Datei-Schnappschuss committet.

## Dauerhafte Backup-Ordner (committet & gepusht)

| Ordner | Design | Commit |
|---|---|---|
| `build/backup/radikale-vereinfachung/` | Radikale Vereinfachung: Entscheidungskarten (statisch) + kurze Reiter Eigenheim/Vermögen/Zukunft/Research | `d908058` |
| `build/backup/karussell-3rubriken/` | **Aktuell:** Hero + Entscheidungs-Karussell (4 sichtbar, Pfeile) + 3 Rubriken Eigenheim/Vermögen/Zukunft, 4-Themen-Reiterleiste | `782ac2a` |

## Alle Design-Stände als Commit-Wiederherstellungspunkte

| Commit | Stand |
|---|---|
| `77f6dae` | Editorial-Version: 4 Themenwelten, einfache „Leitartikel + 3 Beiträge"-Sektionen |
| `851c395` | Redaktionelle Neuordnung: Flagship-Publikation (dunkel/Gold), Dossier, Guide-Pfad |
| `d908058` | Radikale Vereinfachung: Entscheidungskarten + 3 Rubriken + Research-Seite |
| `782ac2a` | **Karussell + 3 Rubriken** (aktueller Stand) |

## Wiederherstellen

Kompletten Stand eines Commits zurückholen (Beispiel Karussell-Version):

```bash
git checkout 782ac2a -- site/ build/build_hub_editorial.py \
  build/build_inventory.py build/smzhhub-content.json
```

Oder einzelne Dateien aus einem Backup-Ordner zurückkopieren, z. B.:

```bash
cp build/backup/karussell-3rubriken/build_hub_editorial.py build/
python3 build/build_hub_editorial.py   # Seiten neu erzeugen
```

> Hinweis: Git-Tags lassen sich in dieser Remote-Umgebung nicht pushen
> (nur der Feature-Branch ist beschreibbar). Die belastbaren Referenzen sind
> daher die oben genannten Commit-IDs und die committeten Backup-Ordner.
