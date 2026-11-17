#!/usr/bin/env python3
"""Wave 2 (TR10-TR17): tally units excluded whole (read in full, nothing quoted) in the reader ledgers,
by first-matching reason keyword. Reads table rows and bullet rows in each ledger's exclusion section, and
table rows whose status column says 'excluded'. Reposts / cross-posts are counted separately as 'duplicate'."""
import re,glob,os,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.normpath(os.path.join(H,'..','..'))
UNIT=re.compile(r'([A-Za-z]+-1[0-9a-z]{5,7})(\.txt)?')
rows={}
for f in sorted(glob.glob(os.path.join(ROOT,'sources','reddit-reading-tr1[0-7].md'))):
    insec=False
    for line in open(f,encoding='utf-8'):
        if line.startswith('## '):
            insec=bool(re.match(r'## (Units excluded|Excluded units)',line)); continue
        if not (line.startswith('|') or line.startswith('- ')): continue
        status=re.search(r'\|\s*excluded\s*\|',line,re.I)
        if not (insec or status): continue
        m=UNIT.search(line)
        if not m: continue
        rest=line[m.end():].lower()
        rows[(os.path.basename(f)[15:19],m.group(1))]=rest
def cls(r):
    if re.search(r'repost|cross-post|duplicate|off-niche',r): return 'duplicate or off-niche'
    if re.search(r'yell|shout|scream(ing)? at|harsh|raising voice|berat|restrain|held still|holding .* down|force|forcing|forced|physical(ly)? (pull|punish|disciplin|force)|physical discipline|physical punishment|punish|grabb|confin|lock|spank|hitting the child|scaring|stern',r): return 'parent or caregiver harshness / force toward a child'
    if re.search(r'medic|laxative|treatment|constipation|infection|surgery|hospital',r): return 'medical treatment detail'
    if re.search(r'mental-health|depression|self-injury|self-harm|head-banging|abuse|neglect|child-protection|safety|aggression toward a newborn|co-parent',r): return 'other safety (parent crisis, self-injury, abuse or neglect, safety incident)'
    if re.search(r'body|privacy|hygiene',r): return 'child body / privacy'
    if re.search(r'autis|adhd|diagnos|delay|neuro|evaluat|therap',r): return 'diagnosis-centred'
    return 'unclassified'
c=collections.Counter(cls(r) for r in rows.values())
print('excluded units found in ledgers:',len(rows))
per=collections.Counter(k[0] for k in rows); print(dict(sorted(per.items())))
harsh=collections.Counter(k[0] for k,r in rows.items() if cls(r).startswith('parent or caregiver'))
print('harshness/force by reader:',dict(sorted(harsh.items())))
for k,v in c.most_common(): print(v,'|',k)
if os.environ.get('V'):
    for k,r in sorted(rows.items()): print(k,cls(r),'::',r.strip()[:140])
