"""Exact assigned inventory, complete reading views, primary outcome and whitespace-only quote audit."""
from july_focused_reader import *
import collections
fail=[]
def check(ok,msg):
 if not ok:fail.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assigned=[]
for r in map(json.loads,(PACKET/'triage-cards-index.jsonl').read_text().splitlines()):
 if r['subreddit'] in {'beyondthebump','ExclusivelyPumping','workingmoms','BabyLedWeaning','BeyondTheBumpUK'}:assigned+=r['post_ids']
with (ROOT/'_raw/reddit-deep/triage/july-focused.tsv').open() as f:tri=list(csv.DictReader(f,delimiter='\t'))
kept={r['post_id'] for r in tri if r['label']!='drop'}
ledger=[json.loads(x) for x in LEDGER.read_text().splitlines()];li={r['post_id']:r for r in ledger}
quotes=[json.loads(x) for x in VOICE.read_text().splitlines()]
check(len(tri)==len({r['post_id'] for r in tri})==len(assigned)==697,'697 unique exact assigned cards')
check({r['post_id'] for r in tri}==set(assigned),'Exact assigned card ID set')
check(len(ledger)==len(li)==len(kept)==406 and set(li)==kept,'406 exact complete kept original outcomes')
check(all(r['post_body_read_complete'] for r in ledger),'Every kept full original body read')
index=[json.loads(x) for x in (ROOT/'_raw/reddit-deep/july-focused-reading-v1/index.jsonl').read_text().splitlines()]
notes=[json.loads(x) for x in (ROOT/'sources/reddit-july-focused-chunk-notes.jsonl').read_text().splitlines()]
check(len(index)==len(notes)==21 and {r['chunk'] for r in notes}==set(range(1,22)),'21 complete primary views')
inspected={r['post_id'] for r in ledger if r['mode']=='full_read_during_eligibility_inspection'}
check(len(inspected)==19,'19 prior complete eligibility reads')
check(inspected.isdisjoint(t for r in index for t in r['post_ids']),'Views exclude prior complete reads')
check(inspected|{t for r in index for t in r['post_ids']}==kept,'Views plus prior reads equal kept set')
views=[]
for n,c in enumerate(index,1):
 expected=''
 for tid in c['post_ids']:
  u=unit(tid);m=u['meta']
  expected+=f"\n{'='*65}\nPOST {tid} | r/{m['subreddit']} | {m['post_date']}\n{m['url']}\nPRIMARY SCOPE: {m['primary_read_scope']} | OP replies={len(u['replies'])} | auxiliary nonOP={m['non_OP_comments_in_separate_unread_auxiliary']} unread\nTITLE: {u['title']}\n\n{u['body']}\n"
  for p in u['replies']:expected+=f"\n--- OP REPLY {p['comment_id']} | {p['date']} | parent={p['parent_id']}\n{p['url']}\n{p['body']}\n"
 path=ROOT/c['file'];check(path.read_text()==expected,'Lossless whole-body and every OP reply view '+str(n));check(path.stat().st_size==c['bytes'],'Frozen view bytes '+str(n))
 note=next(r for r in notes if r['chunk']==n);check(note['post_ids']==c['post_ids'] and note['all_primary_text_and_available_OP_replies_read'],'Human complete view ledger '+str(n))
 views.append({'file':c['file'],'sha256':sha(path),'bytes':path.stat().st_size,'post_ids':c['post_ids']})
for tid,r in li.items():
 u=unit(tid);m=u['meta'];check(r['sha256']==u['sha256'],'Original unchanged '+tid);check(r['available_identifiable_OP_replies_read']==len(u['replies']),'All available OP replies '+tid);check(r['comment_source_available']==bool(m['source_comment_file']),'Source comment scope '+tid)
