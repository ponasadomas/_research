import json,sys,glob,re
ids=set(sys.argv[1:])
pat=re.compile(r"[^.!?]*\b(my sleep|I'?m (so |very |beyond )?(tired|exhausted|sleep)|sleep[- ]deprived|exhaust|my husband|my partner|shifts?|insomnia|I (can'?t|cannot|haven'?t|only|get|got) [^.]{0,30}(sleep|slept)|back to work|hours? of sleep|zombie|burn)[^.!?]*[.!?]",re.I)
for f in glob.glob('_shared/_raw/reddit-2026/*.posts.jsonl'):
    for l in open(f):
        d=json.loads(l)
        if d.get('id') in ids:
            t=(d.get('title') or '')+' || '+(d.get('selftext') or '').replace('\n',' ')
            m=[x.group(0).strip()[:220] for x in pat.finditer(t)][:4]
            print('##',d['id'],len(t),' ## '.join(m),'\n')
