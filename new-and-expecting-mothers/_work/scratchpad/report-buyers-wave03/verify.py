# Research retains every subject in the speaker’s own words. The owner decides later what goes into copy; historical eligibility fields never restrict reading or quotation.
"""Read-only verification of the completed bounded buyer/seller wave."""
import collections,hashlib,html,json,re,subprocess,sys
from pathlib import Path
from urllib.parse import urlsplit
S=Path(__file__).resolve().parent;R=S.parents[1];W=R/'_raw/report-buyers-wave03'
def jl(p):return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s):return re.sub(r'\s+',' ',html.unescape(s)).strip()
def canon(u):
 x=urlsplit(u);return x.netloc.lower().removeprefix('www.')+x.path.rstrip('/')
def readbody(p):
 if p.suffix=='.json':return json.loads(p.read_text())['body']
 return p.read_text()
Q=jl(R/'voice/report-buyers-wave03.jsonl');L=jl(W/'reading.jsonl');T=jl(W/'testimonial-reading.jsonl');D={x['work_id']:x for x in L+T};errors=[];checks=collections.Counter()
def ck(ok,kind,detail):
 checks[kind]+=1
 if not ok:errors.append(dict(category=kind,detail=detail))
ck(len(Q)==len({q['id'] for q in Q})==7,'seven_distinct_quotes','rbw03-0001..0007')
ck(len(L)==5 and sum(x['source_control']=='seller_offer' for x in L)==4 and sum(x['source_control']=='affiliate_review' for x in L)==1,'retained_page_counts','4offers+1affiliate')
ck(all(x['complete_public_text_read'] is True for x in L),'complete_retained_reads','every retained accessible original')
ck(len(T)==len({x['work_id'] for x in T})==18 and all(x['complete_visible_review_read'] is True for x in T),'18_visible_testimonials','15BSA+3BabyPlanner, no carousel inflation')
for l in L+T:ck(sha(R/l['raw_file'])==l['sha256'],'original_unit_hash',l['work_id']);ck(not l.get('independently_inspected_buyer',l.get('independent_paid_written_only_buyer',False)),'no_independent_buyer_inference',l['work_id'])
base=json.loads((W/'pages/babysleepanswers-baby-rendered.json').read_text());expanded=json.loads((W/'pages/babysleepanswers-baby-expanded.json').read_text());chunks=json.loads((S/'bsa-reading-manifest.json').read_text());ck(''.join((S/c['file']).read_text() for c in chunks)==base['body'],'complete_BSA_reading_views','three intact views preserve complete initial body')
for c in chunks:ck(sha(S/c['file'])==c['sha256'],'BSA_view_hash',c['file'])
ck(len(expanded['faq'])==17,'expanded17FAQs','all read individually')
known=set(base['body'].splitlines())|{s for f in expanded['faq'] for s in f['full'].splitlines()};ck(all(s in known for s in expanded['body'].splitlines()),'expanded_body_read_coverage','no new rendered text beyond fully read base+FAQs')
for t in T:
 n=json.loads((R/t['raw_file']).read_text());p=R/n['origin_page_file'];origin=readbody(p) if p.suffix=='.json' else p.read_text();ck(origin[n['origin_body_start']:n['origin_body_end']]==n['body'],'native_testimonial_bounds',t['work_id']);ck(n['author']==t['author'] and n['claimed_review_date']==t['date'],'native_testimonial_metadata',t['work_id'])
allq=[x for f in (R/'voice').glob('*.jsonl') for x in jl(f)];globalids=[x['id'] for x in allq];readme=(R/'README.md').read_text()
def vocab(label):return set(re.findall(r'`([^`]+)`',readme.split(label+':',1)[1].split('\n\n',1)[0]))
sp=vocab('Speakers');st=vocab('Stages');ty=vocab('Types');th=vocab('Seed themes');budgets=collections.Counter();sources_by_canon={canon(q['url']) for q in Q};existing=[]
for q in Q:
 p=R/q['raw_file'];body=readbody(p);ck(q['id'].startswith('rbw03-') and globalids.count(q['id'])==1,'global_unique_quote_ID',q['id']);ck(q['speaker'] in sp and q['stage'] in st and q['type'] in ty and set(q['themes'])<=th,'README_vocab',q['id']);ck(len(q['context'].split())<=25,'context25',q['id']);ck(q['independent_buyer'] is False and q['standalone_customized_report_purchase_established'] is False,'source_restriction_flags',q['id']);ck(q['source_class']=='competitor' and q['work_id'] in D,'source_class_and_read_link',q['id']);ck('u/' not in q['quote']+q['context'] and q['author'] not in q['quote']+q['context'],'no_selected_author_names',q['id']);pos=0
 for part in q['quote'].split(' […] '):
  part=norm(part);at=norm(body).find(part,pos);ck(at>=0,'native_own_original_quote',q['id']);pos=at+len(part)
 if q['evidence_kind']=='seller_hosted_testimonial':
  n=json.loads(p.read_text());ck(q['author']==n['author'] and q['url']==n['source_url'] and q['date']==n['claimed_review_date'],'native_review_attribution',q['id'])
 elif q['evidence_kind']=='seller_claim':ck(q['date']=='' and q['observed_date']=='2026-10-24','unknown_seller_publication_date',q['id'])
 elif q['evidence_kind']=='affiliate_review':
  raw=(W/'pages/blunders-bsa-newborn-review.html').read_text();ck('2020-01-22T14:10:46-05:00' in raw and '2025-05-13T01:46:17-05:00' in raw and q['date']=='2020-01-22' and q['date_modified']=='2025-05-13','affiliate_native_dates',q['id'])
 budgets[canon(q['url'])]+=len(q['quote'].split())