seen=set();actors=set()
for n,r in enumerate(quotes,1):
 check(r['id']==f'rjfc01-{n:04}' and r['id'] not in seen,'Sequential unique quote ID '+r['id']);seen.add(r['id'])
 check(r['speaker'] in SPEAKERS and r['stage'] in STAGES and r['type'] in TYPES,'README vocabulary '+r['id']);check(len(r['context'].split())<=25,'Context <=25 words '+r['id'])
 tid=r['post_id'];u=unit(tid);m=u['meta'];check(tid in kept and li[tid]['read_status']=='read_complete','Eligible fully read source '+r['id'])
 if r.get('comment_id'):s=next(p for p in u['replies'] if p['comment_id']==r['comment_id'])
 else:s={'body':u['body'],'url':m['url'],'date':m['post_date']}
 check(r['raw_file']==u['file'] and r['url']==s['url'] and r['date']==s['date'][:10],'Exact original URL/date/file '+r['id'])
 pos=0
 for p in re.split(r'\s*\[(?:…|\.\.\.)\]\s*',r['quote']):
  at=norm(s['body']).find(norm(p),pos);check(at>=0,'Whitespace-only original wording/case/punctuation '+r['id']);pos=max(pos,at+len(norm(p)))
 check(r['archive_commit']=='ea497c510aa68765c07ed744ec9f84d68bbedf7f' and r['source_class']=='reddit_archive' and r['evidence_kind']=='archived_original','Archive provenance '+r['id'])
 check(r['Mamivio_report_purchase_proven'] is False,'No Mamivio purchase inference '+r['id'])
 if r.get('source_actor_key'):actors.add(r['source_actor_key'])
aux=[json.loads(x) for x in (ROOT/'sources/reddit-july-focused-auxiliary-read.jsonl').read_text().splitlines()]
unread=[json.loads(x) for x in (ROOT/'sources/reddit-july-focused-unread-auxiliary-index.jsonl').read_text().splitlines()]
check(len(aux)==len({(r['post_id'],r['comment_id']) for r in aux})==7,'Seven exact nonOP parent reads')
check(sum(r['archived_nonOP_comments'] for r in unread)==1796 and sum(r['unread_count'] for r in unread)==1789,'Precise auxiliary read/unread inventory')
check(sum(r['available_identifiable_OP_replies_read'] for r in ledger)==414,'414 complete identifiable OP replies')
stats={'assigned_cards':697,'card_files_fully_read':13,'initial_card_drops':sum(r['label']=='drop' for r in tri),'initial_kept_originals':len(kept),'kept_originals_fully_read':len(ledger),'kept_originals_unread':0,'post_read_exclusions':sum(r['read_status']!='read_complete' for r in ledger),'retained_context_originals':sum(r['read_status']=='read_complete' for r in ledger),'original_bytes':sum(unit(t)['bytes'] for t in kept),'original_author_replies_read':414,'nonOP_comments_read':7,'nonOP_comments_unread':1789,'complete_live_threads_read':0,'quote_count':len(quotes),'quoted_post_ids':len({r['post_id'] for r in quotes}),'quoted_archive_account_keys':len(actors),'account_keys_are_not_verified_independent_people':True,'by_community':dict(collections.Counter(r['subreddit'] for r in ledger)),'by_read_status':dict(collections.Counter(r['read_status'] for r in ledger)),'comment_sources_available_originals':sum(r['comment_source_available'] for r in ledger),'comment_sources_unavailable_originals':sum(not r['comment_source_available'] for r in ledger)}
report={'failed':len(fail),'failures':fail,'stats':stats,'voice_sha256':sha(VOICE),'scope':'Every assigned card and all human-kept full original bodies plus all identifiable archived OP replies. NonOP auxiliary comments separately unread except exact7 parent reads. No live-thread completeness, market prevalence, validated clinical outcome or Mamivio purchase claim.','view_manifest':views}
(ROOT/'sources/reddit-july-focused-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='view_manifest'},ensure_ascii=False,indent=2));raise SystemExit(bool(fail))
