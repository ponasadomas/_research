#!/usr/bin/env python3
"""Step 3 of the chain: merge a read-and-sort pass and count posts per pattern.
  python3 -I _tools/count_patterns.py <niche> <round> <label> <prefix> <highest pattern number> <patterns.md>
  (run from ~/GitHub/_research; reads <niche>/_work/<round>/<label>/ and <niche>/quotes/reddit-<prefix>NNN.jsonl)
Writes <niche>/evidence/<round>/<label>/: posts.tsv (every post, one row), counts.md (the
counts), pattern-NN.md (each pattern's posts with their quotes, nothing selected).
Only readers that pass verify_pass.py are counted. Fails if a counted post has two rows."""
import collections, csv, glob, json, os, re, subprocess, sys
niche, rnd, label, prefix, top, patfile = sys.argv[1:7]; top = int(top)
d, qd, out = f"{niche}/_work/{rnd}/{label}", f"{niche}/quotes", f"{niche}/evidence/{rnd}/{label}"
os.makedirs(out, exist_ok=True)
names = {0: "None of these"}
for l in open(patfile):
    m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", l)
    if m: names[int(m.group(1))] = m.group(2)
sample = {r["post_id"]: r for r in csv.DictReader(open(f"{d}/sample.tsv"), delimiter="\t")}
pool = json.load(open(f"{d}/pool.json"))
shares = sorted(re.search(r"reader-(\d+)\.tsv", f).group(1) for f in glob.glob(f"{d}/reader-*.tsv"))
rows, per_reader, failed, quotes = {}, {}, [], collections.defaultdict(list)
for nn in shares:
    if subprocess.run([sys.executable, "-I", "_tools/verify_pass.py", d, qd, prefix, nn, str(top)], capture_output=True).returncode:
        failed.append(nn); continue
    mine = list(csv.DictReader(open(f"{d}/posts-{prefix}{nn}.tsv", encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_NONE))
    for r in mine:
        if r["post_id"] in rows: sys.exit(f"FAIL: post {r['post_id']} has two rows")
        if r["post_id"] not in sample: sys.exit(f"FAIL: post {r['post_id']} is not in the sample")
        r["reader"] = prefix + nn; r.update(subreddit=sample[r["post_id"]]["subreddit"], date=sample[r["post_id"]]["date"]); rows[r["post_id"]] = r
    per_reader[nn] = collections.Counter(r["mark"] for r in mine)
    for l in open(f"{qd}/reddit-{prefix}{nn}.jsonl", encoding="utf-8"):
        if l.strip(): q = json.loads(l); quotes[q["post_id"]].append(q)
R = list(rows.values()); N = len(R)
cols = "post_id subreddit date reader mark border patterns main_pattern other_what ties_to_development about speaker stage wants already_did paid paid_what quotes note".split()
with open(f"{out}/posts.tsv", "w", encoding="utf-8") as f:
    f.write("\t".join(cols) + "\n")
    for r in sorted(R, key=lambda r: (r["date"], r["post_id"])): f.write("\t".join(r[c] or "" for c in cols) + "\n")
yes = [r for r in R if r["mark"] == "yes"]; near = [r for r in R if r["mark"] == "near"]
tied = [r for r in near if r["ties_to_development"] == "yes"]
pc = lambda a, b: f"{100 * a / b:.1f}%" if b else "-"
def table(head, lines): return ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)] + ["| " + " | ".join(str(x) for x in l) + " |" for l in lines] + [""]
def tally(rs, key, base=None):
    c = collections.Counter(key(r) or "(empty)" for r in rs); base = base or len(rs)
    return [(k, n, pc(n, base)) for k, n in c.most_common()]
def pats(r): return [int(x) for x in r["patterns"].replace(" ", "").split(",") if x.isdigit()]
nq = sum(len(quotes[r["post_id"]]) for r in R)
months = collections.Counter(r["date"][:7] for r in R)
L = [f"# Post counts by pattern: {niche}, {label} ({rnd})", "",
     f"Made by `_tools/count_patterns.py` from the readers' files in `{d}/`. Nothing here was chosen by hand.", "",
     "## Read this first", "",
     f"- **How the posts were chosen:** {json.dumps(pool, ensure_ascii=False)}",
     f"- **Counted here:** {N:,} posts from {len(per_reader)} readers that pass the check, out of {len(sample):,} in this sample ({len(shares)} shares made). Dates: " + ", ".join(f"{m} {n:,}" for m, n in sorted(months.items())) + ".",
     f"- **Readers left out** (share made, check not passed or not finished): {', '.join(failed) or 'none'}.",
     "- **A count is a number of posts**, each tagged by one reader against the pattern list. A post is not a person, and Reddit is not the market.",
     "- **Per-pattern counts are soft.** In the first round, three coders agreed on the main pattern for 21 of 30 shared posts. Small differences between patterns mean nothing.",
     f"- **Replies:** see `{d}/posts-without-replies.txt` for the posts that were read without the poster's own replies.",
     f"- **Quotes:** {nq:,}, each checked word for word against its post. They are in `pattern-NN.md`, under the post they come from.", ""]
