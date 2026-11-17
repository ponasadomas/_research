#!/usr/bin/env python3
"""Cards for one reading wave: tier-A posts of a niche from a date onward.
    python3 -I wave_cards.py <niche> <from YYYY-MM-DD> <wave label>
Writes <niche>/_raw/reddit/filter-v1/<wave>/cards/*.txt + cards-index.jsonl + unread-rest.jsonl (tier-A ids outside the wave)."""
import json, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(HERE, "..", ".."))
niche, frm, wave = sys.argv[1:4]
base = os.path.join(R, niche, "_raw", "reddit", "filter-v1"); out = os.path.join(base, wave)
if os.path.exists(out): raise SystemExit("frozen: " + out)
os.makedirs(os.path.join(out, "cards"))
bodies = {}
need = {}
for l in open(os.path.join(base, "A-candidates.jsonl")):
    r = json.loads(l); need[r["id"]] = r
for f in os.listdir(os.path.join(R, "_shared", "_raw", "reddit-2026")):
    if f.endswith(".posts.jsonl"):
        for l in open(os.path.join(R, "_shared", "_raw", "reddit-2026", f)):
            q = json.loads(l)
            if q["id"] in need: bodies[q["id"]] = q.get("selftext") or ""
by = collections.defaultdict(list); rest = []
for r in sorted(need.values(), key=lambda r: (r["subreddit"], r["created_utc"])):
    if r["date"] >= frm:
        by[r["subreddit"]].append(f"ID {r['id']} | r/{r['subreddit']} | {r['date'][:10]} | safety_flag={r['safety_flag']}\nTITLE: {r['title']}\nOPENING: {bodies.get(r['id'],'')[:350]}\nMATCHES: {json.dumps(r['matches'], ensure_ascii=False)}\n\n")
    else: rest.append(r["id"])
idx = []
for sub in sorted(by):
    buf, n, i = "", 0, 1
    for cd in by[sub] + [None]:
        if cd is None or (buf and len((buf + cd).encode()) > 40000):
            if buf:
                name = f"A-{sub}-{i:03d}.txt"; open(os.path.join(out, "cards", name), "w").write(buf)
                idx.append({"file": f"_raw/reddit/filter-v1/{wave}/cards/{name}", "cards": n}); i += 1
            buf, n = "", 0
            if cd is None: break
        buf += cd; n += 1
open(os.path.join(out, "cards-index.jsonl"), "w").write("".join(json.dumps(x) + "\n" for x in idx))
open(os.path.join(out, "unread-rest.jsonl"), "w").write("".join(json.dumps({"id": i}) + "\n" for i in rest))
print(niche, "cards", sum(x["cards"] for x in idx), "chunks", len(idx), "tier-A outside wave", len(rest))
