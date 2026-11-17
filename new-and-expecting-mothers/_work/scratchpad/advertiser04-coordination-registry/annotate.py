from pathlib import Path
import json,sys
S=Path(__file__).parent;m=json.loads((S/'manifest-v2.json').read_text());allowed={x['ad_id'] for x in m['units']};p=S/'decisions.jsonl';old=[json.loads(l) for l in p.read_text().splitlines()] if p.exists() else [];seen={x['ad_id'] for x in old}
for group in json.load(sys.stdin):
 for id in group.pop('ids'):
  assert id in allowed and id not in seen;seen.add(id);old.append(dict(ad_id=id,full_available_body_and_card_text_read=True,images_viewed=False,videos_viewed=False,**group))
p.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in old));print('read decisions',len(old))
