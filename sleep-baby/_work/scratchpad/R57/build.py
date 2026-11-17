# Builds voice/reddit-r57.jsonl from scratchpad/R57/q*.tsv (short-form sources).
# Line: unit_basename || comment_id or - || speaker || stage || type || themes,comma || quote || context[ || R]
import glob, json, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(H, '..', '..')
UP = '../_shared/_raw/reddit-2026/units/'
recs = []; restricted = []; n = 0
for f in sorted(glob.glob(os.path.join(H, 'q*.tsv'))):
    for ln, line in enumerate(open(f, encoding='utf-8'), 1):
        line = line.rstrip('\n')
        if not line.strip() or line.startswith('#'):
            continue
        p = line.split(' || ')
        if len(p) not in (8, 9):
            sys.exit(f'{f}:{ln} has {len(p)} fields')
        unit, cid, sp, st, ty, th, q, ctx = p[:8]
        raw = UP + unit
        text = open(os.path.join(SB, raw), encoding='utf-8').read()
        m = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', text)
        pid, sub, date, url = m.groups()
        r = {}
        if cid != '-':
            cm = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)', text)
            if not cm:
                sys.exit(f'{f}:{ln} comment {cid} not in {unit}')
            date, url = cm.groups()
        n += 1
        rid = 'sb57-%04d' % n
        if len(ctx.split()) > 25:
            sys.exit(f'{f}:{ln} context too long')
        rec = {'id': rid, 'source': 'reddit r/' + sub, 'url': url, 'date': date, 'speaker': sp, 'stage': st,
               'type': ty, 'themes': [t.strip() for t in th.split(',') if t.strip()], 'quote': q, 'context': ctx,
               'raw_file': raw, 'source_class': 'reddit_archive', 'post_id': pid}
        if cid != '-':
            rec['comment_id'] = cid
        recs.append(rec)
        if len(p) == 9 and p[8] == 'R':
            restricted.append(rid)
with open(os.path.join(SB, 'voice', 'reddit-r57.jsonl'), 'w', encoding='utf-8') as o:
    for r in recs:
        o.write(json.dumps(r, ensure_ascii=False) + '\n')
restricted += [x.strip() for x in open(os.path.join(H, 'restricted_extra.txt')) if x.strip()]
restricted = sorted(set(restricted))
open(os.path.join(H, 'restricted.txt'), 'w').write('\n'.join(restricted) + '\n')
print(len(recs), 'records;', len(restricted), 'restricted')
