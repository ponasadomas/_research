import glob,re,collections
M={'c':'keep_core','p':'keep_purchase','s':'keep_success','o':'keep_otherside','d':'drop'}
rows=[]
for f in sorted(glob.glob('p[0-9][0-9].txt')):
    for l in open(f):
        l=l.rstrip('\n')
        if not l: continue
        i,lab,r=l.split(' ',2)
        if len(r.split())>15: print('LONG',i)
        if lab=='d' and re.match(r'(unsafe|crisis)',r): pass
        rows.append((i,M[lab],r))
base='/home/thinkpad/GitHub/ads/mamivio.com/research/sleep-baby/_raw/reddit/'
with open(base+'triage/wave1-T1.tsv','w') as o:
    o.write('post_id\tlabel\treason\n')
    for r in rows: o.write('\t'.join(r)+'\n')
files="A-AttachmentParenting-001 A-Mommit-003 A-NewParents-002 A-NewParents-008 A-Parenting-001 A-beyondthebump-002 A-beyondthebumpUK-001 A-daddit-003 A-sleeptrain-004 A-sleeptrain-010 A-sleeptrain-016 A-toddlers-002 A-workingmoms-001".split()
exp=[]
for f in files:
    exp+=re.findall(r'^ID (\S+) \|',open(base+'filter-v1/wave1/cards/'+f+'.txt').read(),re.M)
got=[r[0] for r in rows]
print(len(exp),len(got),len(set(got)),set(exp)==set(got),[k for k,v in collections.Counter(got).items() if v>1],len(exp)==len(set(exp)))
print(collections.Counter(r[1] for r in rows))
