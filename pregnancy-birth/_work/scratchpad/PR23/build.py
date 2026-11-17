# Build voice records from spec files spec_*.py (each defines R = list of dicts with
# u (unit basename w/o .txt), c (comment id or None), sp, st, ty, th, q, cx, r (restricted reason or None))
import json, re, glob, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.join(BASE, '..', '..')
UNITDIR = '../_shared/_raw/reddit-2026/units/'
out = []
restricted = []
for f in sorted(glob.glob(os.path.join(BASE, 'spec_*.py'))):
    ns = {}
    exec(open(f).read(), ns)
    out.extend(ns['R'])
recs = []
for i, s in enumerate(out, 1):
    if s['ty']=='price_signal' and 'price_value' not in s['th']:
        s['th']=['price_value']+s['th']
    rf = UNITDIR + s['u'] + '.txt'
    txt = open(os.path.join(NICHE, rf), encoding='utf-8').read()
    m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
    pid, sub, date, url = m.groups()
    rec = {'id': 'pb23-%04d' % i, 'source': 'reddit r/' + sub, 'url': url, 'date': date,
           'speaker': s['sp'], 'stage': s['st'], 'type': s['ty'], 'themes': s['th'],
           'quote': s['q'], 'context': s['cx'], 'raw_file': rf, 'source_class': 'reddit_archive', 'post_id': pid}
    if s.get('c'):
        cm = re.search(r'COMMENT ' + s['c'] + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        rec['date'], rec['url'] = cm.group(1), cm.group(2)
        rec['comment_id'] = s['c']
    assert len(s['cx'].split()) <= 25, (rec['id'], len(s['cx'].split()))
    recs.append(rec)
    if s.get('r'):
        restricted.append((rec['id'], s['r']))
with open(os.path.join(NICHE, 'voice', 'reddit-pr23.jsonl'), 'w') as fh:
    for r in recs:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(os.path.join(BASE, 'restricted.txt'), 'w') as fh:
    for a, b in restricted:
        fh.write(f'- {a} — {b}\n')
# per-unit id ranges
from collections import OrderedDict
d = OrderedDict()
for s, r in zip(out, recs):
    d.setdefault(s['u'], []).append(r['id'])
with open(os.path.join(BASE, 'unit_ids.json'), 'w') as fh:
    json.dump(d, fh, indent=0)
print(len(recs), 'records,', len(restricted), 'restricted')
