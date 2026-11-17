# usage: python3 -I add.py batchfile.tsv  -> appends to voice file
# batch lines: unit_basename | speaker | stage | type | themes(comma) | context | quote | R(optional restricted flag)
import json,sys,os,re,html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
V=B+'voice/reddit-pr71.jsonl'
RL=B+'scratchpad/PR71/restricted.txt'
def norm(s): return re.sub(r'\s+',' ',html.unescape(s)).strip()
n=0
if os.path.exists(V): n=sum(1 for l in open(V) if l.strip())
out=open(V,'a'); rl=open(RL,'a')
for line in open(sys.argv[1],encoding='utf-8'):
    if not line.strip() or line.startswith('#'): continue
    p=[x.strip() for x in line.rstrip('\n').split(' | ')]
    unit,spk,stg,typ,th,ctx,q=p[:7]; r=len(p)>7 and p[7]=='R'
    rf='../_shared/_raw/reddit-2026/units/'+unit+'.txt'
    txt=open(B+rf,encoding='utf-8').read()
    first=norm(re.split(r'\s*\[(?:…|\.\.\.)\]\s*',q)[0])
    # find section
    secs=re.split(r'\n(?=COMMENT |POST )',txt)
    hit=None
    for s in secs:
        if first in norm(s): hit=s;break
    if hit is None: sys.exit('NOT FOUND: '+unit+' '+q[:60])
    h=hit.split('\n',1)[0]
    m=re.match(r'(POST|COMMENT) (\S+) \| (?:r/\S+ \| )?(\d{4}-\d\d-\d\d) .*?\| (https\S+)',h)
    kind,cid,date,url=m.groups()
    sub,pid=unit.split('-',1)
    n+=1; i='pb71-%04d'%n
    rec=dict(id=i,source='reddit r/'+sub,url=url,date=date,speaker=spk,stage=stg,type=typ,themes=[t for t in th.split(',') if t],quote=q,context=ctx,raw_file=rf,source_class='reddit_archive',post_id=pid)
    if kind=='COMMENT': rec['comment_id']=cid
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    if r: rl.write(i+'\t'+unit+'\n')
    print(i,unit,'R' if r else '')
