#!/usr/bin/env python3
"""Check that a brief carries its niche's definition, and that the owner has confirmed it.
  python3 -I _tools/check_definition.py <niche> <brief.md>...
The definition is in ~/GitHub/_home/library/niches.md under "## Definitions", "### `<niche>`".
Every line of it except "Confirmed by the owner" must stand word for word in each brief,
and the "Confirmed by the owner" line must begin with a date (yyyy-mm-dd)."""
import os, re, sys
niche, briefs = sys.argv[1], sys.argv[2:]
t = open(os.path.expanduser("~/GitHub/_home/library/niches.md"), encoding="utf-8").read()
m = re.search(r"^### `" + re.escape(niche) + r"`\n(.*?)(?=^### |\Z)", t.split("## Definitions", 1)[-1], flags=re.M | re.S)
if not m: sys.exit(f"FAIL: no definition of {niche} in library/niches.md")
lines = dict(re.findall(r"^- \*\*(.+?):\*\* (.+)$", m.group(1), flags=re.M)); problems = []
conf = lines.pop("Confirmed by the owner", "")
if not re.match(r"\d{4}-\d{2}-\d{2}", conf): problems.append("the owner has not confirmed the definition (library/niches.md)")
norm = lambda s: re.sub(r"\s+", " ", s).strip()
for b in briefs:
    text = norm(open(b, encoding="utf-8").read())
    problems += [f'{b}: the "{k}" line is not in it word for word' for k, v in lines.items() if norm(v) not in text]
print(f"definition of {niche}: " + ("OK" if not problems else "FAIL")); [print("  " + p) for p in problems]
sys.exit(1 if problems else 0)
