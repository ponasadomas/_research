from pathlib import Path
import json,re,hashlib,collections,datetime,sys
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/advertiser04-meal-guides';W=R/'_raw/advertiser04-meal-guides';OUT=R/'sources/advertiser04-meal-guides-reading.jsonl';E=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def chk(b,msg):
 if not b:E.append(msg)
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
I=rows(W/'native-selected.jsonl')+rows(W/'native-page-units.jsonl');native={};byid=collections.defaultdict(list)
for u in I:
 byid[u['ad_id']].append(u);native[u['ad_id']]=u;chk(sha(R/u['source_raw'])==u['source_sha256'],'source hash '+u['ad_id']);w=json.loads((R/u['source_raw']).read_text());p=json.loads(re.search(r'```json\s*([\s\S]*?)\s*```',w['browser_response']['content'][0]['text']).group(1));q=u['native_locator'];n=p['connections'][q['connection']]['edges'][q['edge']]['node']['collated_results'][q['collated_result']];z=n['snapshot'];chk(n['ad_archive_id']==u['ad_id'] and n['page_id']==u['advertiser_page_id'],'native ad/page '+u['ad_id']);chk(u['snapshot_page_id']==z['page_id'] and u['branded_content']==z.get('branded_content'),'creator metadata '+u['ad_id']);chk(u['start_date']==n['start_date'] and u['start_utc']==datetime.datetime.fromtimestamp(n['start_date'],datetime.timezone.utc).isoformat(),'start '+u['ad_id']);chk(u['text']['body']==z['body'],'body native '+u['ad_id']);expected={k:z[k] for k in ['body','title','caption','link_description','cta_text','cta_type','display_format','link_url','extra_texts','extra_links','byline','disclaimer_label'] if z.get(k) not in [None,'',[],{}]};expected['cards']=[{k:v for k,v in q.items() if k in ['body','title','caption','link_description','cta_text','cta_type','link_url'] and v not in [None,'',[],{}]} for q in z.get('cards',[])];chk(u['text']==expected,'all native text fields '+u['ad_id'])
for a,uu in byid.items():chk(len({hashlib.sha256(json.dumps(u['text'],sort_keys=True,ensure_ascii=False).encode()).hexdigest() for u in uu})==1,'same-ID text changed '+a)
rr=rows(OUT);chk(len(rr)==len({r['ad_id'] for r in rr})==33,'33 unique ledger');chk({r['ad_id'] for r in rr}==set(native),'exact selected union');chk(sum(len(r['source_occurrences']) for r in rr)==42,'42 occurrences');chk(all(r.get('page_capture_read_complete') and r['body_and_all_loaded_text_read'] and not r['media_viewed'] for r in rr),'fullread flags')
for r in rr:
 a=r['ad_id'];u=native[a];chk(r['body_sha256']==hashlib.sha256(u['text']['body']['text'].encode()).hexdigest(),'body sha '+a);chk(r['text_sha256']==hashlib.sha256(json.dumps(u['text'],sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'text sha '+a);chk(r['advertiser_page_id']==u['advertiser_page_id'] and r['snapshot_page_id']==u['snapshot_page_id'],'ledger identity '+a);chk(len(r['source_occurrences'])==len(byid[a]),'occurrence attribution '+a)
for log in rows(S/'ad-reading-progress.jsonl'):
 chk(sha(R/log['file'])==log['sha256'],'read view hash '+log['file']);v=(R/log['file']).read_text()
 for a in log['ad_ids']:
  b=native[a]['text']['body']['text'];chk(b in v or json.dumps(b,ensure_ascii=False) in v,'all body displayed '+a)
chk(len(rows(S/'ad-reading-progress.jsonl'))==6,'six read views')
A=rows(W/'access.jsonl')
for a in A:
 if a.get('raw_file'):chk(sha(R/a['raw_file'])==a['sha256'],'HTTP hash '+a['slug'])
old=R/'scratchpad/advertiser04-food-safety-ads/final-freeze.json';F=json.loads(old.read_text());oldbad=[x['file'] for x in F['files'] if sha(R/x['file'])!=x['sha256']];chk(not oldbad,'prior149 frozen changed')
M=json.loads((S/'page-ad-read-manifest.json').read_text());summary=[]
for p in M['pages']:
 r=[x for x in rr if x['advertiser_page_id']==p['expected_page_id']];summary.append(dict(page_id=p['expected_page_id'],query=p['query'],reported_counts=[c['count'] for c in p['connections']],captured_native_count=len(r),read_ad_ids=[x['ad_id'] for x in r],promotion_counts=dict(collections.Counter(x['promoted_offer'] for x in r)),oldest_observed_active_start=min(x['start_utc'] for x in r),creator_partner_records=sum(bool(x['branded_content']) for x in r),different_snapshot_page_records=sum(x['snapshot_page_id']!=x['advertiser_page_id'] for x in r),source_raw=p['raw_file'],source_sha256=p['sha256'],page_info=[x['page_info'] for x in p['connections']]))
(S/'final-page-coverage.json').write_text(json.dumps(summary,indent=2)+'\n');o=dict(unique_native_ad_ids=33,full_native_texts_read=33,unread_native_ids=[],snapshot_occurrences_read=42,duplicate_discovery_occurrences=9,duplicate_same_ID_text_changes=0,new_voice_quotes=0,media_viewed=0,current_offer_HTTP200=sum(a.get('status')==200 for a in A),unresolved_policy_transport_probes=sum(a.get('status') is None for a in A),prior149_frozen_files_verified=len(F['files']),prior149_hash_failures=oldbad,checks_failed=len(E),errors=E,utc=datetime.datetime.now(datetime.timezone.utc).isoformat());(S/'verification.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));print('PAGES',json.dumps(summary,indent=2));sys.exit(bool(E))
