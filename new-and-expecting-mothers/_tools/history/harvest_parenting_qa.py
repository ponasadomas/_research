#!/usr/bin/env python3
"""Official Stack Exchange API corpus, separate from restricted HTML crawling.
Raw response bytes + headers are saved before decoding; only documented read endpoints.
Question inventory: every available Parenting question created 2020-01-01..2026-10-24.
Locally select broad pregnancy/infancy candidates, then fetch all available answers/comments.
"""
from pathlib import Path
import datetime as dt, gzip, html, json, re, sys, time, urllib.parse, urllib.request
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/qa-deep'
for d in [RAW,RAW/'responses',RAW/'threads',ROOT/'scratchpad/qa-deep']:d.mkdir(exist_ok=True)
sys.path.insert(0,str(ROOT/'_tools'))
from fetch_page import extract
MANIFEST=[]

def ts(s):return int(dt.datetime.fromisoformat(s).replace(tzinfo=dt.timezone.utc).timestamp())
def get(path,params,label):
    url='https://api.stackexchange.com/2.3/'+path+'?'+urllib.parse.urlencode(params)
    saved=RAW/'responses'/(label+'.json')
    if saved.exists():return json.loads(saved.read_text())
    req=urllib.request.Request(url,headers={'User-Agent':'MamivioResearch/1.0 (public API research; no authentication)'})
    with urllib.request.urlopen(req,timeout=45) as resp:
        b=resp.read();headers=dict(resp.headers);code=resp.status
    ext='.json.gz' if b.startswith(b'\x1f\x8b') else '.json.raw'
    (RAW/'responses'/(label+ext)).write_bytes(b)
    (RAW/'responses'/(label+'.headers.json')).write_text(json.dumps(headers,indent=2))
    text=(gzip.decompress(b) if ext=='.json.gz' else b).decode()
    d=json.loads(text);saved.write_text(text)
    MANIFEST.append({'url':url,'status':code,'raw_file':str((RAW/'responses'/(label+ext)).relative_to(ROOT)),'label':label,'count':len(d.get('items',[])),'has_more':d.get('has_more'),'quota_remaining':d.get('quota_remaining')})
    with (RAW/'request-manifest.jsonl').open('a') as f:f.write(json.dumps(MANIFEST[-1])+'\n')
    if d.get('error_id'):raise RuntimeError(d)
    if d.get('backoff'):time.sleep(d['backoff'])
    time.sleep(.35)
    return d

questions={}
for year in range(2020,2027):
    before=f'{year+1}-01-01' if year<2026 else '2026-10-25'
    for page in range(1,26):
        d=get('questions',dict(site='parenting',pagesize=100,page=page,filter='withbody',sort='creation',order='asc',fromdate=ts(f'{year}-01-01'),todate=ts(before)-1),f'questions-{year}-{page:02}')
        for q in d.get('items',[]):questions[q['question_id']]=q
        print('questions',year,page,len(d.get('items',[])),'total',len(questions),flush=True)
        if not d.get('has_more'):break
    else:raise RuntimeError(f'Anonymous pagination limit reached for {year}; split documented date window before continuing')
