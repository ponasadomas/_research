# usage: python3 -I add.py batchfile.txt  -- batch lines: unit|comment_id_or_-|date|speaker|stage|type|themes,comma|context|quote
import json, sys, os, re
base = "/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby"
out = base + "/voice/reddit-r12.jsonl"
n = 0
if os.path.exists(out):
    n = sum(1 for l in open(out) if l.strip())
with open(out, "a") as f:
    for line in open(sys.argv[1], encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        unit, cid, date, sp, st, ty, th, ctx, q = line.split("|", 8)
        sub, pid = unit.split("-", 1)
        n += 1
        rec = {"id": "sb12-%04d" % n, "source": "reddit r/" + sub,
               "url": "https://www.reddit.com/r/%s/comments/%s/" % (sub, pid) + ("comment/%s/" % cid if cid != "-" else ""),
               "date": date, "speaker": sp, "stage": st, "type": ty,
               "themes": [t.strip() for t in th.split(",") if t.strip()],
               "quote": q.strip(), "context": ctx.strip(),
               "raw_file": "../_shared/_raw/reddit-2026/units/%s.txt" % unit,
               "source_class": "reddit_archive", "post_id": pid}
        if cid != "-":
            rec["comment_id"] = cid
        assert len(rec["context"].split()) <= 25, rec["context"]
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
print("total", n)
