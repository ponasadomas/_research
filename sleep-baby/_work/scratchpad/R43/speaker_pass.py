import re,glob,os,collections
U="../../../_shared/_raw/reddit-2026/units/"
M=re.compile(r"\b(mom|mum|mother|motherhood|mama|mommy|mummy|momma|mamma|mamas|moms|mums|sahm|ftm|mat leave|maternity leave|postpartum|pp|pregnan\w*|breastfe\w*|ebf|pump\w*|nurs(e|es|ed|ing))\b")
STRIP=re.compile(r"\b(my|her|his|your|their|our|the|a|other|another|some|many|working|first time|new|fellow|other)\s+(mom|mum|mother|moms|mums|mothers)s?\b|night nurse|mother.s day|\bmil\b|mother-in-law|grand\w+")
cache={}
def ismother(unit):
    if unit not in cache:
        t=open(U+unit+".txt",encoding="utf-8").read().lower()
        # OP text only (post + OP replies are all OP)
        t=STRIP.sub(" ",t)
        cache[unit]=M.search(t)
    return cache[unit]
rows={}
for f in sorted(glob.glob("q*.tsv")):
    for l in open(f,encoding="utf-8"):
        if l.strip(): p=l.split(" || "); rows.setdefault(p[0],set()).add(p[2])
plan={}
for u,sp in rows.items():
    if sp & {"partner","relative_caregiver"}: continue
    m=ismother(u)
    if m: lab="experienced_mother" if "experienced_mother" in sp else "new_mother"
    else: lab="parent_unspecified"
    if sp!={lab}: plan[u]=(sorted(sp),lab,m.group(0) if m else None)
for u,v in sorted(plan.items()): print(u,v)
import sys
if len(sys.argv)>1:
    for f in sorted(glob.glob("q*.tsv")):
        out=[]
        for l in open(f,encoding="utf-8"):
            p=l.split(" || ")
            if l.strip() and p[0] in plan: p[2]=plan[p[0]][1]; l=" || ".join(p)
            out.append(l)
        open(f,"w",encoding="utf-8").write("".join(out))
    print("applied")
