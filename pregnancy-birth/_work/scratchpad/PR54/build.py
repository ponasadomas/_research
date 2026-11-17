# Build reddit-pr54.jsonl from scratch record files rec-*.py (each defines R = list of dicts)
import json, re, glob, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(BASE, '..', '..'))
UNITS = '../_shared/_raw/reddit-2026/units/'
def meta(unit, cid):
    path = os.path.join(NICHE, UNITS + unit + '.txt')
    txt = open(path, encoding='utf-8').read()
    first = txt.splitlines()[0]
    m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*\| (\S+)$', first)
    pid, sub, date, url = m.groups()
    if cid:
        m2 = re.search(r'COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        date, url = m2.groups()
    return pid, sub, date, url
out = []
restricted = []
n = 0
for f in sorted(glob.glob(os.path.join(BASE, 'recs', 'rec-*.py'))):
    ns = {}
    exec(open(f, encoding='utf-8').read(), ns)
    for r in ns['R']:
        n += 1
        unit, cid = r['u'], r.get('c')
        pid, sub, date, url = meta(unit, cid)
        rec = {"id": "pb54-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date,
               "speaker": r['sp'], "stage": r['st'], "type": r['ty'], "themes": r['th'],
               "quote": r['q'], "context": r['cx'], "raw_file": UNITS + unit + '.txt',
               "source_class": "reddit_archive", "post_id": pid}
        if cid: rec["comment_id"] = cid
        if r.get('restricted'): restricted.append(rec['id'])
        if len(r['cx'].split()) > 25: print('LONG CONTEXT', rec['id'], file=sys.stderr)
        out.append(rec)
with open(os.path.join(NICHE, 'voice', 'reddit-pr54.jsonl'), 'w', encoding='utf-8') as fh:
    for rec in out: fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(len(out), 'records')
open(os.path.join(BASE,'restricted.txt'),'w').write('\n'.join(restricted)+'\n')
print(len(restricted),'restricted')
