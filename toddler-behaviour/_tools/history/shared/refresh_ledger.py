#!/usr/bin/env python3
"""Refresh the triage/read/quote rows of <niche>/sources/reddit.md from the files on disk.
    python3 -I refresh_ledger.py <niche> <read-label> [...]"""
import csv, glob, json, os, re, sys
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
n, labels = sys.argv[1], sys.argv[2:]; D = os.path.join(R, n)
lab = {}
for f in sorted(glob.glob(os.path.join(D, "_raw/reddit/triage/wave1-*.tsv"))):
    for r in csv.DictReader(open(f), delimiter="\t"): lab[r["post_id"]] = r["label"]
kept = sum(1 for v in lab.values() if v != "drop")
units = set()
for l in labels:
    for line in open(os.path.join(D, "_raw/reddit", l, "chunks.jsonl")): units |= set(json.loads(line)["units"])
recs = [json.loads(x) for f in glob.glob(os.path.join(D, "voice/*.jsonl")) for x in open(f) if x.strip()]
cited = {r["raw_file"] for r in recs}
p = os.path.join(D, "sources/reddit.md"); s = open(p).read()
rows = {"triaged": f"| triaged (wave 1, orchestrator-verified TSVs incl. corrections) | {len(lab):,} |",
        "kept": f"| kept | {kept:,} |",
        "read in full": f"| read in full (units = post + the original poster's replies) | {len(units):,} |",
        "quoted": f"| units with at least one quote · quotes | {len(cited & units):,} · {len(recs):,} |"}
for key, new in rows.items():
    s = re.sub(rf"^\| {re.escape(key)}[^|]*\|[^\n]*$", new, s, count=1, flags=re.M)
open(p, "w").write(s); print(n, len(lab), kept, len(units), len(cited & units), len(recs))
