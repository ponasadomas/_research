#!/usr/bin/env python3
"""Append quotes to voice/reddit-tr16.jsonl from a compact batch file.
Batch lines (JSON): {"u": "<unit basename w/o .txt>", "c": "<comment id or ''>", "sp":..., "st":..., "ty":..., "th":[...], "q":..., "cx":..., "r": optional reason if restricted}
"""
import json, sys, re, os
TB = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
VOICE = os.path.join(TB, "voice", "reddit-tr16.jsonl")
RESTR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "restricted.tsv")
UP = "../_shared/_raw/reddit-2026/units/"
def meta(u):
    t = open(os.path.join(TB, UP + u + ".txt"), encoding="utf-8").read()
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)
    pid, sub, d, url = m.groups()
    cm = {c: (cd, cu) for c, cd, cu in re.findall(r"COMMENT (\S+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", t)}
    return pid, sub, d, url, cm
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = open(VOICE, "a"); rf = open(RESTR, "a")
for line in open(sys.argv[1], encoding="utf-8"):
    if not line.strip(): continue
    b = json.loads(line)
    pid, sub, d, url, cm = meta(b["u"])
    n += 1; i = "tb16-%04d" % n
    rec = {"id": i, "source": "reddit r/" + sub, "url": url, "date": d, "speaker": b["sp"], "stage": b["st"], "type": b["ty"], "themes": b["th"], "quote": b["q"], "context": b["cx"], "raw_file": UP + b["u"] + ".txt", "source_class": "reddit_archive", "post_id": pid}
    if b.get("c"):
        cd, cu = cm[b["c"]]; rec["url"] = cu; rec["date"] = cd; rec["comment_id"] = b["c"]
    out.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if b.get("r"): rf.write(i + "\t" + b["u"] + "\t" + b["r"] + "\n")
    print(i, b["u"])
