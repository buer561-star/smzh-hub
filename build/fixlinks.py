#!/usr/bin/env python3
"""Nachzieh-Pass: entfernt restliche Original-Verweise und root-relative interne
Links aus den fertigen Seiten (site/smzh.ch/**/index.html).
- https://(www.)?smzh.ch/de|en/...   -> lokaler relativer Seitenpfad
- root-relativer href="/de|en/..."   -> lokaler relativer Seitenpfad
  (auch mit ?query / #hash; query/hash wird fuer das Ziel entfernt)
Niemals bleibt eine Original-URL stehen.
"""
import os, re

SMZH = os.path.join('site', 'smzh.ch')

def target_local(tp, prefix):
    tp = tp.split('#')[0].split('?')[0]
    segs = [s for s in tp.strip('/').split('/') if s]
    if not segs:
        segs = ['de']
    return prefix + '/'.join(segs) + '/index.html'

changed = 0
for root, _, names in os.walk(SMZH):
    for n in names:
        if n != 'index.html':
            continue
        full = os.path.join(root, n)
        rel_dir = os.path.relpath(root, SMZH)
        depth = 0 if rel_dir == '.' else len([s for s in rel_dir.split(os.sep) if s])
        prefix = '../' * depth
        html = open(full, encoding='utf-8', errors='ignore').read()
        orig = html
        # 1) absolute (www.)smzh.ch Seiten-Links
        html = re.sub(r'href="https?://(?:www\.)?smzh\.ch(?P<p>/(?:de|en)/[^"]*)"',
                      lambda m: 'href="' + target_local(m.group('p'), prefix) + '"', html)
        # 2) blanke Wurzel-Links auf (www.)smzh.ch
        html = re.sub(r'href="https?://(?:www\.)?smzh\.ch/?"',
                      'href="' + target_local('/', prefix) + '"', html)
        # 3) root-relative interne Links (auch mit ?/#)
        html = re.sub(r'href="(?P<p>/(?:de|en)/[^"]*)"',
                      lambda m: 'href="' + target_local(m.group('p'), prefix) + '"', html)
        # 4) Sicherheitsnetz: jeder verbliebene (www.)smzh.ch-Verweis -> lokal
        html = re.sub(r'(href|src)="https?://(?:www\.)?smzh\.ch(?P<p>/[^"]*)"',
                      lambda m: f'{m.group(1)}="' + prefix + m.group('p').lstrip('/') + '"', html)
        if html != orig:
            with open(full, 'w', encoding='utf-8') as f:
                f.write(html)
            changed += 1
print('geaenderte Dateien:', changed)
