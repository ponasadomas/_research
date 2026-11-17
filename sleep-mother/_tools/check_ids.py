#!/usr/bin/env python3
"""Duplicate-id check across this niche's quote files.  python3 -I check_ids.py"""
import collections, glob, json, os, sys
Q = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "quotes")
c = collections.Counter(); files = collections.defaultdict(set)
for f in glob.glob(os.path.join(Q, "*.jsonl")):
    for line in open(f):
        if line.strip():
            i = json.loads(line)["id"]; c[i] += 1; files[i].add(os.path.basename(f))
d = {i: sorted(files[i]) for i, n in c.items() if n > 1}
print(f"{sum(c.values())} records, {len(c)} distinct ids, {len(d)} duplicated")
for i, fs in list(d.items())[:50]: print(" DUP", i, fs)
sys.exit(1 if d or not c else 0)
