#!/usr/bin/env python3
"""Append quote records. Input: a file with blocks separated by lines '---'.
Block header line: unit|comment_id_or_-|speaker|stage|type|themes,comma|context
following lines: quote (joined with spaces)."""
import json, sys, re, os, html
NICHE = "/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth"
VOICE = NICHE + "/voice/reddit-pr11.jsonl"
UNITS = "../_shared/_raw/reddit-2026/units/"
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
n = 0
if os.path.exists(VOICE):
    n = sum(1 for l in open(VOICE) if l.strip())
blocks = open(sys.argv[1], encoding="utf-8").read().split("\n---\n")
out = []
for b in blocks:
    b = b.strip()
    if not b: continue
    head, *ql = b.split("\n")
    unit, cid, spk, stg, typ, th, ctx = head.split("|")
    quote = " ".join(x.strip() for x in ql if x.strip())
    rf = UNITS + unit + ".txt"
    txt = open(os.path.join(NICHE, rf), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    if cid != "-":
        mm = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
        date, url = mm.groups()
    t = norm(txt); pos = 0
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", quote):
        piece = norm(piece)
        if not piece: continue
        at = t.find(piece, pos)
        if at < 0: sys.exit(f"NOT FOUND in {unit}: {piece[:80]!r}")
        pos = at + len(piece)
    if len(ctx.split()) > 25: sys.exit(f"context too long: {ctx}")
    n += 1
    r = {"id": f"pb11-{n:04d}", "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": spk, "stage": stg, "type": typ,
         "themes": [x.strip() for x in th.split(",") if x.strip()], "quote": quote, "context": ctx, "raw_file": rf,
         "source_class": "reddit_archive", "post_id": pid}
    if cid != "-": r["comment_id"] = cid
    out.append(r)
with open(VOICE, "a", encoding="utf-8") as f:
    for r in out: f.write(json.dumps(r, ensure_ascii=False) + "\n")
for r in out: print(r["id"], r["post_id"], r["type"], r["quote"][:50])
