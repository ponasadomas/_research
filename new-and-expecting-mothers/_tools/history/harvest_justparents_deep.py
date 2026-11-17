#!/usr/bin/env python3
"""Whole finite JustParents board inventories and all visible thread pagination.

Requires beautifulsoup4 (temporary dependency at /tmp/mamivio-forums-vendor).
Public requests only; default requests identity, no login/cookies/UA switching.
Raw responses are preserved before parsing. 1.1s request spacing, one host worker.
"""
import datetime, hashlib, json, pathlib, re, sys, time, urllib.parse
sys.path.insert(0,'/tmp/mamivio-forums-vendor')
import requests
from bs4 import BeautifulSoup

ROOT=pathlib.Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/forums-deep/justparents'
SCRATCH=ROOT/'scratchpad/forums-deep'
for p in [RAW/'responses',RAW/'threads',RAW/'boards',SCRATCH]:p.mkdir(parents=True,exist_ok=True)
BOARDS=['feeding','baby','work-childcare','third-trimester','birth-labour','second-trimester','first-trimester','activities']
BASE='https://www.justparents.co.uk'
last=0

def fetch(url):
    global last
    key=hashlib.sha256(url.encode()).hexdigest()[:20]
    meta_path=RAW/'responses'/f'{key}.json'; body_path=RAW/'responses'/f'{key}.html'
    if meta_path.exists() and body_path.exists():
        meta=json.loads(meta_path.read_text());return meta,BeautifulSoup(body_path.read_bytes(),'html.parser')
    time.sleep(max(0,1.1-(time.monotonic()-last)))
    at=datetime.datetime.now(datetime.timezone.utc).isoformat()
    r=requests.get(url,timeout=30); last=time.monotonic()
    body_path.write_bytes(r.content)
    meta={'requested_url':url,'final_url':r.url,'status':r.status_code,'headers':dict(r.headers),'fetched_at':at,'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest(),'raw_file':str(body_path.relative_to(ROOT))}
    meta_path.write_text(json.dumps(meta,ensure_ascii=False,indent=2))
    bs=BeautifulSoup(r.content,'html.parser')
    title=bs.title.get_text() if bs.title else ''
    if r.status_code!=200 or any(x in title.lower() for x in ['just a moment','checking your browser','captcha','attention required']):
        raise RuntimeError(f'Content wall/error; no retry or bypass: {url} {r.status_code} {title}')
    return meta,bs

def page_links(bs,prefix):
    return sorted({urllib.parse.urljoin(BASE,a['href']).split('#')[0] for a in bs.select('nav.jp-pagination a[href]') if re.fullmatch(re.escape(prefix)+r'(?:page/\d+/)?',urllib.parse.urlsplit(urllib.parse.urljoin(BASE,a['href'])).path)})

def listings(board):
    prefix=f'/forums/{board}/';pending=[BASE+prefix];seen=set();topics={};pages=[];expected=None
    while pending:
        url=pending.pop(0)
        if url in seen:continue
        meta,bs=fetch(url);seen.add(url);pages.append(meta)
        if expected is None:
            stat=bs.select_one('.jp-feature-panel__stat-value')
            expected=int(stat.get_text(strip=True).replace(',','')) if stat else None
        for tr in bs.select('tr[data-jp-row-link]'):
            link=tr['data-jp-row-link'];a=tr.select_one('.jp-forum-topic-titleline a');cells=tr.find_all('td')
            topics[link]={'url':BASE+link,'title':a.get_text(' ',strip=True),'listed_replies':int(cells[2].get_text(' ',strip=True)),'last_reply_as_displayed':cells[3].get_text(' ',strip=True),'board':board,'listing_raw_file':meta['raw_file']}
        pending.extend(u for u in page_links(bs,prefix) if u not in seen)
    result={'board':board,'expected_displayed_topics':expected,'unique_topics':len(topics),'pages':pages,'topics':list(topics.values())}
    (RAW/'boards'/f'{board}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    print(json.dumps({'event':'board_inventory','board':board,'pages':len(pages),'unique_topics':len(topics),'displayed_count':expected}),flush=True)
    return result

def clean_body(node):
    node=BeautifulSoup(str(node),'html.parser')
    for x in node(['script','style']):x.decompose()
    for q in node.select('blockquote'):
        q.insert_before('\n[QUOTE FROM ANOTHER POST]\n');q.insert_after('\n[/QUOTE]\n')
    text=node.get_text('\n',strip=True)
    return re.sub(r'\n{3,}','\n\n',text).strip()

def thread(topic):
    tid=re.search(r'topic-(\d+)',topic['url']).group(1);outpath=RAW/'threads'/f'{tid}.json'
    if outpath.exists():return json.loads(outpath.read_text())
    prefix=f'/forums/topic-{tid}/';pending=[topic['url']];seen=set();posts={};pages=[];title=topic['title']
    while pending:
        url=pending.pop(0)
        if url in seen:continue
        meta,bs=fetch(url);seen.add(url);pages.append(meta)
        h=bs.select_one('main h1');title=h.get_text(' ',strip=True) if h else title
        for b in bs.select('main div[id^="msg"]'):
            pid=b['id'][3:]
            if not pid.isdigit():continue
            head=bs.find(id=pid);author=head.select_one('a.big') if head else None;date=head.select_one('.jp-thread-post-header__meta') if head else None
            posts[pid]={'post_id':pid,'author_handle':author.get_text(' ',strip=True) if author else None,'date_as_displayed':date.get_text(' ',strip=True) if date else None,'body':clean_body(b),'permalink':BASE+prefix+'#'+pid,'raw_file':meta['raw_file'],'page_url':url}
        pending.extend(u for u in page_links(bs,prefix) if u not in seen)
    vals=list(posts.values())
    for i,p in enumerate(vals):p.update(role='original_post' if i==0 else 'response',original_post_id=vals[0]['post_id'] if vals else None)
    out={**topic,'thread_id':'jp-'+tid,'title':title,'pagination_complete':True,'visible_pages_fetched':len(pages),'visible_post_count':len(vals),'listed_expected_posts':topic['listed_replies']+1,'listed_count_matches':len(vals)==topic['listed_replies']+1,'pages':pages,'posts':vals}
    outpath.write_text(json.dumps(out,ensure_ascii=False,indent=2))
    return out

def freeze_board(board,threads):
    chunks=[];entries=[];current='';current_ids=[];chunknum=0
    def flush():
        nonlocal current,current_ids,chunknum
        if not current:return
        chunknum+=1;p=SCRATCH/f'justparents-{board}-{chunknum:03}.txt';p.write_text(current)
        chunks.append({'file':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'thread_ids':list(dict.fromkeys(current_ids)),'read_status':'unread'})
        current='';current_ids=[]
    for t in threads:
        for i,p in enumerate(t['posts']):
            block=f"\n=== THREAD {t['thread_id']} | {t['title']} | board={board} | pagecount={t['visible_pages_fetched']} | postcount={t['visible_post_count']} ===\nURL: {t['url']}\nPOST {p['post_id']} | {p['role']} | original={p['original_post_id']} | {p['date_as_displayed']}\nPERMALINK: {p['permalink']}\nRAW: {p['raw_file']}\n{p['body']}\n"
            if current and len((current+block).encode())>41000:flush()
            current+=block;current_ids.append(t['thread_id'])
        entries.append({'thread_id':t['thread_id'],'board':board,'title':t['title'],'url':t['url'],'raw_thread_json':str((RAW/'threads'/f"{t['thread_id'][3:]}.json").relative_to(ROOT)),'pages':t['visible_pages_fetched'],'posts':t['visible_post_count'],'pagination_complete':t['pagination_complete'],'listed_count_matches':t['listed_count_matches'],'read_status':'unread'})
    flush()
    (SCRATCH/f'justparents-{board}-manifest.json').write_text(json.dumps({'board':board,'chunks':chunks,'threads':entries},ensure_ascii=False,indent=2))
    print(json.dumps({'event':'board_frozen','board':board,'threads':len(threads),'posts':sum(t['visible_post_count'] for t in threads),'chunks':len(chunks),'bytes':sum(c['bytes'] for c in chunks)}),flush=True)

if __name__=='__main__':
    boards=sys.argv[1:] or BOARDS
    for board in boards:
        inventory=listings(board)
        harvested=[]
        for i,topic in enumerate(inventory['topics']):
            t=thread(topic);harvested.append(t)
            if i%20==19:print(json.dumps({'event':'thread_progress','board':board,'done':i+1,'total':len(inventory['topics'])}),flush=True)
        freeze_board(board,harvested)
