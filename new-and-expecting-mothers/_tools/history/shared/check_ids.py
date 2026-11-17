#!/usr/bin/env python3
"""Duplicate-id and prefix check across one niche's voice files.  python3 -I check_ids.py <niche>"""
import collections, glob, json, os, sys
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", sys.argv[1], "voice"))
c = collections.Counter(); files = collections.defaultdict(set)
for f in glob.glob(os.path.join(R, "*.jsonl")):
    for line in open(f):
        if line.strip():
            i = json.loads(line)["id"]; c[i] += 1; files[i].add(os.path.basename(f))
d = {i: sorted(files[i]) for i, n in c.items() if n > 1}
print(f"{sum(c.values())} records, {len(c)} distinct ids, {len(d)} duplicated")
for i, fs in list(d.items())[:50]: print(" DUP", i, fs)
sys.exit(1 if d else 0)
