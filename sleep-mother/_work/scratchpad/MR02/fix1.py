import json,sys
P='voice/reddit-mr02.jsonl'
T={'sm02-0026':'pain','sm02-0029':'success_story','sm02-0036':'belief','sm02-0037':'success_story','sm02-0051':'success_story','sm02-0055':'pain','sm02-0081':'belief','sm02-0125':'pain','sm02-0134':'pain'}
Q={'sm02-0051':('~2','\\~2'),'sm02-0082':('*tisk*','\\*tisk\\*'),'sm02-0135':('SO **loudly','SO \\*\\*loudly')}
out=[]
for l in open(P):
    r=json.loads(l)
    if r['id'] in T: r['type']=T[r['id']]
    if r['id'] in Q: r['quote']=r['quote'].replace(*Q[r['id']])
    out.append(json.dumps(r,ensure_ascii=False))
open(P,'w').write('\n'.join(out)+'\n')
