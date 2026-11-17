import re,sys,os
d='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/_raw/reddit/filter-v1/wave2/cards/'
files="A-AttachmentParenting-003 A-Mommit-004 A-NewParents-004 A-NewParents-010 A-Parenting-004 A-beyondthebump-004 A-beyondthebumpUK-003 A-sahm-002 A-sleeptrain-006 A-sleeptrain-012 A-sleeptrain-018 A-toddlers-004".split()
out=open('all.txt','w'); ids=[]
for f in files:
    t=open(d+f+'.txt').read()
    for b in re.split(r'\n\s*\n(?=ID )',t.strip()):
        m=re.match(r'ID (\S+) \| r/(\S+) \| (\S+) \| safety_flag=(\w+)\nTITLE: (.*)\nOPENING: (.*?)(?:\nMATCHES:.*)?$',b,re.S)
        if not m: print('BAD',f,b[:80]);continue
        i,s,dt,sf,ti,op=m.groups(); ids.append(i)
        op=re.sub(r'\s+',' ',op)[:230]
        out.write(f"{i}|{s[:6]}|{'S!' if sf=='True' else ''}{ti[:110]}|{op}\n")
open('ids.txt','w').write('\n'.join(ids)+'\n')
print(len(ids),len(set(ids)))
