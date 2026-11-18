#!/usr/bin/env python3
"""Check that no quote id is used twice in a niche, across all its rounds.
  python3 -I _tools/check_ids.py <niche>        (run from ~/GitHub/_research)
Reads every .jsonl under <niche>/quotes/ except generated copies in a merged/ folder."""
import collections, glob, json, os, sys
c = collections.Counter(); where = collections.defaultdict(set)
for f in glob.glob(os.path.join(sys.argv[1], "quotes", "**", "*.jsonl"), recursive=True):
    if os.sep + "merged" + os.sep in f: continue
    for line in open(f):
        if line.strip(): i = json.loads(line)["id"]; c[i] += 1; where[i].add(f)
dup = {i: sorted(where[i]) for i, n in c.items() if n > 1}
print(f"{sum(c.values())} records, {len(c)} distinct ids, {len(dup)} duplicated")
for i, fs in list(dup.items())[:50]: print(" DUP", i, fs)
sys.exit(1 if dup or not c else 0)
