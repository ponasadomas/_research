import json,re,sys,glob,os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
SP={'nm':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','rc':'relative_caregiver'}
ST={'nb':'newborn_0_8_weeks','b24':'baby_2_4_months','r4':'regression_4_months','b58':'baby_5_8_months','b912':'baby_9_12_months','t1':'toddler_12_24_months','t2':'toddler_24_36_months','lb':'looking_back','un':'unknown'}
out=[];n=0
for f in sorted(glob.glob(B+'scratchpad/R40/q*.jsonl')):
  for line in open(f):
    if not line.strip(): continue
    r=json.loads(line); n+=1
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%r['u']
    txt=open(os.path.join(B,rf)).read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={'id':'sb40-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date}
    c=r.get('c')
    if c:
      mm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%c,txt)
      rec['url']=mm.group(2); rec['date']=mm.group(1)
    rec.update({'speaker':SP.get(r['sp'],r['sp']),'stage':ST.get(r['st'],r['st']),'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':rf,'source_class':'reddit_archive','post_id':pid})
    if c: rec['comment_id']=c
    if r.get('R'): print('RESTRICTED',rec['id'])
    out.append(rec)
with open(B+'voice/reddit-r40.jsonl','w') as fo:
  for rec in out: fo.write(json.dumps(rec,ensure_ascii=False)+'\n')
print(n)
