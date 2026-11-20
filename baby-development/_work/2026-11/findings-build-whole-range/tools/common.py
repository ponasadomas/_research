import json,glob,os,re,csv
R=os.path.expanduser('~/GitHub/_research/baby-development')
def records():
    rec={}
    for f in sorted(glob.glob(R+'/quotes/reddit-sr*.jsonl'))+sorted(glob.glob(R+'/quotes/reddit-ar*.jsonl')):
        for l in open(f,encoding='utf-8'):
            if l.strip():
                r=json.loads(l); rec[r['id']]=r
    return rec
def posts():
    with open(R+'/evidence/2026-11/birth-to-48-months/posts.tsv',encoding='utf-8') as fh:
        return {row['post_id']:row for row in csv.DictReader(fh,delimiter='\t')}
BAND={'newborn_0_8_weeks':'0-6m','baby_2_4_months':'0-6m','baby_4_6_months':'0-6m','baby_6_9_months':'6-12m','baby_9_12_months':'6-12m',
'toddler_12_18_months':'12-18m','toddler_18_24_months':'18-24m','child_2_years':'2y','2.5-year-old':'2y','just turned 2':'2y','2-year-old':'2y','almost 3':'2y','almost 3-year-olds':'2y','2- and 5-year-olds':'2y',
'child_3_years':'3y','just turned 3':'3y','3.5-year-old':'3y','3-year-old':'3y'}
BANDS=['0-6m','6-12m','12-18m','18-24m','2y','3y']
def band(stage): return BAND.get(stage,'none')
def norm(s):
    for x,y in (("’","'"),("‘","'"),("“",'"'),("”",'"'),("\\n"," "),("\\","")): s=s.replace(x,y)
    return re.sub(r"\s+"," ",s).strip().lower()
def nq(s):
    for x,y in (("’","'"),("‘","'"),("“",'"'),("”",'"')): s=s.replace(x,y)
    return s
def locate(text,p):
    """find p in text ignoring curly/straight quote differences and whitespace runs; return (a,b) or None"""
    T=nq(text); P=nq(p)
    k=T.find(P)
    if k<0:
        P2=P.rstrip('.,;'); k=T.find(P2)
        if k<0:
            m=re.search(r'\s+'.join(re.escape(w) for w in P2.split()),T)
            if not m: return None
            return m.start(),m.end()
        return k,k+len(P2)
    return k,k+len(P)
def whole(text,a,b):
    """does text[a:b] start at a sentence start and end at a sentence end?"""
    pre=text[:a].rstrip(' ')
    startok = (a==0) or pre=='' or pre[-1] in '.!?…\n”"’\')*:;' or text[a-1]=='\n' or re.search(r'[.!?…]["”’\')\]]*\s*$',text[:a]) is not None
    seg=text[a:b].rstrip()
    post=text[b:]
    endok = (post.strip()=='') or re.match(r'^[.!?…]',post) is not None and False or seg[-1:] in '.!?…”"\')' and re.search(r'[.!?…]["”’\')]*$',seg) is not None or post.startswith('\n') or re.match(r'^\s*\n',post) is not None
    if not endok and re.match(r'^[.!?…]+["”’)]*(\s|$)',post): endok='punct'  # quote stops just before the final punctuation
    return startok,endok
def widen(text,a,b):
    s=a
    while s>0 and not (text[s-1]=='\n' or (text[s-1]==' ' and s>=2 and text[s-2] in '.!?…”"')): s-=1
    m=re.search(r'[.!?…]+["”’)]*(?=\s|$)|\n',text[max(b-1,0):])
    e=max(b-1,0)+m.end() if m else len(text)
    return text[s:e].strip()
