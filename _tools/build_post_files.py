#!/usr/bin/env python3
"""Make one reading file per sampled post (the post plus the original poster's own replies)
and split the sample into reader shares.

  python3 -I _tools/build_post_files.py <niche>/_work/<round>/<label> <readers>
  (run from ~/GitHub/_research, after draw_sample.py)

Post files are shared by all niches, live in the archive's units/ folder and are never
rewritten. Replies come from the Arctic Shift archive and are cached in comments/.
Writes reader-NN.tsv next to sample.tsv; shares are dealt out in post-id order."""
import datetime, json, os, sys, time, urllib.request
out, readers = sys.argv[1].rstrip("/"), int(sys.argv[2])
RAW = "new-and-expecting-mothers/reddit/raw/reddit-2026"
API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=100&fields=id,body,author,parent_id,created_utc&link_id="
d = lambda ts: datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
sample = [l.rstrip("\n").split("\t") for l in open(f"{out}/sample.tsv")][1:]
want = {r[0] for r in sample}; posts = {}
for sub in {r[1] for r in sample}:
    for line in open(f"{RAW}/{sub}.posts.jsonl", encoding="utf-8"):
        q = json.loads(line)
        if q["id"] in want: posts[q["id"]] = q
def comments(pid):
    dest = f"{RAW}/comments/{pid}.json"
    if os.path.exists(dest): return json.load(open(dest))
    data, after = [], None
    for _ in range(30):
        url = API + pid + (f"&after={after}" if after else "") + "&sort=asc"
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=60) as r: batch = json.load(r)["data"] or []
                break
            except Exception: time.sleep(3 * (attempt + 1))
        else: raise SystemExit(f"replies could not be fetched for {pid}; run again to resume")
        data += batch; time.sleep(0.4)
        if len(batch) < 100: break
        after = batch[-1]["created_utc"]
    json.dump(data, open(dest, "w")); return data
rows, made, size = [], 0, 0
for pid, sub, day in sample:
    q = posts[pid]; up = f"{RAW}/units/{sub}-{pid}.txt"
    if not os.path.exists(up):
        cs = comments(pid); op = q.get("author") or ""
        mine = [c for c in cs if op and op not in ("[deleted]", "AutoModerator") and c.get("author") == op]
        txt = (f"POST {pid} | r/{sub} | {d(q['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/\nTITLE: {q.get('title','')}\n\n{q.get('selftext','')}\n\n"
               f"--- ORIGINAL POSTER'S REPLIES IN THE THREAD: {len(mine)} of {len(cs)} archived comments ---\n")
        for c in mine: txt += f"\nCOMMENT {c['id']} | {d(c['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/comment/{c['id']}/\n{c.get('body','')}\n"
        open(up, "w", encoding="utf-8").write(txt); made += 1
    rows.append((pid, up)); size += os.path.getsize(up)
for n in range(readers):
    open(f"{out}/reader-{n+1:02d}.tsv", "w").write("post_id\tpost_file\n" + "".join(f"{p}\t{u}\n" for p, u in rows[n::readers]))
print(json.dumps({"posts": len(rows), "post_files_made_now": made, "bytes": size, "per_reader": [len(rows[n::readers]) for n in range(readers)]}))
