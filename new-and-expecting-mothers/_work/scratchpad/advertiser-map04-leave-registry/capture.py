from pathlib import Path
import requests,json,hashlib,sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime,timezone
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];W=R/'_raw/advertiser-map04-leave-registry'
specs=[('mymatleave','https://mymatleave.com/'),('mybumppay','https://mybumppay.com/'),('nugget','https://www.nuggetsavings.com/'),('nugget-membership','https://www.nuggetsavings.com/membership-2'),('mindful-course','https://www.mindfulreturn.com/e-course/'),('parentaly','https://www.parentaly.com/'),('parentaly-coaching','https://www.parentaly.com/join/coaching-program/parentaly-coaching-program'),('cocoon-pricing','https://www.cocoon.com/go/pricing'),('sparrow-faq','https://sparrow.com/faq/'),('tilt-pricing','https://hellotilt.com/pricing/'),('babylist','https://www.babylist.com/'),('myregistry','https://www.myregistry.com/'),('goodbuygear','https://goodbuygear.com/'),('safeintheseat','https://www.safeintheseat.com/'),('sits-course-store','https://courses.safeintheseat.com/store'),('starterset','https://thestarterset.com/'),('mastermaternity','https://mastermaternityleave.com/')]
def fetch(spec):
 slug,url=spec;p=W/'pages'/(slug+'.html');assert not p.exists()
 try:
  r=requests.get(url,timeout=25);p.write_bytes(r.content);p.with_suffix('.headers.json').write_text(json.dumps(dict(headers=dict(r.headers),history=[dict(url=z.url,status=z.status_code,headers=dict(z.headers)) for z in r.history]),indent=2)+'\n')
  s=BeautifulSoup(r.content,'html.parser')
  for n in s(['script','style','noscript']):n.decompose()
  text=s.get_text('\n',strip=True)+'\n';p.with_suffix('.txt').write_text(text)
  links=[dict(text=a.get_text(' ',strip=True),url=a.get('href')) for a in s.find_all('a',href=True)]
  p.with_suffix('.links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n')
  return dict(slug=slug,url=url,final_url=r.url,status=r.status_code,captured_utc=datetime.now(timezone.utc).isoformat(),html_file=str(p.relative_to(R)),html_sha256=hashlib.sha256(r.content).hexdigest(),text_file=str(p.with_suffix('.txt').relative_to(R)),text_sha256=hashlib.sha256(text.encode()).hexdigest(),text_chars=len(text),bytes=len(r.content),facebook_links=[a for a in links if 'facebook.com/' in a['url'] or 'fb.com/' in a['url']])
 except requests.RequestException as e:return dict(slug=slug,url=url,error=str(e))
rows=list(ThreadPoolExecutor(4).map(fetch,specs));(W/'access.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
for x in rows:print(json.dumps(x))
