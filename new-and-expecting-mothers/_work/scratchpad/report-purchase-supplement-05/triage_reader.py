from pathlib import Path
import json,csv,hashlib,collections,datetime
R=Path(__file__).resolve().parents[2];S=R/'scratchpad/report-purchase-supplement-05';A=R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-05.json';M=json.loads(A.read_text());IDX={x['post_id']:x for x in map(json.loads,(R/M['primary_index']).read_text().splitlines())};OUT=R/'_raw/report-purchase-archive-wave03/supplement-v1/triage-05.tsv'
def decide(view,lines):
 c=M['card_chunks'][view-1];assert hashlib.sha256((R/c['file']).read_bytes()).hexdigest()==c['sha256'];rows=[]
 for line in lines.strip().splitlines():
  tid,label,reason=line.split('\t');assert label in ['keep','drop'] and reason;rows.append(dict(post_id=tid,label=label,reason=reason,card_file=IDX[tid]['card_file']))
 assert len(rows)==len(c['post_ids']) and {x['post_id'] for x in rows}==set(c['post_ids']);old=list(csv.DictReader(OUT.open(),delimiter='\t')) if OUT.exists() else [];assert not {x['post_id'] for x in old}&set(c['post_ids'])
 with OUT.open('a') as f:
  w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t')
  if not old:w.writeheader()
  w.writerows(rows)
 with (S/'triage-reading.jsonl').open('a') as f:f.write(json.dumps(dict(view=view,original_card_view=c['file'],sha256=c['sha256'],post_ids=c['post_ids'],all_cards_human_read=True,utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))+'\n')
 cp=dict(assigned_cards=len(M['post_ids']),triaged=len(old+rows),kept=sum(x['label']=='keep' for x in old+rows),dropped=sum(x['label']=='drop' for x in old+rows),views_complete=view,views_total=len(M['card_chunks']));(S/'triage-checkpoint.json').write_text(json.dumps(cp,indent=2)+'\n');print(json.dumps(cp))
