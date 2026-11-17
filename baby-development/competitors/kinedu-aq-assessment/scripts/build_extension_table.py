#!/usr/bin/env python3
"""Build extension-table.csv and EXTENSION-TABLE.md from raw/api/extension-scoring/ (offline)."""
import json, os, glob, csv, collections, re
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for f in sorted(glob.glob(os.path.join(root, 'raw/api/extension-scoring/result_age*_kb*_ke*.json'))):
    m = re.search(r'age(\d+)_kb(\d+)_ke(\d+)', f); age, kb, ke = map(int, m.groups())
    try: d = json.load(open(f))
    except Exception: continue
    b = d.get('basic') or {}; areas = {a['area']: a for a in (d.get('detail') or {}).get('areas', [])}
    rows.append(dict(age=age, Kb=kb, Ke=ke, K_total=kb + ke, stage=d.get('stage'), state=b.get('state'), devAge=b.get('devAge'), band=b.get('band'), capped=b.get('capped'),
        **{f'months_{k.replace("-", "")}': areas.get(k, {}).get('months') for k in ['Physical', 'Cognitive', 'Language', 'Social-Emotional']}, file=os.path.relpath(f, root)))
rows.sort(key=lambda r: (r['age'], r['Kb'], r['Ke']))
with open(os.path.join(root, 'extension-table.csv'), 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
by = collections.defaultdict(dict)
for r in rows: by[r['age']][(r['Kb'], r['Ke'])] = r
# checks
band_ok = band_bad = 0; nonmono = []; only_total = 0; total_conflicts = []
for age, g in by.items():
    for (kb, ke), r in g.items():
        if r['devAge'] is None: continue
        rr = r['devAge'] / max(age, 1); pred = 'well_ahead' if rr > 1.15 else 'little_ahead' if rr > 1.05 else 'on_pace' if rr >= 0.95 else 'building'
        band_ok += pred == r['band']; band_bad += pred != r['band']
        if (kb, ke + 1) in g and g[(kb, ke + 1)]['devAge'] is not None and g[(kb, ke + 1)]['devAge'] < r['devAge']: nonmono.append((age, kb, ke, r['devAge'], g[(kb, ke + 1)]['devAge']))
    bt = collections.defaultdict(set)
    for (kb, ke), r in g.items(): bt[kb + ke].add((r['devAge'], r['capped']))
    for t, s in bt.items():
        if len(s) > 1: total_conflicts.append((age, t, sorted(s, key=str)))
L = ["# Post-extension scoring table (Phase 8)", "", f"{len(rows)} reports, ages 0–41. Base list answered with Kb Yes (ascending rate; Kb from the capped-from count to N), plus the 8 first-batch extension items with Ke Yes (ascending rate), sent with extended:true. Raw: raw/api/extension-scoring/, manifest requests.jsonl, CSV extension-table.csv.", "",
     f"Band formula check (devAge/age thresholds 1.15 / 1.05 / 0.95): {band_ok} match, {band_bad} mismatch.", "",
     f"Does the result depend only on the total Yes count (Kb+Ke)? Conflicts found at (age, total): {len(total_conflicts)}" + (" — none, so total count is sufficient." if not total_conflicts else ""), ""]
if total_conflicts: L += ["| Age | Kb+Ke | distinct (devAge, capped) |", "|---|---|---|"] + [f"| {a} | {t} | {s} |" for a, t, s in total_conflicts[:60]] + [""]
L += [f"Decreases of devAge when one more extension Yes is added: {len(nonmono)}", ""]
if nonmono: L += ["| Age | Kb | Ke → Ke+1 | devAge before → after |", "|---|---|---|---|"] + [f"| {a} | {kb} | {ke} → {ke+1} | {d1} → {d2} |" for a, kb, ke, d1, d2 in nonmono[:80]] + [""]
L += ["## Per age: final devAge by base Yes (rows) and extension Yes (columns)", ""]
for age in sorted(by):
    g = by[age]; kbs = sorted({k[0] for k in g}); kes = sorted({k[1] for k in g})
    L += [f"### Age {age}", "", "| Kb \\ Ke | " + " | ".join(map(str, kes)) + " |", "|---|" + "---|" * len(kes)]
    for kb in kbs:
        cells = []
        for ke in kes:
            r = g.get((kb, ke)); cells.append('—' if not r else ('floor' if r['devAge'] is None else f"{r['devAge']}{'+' if r['capped'] else ''}"))
        L.append(f"| {kb} | " + " | ".join(cells) + " |")
    L.append("")
open(os.path.join(root, 'EXTENSION-TABLE.md'), 'w').write("\n".join(L))
print('rows', len(rows), 'band', band_ok, band_bad, 'total-count conflicts', len(total_conflicts), 'nonmono', len(nonmono))
