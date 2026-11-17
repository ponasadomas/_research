#!/usr/bin/env python3
"""Render questions-by-age.md from saved start responses (offline, no network)."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
by_age = {}
for f in sorted(glob.glob(os.path.join(root, 'raw/api/start_age*_gw-null.json'))):
    d = json.load(open(f))
    if isinstance(d, dict) and 'ageMonths' in d and 'sections' in d:
        by_age.setdefault(d['ageMonths'], (d, os.path.relpath(f, root)))
out = ["# Questions by age (as served by the API, in on-screen order)", "",
       "Indexed by the API's returned `ageMonths`. Each line: `id · rate · text` where rate = share of babies "
       "of that age reported to already do it. `anchor` is shown first in a section, then items, then the "
       "calibration item displayed after that section (its area can differ). Source file linked per age.", ""]
for age in sorted(by_age):
    d, src = by_age[age]
    cal = d.get('calibration') or []
    n = sum(len(s['items']) + (1 if s.get('anchor') else 0) for s in d['sections']) + len(cal)
    out.append(f"## {age} months — {n} questions ([{src}]({src}))"); out.append("")
    for i, s in enumerate(d['sections']):
        out.append(f"### {s['area']}")
        if s.get('anchor'):
            a = s['anchor']; out.append(f"- **anchor** {a['id']} · {a['rate']} · {a['title']}")
        for it in s['items']:
            out.append(f"- {it['id']} · {it['rate']} · {it['title']}")
        if i < len(cal):
            c = cal[i]; out.append(f"- *calibration ({c['area']})* {c['id']} · {c['rate']} · {c['title']}")
        out.append("")
open(os.path.join(root, 'questions-by-age.md'), 'w').write("\n".join(out))
print("ages:", len(by_age), "->", 'questions-by-age.md')
