import collections, hashlib, importlib.util, json, re
from pathlib import Path

P=Path(__file__).parent
spec=importlib.util.spec_from_file_location('reader',P/'ads_reader.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
manifests=[json.loads((P/s/'manifest.json').read_text()) for s in ['ads-reader-v1','ads-reader-wonder-v1']]
units=[u for m in manifests for u in m['units']]
rows=a.jl(a.L)
assert len(units)==len(rows)==199
assert len({u['ad_id'] for u in units})==len({r['ad_id'] for r in rows})==199
assert [r['ad_id'] for r in rows]==[u['ad_id'] for u in units]
cache={}
metrics=collections.defaultdict(lambda: {'read':0,'cards':0,'types':collections.Counter(),'statuses':collections.Counter(),'oldest_start_utc':None,'ad_ids':[],'destinations':[],'body_text_groups':set(),'all_text_groups':set()})
for u,r in zip(units,rows):
 p=a.R/u['capture_file']
 assert a.sha(p)==u['capture_sha256']==r['capture_sha256']
 if str(p) not in cache:cache[str(p)]=a.parse(p)
 d,x=cache[str(p)]
 ci,ei,ri=map(int,re.fullmatch(r'connections\[(\d+)\].edges\[(\d+)\].node.collated_results\[(\d+)\]',u['native_pointer']).groups())
 n=x['connections'][ci]['edges'][ei]['node']['collated_results'][ri]
 assert str(n['ad_archive_id'])==r['ad_id']==u['ad_id']
 assert str(n['page_id'])==str(d['expected_page_id'])==u['page_id']==r['page_id']
 snap=n['snapshot']
 tf={k:snap.get(k) for k in a.TEXT_KEYS}
 tf['cards']=[{k:c.get(k) for k in a.TEXT_KEYS if k in c} for c in snap.get('cards',[])]
 assert tf==u['text_fields']
 assert a.digest(tf)==r['text_fields_sha256']==u['text_fields_sha256']
 assert a.digest(snap)==r['snapshot_sha256']==u['snapshot_sha256']
 assert a.sha(a.R/u['unit_file'])==r['unit_sha256']==u['unit_sha256']
 assert r['native_body_and_all_card_text_read_complete'] is True and r['media_viewed'] is False
 assert n['is_active'] is True and r['is_active'] is True
 assert a.stamp(n['start_date'])==r['start_utc']
 for k in ['body','title','caption','link_description','link_url','cta_text']:
  assert tf[k]==snap.get(k)
 for i,c in enumerate(tf['cards']):
  for k,v in c.items():assert v==snap['cards'][i].get(k)
 links=list(dict.fromkeys(c['link_url'] for c in [tf]+tf['cards'] if c.get('link_url')))
 assert links==r['destination_urls']
 templ='{{' in json.dumps(tf,ensure_ascii=False)
 assert (r['text_status']=='body_template_cards_resolved')==templ
 assert snap.get('root_reshared_post') is None
 assert not snap.get('extra_texts') and not snap.get('extra_links')
 r['native_body_sha256']=a.digest(snap.get('body'))
 r['native_body_text_sha256']=hashlib.sha256((snap.get('body',{}).get('text') or '').encode()).hexdigest()
 r['native_all_card_text_sha256']=a.digest(tf['cards'])
 r['native_text_containment_verified']=True
 z=metrics[r['advertiser']];z['read']+=1;z['cards']+=len(tf['cards']);z['types'].update(r['offer_types']);z['statuses'][r['text_status']]+=1;z['page_id']=r['page_id'];z['ad_ids'].append(r['ad_id']);z['oldest_start_utc']=min(z['oldest_start_utc'] or r['start_utc'],r['start_utc']);z['body_text_groups'].add(a.digest(tf['body']));z['all_text_groups'].add(a.digest(tf))
 for link in links:
  if link not in z['destinations']:z['destinations'].append(link)
for m in manifests:
 for c in m['chunks']:assert a.sha(a.R/c['file'])==c['sha256']
for z in metrics.values():
 z['distinct_native_body_fields']=len(z.pop('body_text_groups'));z['distinct_complete_text_field_groups']=len(z.pop('all_text_groups'))
zero=[]
capture_counts=[]
for path,(d,x) in cache.items():
 native=[n for c in x['connections'] for e in c.get('edges',[]) for n in e['node'].get('collated_results',[])]
 assert all(str(n['page_id'])==str(d['expected_page_id']) for n in native)
 capture_counts.append({'file':str(Path(path).relative_to(a.R)),'native_connection_result_counts':[c.get('count') for c in x['connections']],'loaded_edges':sum(len(c.get('edges',[])) for c in x['connections']),'loaded_collated_ids':len(native),'has_next_page':[c.get('page_info',{}).get('has_next_page') for c in x['connections']],'rounded_visible_result_text':re.findall(r'~[0-9,]+ results',x.get('text',''))})
for f in ['044b-mothercould-page.json','045-busy-toddler-page.json']:
 p=a.Q/f;d,x=a.parse(p)
 native=[n for c in x['connections'] for e in c.get('edges',[]) for n in e['node'].get('collated_results',[])]
 assert not native and 'No ads match your search criteria' in x['text']
 zero.append({'capture_file':str(p.relative_to(a.R)),'sha256':a.sha(p),'expected_page_id':d['expected_page_id'],'query':d['query'],'captured_at':x['captured_at'],'url':x['url'],'native_ads':0,'visible_no_match':True})
a.L.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
out={'retained_native_ids':199,'fully_read_native_ids':199,'unread_native_ids':0,'failures':0,'body_and_card_strings_exact_native_containment':True,'source_hashes_verified':True,'duplicate_ids':0,'media_viewed':0,'ledger_sha256':a.sha(a.L),'metrics':dict(metrics),'zero_pages':zero,'capture_counts':capture_counts,'scope_limit':'All retained loaded native text on seven exact Page captures; not every Library result, creative image/video, or campaign.'}
(P/'ads-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['metrics','zero_pages']},indent=2))
for name,z in metrics.items():print(name,z['read'],dict(z['types']),dict(z['statuses']),'cards',z['cards'],'oldest',z['oldest_start_utc'])
