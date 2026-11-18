#!/usr/bin/env python3
"""Check one reader's output from a sample reading.

  python3 -I _tools/verify_reading.py <niche> <niche>/_work/<round>/<label> <prefix> <NN>
  (run from ~/GitHub/_research)

Checks: the posts file has exactly one row for every post in the reader's share and no
other; every mark is yes, near or no; every quote is word for word in its post file; quote
ids are unique and carry the prefix; every quote belongs to a post in the share marked yes
or near; the quotes column matches the number of quote records."""
import collections, html, json, os, re, sys
niche, d, prefix, nn = sys.argv[1], sys.argv[2].rstrip("/"), sys.argv[3], sys.argv[4]
norm = lambda s: re.sub(r"\s+", " ", html.unescape(s).replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()
share = dict(l.rstrip("\n").split("\t") for l in open(f"{d}/reader-{nn}.tsv").readlines()[1:])
problems = []
pf, qf = f"{d}/posts-{prefix}{nn}.tsv", f"{niche}/quotes/reddit-{prefix}{nn}.jsonl"
for f in (pf, qf, f"{d}/notes-{prefix}{nn}.md"):
    if not os.path.isfile(f): problems.append(f"missing {f}")
if problems: print(f"{prefix}{nn}: FAIL: " + "; ".join(problems)); sys.exit(1)
lines = open(pf, encoding="utf-8").read().split("\n"); head = lines[0].split("\t")
want = "post_id mark about speaker stage wants already_did_or_paid her_words quotes unsure_why".split()
if head != want: problems.append(f"posts header is {head}")
rows = {}
for l in lines[1:]:
    if not l.strip(): continue
    c = l.split("\t") + [""] * 10
    if c[0] in rows: problems.append(f"post {c[0]} has two rows")
    rows[c[0]] = dict(zip(want, c))
if set(rows) - set(share): problems.append(f"{len(set(rows) - set(share))} rows not in the share")
if set(share) - set(rows): problems.append(f"{len(set(share) - set(rows))} posts of the share have no row")
bad = [p for p, r in rows.items() if r["mark"] not in ("yes", "near", "no")]
if bad: problems.append(f"{len(bad)} rows with a mark other than yes, near, no")
noabout = [p for p, r in rows.items() if not r["about"].strip()]
if noabout: problems.append(f"{len(noabout)} rows with no 'about'")
recs = [json.loads(l) for l in open(qf, encoding="utf-8") if l.strip()]
ids = collections.Counter(r["id"] for r in recs)
if any(n > 1 for n in ids.values()): problems.append("duplicate quote ids")
if any(not re.fullmatch(rf"{prefix}{nn}-\d{{4}}", i) for i in ids): problems.append("quote ids not in the agreed form")
per = collections.Counter(); notin = wrongpost = 0; cache = {}
for r in recs:
    p = r.get("post_id"); per[p] += 1
    if p not in share or rows.get(p, {}).get("mark") not in ("yes", "near"): wrongpost += 1; continue
    f = share[p]
    if r.get("raw_file") != f: wrongpost += 1; continue
    if f not in cache: cache[f] = norm(open(f, encoding="utf-8").read())
    for piece in [x for x in re.split(r"\s*\[…\]\s*|\s*\[\.\.\.\]\s*", r["quote"]) if x.strip()]:
        if norm(piece) not in cache[f]: notin += 1; print(f"  {r['id']} not word for word in {f}"); break
if notin: problems.append(f"{notin} quotes not word for word")
if wrongpost: problems.append(f"{wrongpost} quotes on a post outside the share, marked no, or with another raw_file")
miscount = [p for p, r in rows.items() if r["mark"] in ("yes", "near") and str(per.get(p, 0)) != (r["quotes"].strip() or "0")]
if miscount: problems.append(f"{len(miscount)} rows whose quotes number differs from the records")
m = collections.Counter(r["mark"] for r in rows.values())
print(f"{prefix}{nn}: posts {len(rows)} (yes {m['yes']}, near {m['near']}, no {m['no']}), quotes {len(recs)}; " + ("OK" if not problems else "FAIL: " + "; ".join(problems)))
sys.exit(1 if problems else 0)
