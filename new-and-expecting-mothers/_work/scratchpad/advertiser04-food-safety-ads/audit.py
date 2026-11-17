from pathlib import Path
import json,hashlib,collections,datetime,re,sys
from prepare import parse,textpart
from reader import records,R,S,OUT
E=[]
def chk(x,msg):
 if not x:E.append(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((S/'full-read-v1/manifest.json').read_text());ext=json.loads((S/'extension-v3/manifest.json').read_text());pages=base['pages']+ext['pages'];native={};pageby={};zero=[];summaries=[]
for p in pages:
 chk(sha(R/p['file'])==p['sha256'],'source hash '+p['file']);w,b=parse(R/p['file']);ids=[];groups=set();reports=[]
 for c in b.get('connections',[]):
  reports.append(c.get('count'))
  for ei,e in enumerate(c.get('edges',[])):
   for ri,n in enumerate(e.get('node',{}).get('collated_results',[])):
    a=n['ad_archive_id'];chk(a not in native,'duplicate retained ID '+a);native[a]=n;pageby[a]=p;ids.append(a);groups.add(n.get('collation_id'));chk(n.get('page_id')==p['expected_page_id'],'native advertiser identity '+a)
 chk(ids==p['ad_ids'],'frozen page ordered IDs '+p['file'])
 if not ids:zero.append(p)
 summaries.append(dict(query=p['query'],page_id=p['expected_page_id'],file=p['file'],source_sha256=p['sha256'],captured_at=p['captured_at'],reported_counts=reports,loaded_native_ids=ids,loaded_native_count=len(ids),loaded_collation_groups=len(groups),page_info=[c.get('page_info') for c in p['connections']]))
rr=records(OUT);chk(len(rr)==len({r['ad_id'] for r in rr})==149,'exact149 distinct ledger');chk(set(native)=={r['ad_id'] for r in rr},'all retained149 native IDs read');supp=json.loads((S/'partner-metadata-supplement.json').read_text());sp={x['ad_id']:x for x in supp['partner_or_different_snapshot_records']}
for r in rr:
 a=r['ad_id'];n=native[a];z=n['snapshot'];t=textpart(z);b=z.get('body',{});b=b.get('text','') if isinstance(b,dict) else b or '';p=pageby[a];chk(r['body_and_all_loaded_card_headline_text_read'] and r['cta_and_destinations_read'],'read flags '+a);chk(r['body_sha256']==hashlib.sha256(b.encode()).hexdigest(),'native body hash '+a);chk(r['all_text_sha256']==hashlib.sha256(json.dumps(t,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'all native text fields hash '+a);chk(r['snapshot_sha256']==hashlib.sha256(json.dumps(z,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),'full snapshot hash '+a);chk(r['source_sha256']==p['sha256'] and r['raw_file']==p['file'],'source attribution '+a);chk(r['page_id']==n['page_id'] and r['snapshot_page_id']==z['page_id'],'advertiser/creator IDs '+a);chk(r['native_start_date']==n.get('start_date') and r['start_utc']==datetime.datetime.fromtimestamp(n['start_date'],datetime.timezone.utc).isoformat(),'native start date '+a);chk(r['is_active']==n['is_active'],'active flag '+a);chk(not r['media_viewed'] and not r['creative_variants_complete'] and not r['full_advertiser_library_complete'],'bounded scope '+a)
 dest=list(dict.fromkeys(v for v in [t.get('link_url')]+[x.get('link_url') for x in t.get('cards',[])]+[x if isinstance(x,str) else x.get('url') for x in t.get('extra_links',[])] if v));chk(r['destinations']==dest,'all destinations '+a)
 r.update(advertiser_page_name=n.get('page_name'),branded_content=z.get('branded_content'),partner_metadata_reviewed=True,exact_native_text_fields_verified=True)
 if a in sp:r['partner_identity_note']='Native advertiser and displayed creator/partner identities preserved separately; not independent customer testimony.'
# Enrichment only, no ad ID/source/text/category changes.
OUT.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rr))
for phase,count in [('full-read-v1',6),('full-read-v2',84),('extension-lean-v4',59)]:
 m=json.loads((S/phase/'manifest.json').read_text());u={x['ad_id']:x for x in records(S/phase/'units.jsonl')};readlog=[x for x in records(S/'reading-progress.jsonl') if x['phase']==phase];chk(sum(len(x['ad_ids']) for x in readlog)==count,'phase human read count '+phase)
 for c in readlog:
  chk(sha(R/c['file'])==c['view_sha256'],'human read packet hash '+c['file']);v=(R/c['file']).read_text()
  for a in c['ad_ids']:
   chk(u[a]['text']==textpart(native[a]['snapshot']),'preserved native text '+a)
   t=u[a]['text'];b=t.get('body',{});b=b.get('text','') if isinstance(b,dict) else b or '';chk(b in v or json.dumps(b,ensure_ascii=False) in v,'complete body in read packet '+a)
   for k in ['caption','title','link_description','link_url','cta_text']:
    if isinstance(t.get(k),str):chk(t[k] in v,'headline/CTA/destination in packet '+a+' '+k)
   for card in t.get('cards',[]):
    for k,cv in card.items():
     if isinstance(cv,str):chk(cv in v,'complete card field in packet '+a+' '+k)
chk(len(records(S/'reading-progress.jsonl'))==18,'18 actually read packets')
for s in summaries:
 x=[r for r in rr if r['page_id']==s['page_id']];s['full_native_texts_read']=len(x);s['unread_native_ad_ids']=[];s['promoted_offer_counts']=dict(collections.Counter(r['promoted_offer'] for r in x));s['promoted_job_counts']=dict(collections.Counter(r['promoted_job'] for r in x));s['oldest_observed_active_start']=min([r['start_utc'] for r in x if r['is_active']] or [None]);s['newest_observed_active_start']=max([r['start_utc'] for r in x if r['is_active']] or [None]);s['creator_or_partner_ad_ids']=[r['ad_id'] for r in x if r.get('branded_content') or r['page_id']!=r['snapshot_page_id']]
(S/'zero-native-pages.json').write_text(json.dumps(zero,indent=2)+'\n');(S/'final-page-coverage.json').write_text(json.dumps(summaries,indent=2)+'\n')
G=collections.defaultdict(list)
for r in rr:G[r['all_text_sha256']].append(r['ad_id'])
(S/'repeated-copy-groups.json').write_text(json.dumps(dict(scope='Exact full text+destination field repetition among loaded native IDs, not independent customers or creative spend.',groups=[v for v in G.values() if len(v)>1]),indent=2)+'\n')
V=dict(retained_native_ad_ids=149,full_native_texts_read=149,unread_native_ids=[],zero_native_pages=len(zero),source_page_captures=len(pages),positive_pages=sum(bool(p['ad_ids']) for p in pages),new_voice_quotes=0,media_viewed=0,partner_metadata_records_reviewed=len(sp),native_text_hashes_checked=149,body_hashes_checked=149,all_ids_unique=True,all_source_page_id_checks_passed=not any('identity' in e for e in E),promotion_counts=dict(collections.Counter(r['promoted_offer'] for r in rr)),checks_failed=len(E),errors=E,utc=datetime.datetime.now(datetime.timezone.utc).isoformat());(S/'verification.json').write_text(json.dumps(V,indent=2)+'\n');print(json.dumps(V,indent=2));print('BRANDS',[(x['query'],x['reported_counts'],x['loaded_native_count'],x['promoted_offer_counts'],x['oldest_observed_active_start']) for x in summaries]);sys.exit(bool(E))
