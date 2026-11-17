#!/usr/bin/env python3
"""Group a build's unfilter reader files into digest shares of about N quotes and write briefs.
python3 -I unfilter_assign_digests.py <niche> [quotes-per-share=1200]"""
import glob, math, os, sys
niche = sys.argv[1]; per = int(sys.argv[2]) if len(sys.argv) > 2 else 1200
T = os.path.dirname(os.path.abspath(__file__)); R = os.path.normpath(os.path.join(T, "..", "..", niche))
D = os.path.join(R, "scratchpad", "unfilter-reread")
files = sorted(glob.glob(os.path.join(R, "voice", "reddit-ur*.jsonl")))
counts = [(f, sum(1 for l in open(f) if l.strip())) for f in files]
total = sum(c for _, c in counts); n = max(1, round(total / per))
shares = [[] for _ in range(n)]; sizes = [0] * n
for f, c in sorted(counts, key=lambda x: -x[1]):          # largest first into the emptiest share
    k = sizes.index(min(sizes)); shares[k].append((f, c)); sizes[k] += c
tpl = open(os.path.join(T, os.environ.get("DIGEST_BRIEF", "brief-unfilter-digest.md"))).read()
for k, sh in enumerate(shares, 1):
    nn = f"{k:02d}"; sh.sort()
    lines = []
    for f, c in sh:
        ur = os.path.basename(f)[len("reddit-"):-len(".jsonl")]
        lines.append(f"- `voice/reddit-{ur}.jsonl` ({c} quotes) and its ledger `sources/reddit-reading-{ur}.md`")
    open(os.path.join(D, f"digest-{nn}.files"), "w").write("\n".join(os.path.relpath(f, R) for f, _ in sh) + "\n")
    b = (tpl.replace("{NICHE}", niche).replace("{NN}", nn).replace("{N}", str(n))
            .replace("{FILES}", "\n".join(lines)).replace("{COUNT}", str(sum(c for _, c in sh))))
    open(os.path.join(D, f"brief-digest-{nn}.md"), "w").write(b)
print(f"{niche}: {total} new quotes, {n} digest shares, sizes {sizes}")
