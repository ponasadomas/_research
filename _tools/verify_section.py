#!/usr/bin/env python3
"""Check the counts of a findings section merged from digests.
  python3 -I _tools/verify_section.py <section.md> <yes posts> <near posts> [most words above Coverage, default 2500]
The count lines under "## On-niche posts" must be "N of <yes> posts." and sum to <yes>;
those under "## Near posts" likewise for <near>; "## Across the on-niche posts" must hold
four findings counted out of <yes>; the page above "## Coverage" must be 2,500 words at most."""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read(); yes, near = int(sys.argv[2]), int(sys.argv[3]); problems = []
most = int(sys.argv[4]) if len(sys.argv) > 4 else 2500
parts = re.split(r"^## (.*)$", t, flags=re.M); sec = {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
def counts(name):
    if name not in sec: problems.append(f'no "## {name}" section'); return []
    out = []
    for b in re.split(r"^### ", sec[name], flags=re.M)[1:]:
        m = re.search(r"^(\d[\d,]*) of (\d[\d,]*) posts\.", b, re.M)
        if not m: problems.append(f'"{b.splitlines()[0][:50]}": no count line'); continue
        out.append(tuple(int(x.replace(",", "")) for x in m.groups()))
    return out
for name, total in (("On-niche posts", yes), ("Near posts", near)):
    c = counts(name)
    if any(m != total for _, m in c): problems.append(f"{name}: a count is not out of {total}")
    if sum(n for n, _ in c) != total: problems.append(f"{name}: counts sum to {sum(n for n, _ in c)}, not {total}")
c = counts("Across the on-niche posts")
if len(c) != 4: problems.append(f"Across the on-niche posts: {len(c)} findings, not 4")
if any(m != yes or n > yes for n, m in c): problems.append("Across the on-niche posts: a count is not out of the yes posts")
words = len(t.split("## Coverage")[0].split())
if words > most: problems.append(f"{words} words above Coverage, more than {most:,}")
print(f"{sys.argv[1].split('/')[-1]}: counts " + ("OK" if not problems else "FAIL")); [print("  " + p) for p in problems]
sys.exit(1 if problems else 0)
