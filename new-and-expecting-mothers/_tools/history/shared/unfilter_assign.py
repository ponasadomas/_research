#!/usr/bin/env python3
"""Split a build's re-reading queue into reader assignments and briefs.
python3 -I unfilter_assign.py <niche> <id-prefix> [posts-per-reader=300]"""
import csv, math, os, sys
niche, prefix = sys.argv[1], sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 300
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", niche))
D = os.path.join(R, "scratchpad", "unfilter-reread")
rows = list(csv.reader(open(os.path.join(D, "queue.tsv")), delimiter="\t"))[1:]
rows = [r for r in rows if len(r) >= 2 and r[1].strip()]
n = max(1, math.ceil(len(rows) / per))
title = open(os.path.join(R, "README.md")).readline().lstrip("# ").strip()
tpl = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "brief-unfilter-reader.md")).read()
for k in range(n):
    nn = f"{k+1:02d}"
    part = rows[k::n]
    with open(os.path.join(D, f"assign-ur{nn}.tsv"), "w") as f:
        f.write("kind\tid\twhy_it_was_dropped\n")
        for r in part: f.write("\t".join((r + [""])[:3]) + "\n")
    b = (tpl.replace("{NICHE}", niche).replace("{TITLE}", title).replace("{NN}", nn)
            .replace("{PREFIX}", f"{prefix}{nn}").replace("{READERS}", str(n)))
    open(os.path.join(D, f"brief-ur{nn}.md"), "w").write(b)
print(f"{niche}: {len(rows)} posts, {n} readers")