(RAW/'all-questions.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in questions.values()))
pat=re.compile(r'newborn|new.born|infant|pregnan|breast.?feed|breast.?milk|bottle.?feed|formula|pumping|post.?partum|weaning|baby.?led|tummy.?time|first.?foods|starting.?solids|baby.?registry|stroller|pram|baby.?carrier|maternity|paternity|(?:\d{1,2})[- ]?(?:month|week)[- ]old',re.I)
tags={'infant','newborn','pregnancy','breastfeeding','bottle-feeding','weaning','baby-proofing','baby-carrier','postpartum','formula','first-time-parent'}
candidates=[]
for q in questions.values():
    t=q.get('title','')+' '+q.get('body','')+' '+' '.join(q.get('tags',[]))
    if pat.search(t) or tags.intersection(q.get('tags',[])):candidates.append(q)
(RAW/'candidates.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in candidates))
cards=[]
for q in candidates:
    body=extract(q.get('body',''))[2]
    cards.append(f"Q{q['question_id']} | {q['title']} | {','.join(q.get('tags',[]))}\n{body[:500]}\n")
(RAW/'triage-cards.txt').write_text('\n'.join(cards))
print('LOCAL FILTER',len(questions),'questions ->',len(candidates),'candidates',flush=True)
answers={};qids=[q['question_id'] for q in candidates]
for batch in range(0,len(qids),100):
    ids=qids[batch:batch+100]
    for page in range(1,26):
        d=get('questions/'+';'.join(map(str,ids))+'/answers',dict(site='parenting',pagesize=100,page=page,filter='withbody',sort='creation',order='asc'),f'answers-{batch//100:02}-{page:02}')
        for a in d.get('items',[]):answers[a['answer_id']]=a
        print('answers',batch//100,page,len(d.get('items',[])),flush=True)
        if not d.get('has_more'):break
    else:raise RuntimeError('Answer pagination incomplete')
(RAW/'all-candidate-answers.jsonl').write_text(''.join(json.dumps(a,ensure_ascii=False)+'\n' for a in answers.values()))
postids=qids+list(answers);comments={}
for batch in range(0,len(postids),100):
    ids=postids[batch:batch+100]
    for page in range(1,26):
        d=get('posts/'+';'.join(map(str,ids))+'/comments',dict(site='parenting',pagesize=100,page=page,filter='withbody',sort='creation',order='asc'),f'comments-{batch//100:02}-{page:02}')
        for c in d.get('items',[]):comments[c['comment_id']]=c
        print('comments',batch//100,page,len(d.get('items',[])),flush=True)
        if not d.get('has_more'):break
    else:raise RuntimeError('Comment pagination incomplete')
(RAW/'all-candidate-comments.jsonl').write_text(''.join(json.dumps(c,ensure_ascii=False)+'\n' for c in comments.values()))
index=[]
for q in candidates:
    id=q['question_id'];aa=[a for a in answers.values() if a['question_id']==id];ids={id}|{a['answer_id'] for a in aa};cc=[c for c in comments.values() if c['post_id'] in ids]
    bundle={'question':q,'answers':aa,'comments':cc}
    (RAW/'threads'/f'{id}.json').write_text(json.dumps(bundle,ensure_ascii=False,indent=2))
    out=[f"SOURCE: Stack Exchange Parenting, official API v2.3\nTHREAD: {id}\nURL: {q['link']}\nCREATED: {dt.datetime.fromtimestamp(q['creation_date'],dt.timezone.utc).isoformat()}\nTITLE: {html.unescape(q['title'])}\nTAGS: {','.join(q.get('tags',[]))}\n"]
    for typ,p in [('QUESTION',q)]+[('ANSWER',a) for a in aa]:
        pid=p.get('question_id') if typ=='QUESTION' else p['answer_id']
        out.append(f"\n{typ} {pid} | owner_id={p.get('owner',{}).get('user_id','unknown')} | license={p.get('content_license','unspecified')}\n"+extract(p.get('body',''))[2]+'\n')
        for c in cc:
            if c['post_id']==pid:out.append(f"COMMENT {c['comment_id']} | owner_id={c.get('owner',{}).get('user_id','unknown')}\n"+extract(c.get('body',''))[2]+'\n')
    p=RAW/'threads'/f'{id}.txt';p.write_text('\n'.join(out))
    index.append({'id':id,'url':q['link'],'title':html.unescape(q['title']),'date':dt.datetime.fromtimestamp(q['creation_date'],dt.timezone.utc).date().isoformat(),'answers':len(aa),'comments':len(cc),'raw_file':str(p.relative_to(ROOT)),'full_available_api_relations_saved':True})
(RAW/'thread-index.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in index))
print('DONE',len(questions),'questions downloaded;',len(index),'candidate threads;',len(answers),'answers;',len(comments),'comments',flush=True)
