import json, re, sys, os, glob
base = os.path.dirname(os.path.abspath(__file__))
nich = os.path.normpath(os.path.join(base, '..', '..'))
chunks = json.load(open(os.path.join(base, 'chunks.json')))
order = ['read-v1a-keep_success-00%d' % i for i in range(1, 7)] + ['read-v1a-keep_otherside-001', 'read-v1a-keep_otherside-002']
paths = {}
for d in chunks:
    for u in d['units']:
        paths[os.path.basename(u)[:-4]] = u
recs = []
def R(unit, cid, sp, st, ty, th, q, cx):
    recs.append((unit, cid, sp, st, ty, th, q, cx))
for f in ['q_s1.py','q_s2.py','q_s3.py','q_s4.py','q_s5.py','q_s6.py','q_o1.py','q_o2.py']:
    p = os.path.join(base, f)
    if os.path.exists(p):
        exec(open(p).read())
out = []
problems = []
for i, (unit, cid, sp, st, ty, th, q, cx) in enumerate(recs, 1):
    rf = paths[unit]
    txt = open(os.path.join(nich, rf)).read()
    m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)', txt)
    pid, sub, date, url = m.groups()
    rec = {'id': 'sb02-%04d' % i, 'source': 'reddit r/' + sub, 'url': url, 'date': date}
    if cid:
        cm = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)', txt)
        rec['url'] = cm.group(2); rec['date'] = cm.group(1)
    themes = th.split(',')
    rec.update({'speaker': sp, 'stage': st, 'type': ty, 'themes': themes, 'quote': q, 'context': cx,
                'raw_file': rf, 'source_class': 'reddit_archive', 'post_id': pid})
    if cid: rec['comment_id'] = cid
    if len(cx.split()) > 25: problems.append((rec['id'], 'context words', len(cx.split())))
    if re.search(r'\bu/|\bOP\b', q + cx): problems.append((rec['id'], 'username/OP'))
    out.append(rec)
open(os.path.join(nich, 'voice', 'reddit-r02.jsonl'), 'w').write(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in out))
print(len(out), 'records'); print(problems)
