from pathlib import Path
import json,re,hashlib,datetime,sys
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/advertiser04-food-safety-ads';D=R/'_raw/advertiser-census-wave04-2026-10-25/queries'
NAMES=['006-solid-starts-page.json','007-village-page.json','031b-feeding-littles-page.json','032-kids-eat-color-page.json','034b-little-lunches-page.json','035-blw-meals-page.json','036-boob-food-page.json','037b-101beforeone-page.json','038-safe-beginnings-page.json','039-tinyhood-page.json']
def parse(f):
 x=json.loads(f.read_text());p=[]
 for c in x['browser_response']['content']:
  m=re.search(r'```json\s*([\s\S]*?)\s*```',c.get('text',''))
  if m:p.append(json.loads(m.group(1)))
 assert len(p)==1;return x,p[0]
def textpart(s):
 keys=['byline','disclaimer_label','caption','cta_text','cta_type','display_format','body','title','link_description','link_url','extra_texts','extra_links','additional_info','event']
 o={k:s[k] for k in keys if s.get(k) not in [None,'',[],{}]};o['cards']=[{k:v for k,v in c.items() if k in ['body','title','caption','cta_type','cta_text','link_description','link_url'] and v not in [None,'',[],{}]} for c in s.get('cards',[])];return o
if __name__=='__main__':
 phase=sys.argv[1] if len(sys.argv)>1 else 'full-read-v1';names=NAMES if len(sys.argv)<3 else sys.argv[2:];V=S/phase;V.mkdir(exist_ok=False);pages=[];units=[]
 for name in names:
  f=D/name;x,p=parse(f);page=dict(file=str(f.relative_to(R)),sha256=hashlib.sha256(f.read_bytes()).hexdigest(),query=x['query'],expected_page_id=x.get('expected_page_id'),library_url=p['url'],captured_at=p.get('captured_at'),connections=[dict(count=c.get('count'),edge_count=len(c.get('edges',[])),page_info=c.get('page_info')) for c in p.get('connections',[])],ad_ids=[]);seen=set()
  for ci,c in enumerate(p.get('connections',[])):
   for ei,e in enumerate(c.get('edges',[])):
    for ri,n in enumerate(e.get('node',{}).get('collated_results',[])):
     aid=n['ad_archive_id'];assert aid not in seen,(name,aid);seen.add(aid);z=n['snapshot'];tp=textpart(z);start=n.get('start_date');end=n.get('end_date');unit=dict(ad_id=aid,page_name=z.get('page_name',n.get('page_name')),page_id=n.get('page_id'),snapshot_page_id=z.get('page_id'),is_active=n.get('is_active'),collation_id=n.get('collation_id'),collation_count=n.get('collation_count'),native_start_date=start,start_utc=datetime.datetime.fromtimestamp(start,datetime.timezone.utc).isoformat() if start else None,native_end_date=end,end_utc=datetime.datetime.fromtimestamp(end,datetime.timezone.utc).isoformat() if end else None,publisher_platform=n.get('publisher_platform'),media_count=dict(videos=len(z.get('videos',[])),images=len(z.get('images',[])),cards=len(z.get('cards',[]))),media_viewed=False,text=tp,raw_file=page['file'],raw_sha256=page['sha256'],native_locator=dict(connection=ci,edge=ei,collated_result=ri),snapshot_sha256=hashlib.sha256(json.dumps(z,sort_keys=True,ensure_ascii=False).encode()).hexdigest());units.append(unit);page['ad_ids'].append(aid)
  pages.append(page)
 views=[];parts=[];ids=[]
 def flush():
  global parts,ids
  if not ids:return
  f=V/f'{len(views)+1:03d}.txt';f.write_text(''.join(parts));views.append(dict(view=len(views)+1,file=str(f.relative_to(R)),ad_ids=ids[:],bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()));parts=[];ids=[]
 for u in units:
  t=json.dumps(u,indent=2,ensure_ascii=False)+'\n\n'
  if parts and sum(map(len,parts))+len(t)>13500:flush()
  parts.append(t);ids.append(u['ad_id'])
 flush();(V/'units.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in units));(V/'manifest.json').write_text(json.dumps(dict(scope='All loaded native original ad text/card headlines/CTAs/destinations; no media view or pagination. No new collection.',pages=pages,units=len(units),views=views),indent=2)+'\n');print('VIEWS',[(v['view'],len(v['ad_ids']),v['bytes']) for v in views]);print('PAGES',[(p['query'],len(p['ad_ids'])) for p in pages])
