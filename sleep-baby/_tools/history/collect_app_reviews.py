#!/usr/bin/env python3
"""Save permitted public App Store review HTML and freeze its visible review units (sleep-baby, RV1).

Copied from global/_tools/collect_app_reviews.py on 2026-10-25 and adapted: sleep-baby app list,
per-app storefronts (Huckleberry and Napper ca+au only: us+gb already in global/), id-only URL route.
Only public app pages are fetched. No Apple API/RSS endpoints (robots-disallowed).
Apple selects the reviews; this is not its complete archive. Never overwrites a capture or corpus.
"""
from pathlib import Path
import concurrent.futures, subprocess, json, re

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / '_raw/reviews'
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
ALL = ['us', 'gb', 'ca', 'au']
APPS = {
 'huckleberry': ('1169136078', ['ca', 'au']),
 'napper': ('1491340863', ['ca', 'au']),
 'nara': ('1444639029', ALL),
 'glowbaby': ('1077177456', ALL),
 'smartsleepcoach': ('1616824897', ALL),
 'littleones': ('1382444112', ALL),
 'happybaby': ('6450744756', ALL),
}

def collect(task):
 app, country = task
 aid, _ = APPS[app]
 url = f'https://apps.apple.com/{country}/app/id{aid}?see-all=reviews'
 path = RAW/f'{app}-{country}-reviews.html'
 if not path.exists():
  r = subprocess.run(['curl','-sS','-L','-A',UA,'--max-time','30','-D',str(path.with_suffix('.headers.txt')),'-o',str(path),'-w','%{http_code}',url],capture_output=True,text=True)
  status = r.stdout.strip()
 else:
  status = '200_existing_capture'
 source = path.read_text(errors='replace') if path.exists() else ''
 m = re.search(r'<script[^>]*id="serialized-server-data"[^>]*>(.*?)</script>', source, re.S)
 reviews = []
 if m:
  data = json.loads(m.group(1))
  for page in data.get('data', []):
   shelf = page.get('data', {}).get('shelfMapping', {}).get('allProductReviews', {})
   for item in shelf.get('items', []):
    q = item.get('review', {})
    if q.get('$kind') == 'Review':
     reviews.append({k: q.get(k) for k in ['id','title','contents','rating','date']})
 corpus = RAW/f'{app}-{country}-corpus.txt'
 if corpus.exists():
  raise RuntimeError('Refusing to overwrite frozen corpus '+str(corpus))
 with corpus.open('w') as f:
  for q in reviews:
   f.write(f"REVIEW {app}-{country}-{q['id']} | {q['rating']} stars | {q['date']}\nTITLE: {q['title']}\n{q['contents']}\n\n")
 meta = {'app':app,'country':country,'url':url,'http_status':status,'raw_file':str(path.relative_to(ROOT)),'corpus_file':str(corpus.relative_to(ROOT)),'reviews':reviews}
 path.with_suffix('.units.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2))
 return {k: meta[k] for k in ['app','country','url','http_status','raw_file','corpus_file']} | {'review_count': len(reviews)}

if __name__ == '__main__':
 RAW.mkdir(exist_ok=True, parents=True)
 jobs = [(a, c) for a in APPS for c in APPS[a][1]]
 records = []
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
  for r in ex.map(collect, jobs):
   records.append(r); print(r['app'], r['country'], r['http_status'], r['review_count'], flush=True)
 (RAW/'appstore-collection-manifest-rv1.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
