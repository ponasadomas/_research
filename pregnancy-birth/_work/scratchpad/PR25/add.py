#!/usr/bin/env python3
# usage: add.py entries.json  -> appends to voice/reddit-pr25.jsonl
# entries: list of [unitfile, comment_id or "", speaker, stage, type, themes(list), quote, context]
import json, sys, re, os
B = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/"
V = B + "voice/reddit-pr25.jsonl"
n = 0
if os.path.exists(V):
    n = sum(1 for l in open(V) if l.strip())
out = open(V, "a")
for u, cid, sp, st, ty, th, q, ctx in json.load(open(sys.argv[1])):
    rf = "../_shared/_raw/reddit-2026/units/" + u + ".txt"
    t = open(B + rf, encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
    pid, sub, date, url = m.groups()
    rec = {}
    if cid:
        cm = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
        date, url = cm.groups()
    n += 1
    rec = {"id": "pb25-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": sp, "stage": st, "type": ty, "themes": th, "quote": q, "context": ctx, "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
    if cid: rec["comment_id"] = cid
    if len(ctx.split()) > 25: print("LONG CTX", rec["id"])
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    print(rec["id"], u, cid)
