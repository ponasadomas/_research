import json,sys,re
o=json.load(open('all.json'))
pat=re.compile(r'consultant|sleep coach|\bcoach\b|course|bought|\bpaid\b|\$\d|£\d|€\d|snoo\b|huckleberry|taking cara|cara babies|\bapp\b|subscription|program\b|nanit|owlet|ewan|lovevery|dr\.? harvey|polly|precious little|sleep lady|\bebook\b|e-book|hatch|cradlewise|money',re.I)
a,b=int(sys.argv[1]),int(sys.argv[2])
for k in range(a,b):
    f,i,fl,n,L,t,body=o[k]
    txt=' '.join(body.split())
    hs=[]
    for m in pat.finditer(txt):
        s=max(0,m.start()-50); hs.append(txt[s:m.end()+50])
        if len(hs)>=3: break
    if hs: print(k,t[:50],'||',' // '.join(hs))
