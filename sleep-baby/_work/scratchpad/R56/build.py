import json, re, html, sys, glob, os
B='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/'
def norm(s):
    s=html.unescape(s).replace("\\n"," "); return re.sub(r"\s+"," ",s).strip()
SP={'p':'parent_unspecified','nm':'new_mother','em':'experienced_mother','pa':'partner','rc':'relative_caregiver','sk':'skeptic','rp':'recovered_parent','gu':'gave_up_parent','ad':'advisor'}
units={}
for l in open(B+'scratchpad/R56/units.txt'):
    c,u=l.rstrip('\n').split('\t'); units[os.path.basename(u)[:-4]]=u
out=[]; restricted=[]; n=0; errs=0
for f in sorted(glob.glob(B+'scratchpad/R56/q*.jsonl')):
    for line in open(f):
        if not line.strip(): continue
        r=json.loads(line); u=units[r['u']]
        t=norm(open(B+u,encoding='utf-8').read())
        first=norm(r['q'].split(' […] ')[0])
        pos=t.find(first)
        if pos<0: print('NOTFOUND',r['u'],r['q'][:60]); errs+=1; continue
        head=t[:pos]
        m=list(re.finditer(r'COMMENT (\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)',head))
        p=re.match(r'POST (\w+) \| r/(\w+) \| (\d{4}-\d\d-\d\d) [\d:]+ UTC \| (\S+)',t)
        n+=1; rec={'id':'sb56-%04d'%n,'source':'reddit r/'+p.group(2)}
        if m: rec['url']=m[-1].group(3); rec['date']=m[-1].group(2)
        else: rec['url']=p.group(4); rec['date']=p.group(3)
        rec.update(speaker=SP.get(r['sp'],r['sp']),stage=r['st'],type=r['ty'],themes=r['th'],quote=r['q'],context=r['c'],raw_file=u,source_class='reddit_archive',post_id=p.group(1))
        if m: rec['comment_id']=m[-1].group(1)
        if r.get('r'): restricted.append((rec['id'],r['r']))
        if len(r['c'].split())>25: print('LONGCTX',rec['id'])
        out.append(rec)
with open(B+'voice/reddit-r56.jsonl','w') as o:
    for rec in out: o.write(json.dumps(rec,ensure_ascii=False)+'\n')
with open(B+'scratchpad/R56/restricted.txt','w') as o:
    for i,why in restricted: o.write(f'- {i} ({why})\n')
print(n,'written',errs,'errors',len(restricted),'restricted')