L += ["## Marks", ""] + table(["Mark", "Posts", "Share"], [(m, sum(1 for r in R if r["mark"] == m), pc(sum(1 for r in R if r["mark"] == m), N)) for m in ("yes", "near", "no")])
rates = sorted(100 * c["yes"] / sum(c.values()) for c in per_reader.values())
if rates: L += [f"Yes rate per reader: lowest {rates[0]:.1f}%, middle {rates[len(rates)//2]:.1f}%, highest {rates[-1]:.1f}%. Readers differ in where they draw the line.", ""]
L += ["## On-niche posts (yes) by pattern", "", "Main = the one pattern the post is mostly about (sums to all yes posts). Any = the post shows it at all.", ""]
main = collections.Counter(int(r["main_pattern"]) for r in yes); anyp = collections.Counter(p for r in yes for p in set(pats(r)))
ntm = collections.Counter(int(r["main_pattern"]) for r in tied)
L += table(["#", "Pattern", "Main", "Share of yes", "Share of all posts", "Any", "Near posts tied to development (main)"],
           [(p, names.get(p, "?"), main[p], pc(main[p], len(yes)), pc(main[p], N), anyp[p], ntm[p]) for p in sorted(range(top + 1), key=lambda p: -main[p])])
L += [f"Near posts tied to development: {len(tied):,} of {len(near):,} near posts.", ""]
L += ["## Near posts by border", ""] + table(["Border", "Posts", "Share of near"], tally(near, lambda r: r["border"]))
L += ["## Yes posts by child's stage", ""] + table(["Stage", "Posts", "Share"], tally(yes, lambda r: r["stage"]))
L += ["## Yes posts by speaker", "", "`parent_unspecified` means the author did not say they are a mother.", ""] + table(["Speaker", "Posts", "Share"], tally(yes, lambda r: r["speaker"]))
L += ["## By subreddit", ""] + table(["Subreddit", "Posts read", "Yes", "Yes share", "Near"], sorted(((s, n, sum(1 for r in yes if r["subreddit"] == s), pc(sum(1 for r in yes if r["subreddit"] == s), n), sum(1 for r in near if r["subreddit"] == s)) for s, n in collections.Counter(r["subreddit"] for r in R).items()), key=lambda x: -x[2]))
paid = [r for r in yes if r["paid"] == "yes"]; paidn = [r for r in near if r["paid"] == "yes"]
L += ["## Paying", "", f"- Yes posts where the author says they paid for something about it: {len(paid):,} of {len(yes):,} ({pc(len(paid), len(yes))}).", f"- Near posts: {len(paidn):,} of {len(near):,}.", "", "Every yes post that mentions paying:", ""]
L += table(["Post", "Main pattern", "Paid for"], [(r["post_id"], r["main_pattern"], r["paid_what"]) for r in sorted(paid, key=lambda r: int(r["main_pattern"]))])
other = [r for r in yes if r["main_pattern"] == "0"]
L += ["## Yes posts that fit no pattern (all of them)", "", "This is where a missing pattern would show.", ""] + table(["Post", "What it is about", "Reader's one line"], [(r["post_id"], r["other_what"], r["about"]) for r in other])
L += ["## Files", "", "- `posts.tsv`: every counted post, one row, with subreddit, date and reader.", "- `pattern-NN.md`: the yes posts whose main pattern is NN, then the near posts tied to development, each with its quotes."]
open(f"{out}/counts.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
for p in range(top + 1):
    P = [f"# Pattern {p}: {names.get(p, '?')}", "", f"{niche}, {label} ({rnd}). Every post whose main pattern is {p}, with every quote the reader pulled from it. Nothing selected.", ""]
    for title, rs in (("On-niche posts (yes)", yes), ("Near posts tied to development", tied)):
        rs = sorted((r for r in rs if int(r["main_pattern"]) == p), key=lambda r: (r["date"], r["post_id"]))
        P += [f"## {title}: {len(rs):,} posts", ""]
        for r in rs:
            extra = f" | border: {r['border']}" if r["border"] else ""
            P += [f"### {r['post_id']} | r/{r['subreddit']} | {r['date']} | {r['stage']} | {r['speaker']} | patterns {r['patterns']}{extra}", "",
                  f"About: {r['about']}. Wants: {r['wants'] or '-'}. Already did: {r['already_did'] or '-'}." + (f" Paid: {r['paid_what']}." if r["paid"] == "yes" else ""), ""]
            P += [f"- `{q['id']}` ({q['type']}) {q['quote']}" for q in quotes[r["post_id"]]] + [""]
    open(f"{out}/pattern-{p:02d}.md", "w", encoding="utf-8").write("\n".join(P) + "\n")
print(f"COUNTED {N} posts, {len(yes)} yes, {len(near)} near, {nq} quotes, readers left out: {failed or 'none'} -> {out}/")
