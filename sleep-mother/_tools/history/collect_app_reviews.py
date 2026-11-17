#!/usr/bin/env python3
"""(sleep-mother copy, RV1 2026-10-25: copied from toddler-behaviour/_tools; apps and per-app storefronts adapted.)
Save permitted public App Store review HTML and freeze its visible review units.

Only public app pages are fetched. No Apple API/RSS endpoints: those are disallowed
by the saved robots.txt. Apple selects the reviews; this is not its complete archive.
Never overwrite a capture or corpus after quotation. Run once, then inspect corpus.
"""
from pathlib import Path
import concurrent.futures, subprocess, json, re, sys

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / '_raw/reviews'
APPS = {
 'sleepio3': ('6698893964','sleepio-3-0'),            # Sleepio 3.0 (us/ca/au; gb 404)
 'sleepiouk': ('1538191784','sleepio-insomnia-treatment'),  # Sleepio NHS/UK listing (gb)
 'stellarsleep': ('1602312365','stellar-sleep-insomnia-cbt'),
 'bettersleep': ('314498713','-'),
 'calm': ('571800810','-'),
 'headspace': ('493145008','-'),
 'slumber': ('1109543953','slumber-calm-stories-for-sleep'),
 'rise': ('1453884781','-'),
 'blissful': ('6739263953','blissful-self-care-for-moms'),  # self-care app for moms with sleep audio
}
STOREFRONTS = {'sleepio3': ['us','ca','au'], 'sleepiouk': ['gb','ca','au']}

def collect(task):
 app, country = task
 aid, slug = APPS[app]
 url = f'https://apps.apple.com/{country}/app/{slug}/id{aid}?see-all=reviews'
 path = RAW/f'{app}-{country}-reviews.html'
 if not path.exists():
  r=subprocess.run(['curl','-sS','-L','--max-time','30','-D',str(path.with_suffix('.headers.txt')),'-o',str(path),'-w','%{http_code}',url],capture_output=True,text=True)
  status=r.stdout.strip()
 else:
  status='200_existing_capture'
 source=path.read_text(errors='replace') if path.exists() else ''
 m=re.search(r'<script[^>]*id="serialized-server-data"[^>]*>(.*?)</script>',source,re.S)
 reviews=[]
 if m:
  data=json.loads(m.group(1))
  for page in data.get('data',[]):
   shelf=page.get('data',{}).get('shelfMapping',{}).get('allProductReviews',{})
   for item in shelf.get('items',[]):
    q=item.get('review',{})
    if q.get('$kind')=='Review':
     reviews.append({k:q.get(k) for k in ['id','title','contents','rating','date']})
 corpus=RAW/f'{app}-{country}-corpus.txt'
 if corpus.exists():
  raise RuntimeError('Refusing to overwrite frozen corpus '+str(corpus))
 with corpus.open('w') as f:
  for q in reviews:
   f.write(f"REVIEW {app}-{country}-{q['id']} | {q['rating']} stars | {q['date']}\nTITLE: {q['title']}\n{q['contents']}\n\n")
 meta={'app':app,'country':country,'url':url,'http_status':status,'raw_file':str(path.relative_to(ROOT)),'corpus_file':str(corpus.relative_to(ROOT)),'reviews':reviews}
 path.with_suffix('.units.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
 return {k:meta[k] for k in ['app','country','url','http_status','raw_file','corpus_file']}|{'review_count':len(reviews)}

if __name__=='__main__':
 RAW.mkdir(exist_ok=True,parents=True)
 only=sys.argv[1:] or list(APPS)  # second run: pass app keys, never re-run captured ones
 jobs=[(a,c) for a in only for c in STOREFRONTS.get(a,['us','gb','ca','au'])]
 records=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
  for r in ex.map(collect,jobs):
   records.append(r); print(r['app'],r['country'],r['http_status'],r['review_count'],flush=True)
 (RAW/('appstore-collection-manifest'+('-'+'-'.join(sys.argv[1:]) if sys.argv[1:] else '')+'.json')).write_text(json.dumps(records,ensure_ascii=False,indent=2))
