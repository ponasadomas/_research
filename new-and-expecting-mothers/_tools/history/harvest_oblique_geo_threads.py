#!/usr/bin/env python3
"""All kept original GeoBaby archive discussions in declared finite scope."""
import sys,json,csv,re,time
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0,str(Path(__file__).parent))
from harvest_oblique_mse import RAW,fetch
from harvest_oblique_threads import write_json,freeze_new_threads
from oblique_html import parse

def main():
 rows={r['discussion_id']:r for r in map(json.loads,(RAW/'geo-listing-unique.jsonl').read_text().splitlines())}
 with (RAW/'agent-geo-triage.tsv').open() as f:decisions=list(csv.DictReader(f,delimiter='\t'))
 keep=[(rows[r['discussion_id']],r) for r in decisions if r['decision']=='keep']
 write_json(RAW/'geo-thread-scope.json',{'listing_unique':1224,'title_filter_matches':594,'scoped_cards':231,'kept':len(keep),'scoped_excluded':48,'out_of_window_matches':363,'unmatched':630,'date_window':'PreparingArrival created2010-01-01 onward; both complete multiples boards all dates','scope_set_before_full_discussion_read':True})
 manifest=[]
 for index,(r,decision) in enumerate(keep,1):
  tid=r['discussion_id'];dest=RAW/'threads'/f'geo-{tid}.json'
  if dest.exists():
   old=json.loads(dest.read_text())
   if old.get('complete_visible_pagination'):manifest.append({k:old[k] for k in ['discussion_id','url','title','complete_visible_pagination','pages','post_count']});continue
  base=r['url'].rstrip('/');queue={1:base+'/'};seen=set();posts={};pages=[];errors=[];op=None
  while set(queue)-seen:
   page=min(set(queue)-seen);seen.add(page);url=queue[page];time.sleep(.5)
   html,access=fetch(url,RAW/'threads'/f'geo-{tid}-p{page:03}.html.gz');pages.append(access)
   if access['http_status']!=200:errors.append('page '+str(page)+' HTTP '+str(access['http_status']));break
   tree=parse(html)
   for a in tree.all(lambda n:n.tag=='a' and bool(n.attrs.get('href'))):
    link=urljoin(base+'/',a.attrs['href']).split('#')[0].split('?')[0].rstrip('/')
    if m:=re.fullmatch(re.escape(base)+r'/page-(\d+)',link):queue[int(m.group(1))]=link
   messages=list(tree.all(lambda n:n.tag=='article' and n.has('message--post')))
   if not messages:errors.append('page '+str(page)+' has no original public post bodies');break
   for n in messages:
    body=n.first(lambda z:z.has('bbWrapper'));author=n.first(lambda z:'data-user-id' in z.attrs);date=n.first(lambda z:z.tag=='time')
    pid=n.attrs.get('data-content','');uid=author.attrs['data-user-id'] if author else 'unknown'
    if op is None:op=uid
    if not pid or body is None:errors.append('post without source id/body');continue
    posts[pid]={'post_id':pid,'author_id':uid,'date':date.attrs.get('datetime','') if date else '', 'is_op':uid==op and uid!='unknown','url':url+'#'+pid,'page':page,'body':body.clean(skip_quotes=True),'body_with_quotes':body.clean(),'raw_file':access['raw_file']}
  obj={'discussion_id':tid,'title':r['title'],'url':base+'/','label':decision['label'],'listing_created':r['created'],'listing_comment_count':r['metadata'],'complete_visible_pagination':not errors and seen==set(queue),'errors':errors,'pages':pages,'post_count':len(posts),'posts':list(posts.values())}
  write_json(dest,obj);manifest.append({k:obj[k] for k in ['discussion_id','url','title','complete_visible_pagination','pages','post_count']})
  write_json(RAW/'geo-thread-manifest.json',manifest)
  print('GEO THREAD',index,'/',len(keep),tid,'pages',len(pages),'posts',len(posts),'errors',errors,flush=True)
  if index%15==0:freeze_new_threads('geo')
 freeze_new_threads('geo');write_json(RAW/'geo-thread-manifest.json',manifest)
 print('COMPLETE',len(manifest),'threads',sum(r['post_count'] for r in manifest),'posts',flush=True)

if __name__=='__main__':main()
