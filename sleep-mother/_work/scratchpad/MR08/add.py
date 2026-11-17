#!/usr/bin/env python3
# usage: add.py input.jsonl  -- short-key records -> appends to voice/reddit-mr08.jsonl
import json, sys, os, re, html
NICHE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
VOICE = os.path.join(NICHE, "voice", "reddit-mr08.jsonl")
RESTR = os.path.join(os.path.dirname(__file__), "restricted.txt")
UNITS = "../_shared/_raw/reddit-2026/units/"
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
out = []; restr = []; bad = 0
for i, line in enumerate(open(sys.argv[1]), 1):
    if not line.strip(): continue
    r = json.loads(line)
    rf = UNITS + r["u"] + ".txt"
    txt = open(os.path.join(NICHE, rf), encoding="utf-8").read()
    head = txt.split("\n", 1)[0]
    m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*\| (\S+)$", head)
    pid, sub, date, url = m.groups()
    c = r.get("c", "")
    if c:
        cm = re.search(r"COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)" % re.escape(c), txt)
        if not cm: print("no comment", c, r["u"]); bad += 1; continue
        date, url = cm.groups()
    nt = norm(txt); pos = 0; ok = True
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", r["q"]):
        piece = norm(piece)
        if not piece: continue
        at = nt.find(piece, pos)
        if at < 0: ok = False; print("LINE", i, "NOT FOUND:", piece[:80]); break
        pos = at + len(piece)
    if not ok: bad += 1; continue
    if len(r["cx"].split()) > 25: print("LINE", i, "context too long"); bad += 1; continue
    n += 1
    rid = "sm08-%04d" % n
    rec = {"id": rid, "source": "reddit r/" + sub, "url": url, "date": date, "speaker": r["sp"], "stage": r["st"],
           "type": r["ty"], "themes": r["th"], "quote": r["q"], "context": r["cx"], "raw_file": rf,
           "source_class": "reddit_archive", "post_id": pid}
    if c: rec["comment_id"] = c
    out.append(rec)
    if r.get("r"): restr.append(rid + "\t" + r.get("rr", ""))
if bad:
    print("ABORT:", bad, "bad records; nothing written"); sys.exit(1)
with open(VOICE, "a") as f:
    for rec in out: f.write(json.dumps(rec, ensure_ascii=False) + "\n")
with open(RESTR, "a") as f:
    for x in restr: f.write(x + "\n")
print("wrote", len(out), "last id", out[-1]["id"] if out else None, "restricted", len(restr))
