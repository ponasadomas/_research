#!/usr/bin/env python3
"""build.py [out] -> assembles spec/*.md into the findings page: fills count lines from the 26 sections, checks sums,
checks quotes (word for word, whole sentence, age of the post fits the run), builds Coverage by script.

Spec directives (a line starting with @):
  @pattern NN                  sets the pattern for the lines that follow
  @count pattern               "<u2+a23> of 3,811 posts."
  @run u2 | @run a23           bold line that opens a run of form findings; quotes below must fit that age
  @forms u2|a23 ... @end       lines "<section heading>"; emits "<sum> of <run's yes posts> posts."
  @small u2|a23 ... @end       lines "<section heading> => <short claim>"; emits the count line and "Counted here: ...".
  @across tried|others|paid|feel   emits "<sum of the two sections> of <pattern total> posts." and the split by age
  @bands a b ..                quotes below (until the next ###) must come from posts in these age bands
  @nearmap u2|a23 NN [NN..]    every Near-posts heading of those sections goes (in Coverage) to the current finding
  @nearlist ... @end           lines "u2|a23 NN | <near heading> => <short>"; emits "<short> (n); ..." sentence
  @raw text                    the text, as is
Placeholders in any line: {U2} {A23} {TOT} = the current pattern's yes posts under 2, at 2 and 3, and both.
"""
import re,os,sys,glob,json
sys.path.insert(0,os.path.dirname(__file__))
from sections import load
from common import *
S=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT=R+'/findings/what-hurts-and-what-she-wants.md'
if len(sys.argv)>1: OUT=sys.argv[1]
sec=load(); rec=records(); P=posts()
YES={k:[h for h in v['heads'] if h['level']==3 and h['part']=='On-niche posts'][0]['m'] for k,v in sec.items()}
assert sum(v for (g,k),v in YES.items() if g=='u2')==2471 and sum(v for (g,k),v in YES.items() if g=='a23')==1340
def tag(h):
    t=h.lower()
    if re.search(r'\bpay|paying|purchas|\bbuy|bought|spending|acquiring',t): return 'paid'
    if re.search(r'tried|\btry|\btries|tested|adjusting|practised|changed feeding|already acted',t): return 'tried'
    if re.search(r'\bother|receiv|\bhear|encounter|gets help',t): return 'others'
    if re.search(r'\bfeel|express|describe|\bname',t): return 'feel'
    return '?'
ACR={}
for key,v in sec.items():
    hs=[h for h in v['heads'] if h['level']==3 and h['part']=='Across the on-niche posts']
    d={tag(h['head']):h for h in hs}
    assert len(hs)==4 and set(d)=={'tried','others','paid','feel'},(key,[(tag(h['head']),h['head']) for h in hs])
    ACR[key]=d
def find(g,k,part,head):
    hs=[h for h in sec[(g,k)]['heads'] if h['level']==3 and h['part']==part and h['head']==head]
    if len(hs)!=1: raise SystemExit(f"{g} pattern {k} {part}: heading not found or not unique: {head!r}")
    return hs[0]
