import json, re, glob, os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SP = {'nm':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','rc':'relative_caregiver','sk':'skeptic'}
ST = {'nb':'newborn_0_8_weeks','b2':'baby_2_4_months','r4':'regression_4_months','b5':'baby_5_8_months','b9':'baby_9_12_months','t1':'toddler_12_24_months','t2':'toddler_24_36_months','lb':'looking_back','u':'unknown'}
recs = []
n = 0
for f in sorted(glob.glob(os.path.join(os.path.dirname(__file__), 'q*.jsonl'))):
    for line in open(f):
        if not line.strip(): continue
        r = json.loads(line)
        uf = '../_shared/_raw/reddit-2026/units/%s.txt' % r['u']
        txt = open(os.path.join(ROOT, uf), encoding='utf-8').read()
        m = re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        pid, sub, date, url = m.groups()
        cid = r.get('c')
        if cid:
            mc = re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)' % re.escape(cid), txt)
            date, url = mc.groups()
        n += 1
        o = {'id': 'sb48-%04d' % n, 'source': 'reddit r/' + sub, 'url': url, 'date': date,
             'speaker': SP.get(r['sp'], r['sp']), 'stage': ST.get(r['st'], r['st']), 'type': r['ty'],
             'themes': r['th'], 'quote': r['q'], 'context': r['cx'], 'raw_file': uf,
             'source_class': 'reddit_archive', 'post_id': pid}
        if cid: o['comment_id'] = cid
        if len(r['cx'].split()) > 25: print('LONG CONTEXT', o['id'], file=sys.stderr)
        recs.append(o)
        if r.get('r'): print('RESTRICTED', o['id'])
        if r.get('tag'): print('TAG', r['tag'], o['id'])
with open(os.path.join(ROOT, 'voice', 'reddit-r48.jsonl'), 'w') as out:
    for o in recs: out.write(json.dumps(o, ensure_ascii=False) + '\n')
print(len(recs), 'records')
