import json,sys,re
r={}
for l in open('voice-merged/all.jsonl'):
    x=json.loads(l); r[x['id']]=x
mode=sys.argv[1]
if mode=='ids':
    for i in sys.argv[2:]:
        x=r[i]; print(i,'R' if x['restricted'] else '-',x['speaker'],x['stage'],x['type'],x['themes'],'|',x['quote'].replace('\n',' ')[:500],'|| CTX',x['context']);print()
elif mode=='grep':
    pat=re.compile(sys.argv[2],re.I)
    for i,x in r.items():
        if i[:4] in('dv03','dv04') and (pat.search(x['quote']) or (len(sys.argv)>3 and pat.search(x['context']))):
            print(i,'R' if x['restricted'] else '-','|',x['quote'].replace('\n',' ')[:300],'|| CTX',x['context'][:150])
