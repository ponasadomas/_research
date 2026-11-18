#!/usr/bin/env python3
"""Check one reader's output from a read-and-sort pass.
  python3 -I _tools/verify_pass.py <dir> <quotes dir> <prefix> <NN> <highest pattern number>
  (run from ~/GitHub/_research)
Checks: one row per post of the share and no other; allowed values; patterns in range;
every quote word for word in its post file; ids unique and in the agreed form; quotes only
on posts of the share marked yes or near; the quotes column matches the records."""
import collections, html, json, os, re, sys
d, qd, prefix, nn, top = sys.argv[1].rstrip("/"), sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4], int(sys.argv[5])
norm = lambda s: re.sub(r"\s+", " ", html.unescape(s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
share = dict(l.split("\t")[:2] for l in open(f"{d}/reader-{nn}.tsv").read().split("\n")[1:] if l.strip())
pf, qf = f"{d}/posts-{prefix}{nn}.tsv", f"{qd}/reddit-{prefix}{nn}.jsonl"
missing = [f for f in (pf, qf, f"{d}/notes-{prefix}{nn}.md") if not os.path.isfile(f)]
if missing: print(f"{prefix}{nn}: FAIL: missing " + ", ".join(missing)); sys.exit(1)
want = "post_id mark border patterns main_pattern other_what ties_to_development about speaker stage wants already_did paid paid_what quotes note".split()
lines = open(pf, encoding="utf-8").read().split("\n"); problems = []; bad = collections.Counter(); rows = {}
if lines[0].split("\t") != want: problems.append("wrong header")
borders = {"sleep", "feeding", "parent_state", "age_unknown", "age_over_24", "logistics", "other"}
for l in lines[1:]:
    if not l.strip(): continue
    r = dict(zip(want, l.split("\t") + [""] * 16))
    if r["post_id"] in rows: bad["post with two rows"] += 1
    rows[r["post_id"]] = r
    if r["mark"] not in ("yes", "near", "no"): bad["mark not yes, near, no"] += 1; continue
    if not r["about"].strip(): bad["no 'about'"] += 1
    if r["mark"] == "near" and r["border"] not in borders: bad["near without a valid border"] += 1
    if r["mark"] == "no": continue
    try: ps = [int(x) for x in r["patterns"].replace(" ", "").split(",") if x != ""]
    except ValueError: bad["patterns not numbers"] += 1; continue
    if not ps or any(p < 0 or p > top for p in ps): bad["patterns empty or out of range"] += 1
    if r["main_pattern"].strip() not in {str(p) for p in ps}: bad["main_pattern not among patterns"] += 1
    if 0 in ps and not r["other_what"].strip(): bad["pattern 0 without other_what"] += 1
    if r["ties_to_development"] not in ("yes", "no") or r["paid"] not in ("yes", "no"): bad["yes/no column with another value"] += 1
if set(rows) != set(share): problems.append(f"{len(set(share) - set(rows))} posts without a row, {len(set(rows) - set(share))} rows not in the share")
recs = [json.loads(l) for l in open(qf, encoding="utf-8") if l.strip()]
ids = collections.Counter(r["id"] for r in recs)
if any(n > 1 for n in ids.values()): problems.append("duplicate quote ids")
if any(not re.fullmatch(rf"{prefix}{nn}-\d{{4}}", i) for i in ids): problems.append("quote ids not in the agreed form")
per = collections.Counter(); cache = {}
for r in recs:
    p = r.get("post_id"); per[p] += 1
    if p not in share or rows.get(p, {}).get("mark") not in ("yes", "near") or r.get("raw_file") != share[p]: bad["quote on a post outside the share, marked no, or with another raw_file"] += 1; continue
    f = share[p]
    if f not in cache: cache[f] = norm(open(f, encoding="utf-8").read())
    for piece in [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*", r["quote"]) if x.strip()]:
        if norm(piece) not in cache[f]: bad["quote not word for word"] += 1; print(f"  {r['id']} not word for word in {f}"); break
for p, r in rows.items():
    if r["mark"] in ("yes", "near") and str(per.get(p, 0)) != (r["quotes"].strip() or "0"): bad["quotes number differs from the records"] += 1
    if r["mark"] == "yes" and per.get(p, 0) == 0: bad["yes post with no quote"] += 1
problems += [f"{n} x {k}" for k, n in bad.items()]
m = collections.Counter(r["mark"] for r in rows.values())
print(f"{prefix}{nn}: posts {len(rows)} (yes {m['yes']}, near {m['near']}, no {m['no']}), quotes {len(recs)}; " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
