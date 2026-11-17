import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent;W=R/'_raw/report-purchase-archive-wave03';O=R/'sources/report-purchase-archive-wave03-transactions.jsonl'
ix={x['post_id']:x for x in map(json.loads,(W/'native-index.jsonl').read_text().splitlines())}
scope,n=sys.argv[1],int(sys.argv[2]);d=S if scope=='initial' else S/'supplement-own-full-v1';m=json.loads((d/'full-views/manifest.json').read_text());c=m['chunks'][n-1];spec=json.load(sys.stdin);assert [x['post_id'] for x in spec]==c['post_ids'];prev=[json.loads(l) for l in O.read_text().splitlines()] if O.exists() else [];assert not {x['post_id'] for x in spec}&{x['post_id'] for x in prev}
for s in spec:
 assert s['payment_evidence'] and s['product_or_service'] and s['deliverable_format'] and s['use_or_outcome']
 u=ix[s['post_id']];x={'post_id':s['post_id'],'trigger':None,'actual_price':None,'currency':None,'personalization_inputs':None,'personalization_output':None,'support_bundle':None,'qualifications_claimed':None,'refund':None,'affiliation':'not stated; archived author identity and independence unverified','standalone_customized_written_report_verified':False,**s,'raw_file':u['raw_file'],'primary_unit_sha256':u['sha256'],'scope':scope,'missing_values_mean':'not stated in complete saved original, not evidence of absence'}
 with O.open('a') as f:f.write(json.dumps(x,ensure_ascii=False)+'\n')
print('transaction_fields_logged',len(prev)+len(spec))
