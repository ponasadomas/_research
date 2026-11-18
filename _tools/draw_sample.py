#!/usr/bin/env python3
"""Draw a random sample of Reddit posts from the shared archive for one niche.

  python3 -I _tools/draw_sample.py <niche> <round> <label> <size> <seed> --subs A,B,C [--only-ids FILE]
  (run from ~/GitHub/_research)

Pool: every post in the named subreddits whose text is still there. No keyword is applied.
--only-ids FILE narrows the pool to the post ids listed in FILE (one per line), for a sample
of the posts a word list matched. The same seed always gives the same sample.
Writes <niche>/_work/<round>/<label>/sample.tsv and pool.json."""
import datetime, json, os, random, sys
a = sys.argv[1:]
opt = lambda k: a[a.index(k) + 1] if k in a else None
niche, rnd, label, size, seed = a[0], a[1], a[2], int(a[3]), int(a[4])
subs = sorted(opt("--subs").split(","))
only = opt("--only-ids")
only = {l.split()[0] for l in open(only) if l.strip()} if only else None
RAW = "new-and-expecting-mothers/reddit/raw/reddit-2026"
pool, gone = [], 0
for sub in subs:
    for line in open(f"{RAW}/{sub}.posts.jsonl", encoding="utf-8"):
        q = json.loads(line)
        if only is not None and q["id"] not in only: continue
        if (q.get("selftext") or "").strip() in ("", "[removed]", "[deleted]"): gone += 1; continue
        day = datetime.datetime.fromtimestamp(int(q["created_utc"]), datetime.timezone.utc).strftime("%Y-%m-%d")
        pool.append((q["id"], sub, day))
pool.sort()
random.seed(seed); sample = sorted(random.sample(pool, size))
out = f"{niche}/_work/{rnd}/{label}"; os.makedirs(out, exist_ok=True)
open(f"{out}/sample.tsv", "w").write("post_id\tsubreddit\tdate\n" + "".join("\t".join(x) + "\n" for x in sample))
info = {"subreddits": subs, "pool": len(pool), "text_gone_not_in_pool": gone, "sample": size, "seed": seed,
        "narrowed_to_ids_from": opt("--only-ids"), "first_day": min(x[2] for x in pool), "last_day": max(x[2] for x in pool)}
json.dump(info, open(f"{out}/pool.json", "w"), indent=1); print(json.dumps(info))
