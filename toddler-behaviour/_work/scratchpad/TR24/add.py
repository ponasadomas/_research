# usage: python3 -I add.py < batch.jsonl ; each line: {"p":post_id,"c":comment_id or "", "sp","st","ty","th":[...],"q","cx","r":bool}
import json,sys,os,re,glob
ROOT='/home/thinkpad/GitHub/ads/mamivio.com/research/toddler-behaviour'
OUT=ROOT+'/voice/reddit-tr24.jsonl'
paths=[l.strip() for l in open(ROOT+'/scratchpad/TR24/paths.txt')]
bypid={os.path.basename(p).rsplit('-',1)[1][:-4]:p for p in paths}
n=0
if os.path.exists(OUT):
    n=sum(1 for l in open(OUT) if l.strip())
SP={'mn':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','pr':'professional','rc':'relative_caregiver'}
out=open(OUT,'a')
for line in sys.stdin:
    if not line.strip(): continue
    d=json.loads(line)
    p=bypid[d['p']]
    txt=open(os.path.join(ROOT,p),encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
    sub=m.group(2); date=m.group(3); url=m.group(4)
    if d.get('c'):
        mc=re.search(r'COMMENT '+d['c']+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
        date=mc.group(1); url=mc.group(2)
    n+=1
    rec={'id':'tb24-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':SP.get(d['sp'],d['sp']),'stage':d['st'],'type':d['ty'],'themes':d['th'],'quote':d['q'],'context':d['cx'],'raw_file':p,'source_class':'reddit_archive','post_id':d['p']}
    if d.get('c'): rec['comment_id']=d['c']
    rec['restricted']=bool(d.get('r',False))
    out.write(json.dumps(rec,ensure_ascii=False)+'\n')
    print(rec['id'], d['q'][:50])
