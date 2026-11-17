#!/usr/bin/env python3
"""Append records from a tab-separated batch file to voice/reddit-mr07.jsonl.
Batch line: unit<TAB>comment_id|-<TAB>speaker<TAB>stage<TAB>type<TAB>themes,comma<TAB>R|-<TAB>quote<TAB>context
unit = short name like daddit-1s9r7ep. Lines starting # ignored."""
import json, sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.join(HERE, "..", "..")
VOICE = os.path.join(NICHE, "voice", "reddit-mr07.jsonl")
RESTR = os.path.join(HERE, "restricted.txt")
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = []
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.rstrip("\n")
    if not line.strip() or line.startswith("#"):
        continue
    f = line.split("\t")
    assert len(f) == 9, (len(f), line[:80])
    unit, cid, sp, st, ty, th, r, q, ctx = f
    rel = f"../_shared/_raw/reddit-2026/units/{unit}.txt"
    txt = open(os.path.join(NICHE, rel), encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    rec = {}
    if cid != "-":
        cm = re.search(r"COMMENT " + re.escape(cid) + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
        assert cm, cid
        date, url = cm.groups()
    assert len(ctx.split()) <= 25, ctx
    n += 1
    rid = f"sm07-{n:04d}"
    rec = {"id": rid, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": sp, "stage": st,
           "type": ty, "themes": [t.strip() for t in th.split(",") if t.strip()], "quote": q, "context": ctx,
           "raw_file": rel, "source_class": "reddit_archive", "post_id": pid}
    if cid != "-":
        rec["comment_id"] = cid
    out.append(rec)
    if r == "R":
        open(RESTR, "a").write(rid + "\n")
with open(VOICE, "a", encoding="utf-8") as fo:
    for rec in out:
        fo.write(json.dumps(rec, ensure_ascii=False) + "\n")
print(f"added {len(out)}, last {out[-1]['id'] if out else '-'}")
