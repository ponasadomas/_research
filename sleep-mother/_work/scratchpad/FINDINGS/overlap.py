#!/usr/bin/env python3
"""Posts (units) quoted in both sleep-mother and sleep-baby merged files, by post_id or URL post segment."""
import json, re, collections, os
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..','..'))
def pid(r):
    m=re.search(r'/comments/([a-z0-9]+)',r.get('url',''))
    return r.get('post_id') or (m.group(1) if m else None)
def load(n): return [json.loads(l) for l in open(os.path.join(ROOT,n,'voice-merged','all.jsonl')) if l.strip()]
sm=load('sleep-mother'); sb=load('sleep-baby')
smp=collections.defaultdict(list)
for r in sm: smp[pid(r)].append(r)
sbp={pid(r) for r in sb}
both=[p for p in smp if p in sbp]
q=[r for p in both for r in smp[p]]
print('sleep-mother quoted units',len(smp),'| also quoted in sleep-baby',len(both),'| sleep-mother quotes from those units',len(q))
print('stage of those quotes',collections.Counter(r['stage'] for r in q).most_common())
print('source of those quotes',collections.Counter(r['source'] for r in q).most_common())
preg=[r for r in sm if r['stage'].startswith('pregnancy')]
print('pregnancy-stage quotes (all sleep-mother)',len(preg),'| of them in shared units',sum(1 for r in preg if pid(r) in sbp))
th=collections.Counter()
for r in sm:
    if pid(r) not in sbp: th.update(r['themes'])
print('top themes in units NOT in sleep-baby',th.most_common(12))
