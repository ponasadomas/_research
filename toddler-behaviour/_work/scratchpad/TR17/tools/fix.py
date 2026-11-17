#!/usr/bin/env python3
"""Replace quote (and optionally context) of existing tb17 records. Input JSON: {id: [spec, context_or_null]}"""
import json, sys, os, re, html
T = "/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour"
V = T + "/voice/reddit-tr17.jsonl"
MAP = str.maketrans({"’": "'", "‘": "'", "“": '"', "”": '"'})
def norm(s):
    s = html.unescape(s).replace("\\n", " ")
    return re.sub(r"\s+", " ", s).strip()
fixes = json.load(open(sys.argv[1]))
rs = [json.loads(l) for l in open(V)]
for r in rs:
    if r["id"] not in fixes: continue
    spec, ctx = fixes[r["id"]]
    if spec is not None:
        N = norm(open(os.path.join(T, r["raw_file"]), encoding="utf-8").read()); M = N.translate(MAP)
        pos = M.find("COMMENT " + r["comment_id"]) if r.get("comment_id") else 0
        out = []
        for p in (spec if isinstance(spec, list) else [spec]):
            if " ~~ " in p:
                a, b = [norm(x).translate(MAP) for x in p.split(" ~~ ")]
                i = M.find(a, pos); assert i >= 0, (r["id"], a); j = M.find(b, i + len(a)); assert j >= 0, (r["id"], b); j += len(b)
            else:
                a = norm(p).translate(MAP); i = M.find(a, pos); assert i >= 0, (r["id"], a); j = i + len(a)
            out.append(N[i:j]); pos = j
        r["quote"] = " […] ".join(out)
    if ctx is not None:
        assert len(ctx.split()) <= 25; r["context"] = ctx
    print(r["id"], len(r["quote"]))
with open(V, "w") as f:
    for r in rs: f.write(json.dumps(r, ensure_ascii=False) + "\n")
