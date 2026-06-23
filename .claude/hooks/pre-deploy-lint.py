#!/usr/bin/env python3
"""Pre-Deploy-Lint für smzhHub.

Blockt einen Deploy, wenn auf den von uns gebauten Hub-Seiten GROSSBUCHSTABEN-
Texte auftauchen – entweder via CSS `text-transform:uppercase` in unserem
v5-CSS-Block oder als literale ALL-CAPS in unseren Label-Klassen.

Zwei Modi:
  • Als Claude-Code PreToolUse-Hook (Default): liest das Tool-JSON von stdin und
    wird NUR bei einem Deploy-Push aktiv (git push … auf den Pages-Deploy-Branch).
  • Standalone:  python3 .claude/hooks/pre-deploy-lint.py --scan

Exit 2 + Meldung auf stderr  ⇒  Deploy/Tool wird geblockt (Claude bekommt die Meldung).
Exit 0  ⇒  sauber bzw. kein Deploy-Befehl.
"""
import sys, os, re, glob, json

DEPLOY_BRANCH = 'claude/inspiring-dirac-2ioa4s'
LABEL_CLASSES = ['art-cta-eyebrow', 'art-fig-tag', 'art-rel-k',
                 'art-related-eyebrow', 'v5-eyebrow', 'v5-dec-fresh']

def root():
    return os.environ.get('CLAUDE_PROJECT_DIR') or os.getcwd()

def rel(f, r):
    try: return os.path.relpath(f, r)
    except Exception: return f

def hub_pages(r):
    d = os.path.join(r, 'site', 'smzh.ch', 'de')
    pages = [os.path.join(d, p, 'index.html')
             for p in ('smzhub', 'smzhub-horizon', 'smzhub-immobilienanlagen')]
    pages += sorted(glob.glob(os.path.join(d, 'ratgeber-*', 'index.html')))
    return [p for p in pages if os.path.exists(p)]

def scan(r):
    issues = []
    # 1) Quelle: unser v5-CSS darf kein text-transform:uppercase enthalten
    src = os.path.join(r, 'build', 'build_hub_v5.py')
    if os.path.exists(src):
        n = open(src, encoding='utf-8').read().count('text-transform:uppercase')
        if n:
            issues.append(f'build/build_hub_v5.py: {n}× text-transform:uppercase (Quelle)')
    # 2) Gerenderte Hub-Seiten: v5-CSS-Block + literale Caps in Label-Klassen
    cls = '|'.join(LABEL_CLASSES)
    for f in hub_pages(r):
        s = open(f, encoding='utf-8').read()
        m = re.search(r'<style id="smzh-v5-css">(.*?)</style>', s, re.S)
        if m and 'text-transform:uppercase' in m.group(1):
            issues.append(f'{rel(f, r)}: text-transform:uppercase im smzh-v5-css')
        for txt in re.findall(r'class="(?:' + cls + r')"[^>]*>([^<]*)', s):
            if re.search(r'[A-ZÄÖÜ]{4,}', txt):
                issues.append(f'{rel(f, r)}: ALL-CAPS-Text „{txt.strip()[:40]}"')
    return issues

def main():
    standalone = '--scan' in sys.argv
    if not standalone:
        # Hook-Modus: nur bei einem Deploy-Push aktiv werden
        try:
            data = json.load(sys.stdin)
        except Exception:
            sys.exit(0)
        cmd = (data.get('tool_input') or {}).get('command', '') or ''
        if not ('git push' in cmd and DEPLOY_BRANCH in cmd):
            sys.exit(0)
    issues = scan(root())
    if issues:
        sys.stderr.write(
            'Pre-Deploy-Lint: Deploy GEBLOCKT – GROSSBUCHSTABEN auf Hub-Seiten:\n'
            + '\n'.join('  - ' + i for i in issues)
            + '\n\nBitte beheben (text-transform:uppercase entfernen bzw. Text normal '
              'schreiben) oder den Subagenten „pre-deploy-sprachcheck" laufen lassen, '
              'dann erneut deployen.\n')
        sys.exit(2)
    sys.stderr.write('Pre-Deploy-Lint: keine GROSSBUCHSTABEN-Probleme auf den Hub-Seiten. ✓\n')
    sys.exit(0)

if __name__ == '__main__':
    main()
