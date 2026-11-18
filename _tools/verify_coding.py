#!/usr/bin/env python3
"""Check one coder's output from a pattern-sorting pass.
  python3 -I _tools/verify_coding.py <dir> <prefix> <NN> <highest pattern number>
  (run from ~/GitHub/_research; <dir> holds coder-NN.tsv and coded-<prefix>NN.tsv)"""
import collections, os, sys
d, prefix, nn, top = sys.argv[1].rstrip("/"), sys.argv[2], sys.argv[3], int(sys.argv[4])
share = [l.split("\t")[0] for l in open(f"{d}/coder-{nn}.tsv").read().split("\n")[1:] if l.strip()]
f = f"{d}/coded-{prefix}{nn}.tsv"
if not os.path.isfile(f): print(f"{prefix}{nn}: FAIL: missing {f}"); sys.exit(1)
want = "post_id mark border patterns main_pattern other_what ties_to_development paid paid_what note".split()
lines = open(f, encoding="utf-8").read().split("\n"); problems = []
if lines[0].split("\t") != want: problems.append("wrong header")
rows = {}; bad = collections.Counter()
borders = {"sleep", "feeding", "parent_state", "age_unknown", "age_over_24", "logistics", "other"}
for l in lines[1:]:
    if not l.strip(): continue
    r = dict(zip(want, l.split("\t") + [""] * 10))
    if r["post_id"] in rows: bad["post with two rows"] += 1
    rows[r["post_id"]] = r
    if r["mark"] not in ("yes", "near", "no"): bad["mark not yes, near, no"] += 1; continue
    if r["mark"] == "near" and r["border"] not in borders: bad["near without a valid border"] += 1
    if r["mark"] != "near" and r["border"].strip(): bad["border on a post that is not near"] += 1
    if r["mark"] == "no": continue
    try: ps = [int(x) for x in r["patterns"].replace(" ", "").split(",") if x != ""]
    except ValueError: bad["patterns not numbers"] += 1; continue
    if not ps or any(p < 0 or p > top for p in ps): bad["patterns empty or out of range"] += 1
    if r["main_pattern"].strip() not in {str(p) for p in ps}: bad["main_pattern not among patterns"] += 1
    if 0 in ps and not r["other_what"].strip(): bad["pattern 0 without other_what"] += 1
    if r["ties_to_development"] not in ("yes", "no") or r["paid"] not in ("yes", "no"): bad["yes/no column with another value"] += 1
if set(rows) != set(share): problems.append(f"{len(set(share) - set(rows))} posts without a row, {len(set(rows) - set(share))} rows not in the share")
problems += [f"{n} rows: {k}" for k, n in bad.items()]
m = collections.Counter(r["mark"] for r in rows.values())
print(f"{prefix}{nn}: posts {len(rows)} (yes {m['yes']}, near {m['near']}, no {m['no']}); " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
