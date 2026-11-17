# Build R05 voice file from scratchpad/R05/q-*.json (lists of compact records).
import json, glob, os, re, sys
NICHE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
UNITS = '../_shared/_raw/reddit-2026/units/'
out = []
n = 0
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'q-*.json'))):
    for r in json.load(open(f)):
        unit = r['u']; raw_file = UNITS + unit + '.txt'
        text = open(os.path.join(NICHE, raw_file), encoding='utf-8').read()
        m = re.search(r'^POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', text, re.M)
        post_id, sub, date, url = m.groups()
        rec = {}
        cid = r.get('c')
        if cid:
            cm = re.search(r'^COMMENT ' + cid + r' \| (\d{4}-\d\d-\d\d) .*?\| (\S+)$', text, re.M)
            date, url = cm.groups()
        n += 1
        rec = {'id': 'sb05-%04d' % n, 'source': 'reddit r/' + sub, 'url': url, 'date': date,
               'speaker': r['sp'], 'stage': r['st'], 'type': r['t'], 'themes': r['th'],
               'quote': r['q'], 'context': r['x'], 'raw_file': raw_file,
               'source_class': 'reddit_archive', 'post_id': post_id}
        if cid: rec['comment_id'] = cid
        assert len(r['x'].split()) <= 25, r['x']
        out.append(rec)
with open(os.path.join(NICHE, 'voice', 'reddit-r05.jsonl'), 'w') as fh:
    for rec in out: fh.write(json.dumps(rec, ensure_ascii=False) + '\n')
print(len(out))
