#!/usr/bin/env python3
"""Strict scoped audit of qdeep01; reads preserved API bodies, never collects sources."""
import collections,csv,datetime,hashlib,html,json,pathlib,re,sys
from html.parser import HTMLParser
ROOT=pathlib.Path(__file__).resolve().parents[1];RAW=ROOT/'_raw/qa-deep'
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[];self.depth=0
 def handle_starttag(self,tag,attrs):
  if tag=='blockquote':self.depth+=1
  if tag in ['p','li','br','div','h1','h2','h3']:self.parts.append(' ')
 def handle_endtag(self,tag):
  if tag=='blockquote':self.depth-=1
  if tag in ['p','li','div']:self.parts.append(' ')
 def handle_data(self,data):
  if self.depth==0:self.parts.append(data)
def norm(s):return re.sub(r'\s+',' ',html.unescape(s)).strip()
def own(s):
 p=Text();p.feed(s);return norm(''.join(p.parts))
def read(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
quotes=read(ROOT/'voice/qa-deep-01.jsonl');index=read(RAW/'thread-index.jsonl');ledger=read(RAW/'read-ledger-qdeep01.jsonl');state=json.loads((RAW/'reader-state-qdeep01.json').read_text());attrs=read(RAW/'attribution-qdeep01.jsonl')
triage=list(csv.DictReader((RAW/'human-triage.tsv').open(),delimiter='\t'));native={x['id']:json.loads((RAW/f"threads/{x['id']}.json").read_text()) for x in index};ix={x['id']:x for x in index};ll={x['question_id']:x for x in ledger};aa={x['quote_id']:x for x in attrs}
fail=[]
def ck(v,msg):
 if not v:fail.append(msg)
manifest={x['id'] for x in index};cardids=[int(x) for x in re.findall(r'^Q(\d+) \|',(RAW/'triage-cards.txt').read_text(),re.M)];ck(set(cardids)==manifest and len(cardids)==len(set(cardids)),'card_manifest_id_set');triageids=[int(x['id']) for x in triage];kept={int(x['id']) for x in triage if x['label']=='keep'};reads=[x['question_id'] for x in ledger];excluded={x['question_id'] for x in ledger if x['outcome']=='excluded_after_full_read'}
ck(len(manifest)==248,'index_count');ck(set(triageids)==manifest and len(triageids)==len(set(triageids)),'triage_id_set');ck(state['card_read_complete'] and state['card_count']==248,'all_cards_read');ck(set(reads)==kept and len(reads)==len(set(reads)),'kept_read_reconciliation');ck(set(state['read_ids'])==kept and set(state['kept_ids'])==kept,'state_reconciliation');ck(set(state['excluded_after_read_ids'])==excluded,'state_exclusions')
for qid in reads:
 n=native[qid];l=ll[qid];ck(ix[qid]['full_available_api_relations_saved'] and ix[qid]['answers']==len(n['answers']) and ix[qid]['comments']==len(n['comments']),f'{qid}:saved_relation_index');ck(l['read_question'] and l['read_scope']=='full_available_API_thread',f'{qid}:read_scope');ck(l['answers_read']==len(n['answers']) and l['comments_read']==len(n['comments']),f'{qid}:relation_counts')
readme=(ROOT/'README.md').read_text();speakers={'expecting_mother','new_mother','experienced_mother','parent_unspecified','partner','relative_caregiver','recovered_parent','gave_up_parent','advisor','professional','reviewer','skeptic'};stages={'pregnancy_early','pregnancy_late','newborn_0_6_weeks','baby_6_16_weeks','baby_4_6_months','baby_6_12_months','toddler','return_to_work','looking_back','unknown'};types={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said'}
budget=collections.Counter();qids=[]
for q in quotes:
 qid=q['question_id'];pid=q['post_id'];cid=q.get('comment_id');n=native[qid];question=n['question'];post=next((c for c in n['comments'] if c['comment_id']==cid),None) if cid is not None else (question if pid==qid else next((a for a in n['answers'] if a['answer_id']==pid),None));key=('comment',cid) if cid is not None else ('post',pid);qids.append(q['id'])
 ck(post is not None,f"{q['id']}:native_post");
 if post is None:continue
 budget[key]+=len(q['quote'].split());ck(norm(q['quote']) in own(post['body']),f"{q['id']}:own_original_not_third_party_exact");ck(norm(q['quote']) in norm((ROOT/q['raw_file']).read_text()),f"{q['id']}:preserved_txt_exact");ck(qid in kept and qid not in excluded,f"{q['id']}:retained");ck(q['read_scope']=='full_available_API_thread',f"{q['id']}:scope");ck(q['raw_file']==ix[qid]['raw_file'],f"{q['id']}:raw_file");ck(len(q['context'].split())<=25,f"{q['id']}:context_limit");ck(q['content_license']==post.get('content_license') and bool(q['content_license']),f"{q['id']}:license");ck(q['date']==datetime.datetime.fromtimestamp(post['creation_date'],datetime.timezone.utc).date().isoformat(),f"{q['id']}:author_date");ck(q['source_class']=='qa_community' and q['evidence_kind']=='original_api_post',f"{q['id']}:class_kind");ck(q['speaker'] in speakers and q['stage'] in stages and q['type'] in types,f"{q['id']}:vocabulary");ck(all('`'+x+'`' in readme for x in q['themes']),f"{q['id']}:themes");ck(q['id'] in aa and aa[q['id']]['original_author']==post.get('owner'),f"{q['id']}:attribution");ck(aa[q['id']]['content_license']==q['content_license'] and aa[q['id']]['source_url']==q['url'],f"{q['id']}:attribution_fields")
 expected_op=True if cid is None and pid==qid else (post.get('owner',{}).get('user_id') is not None and post.get('owner',{}).get('user_id')==question.get('owner',{}).get('user_id'));ck(q['is_op']==expected_op,f"{q['id']}:is_op")
 if cid is not None:ck(post['post_id']==pid and q['url']==question['link']+f'#comment{cid}_{pid}',f"{q['id']}:comment_url")
 else:ck(q['url']==(question['link'] if pid==qid else f'https://parenting.stackexchange.com/a/{pid}'),f"{q['id']}:post_url")
 name=html.unescape(post.get('owner',{}).get('display_name',''));ck(not(name and len(name)>3 and name.lower() in (q['quote']+' '+q['context']).lower()),f"{q['id']}:author_name")
for key,words in budget.items():ck(words<=25,f'work_budget:{key}:{words}')
allids=[]
for p in (ROOT/'voice').glob('*.jsonl'):
 for q in read(p):allids.append(q['id'])
ck(len(allids)==len(set(allids)),'global_duplicate_quote_ids');ck(len(qids)==len(set(qids))==len(attrs),'quote_attribution_id_count')
qby=collections.defaultdict(list)
for q in quotes:qby[q['question_id']].append(q['id'])
reconciliation=[]
for t in triage:
 qid=int(t['id']);l=ll.get(qid);reconciliation.append({'question_id':qid,'title':ix[qid]['title'],'triage':t['label'],'job':t['job'],'read_status':'full_available_API_thread' if l else 'card_only_not_original_read','final_outcome':l['outcome'] if l else 'excluded_at_card_triage','answers_read':l['answers_read'] if l else 0,'comments_read':l['comments_read'] if l else 0,'quote_count':len(qby.get(qid,[])),'quote_ids':','.join(qby.get(qid,[])),'reason':l['reason'] if l else t['reason'],'raw_file':ix[qid]['raw_file']})
with (RAW/'reconciliation-qdeep01.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(reconciliation[0]),delimiter='\t');w.writeheader();w.writerows(reconciliation)
report={'date':'2026-10-24','cards':len(triage),'card_exclusions':len(triage)-len(kept),'initially_kept':len(kept),'full_available_api_threads_read':len(reads),'answers_read':sum(x['answers_read'] for x in ledger),'comments_read':sum(x['comments_read'] for x in ledger),'full_read_word_count':sum(len((ROOT/ix[x]['raw_file']).read_text().split()) for x in reads),'excluded_after_full_read':len(excluded),'retained_after_full_read':len(kept-excluded),'retained_originals_unread':sorted(kept-set(reads)),'quoted_questions':len(qby),'retained_without_quotes':sorted(kept-excluded-set(qby)),'quotes':len(quotes),'quoted_original_works':len(budget),'max_per_original_work_quoted_words':max(budget.values()),'max_context_words':max(len(x['context'].split()) for x in quotes),'failed':len(fail),'failures':fail,'voice_sha256':hashlib.sha256((ROOT/'voice/qa-deep-01.jsonl').read_bytes()).hexdigest(),'checks':['exact candidate/triage/read/exclusion ID sets','all saved answers/comments counted per fully read question','exact original author body excluding third-party blockquotes','exact preserved thread text, case and punctuation','aggregate 25-word maximum per individual original post/comment','context maximum, README vocabulary, existing themes','correct original URL/date/author attribution/license/is_op','quotes only on retained full reads','global quote ID uniqueness']}
(ROOT/'synthesis/qa-deep-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(fail))