for q in allq:
 if q['id'].startswith('rbw03-'):continue
 if canon(q.get('url','')) in sources_by_canon:existing.append(q['id']);budgets[canon(q['url'])]+=len(q['quote'].split())
ck(not existing,'no_existing_work_overlap',existing)
competitors=sorted((R/'competitors').glob('wave03-buyers-*.md'));ck(len(competitors)==4,'four_unique_competitor_notes','four serious retained offers')
notes=[R/'sources/report-buyers-wave03.md',R/'synthesis/reader-notes-report-buyers-wave03.md']+competitors;noteids=[]
for p in notes:
 text=p.read_text()
 for ident in re.findall(r'rbw03-\d{4}',text):noteids.append(ident);ck(ident in {q['id'] for q in Q},'note_ID_lookup',p.name+':'+ident)
 if p in competitors:
  mechanism=re.search(r'^Mechanism: (.+)$',text,re.M).group(1);ck(len(mechanism.split())<=8,'mechanism_eight_words',p.name)
  ident=re.search(r'Verified excerpt, (rbw03-\d{4})',text).group(1);q=next(q for q in Q if q['id']==ident);excerpts=re.findall(r'^> (.+)$',text,re.M);ck(excerpts==[q['quote']],'competitor_verified_quote',p.name);budgets[canon(q['url'])]+=sum(len(x.split()) for x in excerpts)
for u,n in budgets.items():ck(n<=25,'aggregate_nonReddit25_including_note_repeats',u+':'+str(n))
lead=jl(W/'unread-leads.jsonl');ck(len(lead)==15 and all(x['original_fully_read'] is False and x['new_quote_selected'] is False for x in lead),'exact_unread_lead_boundaries','15URLs')
policy=jl(W/'policy-review.jsonl');ck(len(policy)==10,'policy_decisions','ten domain decisions;9fresh plus saved Reddit')
search=json.loads((W/'search-manifest.json').read_text());ck(search['query_count']==sum(len(x['queries']) for x in search['query_batches'])==20 and len(search['query_batches'])==5,'search20_queries','discovery not original reading')
for b in search['query_batches']:ck((W/b['raw_response']).exists(),'saved_discovery_response',b['raw_response'])
ck(sum(q['evidence_kind']=='seller_claim' for q in Q)==4 and sum(q['evidence_kind']=='seller_hosted_testimonial' for q in Q)==2 and sum(q['evidence_kind']=='affiliate_review' for q in Q)==1,'evidence_kind_counts','4seller+2hosted+1affiliate')
strict=subprocess.run([sys.executable,str(R/'_tools/verify_quotes.py'),str(R/'voice/report-buyers-wave03.jsonl')],capture_output=True,text=True);ck(strict.returncode==0,'strict_verify_quotes',strict.stdout+strict.stderr)
files=[R/'voice/report-buyers-wave03.jsonl']+notes+list(W.glob('*.jsonl'))+[W/'search-manifest.json',W/'local-search-review.json']
audit=dict(date='2026-10-24',counts=dict(complete_retained_offer_pages=4,complete_affiliate_review_pages=1,full_visible_seller_hosted_testimonial_units=18,expanded_FAQ_answers=17,independent_original_buyer_accounts_read=0,standalone_customized_report_purchases_established=0,new_quotes=7,research_only_quotes=7,individual_competitor_notes=4,unread_discovery_lead_URLs=15,query_batches=5,queries=20,new_Reddit_full_read_credit=0,distinct_notes_IDs=len(set(noteids)),note_ID_occurrences=len(noteids)),checks=dict(checks),failed=len(errors),errors=errors,strict_exit_code=strict.returncode,strict_output=strict.stdout.strip(),nonReddit_quote_words_including_competitor_note_repeats=dict(budgets),source_classes=dict(collections.Counter(q['source_class'] for q in Q)),evidence_kinds=dict(collections.Counter(q['evidence_kind'] for q in Q)),output_sha256={str(p.relative_to(R)):sha(p) for p in files},raw_page_sha256={str((R/x['raw_file']).relative_to(R)):sha(R/x['raw_file']) for x in L},full_testimonial_sha256={x['work_id']:sha(R/x['raw_file']) for x in T},limitations=['No independently inspected paid standalone customized report transaction; index-only leads cannot resolve this gap.','No paid output, receipt, parent-input submission, private community or clinical outcome inspected.','Seller testimonials/affiliate reviews not independent buyer evidence.','Access limits and unread URLs explicit; no global absence or complete buyer-history claim.'])
(W/'verification.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:audit[k] for k in ['counts','failed','errors','strict_output','nonReddit_quote_words_including_competitor_note_repeats']},ensure_ascii=False,indent=2))
