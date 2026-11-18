#!/usr/bin/env python3
"""Draw a random sample of this niche's on-topic Reddit posts and make a reading unit for each
(the post plus the original poster's own replies), split into reader shares.
  python3 -I _tools/build_sample_units.py <label> <size> <seed> <readers>      (run from the niche folder)
Frame: every post in _work/reddit-selection/filter-v1/index.jsonl whose body is available,
whatever its tier and whether or not it was read before. Units are shared across niches and
never rewritten. Comments come from the Arctic Shift archive and are cached."""
import collections, datetime, json, os, random, sys, time, urllib.request
label, size, seed, readers = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
SEL = "_work/reddit-selection"; RAW = "../new-and-expecting-mothers/reddit/raw/reddit-2026"
out = f"{SEL}/{label}"; os.makedirs(out, exist_ok=True)
API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=100&fields=id,body,author,parent_id,created_utc&link_id="
d = lambda ts: datetime.datetime.fromtimestamp(int(ts), datetime.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
idx = [json.loads(l) for l in open(f"{SEL}/filter-v1/index.jsonl") if l.strip()]
frame = [r for r in idx if r.get("tier") != "unavailable"]
random.seed(seed); sample = random.sample(frame, size)
want = {r["id"] for r in sample}; posts = {}
for f in os.listdir(RAW):
    if f.endswith(".posts.jsonl"):
        for line in open(os.path.join(RAW, f)):
            q = json.loads(line)
            if q["id"] in want: q["subreddit"] = f[:-len(".posts.jsonl")]; posts[q["id"]] = q
def comments(pid):
    dest = os.path.join(RAW, "comments", pid + ".json")
    if os.path.exists(dest): return json.load(open(dest))
    data, after = [], None
    for _ in range(30):
        url = API + pid + (f"&after={after}" if after else "") + "&sort=asc"
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=60) as r: batch = json.load(r)["data"] or []
                break
            except Exception: time.sleep(3 * (attempt + 1))
        else: raise SystemExit(f"comments failed for {pid}")
        data += batch; time.sleep(0.4)
        if len(batch) < 100: break
        after = batch[-1]["created_utc"]
    json.dump(data, open(dest, "w")); return data
rows = []; made = 0
for r in sample:
    pid = r["id"]
    if pid not in posts: rows.append((pid, r["subreddit"], r["date"][:10], r["tier"], "", 0, "post not in archive")); continue
    q = posts[pid]; sub = q["subreddit"]; up = os.path.join(RAW, "units", f"{sub}-{pid}.txt")
    if not os.path.exists(up):
        cs = comments(pid); op = q.get("author") or ""
        mine = [c for c in cs if op and op not in ("[deleted]", "AutoModerator") and c.get("author") == op]
        txt = (f"POST {pid} | r/{sub} | {d(q['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/\nTITLE: {q.get('title','')}\n\n{q.get('selftext','')}\n\n"
               f"--- ORIGINAL POSTER'S REPLIES IN THE THREAD: {len(mine)} of {len(cs)} archived comments ---\n")
        for c in mine: txt += f"\nCOMMENT {c['id']} | {d(c['created_utc'])} | https://www.reddit.com/r/{sub}/comments/{pid}/comment/{c['id']}/\n{c.get('body','')}\n"
        open(up, "w", encoding="utf-8").write(txt); made += 1
    rows.append((pid, sub, r["date"][:10], r["tier"], f"{RAW}/units/{sub}-{pid}.txt", os.path.getsize(up), ""))
rows.sort(key=lambda x: x[0])                      # order by id, which is unrelated to tier or subject
ok = [x for x in rows if x[4]]
open(f"{out}/sample.tsv", "w").write("post_id\tsubreddit\tdate\ttier\tunit\tbytes\tnote\n" + "".join("\t".join(map(str, x)) + "\n" for x in rows))
for n in range(readers):
    share = ok[n::readers]
    open(f"{out}/reader-{n+1:02d}.tsv", "w").write("post_id\tunit\n" + "".join(f"{x[0]}\t{x[4]}\n" for x in share))
print(json.dumps({"frame": len(frame), "sample": len(sample), "units_made": made, "missing": len(rows) - len(ok),
                  "tiers": collections.Counter(x[3] for x in rows), "bytes": sum(x[5] for x in ok), "per_reader": [len(ok[n::readers]) for n in range(readers)]}))
