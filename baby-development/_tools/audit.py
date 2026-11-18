#!/usr/bin/env python3
"""Coverage check for this niche: every post handed to a reader is either quoted or named in a
reading ledger. Writes nothing.
    python3 -I audit.py <read-label> [<read-label> ...]     labels are folders in _work/reddit-selection/
(The script that generated evidence/counts.md and quotes/merged/all.jsonl is history/shared/audit_niche.py.)"""
import collections, glob, json, os, random, re, sys
D = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
check_only = True
labels = [arg for arg in sys.argv[1:] if arg != "--check-only"]
ARCHIVE = "../new-and-expecting-mothers/reddit/raw/"
def moved(p):   # reading lists were written before the move and still use the old archive path
    return ARCHIVE + p[len("../_shared/_raw/"):] if p.startswith("../_shared/_raw/") else p
recs = []
for f in sorted(glob.glob(os.path.join(D, "quotes", "2026-10", "*.jsonl"))):
    for l in open(f):
        if l.strip():
            r = json.loads(l); r["_file"] = os.path.basename(f); recs.append(r)
# Historical labels only: no quote is actively restricted.
restr = set()
rp = os.path.join(D, "evidence", "2026-10", "restricted-ids.md")
if os.path.exists(rp):
    for line in open(rp):
        if line.startswith("|") and not line.startswith("| id") and not line.startswith("|---"):
            cell = line.split("|")[1]
            for m in re.finditer(r"([a-z]{2,3}\d{1,2})-(\d{4})((?:\s*,\s*\d{4})*)", cell):
                restr.add(f"{m.group(1)}-{m.group(2)}")
                for extra in re.findall(r"\d{4}", m.group(3)): restr.add(f"{m.group(1)}-{extra}")
            for m in re.finditer(r"([a-z]{2,3}\d{1,2})-(\d{4})–(\d{4})", cell):
                for i in range(int(m.group(2)), int(m.group(3)) + 1): restr.add(f"{m.group(1)}-{i:04d}")
# coverage
assigned = set()
for lab in labels:
    for l in open(os.path.join(D, "_work", "2026-10", "reddit-selection", lab, "chunks.jsonl")):
        assigned |= set(moved(u) for u in json.loads(l)["units"])
cited = collections.Counter(r["raw_file"] for r in recs)
uncited = sorted(u for u in assigned if u not in cited)
ledgers = " ".join(open(f).read() for f in glob.glob(os.path.join(D, "_work", "2026-10", "reading-ledgers", "reddit-reading-*.md")))
unexplained = [u for u in uncited if os.path.basename(u)[:-4] not in ledgers and os.path.basename(u)[:-4].split("-", 1)[1] not in ledgers]
# Descriptive sweep; a match never excludes evidence.
SAFE = re.compile(r"kill myself|suicid|self.?harm|want to die|hurt (?:myself|my baby|him|her)|shak(?:e|ing|en) (?:the|my|him|her)|smack|spank|slap|hit (?:him|her|my)|abus|sids|stopped breathing|not breathing|face down|suffocat|smother|died|dead\b|funeral|psychosis|intrusive thought|cps\b|police|asleep at the wheel|car accident|crash", re.I)
hits = [(r["id"], m.group(0), r["quote"][:160].replace("\t", " ").replace("\n", " ")) for r in recs if (m := SAFE.search(r["quote"]))]
if check_only:
    print(json.dumps({"quotes": len(recs), "assigned": len(assigned), "units_quoted": len(cited),
                      "assigned_units_quoted": len(assigned & set(cited)), "uncited": len(uncited),
                      "unexplained": len(unexplained), "historically_marked": len(restr),
                      "active_restrictions": 0, "safety_hits": len(hits)}))
    for u in unexplained:
        print("UNEXPLAINED", u)
    sys.exit(1 if unexplained else 0)
