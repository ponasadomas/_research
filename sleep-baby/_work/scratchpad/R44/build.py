import json,re,glob,os,html
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
SP={'nm':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','rc':'relative_caregiver'}
ST={'nb':'newborn_0_8_weeks','b24':'baby_2_4_months','r4':'regression_4_months','b58':'baby_5_8_months','b912':'baby_9_12_months','t1':'toddler_12_24_months','t2':'toddler_24_36_months','lb':'looking_back','un':'unknown'}
def norm(s): return re.sub(r'\s+',' ',html.unescape(s)).strip()
out=[];n=0;R=[]
for f in sorted(glob.glob(B+'scratchpad/R44/q*.jsonl')):
  for line in open(f):
    if not line.strip(): continue
    r=json.loads(line); n+=1
    rf='../_shared/_raw/reddit-2026/units/%s.txt'%r['u']
    txt=open(os.path.join(B,rf)).read()
    m=re.match(r'POST (\S+) \| r/(\S+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',txt)
    pid,sub,date,url=m.groups()
    rec={'id':'sb44-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date}
    c=r.get('c')
    if not c:
      first=norm(r['q'].split(' […] ')[0])[:60]
      # locate in raw lines
      pos=None; acc=''
      lines=txt.split('\n'); cur=None
      body=''
      for ln in lines:
        mm=re.match(r'COMMENT (\S+) \|',ln)
        if mm: cur=mm.group(1); continue
      # approximate: search normalized per-segment
      segs=re.split(r'(?m)^(COMMENT \S+ \|.*)$',txt)
      cur=None;hits=[]
      for s in segs:
        mm=re.match(r'COMMENT (\S+) \|',s)
        if mm: cur=mm.group(1); continue
        if first in norm(s): hits.append(cur)
      if not hits: print('WARN nohit',n,r['u'],first[:30])
      if len(hits)>1: print('WARN multi',n,r['u'],hits)
      c=hits[0] if hits else None
    if c:
      mm=re.search(r'COMMENT %s \| (\d{4}-\d\d-\d\d) [^|]*\| (\S+)'%c,txt)
      rec['url']=mm.group(2); rec['date']=mm.group(1)
    rec.update({'speaker':SP.get(r['sp'],r['sp']),'stage':ST.get(r['st'],r['st']),'type':r['ty'],'themes':r['th'],'quote':r['q'],'context':r['cx'],'raw_file':rf,'source_class':'reddit_archive','post_id':pid})
    if c: rec['comment_id']=c
    if r.get('R'): R.append(rec['id'])
    out.append(rec)
with open(B+'voice/reddit-r44.jsonl','w') as fo:
  for rec in out: fo.write(json.dumps(rec,ensure_ascii=False)+'\n')
open(B+'scratchpad/R44/restricted.txt','w').write('\n'.join(R)+'\n')
print(n,'records;',len(R),'restricted')
