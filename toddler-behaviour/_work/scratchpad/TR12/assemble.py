import json, re, glob, os, sys
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(base, '..', '..')
units = {}
for line in open(os.path.join(base, 'units.txt')):
    c, u = line.rstrip('\n').split('\t')
    units[os.path.basename(u)[:-4]] = u
out = []; restricted = []
n = 0
for f in sorted(glob.glob(os.path.join(base, 's[0-9][0-9].jsonl'))):
    for line in open(f):
        if not line.strip(): continue
        r = json.loads(line)
        u = units[r['u']]
        txt = open(os.path.join(root, u), encoding='utf-8').read()
        m = re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt, re.M)
        pid, sub, date, url = m.groups()
        if r['c']:
            cm = re.search(r'^COMMENT ' + re.escape(r['c']) + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt, re.M)
            if not cm: sys.exit('no comment ' + r['c'])
            date, url = cm.groups()
        n += 1
        rid = 'tb12-%04d' % n
        rec = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date,
               "speaker": r['sp'], "stage": r['st'], "type": r['ty'], "themes": r['th'],
               "quote": r['q'].replace('[...]', '[…]'), "context": r['cx'], "raw_file": u,
               "source_class": "reddit_archive", "post_id": pid}
        if r['c']: rec['comment_id'] = r['c']
        if len(r['cx'].split()) > 25: print('long context', rid)
        out.append(rec)
        if r.get('r'): restricted.append((rid, r['u']))
with open(os.path.join(root, 'voice', 'reddit-tr12.jsonl'), 'w', encoding='utf-8') as fo:
    for rec in out: fo.write(json.dumps(rec, ensure_ascii=False) + '\n')
with open(os.path.join(base, 'restricted.tsv'), 'w') as fo:
    for a, b in restricted: fo.write(a + '\t' + b + '\n')
print(n, 'records', len(restricted), 'restricted')
