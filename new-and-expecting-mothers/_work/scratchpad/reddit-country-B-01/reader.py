import collections,csv,hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
W=R/'_raw/reddit-deep/next-july-country-B-v1';P=W/'primary-v1'
A=json.loads((P/'assignments/batch-01.json').read_text());I={u['post_id']:u for u in map(json.loads,(P/'primary-index.jsonl').read_text().splitlines())}
T=R/'_raw/reddit-deep/triage/country-B-01.tsv';L=R/'sources/reddit-country-B-01-reading.jsonl';V=R/'voice/reddit-country-B-01.jsonl'
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build_cards():
 target=S/'card-views/manifest.json';assert not target.exists();target.parent.mkdir(exist_ok=True)
 chunks=[];parts=[];ids=[];mapping={};size=0
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=target.parent/f'{len(chunks)+1:03d}.txt';p.write_text('\n\n'.join(parts)+'\n');chunks.append({'file':str(p.relative_to(R)),'post_ids':ids,'sha256':sha(p)});parts=[];ids=[];size=0
 for c in A['chunks']:
  p=R/c['file'];assert sha(p)==c['sha256'];cards=re.split(r'\n\n(?=ID [a-z0-9]+ \|)',p.read_text().strip());found=[]
  for card in cards:
   pid=re.match(r'ID ([a-z0-9]+) \|',card)[1];found.append(pid);mapping[pid]=c['file']
   if size+len(card.encode())>14500:flush()
   parts.append(card);ids.append(pid);size+=len(card.encode())+2
  assert found==c['post_ids']
 flush();target.write_text(json.dumps({'scope':'complete assigned cards only; frozen display views','chunks':chunks,'original_card_files':mapping},indent=2)+'\n');print('card_views',len(chunks),'cards',len(mapping))
def cards(n):
 m=json.loads((S/'card-views/manifest.json').read_text());c=m['chunks'][n-1];assert sha(R/c['file'])==c['sha256'];print((R/c['file']).read_text(),end='')
def triage(n,text):
 m=json.loads((S/'card-views/manifest.json').read_text());c=m['chunks'][n-1];specs=[l.split('|',2) for l in text.strip().splitlines()];assert [s[0] for s in specs]==c['post_ids'];previous=list(csv.DictReader(T.open(),delimiter='\t')) if T.exists() else [];assert not {s[0] for s in specs}&{t['post_id'] for t in previous}
 allowed={'keep_play','keep_solids','keep_pumping_work','keep_sleep','keep_postpartum','keep_pregnancy','keep_registry','keep_other','drop'}
 with T.open('a',newline='') as f:
  w=csv.writer(f,delimiter='\t')
  if not previous:w.writerow(['post_id','label','reason','card_file'])
  for pid,label,reason in specs:
   assert label in allowed and reason.strip();w.writerow([pid,label,reason,m['original_card_files'][pid]])
 rows=list(csv.DictReader(T.open(),delimiter='\t'));progress={'cards':len(rows),'labels':dict(collections.Counter(r['label'] for r in rows)),'last_card_view':n};(S/'triage-progress.json').write_text(json.dumps(progress,indent=2)+'\n');print(json.dumps(progress))
def build_full():
 target=S/'full-views/manifest.json';assert not target.exists();rows=list(csv.DictReader(T.open(),delimiter='\t'));assert len(rows)==len(A['post_ids'])==292 and {r['post_id'] for r in rows}==set(A['post_ids']);keep=[r['post_id'] for r in rows if r['label'].startswith('keep_')];target.parent.mkdir(exist_ok=True)
 chunks=[];parts=[];ids=[];size=0
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=target.parent/f'{len(chunks)+1:03d}.txt';p.write_text('\n\n'.join(parts)+'\n');chunks.append({'file':str(p.relative_to(R)),'post_ids':ids,'sha256':sha(p)});parts=[];ids=[];size=0
 for pid in keep:
  u=I[pid];p=R/u['raw_file'];assert sha(p)==u['sha256'];text=p.read_text();content=text[text.index('=== COMPLETE ORIGINAL POST TITLE ==='):];meta={k:u[k] for k in ['post_id','subreddit','url','post_date','raw_file']};view='PRIMARY UNIT '+json.dumps(meta,ensure_ascii=False)+'\n'+content
  if size+len(view.encode())>22000:flush()
  parts.append(view);ids.append(pid);size+=len(view.encode())+2
 flush();target.write_text(json.dumps({'post_ids':keep,'units':[I[p] for p in keep],'chunks':chunks},indent=2)+'\n');print('keeps',len(keep),'full_views',len(chunks))
def full(n):
 m=json.loads((S/'full-views/manifest.json').read_text());c=m['chunks'][n-1];assert sha(R/c['file'])==c['sha256']
 for g in jl(P/'duplicate-flags.jsonl'):
  if set(c['post_ids'])&{r['post_id'] for r in g['records']}:print('EXACT BODY FLAG',json.dumps(g,ensure_ascii=False))
 old=[{'id':q['id'],'post_id':q.get('post_id')} for p in (R/'voice').glob('*.jsonl') if p!=V for q in jl(p) if q.get('post_id') in c['post_ids']]
 if old:print('EXISTING QUOTE IDS',json.dumps(old))
 print((R/c['file']).read_text(),end='')
def quotes(specs):
 prev=jl(V)
 for s in specs:
  u=I[s['post_id']];q={'id':f'rcb01-{len(prev)+1:04d}','source':'Reddit r/'+u['subreddit']+' — July country B','url':u['url'],'date':u['post_date'],'speaker':'parent_unspecified','stage':'unknown',**s,'raw_file':u['raw_file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','read_scope':'full_post_comment_source_unavailable'}
  assert q['quote'] in (R/u['raw_file']).read_text() and len(q['context'].split())<=25
  with V.open('a') as f:f.write(json.dumps(q,ensure_ascii=False)+'\n')
  prev.append(q);print(q['id'],q['post_id'])
def save(n,text):
 m=json.loads((S/'full-views/manifest.json').read_text());c=m['chunks'][n-1];specs=[l.split('|',2) for l in text.strip().splitlines()];assert [s[0] for s in specs]==c['post_ids'];prev=jl(L);assert not {s[0] for s in specs}&{r['post_id'] for r in prev};qs=jl(V)
 for pid,status,reason in specs:
  u=I[pid];assert status in {'e','x'} and sha(R/u['raw_file'])==u['sha256']
  row={'post_id':pid,'raw_file':u['raw_file'],'post_body_read_complete':True,'available_identifiable_OP_replies_read':0,'op_reply_ids_read':[],'primary_unit_sha256':u['sha256'],'status':'eligible' if status=='e' else 'read_pending_topic_review','reason':reason,'quote_ids':[q['id'] for q in qs if q['post_id']==pid],'reading_chunk':c['file']}
  with L.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 now=jl(L);progress={'full_originals':len(now),'keeps':len(m['post_ids']),'statuses':dict(collections.Counter(r['status'] for r in now)),'last_full_view':n};(S/'reading-progress.json').write_text(json.dumps(progress,indent=2)+'\n');print(json.dumps(progress))
if __name__=='__main__':
 cmd=sys.argv[1]
 if cmd=='build_cards':build_cards()
 if cmd=='cards':cards(int(sys.argv[2]))
 if cmd=='triage':triage(int(sys.argv[2]),sys.stdin.read())
 if cmd=='build_full':build_full()
 if cmd=='full':full(int(sys.argv[2]))
 if cmd=='quotes':quotes(json.load(sys.stdin))
 if cmd=='save':save(int(sys.argv[2]),sys.stdin.read())
