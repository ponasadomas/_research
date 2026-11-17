#!/usr/bin/env python3
"""For ages 0-41: send extended:false at K = capped_from and capped_from-1 (ascending-rate order) via scripts/proxy_curl.sh.
Records whether stage == 'extension'. Resumable; 2 s pacing."""
import json, glob, os, subprocess, time, sys, hashlib
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
plan = json.load(open(sys.argv[1]))
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
out = os.path.join(root, 'raw/api/extension-probe'); man = os.path.join(out, 'requests.jsonl')
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
for age in range(42):
    cap = plan[str(age)]; items = served(by[age])
    for K in (cap - 1, cap):
        path = os.path.join(out, f'result_age{age:02d}_k{K:02d}_extfalse.json')
        if os.path.exists(path): continue
        answers = [{"id": it['id'], "y": 1 if i < K else 0} for i, it in enumerate(items)]
        body = json.dumps({"action": "result", "ageMonths": age, "extended": False, "answers": answers})
        time.sleep(2.0)
        r = subprocess.run([os.path.join(root, 'scripts/proxy_curl.sh'), '-s', '--max-time', '60', '-X', 'POST',
            'https://webpromo.kinedu.com/api/assessment', '-A', UA, '-H', 'Content-Type: application/json',
            '-H', 'Origin: https://webpromo.kinedu.com', '-H', 'Referer: https://webpromo.kinedu.com/aq-assessment',
            '--data-raw', body, '-o', path, '-w', '%{http_code}'], capture_output=True, text=True)
        code = r.stdout.strip()
        try: stage = json.load(open(path)).get('stage')
        except Exception: stage = None
        rec = {"ts": time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), "age": age, "K": K, "N": len(items), "http": code, "stage": stage, "file": os.path.relpath(path, root)}
        open(man, 'a').write(json.dumps(rec) + "\n"); print(rec, flush=True)
