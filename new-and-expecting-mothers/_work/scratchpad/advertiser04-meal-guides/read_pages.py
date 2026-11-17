from pathlib import Path
import json,hashlib,datetime
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/advertiser04-meal-guides';W=R/'_raw/advertiser04-meal-guides';OUT=R/'sources/advertiser04-meal-guides-reading.jsonl';U={x['ad_id']:x for x in map(json.loads,(W/'native-page-units.jsonl').read_text().splitlines())};M=json.loads((S/'page-ad-read-manifest.json').read_text())
def finish(view,decisions):
 v=M['views'][view-1];assert hashlib.sha256((R/v['file']).read_bytes()).hexdigest()==v['sha256'];assert set(decisions)==set(v['ad_ids']);rows=[json.loads(l) for l in OUT.read_text().splitlines()];by={x['ad_id']:x for x in rows};added=0
 for a in v['ad_ids']:
  u=U[a];b=u['text']['body']['text'];th=hashlib.sha256(json.dumps(u['text'],sort_keys=True,ensure_ascii=False).encode()).hexdigest();occ=dict(raw_file=u['source_raw'],sha256=u['source_sha256'],native_locator=u['native_locator'],capture_kind='advertiser_page',text_sha256=th,all_loaded_text_read=True)
  if a in by:
   r=by[a];assert not any(x['raw_file']==occ['raw_file'] for x in r['source_occurrences']);assert r['text_sha256']==th,(a,'Native text changed between discovery andPage; retain both versions explicitly before deciding');r['source_occurrences'].append(occ);r['page_capture_read_complete']=True
  else:
   r=dict(ad_id=a,advertiser_page_id=u['advertiser_page_id'],snapshot_page_id=u['snapshot_page_id'],advertiser_name=u['advertiser_name'],snapshot_page_name=u['snapshot_page_name'],branded_content=u['branded_content'],is_active=u['is_active'],start_utc=u['start_utc'],source_occurrences=[occ],body_sha256=hashlib.sha256(b.encode()).hexdigest(),text_sha256=th,body_and_all_loaded_text_read=True,destinations=list(dict.fromkeys([u['text'].get('link_url')]+[q.get('link_url') for q in u['text'].get('cards',[])])),media_viewed=False,page_capture_read_complete=True);rows.append(r);by[a]=r;added+=1
  r['promoted_offer'],r['assessment']=decisions[a]
 OUT.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in rows))
 with (S/'ad-reading-progress.jsonl').open('a') as f:f.write(json.dumps(dict(file=v['file'],sha256=v['sha256'],ad_ids=v['ad_ids'],all_full_loaded_text_read=True,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))+'\n')
 print('UNIQUE_LEDGER',len(rows),'PAGE_RECORDS_READ',sum(x.get('page_capture_read_complete',False) for x in rows),'NEW',added)
