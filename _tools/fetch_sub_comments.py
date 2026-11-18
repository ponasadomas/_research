#!/usr/bin/env python3
"""Download every comment of the named subreddits for a date range from the Arctic Shift
archive, by paging through each subreddit by date. Safe to stop; run again to go on.
  python3 -I _tools/fetch_sub_comments.py <first day> <last day> <subreddits, comma separated> [streams=4]
  (run from ~/GitHub/_research)
Writes new-and-expecting-mothers/reddit/raw/reddit-2026/comments-bulk/<sub>.<yyyy-mm>.jsonl,
one comment per line (id, link_id, parent_id, author, created_utc, body), and <sub>.state
with the time reached. A subreddit is finished when its state file says "done"."""
import datetime, json, os, sys, threading, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
ts = lambda d: int(datetime.datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc).timestamp())
START, END = ts(sys.argv[1]), ts(sys.argv[2]) + 86400
subs = sys.argv[3].split(","); streams = int(sys.argv[4]) if len(sys.argv) > 4 else 4
OUT = "new-and-expecting-mothers/reddit/raw/reddit-2026/comments-bulk"; os.makedirs(OUT, exist_ok=True)
API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=auto&sort=asc&fields=id,link_id,parent_id,author,created_utc,body"
prog = {}; lock = threading.Lock()
def get(url):
    for attempt in range(12):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=120) as r: return json.load(r)["data"] or []
        except urllib.error.HTTPError as e:
            wait = int(e.headers.get("X-RateLimit-Reset", "20")) + 1 if e.code == 429 else 10 * (attempt + 1)
            time.sleep(min(wait, 120))
        except Exception: time.sleep(10 * (attempt + 1))
    raise RuntimeError("gave up on " + url)
def one(sub):
    st = f"{OUT}/{sub}.state"; at = START; n = 0
    if os.path.exists(st):
        s = json.load(open(st))
        if s.get("done"): prog[sub] = ("done", s["comments"]); return
        at, n = s["at"], s["comments"]
    recent = set()
    while True:
        data = get(f"{API}&subreddit={sub}&after={at - 1}&before={END}")
        new = [c for c in data if c["id"] not in recent]
        if not new:
            if not data or len(data) < 100: break
            at = int(data[-1]["created_utc"]) + 1; continue
        by = {}
        for c in new:
            m = datetime.datetime.fromtimestamp(int(c["created_utc"]), datetime.timezone.utc).strftime("%Y-%m")
            by.setdefault(m, []).append(json.dumps(c, ensure_ascii=False))
        for m, ls in by.items():
            with open(f"{OUT}/{sub}.{m}.jsonl", "a", encoding="utf-8") as f: f.write("\n".join(ls) + "\n")
        n += len(new); at = int(new[-1]["created_utc"]); recent = {c["id"] for c in data if int(c["created_utc"]) >= at - 1}
        json.dump({"at": at, "comments": n}, open(st, "w")); prog[sub] = (at, n)
        if len(data) < 100: break
        time.sleep(0.2)
    json.dump({"done": True, "at": at, "comments": n}, open(st, "w")); prog[sub] = ("done", n)
def report():
    while True:
        time.sleep(60)
        parts = []
        for s in subs:
            a, n = prog.get(s, (None, 0))
            parts.append(f"{s} " + ("waiting" if a is None else "DONE" if a == "done" else datetime.datetime.fromtimestamp(a, datetime.timezone.utc).strftime("%b %d")) + f" {n:,}")
        print(f"  {time.strftime('%H:%M')}  total {sum(v[1] for v in prog.values()):,} comments | " + " | ".join(parts), flush=True)
threading.Thread(target=report, daemon=True).start()
print(f"downloading all comments of {len(subs)} subreddits, {sys.argv[1]} to {sys.argv[2]}, {streams} at a time", flush=True)
with ThreadPoolExecutor(streams) as ex: list(ex.map(one, subs))
print(f"BULK-DONE {sum(v[1] for v in prog.values()):,} comments")
