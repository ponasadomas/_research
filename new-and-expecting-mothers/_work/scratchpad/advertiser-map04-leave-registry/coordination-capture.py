from pathlib import Path
import requests,json,hashlib,sys
from datetime import datetime,timezone
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).resolve().parents[2];W=R/'_raw/advertiser-map04-leave-registry'
specs=[('ohai-how','https://www.ohai.ai/how-it-works/'),('maple','https://www.growmaple.com/'),('familywall-premium','https://www.familywall.com/premium.html?lang=en'),('cozi-plans','https://www.cozi.com/compare-plans/'),('skylight','https://myskylight.com/')]
def capture(spec):
 slug,url=spec;p=W/'pages'/(slug+'.html');assert not p.exists()
 try:
  r=requests.get(url,timeout=25);p.write_bytes(r.content);p.with_suffix('.headers.json').write_text(json.dumps(dict(headers=dict(r.headers),history=[dict(url=z.url,status=z.status_code,headers=dict(z.headers)) for z in r.history]),indent=2)+'\n');s=BeautifulSoup(r.content,'html.parser')
  for n in s(['script','style','noscript']):n.decompose()
  txt=s.get_text('\n',strip=True)+'\n';p.with_suffix('.txt').write_text(txt)
  links=[dict(text=a.get_text(' ',strip=True),url=a['href']) for a in s.find_all('a',href=True)];p.with_suffix('.links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n')
  return dict(slug=slug,url=url,final_url=r.url,status=r.status_code,captured_utc=datetime.now(timezone.utc).isoformat(),html_file=str(p.relative_to(R)),html_sha256=hashlib.sha256(r.content).hexdigest(),text_file=str(p.with_suffix('.txt').relative_to(R)),text_sha256=hashlib.sha256(txt.encode()).hexdigest(),text_chars=len(txt),bytes=len(r.content),facebook_links=[a for a in links if 'facebook.com/' in a['url']])
 except requests.RequestException as e:return dict(slug=slug,url=url,error=str(e))
rows=list(ThreadPoolExecutor(4).map(capture,specs))
with (W/'access.jsonl').open('a') as f:
 for x in rows:f.write(json.dumps(x)+'\n')
for x in rows:print(json.dumps(x))
