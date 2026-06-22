#!/usr/bin/env bash
# Reproduzierbarer 1:1-Mirror der smzHub-Seite und aller direkt verlinkten Seiten.
# Laedt HTML + alle Page-Requisites (CSS, JS, Bilder, Fonts) von smzh.ch und
# cms.smzh.ch, schreibt alle Links auf lokale, relative Pfade um.
# Tracking (Google Tag Manager) und Social-Media-Hosts werden bewusst ausgelassen.
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p build
wget \
  -e robots=off \
  --no-verbose \
  --tries=4 --waitretry=8 --timeout=30 \
  --user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36" \
  --page-requisites \
  --convert-links \
  --adjust-extension \
  --span-hosts --domains=smzh.ch,cms.smzh.ch \
  --restrict-file-names=windows \
  --directory-prefix=site \
  --input-file=build/urls.txt \
  2> build/wget.log
echo "wget exit: $? (Code 8 = einzelne Upstream-HTTP-Fehler, z. B. RegularItalic-Font 500)"
echo "Dateien:   $(find site -type f | wc -l)"
echo "Groesse:   $(du -sh site | cut -f1)"
