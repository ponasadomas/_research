#!/usr/bin/env python3
"""Verify current forum quotes against preserved post/raw text, disposition and read ledger."""
import collections,hashlib,json,pathlib,re,sys
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
from bs4 import BeautifulSoup
ROOT=pathlib.Path(__file__).resolve().parents[1]
effective=json.loads((ROOT/'sources/forums-deep-effective-kept-manifest.json').read_text());kept={x['thread_id']:x for x in effective['threads']}
counts=collections.Counter();ids=[];fail=[];total=0;contexts=[]
def norm(s):return re.sub(r'\s+',' ',s).strip()
def own(body):
    depth=0;out=[]
    for line in body.splitlines():
        if line=='[QUOTE FROM ANOTHER POST]':depth+=1
        elif line=='[/QUOTE]':depth-=1
        elif depth==0:out.append(line)
    return '\n'.join(out)
for f in sorted((ROOT/'voice').glob('forums-deep-*.jsonl')):
    for line in f.read_text().splitlines():
        q=json.loads(line);total+=1;ids.append(q['id']);wc=len(q['quote'].split());contexts.append(len(q['context'].split()))
        t=json.loads((ROOT/q['raw_thread_json']).read_text());p=next(x for x in t['posts'] if x['post_id']==q['post_id']);counts[p['author_handle'].lower()]+=wc
        html=BeautifulSoup((ROOT/q['raw_file']).read_bytes(),'html.parser').get_text(' ',strip=True)
        k=kept[q['thread_id']]
        checks={'raw_exact':norm(q['quote']) in norm(html),'own_post_exact':q['quote'] in own(p['body']),'quote_limit':wc<=25,'context_limit':len(q['context'].split())<=25,'raw_matches_post':q['raw_file']==p['raw_file'],'source_class':q['source_class']=='forum','kind':q['evidence_kind']=='original_thread_post','all_pages':t['pagination_complete'] and t['listed_count_matches'],'read':k['read_status']=='full','not_dropped':not k['final_disposition'].startswith('drop')}
        if not all(checks.values()):fail.append({'id':q['id'],'failed_checks':[x for x,v in checks.items() if not v]})
for a,n in counts.items():
    if n>25:fail.append({'author_word_budget':a,'words':n})
if len(ids)!=len(set(ids)):fail.append({'duplicate_ids':True})
stats=effective['stats']
if stats['retained_threads_unread'] or stats['retained_chunks_unread']:fail.append({'unread_kept':stats})
report={'quotes':total,'failed':len(fail),'failures':fail,'max_author_aggregate_quoted_words':max(counts.values()),'max_context_words':max(contexts),'corpus_stats':stats,'checks':'Exact own-post substring, normalized preserved HTML match, quote/context limits, cross-wave author aggregate, unique IDs, source metadata, not-dropped final disposition, full visible pagination/post counts, all required chunk reads.'}
(ROOT/'synthesis/forums-deep-quote-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,indent=2));assert not fail,fail
