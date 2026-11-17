# Build voice/reddit-r63.jsonl from scratchpad/R63/q*.py spec files (lists named Q).
import json, re, os, glob, sys
BASE = os.path.dirname(os.path.abspath(__file__)) + '/../..'
UD = '../_shared/_raw/reddit-2026/units/'
def meta(unit):
    txt = open(os.path.join(BASE, UD + unit + '.txt'), encoding='utf-8').read()
    m = re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
    com = {c: (d, u) for c, d, u in re.findall(r'^COMMENT (\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt, re.M)}
    return m.groups(), com
recs, restricted, n = [], [], 0
for f in sorted(glob.glob(os.path.join(BASE, 'scratchpad/R63/q*.py'))):
    ns = {}; exec(open(f).read(), ns)
    for e in ns['Q']:
        (pid, sub, pdate, purl), com = meta(e['u'])
        n += 1; rid = 'sb63-%04d' % n
        r = {'id': rid, 'source': 'reddit r/' + sub}
        if e.get('c'):
            d, u = com[e['c']]; r['url'] = u; r['date'] = d
        else:
            r['url'] = purl; r['date'] = pdate
        r.update(speaker=e['sp'], stage=e['st'], type=e['ty'], themes=e['th'], quote=e['q'], context=e['cx'],
                 raw_file=UD + e['u'] + '.txt', source_class='reddit_archive', post_id=pid)
        if e.get('c'): r['comment_id'] = e['c']
        assert len(e['cx'].split()) <= 25, (rid, e['cx'])
        recs.append(r)
        if e.get('r'): restricted.append(rid)
with open(os.path.join(BASE, 'voice/reddit-r63.jsonl'), 'w', encoding='utf-8') as o:
    for r in recs: o.write(json.dumps(r, ensure_ascii=False) + '\n')
open(os.path.join(BASE, 'scratchpad/R63/restricted.txt'), 'w').write('\n'.join(restricted) + '\n')
print(len(recs), 'records;', len(restricted), 'restricted')
