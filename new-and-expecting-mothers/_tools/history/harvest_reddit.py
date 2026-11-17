#!/usr/bin/env python3
"""Bulk-download a subreddit's posts for a date range from the Arctic Shift archive.

Reddit itself blocks this machine (403 / "Welcome to Reddit" wall), and the archive's
text search times out, so we page through every post by date and filter locally.

    python3 harvest_reddit.py Divorce 2025-10-01 2026-10-13

Appends to _raw/reddit/<sub>.posts.jsonl and resumes from the newest post already saved.
"""
import json, sys, time, urllib.request, urllib.parse, datetime, os

API = "https://arctic-shift.photon-reddit.com/api/posts/search"
FIELDS = "id,title,selftext,score,num_comments,created_utc,author,link_flair_text"
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_raw", "reddit")


def ts(d):
    return int(datetime.datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=datetime.timezone.utc).timestamp())


def get(params):
    url = API + "?" + urllib.parse.urlencode(params)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=60) as r:
                return json.load(r)["data"] or []
        except Exception as e:
            time.sleep(3 * (attempt + 1))
    raise SystemExit(f"gave up on {url}")


def main():
    sub, start, end = sys.argv[1], ts(sys.argv[2]), ts(sys.argv[3])
    path = os.path.join(RAW, f"{sub}.posts.jsonl")
    seen = set()
    if os.path.exists(path):
        for line in open(path):
            p = json.loads(line)
            seen.add(p["id"])
            start = max(start, p["created_utc"])
    out = open(path, "a")
    n = 0
    while start < end:
        batch = get({"subreddit": sub, "limit": 100, "after": start, "before": end, "sort": "asc", "fields": FIELDS})
        if not batch:
            break
        for p in batch:
            if p["id"] not in seen:
                seen.add(p["id"])
                out.write(json.dumps(p) + "\n")
                n += 1
        out.flush()
        nxt = batch[-1]["created_utc"]
        start = nxt if nxt > start else start + 1
        time.sleep(0.6)
    print(f"{sub}: +{n} posts, {len(seen)} total")


if __name__ == "__main__":
    main()
