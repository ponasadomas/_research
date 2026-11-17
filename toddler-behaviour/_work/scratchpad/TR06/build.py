# Build voice records from scratchpad/TR06/q/*.json (lists of [unit_no, comment_id|null, speaker, stage, type, themes, quote, context])
import json, re, glob, os, sys
B = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(B, '..', '..'))
units = [l.split()[1] for l in open(os.path.join(B, 'units.txt')) if len(l.split()) == 3]
recs = []
for f in sorted(glob.glob(os.path.join(B, 'q', '*.json'))):
    recs += json.loads(open(f).read(), strict=False)
out = []; n = 0
for r in recs:
    un, cid, sp, st, ty, th, q, ctx = r; q = re.sub(r"\s*\n\s*", " ", q)
    u = units[un - 1]
    t = open(os.path.join(NICHE, u), encoding='utf-8').read()
    m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', t)
    pid, sub, date, url = m.groups()
    if cid:
        mc = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', t)
        assert mc, (un, cid)
        date, url = mc.groups()
    assert len(ctx.split()) <= 25, ctx
    SEED=open(os.path.join(NICHE,'README.md')).read().split('Seed themes')[1].split('The other side')[0]
    th=[t for t in th if '`'+t+'`' in SEED]+[t for t in th if '`'+t+'`' not in SEED]
    n += 1
    d = {"id": f"tb06-{n:04d}", "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": sp, "stage": st,
         "type": ty, "themes": th, "quote": q, "context": ctx, "raw_file": u, "source_class": "reddit_archive", "post_id": pid}
    if cid: d["comment_id"] = cid
    out.append(d)
with open(os.path.join(NICHE, 'voice', 'reddit-tr06.jsonl'), 'w') as fo:
    for d in out: fo.write(json.dumps(d, ensure_ascii=False) + '\n')
print(len(out))
