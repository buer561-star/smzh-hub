#!/usr/bin/env bash
# Serviert den lokalen smzHub-Mirror ueber HTTP.
# WICHTIG: Der Mirror muss ueber HTTP ausgeliefert werden (nicht per file://),
# da die optimierten Bilder (Next.js /_next/image) Dateinamen mit kodierten
# Zeichen verwenden, die erst der HTTP-Server korrekt aufloest.
set -euo pipefail
PORT="${1:-8099}"
ROOT="$(cd "$(dirname "$0")/site" && pwd)"
echo "smzHub-Mirror laeuft auf:  http://localhost:${PORT}/"
echo "smzHub-Seite direkt:       http://localhost:${PORT}/smzh.ch/de/smzhub/index.html"
cd "$ROOT"
exec python3 -m http.server "$PORT"
