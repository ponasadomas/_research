#!/usr/bin/env python3
"""Manual primary-reading ledger and exact Reddit-archive excerpt helper."""
from pathlib import Path
import json,re,csv,hashlib,datetime
ROOT=Path(__file__).resolve().parents[1];PACKET=ROOT/'_raw/reddit-deep/july-2025-wave-v1'
LEDGER=ROOT/'sources/reddit-july-focused-primary-ledger.jsonl';VOICE=ROOT/'voice/reddit-july-focused.jsonl'
CANDIDATES={r['id']:r for r in map(json.loads,(PACKET/'candidates.jsonl').read_text().splitlines())}
SPEAKERS={'expecting_mother','new_mother','experienced_mother','parent_unspecified','partner','relative_caregiver','recovered_parent','gave_up_parent','advisor','professional','reviewer','skeptic'}
STAGES={'pregnancy_early','pregnancy_late','newborn_0_6_weeks','baby_6_16_weeks','baby_4_6_months','baby_6_12_months','toddler','return_to_work','looking_back','unknown'}
TYPES={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said'}
def norm(s):return ' '.join(s.split())
def unit(tid):
 c=CANDIDATES[tid];path=PACKET/'primary-units'/f"{c['subreddit']}-{tid}.txt";s=path.read_text()
 meta=json.loads(s.split('\n',1)[1].split('\n=== COMPLETE ORIGINAL POST TITLE ===',1)[0])
 title=s.split('=== COMPLETE ORIGINAL POST TITLE ===\n',1)[1].split('\n=== COMPLETE ORIGINAL POST BODY ===',1)[0].strip()
 body=s.split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
 replies=[]
 for block in s.split('\n--- OP REPLY ---\n')[1:]:
  metadata,text=block.split('\n',1);replies.append(json.loads(metadata)|{'body':text.strip()})
 assert len(replies)==meta['OP_replies'],(tid,len(replies),meta['OP_replies'])
 return {'file':str(path.relative_to(ROOT)),'meta':meta,'title':title,'body':body,'replies':replies,'bytes':len(s.encode()),'sha256':hashlib.sha256(s.encode()).hexdigest()}
def mark_read(ids,note,mode='complete_primary_read',excluded=None):
 old=[json.loads(s) for s in LEDGER.read_text().splitlines()] if LEDGER.exists() else []
 used={r['post_id'] for r in old}
 for tid in ids:
  assert tid not in used,('Already logged',tid);u=unit(tid);m=u['meta']
  record={'post_id':tid,'subreddit':m['subreddit'],'raw_file':u['file'],'sha256':u['sha256'],'read_status':'read_pending_topic_review' if excluded else 'read_complete','mode':mode,'post_body_read_complete':True,'available_identifiable_OP_replies_read':len(u['replies']),'comment_source_available':bool(m['source_comment_file']),'OP_identifiable':m['OP_identifiable'],'read_scope':'full_post_and_available_identifiable_OP_replies' if m['source_comment_file'] else 'full_post_comment_source_unavailable','non_OP_auxiliary_comments':m['non_OP_comments_in_separate_unread_auxiliary'],'non_OP_auxiliary_scope':'unread except exact parent records separately logged','note':note,'exclusion_reason':excluded,'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
  with LEDGER.open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
 print('Logged',len(ids),'complete primary reads')
def add(tid,quote,kind,themes,context,speaker='parent_unspecified',stage='unknown',comment_id=None,**extra):
 assert speaker in SPEAKERS and stage in STAGES and kind in TYPES
 assert len(context.split())<=25
 ledger=[json.loads(s) for s in LEDGER.read_text().splitlines()]
 assert any(r['post_id']==tid and r['post_body_read_complete'] is True for r in ledger),'Only completely read primary units may be quoted'
 u=unit(tid);m=u['meta'];source=next(r for r in u['replies'] if r['comment_id']==comment_id) if comment_id else {'body':u['body'],'url':m['url'],'date':m['post_date']}
 pos=0;body=norm(source['body'])
 for piece in re.split(r'\s*\[(?:…|\.\.\.)\]\s*',quote):
  found=body.find(norm(piece),pos);assert found>=0,(tid,comment_id,quote);pos=found+len(norm(piece))
 old=[json.loads(s) for s in VOICE.read_text().splitlines()] if VOICE.exists() else []
 assert not any(r['post_id']==tid and r.get('comment_id')==comment_id and r['quote']==quote for r in old),'Duplicate excerpt'
 author=CANDIDATES[tid]['author'];actor=None if author in ['[deleted]','[removed]',''] else 'archive-account-'+hashlib.sha256(author.encode()).hexdigest()[:16]
 rec={'id':f'rjfc01-{len(old)+1:04}','source':'reddit-r/'+m['subreddit']+' archived original','url':source['url'],'date':source['date'][:10],'speaker':speaker,'stage':stage,'type':kind,'themes':themes,'quote':quote,'context':context,'raw_file':u['file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','post_id':tid,'read_scope':'full_post_and_available_identifiable_OP_replies' if m['source_comment_file'] else 'full_post','comment_source_available':bool(m['source_comment_file']),'identifiable_OP_replies_available':len(u['replies']),'source_actor_key':actor,**extra}
 if comment_id:rec['comment_id']=comment_id
 with VOICE.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
 print(rec['id'],tid,'words',len(quote.split()))
def prepare():
 dest=ROOT/'_raw/reddit-deep/july-focused-reading-v1';dest.mkdir(exist_ok=True)
 assert not (dest/'index.jsonl').exists(),'Frozen packet already exists'
 with (ROOT/'_raw/reddit-deep/triage/july-focused.tsv').open() as f:kept=[r['post_id'] for r in csv.DictReader(f,delimiter='\t') if r['label']!='drop']
 cardledger=[json.loads(s) for s in (ROOT/'sources/reddit-july-focused-card-ledger.jsonl').read_text().splitlines()]
 inspected=list(dict.fromkeys(tid for r in cardledger for tid in r.get('full_source_eligibility_inspections',[]) if tid in kept))
 mark_read(inspected,'Complete frozen original and all included OP replies were read to EOF during documented eligibility inspection; accepted after human triage.','full_read_during_eligibility_inspection')
 index=[];pending=[];body=''
 def flush():
  nonlocal body,pending
  if not pending:return
  file=dest/f'focused-primary-{len(index)+1:03}.txt';file.write_text(body)
  index.append({'file':str(file.relative_to(ROOT)),'post_ids':pending,'bytes':len(body.encode()),'read_status':'unread','scope':'complete original body/title and all available identifiable OP replies; provenance metadata retained per unit'})
  body='';pending=[]
 for tid in kept:
  if tid in inspected:continue
  u=unit(tid);m=u['meta'];text=f"\n{'='*65}\nPOST {tid} | r/{m['subreddit']} | {m['post_date']}\n{m['url']}\nPRIMARY SCOPE: {m['primary_read_scope']} | OP replies={len(u['replies'])} | auxiliary nonOP={m['non_OP_comments_in_separate_unread_auxiliary']} unread\nTITLE: {u['title']}\n\n{u['body']}\n"
  for reply in u['replies']:text+=f"\n--- OP REPLY {reply['comment_id']} | {reply['date']} | parent={reply['parent_id']}\n{reply['url']}\n{reply['body']}\n"
  if pending and len((body+text).encode())>42000:flush()
  body+=text;pending.append(tid)
  if len(body.encode())>=35000:flush()
 flush();(dest/'index.jsonl').write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in index))
 print('Kept',len(kept),'already full-read',len(inspected),'unread units',sum(len(r['post_ids']) for r in index),'chunks',len(index),'reading bytes',sum(r['bytes'] for r in index))
if __name__=='__main__':prepare()
