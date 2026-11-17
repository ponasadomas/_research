#!/usr/bin/env python3
"""Independent native-body/attribution and full-read audit for new wave03 evidence."""
from pathlib import Path
import json,gzip,hashlib,re,datetime,collections,sys
R=Path(__file__).resolve().parents[1];O=R/'_raw/audit/wave03-2026-10-24';base=json.loads((O/'baseline-frozen-hashes.json').read_text());oldnames={Path(p).name for p in base if '/voice/' in p};norm=lambda s:re.sub(r'\s+',' ',s).strip()
def jl(p):return [json.loads(s) for s in p.read_text().splitlines() if s.strip()]
def contains(body,quote):
 pos=0
 for part in re.split(r'\[(?:…|\.\.\.)\]',quote):
  part=norm(part)
  if not part:continue
  at=norm(body).find(part,pos)
  if at<0:return False
  pos=at+len(part)
 return True
quotes=[dict(q,_voice_file=p.name) for p in (R/'voice').glob('*.jsonl') if p.name not in oldnames for q in jl(p)];reddit=[q for q in quotes if q['source_class']=='reddit_archive']
ledgerpaths=[R/f'sources/reddit-country-B-{n:02}-reading.jsonl' for n in range(1,4)]+[R/'sources/reddit-country-B-03-duplicate-inspections.jsonl',R/'sources/reddit-report-purchases-v2-reading.jsonl',R/'sources/reddit-purchase-followups-wave03-reading.jsonl',R/'sources/reddit-index-leads-wave03-reading.jsonl',R/'sources/report-purchase-archive-wave03-reading.jsonl']+[R/f'sources/report-purchase-supplement-{n:02}-reading.jsonl' for n in [4,5]]
ledgers=[dict(x,_ledger=str(p.relative_to(R))) for p in ledgerpaths for x in jl(p)];wanted={q['post_id'] for q in reddit}|{x['post_id'] for x in ledgers};native={}
files=list((R/'_raw/reddit-deep/windows/2025-h2-v1').glob('*_submissions.jsonl.gz'))+list((R/'_raw/report-purchase-archive-wave03/window').glob('*_submissions.jsonl.gz'))
for p in files:
 with gzip.open(p,'rt') as f:
  for line in f:
   x=json.loads(line)
   if x['id'] in wanted:native[x['id']]=x
for directory in ['outside-window-discovery','index-leads-native-v2']:
 for p in (R/f'_raw/reddit-deep/report-purchases-v2/{directory}').glob('*.json'):
  x=json.loads(p.read_text())
  if x.get('id') and 'selftext' in x:native[x['id']]=x
errors=[];checks=collections.Counter()
def ck(ok,message,key):
 checks[key]+=1
 if not ok:errors.append(message)
for x in ledgers:
 pid=x['post_id'];n=native.get(pid);ck(n is not None,pid+': native missing','ledger_native_exists')
 if not n:continue
 p=R/x['raw_file'];ck(x['post_body_read_complete'] is True,pid+': incomplete','full_read_flag');ck(hashlib.sha256(p.read_bytes()).hexdigest()==x['primary_unit_sha256'],pid+': raw hash','unit_hash')
 t=p.read_text()
 if p.suffix=='.json':
  j=json.loads(t)
  if j.get('id')==pid and 'selftext' in j:t=j.get('title','')+'\n'+j['selftext']
 ck(norm(n['title']) in norm(t) and norm(n['selftext']) in norm(t),pid+': native full title/body missing','native_whole_title_body')
 ck(len(x['op_reply_ids_read'])==x['available_identifiable_OP_replies_read'],pid+': OP count','OP_ID_count')
for q in reddit:
 n=native.get(q['post_id']);ck(n is not None,q['id']+': native missing','quote_native_exists')
 if not n:continue
 ck(contains(n['selftext'],q['quote']),q['id']+': not exact own native body','quote_case_punctuation_native_body')
 url=n['permalink'];url='https://www.reddit.com'+url if url.startswith('/') else url;ck(q['url']==url,q['id']+': URL','native_permalink')
 dt=datetime.datetime.fromtimestamp(int(n['created_utc']),datetime.timezone.utc);published=q['date']
 ck(published[:10]==dt.date().isoformat(),q['id']+': date','native_date')
 if len(published)>10:
  try:ck(datetime.datetime.fromisoformat(published.replace('Z','+00:00'))==dt,q['id']+': timestamp','native_timestamp')
  except ValueError:errors.append(q['id']+': invalid timestamp')
 if q.get('author'):ck(q['author']==n.get('author'),q['id']+': author','native_author')
 ck(any(x['post_id']==q['post_id'] and x['post_body_read_complete'] for x in ledgers),q['id']+': missing full-read ledger','quote_fullread_link')
# Raw Apple review body and native review identity, not corpus metadata or seller copy.
for q in quotes:
 if q['source_class']!='app_review':continue
 candidates=[]
 for p in (R/'_raw/market-wave-03/reviews').glob('*.units.json'):
  m=json.loads(p.read_text());candidates +=[(m,x) for x in m['reviews'] if str(x['id'])==str(q.get('review_id'))]
 ck(len(candidates)==1,q['id']+': native review count','native_review_ID')
 if candidates:
  m,n=candidates[0];ck(q['quote'] in n['contents'] and q['date']==n['date'] and q['url']==m['url'],q['id']+': review body/date/URL','native_review_body_metadata')
# Dependence flags cover newly selected archived post bodies across all readers.
groups=collections.defaultdict(list)
for q in reddit:
 n=native[q['post_id']];author=n.get('author','')
 if author and author not in {'[deleted]','[removed]'}:groups[hashlib.sha256(author.encode()).hexdigest()].append({'post_id':q['post_id'],'quote_id':q['id'],'date':q['date'],'source':n['subreddit']})
flags=[{'native_author_sha256':a,'selected_posts':v} for a,v in groups.items() if len({x['post_id'] for x in v})>1];(O/'new-selected-author-dependence.json').write_text(json.dumps(flags,indent=2)+'\n')
for p,h in base.items():ck(Path(p).is_file() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p+': committed baseline changed','frozen_baseline_hash')
report={'new_quotes':len(quotes),'new_reddit_quotes':len(reddit),'new_read_occurrences':len(ledgers),'distinct_newwave_read_postIDs':len({x['post_id'] for x in ledgers}),'native_checks':dict(checks),'selected_repeated_author_groups_requiring_human_review':len(flags),'failed':len(errors),'errors':errors};(O/'native-source-audit.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));sys.exit(bool(errors))
