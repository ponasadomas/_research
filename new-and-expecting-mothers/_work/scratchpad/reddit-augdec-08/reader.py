import collections,gzip,hashlib,json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];S=Path(__file__).parent
W=R/'_raw/reddit-deep/aug-dec-2025-wave-v1'
M=json.loads((S/'full-read-v1/manifest.json').read_text())
I={u['post_id']:u for u in map(json.loads,(W/'primary-index.jsonl').read_text().splitlines())}
L=R/'sources/reddit-augdec-08-reading.jsonl';V=R/'voice/reddit-augdec-08.jsonl'
def jl(p):return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def view(n):
 c=M['chunks'][n-1];assert 1<=n<=20 and sha(R/c['file'])==c['sha256']
 for g in jl(W/'exact-body-duplicate-flags.jsonl'):
  if set(c['post_ids'])&{x['post_id'] for x in g['records']}:print('EXACT BODY DUPLICATE FLAG',json.dumps(g,ensure_ascii=False))
 print((R/c['file']).read_text(),end='')
def quotes(specs):
 prev=jl(V)
 for s in specs:
  u=I[s['post_id']];assert s['post_id'] in M['post_ids']
  q={'id':f'rad08-{len(prev)+1:04d}','source':'Reddit r/'+u['subreddit']+' — helper08 continuation','url':u['url'],'date':u['post_date'],'speaker':'parent_unspecified','stage':'unknown',**s,'raw_file':u['raw_file'],'source_class':'reddit_archive','evidence_kind':'archived_original','archive_dataset':'yikeee/reddit-subreddits25','archive_commit':'ea497c510aa68765c07ed744ec9f84d68bbedf7f','read_scope':'full_post_and_available_identifiable_OP_replies' if u['comment_source_available'] else 'full_post_comment_source_unavailable'}
  if q.get('comment_id'):
   with gzip.open(R/u['source_comment_file'],'rt') as f:
    for line in f:
     native=json.loads(line)
     if native['id']==q['comment_id']:
      import datetime
      q['date']=datetime.datetime.fromtimestamp(int(native['created_utc']),datetime.timezone.utc).isoformat();q['url']=native['permalink'] if native['permalink'].startswith('https://') else 'https://www.reddit.com'+native['permalink'];assert q['quote'] in native['body'];break
    else:raise ValueError('native comment absent')
  assert q['quote'] in (R/u['raw_file']).read_text() and len(q['context'].split())<=25
  with V.open('a') as f:f.write(json.dumps(q,ensure_ascii=False)+'\n')
  prev.append(q);print(q['id'],q['post_id'])
def save(n,ds):
 c=M['chunks'][n-1];assert sha(R/c['file'])==c['sha256']
 specs=[l.split('|',2) for l in ds.strip().splitlines()];assert [s[0] for s in specs]==c['post_ids'];prev=jl(L);assert not {s[0] for s in specs}&{r['post_id'] for r in prev}
 qs=jl(V)
 for pid,status,reason in specs:
  assert status in {'e','x'};u=I[pid];assert sha(R/u['raw_file'])==u['sha256']
  row={'post_id':pid,'raw_file':u['raw_file'],'post_body_read_complete':True,'available_identifiable_OP_replies_read':u['OP_replies'],'op_reply_ids_read':u['OP_comment_ids'],'primary_unit_sha256':u['sha256'],'status':'eligible' if status=='e' else 'read_pending_topic_review','reason':reason,'quote_ids':[q['id'] for q in qs if q['post_id']==pid],'reading_chunk':c['file']}
  with L.open('a') as f:f.write(json.dumps(row,ensure_ascii=False)+'\n')
 now=jl(L);p={'complete_originals':len(now),'OP_replies':sum(r['available_identifiable_OP_replies_read'] for r in now),'statuses':dict(collections.Counter(r['status'] for r in now)),'last_chunk':n};(S/'progress.json').write_text(json.dumps(p,indent=2)+'\n');print(json.dumps(p))
if __name__=='__main__':
 cmd=sys.argv[1]
 if cmd=='view':view(int(sys.argv[2]))
 if cmd=='quotes':quotes(json.load(sys.stdin))
 if cmd=='save':save(int(sys.argv[2]),sys.stdin.read())
