#!/usr/bin/env python3
"""Build voice/reddit-pr13.jsonl from scratchpad/PR13/q*.py batch files (each defines S and Q)."""
import json, os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__))
NICHE = os.path.abspath(os.path.join(HERE, "..", ".."))
units = [l.rstrip("\n").split("\t") for l in open(os.path.join(HERE, "units.tsv"))]
recs, restricted, status = [], [], {}
n = 0
for f in sorted(glob.glob(os.path.join(HERE, "q[0-9][0-9].py"))):
    ns = {}
    exec(open(f, encoding="utf-8").read(), ns)
    status.update(ns["S"])
    for e in ns["Q"]:
        u, c, sp, st, ty, th, q, cx, r = e
        path = units[u - 1][1]
        text = open(os.path.join(NICHE, path), encoding="utf-8").read()
        m = re.match(r"POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", text)
        pid, sub, date, url = m.groups()
        if c:
            cm = re.search(r"COMMENT " + c + r" \| (\d{4}-\d\d-\d\d)[^|]*\| (\S+)", text)
            date, url = cm.groups()
        n += 1
        rid = f"pb13-{n:04d}"
        rec = {"id": rid, "source": f"reddit r/{sub}", "url": url, "date": date, "speaker": sp, "stage": st,
               "type": ty, "themes": th, "quote": q, "context": cx, "raw_file": path,
               "source_class": "reddit_archive", "post_id": pid}
        if c:
            rec["comment_id"] = c
        assert len(cx.split()) <= 25, (rid, cx)
        recs.append(rec)
        if r:
            restricted.append((rid, r))
assert sorted(status) == list(range(1, len(units) + 1)), set(range(1, len(units) + 1)) - set(status)
with open(os.path.join(NICHE, "voice", "reddit-pr13.jsonl"), "w", encoding="utf-8") as o:
    for r in recs:
        o.write(json.dumps(r, ensure_ascii=False) + "\n")
with open(os.path.join(HERE, "restricted.txt"), "w") as o:
    for rid, r in restricted:
        o.write(f"- {rid} — {r}\n")
um = {}
for r in recs:
    um.setdefault(r["raw_file"], []).append(r["id"])
with open(os.path.join(HERE, "ledger_rows.md"), "w") as o:
    for i, p, ch in units:
        ids = um.get(p, [])
        rng = (f"{ids[0]}–{ids[-1].split('-')[1]}" if len(ids) > 1 else ids[0]) if ids else "—"
        o.write(f"| {ch.replace('read-v1-','')} | `{p}` | {status[int(i)]} | {rng} ({len(ids)}) |\n")
print(len(recs), "records,", len(restricted), "restricted,", len(um), "units quoted")
