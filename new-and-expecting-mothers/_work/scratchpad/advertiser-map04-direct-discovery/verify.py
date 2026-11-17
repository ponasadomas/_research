import collections, datetime, hashlib, json, re, urllib.parse, urllib.robotparser
from pathlib import Path

S=Path(__file__).parent;R=S.parents[1];W=R/'_raw/advertiser-map04-direct-discovery'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def parse(p):
 d=json.loads(p.read_text());t='\n'.join(c['text'] for c in d['browser_response']['content'] if c.get('type')=='text');return d,json.loads(re.search(r'```json\s*(.*?)\s*```',t,re.S)[1])
m=json.loads((S/'native-manifest.json').read_text());rows=[json.loads(l) for l in (R/'sources/advertiser04-direct-discovery-reading.jsonl').read_text().splitlines()];ix=collections.defaultdict(list);cache={}
for u in m['units']:
 p=R/u['capture_file'];assert sha(p)==u['capture_sha256']
 if str(p) not in cache:cache[str(p)]=parse(p)
 d,x=cache[str(p)];ci,ei,ri=map(int,re.fullmatch(r'connections\[(\d+)\].edges\[(\d+)\].node.collated_results\[(\d+)\]',u['native_pointer']).groups());n=x['connections'][ci]['edges'][ei]['node']['collated_results'][ri];sn=n['snapshot']
 assert str(n['ad_archive_id'])==u['ad_id'] and str(n['page_id'])==u['page_id'] and n['is_active'] is True
 assert u['page_id'] in {'124737507587747','482750678569835'}
 tf={k:sn.get(k) for k in m['keys']};tf['cards']=[{k:c.get(k) for k in m['keys'] if k in c} for c in sn['cards']]
 assert tf==u['text_fields'] and digest(tf)==u['text_fields_sha256'] and digest(sn)==u['snapshot_sha256']
 assert hashlib.sha256((sn['body']['text'] or '').encode()).hexdigest()==u['native_body_text_sha256']
 assert not sn['extra_texts'] and not sn['extra_links'] and sn['root_reshared_post'] is None
 for i,c in enumerate(tf['cards']):
  for k,v in c.items():assert v==sn['cards'][i].get(k)
 ix[u['ad_id']].append(u)
assert len(m['units'])==24 and len(ix)==len(rows)==22 and len({r['ad_id'] for r in rows})==22 and {r['ad_id'] for r in rows}==set(ix)
for r in rows:
 os=ix[r['ad_id']];assert len(os)==r['occurrence_count'];assert r['native_body_and_all_card_text_read_complete'] and r['all_occurrences_full_text_read'] and not r['media_viewed']
 assert r['source_occurrences']==[{k:v for k,v in u.items() if k!='text_fields'} for u in os]
 assert len({u['text_fields_sha256'] for u in os})==1
 links=list(dict.fromkeys(c['link_url'] for u in os for c in [u['text_fields']]+u['text_fields']['cards'] if c.get('link_url')));assert links==r['destination_urls']
for v in json.loads((S/'views-manifest.json').read_text()):assert sha(R/v['file'])==v['sha256']
page=[u for u in m['units'] if u['capture_file'].endswith('069-goodinside-baby-page.json')];assert len(page)==21
d,x=cache[str(R/page[0]['capture_file'])];assert d['expected_page_id']=='482750678569835' and [c['count'] for c in x['connections']]==[21]
native_ids=[str(n['ad_archive_id']) for c in x['connections'] for e in c['edges'] for n in e['node']['collated_results']];assert set(native_ids)=={u['ad_id'] for u in page} and len(native_ids)==21
source_metas=[]
for p in sorted(W.glob('*.meta.json')):
 meta=json.loads(p.read_text());assert meta['status']==200 and sha(R/meta['raw_file'])==meta['sha256'];source_metas.append({'meta_file':str(p.relative_to(R)),'raw_file':meta['raw_file'],'sha256':meta['sha256'],'status':meta['status'],'date_utc':meta['date_utc']})
 if not p.name.startswith('robots-'):
  domain=urllib.parse.urlsplit(meta['requested_url']).netloc;robot=json.loads((W/f'robots-{domain}.meta.json').read_text());rp=urllib.robotparser.RobotFileParser();rp.parse((R/robot['raw_file']).read_text().splitlines());assert all(rp.can_fetch(agent,meta['requested_url']) for agent in ['*','GPTBot','ChatGPT-User','OAI-SearchBot'])
assert len(source_metas)==13
price=json.loads((W/'goodinside-public-bundle-price.body').read_text());assert price['amount']==17500
client=(W/'goodinside-checkout-client.body').read_text();assert 'currency:"USD"' in client and '.format(e/100)' in client and '/api/stripe/get-purchasable-item-price/?id=' in client
old=json.loads((R/'scratchpad/advertiser-map04-sleep-play/ads-freeze.json').read_text());assert all(sha(R/x['file'])==x['sha256'] for x in old['files'])
out={'verified_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'failures':0,'unique_native_ads':22,'fully_read_unique_ads':22,'source_occurrences':24,'fully_read_occurrences':24,'unread_unique_ads':0,'duplicate_discovery_occurrences_collapsed':2,'Good_Inside_Page_reported_native_count':21,'Good_Inside_Page_loaded_retained_read':21,'Good_Inside_Page_cards':sum(len(u['text_fields']['cards']) for u in page),'all_occurrence_cards_read_including_repeats':sum(len(u['text_fields']['cards']) for u in m['units']),'media_viewed':0,'source_response_hashes_verified':source_metas,'prior_frozen_file_hashes_unchanged':len(old['files']),'bundle_base_price':{'amount_minor_units':17500,'currency':'USD','amount_major_units':175,'method':'Public checkout client GET price response plus same client USD cents formatter; no payment action'},'ledger_sha256':sha(R/'sources/advertiser04-direct-discovery-reading.jsonl')}
(S/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='source_response_hashes_verified'},indent=2))
