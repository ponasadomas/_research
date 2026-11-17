import requests,json,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[2];W=R/'_raw/advertiser-map04-leave-registry'
hosts=['mymatleave.com','www.nuggetsavings.com','www.mindfulreturn.com','www.parentaly.com','www.cocoon.com','sparrow.com','hellotilt.com','www.babylist.com','www.myregistry.com','goodbuygear.com','strolleria.com','www.safeintheseat.com','shop.safeintheseat.com','courses.safeintheseat.com','thestarterset.com','mastermaternityleave.com']
def fetch(host):
 p=W/'policies'/(host+'.txt');assert not p.exists();url='https://'+host+'/robots.txt'
 try:
  r=requests.get(url,timeout=20);p.write_bytes(r.content);p.with_suffix('.headers.json').write_text(json.dumps(dict(headers=dict(r.headers),redirects=[dict(url=x.url,status=x.status_code,headers=dict(x.headers)) for x in r.history]),indent=2)+'\n');return dict(host=host,url=url,final_url=r.url,status=r.status_code,raw_file=str(p.relative_to(R)),bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest())
 except requests.RequestException as e:return dict(host=host,url=url,error=str(e))
rows=list(ThreadPoolExecutor(4).map(fetch,hosts));(W/'policy-access.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
for x in rows:
 print(json.dumps(x))
 if 'raw_file' in x:print((R/x['raw_file']).read_text(errors='replace'))
