import re,sys
t=open(sys.argv[1],encoding='utf-8').read().split('## Coverage')[0]
L=t.split('\n')
cat={'heading':0,'count':0,'bullet_quote':0,'but':0,'other':0,'limits':0}
inlim=False; fs=[]; cur=None
for l in L:
    w=len(l.split())
    if l.startswith('## '): inlim=(l.strip()=='## Limits'); cat['heading']+=w; continue
    if inlim or l.startswith('# ') or l.startswith('**Written') or l.startswith('**Reviewed'): cat['limits']+=w; continue
    if l.startswith('### '): cat['heading']+=w; cur=[l[4:],0]; fs.append(cur); cur[1]+=w; continue
    if cur: cur[1]+=w
    if re.match(r'^\d[\d,]* of [\d,]+ posts\.',l): cat['count']+=w
    elif l.startswith('- "'): cat['bullet_quote']+=w
    elif l.startswith('**But:**'): cat['but']+=w
    else: cat['other']+=w
print(cat,sum(cat.values()),len(fs))
qs=re.findall(r'"([^"\n]{8,})" \[sr',t)
import statistics
ql=[len(q.split()) for q in qs]
print('quotes',len(ql),'avg',statistics.mean(ql),'total',sum(ql))
if len(sys.argv)>2:
    for c,w in sorted(fs,key=lambda x:-x[1])[:int(sys.argv[2])]: print(w,c[:90])
