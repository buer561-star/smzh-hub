#!/usr/bin/env python3
"""Entfernt site-weit alle verbliebenen Verweise auf das Original aus den
Metadaten (kein klickbarer Link, aber laut Vorgabe soll NICHTS aufs Original
zeigen): canonical, og:url, twitter:url/domain, alternate/hreflang sowie als
Sicherheitsnetz jeden uebrig gebliebenen smzh.ch-/cms.smzh.ch-Literal.
"""
import os, re

SMZH = os.path.join('site', 'smzh.ch')
HOST = re.compile(r'https?://(?:www\.|cms\.)?smzh\.ch')

patterns = [
    re.compile(r'<link\b[^>]*\brel="canonical"[^>]*>', re.I),
    re.compile(r'<link\b[^>]*\brel="alternate"[^>]*\bhreflang="[^"]*"[^>]*>', re.I),
    re.compile(r'<link\b[^>]*\bhreflang="[^"]*"[^>]*>', re.I),
    re.compile(r'<meta\b[^>]*\bproperty="og:url"[^>]*>', re.I),
    re.compile(r'<meta\b[^>]*\bname="twitter:(?:url|domain)"[^>]*>', re.I),
]

changed = 0
residual_files = 0
for root, _, names in os.walk(SMZH):
    for n in names:
        if n != 'index.html':
            continue
        f = os.path.join(root, n)
        html = open(f, encoding='utf-8', errors='ignore').read()
        orig = html
        for p in patterns:
            html = p.sub('', html)
        # Sicherheitsnetz: jeder verbliebene Original-Host-Literal -> leeren String
        # (betrifft nur noch vereinzelte Meta-/JSON-Reste; klickbare Links/Assets
        #  wurden bereits zuvor lokalisiert)
        if HOST.search(html):
            html = HOST.sub('', html)
        if html != orig:
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(html)
            changed += 1
print('geaenderte Dateien:', changed)
