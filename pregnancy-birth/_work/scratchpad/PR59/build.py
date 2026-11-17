import json, re, html, sys, glob, os
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(base, '..', '..')
units = [l.rstrip('\n').split('\t')[1] for l in open(os.path.join(base,'units.tsv'))]
byname = {os.path.basename(u)[:-4]: u for u in units}
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
out = []; restricted = []; n = 0; bad = 0
for f in sorted(glob.glob(os.path.join(base, 'c0*.jsonl'))):
    for line in open(f):
        if not line.strip(): continue
        c = json.loads(line)
        rf = byname[c['u']]
        txt = open(os.path.join(root, rf), encoding='utf-8').read()
        head = txt.splitlines()[0]
        m = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', head)
        pid, sub, date, url = m.groups()
        if c['c']:
            mm = re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)' % c['c'], txt)
            date, url = mm.group(1), mm.group(2)
            seg = txt[mm.start():]
            nxt = re.search(r'\nCOMMENT |\Z', seg[10:]); seg = seg[:10+nxt.start()] if nxt else seg
        else:
            seg = txt.split('--- ORIGINAL POSTER')[0]
        q = re.sub(r'[ \t]*\n[ \t]*', ' ', c['q']).strip()
        T = norm(seg); pos = 0
        for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", q):
            p = norm(piece)
            at = T.find(p, pos)
            if at < 0: print('MISS', c['u'], c['c'], p[:80]); bad += 1; break
            pos = at + len(p)
        n += 1
        rid = 'pb59-%04d' % n
        rec = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": c['sp'], "stage": c['st'], "type": c['ty'], "themes": c['th'], "quote": q, "context": c['cx'], "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
        if c['c']: rec['comment_id'] = c['c']
        if len(c['cx'].split()) > 25: print('LONGCTX', rid)
        out.append(rec)
        if c['r']: restricted.append(rid)
print(n, 'records', bad, 'missing in own segment')
if bad == 0 and '--write' in sys.argv:
    with open(os.path.join(root, 'voice', 'reddit-pr59.jsonl'), 'w') as fo:
        for r in out: fo.write(json.dumps(r, ensure_ascii=False) + '\n')
    open(os.path.join(base, 'restricted.txt'), 'w').write('\n'.join(restricted) + '\n')
    json.dump({r['id']: (r['raw_file'].split('/')[-1], r.get('comment_id','')) for r in out}, open(os.path.join(base,'idmap.json'),'w'), indent=0)
    print('written; restricted', len(restricted))
