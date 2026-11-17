# usage: python3 -I add.py batchfile.json  (list of dicts: u (unit index 1-based), c (comment id or ""), sp, st, ty, th, q, cx)
import json,sys,re,os
ARG=os.path.abspath(sys.argv[1])
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
units=[l.rstrip('\n').split('\t')[1] for l in open('scratchpad/TR26/units.tsv')]
vf='voice/reddit-tr26.jsonl'
n=sum(1 for l in open(vf)) if os.path.exists(vf) else 0
SP={'nm':'new_mother','em':'experienced_mother','pu':'parent_unspecified','pa':'partner','pr':'professional','rc':'relative_caregiver'}
ST={'12':'toddler_12_18_months','18':'toddler_18_24_months','2':'toddler_2_3_years','3':'preschool_3_4_years','sib':'new_sibling','dc':'daycare_start','lb':'looking_back','u':'unknown'}
out=open(vf,'a')
for e in json.load(open(ARG)):
    u=units[e['u']-1]; t=open(u,encoding='utf-8').read()
    m=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) .*?\| (\S+)',t)
    pid,sub,date,url=m.groups()
    r={}
    if e.get('c'):
        cm=re.search(r'COMMENT '+e['c']+r' \| (\d{4}-\d\d-\d\d) \S+ UTC \| (\S+)',t)
        date,url=cm.groups()
    n+=1
    r={'id':'tb26-%04d'%n,'source':'reddit r/'+sub,'url':url,'date':date,'speaker':SP.get(e['sp'],e['sp']),'stage':ST.get(e['st'],e['st']),'type':e['ty'],'themes':e['th'],'quote':e['q'],'context':e['cx'],'raw_file':u,'source_class':'reddit_archive','post_id':pid}
    if e.get('c'): r['comment_id']=e['c']
    if e.get('restricted'): r['restricted']=True
    out.write(json.dumps(r,ensure_ascii=False)+'\n')
print(n)
