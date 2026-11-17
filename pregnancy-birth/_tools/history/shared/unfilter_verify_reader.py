#!/usr/bin/env python3
"""Check one unfilter reader's output.  python3 -I unfilter_verify_reader.py <niche> <NN> <id-prefix>
Exit 0 when every quote is found in its raw file, ids are unique and the ledger covers the assignment."""
import csv, json, os, re, sys
niche, nn, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
R = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", niche))
norm = lambda s: re.sub(r"\s+", " ", s).strip()
cache = {}
def strings(o):
    if isinstance(o, str): yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
def raw(p):
    if p not in cache:
        if p.endswith(".gz"):
            import gzip; t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read()
        else: t = open(p, encoding="utf-8", errors="replace").read()
        parts = []
        if ".jsonl" in p:
            for l in t.split("\n"):
                try: parts.extend(strings(json.loads(l)))
                except Exception: continue
        elif ".json" in p:
            try: parts.extend(strings(json.loads(t)))
            except Exception: pass
        if parts: t = t + "\n" + "\n".join(parts)
        cache.clear(); cache[p] = norm(t)
    return cache[p]
vf = os.path.join(R, "voice", f"reddit-ur{nn}.jsonl"); lf = os.path.join(R, "sources", f"reddit-reading-ur{nn}.md")
problems = []
if not os.path.exists(vf): problems.append("no voice file")
if not os.path.exists(lf): problems.append("no ledger")
recs = []
if os.path.exists(vf):
    for k, l in enumerate(open(vf), 1):
        if not l.strip(): continue
        try: recs.append(json.loads(l))
        except Exception: problems.append(f"line {k}: not JSON")
ids = [r.get("id", "") for r in recs]
if len(ids) != len(set(ids)): problems.append("duplicate ids")
badp = [i for i in ids if not re.fullmatch(re.escape(prefix + nn) + r"-\d{4}", i)]
if badp: problems.append(f"{len(badp)} ids with the wrong prefix")
miss = bad = 0
for r in sorted(recs, key=lambda r: r.get("raw_file", "")):
    p = os.path.normpath(os.path.join(R, r.get("raw_file", "")))
    if not os.path.isfile(p): miss += 1; continue
    segs = [s for s in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*", r.get("quote", "")) if s.strip()]
    if not segs or not all(norm(s) in raw(p) for s in segs): bad += 1
if miss: problems.append(f"{miss} quotes whose raw_file is missing")
if bad: problems.append(f"{bad} quotes not found in their raw file")
asg = [r[1] for r in list(csv.reader(open(os.path.join(R, "scratchpad", "unfilter-reread", f"assign-ur{nn}.tsv")), delimiter="\t"))[1:] if len(r) > 1]
led = open(lf, encoding="utf-8", errors="replace").read() if os.path.exists(lf) else ""
unc = [a for a in asg if a.split("-")[-1] not in led]
if len(unc) > max(3, len(asg) // 50): problems.append(f"{len(unc)} of {len(asg)} assigned rows missing from the ledger")
print(f"{niche} ur{nn}: assigned {len(asg)}, quotes {len(recs)}, not in ledger {len(unc)}; " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
