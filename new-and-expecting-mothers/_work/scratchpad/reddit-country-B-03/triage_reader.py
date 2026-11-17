from pathlib import Path
import json,hashlib,csv,collections,datetime
ROOT=Path(__file__).resolve().parents[2];S=ROOT/'scratchpad/reddit-country-B-03';M=json.loads((S/'card-views-v1/manifest.json').read_text());OUT=ROOT/'_raw/reddit-deep/triage/country-B-03.tsv'
LABELS=set('keep_play keep_solids keep_pumping_work keep_sleep keep_postpartum keep_pregnancy keep_registry keep_other drop'.split())
def decide(view,lines):
 c=M['views'][view-1];assert c['view']==view;assert hashlib.sha256((ROOT/c['file']).read_bytes()).hexdigest()==c['sha256']
 rows=[]
 for line in lines.strip().splitlines():
  tid,label,reason=line.split('\t');assert label in LABELS and reason;rows.append(dict(post_id=tid,label=label,reason=reason,card_file=M['source_card_file_by_post_id'][tid]))
 assert {x['post_id'] for x in rows}==set(c['post_ids']) and len(rows)==len(c['post_ids'])
 old=list(csv.DictReader(OUT.open(),delimiter='\t')) if OUT.exists() else [];assert not {x['post_id'] for x in old}&set(c['post_ids'])
 with OUT.open('a') as f:
  w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t')
  if not old:w.writeheader()
  w.writerows(rows)
 with (S/'triage-reading.jsonl').open('a') as f:f.write(json.dumps(dict(view=view,card_view=c['file'],sha256=c['sha256'],all_cards_human_read=True,post_ids=c['post_ids'],utc=datetime.datetime.now(datetime.timezone.utc).isoformat()))+'\n')
 tally=collections.Counter(x['label'] for x in old+rows);(S/'triage-checkpoint.json').write_text(json.dumps(dict(assigned=291,triaged=len(old+rows),kept=sum(v for k,v in tally.items() if k!='drop'),dropped=tally['drop'],labels=dict(tally),views_complete=view),indent=2)+'\n');print((S/'triage-checkpoint.json').read_text())
