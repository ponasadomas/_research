import re,json
S='scratchpad/RESTRICTED-REVIEW/'
before=set()
for n in range(1,6):
    t=open(f'synthesis/reader-notes-pr0{n}.md').read()
    m=re.search(r'^## Restricted ids.*?(?=^## |\Z)',t,re.S|re.M)
    ids=set(re.findall(r'pb0%d-\d+'%n,m.group(0)))
    print(n,len(ids)); before|=ids
recs=[json.loads(l) for n in range(1,6) for l in open(f'voice/reddit-pr0{n}.jsonl')]
print(len(recs),len(before),len(before-{r['id'] for r in recs}))
json.dump(sorted(before),open(S+'before.json','w'))
out=open(S+'all.txt','w')
for r in recs:
    q=r['quote'].replace('\n',' ')
    out.write(f"{r['id']}|{'B' if r['id'] in before else '-'}|{q[:450]}|| {r['context'][:150]}\n")
