#!/usr/bin/env python3
# Rebuilds voice/reddit-pr57.jsonl from scratchpad/PR57/recs/rec-*.py (each defines R = [ (unit, cid, speaker, stage, type, themes, quote, context, restricted), ... ])
import json, re, glob, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(HERE, '..', '..'))
UNITS = '../_shared/_raw/reddit-2026/units/'
out = []; restricted = []
for f in sorted(glob.glob(os.path.join(HERE, 'recs', 'rec-*.py'))):
    ns = {}; exec(open(f).read(), ns)
    for r in ns['R']:
        unit, cid, sp, st, ty, th, q, ctx, rs = r
        rf = UNITS + unit + '.txt'
        txt = open(os.path.join(NICHE, rf), encoding='utf-8').read()
        m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        pid, sub, date, url = m.groups()
        if cid:
            mc = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
            if not mc: sys.exit('no comment %s in %s' % (cid, unit))
            date, url = mc.groups()
        assert len(ctx.split()) <= 25, ctx
        n = len(out) + 1
        rec = {"id": "pb57-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": sp, "stage": st, "type": ty, "themes": th, "quote": q, "context": ctx, "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
        if cid: rec["comment_id"] = cid
        out.append(rec)
        if rs: restricted.append(rec["id"])
with open(os.path.join(NICHE, 'voice', 'reddit-pr57.jsonl'), 'w', encoding='utf-8') as fo:
    for r in out: fo.write(json.dumps(r, ensure_ascii=False) + '\n')
open(os.path.join(HERE, 'restricted.txt'), 'w').write(', '.join(restricted) + '\n')
print(len(out), 'records;', len(restricted), 'restricted')
