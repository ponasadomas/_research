# usage: python3 -I build.py <niche_dir> <spec.py>...  -> writes voice file + restricted list
import json, re, sys, os, runpy
niche = sys.argv[1]
recs = []
for spec in sys.argv[2:]:
    recs += runpy.run_path(spec)['R']
def sections(txt):
    # returns dict: '' -> (date,url,body) for post, cid -> ...
    out = {}
    parts = re.split(r'(?m)^(POST \S+ \|.*|COMMENT \S+ \|.*)$', txt)
    for i in range(1, len(parts), 2):
        h = parts[i]; body = parts[i+1]
        m = re.match(r'(POST|COMMENT) (\S+) \| (?:r/\S+ \| )?(\d{4}-\d\d-\d\d)[^|]*\| (\S+)', h)
        kind, pid, date, url = m.groups()
        out['' if kind == 'POST' else pid] = (date, url, body)
    return out
ov = runpy.run_path(os.path.join(niche,'scratchpad/PR07/rs_override.py'))
lines = []; restricted = []
for n, r in enumerate(recs, 1):
    rid = 'pb07-%04d' % n
    raw_file = '../_shared/_raw/reddit-2026/units/%s.txt' % r['u']
    txt = open(os.path.join(niche, raw_file), encoding='utf-8').read()
    sec = sections(txt)
    date, url, body = sec[r.get('c', '')]
    pieces = []
    for s, e in r['q']:
        a = body.find(s)
        if a < 0: sys.exit('%s start not found: %r' % (rid, s))
        b = body.find(e, a) if e else a
        if b < 0: sys.exit('%s end not found: %r' % (rid, e))
        pieces.append(body[a:b + len(e)] if e else s)
    quote = ' […] '.join(p.strip() for p in pieces)
    sub = r['u'].split('-')[0]; pid = r['u'].split('-', 1)[1]
    rec = dict(id=rid, source='reddit r/' + sub, url=url, date=date, speaker=r['sp'], stage=r['st'],
               type=r['t'], themes=r['th'], quote=quote, context=r['cx'], raw_file=raw_file,
               source_class='reddit_archive', post_id=pid)
    if r.get('c'): rec['comment_id'] = r['c']
    if len(r['cx'].split()) > 25: sys.exit('%s context too long' % rid)
    lines.append(json.dumps(rec, ensure_ascii=False))
    reason = ov['OV'].get(rid) if n <= ov['UPTO'] else r.get('rs')
    if reason: restricted.append('- %s — %s' % (rid, reason))
open(os.path.join(niche, 'voice/reddit-pr07.jsonl'), 'w').write('\n'.join(lines) + '\n')
open(os.path.join(niche, 'scratchpad/PR07/restricted.txt'), 'w').write('\n'.join(restricted) + '\n')
print(len(lines), 'records;', len(restricted), 'restricted')
