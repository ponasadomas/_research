#!/usr/bin/env python3
"""Fetch and cache the replies for every post of a sample, several at a time, so that
build_post_files.py afterwards runs from the cache. Safe to stop and run again.
  python3 -I _tools/fetch_replies.py <niche>/_work/<round>/<label> [workers=4]"""
import json, os, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor
out = sys.argv[1].rstrip("/"); workers = int(sys.argv[2]) if len(sys.argv) > 2 else 4
RAW = "new-and-expecting-mothers/reddit/raw/reddit-2026"
API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=100&fields=id,body,author,parent_id,created_utc&link_id="
ids = [l.split("\t")[0] for l in open(f"{out}/sample.tsv").read().split("\n")[1:] if l.strip()]
todo = [p for p in ids if not os.path.exists(f"{RAW}/comments/{p}.json")]
print(f"{len(ids)} posts, {len(ids) - len(todo)} already fetched, {len(todo)} to fetch, {workers} at a time", flush=True)
def fetch(pid):
    data, after = [], None
    for _ in range(30):
        url = API + pid + (f"&after={after}" if after else "") + "&sort=asc"
        for attempt in range(6):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "research"}), timeout=60) as r: batch = json.load(r)["data"] or []
                break
            except Exception: time.sleep(5 * (attempt + 1))
        else: return pid, False
        data += batch; time.sleep(0.4)
        if len(batch) < 100: break
        after = batch[-1]["created_utc"]
    tmp = f"{RAW}/comments/{pid}.json.tmp"; json.dump(data, open(tmp, "w")); os.replace(tmp, f"{RAW}/comments/{pid}.json"); return pid, True
done = failed = 0; t0 = time.time()
with ThreadPoolExecutor(workers) as ex:
    for pid, ok in ex.map(fetch, todo):
        done += ok; failed += not ok
        if (done + failed) % 100 == 0:
            rate = (done + failed) / (time.time() - t0); left = (len(todo) - done - failed) / rate / 60
            print(f"  {time.strftime('%H:%M:%S')}  {done + failed} of {len(todo)} fetched, {failed} failed, about {left:.0f} minutes left", flush=True)
print(f"FETCH-DONE fetched {done}, failed {failed}. Run again to retry failed ones." )
