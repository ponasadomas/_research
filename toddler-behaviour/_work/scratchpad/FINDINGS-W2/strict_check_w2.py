#!/usr/bin/env python3
"""Check cited ids and quoted fragments; historical markings have no effect."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
recs = {}
for path in sorted((ROOT / 'voice').glob('*.jsonl')):
    for line in path.read_text(encoding='utf-8').splitlines():
        if line.strip():
            record = json.loads(line)
            recs[record['id']] = record
text = Path(sys.argv[1]).read_text(encoding='utf-8')
text = text[text.index('## 16. '):]
def norm(value):
    value = value.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"').replace(' ', ' ')
    return re.sub(r'\s+', ' ', value).strip()
ids = set(re.findall(r'\b(tb(?:r1|\d{2})-\d{4})\b', text))
unresolved = sorted(ids - recs.keys())
for rid in unresolved:
    print('UNRESOLVED', rid)
bad = checked = 0
for match in re.finditer(r'"([^"\n]{3,}?)"\s*\[(tb(?:r1|\d{2})-\d{4})\]', text):
    fragment, rid = match.groups()
    checked += 1
    if rid not in recs or norm(fragment) not in norm(recs[rid]['quote']):
        bad += 1
        print('FAIL', rid, repr(fragment[:80]))
print(f'{len(ids)} ids, {len(unresolved)} unresolved; checked {checked} fragments, {bad} failed')
sys.exit(1 if bad or unresolved else 0)
