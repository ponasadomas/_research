#!/usr/bin/env python3
"""Assemble RV1 drafts into voice/reviews-rv1.jsonl (ids pbr1-NNNN in draft order)."""
import json, glob, os, re
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
NAMES = {'flo':'Flo','babycenter':'BabyCenter','wte':'What to Expect','ovia':'Ovia','pregnancyplus':'Pregnancy+','thebump':'The Bump',
 'gentlebirth':'GentleBirth','christianhypno':'Christian Hypnobirthing','freya':'Freya (Positive Birth Company)','everymother':'Every Mother','expect':'Expect','expectful':'Expectful'}
units = {}
for f in glob.glob(os.path.join(ROOT, '_raw/reviews/*.units.json')):
    d = json.load(open(f))
    for r in d['reviews']:
        units[f"{d['app']}-{d['country']}-{r['id']}"] = (d, r)
out, restricted = [], []
for df in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'drafts-*.jsonl'))):
    for line in open(df):
        if not line.strip(): continue
        q = json.loads(line)
        rid = q['rid']
        if rid in units:
            d, r = units[rid]
            rec = dict(source=f"App Store {d['country']} {NAMES[d['app']]}", url=d['url'], date=r['date'][:10],
                       raw_file=d['corpus_file'], source_class='app_review', rating=r['rating'])
        else:
            rec = dict(source=q['source'], url=q['url'], date=q['date'], raw_file=q['raw_file'],
                       source_class=q.get('source_class', 'book_review' if 'book' in q['raw_file'] else 'app_review'), rating=q.get('rating'))
        n = len(out) + 1
        row = dict(id=f"pbr1-{n:04d}", source=rec['source'], url=rec['url'], date=rec['date'], speaker='reviewer',
                   stage=q['stage'], type=q['type'], themes=q['themes'], quote=q['quote'], context=q['context'],
                   raw_file=rec['raw_file'], source_class=rec['source_class'], review_id=rid, rating=rec['rating'])
        if q.get('r'):
            row['restricted'] = True; row['restricted_reason'] = q['r']; restricted.append((row['id'], q['r']))
        assert len(q['context'].split()) <= 25, (rid, len(q['context'].split()))
        out.append(row)
with open(os.path.join(ROOT, 'voice/reviews-rv1.jsonl'), 'w') as f:
    for row in out: f.write(json.dumps(row, ensure_ascii=False) + '\n')
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'restricted.tsv'), 'w') as f:
    for i, r in restricted: f.write(f"{i}\t{r}\n")
print(len(out), 'quotes;', len(restricted), 'restricted')
