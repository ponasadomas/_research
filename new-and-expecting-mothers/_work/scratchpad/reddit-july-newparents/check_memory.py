from work import R,W,M
import gzip,json,re,collections
ids=['1lt7fap','1m14kxp','1m4ezom','1m7h6ho','1lpm9q2']
def body(pid):return (R/M[pid]['raw_file']).read_text().split('=== COMPLETE ORIGINAL POST BODY ===\n',1)[1].split('\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===',1)[0].strip()
def grams(s):
 t=re.findall(r'\w+',s.lower());return set(zip(t,t[1:],t[2:],t[3:]))
target={p:grams(body(p)) for p in ids}; matches=[];read=[]
for f in sorted((R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz')):
 for ln,line in enumerate(gzip.open(f,'rt'),1):
  d=json.loads(line);s=d.get('selftext','');g=None
  for pid,t in target.items():
   # cheap exact word filter before four-word matching
   if not ('book' in s.lower() or 'photo' in s.lower()):continue
   if g is None:g=grams(s)
   shared=len(g&t);denom=min(len(g),len(t)) or 1
   if d['id']==pid or (shared>=12 and shared/denom>=.18):
    m={'target_id':pid,'matched_id':d['id'],'subreddit':d['subreddit'],'title':d['title'],'source_window':str(f.relative_to(R)),'line':ln,'shared_fourgrams':shared,'minimum_length_overlap':round(shared/denom,3),'body':s}
    matches.append(m)
  if re.search(r'welcome baby',s+' '+d.get('title',''),re.I) and re.search(r'book',s+' '+d.get('title',''),re.I):
   read.append({'post_id':d['id'],'subreddit':d['subreddit'],'title':d['title'],'source_window':str(f.relative_to(R)),'line':ln,'body':s})
(W/'memory-comparison.json').write_text(json.dumps({'targets':ids,'method':'All nine frozen H2 submission files scanned to EOF; shared exact normalized four-word sequences >=12 and min-length overlap >=0.18; plus Welcome Baby/book keyword check. Detection supports comparison, not authorship/authenticity claims.','matches':matches,'welcome_book_records':read},ensure_ascii=False,indent=2)+'\n')
for m in matches:
 if m['target_id']!=m['matched_id']: print(json.dumps(m,ensure_ascii=False))
print('WELCOME_BOOK')
for m in read:print(json.dumps(m,ensure_ascii=False))
print('comparison_matches',len(matches),'welcome_records',len(read))
