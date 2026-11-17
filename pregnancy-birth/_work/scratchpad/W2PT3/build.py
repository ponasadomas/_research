import re,sys
card,out=sys.argv[1],sys.argv[2]
order=re.findall(r'^ID (\w+) \|',open('../../_raw/reddit/filter-v1/wave2/cards/'+card).read(),re.M)
rows={}
for l in sys.stdin:
    l=l.rstrip('\n')
    if not l.strip(): continue
    p=l.split('|',2)
    assert len(p)==3,l
    i,lab,r=[x.strip() for x in p]
    assert lab in('keep_core','keep_purchase','keep_success','keep_otherside','drop'),l
    assert i not in rows,'dup '+i
    rows[i]=(lab,r)
miss=[i for i in order if i not in rows]; extra=[i for i in rows if i not in order]
print(card,len(order),len(rows),'missing',miss,'extra',extra)
if not miss and not extra:
    open(out,'w').write(''.join(f"{i}\t{rows[i][0]}\t{rows[i][1]}\n" for i in order))
