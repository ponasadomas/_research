# Rebuild voice/reddit-pr55.jsonl from scratchpad/PR55/recs/rec-*.py. Run from pregnancy-birth folder with python3 -I.
import json, glob, re, os
units = [l.rstrip('\n').split('\t')[1] for l in open('scratchpad/PR55/units.txt')]
recs = []
for f in sorted(glob.glob('scratchpad/PR55/recs/rec-*.py')):
    ns = {}
    exec(open(f).read(), ns)
    recs += ns['R']
out = open('voice/reddit-pr55.jsonl', 'w')
restricted = []
for i, r in enumerate(recs, 1):
    u, c, sp, st, ty, th, q, cx = r[:8]
    flag = len(r) > 8 and r[8]
    path = units[u - 1]
    txt = open(path).read()
    head = txt.split('\n', 1)[0]
    m = re.match(r'POST (\w+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*\| (\S+)', head)
    pid, sub, date, url = m.groups()
    rec = {"id": "pb55-%04d" % i, "source": "reddit r/" + sub}
    if c:
        cm = re.search(r'COMMENT ' + c + r' \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)', txt)
        rec["url"] = cm.group(2); rec["date"] = cm.group(1)
    else:
        rec["url"] = url; rec["date"] = date
    rec.update({"speaker": sp, "stage": st, "type": ty, "themes": th, "quote": q, "context": cx,
                "raw_file": path, "source_class": "reddit_archive", "post_id": pid})
    if c: rec["comment_id"] = c
    assert len(cx.split()) <= 25, rec["id"]
    out.write(json.dumps(rec, ensure_ascii=False) + '\n')
    if flag: restricted.append(rec["id"])
out.close()
open('scratchpad/PR55/restricted.txt', 'w').write(', '.join(restricted) + '\n')
print(len(recs), 'records;', len(restricted), 'restricted')
