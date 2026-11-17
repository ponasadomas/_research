import collections,csv,hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent/'supplement-v1';S.mkdir(exist_ok=True);W=R/'_raw/report-purchase-archive-wave03'
T=S/'triage.tsv';L=R/'sources/report-purchase-archive-wave03-reading.jsonl';V=R/'voice/report-purchase-archive-wave03.jsonl'
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
I={x['post_id']:x for x in jl(W/'supplement-v1/commercial-candidates.jsonl')}
def build_cards():
 target=S/'card-views/manifest.json';assert not target.exists();target.parent.mkdir(exist_ok=True);chunks=[];parts=[];ids=[];size=0
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=target.parent/f'{len(chunks)+1:03d}.txt';p.write_text('\n\n'.join(parts)+'\n');chunks.append({'file':str(p.relative_to(R)),'post_ids':ids,'sha256':sha(p)});parts=[];ids=[];size=0
 for pid,u in I.items():
  p=R/u['card_file'];assert sha(p)==u['card_sha256'];card=p.read_text()
  if size+len(card.encode())>14500:flush()
  parts.append(card);ids.append(pid);size+=len(card.encode())+2
 flush();target.write_text(json.dumps({'post_ids':list(I),'chunks':chunks},indent=2)+'\n');print('cards',len(I),'views',len(chunks))
def cards(n):
 c=json.loads((S/'card-views/manifest.json').read_text())['chunks'][n-1];assert sha(R/c['file'])==c['sha256'];print((R/c['file']).read_text(),end='')
def triage(n,text):
 c=json.loads((S/'card-views/manifest.json').read_text())['chunks'][n-1];spec=[s.split('|',2) for s in text.strip().splitlines()];assert [x[0] for x in spec]==c['post_ids'];prev=list(csv.DictReader(T.open(),delimiter='\t')) if T.exists() else [];assert not {x[0] for x in spec}&{x['post_id'] for x in prev}
 with T.open('a',newline='') as f:
  w=csv.writer(f,delimiter='\t')
  if not prev:w.writerow(['post_id','label','reason','card_file'])
  for pid,label,reason in spec:assert label in {'keep','drop'} and reason.strip();w.writerow([pid,label,reason,I[pid]['card_file']])
 rows=list(csv.DictReader(T.open(),delimiter='\t'));print('triaged',len(rows),dict(collections.Counter(x['label'] for x in rows)))
def build_full():
 target=S/'full-views/manifest.json';assert not target.exists();rows=list(csv.DictReader(T.open(),delimiter='\t'));assert [r['post_id'] for r in rows]==list(I);keep=[r['post_id'] for r in rows if r['label']=='keep'];target.parent.mkdir(exist_ok=True);chunks=[];parts=[];ids=[];size=0
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=target.parent/f'{len(chunks)+1:03d}.txt';p.write_text('\n\n'.join(parts)+'\n');chunks.append({'file':str(p.relative_to(R)),'post_ids':ids,'sha256':sha(p)});parts=[];ids=[];size=0
 for pid in keep:
  u=I[pid];p=R/u['raw_file'];assert sha(p)==u['sha256'];text=p.read_text();part='PRIMARY UNIT '+json.dumps({k:u[k] for k in ['post_id','subreddit','url','date','raw_file']},ensure_ascii=False)+'\n'+text[text.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
  if size+len(part.encode())>22000:flush()
  parts.append(part);ids.append(pid);size+=len(part.encode())+2
 flush();target.write_text(json.dumps({'post_ids':keep,'chunks':chunks},indent=2)+'\n');print('keeps',len(keep),'views',len(chunks))
def full(n):
 c=json.loads((S/'full-views/manifest.json').read_text())['chunks'][n-1];assert sha(R/c['file'])==c['sha256'];print((R/c['file']).read_text(),end='')
def quotes(spec):
 prev=jl(V)
 for s in spec:
  u=I[s['post_id']];q={'id':f'rpa03-{len(prev)+1:04d}','source':'Reddit r/'+u['subreddit']+' — additional commercial archive','date':u['date'],'url':u['url'],'speaker':'parent_unspecified','stage':'unknown',**s,'raw_file':u['raw_file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','read_scope':'full_post_comment_source_unavailable'};assert q['quote'] in (R/u['raw_file']).read_text() and len(q['context'].split())<=25
  with V.open('a') as f:f.write(json.dumps(q,ensure_ascii=False)+'\n')
  prev.append(q);print(q['id'],q['post_id'])
def save(n,text):
 c=json.loads((S/'full-views/manifest.json').read_text())['chunks'][n-1];spec=[s.split('|',2) for s in text.strip().splitlines()];assert [x[0] for x in spec]==c['post_ids'];prev=jl(L);assert not {x[0] for x in spec}&{x['post_id'] for x in prev};qs=jl(V)
 for pid,status,reason in spec:
  u=I[pid];assert status in {'e','x'} and sha(R/u['raw_file'])==u['sha256'];row={'post_id':pid,'raw_file':u['raw_file'],'post_body_read_complete':True,'available_identifiable_OP_replies_read':0,'op_reply_ids_read':[],'comment_source_available':False,'comment_status':'publisher_comment_file_unavailable','primary_unit_sha256':u['sha256'],'date':u['date'],'url':u['url'],'source_archive':u['archive_file'],'status':'eligible' if status=='e' else 'read_pending_topic_review','reason':reason,'quote_ids':[q['id'] for q in qs if q['post_id']==pid],'reading_chunk':c['file']}
  with L.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 now=jl(L);progress={'full_originals':len(now),'keeps':len(json.loads((S/'full-views/manifest.json').read_text())['post_ids']),'statuses':dict(collections.Counter(r['status'] for r in now)),'last_full_view':n};(S/'reading-progress.json').write_text(json.dumps(progress,indent=2)+'\n');print(json.dumps(progress))
if __name__=='__main__':
 cmd=sys.argv[1]
 if cmd in {'build_cards','build_full'}:globals()[cmd]()
 if cmd in {'cards','full'}:globals()[cmd](int(sys.argv[2]))
 if cmd in {'triage','save'}:globals()[cmd](int(sys.argv[2]),sys.stdin.read())
 if cmd=='quotes':quotes(json.load(sys.stdin))
