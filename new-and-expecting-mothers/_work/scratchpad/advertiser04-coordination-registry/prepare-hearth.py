from pathlib import Path
import json,re,hashlib
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;D=R/'_raw/advertiser-census-wave04-2026-10-25/queries'
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
specs=[('054-hearth-page.json',11)]
fields=['caption','cta_text','cta_type','title','link_description','link_url','display_format','byline','disclaimer_label','additional_info','extra_links','extra_texts','branded_content','root_reshared_post']
cardfields=['body','caption','title','link_description','cta_text','cta_type','link_url','display_format']
units=[];parts=[]
for file,count in specs:
 p=D/file;x=json.loads(p.read_text());o=json.loads(re.search(r'```json\n([\s\S]*?)\n```',x['browser_response']['content'][0]['text']).group(1));ads=[z for con in o['connections'] for edge in con['edges'] for z in edge['node']['collated_results']]
 assert len(ads)==count
 displayed=dict(re.findall(r'Library ID: (\d+)\nStarted running on ([^\n]+)',o['text']))
 for a in ads:
  id=str(a['ad_archive_id']);n=a['snapshot'];assert str(a['page_id'])==str(x['expected_page_id'])
  body=n.get('body',{});body=body.get('text','') if isinstance(body,dict) else (body or '')
  bundle=dict(body=body,top={k:n[k] for k in fields if k in n},cards=[{k:z[k] for k in cardfields if k in z} for z in n.get('cards',[])])
  # Check for unexpected textual card fields so none is silently omitted.
  extras=set().union(*(set(z)-set(cardfields) for z in n.get('cards',[]))) if n.get('cards') else set()
  assert all(any(t in k.lower() for t in ['image','video']) for k in extras),extras
  bp=S/'units'/f'{id}.json';bp.parent.mkdir(exist_ok=True);assert not bp.exists()
  meta=dict(ad_id=id,page_id=str(a['page_id']),page_name=a['page_name'],snapshot_page_id=str(n.get('page_id')),snapshot_page_name=n.get('page_name'),snapshot_identity_differs=str(n.get('page_id'))!=str(a['page_id']),source_file=str(p.relative_to(R)),source_file_sha256=H(p),captured_at=o['captured_at'],native_is_active=a['is_active'],start_timestamp=a['start_date'],start_utc=datetime.fromtimestamp(a['start_date'],timezone.utc).isoformat() if a.get('start_date') else None,displayed_start_date=displayed.get(id),collation_id=a.get('collation_id'),collation_count=a.get('collation_count'),display_format=n.get('display_format'),primary_destination=n.get('link_url'),card_destinations=[z.get('link_url') for z in n.get('cards',[])],native_body_sha256=hashlib.sha256(body.encode()).hexdigest(),native_text_bundle_sha256=hashlib.sha256(json.dumps(bundle,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),native_ad_sha256=hashlib.sha256(json.dumps(a,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),text_bundle=bundle,excluded_card_media_fields=sorted(extras))
  bp.write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n');meta['unit_file']=str(bp.relative_to(R));meta['unit_sha256']=H(bp);units.append(meta)
  view='\n=== AD '+id+' | '+a['page_name']+' | PAGE '+str(a['page_id'])+' ===\nSTART '+str(meta['start_utc'])+' | DISPLAYED '+str(meta['displayed_start_date'])+'\nSOURCE '+file+'\nSNAPSHOT PAGE '+str(n.get('page_id'))+' | '+str(n.get('page_name'))+'\nBODY\n'+body+'\nTOP TEXT / DESTINATION\n'+json.dumps(bundle['top'],ensure_ascii=False,indent=2)+'\nALL CARDS ('+str(len(bundle['cards']))+')\n'+json.dumps(bundle['cards'],ensure_ascii=False,indent=2)+'\n'
  parts.append((meta,view))
assert len(units)==len({x['ad_id'] for x in units})==11
chunks=[];cur=[];size=0
for u,text in parts:
 if cur and (size+len(text.encode())>15000 or cur[-1][0]['page_name']!=u['page_name']):chunks.append(cur);cur=[];size=0
 cur.append((u,text));size+=len(text.encode())
if cur:chunks.append(cur)
views=[]
for i,c in enumerate(chunks,20):
 p=S/f'read-{i:02}.txt';assert not p.exists();p.write_text(''.join(z for _,z in c));views.append(dict(file=str(p.relative_to(R)),ad_ids=[u['ad_id'] for u,_ in c],sha256=H(p),bytes=p.stat().st_size,page_name=c[0][0]['page_name']))
(S/'extension-manifest.json').write_text(json.dumps(dict(source_specs=specs,units=[{k:v for k,v in u.items() if k!='text_bundle'} for u in units],views=views),ensure_ascii=False,indent=2)+'\n')
print(json.dumps(dict(ads=len(units),chunks=len(views),views=views),indent=2))
