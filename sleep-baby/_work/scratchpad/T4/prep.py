import json,re,sys,glob,os
C='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/_raw/reddit/filter-v1/wave1/cards/'
R='/home/thinkpad/GitHub/ads/mamivio.com/research/_shared/_raw/reddit-2026/'
files="A-GentleParenting-001 A-Mommit-006 A-NewParents-005 A-NewParents-011 A-Parenting-004 A-beyondthebump-005 A-beyondthebumpUK-004 A-sleeptrain-001 A-sleeptrain-007 A-sleeptrain-013 A-sleeptrain-019 A-toddlers-005".split()
sl=re.compile(r'sleep|nap|bedtime|night|wake|waking|crib|cot|bassinet|cosleep|co-sleep|bed.?shar',re.I)
subs={}
out=[]
for f in files:
    sub=f.split('-')[1]
    if sub not in subs:
        subs[sub]={}
        for l in open(R+sub+'.posts.jsonl'):
            d=json.loads(l); subs[sub][d['id']]=d
    txt=open(C+f+'.txt').read()
    for blk in re.split(r'\n(?=ID )',txt):
        m=re.match(r'ID (\w+) \| (\S+) \| (\S+) \| safety_flag=(\w+)',blk)
        if not m: continue
        i=m.group(1); d=subs[sub].get(i,{})
        body=(d.get('selftext') or '')
        n=len(sl.findall(body+' '+d.get('title','')))
        t=re.search(r'TITLE: (.*)',blk).group(1)
        out.append((f,i,m.group(4),n,len(body),t,body))
json.dump(out,open('all.json','w'))
print(len(out))
