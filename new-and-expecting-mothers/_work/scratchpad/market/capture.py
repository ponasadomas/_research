"""Task wrapper around copied SYD fetch_page.py. Save robots and skip disallowed pages."""
from pathlib import Path
import json,sys,urllib.request,urllib.error,urllib.parse,urllib.robotparser,concurrent.futures,subprocess
ROOT=Path(__file__).resolve().parents[2]
manifest_path=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'manifest.json'
manifest=json.loads(manifest_path.read_text())
robots_dir=ROOT/'_raw/competitors/robots'; robots_dir.mkdir(parents=True,exist_ok=True)
origins=sorted({urllib.parse.urlsplit(row[1]).scheme+'://'+urllib.parse.urlsplit(row[1]).netloc for row in manifest})
def policy(origin):
 url=origin+'/robots.txt'; status=0; content=''; error=''
 try:
  with urllib.request.urlopen(url,timeout=25) as r: status=r.status; content=r.read().decode(errors='replace')
 except urllib.error.HTTPError as e: status=e.code; content=e.read().decode(errors='replace')
 except Exception as e: error=str(e)
 path=robots_dir/(urllib.parse.urlsplit(origin).netloc+'.txt')
 path.write_text(f'SOURCE: {url}\nHTTP: {status}\nERROR: {error}\n\n{content}')
 rp=urllib.robotparser.RobotFileParser();rp.parse(content.splitlines() if status==200 else [])
 return origin,dict(status=status,error=error,path=str(path.relative_to(ROOT))),rp
policies={}
for origin,meta,rp in concurrent.futures.ThreadPoolExecutor(max_workers=6).map(policy,origins):policies[origin]=(meta,rp)
def fetch(row):
 slug,url,segment=row; s=urllib.parse.urlsplit(url); origin=s.scheme+'://'+s.netloc; meta,rp=policies[origin]
 allowed=meta['status'] in (200,404,410)
 reason=''
 if meta['status']==200:
  for ua in ['ChatGPT-User','OAI-SearchBot','GPTBot']:
   if not rp.can_fetch(ua,url): allowed=False;reason='robots disallows '+ua;break
 if not allowed:
  return dict(slug=slug,url=url,segment=segment,robots=meta,status='not_fetched',reason=reason or 'robots unavailable; conservative exclusion')
 r=subprocess.run([sys.executable,str(ROOT/'_tools/fetch_page.py'),slug,url],capture_output=True,text=True)
 path=ROOT/'_raw/competitors'/f'{slug}.txt'
 txt=path.read_text() if path.exists() else ''
 import re
 m=re.search(r'HTTP: (\S+)',txt)
 return dict(slug=slug,url=url,segment=segment,robots=meta,status=m.group(1) if m else 'unknown',result=r.stdout.strip(),raw_file=str(path.relative_to(ROOT)))
rows=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(fetch,manifest))
logname='competitor-access-extra.jsonl' if len(sys.argv)>1 else 'competitor-access.jsonl'
(ROOT/'sources'/logname).write_text(''.join(json.dumps(row,ensure_ascii=False)+'\n' for row in rows))
for row in rows: print(row['slug'],row['status'],row.get('result',row.get('reason','')))
