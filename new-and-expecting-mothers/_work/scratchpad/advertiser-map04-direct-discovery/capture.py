import concurrent.futures,datetime,hashlib,json,re,sys,urllib.parse,urllib.robotparser
from pathlib import Path
import requests
from html.parser import HTMLParser
class Extract(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.text=[];self.links=[];self.link=None
 def handle_starttag(self,tag,attrs):
  if tag in {'script','style','noscript','svg'}:self.skip+=1
  if not self.skip and tag=='a':self.link={'text':'','url':dict(attrs).get('href','')}
 def handle_endtag(self,tag):
  if tag in {'script','style','noscript','svg'}:self.skip=max(0,self.skip-1)
  if tag=='a' and self.link:self.links.append(self.link);self.link=None
 def handle_data(self,data):
  if self.skip:return
  value=data.strip()
  if value:self.text.append(value)
  if self.link:self.link['text']+=data
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;W=R/'_raw/advertiser-map04-direct-discovery'
def sha(b):return hashlib.sha256(b).hexdigest()
def save(label,url):
 p=W/(label+'.body');assert not p.exists()
 try:
  r=requests.get(url,timeout=(25,45));p.write_bytes(r.content);meta={'requested_url':url,'final_url':r.url,'status':r.status_code,'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'headers':dict(r.headers),'redirects':[{'url':h.url,'status':h.status_code} for h in r.history],'raw_file':str(p.relative_to(R)),'sha256':sha(r.content),'bytes':len(r.content)}
 except Exception as e:
  meta={'requested_url':url,'error':str(e),'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()};(W/(label+'.error.txt')).write_text(str(e)+'\n')
 (W/(label+'.meta.json')).write_text(json.dumps(meta,indent=2)+'\n');return meta
def robots(domains):
 for domain in domains:
  label='robots-'+domain;meta=save(label,'https://'+domain+'/robots.txt');print(domain,meta.get('status',meta.get('error')))
def pages(specs):
 for slug,url in specs:
  domain=urllib.parse.urlsplit(url).netloc;mp=W/('robots-'+domain+'.meta.json');assert mp.exists();meta=json.loads(mp.read_text());allowed=meta.get('status')==200
  if allowed:
   rp=urllib.robotparser.RobotFileParser();rp.parse((R/meta['raw_file']).read_bytes().decode('utf8',errors='replace').splitlines());allowed=all(rp.can_fetch(a,url) for a in ['*','GPTBot','ChatGPT-User','OAI-SearchBot'])
  if not allowed:
   (W/(slug+'.not-fetched.json')).write_text(json.dumps({'url':url,'reason':'robots unavailable or disallowed; no alternate route attempted','robots_meta':str(mp.relative_to(R))},indent=2)+'\n');print(slug,'NOT_FETCHED_ROBOTS');continue
  m=save(slug,url)
  if m.get('status')==200:
   parser=Extract();parser.feed((R/m['raw_file']).read_bytes().decode('utf8',errors='replace'));(W/(slug+'.text.txt')).write_text('\n'.join(parser.text)+'\n');links=[{'text':x['text'].strip(),'url':urllib.parse.urljoin(m['final_url'],x['url'])} for x in parser.links];(W/(slug+'.links.json')).write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n')
  print(slug,m.get('status',m.get('error')),m.get('bytes',''))
if __name__=='__main__':
 action=sys.argv[1];data=json.load(sys.stdin);globals()[action](data)