import collections
_yes=[p for p in P.values() if p['mark']=='yes']; _near=[p for p in P.values() if p['mark']=='near']
_bt=collections.Counter(band(p['stage']) for p in _yes); _bp=collections.Counter((band(p['stage']),int(p['main_pattern'])) for p in _yes)
_sp=collections.Counter(p['speaker'] for p in _yes); _sub=collections.Counter(p['subreddit'] for p in _yes); _bo=collections.Counter(p['border'] for p in _near)
_subband=collections.Counter((p['subreddit'],band(p['stage'])) for p in _yes)
NEARSORTED={g:sum([h for h in v['heads'] if h['level']==3 and h['part']=='Near posts'][0]['m'] for (gg,k),v in sec.items() if gg==g) for g in ('u2','a23')}
def ph(m):
    a=m.group(1).split(':')
    try:
        if a[0]=='n': v=sum(_bp[(b,int(k))] for b in a[1].split('+') for k in a[2].split('+'))
        elif a[0]=='t': v=sum(_bt[b] for b in a[1].split('+'))
        elif a[0]=='speaker': v=sum(_sp[x] for x in a[1].split('+'))
        elif a[0]=='sub': v=sum(_sub[x] for x in a[1].split('+')) if len(a)==2 else sum(_subband[(a[1],b)] for b in a[2].split('+'))
        elif a[0]=='border': v=sum(_bo[x] for x in a[1].split('+'))
        elif a[0]=='nearsorted': v=sum(NEARSORTED[x] for x in a[1].split('+'))
        elif a[0]=='pct': 
            num=sum(_bp[(b,int(k))] for b in a[1].split('+') for k in a[2].split('+')); den=sum(_bt[b] for b in a[1].split('+')); return f"{round(100*num/den)}%"
        else: return m.group(0)
    except Exception as e:
        errors.append(f"bad placeholder {m.group(0)}: {e}"); return m.group(0)
    return f"{v:,}"
went={}; errors=[]; warns=[]; out=[]; groupwords=[]
pat=None; claim=None; allowed=None; run=None; curids=None
formsum={}; claims=[]; runcount={}
def setwent(g,k,part,head,c):
    key=(g,k,part,head)
    if key in went and part!='Near posts': errors.append(f"used twice: {key}")
    went[key]=c
U2B={'0-6m','6-12m','12-18m','18-24m'}; A23B={'2y','3y'}
def checkquotes(line,fname):
    for q,i in re.findall(r'"([^"\n]+)" \[([a-z]{2,}\d+-\d+)\]',line):
        if i not in rec: errors.append(f"{fname}: id {i} not in quotes"); continue
        text=rec[i]['quote']; p=P.get(rec[i]['post_id'],{})
        for part in [x for x in re.split(r'\s*\[…\]\s*',q) if x.strip()]:
            loc=locate(text,part)
            if not loc: errors.append(f"{fname}: not word for word {i}: {part[:50]}"); continue
            s,e=whole(text,*loc)
            if not s or not e: warns.append(f"not a whole sentence? [{i}] {part[:60]!r}  -> widened: {widen(text,*loc)[:200]!r}")
        b=band(p.get('stage',''))
        if curids is not None and i not in curids and not line.startswith('**But'): warns.append(f"quote {i} is not cited under this finding's own forms: {claim[:70]}")
        if run is not None and b=='none': warns.append(f"quote {i} in a run is from a post with no stated age ({p.get('stage')}): {claim[:60]}")
        if allowed is not None and b not in allowed: errors.append(f"{fname}: quote {i} is from a post of stage {p.get('stage')!r} (mark {p.get('mark')}), not in {sorted(allowed)}: {claim[:50]}")
        if p.get('mark')!='yes' and not nearok: warns.append(f"quote {i} is from a {p.get('mark')} post ({p.get('border')}), under: {claim[:60]}")
