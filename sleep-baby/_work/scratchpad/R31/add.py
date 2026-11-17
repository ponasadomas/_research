# usage: python3 -I add.py recs_file.py  -> appends to voice file, assigns ids, checks quotes
import json, sys, re, os, html
BASE='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby'
VOICE=BASE+'/voice/reddit-r31.jsonl'
RESTR=BASE+'/scratchpad/R31/restricted.tsv'
def norm(s):
    s=html.unescape(s).replace("\\n"," "); return re.sub(r"\s+"," ",s).strip()
ns={}; exec(open(sys.argv[1]).read(), ns); R=ns['R']
TYPES='trigger_moment pain fear tried_failed desire belief question objection advice_given success_story failure_story regret others_said purchase price_signal'.split()
SPK='new_mother experienced_mother expecting_mother recovered_parent parent_unspecified partner relative_caregiver advisor professional reviewer skeptic gave_up_parent'.split()
STG='newborn_0_8_weeks baby_2_4_months regression_4_months baby_5_8_months baby_9_12_months toddler_12_24_months toddler_24_36_months looking_back unknown'.split()
n=0
if os.path.exists(VOICE): n=sum(1 for l in open(VOICE) if l.strip())
out=[]; rs=[]; errs=0
for r in R:
    unit,cid,spk,stage,typ,themes,quote,ctx=r[:8]; restr=r[8] if len(r)>8 else ''
    raw='../_shared/_raw/reddit-2026/units/%s.txt'%unit
    txt=open(BASE+'/'+raw,encoding='utf-8').read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',txt)
    pid,sub,date,url=m.groups()
    if cid:
        mm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)'%cid,txt)
        if not mm: print('NO COMMENT',unit,cid); errs+=1; continue
        date,url=mm.groups()
    t=norm(txt); pos=0; ok=True
    for p in re.split(r"\s*\[(?:…|\.\.\.)\]\s*",quote):
        p=norm(p)
        if not p: continue
        a=t.find(p,pos)
        if a<0: ok=False; print('FAIL',unit,repr(p[:80])); break
        pos=a+len(p)
    if not ok: errs+=1; continue
    if len(ctx.split())>25: print('LONGCTX',ctx)
    if typ not in TYPES: print('BADTYPE',typ); errs+=1; continue
    if spk not in SPK: print('BADSPK',spk); errs+=1; continue
    if stage not in STG: print('BADSTAGE',stage); errs+=1; continue
    out.append((unit,cid,spk,stage,typ,themes,quote,ctx,restr,pid,sub,date,url,raw))
if errs: print('ERRORS',errs,'nothing written'); sys.exit(1)
if len(sys.argv)>2: print('dry ok',len(out)); sys.exit(0)
with open(VOICE,'a') as f:
    for (unit,cid,spk,stage,typ,themes,quote,ctx,restr,pid,sub,date,url,raw) in out:
        n+=1; i='sb31-%04d'%n
        d=dict(id=i,source='reddit r/'+sub,url=url,date=date,speaker=spk,stage=stage,type=typ,themes=[x.strip() for x in themes.split(',') if x.strip()],quote=quote,context=ctx,raw_file=raw,source_class='reddit_archive',post_id=pid)
        if cid: d['comment_id']=cid
        f.write(json.dumps(d,ensure_ascii=False)+'\n')
        if restr: rs.append((i,restr))
with open(RESTR,'a') as f:
    for i,w in rs: f.write(i+'\t'+w+'\n')
print('wrote',len(out),'last id',n)
