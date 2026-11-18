#!/usr/bin/env python3
"""From the bulk comment download, write for every post the poster's own replies, in the
place make_block.py and build_post_files.py look for them. Posts already there are left.
  python3 -I _tools/index_own_replies.py <subreddits, comma separated>     (run from ~/GitHub/_research)
Each file comments/<post id>.json becomes {"total": all comments on the post, "own": [the poster's]}."""
import collections, glob, json, os, sys
RAW = "new-and-expecting-mothers/reddit/raw/reddit-2026"; subs = sys.argv[1].split(",")
made = 0
for sub in subs:
    assert json.load(open(f"{RAW}/comments-bulk/{sub}.state")).get("done"), f"{sub} is not fully downloaded"
    author = {}
    for line in open(f"{RAW}/{sub}.posts.jsonl", encoding="utf-8"):
        q = json.loads(line); author[q["id"]] = q.get("author") or ""
    total = collections.Counter(); own = collections.defaultdict(list)
    for f in sorted(glob.glob(f"{RAW}/comments-bulk/{sub}.*.jsonl")):
        for line in open(f, encoding="utf-8"):
            c = json.loads(line); pid = (c.get("link_id") or "")[3:]
            if pid not in author: continue
            total[pid] += 1
            if author[pid] and author[pid] not in ("[deleted]", "AutoModerator") and c.get("author") == author[pid]: own[pid].append(c)
    for pid in author:
        dest = f"{RAW}/comments/{pid}.json"
        if os.path.exists(dest): continue
        json.dump({"total": total[pid], "own": sorted(own[pid], key=lambda c: int(c["created_utc"]))}, open(dest, "w")); made += 1
    print(f"{sub}: {len(author):,} posts, {sum(total.values()):,} comments on them, {sum(len(v) for v in own.values()):,} by the posters", flush=True)
print(f"INDEX-DONE wrote {made:,} files")
