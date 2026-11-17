#!/usr/bin/env python3
"""Whole public MSE mums/dads category listings; immutable raw HTTP responses.

Adapted around the SYD fetch_page extraction and raw-first pipeline. No search,
login, RSS, profile or discussion/comment endpoints. Default mode saves all
public listing pages exposed by each category's own pagination (49/19 initially).
"""
from pathlib import Path
from html.parser import HTMLParser
import urllib.request, urllib.error, re, json, gzip, time, sys, datetime
sys.path.insert(0,str(Path(__file__).parent))
from fetch_page import extract

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/oblique-deep'
BASE='https://forums.moneysavingexpert.com'

class Props(HTMLParser):
 def __init__(self):super().__init__(convert_charrefs=True);self.values=[];self.links=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='a' and d.get('href'):self.links.append(d['href'])
  if d.get('data-props'):
   try:self.values.append(json.loads(d['data-props']))
   except json.JSONDecodeError:pass

def fetch(url,path):
 if path.exists():
  logpath=path.with_suffix('.http.json')
  prior=json.loads(logpath.read_text()) if logpath.exists() else {'url':url,'http_status':200,'raw_file':str(path.relative_to(ROOT))}
  return gzip.open(path,'rt',encoding='utf-8').read(),prior|{'existing':True}
 status=0;final=url
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'ChatGPT-User (public research; no login)'})
  with urllib.request.urlopen(req,timeout=35) as response:
   data=response.read();status=response.status;final=response.url;headers=dict(response.headers)
 except urllib.error.HTTPError as e:
  data=e.read();status=e.code;headers=dict(e.headers)
 except Exception as e:
  data=str(e).encode();headers={}
 path.parent.mkdir(parents=True,exist_ok=True)
 with gzip.open(path,'wb') as f:f.write(data)
 record={'url':url,'final_url':final,'http_status':status,'bytes':len(data),'captured_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'raw_file':str(path.relative_to(ROOT)),'headers':headers}
 path.with_suffix('.http.json').write_text(json.dumps(record,indent=2)+'\n')
 return data.decode('utf-8',errors='replace'),record

def listings():
 manifest=[];records=[]
 for category in ['moneysaving-mums','moneysaving-dads']:
  first=BASE+'/categories/'+category
  s,log=fetch(first,RAW/'boards'/f'{category}-p001.html.gz');manifest.append(log)
  p=Props();p.feed(s)
  nums=[int(m.group(1)) for u in p.links if (m:=re.search(r'/categories/'+category+r'/p(\d+)(?:$|[?#])',u))]
  last=max(nums or [1]);print(category,'pages',last,flush=True)
  for page in range(1,last+1):
   if page!=1:
    time.sleep(.45);s,log=fetch(first+'/p'+str(page),RAW/'boards'/f'{category}-p{page:03}.html.gz');manifest.append(log)
    p=Props();p.feed(s)
   if manifest[-1]['http_status']!=200:raise RuntimeError('Stopping on access failure '+str(manifest[-1]))
   batch=[]
   for v in p.values:
    if isinstance(v,dict) and isinstance(v.get('discussions'),list):batch+=v['discussions']
   if not batch:raise RuntimeError('No original discussion listing units at '+first+' page '+str(page))
   for q in batch:
    records.append({'discussion_id':q['discussionID'],'title':q['name'],'excerpt':q.get('excerpt',''),'created':q.get('dateInserted',''),'last_comment':q.get('dateLastComment',''),'comment_count':q.get('countComments'),'url':q.get('canonicalUrl') or q['url'],'board':category,'listing_page':page,'pinned':q.get('pinned',False)})
   print(category,page,len(batch),'cumulative',len(records),flush=True)
   (RAW/'listing-access.json').write_text(json.dumps(manifest,indent=2)+'\n')
   (RAW/'listing-rows.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in records))
 unique={q['discussion_id']:q for q in records}
 (RAW/'listing-unique.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in unique.values()))
 print('LISTINGS',len(records),'rows,',len(unique),'unique discussions',flush=True)

if __name__=='__main__':listings()
