import json,re
R=[json.loads(l) for l in open('voice/reddit-mr02.jsonl')]
MH_UNITS={'beyondthebump-1w3kqd5','Mommit-1w3mhdm','Postpartum_Depression-1w4v130','Postpartum_Depression-1w5dc6o','Postpartum_Depression-1w5kc4o','Postpartum_Depression-1w94it4','beyondthebump-1w6ghvp','NewParents-1w7vrmz','beyondthebump-1w9e6f7','sleeptrain-1w9h1c6','NewParents-1wajuwt','BabyBumps-1wb7wqq','NewParents-1wbvw1q','beyondthebump-1wchoap','beyondthebump-1wdxbhs','beyondthebumpUK-1wikzue','workingmoms-1wig5vv','beyondthebump-1wm71jx','pregnant-1wnd923','beyondthebump-1wl4d9r','pregnant-1w7rmes','pregnant-1w8o7j5','beyondthebump-1w70kt8'}
MH_KW=re.compile(r'anxi|panick|mental health|crying|cry |sob|rage|angry|spiral|die|breathing',re.I)
SS_KW=re.compile(r'co-?sleep|cosleep|into bed with us|sleeps on me|lying on me|next to baby|right next to me|bed with',re.I)
MED_KW=re.compile(r'[Mm]edicat|magnesium|melatonin|unisom|sleep aid',re.I)
mh,ss,med=[],[],[]
for r in R:
    u=r['raw_file'].split('/')[-1][:-4]; q=r['quote']
    if u in MH_UNITS or MH_KW.search(q): mh.append(r['id'])
    if SS_KW.search(q): ss.append(r['id'])
    if MED_KW.search(q) or u=='Mommit-1w3mhdm': med.append(r['id'])
for name,l in (('MH',mh),('SS',ss),('MED',med)):
    print(name,len(l)); 
    for i in l:
        r=next(x for x in R if x['id']==i); print(' ',i,r['raw_file'].split('/')[-1][:-4],'|',r['quote'][:80].replace('\n',' '))