nearok=False
files=sorted(glob.glob(S+'/spec/*.md'))
for f in files:
    fname=os.path.basename(f)
    L=open(f,encoding='utf-8').read().split('\n'); i=0; start=len(out)
    while i<len(L):
        l=L[i]
        if pat:
            l=l.replace('{U2}',f"{YES[('u2',pat)]:,}").replace('{A23}',f"{YES[('a23',pat)]:,}").replace('{TOT}',f"{YES[('u2',pat)]+YES[('a23',pat)]:,}").replace('{U2P}',f"{round(100*YES[('u2',pat)]/2471)}%").replace('{A23P}',f"{round(100*YES[('a23',pat)]/1340)}%")
        l=re.sub(r'\{((?:n|t|speaker|sub|border|nearsorted|pct):[^}]+)\}',ph,l)
        if l.startswith('@include '):
            out+=open(S+'/'+l.split()[1],encoding='utf-8').read().rstrip().split('\n'); i+=1; continue
        if l.startswith('## '):
            nearok=l.strip() in ('## Next to the niche','## Limits'); pat=None; run=None; allowed=None
            out.append(l); i+=1; continue
        if l.startswith('@pattern '): pat=l.split()[1]; i+=1; continue
        if l.startswith('@run '):
            run=l.split()[1]; allowed=U2B|{'none'} if run=='u2' else A23B
            out.append(f"**{'Under 2' if run=='u2' else 'At 2 and 3'}** ({YES[(run,pat)]:,} posts)"); out.append(''); i+=1; continue
        if l.startswith('@bands'): allowed=set(l.split()[1:]) or None; i+=1; continue
        if l.startswith('### '):
            curids=None
            claim=l[4:].strip()
            if claim in claims: errors.append(f"claim not unique: {claim}")
            claims.append(claim); out.append(l); out.append(''); i+=1
            allowed=None if run is None else (U2B|{'none'} if run=='u2' else A23B)
            continue
        if l.strip()=='@count pattern':
            run=None; allowed=None
            out.append(f"{YES[('u2',pat)]+YES[('a23',pat)]:,} of 3,811 posts."); i+=1; continue
        if l.startswith('@raw '): out.append(l[5:]); i+=1; continue
        m=re.match(r'^@(forms|small) (u2|a23)\s*$',l)
        if m:
            kind,g=m.groups(); i+=1; tot=0; items=[]
            if g!=run: errors.append(f"{fname}: @{kind} {g} outside its run: {claim}")
            while L[i].strip()!='@end':
                if L[i].strip():
                    h,_,short=L[i].partition(' => ')
                    x=find(g,pat,'On-niche posts',h.strip()); tot+=x['n']; items.append((short.strip(),x['n'])); setwent(g,pat,'On-niche posts',h.strip(),claim)
                i+=1
            i+=1
            formsum[(g,pat)]=formsum.get((g,pat),0)+tot; runcount[(g,pat)]=runcount.get((g,pat),0)+1
            curids=set(i_ for hh in sec[(g,pat)]['heads'] if hh['level']==3 and hh['part']=='On-niche posts' and (g,pat,'On-niche posts',hh['head']) in went and went[(g,pat,'On-niche posts',hh['head'])]==claim for i_ in hh['ids'])
            out.append(f"{tot:,} of {YES[(g,pat)]:,} posts.")
            if kind=='small':
                if any(not s for s,n in items): errors.append(f"{fname}: @small item without short claim: {claim}")
                out.append(''); out.append('Counted here: '+'; '.join(f"{s} ({n})" for s,n in items)+'.')
            continue
        if l.startswith('@across '):
            run=None; allowed=None
            t=l.split()[1]; a=ACR[('u2',pat)][t]; b=ACR[('a23',pat)][t]
            setwent('u2',pat,'Across the on-niche posts',a['head'],claim); setwent('a23',pat,'Across the on-niche posts',b['head'],claim)
            mu,ma=YES[('u2',pat)],YES[('a23',pat)]
            out.append(f"{a['n']+b['n']:,} of {mu+ma:,} posts."); out.append('')
            out.append(f"Under 2: {a['n']:,} ({round(100*a['n']/mu)}%). At 2 and 3: {b['n']:,} ({round(100*b['n']/ma)}%)."+(' '+L[i+1][2:].strip() if i+1<len(L) and L[i+1].startswith('+ ') else ''))
            i+=2 if i+1<len(L) and L[i+1].startswith('+ ') else 1; continue
        if l.startswith('@nearmap '):
            a=l.split(); g=a[1]
            for k in a[2:]:
                for h in sec[(g,k)]['heads']:
                    if h['level']==3 and h['part']=='Near posts': went[(g,k,'Near posts',h['head'])]=claim
            i+=1; continue
        if l.strip()=='@nearlist':
            i+=1; items=[]
            while L[i].strip()!='@end':
                if L[i].strip():
                    gk,_,rest=L[i].partition(' | '); g,k=gk.split(); h,_,short=rest.partition(' => ')
                    x=find(g,k,'Near posts',h.strip()); items.append((short.strip(),x['n']))
                i+=1
            i+=1
            out.append('The largest forms: '+'; '.join(f"{s} ({n})" for s,n in items)+'.'); continue
        if l.startswith('@'): errors.append(f"{fname}: unknown directive {l}")
        checkquotes(l,fname)
        out.append(l); i+=1
    groupwords.append((fname,len(' '.join(out[start:]).split())))
