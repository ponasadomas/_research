# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
import json,hashlib,re,sys,csv,collections
from pathlib import Path
S=Path(__file__).resolve().parent;R=S.parents[1];W=R/'_raw/reddit-deep/next-july-country-B-v1';M=json.loads((W/'primary-v1/assignments/batch-02.json').read_text());I={x['post_id']:x for x in map(json.loads,(W/'primary-v1/primary-index.jsonl').read_text().splitlines())};T=R/'_raw/reddit-deep/triage/country-B-02.tsv'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
if sys.argv[1]=='prepare':
 assert not (S/'card-views.json').exists();views=[];buf='';ids=[];files={}
 for c in M['chunks']:
  assert sha(R/c['file'])==c['sha256'];parts=re.split(r'\n\n(?=ID )',(R/c['file']).read_text());seen=[]
  for p in parts:
   pid=re.match(r'ID (\S+)',p).group(1);seen.append(pid);files[pid]=c['file']
   if buf and len((buf+p).encode())>14500:
    f=f'cards-{len(views)+1:02d}.txt';(S/f).write_text(buf);views.append(dict(file=f,ids=ids,sha256=sha(S/f)));buf='';ids=[]
   buf+=p+'\n\n';ids.append(pid)
  assert seen==c['post_ids']
 if buf:
  f=f'cards-{len(views)+1:02d}.txt';(S/f).write_text(buf);views.append(dict(file=f,ids=ids,sha256=sha(S/f)))
 (S/'card-views.json').write_text(json.dumps(views,indent=2));(S/'card-files.json').write_text(json.dumps(files,indent=2));print('Frozen',len(views),'views',sum(len(c['ids']) for c in views),'cards')
elif sys.argv[1]=='cards':
 v=json.loads((S/'card-views.json').read_text())[int(sys.argv[2])-1];print('CARD VIEW',sys.argv[2],v['ids']);print((S/v['file']).read_text())
elif sys.argv[1]=='triage':
 v=json.loads((S/'card-views.json').read_text())[int(sys.argv[2])-1];rows=[];files=json.loads((S/'card-files.json').read_text());allowed={'keep_'+x for x in ['play','solids','pumping_work','sleep','postpartum','pregnancy','registry','other']}|{'drop'}
 for line in sys.stdin.read().splitlines():
  if not line.strip():continue
  pid,label,reason=line.split(' ',2);assert label in allowed;rows.append(dict(post_id=pid,label=label,reason=reason,card_file=files[pid]))
 assert [x['post_id'] for x in rows]==v['ids'];old=list(csv.DictReader(T.open(),delimiter='\t')) if T.exists() else [];assert not {x['post_id'] for x in old}&set(v['ids'])
 with T.open('a') as f:
  w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t');
  if not old:w.writeheader()
  w.writerows(rows)
 print('Triaged',len(rows),'total',len(old)+len(rows))
elif sys.argv[1]=='freeze_keeps':
 assert not (S/'kept-manifest.json').exists();rows=list(csv.DictReader(T.open(),delimiter='\t'));assert len(rows)==len(M['post_ids']) and {x['post_id'] for x in rows}==set(M['post_ids']);kept=[x['post_id'] for x in rows if x['label']!='drop'];views=[];buf='';ids=[]
 for p in kept:
  i=I[p];assert sha(R/i['raw_file'])==i['sha256'];raw=(R/i['raw_file']).read_text();text='\n\n######## READUNIT '+p+' | '+i['subreddit']+' | '+i['post_date']+' ########\n'+raw[raw.index('=== COMPLETE ORIGINAL POST TITLE ==='):]
  if buf and len((buf+text).encode())>15500:
   f=f'kept-{len(views)+1:03d}.txt';(S/f).write_text(buf);views.append(dict(file=f,ids=ids,sha256=sha(S/f)));buf='';ids=[]
  buf+=text;ids.append(p)
 if buf:
  f=f'kept-{len(views)+1:03d}.txt';(S/f).write_text(buf);views.append(dict(file=f,ids=ids,sha256=sha(S/f)))
 (S/'kept-manifest.json').write_text(json.dumps(dict(triage_sha256=sha(T),post_ids=kept,chunks=views),indent=2));print('Triaged',len(rows),collections.Counter(x['label'] for x in rows),'keeps',len(kept),'frozenchunks',len(views))
elif sys.argv[1]=='show':
 c=json.loads((S/'kept-manifest.json').read_text())['chunks'][int(sys.argv[2])-1];print('READCHUNK',sys.argv[2],c['ids']);print((S/c['file']).read_text())
elif sys.argv[1]=='record':
 c=json.loads((S/'kept-manifest.json').read_text())['chunks'][int(sys.argv[2])-1];a=json.load(sys.stdin);ex=a.get('excluded',{});assert set(ex)<=set(c['ids']);p=R/'sources/reddit-country-B-02-reading.jsonl';old={json.loads(s)['post_id'] for s in p.read_text().splitlines()} if p.exists() else set();assert not old&set(c['ids'])
 with p.open('a') as f:
  for pid in c['ids']:
   i=I[pid];assert sha(R/i['raw_file'])==i['sha256'];x=dict(post_id=pid,raw_file=i['raw_file'],post_body_read_complete=True,available_identifiable_OP_replies_read=0,op_reply_ids_read=[],primary_unit_sha256=i['sha256'],status='read_pending_topic_review' if pid in ex else 'eligible',reason=ex.get(pid,'Complete saved original read; bounded ordinary practical context, including clinical/safety advice as attributed speech.'),quote_ids=[],reading_chunk=c['file']);f.write(json.dumps(x,ensure_ascii=False)+'\n')
 with (S/'selections.jsonl').open('a') as f:
  for x in a.get('selections',[]):assert x['post_id'] in c['ids'] and len(x['context'].split())<=25;f.write(json.dumps(x,ensure_ascii=False)+'\n')
 print('Read recorded',len(c['ids']),'total',len(old)+len(c['ids']))
