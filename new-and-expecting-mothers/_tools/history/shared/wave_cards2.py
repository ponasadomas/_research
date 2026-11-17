#!/usr/bin/env python3
"""Cards for a reading wave over a date range, skipping posts already triaged in any earlier wave.
    python3 -I wave_cards2.py <niche folder> <filter label> <from YYYY-MM-DD> <to-exclusive YYYY-MM-DD> <wave label>
Writes <niche>/_raw/reddit/<filter label>/<wave>/cards/*.txt + cards-index.jsonl. Frozen."""
import collections, csv, glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(HERE, "..", ".."))
niche, flab, frm, to, wave = sys.argv[1:6]
base = os.path.join(R, niche, "_raw", "reddit", flab); out = os.path.join(base, wave)
if os.path.exists(out): raise SystemExit("frozen: " + out)
seen = set()
for f in glob.glob(os.path.join(R, niche, "_raw", "reddit", "triage", "*.tsv")):
    for r in csv.DictReader(open(f), delimiter="\t"): seen.add(r["post_id"].strip())
need = {}
for l in open(os.path.join(base, "A-candidates.jsonl")):
    r = json.loads(l)
    if frm <= r["date"][:10] < to and r["id"] not in seen: need[r["id"]] = r
bodies = {}
for f in os.listdir(os.path.join(R, "_shared", "_raw", "reddit-2026")):
    if f.endswith(".posts.jsonl"):
        for l in open(os.path.join(R, "_shared", "_raw", "reddit-2026", f)):
            q = json.loads(l)
            if q["id"] in need: bodies[q["id"]] = q.get("selftext") or ""
os.makedirs(os.path.join(out, "cards"))
by = collections.defaultdict(list)
for r in sorted(need.values(), key=lambda r: (r["subreddit"], r["created_utc"])):
    by[r["subreddit"]].append(f"ID {r['id']} | r/{r['subreddit']} | {r['date'][:10]} | safety_flag={r['safety_flag']}\nTITLE: {r['title']}\nOPENING: {bodies.get(r['id'],'')[:350]}\nMATCHES: {json.dumps(r['matches'], ensure_ascii=False)}\n\n")
idx = []
for sub in sorted(by):
    buf, n, i = "", 0, 1
    for cd in by[sub] + [None]:
        if cd is None or (buf and len((buf + cd).encode()) > 40000):
            if buf:
                name = f"A-{sub}-{i:03d}.txt"; open(os.path.join(out, "cards", name), "w").write(buf)
                idx.append({"file": f"_raw/reddit/{flab}/{wave}/cards/{name}", "cards": n}); i += 1
            buf, n = "", 0
            if cd is None: break
        buf += cd; n += 1
open(os.path.join(out, "cards-index.jsonl"), "w").write("".join(json.dumps(x) + "\n" for x in idx))
print(niche, wave, "cards", sum(x["cards"] for x in idx), "chunks", len(idx), "skipped as already triaged", len(seen))