# checks
for (g,k) in sec:
    on=[h for h in sec[(g,k)]['heads'] if h['level']==3 and h['part']=='On-niche posts']
    miss=[h['head'] for h in on if (g,k,'On-niche posts',h['head']) not in went]
    if miss: errors.append(f"{g} pattern {k}: {len(miss)} on-niche forms unused, e.g. {miss[:3]}")
    if formsum.get((g,k),0)!=YES[(g,k)]: errors.append(f"{g} pattern {k}: forms sum {formsum.get((g,k),0)} != {YES[(g,k)]}")
    if not 3<=runcount.get((g,k),0)<=6: errors.append(f"{g} pattern {k}: {runcount.get((g,k),0)} form findings in the run (3 to 6 wanted)")
    for h in sec[(g,k)]['heads']:
        if h['level']==3 and h['part']!='On-niche posts' and (g,k,h['part'],h['head']) not in went: errors.append(f"{g} pattern {k}: {h['part']} heading unmapped: {h['head']}")
body='\n'.join(out).rstrip()+'\n'
body=re.sub(r'\n{3,}','\n\n',body)
above=len(body.split())
# coverage
cov=['','## Coverage','','<details>','<summary>Every heading of the evidence file, and where it went</summary>','',
 'The evidence file is `counts.md` plus the 26 sections: thirteen for children under 2 (`findings/2026-11/patterns/`) and thirteen for children of 2 and 3 years (`findings/2026-11/patterns-2-3-years/`). Headings are given file by file, because some repeat. This table is made by `_work/2026-11/findings-build-whole-range/tools/build.py`.','',
 '| Section file | Evidence heading | Went to |','|---|---|---|']
SECT={'Limits':'Limits','On-niche posts':"section title: the pattern's group",'Near posts':'section title: Next to the niche','Across the on-niche posts':"section title: the four across findings of the pattern's group",'Coverage':"not about her: the section's own coverage table"}
order=['03','01','04','02','09','11','05','08','07','06','12','10','00']
for k in order:
    for g,d in (('u2','patterns'),('a23','patterns-2-3-years')):
        fn=f"{d}/pattern-{k}.md"
        for h in sec[(g,k)]['heads']:
            if h['level']==2: cov.append(f"| {fn} | {h['head']} | {SECT[h['head']]} |")
            else: cov.append(f"| {fn} | {h['head']} | {went.get((g,k,h['part'],h['head']),'UNMAPPED')} |")
extra=open(S+'/cov-counts.md',encoding='utf-8').read().strip().split('\n') if os.path.exists(S+'/cov-counts.md') else []
cov+=extra
cov+=['','</details>','']
open(OUT,'w',encoding='utf-8').write(body+'\n'.join(cov))
json.dump([[g,k,part,h,c] for (g,k,part,h),c in went.items()],open(S+'/went.json','w'),ensure_ascii=False,indent=0)
print('written',OUT); print('words above Coverage:',above,' findings:',len(claims))
for g,w in groupwords: print(f"  {g}: {w}")
print(f"WARNINGS {len(warns)}"); [print('  ',w) for w in warns[:60]]
print('ERRORS' if errors else 'build checks OK'); [print('  ',e) for e in errors[:60]]
