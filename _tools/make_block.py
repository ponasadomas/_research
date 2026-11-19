#!/usr/bin/env python3
"""Build the post files and reader shares for one block of a sample, from cached replies.
  python3 -I _tools/make_block.py <dir> <block number, from 0> <posts per share> <shares per block> <seed> [without-replies-ok]
  (run from ~/GitHub/_research, after fetch_replies.py has reached this block)
A block is the next <posts per share> x <shares per block> rows of <dir>/sample.tsv, taken in
shuffled order (see order.txt below), so a run that stops early has read a fair sample. Its posts
are dealt at random (seeded) to its readers, numbered on from the blocks before it.
With without-replies-ok, a post whose replies are not fetched yet gets a post file without
them (listed in <dir>/posts-without-replies.txt) instead of holding the block up.
Exit 0: shares written (or already there). Exit 2: replies not all fetched yet. Exit 3: no such block."""
import datetime, json, math, os, random, sys
out, b, per, k, seed = sys.argv[1].rstrip("/"), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
RAW = "new-and-expecting-mothers/reddit/raw/reddit-2026"
rows = [l.split("\t") for l in open(f"{out}/sample.tsv").read().split("\n")[1:] if l.strip()]
# sample.tsv is in date order. Blocks are cut from a shuffled order, so that a run which
# stops early has still read a fair sample. <dir>/order.txt holds how many leading rows
# keep the sample's order (0 for a new reading; more only where shares were already dealt
# by date before this was fixed, 2026-11-20).
of = f"{out}/order.txt"
if not os.path.exists(of): open(of, "w").write("0\n")
keep = int(open(of).read().split()[0]); rest = rows[keep:]; random.Random(seed).shuffle(rest); rows = rows[:keep] + rest
block = rows[b * per * k:(b + 1) * per * k]
if not block: sys.exit(3)
n = math.ceil(len(block) / per); names = [f"{out}/reader-{b * k + i + 1:03d}.tsv" for i in range(n)]
if all(os.path.exists(f) for f in names): print(" ".join(f"{b * k + i + 1:03d}" for i in range(n))); sys.exit(0)
ALLOW = len(sys.argv) > 6 and sys.argv[6] == "without-replies-ok"
if not ALLOW and any(not os.path.exists(f"{RAW}/comments/{r[0]}.json") for r in block): sys.exit(2)
d = lambda ts: datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
want = {r[0] for r in block}; posts = {}
for sub in {r[1] for r in block}:
    for line in open(f"{RAW}/{sub}.posts.jsonl", encoding="utf-8"):
        q = json.loads(line)
        if q["id"] in want: posts[q["id"]] = q
files = {}
for pid, sub, day in block:
    q = posts[pid]; up = f"{RAW}/units/{sub}-{pid}.txt"; files[pid] = up
    if os.path.exists(up): continue
    head = f"POST {pid} | r/{sub} | {d(q['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/\nTITLE: {q.get('title','')}\n\n{q.get('selftext','')}\n\n"
    if not os.path.exists(f"{RAW}/comments/{pid}.json"):      # only with without-replies-ok
        open(up, "w", encoding="utf-8").write(head + "--- ORIGINAL POSTER'S REPLIES IN THE THREAD: not fetched when this file was made ---\n")
        open(f"{out}/posts-without-replies.txt", "a").write(pid + "\n"); continue
    cs = json.load(open(f"{RAW}/comments/{pid}.json")); op = q.get("author") or ""
    if isinstance(cs, dict): mine, cs = cs["own"], [None] * cs["total"]      # written by index_own_replies.py
    else: mine = [c for c in cs if op and op not in ("[deleted]", "AutoModerator") and c.get("author") == op]
    txt = (f"POST {pid} | r/{sub} | {d(q['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/\nTITLE: {q.get('title','')}\n\n{q.get('selftext','')}\n\n"
           f"--- ORIGINAL POSTER'S REPLIES IN THE THREAD: {len(mine)} of {len(cs)} archived comments ---\n")
    for c in mine: txt += f"\nCOMMENT {c['id']} | {d(c['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/comment/{c['id']}/\n{c.get('body','')}\n"
    open(up, "w", encoding="utf-8").write(txt)
ids = [r[0] for r in block]; random.seed(seed + b); random.shuffle(ids)
for i, f in enumerate(names):
    open(f, "w").write("post_id\tpost_file\n" + "".join(f"{p}\t{files[p]}\n" for p in sorted(ids[i::n])))
print(" ".join(f"{b * k + i + 1:03d}" for i in range(n)))
