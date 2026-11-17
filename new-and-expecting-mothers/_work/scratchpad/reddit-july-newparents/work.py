from pathlib import Path
import json,csv,sys
R=Path('mamivio.com/research/global'); W=R/'scratchpad/reddit-july-newparents'; P=R/'_raw/reddit-deep/july-2025-wave-v1'
M={x['post_id']:x for x in map(json.loads,(P/'primary-index.jsonl').read_text().splitlines()) if x['subreddit']=='NewParents'}
def decide(chunk, lines):
    rows=[x.split('|',2) for x in lines.strip().splitlines()]
    idx=next(x for x in map(json.loads,(P/'triage-cards-index.jsonl').read_text().splitlines()) if x['file'].endswith(f'July-A-NewParents-{chunk:03}.txt'))
    assert set(x[0] for x in rows)==set(idx['post_ids']),(len(rows),len(idx['post_ids']),set(idx['post_ids'])-set(x[0] for x in rows))
    (W/f'decisions-{chunk:03}.json').write_text(json.dumps(rows,indent=2))
    allrows=[]
    for f in sorted(W.glob('decisions-*.json')):allrows+=json.loads(f.read_text())
    with (R/'_raw/reddit-deep/triage/july-newparents.tsv').open('w') as out:
        wr=csv.writer(out,delimiter='\t',lineterminator='\n');wr.writerow(['post_id','label','reason']);wr.writerows(allrows)
def readchunk(chunk,batch=0,size=20):
    rows=json.loads((W/f'decisions-{chunk:03}.json').read_text()); ids=[x[0] for x in rows if x[1]!='drop'][batch*size:(batch+1)*size]
    for pid in ids:
        txt=(R/M[pid]['raw_file']).read_text(); meta,body=txt.split('\n=== COMPLETE ORIGINAL POST TITLE ===',1); print('\n'+ '='*12+' '+pid+' '+ '='*12+'\n'+json.dumps({k:M[pid][k] for k in ['post_id','url','post_date','topics','safety_flag','raw_file']})+ '\n=== COMPLETE ORIGINAL POST TITLE ==='+body)
    print('BATCH_IDS',ids)
if __name__=='__main__':readchunk(int(sys.argv[1]),int(sys.argv[2]) if len(sys.argv)>2 else 0,int(sys.argv[3]) if len(sys.argv)>3 else 20)
