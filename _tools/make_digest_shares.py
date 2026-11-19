#!/usr/bin/env python3
"""Cut an evidence folder's pattern-NN.md files into shares for digest readers.
  python3 -I _tools/make_digest_shares.py <evidence dir> <work dir> <most posts per share>
  (run from ~/GitHub/_research)
A pattern with more posts than the limit is dealt over several shares, every k-th post to
each, so each share spans the whole period. Writes <work dir>/share-NN.md and shares.tsv
(share, pattern number, pattern name, yes posts, near posts)."""
import glob, math, os, re, sys
ev, wd, most = sys.argv[1].rstrip("/"), sys.argv[2].rstrip("/"), int(sys.argv[3])
os.makedirs(wd, exist_ok=True); n = 0; index = ["share\tpattern\tname\tyes\tnear"]
for f in sorted(glob.glob(f"{ev}/pattern-*.md")):
    t = open(f, encoding="utf-8").read(); p = int(re.search(r"pattern-(\d+)", f).group(1))
    name = re.match(r"# Pattern \d+: (.*)", t).group(1).strip()
    secs = re.split(r"^## .*$", t, flags=re.M)[1:]
    posts = [["### " + b.rstrip() for b in re.split(r"^### ", s, flags=re.M)[1:]] for s in secs]
    k = max(1, math.ceil(sum(map(len, posts)) / most))
    for i in range(k):
        n += 1; y, nr = posts[0][i::k], posts[1][i::k]
        open(f"{wd}/share-{n:02d}.md", "w", encoding="utf-8").write(
            f"# Share {n:02d}: pattern {p}, {name}\n\n## On-niche posts (yes): {len(y)} posts\n\n" + "\n\n".join(y) +
            f"\n\n## Near posts tied to development: {len(nr)} posts\n\n" + "\n\n".join(nr) + "\n")
        index.append(f"{n:02d}\t{p}\t{name}\t{len(y)}\t{len(nr)}")
open(f"{wd}/shares.tsv", "w").write("\n".join(index) + "\n"); print("\n".join(index))
