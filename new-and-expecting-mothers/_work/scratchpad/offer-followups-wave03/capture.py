import requests,json,hashlib,sys
from pathlib import Path
from datetime import datetime,timezone
from bs4 import BeautifulSoup
R=Path(__file__).resolve().parents[2];W=R/'_raw/offer-followups-wave03';A=W/'access.jsonl'
allowed={'www.stresslessmom.com','thevillageparentcommunity.com','www.curatedtogrow.com','www.nestingnotesco.com'}
for spec in json.load(sys.stdin):
 slug,url=spec;assert url.split('/')[2] in allowed
 p=W/'pages'/f'{slug}.html';assert not p.exists()
 try:
  r=requests.get(url,timeout=25);p.write_bytes(r.content)
  h=p.with_suffix('.headers.json');h.write_text(json.dumps(dict(headers=dict(r.headers),history=[dict(url=x.url,status=x.status_code,headers=dict(x.headers)) for x in r.history]),indent=2)+'\n')
  soup=BeautifulSoup(r.content,'html.parser')
  for x in soup(['script','style','noscript']):x.decompose()
  text=soup.get_text('\n',strip=True);p.with_suffix('.txt').write_text(text+'\n')
  links=[dict(text=a.get_text(' ',strip=True),url=a.get('href')) for a in soup.find_all('a',href=True)]
  p.with_suffix('.links.json').write_text(json.dumps(links,ensure_ascii=False,indent=2)+'\n')
  row=dict(url=url,final_url=r.url,status=r.status_code,captured_utc=datetime.now(timezone.utc).isoformat(),raw_file=str(p.relative_to(R)),raw_sha256=hashlib.sha256(r.content).hexdigest(),text_file=str(p.with_suffix('.txt').relative_to(R)),text_sha256=hashlib.sha256(p.with_suffix('.txt').read_bytes()).hexdigest(),bytes=len(r.content),text_chars=len(text))
 except requests.RequestException as e:row=dict(url=url,error=str(e))
 with A.open('a') as f:f.write(json.dumps(row)+'\n')
 print(json.dumps(row))
