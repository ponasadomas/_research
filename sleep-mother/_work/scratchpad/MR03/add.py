#!/usr/bin/env python3
"""Append records to voice file. Input: a python file defining RECS = [(unit, comment_id or None, speaker, stage, type, themes, quote, context), ...]"""
import json, re, sys, os
NICHE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(NICHE, "voice", "reddit-mr03.jsonl")
def meta(unit, cid):
    raw = f"../_shared/_raw/reddit-2026/units/{unit}.txt"
    txt = open(os.path.join(NICHE, raw), encoding="utf-8").read()
    if cid:
        m = re.search(r"^COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)" % cid, txt, re.M)
    else:
        m = re.search(r"^POST \S+ \| (r/\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt, re.M)
    if not m: sys.exit(f"no meta {unit} {cid}")
    sub = re.search(r"^POST \S+ \| r/(\S+)", txt, re.M).group(1)
    date, url = (m.group(1), m.group(2)) if cid else (m.group(2), m.group(3))
    return raw, sub, date, url, unit.split("-",1)[1]
ns = {}; exec(open(sys.argv[1]).read(), ns)
n = sum(1 for l in open(OUT)) if os.path.exists(OUT) else 0
with open(OUT, "a") as f:
    for unit, cid, sp, st, ty, th, q, ctx in ns["RECS"]:
        raw, sub, date, url, pid = meta(unit, cid)
        n += 1
        if len(ctx.split()) > 25: sys.exit(f"context too long: {ctx}")
        r = dict(id=f"sm03-{n:04d}", source=f"reddit r/{sub}", url=url, date=date, speaker=sp, stage=st, type=ty, themes=th, quote=q, context=ctx, raw_file=raw, source_class="reddit_archive", post_id=pid)
        if cid: r["comment_id"] = cid
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("now", n)
