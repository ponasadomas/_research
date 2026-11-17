# Build voice/reddit-pr21.jsonl from scratch records q*.py (each defines R = [ ... ])
import json, re, glob, os, sys
NICHE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UP = '../_shared/_raw/reddit-2026/units/'
recs = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'q1*.py'))):
    ns = {}
    exec(open(f).read(), ns)
    recs += ns['R']
out = []; restricted = []
for n, r in enumerate(recs, 1):
    unit, cid, spk, stg, typ, th, quote, ctx = r[:8]
    rest = r[8] if len(r) > 8 else None
    rawf = UP + unit + '.txt'
    text = open(os.path.join(NICHE, rawf), encoding='utf-8').read()
    m = re.search(r'^POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', text, re.M)
    pid, sub, date, url = m.groups()
    if cid:
        mc = re.search(r'^COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', text, re.M)
        if not mc: sys.exit('no comment ' + cid + ' in ' + unit)
        date, url = mc.groups()
    rid = 'pb21-%04d' % n
    d = dict(id=rid, source='reddit r/' + sub, url=url, date=date, speaker=spk, stage=stg, type=typ,
             themes=th, quote=quote, context=ctx, raw_file=rawf, source_class='reddit_archive', post_id=pid)
    if cid: d['comment_id'] = cid
    if len(ctx.split()) > 25: print('LONG CONTEXT', rid, len(ctx.split()))
    out.append(d)
    if rest: restricted.append((rid, rest))
with open(os.path.join(NICHE, 'voice/reddit-pr21.jsonl'), 'w', encoding='utf-8') as fo:
    for d in out: fo.write(json.dumps(d, ensure_ascii=False) + '\n')
with open(os.path.join(os.path.dirname(__file__), 'restricted.txt'), 'w') as fo:
    for rid, why in restricted: fo.write(f'- {rid} — {why}\n')
print(len(out), 'records,', len(restricted), 'restricted')
