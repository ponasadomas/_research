import json,re,sys,csv
from pathlib import Path
R=Path(__file__).resolve().parents[2];A=json.loads((R/'_raw/reddit-deep/aug-dec-2025-wave-v1/assignments/batch-02.json').read_text());D=R/'_raw/reddit-deep/triage/augdec-02.tsv'
labels=dict(r='keep_registry',g='keep_pregnancy',h='keep_postpartum',s='keep_sleep',w='keep_pumping_work',p='keep_play',f='keep_solids',o='keep_other',d='drop')
def cards(c):return re.split(r'\n(?=ID )',(R/A['chunks'][c-1]['file']).read_text().strip())
def show(c,part=1):
 cs=cards(c);pages=[];buf=''
 for i,s in enumerate(cs,1):
  v=f'CARD {i}\n{s}\n'
  if len(buf)+len(v)>24500 and buf:pages.append(buf);buf=''
  buf+=v
 if buf:pages.append(buf)
 print(f'CHUNK {c} PART {part}/{len(pages)}');print(pages[part-1])
def add(c):
 cs=cards(c);chunk=A['chunks'][c-1];old=list(csv.DictReader(D.open(),delimiter='\t')) if D.exists() else [];seen={x['post_id'] for x in old};new=[]
 for line in sys.stdin:
  if not line.strip():continue
  z=re.fullmatch(r'(\d+)([rghswpfod]) (.+)',line.strip());assert z,line;i,lab,reason=z.groups();i=int(i);pid=re.search(r'^ID (\S+)',cs[i-1]).group(1);assert pid not in seen,pid;seen.add(pid);new.append(dict(post_id=pid,label=labels[lab],reason=reason,card_file=chunk['file']))
 with D.open('a') as f:
  w=csv.DictWriter(f,fieldnames=['post_id','label','reason','card_file'],delimiter='\t');
  if not old:w.writeheader()
  w.writerows(new)
 print('saved',len(new),'total',len(old)+len(new))
if __name__=='__main__':
 (show if sys.argv[1]=='show' else add)(int(sys.argv[2]),*([int(sys.argv[3])] if len(sys.argv)>3 else []))
