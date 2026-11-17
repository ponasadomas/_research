from pathlib import Path
import json,csv,hashlib
R=Path(__file__).resolve().parents[2]; S=Path(__file__).parent
H=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((R/'_raw/report-purchase-archive-wave03/supplement-v1/assignments/reader-04.json').read_text())
x={z['post_id']:z for z in map(json.loads,(R/a['primary_index']).read_text().splitlines())}
t=list(csv.DictReader((R/'_raw/report-purchase-archive-wave03/supplement-v1/triage-04.tsv').open(),delimiter='\t'))
assert len(t)==142 and set(z['post_id'] for z in t)==set(a['post_ids'])
for c in a['card_chunks']:assert H(R/c['file'])==c['sha256']
for z in t:assert H(R/z['card_file'])==x[z['post_id']]['card_sha256']
kept=[x[z['post_id']] for z in t if z['label']=='keep']
chunks=[];cur=[];size=0
for z in kept:
 p=R/z['raw_file']; assert H(p)==z['sha256']
 text=p.read_text()
 if cur and size+len(text.encode())>14000:chunks.append(cur);cur=[];size=0
 cur.append(z);size+=len(text.encode())
if cur:chunks.append(cur)
views=[]
for i,c in enumerate(chunks,1):
 p=S/f'full-{i:02}.txt';assert not p.exists();p.write_text('\n\n'.join((R/z['raw_file']).read_text() for z in c))
 views.append(dict(file=str(p.relative_to(R)),post_ids=[z['post_id'] for z in c],sha256=H(p)))
(S/'full-manifest.json').write_text(json.dumps(dict(keeps=kept,views=views),indent=2)+'\n')
print(json.dumps(views,indent=2))
