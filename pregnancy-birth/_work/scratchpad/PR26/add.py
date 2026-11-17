# usage: python3 -I add.py batch.json  -- appends records to voice file, assigns ids, checks quote in raw
import json, sys, os, re, html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/pregnancy-birth/'
V=B+'voice/reddit-pr26.jsonl'
def norm(s):
    s=html.unescape(s).replace("\\n"," "); return re.sub(r"\s+"," ",s).strip()
n=0
if os.path.exists(V):
    n=sum(1 for l in open(V) if l.strip())
recs=json.load(open(sys.argv[1]))
out=[]; bad=0
for r in recs:
    u=r.pop('u'); raw=f'../_shared/_raw/reddit-2026/units/{u}.txt'
    txt=open(B+raw,encoding='utf-8').read()
    sub,pid=u.rsplit('-',1)
    first=txt.split('\n',1)[0]
    m=re.search(r'\| (\d{4}-\d\d-\d\d) ',first); pdate=m.group(1)
    purl=re.search(r'(https://\S+)',first).group(1)
    cid=r.pop('c',None)
    if cid:
        m=re.search(r'COMMENT '+cid+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
        if not m: print('NO COMMENT',u,cid); bad+=1; continue
        date,url=m.group(1),m.group(2)
    else: date,url=pdate,purl
    t=norm(txt); pos=0; ok=True
    for piece in re.split(r"\s*\[(?:…|\.\.\.)\]\s*", r['quote']):
        piece=norm(piece)
        if not piece: continue
        a=t.find(piece,pos)
        if a<0: print('MISS',u,piece[:80]); ok=False; break
        pos=a+len(piece)
    if not ok: bad+=1; continue
    n+=1
    d={'id':'pb26-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':r['sp'],'stage':r['st'],'type':r['ty'],'themes':r['th'],'quote':r['quote'],'context':r['cx'],'raw_file':raw,'source_class':'reddit_archive','post_id':pid}
    if cid: d['comment_id']=cid
    if len(r['cx'].split())>25: print('LONG CTX',d['id'])
    out.append(d)
if bad: print('ABORT, nothing written', bad); sys.exit(1)
with open(V,'a') as f:
    for d in out: f.write(json.dumps(d,ensure_ascii=False)+'\n')
for d in out: print(d['id'], d['post_id'], d['quote'][:50])
