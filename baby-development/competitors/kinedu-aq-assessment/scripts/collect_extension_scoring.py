#!/usr/bin/env python3
"""Post-extension scoring grid. For each age 0-41: base Yes count Kb from capped_from..N (ascending-rate order of the served list),
plus the 8 first-batch extension items with Ke = 0..8 Yes (ascending rate). POST extended:true. Via scripts/proxy_curl.sh, 2 s pacing,
resumable, aborts after 3 consecutive blocking responses."""
import json, glob, os, subprocess, time, sys, csv, hashlib
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
by = {}
for f in glob.glob(os.path.join(root, 'raw/api/start_age*_gw-null.json')):
    d = json.load(open(f))
    if isinstance(d, dict) and 'sections' in d: by.setdefault(d['ageMonths'], d)
def served(d):
    items = []
    for s in d['sections']:
        if s.get('anchor'): items.append(s['anchor'])
        items += s['items']
    items += d['calibration']
    return sorted(items, key=lambda i: (i['rate'], i['id']))
cap = {}
for r in csv.DictReader(open(os.path.join(root, 'scoring-table.csv'))):
    if r['capped'].lower() == 'true':
        a, k = int(r['age']), int(r['K']); cap[a] = min(cap.get(a, 999), k)
out = os.path.join(root, 'raw/api/extension-scoring'); man = os.path.join(out, 'requests.jsonl')
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
plan = []
for age in range(42):
    ext = json.load(open(os.path.join(root, f'raw/api/result_age{age:02d}_all_yes_numeric.json')))
    assert ext['stage'] == 'extension'
    eitems = sorted(ext['items'], key=lambda i: (i['rate'], i['id']))
    base = served(by[age])
    for Kb in range(cap[age], len(base) + 1):
        for Ke in range(0, len(eitems) + 1):
            plan.append((age, Kb, Ke, base, eitems))
print('planned', len(plan), flush=True)
blocking = 0; done = 0
for age, Kb, Ke, base, eitems in plan:
    path = os.path.join(out, f'result_age{age:02d}_kb{Kb:02d}_ke{Ke}.json')
    if os.path.exists(path): continue
    answers = [{"id": it['id'], "y": 1 if i < Kb else 0} for i, it in enumerate(base)] + [{"id": it['id'], "y": 1 if i < Ke else 0} for i, it in enumerate(eitems)]
    body = json.dumps({"action": "result", "ageMonths": age, "extended": True, "answers": answers})
    time.sleep(2.0)
    r = subprocess.run([os.path.join(root, 'scripts/proxy_curl.sh'), '-s', '--max-time', '60', '-X', 'POST', 'https://webpromo.kinedu.com/api/assessment',
        '-A', UA, '-H', 'Content-Type: application/json', '-H', 'Origin: https://webpromo.kinedu.com', '-H', 'Referer: https://webpromo.kinedu.com/aq-assessment',
        '--data-raw', body, '-o', path, '-w', '%{http_code}'], capture_output=True, text=True)
    code = r.stdout.strip()
    ok = code == '200'
    blocking = 0 if ok else blocking + 1
    try: d = json.load(open(path)); b = d.get('basic', {})
    except Exception: d = {}; b = {}
    rec = {"ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), "age": age, "Kb": Kb, "Ke": Ke, "http": code, "stage": d.get('stage'), "state": b.get('state'), "devAge": b.get('devAge'), "band": b.get('band'), "capped": b.get('capped'), "file": os.path.relpath(path, root), "sha256": hashlib.sha256(open(path, 'rb').read()).hexdigest() if os.path.exists(path) else None}
    open(man, 'a').write(json.dumps(rec) + "\n"); done += 1
    if done % 25 == 0: print(json.dumps({"done": done, "age": age, "Kb": Kb, "Ke": Ke, "http": code}), flush=True)
    if blocking >= 3:
        print(json.dumps({"status": "BLOCKED", "last_http": code, "age": age}), flush=True); sys.exit(2)
print(json.dumps({"status": "FINISHED", "requests": done}), flush=True)
