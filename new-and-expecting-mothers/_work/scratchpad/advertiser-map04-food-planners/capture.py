from pathlib import Path
from urllib.parse import urlsplit,urljoin
from urllib.robotparser import RobotFileParser
import urllib.request,urllib.error,json,hashlib,datetime,re,sys,concurrent.futures
from html.parser import HTMLParser
R=Path(__file__).resolve().parents[2];W=R/'_raw/advertiser-map04-food-planners';W.mkdir(exist_ok=True);(W/'robots').mkdir(exist_ok=True);(W/'pages').mkdir(exist_ok=True)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.out=[];self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t in ['script','style','noscript','svg']:self.skip+=1
  if t=='a' and d.get('href'):self.links.append(d['href'])
  if t in ['p','div','h1','h2','h3','h4','li','section','br','tr']:self.out.append('\n')
 def handle_endtag(self,t):
  if t in ['script','style','noscript','svg'] and self.skip:self.skip-=1
  if t in ['p','div','h1','h2','h3','h4','li','section','tr']:self.out.append('\n')
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
def request(url):
 req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; research-access-check/1.0)'})
 try:
  with urllib.request.urlopen(req,timeout=35) as r:return dict(status=r.status,final_url=r.url,headers=dict(r.headers),body=r.read())
 except urllib.error.HTTPError as e:return dict(status=e.code,final_url=e.url,headers=dict(e.headers),body=e.read())
 except Exception as e:return dict(status=None,final_url=url,headers={},body=b'',error=str(e))
def fetch(slug,url):
 host=urlsplit(url).netloc;rp=W/'robots'/f'{host}.txt';rm=rp.with_suffix('.json')
 if not rp.exists():
  z=request(urljoin(url,'/robots.txt'));rp.write_bytes(z.pop('body'));rm.write_text(json.dumps(dict(url=urljoin(url,'/robots.txt'),**z),indent=2)+'\n')
 z=json.loads(rm.read_text());policy=RobotFileParser();policy.set_url(urljoin(url,'/robots.txt'));policy.parse(rp.read_text(errors='replace').splitlines());permitted=z['status']==404 or z['status']==200 and policy.can_fetch('*',url)
 if not permitted:return dict(slug=slug,url=url,robots_status=z['status'],robots_allowed=False,result='not_requested_due_to_explicit_disallow_or_unresolved_policy',robots_file=str(rp.relative_to(R)))
 p=W/'pages'/f'{slug}.html';assert not p.exists(),slug;x=request(url);p.write_bytes(x.pop('body'));raw=p.read_text(errors='replace');t=Text();t.feed(raw);txt=re.sub(r'[ \t\r\f\v]+',' ',''.join(t.out));txt=re.sub(r'\n\s*\n+','\n\n',txt).strip();p.with_suffix('.txt').write_text(txt+'\n');links=sorted(set(urljoin(x['final_url'],h) for h in t.links));p.with_suffix('.links.json').write_text(json.dumps(links,indent=2)+'\n');o=dict(slug=slug,url=url,robots_status=z['status'],robots_allowed=True,robots_file=str(rp.relative_to(R)),raw_file=str(p.relative_to(R)),text_file=str(p.with_suffix('.txt').relative_to(R)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),**x);p.with_suffix('.meta.json').write_text(json.dumps(o,indent=2)+'\n');return o
if __name__=='__main__':
 jobs=json.loads(Path(sys.argv[1]).read_text())
 # Different host jobs may run concurrently; same host follow-up pages run only in separate calls.
 with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:
  for o in ex.map(lambda x:fetch(x[0],x[1]),jobs):
   with (W/'access.jsonl').open('a') as f:f.write(json.dumps(o)+'\n')
   print(json.dumps({k:o.get(k) for k in ['slug','url','robots_status','robots_allowed','status','bytes','result','error']}),flush=True)
