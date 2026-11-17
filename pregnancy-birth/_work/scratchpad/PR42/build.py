# usage: python3 -I build.py  -> reads entries-*.tsv in this folder, writes voice file
# entry TSV columns: unit  comment  speaker  stage  type  themes(comma)  restricted(0/1)  quote  context
import json, re, glob, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(HERE, '..', '..'))
UNITS = '../_shared/_raw/reddit-2026/units/'
out, restricted, n, withdrawn = [], [], 0, []
def meta(unit):
    txt = open(os.path.join(NICHE, UNITS + unit + '.txt'), encoding='utf-8').read()
    m = {}
    for mm in re.finditer(r'^(POST|COMMENT) (\w+) \| (?:r/\w+ \| )?(\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt, re.M):
        m[mm.group(2)] = (mm.group(3), mm.group(4))
    return m
for f in sorted(glob.glob(os.path.join(HERE, 'entries-*.tsv'))):
    for line in open(f, encoding='utf-8'):
        if line.startswith('##'):
            n += 1; withdrawn.append('pb42-%04d' % n); continue
        if not line.strip() or line.startswith('#'): continue
        p = [x.strip() for x in line.rstrip('\n').split(' || ')]
        assert len(p) == 9, (f, line)
        unit, com, sp, st, ty, th, r, q, cx = p
        sub, pid = unit.rsplit('-', 1)
        m = meta(unit)
        key = com or pid
        date, url = m[key]
        n += 1
        rec = {"id": "pb42-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date,
               "speaker": sp, "stage": st, "type": ty, "themes": th.split(','), "quote": q,
               "context": cx, "raw_file": UNITS + unit + '.txt', "source_class": "reddit_archive", "post_id": pid}
        if com: rec["comment_id"] = com
        assert len(cx.split()) <= 25, ('context too long', rec['id'], cx)
        out.append(rec)
        if r == '1': restricted.append(rec['id'])
with open(os.path.join(NICHE, 'voice', 'reddit-pr42.jsonl'), 'w', encoding='utf-8') as fh:
    for r in out: fh.write(json.dumps(r, ensure_ascii=False) + '\n')
open(os.path.join(HERE, 'restricted.txt'), 'w').write('\n'.join(restricted) + '\n')
from collections import Counter
print(len(out), 'records;', len(restricted), 'restricted; withdrawn', withdrawn)
print(Counter(r['raw_file'].split('/')[-1][:-4] for r in out).most_common(3))
