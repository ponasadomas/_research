#!/usr/bin/env python3
"""Append records to voice/reddit-tr17.jsonl. Input: JSON list of
[unit_basename, comment_id_or_empty, speaker, stage, type, themes_list, quote_spec, context].
quote_spec: string or list of pieces joined by ' […] '. A piece 'A ~~ B' means the raw span
from A through B. Matching ignores curly vs straight quotes; text is extracted from the raw."""
import json, sys, os, re, html
T = "/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour"
V = T + "/voice/reddit-tr17.jsonl"
MAP = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
recs = json.load(open(sys.argv[1]))
n = sum(1 for l in open(V) if l.strip()) if os.path.exists(V) else 0
lines = []
for base, cid, sp, st, ty, th, q, ctx in recs:
    rf = "../_shared/_raw/reddit-2026/units/" + base + ".txt"
    txt = open(os.path.join(T, rf), encoding="utf-8").read()
    m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
    pid, sub, date, url = m.groups()
    if cid:
        mc = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)", txt)
        date, url = mc.groups()
    N = norm(txt); M = N.translate(MAP)
    pos = 0
    if cid:
        pos = M.find("COMMENT " + cid)
    pieces = q if isinstance(q, list) else [q]
    outp = []
    for p in pieces:
        if " ~~ " in p:
            a, b = [norm(x).translate(MAP) for x in p.split(" ~~ ")]
            i = M.find(a, pos); assert i >= 0, ("start not found", base, a)
            j = M.find(b, i + len(a)); assert j >= 0, ("end not found", base, b)
            j += len(b)
        else:
            a = norm(p).translate(MAP)
            i = M.find(a, pos); assert i >= 0, ("not found", base, a)
            j = i + len(a)
        outp.append(N[i:j]); pos = j
    quote = " […] ".join(outp)
    assert len(ctx.split()) <= 25, ctx
    n += 1
    r = {"id": "tb17-%04d" % n, "source": "reddit r/" + sub, "url": url, "date": date,
         "speaker": sp, "stage": st, "type": ty, "themes": th, "quote": quote, "context": ctx,
         "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
    if cid: r["comment_id"] = cid
    lines.append(json.dumps(r, ensure_ascii=False))
    print(r["id"], base, cid or "-", len(quote))
with open(V, "a") as out:
    for l in lines: out.write(l + "\n")
