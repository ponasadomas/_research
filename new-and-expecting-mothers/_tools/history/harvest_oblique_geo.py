#!/usr/bin/env python3
"""Harvest every exposed listing page of three finite historical GeoBaby boards."""
from pathlib import Path
import sys,json,re,time,urllib.parse
sys.path.insert(0,str(Path(__file__).parent))
from harvest_oblique_mse import fetch,ROOT,RAW
from oblique_html import parse

BASE='https://archive.geoclicks.com'
BOARDS=['preparing-for-the-arrival.16','twins-and-multiples.59','pregnant-with-multiples.40']

def main():
 records=[];logs=[]
 for slug in BOARDS:
  first=BASE+'/forums/'+slug+'/'
  s,log=fetch(first,RAW/'boards'/f'geo-{slug}-p001.html.gz');logs.append(log);tree=parse(s)
  nums=[int(m.group(1)) for n in tree.all(lambda n:n.tag=='a') if (m:=re.fullmatch('/forums/'+re.escape(slug)+r'/page-(\d+)',n.attrs.get('href','')))]
  last=max(nums or [1]);print(slug,'pages',last,flush=True)
  for page in range(1,last+1):
   if page!=1:
    time.sleep(.5);s,log=fetch(first+'page-'+str(page),RAW/'boards'/f'geo-{slug}-p{page:03}.html.gz');logs.append(log);tree=parse(s)
   if logs[-1]['http_status']!=200:raise RuntimeError('Stopped on access failure '+str(logs[-1]))
   nodes=list(tree.all(lambda n:n.has('structItem--thread')))
   if not nodes:raise RuntimeError('No listing nodes '+first+' page '+str(page))
   for node in nodes:
    title=node.first(lambda n:n.has('structItem-title'));link=title.first(lambda n:n.tag=='a' and '/threads/' in n.attrs.get('href','')) if title else None
    if not link:continue
    url=urllib.parse.urljoin(BASE,link.attrs['href']);m=re.search(r'\.(\d+)/?$',urllib.parse.urlparse(url).path)
    times=[n.attrs.get('datetime','') for n in node.all(lambda n:n.tag=='time')]
    meta=node.first(lambda n:n.has('structItem-cell--meta'))
    records.append(dict(discussion_id=m.group(1) if m else url,title=link.clean(),url=url,board=slug,listing_page=page,created=times[0] if times else '',last_comment=times[-1] if times else '',metadata=meta.clean() if meta else '',excerpt=''))
   print(slug,page,len(nodes),'cumulative',len(records),flush=True)
   (RAW/'geo-listing-access.json').write_text(json.dumps(logs,indent=2)+'\n')
   (RAW/'geo-listing-rows.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in records))
 unique={q['discussion_id']:q for q in records}
 (RAW/'geo-listing-unique.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in unique.values()))
 print('GEO LISTINGS',len(records),'rows',len(unique),'unique',flush=True)

if __name__=='__main__':main()
