#!/usr/bin/env python3
"""Verify ids and exact quoted strings in the findings/opportunity documents.

Use `“verbatim words” [id]`, or an [id] line immediately before a blockquote.
An id-before-blockquote may contain a contiguous source fragment. Complete-field
coverage in the recovery evidence is checked separately by verify_reread_merge.py.
Other [ids] are evidence links; their semantic support requires editorial review.
"""
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
records = [q for p in (ROOT/'voice').glob('*.jsonl') for l in p.read_text().splitlines() if l.strip() for q in [json.loads(l)]]
rows = {q['id']: q for q in records}
bad = []; checked = pairs = 0
if len(rows) != len(records): bad.append('Duplicate voice ids')
paths = [Path(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [ROOT/'synthesis'/x for x in ['findings.md', 'niche-opportunities.md', 'success-stories.md', 'purchase-evidence.md', 'evidence.md', 'quote-index.md']]
norm = lambda s: re.sub(r'\s+', ' ', s).strip()
for p in paths:
    name = p.name
    if not p.exists(): bad.append(f'{name}: missing'); continue
    s = p.read_text()
    for id in re.findall(r'\[([a-z][a-z0-9]*-\d+)\]', s):
        checked += 1
        if id not in rows: bad.append(f'{name}: unknown id {id}')
    for quoted, id in re.findall(r'“([^”\n]+)”[ \t]*\[([a-z][a-z0-9]*-\d+)\]', s):
        pairs += 1
        if id in rows and quoted != rows[id]['quote']: bad.append(f'{name}: quoted words differ from {id}')
    lines = s.splitlines()
    for n, line in enumerate(lines):
        m = re.fullmatch(r'\[([a-z][a-z0-9]*-\d+)\]', line)
        if not m or n + 1 >= len(lines) or not lines[n+1].startswith('>'): continue
        id = m[1]; parts = []; k = n + 1
        while k < len(lines) and lines[k].startswith('>'):
            parts.append(lines[k][2:] if lines[k].startswith('> ') else lines[k][1:]); k += 1
        pairs += 1
        if id not in rows or not norm('\n'.join(parts)) or norm('\n'.join(parts)) not in norm(rows[id]['quote']):
            bad.append(f'{name}: blockquote differs from {id}')
print(f'TOTAL {checked} id references, {pairs} exact quote pairs, {len(bad)} failed')
for e in bad: print(e)
sys.exit(bool(bad))
