import json, re, os, sys
base = os.path.dirname(os.path.abspath(__file__))
niche = os.path.abspath(os.path.join(base, '..', '..'))
S_all = []
for i in range(1, 7):
    ns = {}
    exec(open(os.path.join(base, f'spec{i}.py'), encoding='utf-8').read(), ns)
    S_all += ns['S']
U = '../_shared/_raw/reddit-2026/units/'
def norm(s): return re.sub(r'\s+', ' ', s).strip()
def pat(q):
    out = ''
    for ch in norm(q):
        if ch in "'’‘": out += "['’‘]"
        elif ch in '"“”': out += '["“”]'
        elif ch == ' ': out += r'\s+'
        else: out += re.escape(ch)
    return out
def sections(text):
    # split into header->body
    parts = re.split(r'\n(?=(?:POST|COMMENT) \S+ \| )', '\n' + text)
    secs = []
    for p in parts:
        p = p.strip('\n')
        if not p: continue
        hdr, _, body = p.partition('\n')
        m = re.match(r'(POST|COMMENT) (\S+) \| (?:r/\S+ \| )?(\d{4}-\d{2}-\d{2}) [^|]*\| (\S+)', hdr)
        secs.append((m.group(1), m.group(2), m.group(3), m.group(4), body))
    return secs
recs = []; errs = 0; restricted = []
for n, (unit, cid, spk, stg, typ, th, q, ctx, r) in enumerate(S_all, 1):
    rf = U + unit + '.txt'
    text = open(os.path.join(niche, rf), encoding='utf-8').read()
    secs = sections(text)
    if cid is None:
        sec = [s for s in secs if s[0] == 'POST'][0]
    else:
        sec = [s for s in secs if s[1] == cid][0]
    body = sec[4]
    m = re.search(pat(q), body)
    if not m:
        print('NOT FOUND', unit, cid, q[:60]); errs += 1; continue
    orig = m.group(0)
    sub = unit.split('-')[0]; pid = unit.split('-', 1)[1]
    rid = 'pb35-%04d' % (len(recs) + 1)
    rec = {'id': rid, 'source': 'reddit r/' + sub, 'url': sec[3], 'date': sec[2], 'speaker': spk, 'stage': stg,
           'type': typ, 'themes': th, 'quote': orig, 'context': ctx, 'raw_file': rf,
           'source_class': 'reddit_archive', 'post_id': pid}
    if cid: rec['comment_id'] = cid
    if len(ctx.split()) > 25: print('LONG CONTEXT', rid, len(ctx.split()))
    recs.append(rec)
    if r: restricted.append(rid)
if errs: sys.exit(1)
with open(os.path.join(niche, 'voice', 'reddit-pr35.jsonl'), 'w', encoding='utf-8') as f:
    for r in recs: f.write(json.dumps(r, ensure_ascii=False) + '\n')
json.dump(restricted, open(os.path.join(base, 'restricted.json'), 'w'))
print(len(recs), 'records;', len(restricted), 'restricted:', ', '.join(restricted))
