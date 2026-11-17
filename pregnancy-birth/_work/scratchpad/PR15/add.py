# usage: python3 -I add.py batchfile.jsonl   (each line: [unit, cid, speaker, stage, type, themes, quote, context, restricted_reason_or_empty])
import json, sys, os, re
PB = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
VOICE = PB + "/voice/reddit-pr15.jsonl"
RESTR = PB + "/scratchpad/PR15/restricted.tsv"
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = open(VOICE, "a"); rout = open(RESTR, "a")
for line in open(sys.argv[1]):
    if not line.strip(): continue
    unit, cid, sp, st, ty, th, q, ctx, r = json.loads(line)
    rf = "../_shared/_raw/reddit-2026/units/%s.txt" % unit
    txt = open(os.path.join(PB, rf)).read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    if cid:
        mm = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) .*?\| (\S+)" % cid, txt)
        date, url = mm.groups()
    n += 1
    rec = {"id": "pb15-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": sp, "stage": st, "type": ty,
           "themes": th if isinstance(th, list) else [t.strip() for t in th.split(",")], "quote": q, "context": ctx, "raw_file": rf,
           "source_class": "reddit_archive", "post_id": pid}
    if cid: rec["comment_id"] = cid
    assert len(ctx.split()) <= 25, ctx
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if r: rout.write("%s\t%s\n" % (rec["id"], r))
print("total", n)
