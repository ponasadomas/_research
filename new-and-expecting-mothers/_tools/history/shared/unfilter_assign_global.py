#!/usr/bin/env python3
"""Split the global set's re-reading queue (unit_id, raw_file, stage, reason) into reader
assignments balanced by size, and write briefs.
python3 -I unfilter_assign_global.py global <id-prefix> [units-per-reader=300]"""
import csv, math, os, sys
niche, prefix = sys.argv[1], sys.argv[2]
per = int(sys.argv[3]) if len(sys.argv) > 3 else 300
T = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(T, "..", "..", niche))
D = os.path.join(R, "scratchpad", "unfilter-reread")
rows = [r for r in list(csv.reader(open(os.path.join(D, "queue.tsv")), delimiter="\t"))[1:] if len(r) >= 4 and r[0].strip()]
n = max(1, math.ceil(len(rows) / per))
seen = {}
def size(r):                       # a bundle file shared by many units counts once per unit, split evenly
    p = os.path.join(R, r[1]); s = os.path.getsize(p) if os.path.isfile(p) else 0
    return s / seen[r[1]]
for r in rows: seen[r[1]] = seen.get(r[1], 0) + 1
rows.sort(key=lambda r: (-size(r), r[0]))
tpl = open(os.path.join(T, "brief-unfilter-reader-global.md")).read()
for k in range(n):
    nn = f"{k+1:02d}"; part = sorted(rows[k::n], key=lambda r: (r[1], r[0]))
    with open(os.path.join(D, f"assign-ur{nn}.tsv"), "w") as f:
        f.write("stage\tunit_id\traw_file\twhy_it_was_dropped\n")
        for r in part: f.write("\t".join([r[2], r[0], r[1], r[3]]) + "\n")
    kb = round(sum(size(r) for r in part) / 1000)
    b = tpl.replace("{NN}", nn).replace("{PREFIX}", f"{prefix}{nn}").replace("{READERS}", str(n)).replace("{COUNT}", str(len(part)))
    open(os.path.join(D, f"brief-ur{nn}.md"), "w").write(b)
    print(f"ur{nn}: {len(part)} units, about {kb} KB")
print(f"{niche}: {len(rows)} posts, {n} readers")
