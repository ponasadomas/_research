# usage: python3 -I add.py batch.py  -- batch.py defines R = [ (unit, cid, speaker, stage, type, themes, quote, context, restricted) ]
import json, re, sys, os
B = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(B, '..', '..'))
VOICE = os.path.join(NICHE, 'voice', 'reddit-pr12.jsonl')
RESTR = os.path.join(B, 'restricted.tsv')
ns = {}
exec(open(sys.argv[1]).read(), ns)
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = open(VOICE, 'a'); rf = open(RESTR, 'a')
for unit, cid, sp, st, ty, th, q, ctx, restr in ns['R']:
    rawp = '../_shared/_raw/reddit-2026/units/%s.txt' % unit
    txt = open(os.path.join(NICHE, rawp), encoding='utf-8').read()
    sub, pid = unit.split('-', 1)
    m = re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', txt, re.M)
    url, date = m.group(4), m.group(3)
    rec = {}
    if cid:
        mc = re.search(r'^COMMENT %s \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$' % cid, txt, re.M)
        assert mc, (unit, cid)
        url, date = mc.group(2), mc.group(1)
    assert len(ctx.split()) <= 25, ctx
    n += 1
    i = 'pb12-%04d' % n
    rec = {'id': i, 'source': 'reddit r/' + m.group(2), 'url': url, 'date': date, 'speaker': sp, 'stage': st,
           'type': ty, 'themes': th, 'quote': q, 'context': ctx, 'raw_file': rawp, 'source_class': 'reddit_archive', 'post_id': pid}
    if cid: rec['comment_id'] = cid
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
    if restr: rf.write('%s\t%s\n' % (i, restr))
    print(i, unit, q[:50])
