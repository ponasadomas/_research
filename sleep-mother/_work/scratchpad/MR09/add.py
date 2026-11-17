#!/usr/bin/env python3
"""Build voice/reddit-mr09.jsonl from drafts/*.jsonl (rebuilds whole file each run, ids in draft order)."""
import json, re, glob, os, sys
NICHE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SEED = [l.strip() for l in open(os.path.join(os.path.dirname(__file__), 'seed.txt')) if l.strip()]
UNITDIR = '../_shared/_raw/reddit-2026/units/'
out = []
n = 0
for d in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'drafts', '*.jsonl'))):
    for line in open(d, encoding='utf-8'):
        if not line.strip(): continue
        r = json.loads(line)
        u = r['u'] if r['u'].endswith('.txt') else r['u'] + '.txt'
        raw_file = UNITDIR + u
        text = open(os.path.join(NICHE, raw_file), encoding='utf-8').read()
        m = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', text)
        post_id, sub, pdate, purl = m.groups()
        rec_url, rec_date = purl, pdate
        cid = r.get('c')
        if cid:
            cm = re.search(r'COMMENT ' + re.escape(cid) + r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', text)
            if not cm: sys.exit('no comment ' + cid + ' in ' + u)
            rec_date, rec_url = cm.groups()
        n += 1
        rec = {"id": f"sm09-{n:04d}", "source": f"reddit r/{sub}", "url": rec_url, "date": rec_date,
               "speaker": r['sp'], "stage": r['st'], "type": r['ty'], "themes": sorted(r['th'], key=lambda t: (t not in SEED, SEED.index(t) if t in SEED else 0)), "quote": r['q'],
               "context": r['cx'], "raw_file": raw_file, "source_class": "reddit_archive", "post_id": post_id}
        if cid: rec["comment_id"] = cid
        if r.get('R'): restricted = True
        out.append((rec, bool(r.get('R'))))
with open(os.path.join(NICHE, 'voice', 'reddit-mr09.jsonl'), 'w', encoding='utf-8') as f:
    for rec, _ in out: f.write(json.dumps(rec, ensure_ascii=False) + '\n')
with open(os.path.join(os.path.dirname(__file__), 'restricted.txt'), 'w') as f:
    for rec, R in out:
        if R: f.write(rec['id'] + '\t' + rec['post_id'] + '\n')
print(n, 'records;', sum(R for _, R in out), 'restricted')
