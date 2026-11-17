#!/usr/bin/env python3
"""Freeze every kept MSE discussion, all exposed pages, and immutable reading chunks."""
import sys,json,csv,re,time
from pathlib import Path
from urllib.parse import urljoin
sys.path.insert(0,str(Path(__file__).parent))
from harvest_oblique_mse import ROOT,RAW,fetch
from oblique_html import parse

def write_json(p,obj):p.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def freeze_new_threads(prefix='mse'):
 corpus=RAW/'corpus';corpus.mkdir(exist_ok=True)
 ip=corpus/(prefix+'-chunks.jsonl')
 previous=[json.loads(s) for s in ip.read_text().splitlines()] if ip.exists() else []
 frozen={d for r in previous for d in r['thread_ids']};pending=[];size=0
 def flush():
  nonlocal pending,size
  if not pending:return
  number=len(previous)+1;name=f'{prefix}-chunk-{number:03}.txt';body=''.join(x[1] for x in pending)
  target=corpus/name
  if target.exists():raise RuntimeError('Refusing to overwrite frozen '+str(target))
  target.write_text(body)
  rec={'file':str(target.relative_to(ROOT)),'bytes':len(body.encode()),'thread_ids':list(dict.fromkeys(x[0] for x in pending)),'parts':[x[2] for x in pending],'reading_status':'unread'}
  previous.append(rec)
  with ip.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
  print('CHUNK',name,rec['bytes'],rec['thread_ids'],flush=True);pending=[];size=0
 for p in sorted((RAW/'threads').glob(prefix+'-*.json')):
  if p.name.endswith('.http.json'):continue
  obj=json.loads(p.read_text());tid=obj['discussion_id']
  if tid in frozen or not obj.get('complete_visible_pagination'):continue
  header=f"\n{'='*65}\nTHREAD {prefix.upper()}-{tid}: {obj['title']}\nURL: {obj['url']}\nCATEGORY: {obj['label']} | pages={len(obj['pages'])} posts={len(obj['posts'])} listing_comments={obj['listing_comment_count']}\nFull visible discussion; bodies exclude repeated blockquotes and signatures.\n"
  units=[];current=header
  for post in obj['posts']:
   text=f"\nPOST {post['post_id']} | {'OP' if post['is_op'] else 'reply'} | author_id={post['author_id']} | {post['date']}\n{post['url']}\n{post['body']}\n"
   if len((current+text).encode())>42000 and current!=header:units.append(current);current=header+'CONTINUED\n'
   current+=text
  if current!=header:units.append(current)
  for i,unit in enumerate(units,1):
   if pending and size+len(unit.encode())>45000:flush()
   pending.append((tid,unit,{'thread_id':tid,'part':i,'total_parts':len(units)}));size+=len(unit.encode())
   if size>=35000:flush()
 flush()

def main():
 rows={str(r['discussion_id']):r for r in map(json.loads,(RAW/'mse-filtered.jsonl').read_text().splitlines())}
 decisions={}
 for p in sorted(RAW.glob('*mse-triage*.tsv')):
  with p.open() as f:
   for r in csv.DictReader(f,delimiter='\t'):
    k=r['discussion_id']
    if k in decisions and decisions[k]!=r:raise RuntimeError('Conflicting decisions '+k)
    decisions[k]=r
 keep=[(rows[k],r) for k,r in decisions.items() if r['decision']=='keep']
 write_json(RAW/'mse-thread-scope.json',{'listing_unique':1356,'filtered_cards':len(rows),'decisions':len(decisions),'kept':len(keep),'dropped':sum(r['decision']=='drop' for r in decisions.values()),'missing_decisions':sorted(set(rows)-set(decisions)),'triage_files':[p.name for p in sorted(RAW.glob('*mse-triage*.tsv'))]})
 print('SCOPE',len(keep),'kept',len(decisions),'triaged',flush=True)
 manifest=[]
 for index,(r,decision) in enumerate(keep,1):
  tid=str(r['discussion_id']);dest=RAW/'threads'/f'mse-{tid}.json'
  if dest.exists():
   old=json.loads(dest.read_text())
   if old.get('complete_visible_pagination'):manifest.append({k:old[k] for k in ['discussion_id','url','title','complete_visible_pagination','pages','post_count']});continue
  base=r['url'].split('#')[0].split('?')[0].rstrip('/');queue={1:base};seen=set();posts={};pages=[];errors=[];op=None
  while set(queue)-seen:
   page=min(set(queue)-seen);seen.add(page);url=queue[page]
   time.sleep(.4)
   html,access=fetch(url,RAW/'threads'/f'mse-{tid}-p{page:03}.html.gz');pages.append(access)
   if access['http_status']!=200:errors.append('page '+str(page)+' HTTP '+str(access['http_status']));break
   tree=parse(html)
   for a in tree.all(lambda n:n.tag=='a' and bool(n.attrs.get('href'))):
    link=urljoin(base,a.attrs['href']).split('#')[0].split('?')[0].rstrip('/')
    if m:=re.fullmatch(re.escape(base)+r'/p(\d+)',link):queue[int(m.group(1))]=link
   bodies=list(tree.all(lambda n:n.has('Message') and n.has('userContent')))
   if not bodies:errors.append('page '+str(page)+' has no public post bodies');break
   for body in bodies:
    wrap=body
    while wrap.parent and not (wrap.has('ItemDiscussion') or wrap.has('ItemComment')):wrap=wrap.parent
    pid=wrap.attrs.get('id','');author=wrap.first(lambda n:'data-userid' in n.attrs);date=wrap.first(lambda n:n.tag=='time')
    uid=author.attrs['data-userid'] if author else 'unknown'
    if wrap.has('ItemDiscussion'):op=uid
    if not pid:errors.append('post without source id');continue
    posts[pid]={'post_id':pid,'author_id':uid,'date':date.attrs.get('datetime','') if date else '', 'is_op':uid==op,'url':url+'#'+pid,'page':page,'body':body.clean(skip_quotes=True),'body_with_quotes':body.clean(),'raw_file':access['raw_file']}
  ordered=list(posts.values())
  obj={'discussion_id':tid,'title':r['title'],'url':base,'label':decision['label'],'listing_created':r['created'],'listing_comment_count':r['comment_count'],'complete_visible_pagination':not errors and seen==set(queue),'errors':errors,'pages':pages,'post_count':len(ordered),'posts':ordered}
  write_json(dest,obj);manifest.append({k:obj[k] for k in ['discussion_id','url','title','complete_visible_pagination','pages','post_count']})
  write_json(RAW/'mse-thread-manifest.json',manifest)
  print('THREAD',index,'/',len(keep),tid,'pages',len(pages),'posts',len(ordered),'errors',errors,flush=True)
  if index%15==0:freeze_new_threads()
 freeze_new_threads();write_json(RAW/'mse-thread-manifest.json',manifest)
 print('COMPLETE',len(manifest),'threads',sum(r['post_count'] for r in manifest),'posts',flush=True)

if __name__=='__main__':main()
