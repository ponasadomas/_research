from pathlib import Path
import json,hashlib,collections,datetime
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/report-purchase-supplement-05'
def rows(p):return [json.loads(l) for l in p.read_text().splitlines()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
I={x['post_id']:x for x in rows(R/'_raw/report-purchase-archive-wave03/native-index.jsonl')};own=set(json.loads((S/'full-read-v1/manifest.json').read_text())['kept_post_ids']);allq=[];snap=[]
for f in sorted((R/'voice').glob('*.jsonl')):
 rr=rows(f);snap.append(dict(file=str(f.relative_to(R)),sha256=sha(f),records=len(rr)))
 for q in rr:
  if q.get('post_id'):allq.append((q['id'],q['post_id'],str(f.relative_to(R))))
G=collections.defaultdict(list);current=collections.defaultdict(list)
for tid in own:G[I[tid]['native_author_sha256']].append(tid)
for q,t,f in allq:
 if t in I and f!='voice/report-purchase-supplement-05.jsonl':current[I[t]['native_author_sha256']].append(dict(id=q,post_id=t,file=f))
auth=[dict(native_author_sha256=k,own_post_ids=sorted(v),other_voice_records=current[k]) for k,v in sorted(G.items()) if len(v)>1 or current[k]]
B=collections.defaultdict(list)
for x in I.values():
 if x['body_status']=='present':B[x['native_body_sha256']].append(x['post_id'])
exact=[dict(own_post_id=t,other_post_ids=[z for z in B[I[t]['native_body_sha256']] if z!=t]) for t in sorted(own) if len(B[I[t]['native_body_sha256']])>1];same=[dict(id=q,post_id=t,file=f) for q,t,f in allq if t in own and f!='voice/report-purchase-supplement-05.jsonl'];shared=[];ledgers=[]
for f in sorted((R/'sources').glob('report-purchase*reading.jsonl')):
 if f.name=='report-purchase-supplement-05-reading.jsonl':continue
 rr=rows(f);ledgers.append(dict(file=str(f.relative_to(R)),sha256=sha(f),records=len(rr)))
 for x in rr:
  t=x['post_id']
  if t in I and I[t]['native_author_sha256'] in G:shared.append(dict(other_post_id=t,other_ledger=str(f.relative_to(R)),own_post_ids=sorted(G[I[t]['native_author_sha256']])))
C=[x for p in [R/'_raw/report-purchase-archive-wave03/commercial-candidates.jsonl',R/'_raw/report-purchase-archive-wave03/supplement-v1/commercial-candidates.jsonl'] for x in rows(p)];CG=collections.defaultdict(list)
for x in C:CG[I[x['post_id']]['native_author_sha256']].append(x['post_id'])
cs=[dict(own_full_read_post_ids=sorted(z for z in v if z in own),all_candidate_post_ids=sorted(v),outside_full_read_ids_are_metadata_only=True) for k,v in sorted(CG.items()) if len(v)>1 and own&set(v)]
O=dict(repeated_native_authors=auth,exact_native_body_matches=exact,same_post_other_voice_records=same,index_records=len(I),other_commercial_reader_shared_authors=shared,other_commercial_ledgers_checked=ledgers,all_391_candidate_shared_authors=cs,voice_snapshot=snap,scope='Machine metadata/hash dependence audit only, not new human full-original credit. All voice work IDs checked; author comparison is limited to the two-community native index and its shared hash namespace. Archived identity/authenticity unverified.',utc=datetime.datetime.now(datetime.timezone.utc).isoformat());(S/'dependence-audit.json').write_text(json.dumps(O,indent=2)+'\n');print(json.dumps(dict(shared_fullread_authors=shared,same_works=same,exact_bodies=exact,groups=cs,voice_files_checked=len(snap)),indent=2))
