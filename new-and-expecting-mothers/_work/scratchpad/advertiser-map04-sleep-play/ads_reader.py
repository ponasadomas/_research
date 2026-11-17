import collections,datetime,hashlib,json,re,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent/'ads-reader-v1';Q=R/'_raw/advertiser-census-wave04-2026-10-25/queries';L=R/'sources/advertiser04-sleep-play-reading.jsonl'
FILES=['002-huckleberry-page.json','003-babysparks-page.json','004-kinedu-english-page.json','005-lovevery-page.json','019-taking-cara-babies-page.json','020-napper-page.json']
TEXT_KEYS=['body','title','caption','link_description','link_url','cta_text','cta_type','byline','disclaimer_label','event','extra_texts','extra_links','additional_info']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(v):return hashlib.sha256(json.dumps(v,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
def stamp(v):return datetime.datetime.fromtimestamp(int(v),datetime.timezone.utc).isoformat() if v else None
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []
def parse(p):
 d=json.loads(p.read_text());t='\n'.join(v['text'] for v in d['browser_response']['content'] if v.get('type')=='text');return d,json.loads(re.search(r'```json\s*(.*?)\s*```',t,re.S)[1])
def prepare():
 target=S/'manifest.json';assert not target.exists();(S/'units').mkdir(parents=True);(S/'chunks').mkdir();units=[];caps=[]
 for name in FILES:
  p=Q/name;d,x=parse(p);assert d['kind']=='advertiser_page';records=[]
  for ci,c in enumerate(x['connections']):
   for ei,e in enumerate(c.get('edges',[])):
    for ri,n in enumerate(e['node'].get('collated_results',[])):
     if str(n['page_id'])!=str(d['expected_page_id']):continue
     snap=n['snapshot'];text={k:snap.get(k) for k in TEXT_KEYS};text['cards']=[{k:c.get(k) for k in TEXT_KEYS if k in c} for c in snap.get('cards',[])];adid=str(n['ad_archive_id']);u={'ad_id':adid,'advertiser':n['page_name'],'page_id':str(n['page_id']),'capture_file':str(p.relative_to(R)),'capture_sha256':sha(p),'native_pointer':f'connections[{ci}].edges[{ei}].node.collated_results[{ri}]','capture_url':x['url'],'captured_at':x['captured_at'],'is_active':n['is_active'],'start_utc':stamp(n['start_date']),'display_format':snap.get('display_format'),'ad_library_url':'https://www.facebook.com/ads/library/?id='+adid,'snapshot_sha256':digest(snap),'text_fields':text,'text_fields_sha256':digest(text),'media_seen':False,'image_count':len(snap.get('images',[])),'video_count':len(snap.get('videos',[])),'cards_count':len(snap.get('cards',[]))}
     unit=S/'units'/f'{name[:3]}-{adid}.json';assert not unit.exists();unit.write_text(json.dumps(u,ensure_ascii=False,indent=2)+'\n');u.update(unit_file=str(unit.relative_to(R)),unit_sha256=sha(unit));units.append(u);records.append(adid)
  caps.append({'file':str(p.relative_to(R)),'sha256':sha(p),'expected_page_id':d['expected_page_id'],'advertiser':d['query'],'captured_at':x['captured_at'],'ad_ids':records})
 assert len(units)==len({u['ad_id'] for u in units})==176
 chunks=[];parts=[];ids=[];size=0
 def flush():
  nonlocal parts,ids,size
  if not ids:return
  p=S/'chunks'/f'{len(chunks)+1:03d}.txt';p.write_text('\n\n'.join(parts)+'\n');chunks.append({'file':str(p.relative_to(R)),'sha256':sha(p),'ad_ids':ids});parts=[];ids=[];size=0
 for u in units:
  v={k:u[k] for k in ['ad_id','advertiser','page_id','start_utc','display_format','cards_count','image_count','video_count']};part='AD '+json.dumps(v,ensure_ascii=False)+'\nALL NATIVE TEXT FIELDS AND DESTINATIONS\n'+json.dumps(u['text_fields'],ensure_ascii=False,indent=2)
  if size+len(part.encode())>22000:flush()
  parts.append(part);ids.append(u['ad_id']);size+=len(part.encode())+2
 flush();target.write_text(json.dumps({'scope':'All loaded collated native records on six selected advertiser_page captures; no broad keyword captures, no media viewed','captures':caps,'units':units,'ad_ids':[u['ad_id'] for u in units],'chunks':chunks},ensure_ascii=False,indent=2)+'\n');print('ads',len(units),'chunks',len(chunks),'max_bytes',max((R/c['file']).stat().st_size for c in chunks))
def read(n):
 m=json.loads((S/'manifest.json').read_text());c=m['chunks'][n-1];assert sha(R/c['file'])==c['sha256'];print((R/c['file']).read_text(),end='')
def save(n,text):
 m=json.loads((S/'manifest.json').read_text());c=m['chunks'][n-1];ix={u['ad_id']:u for u in m['units']};spec=[l.split('|',3) for l in text.strip().splitlines()];assert [x[0] for x in spec]==c['ad_ids'];prev=jl(L);assert not {x[0] for x in spec}&{x['ad_id'] for x in prev}
 for adid,types,status,reason in spec:
  formats=types.split(',');assert set(formats)<={'app','course','custom_report_bundle','free_lead','physical','general_digital','brand_unspecified','unresolved'} and status in {'resolved','body_template_cards_resolved','template_unresolved','empty'} and reason.strip();u=ix[adid];links=[]
  for record in [u['text_fields']]+u['text_fields']['cards']:
   if record.get('link_url') and record['link_url'] not in links:links.append(record['link_url'])
  row={k:u[k] for k in ['ad_id','advertiser','page_id','capture_file','capture_sha256','native_pointer','capture_url','captured_at','is_active','start_utc','ad_library_url','snapshot_sha256','text_fields_sha256','unit_file','unit_sha256','cards_count']};row.update(native_body_and_all_card_text_read_complete=True,offer_types=formats,text_status=status,reason=reason,destination_urls=links,media_viewed=False,media_status='images and video not viewed; no imagery or playback inference',reading_chunk=c['file'])
  with L.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 now=jl(L);print('read',len(now),'of',len(m['ad_ids']),dict(collections.Counter(x['advertiser'] for x in now)))
if __name__=='__main__':
 if sys.argv[1]=='prepare':prepare()
 elif sys.argv[1]=='read':read(int(sys.argv[2]))
 elif sys.argv[1]=='save':save(int(sys.argv[2]),sys.stdin.read())
