#!/usr/bin/env python3
"""Build voice/reddit-pr09.jsonl from scratchpad/PR09/q*.py batch files (each defines Q = [...])."""
import json, os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(HERE, "..", ".."))
units = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "units.tsv"))]
recs, restricted = [], []
xs = {}
exec(open(os.path.join(HERE, "extra_restrict.py"), encoding="utf-8").read(), xs)
X = xs["X"]; used = set()
n = 0
for f in sorted(glob.glob(os.path.join(HERE, "q[0-9][0-9].py"))):
    ns = {}
    exec(open(f, encoding="utf-8").read(), ns)
    for e in ns["Q"]:
        u, c, sp, st, ty, th, q, cx, r = e
        path = units[u - 1][1]
        text = open(os.path.join(NICHE, path), encoding="utf-8").read()
        m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", text)
        pid, sub, date, url = m.groups()
        rec = {}
        if c:
            cm = re.search(r"COMMENT " + c + r" \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", text)
            date, url = cm.groups()
        n += 1
        rid = f"pb09-{n:04d}"
        rec = {"id": rid, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": sp, "stage": st,
               "type": ty, "themes": th, "quote": q, "context": cx, "raw_file": path,
               "source_class": "reddit_archive", "post_id": pid}
        if c:
            rec["comment_id"] = c
        assert len(cx.split()) <= 25, (rid, cx)
        recs.append(rec)
        for k, v in X.items():
            if q.startswith(k):
                r = r or v; used.add(k)
        if r:
            restricted.append((rid, r))
with open(os.path.join(NICHE, "voice", "reddit-pr09.jsonl"), "w", encoding="utf-8") as o:
    for r in recs:
        o.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(os.path.join(HERE, "restricted.txt"), "w") as o:
    for rid, r in restricted:
        o.write(f"- {rid} — {r}\n")
# per-unit id map
um = {}
for r in recs:
    um.setdefault(r["raw_file"], []).append(r["id"])
json.dump(um, open(os.path.join(HERE, "unitmap.json"), "w"), indent=0)
assert used == set(X), set(X) - used
print(len(recs), "records,", len(restricted), "restricted")
