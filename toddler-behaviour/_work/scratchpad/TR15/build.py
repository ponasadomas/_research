# Build voice/reddit-tr15.jsonl from scratchpad/TR15/drafts/*.txt
# Draft format: blocks separated by blank line:
# U <unit basename without .txt>
# S speaker | T stage | Y type | H theme,theme
# Q quote (single line)
# C context
import json,re,glob,os,html,sys
ROOT=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
def norm(s):
    s=html.unescape(s); return re.sub(r'\s+',' ',s).strip()
SP={'new_mother','experienced_mother','recovered_parent','parent_unspecified','partner','relative_caregiver','advisor','professional','reviewer','skeptic','gave_up_parent'}
ST={'toddler_12_18_months','toddler_18_24_months','toddler_2_3_years','preschool_3_4_years','new_sibling','daycare_start','looking_back','unknown'}
TY={'trigger_moment','pain','fear','tried_failed','desire','belief','question','objection','advice_given','success_story','failure_story','regret','others_said','purchase','price_signal'}
out=[];n=0;err=0;restr=[]
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),'drafts','*.txt'))):
    for blk in open(f,encoding='utf-8').read().split('\n\n'):
        lines=[l for l in blk.strip().split('\n') if l.strip()]
        if not lines: continue
        d={l[0]:l[2:].strip() for l in lines}
        unit=d['U']; rf='../_shared/_raw/reddit-2026/units/%s.txt'%unit
        txt=open(os.path.join(ROOT,rf),encoding='utf-8').read()
        parts=re.split(r'\n(?=COMMENT \w+ \| )',txt)
        sp,stg,ty,th=[x.strip() for x in d['S'].split('|')]
        q=d['Q']; first=norm(re.split(r'\s*\[(?:…|\.\.\.)\]\s*',q)[0])
        seg=None
        for p in parts:
            if first in norm(p): seg=p;break
        if seg is None: print('NOTFOUND',unit,q[:60]);err+=1;continue
        h=seg.split('\n')[0]
        m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d).*?\| (\S+)',h)
        rec={}
        n+=1
        pm=re.match(r'POST (\w+) \| r/(\w+) \|',parts[0])
        if m:
            pid,sub,date,url=m.groups(); cid=None
        else:
            c=re.match(r'COMMENT (\w+) \| (\d{4}-\d\d-\d\d).*?\| (\S+)',h)
            cid,date,url=c.groups(); pid,sub=pm.groups()
        for k,v,S in (('speaker',sp,SP),('stage',stg,ST),('type',ty,TY)):
            if v not in S: print('BAD',k,v,unit);err+=1
        if len(d['C'].split())>25: print('LONGCTX',unit,d['C'][:40]);err+=1
        rec=dict(id='tb15-%04d'%n,source='reddit r/'+sub,url=url,date=date,speaker=sp,stage=stg,type=ty,
                 themes=[t.strip() for t in th.split(',') if t.strip()],quote=q,context=d['C'],raw_file=rf,
                 source_class='reddit_archive',post_id=pid)
        if cid: rec['comment_id']=cid
        out.append(rec)
        if 'R' in d: restr.append((rec['id'],d['R']))
with open(os.path.join(ROOT,'voice','reddit-tr15.jsonl'),'w',encoding='utf-8') as o:
    for r in out: o.write(json.dumps(r,ensure_ascii=False)+'\n')
print(n,'records',err,'errors')
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'restricted.txt'),'w').write(''.join('- %s (%s)\n'%r for r in restr))
print(len(restr),'restricted')
