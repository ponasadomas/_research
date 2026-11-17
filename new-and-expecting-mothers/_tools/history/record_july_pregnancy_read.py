#!/usr/bin/env python3
"""Record a completed human chunk read and supplied per-post final outcomes; no automated relevance decisions."""
import sys,json,hashlib,datetime
from pathlib import Path
r=Path(__file__).resolve().parents[1]; num=int(sys.argv[1]); decisions=Path(sys.argv[2]); m=json.loads((r/'scratchpad/reddit-july-pregnancy/kept-manifest.json').read_text()); c=m['chunks'][num-1];p=r/c['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256']; rows=[]
for line in decisions.read_text().splitlines():
 i,status,reason=line.split('\t',2);assert status in {'retain','drop'};rows.append({'post_id':i,'final_status':status,'reason':reason})
assert len(rows)==len(c['post_ids']);assert {x['post_id'] for x in rows}==set(c['post_ids']); dst=r/'sources/reddit-july-pregnancy-fullread-outcomes.jsonl';previous=[json.loads(x) for x in dst.read_text().splitlines()] if dst.exists() else [];assert not {x['post_id'] for x in previous}.intersection(c['post_ids']); index={x['post_id']:x for x in m['units']};now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with dst.open('a') as f:
 for row in rows:
  u=index[row['post_id']];row.update({'reader':'market','read_scope':'full_post','complete_archived_original_read':True,'OP_followups_available':False,'comments_available':False,'raw_file':u['raw_file'],'sha256':u['sha256'],'chunk':c['file'],'read_at':now});f.write(json.dumps(row,ensure_ascii=False)+'\n')
log=r/'scratchpad/reddit-july-pregnancy/fullreading-ledger.jsonl';log.open('a').write(json.dumps({'chunk':c['file'],'sha256':c['sha256'],'posts_read':len(rows),'all_originals_fully_read':True,'read_at':now})+'\n');print({'chunk':num,'posts':len(rows),'retained':sum(x['final_status']=='retain' for x in rows),'dropped':sum(x['final_status']=='drop' for x in rows)})
