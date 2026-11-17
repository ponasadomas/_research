#!/usr/bin/env python3
# Build voice/reddit-r43.jsonl from scratchpad/R43/q*.tsv (unit, cid, speaker, stage, type, themes, quote, context[, R])
import json, re, glob, os, sys
B = os.path.dirname(os.path.abspath(__file__)); NICHE = os.path.join(B, "..", "..")
U = "../_shared/_raw/reddit-2026/units/"
out = []; restricted = []; n = 0
for f in sorted(glob.glob(os.path.join(B, "q*.tsv"))):
    for ln, line in enumerate(open(f, encoding="utf-8"), 1):
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"): continue
        p = [x.strip() for x in line.split(" || ")]
        if len(p) < 8: sys.exit(f"{f}:{ln} has {len(p)} fields")
        unit, cid, spk, stg, typ, th, q, ctx = p[:8]
        flag = len(p) > 8 and p[8].strip() == "R"
        rf = U + unit + ".txt"
        txt = open(os.path.join(NICHE, rf), encoding="utf-8").read()
        m = re.match(r"POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)", txt)
        pid, sub, date, url = m.groups()
        if cid and cid != "-":
            mc = re.search(r"COMMENT " + cid + r" \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)", txt)
            if not mc: sys.exit(f"{f}:{ln} comment {cid} not in {unit}")
            date, url = mc.groups()
        n += 1; i = f"sb43-{n:04d}"
        if len(ctx.split()) > 25: print("long context", i, file=sys.stderr)
        r = {"id": i, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": spk, "stage": stg,
             "type": typ, "themes": [t.strip() for t in th.split(",") if t.strip()], "quote": q, "context": ctx,
             "raw_file": rf, "source_class": "reddit_archive", "post_id": pid}
        if cid and cid != "-": r["comment_id"] = cid
        out.append(r)
        if flag: restricted.append(i)
with open(os.path.join(NICHE, "voice", "reddit-r43.jsonl"), "w", encoding="utf-8") as o:
    for r in out: o.write(json.dumps(r, ensure_ascii=False) + "\n")
open(os.path.join(B, "restricted.txt"), "w").write("\n".join(restricted) + "\n")
print(n, "records;", len(restricted), "restricted")
