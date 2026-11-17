#!/usr/bin/env python3
"""Download all archived comments for Reddit post ids into _raw/reddit/comments/<id>.json.

    python3 fetch_comments.py 1tuc51e 1ttc9s4 ...
"""
import json, sys, time, urllib.request, os

API = "https://arctic-shift.photon-reddit.com/api/comments/search?limit=100&fields=id,body,score,author,parent_id,created_utc&link_id="
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_raw", "reddit", "comments")
os.makedirs(OUT, exist_ok=True)

for pid in sys.argv[1:]:
    dest = os.path.join(OUT, pid + ".json")
    if os.path.exists(dest):
        continue
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(API + pid, headers={"User-Agent": "research"}), timeout=60) as r:
                data = json.load(r)["data"] or []
            json.dump(data, open(dest, "w"))
            break
        except Exception:
            time.sleep(3 * (attempt + 1))
    time.sleep(0.6)
