#!/usr/bin/env python3
"""Freeze all July2025 tier-A cards and full-post-plus-OP-reply primary units.

No network, new quotations, ranking or automatic keep decisions. All non-OP
archived comments remain in a separate unread auxiliary queue.
"""
from pathlib import Path
import collections,datetime,gzip,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/reddit-deep'
WINDOW=RAW/'windows/2025-h2-v1'
OUT=RAW/'july-2025-wave-v1'

def stamp(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()
def rel(p):return str(p.relative_to(ROOT))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    if OUT.exists():raise SystemExit('Frozen July packet exists; use a new version rather than rebuild.')
    OUT.mkdir()
    for d in ['triage-cards','primary-units','primary-chunks','auxiliary-comments']:(OUT/d).mkdir()
    baseline={rel(p):sha(p) for p in [RAW/'filter-v1/summary.json',RAW/'filter-v1/cards-index.jsonl',RAW/'corpus-A-v1/index.jsonl',RAW/'corpus-A-v1/chunks-index.jsonl',RAW/'reading-queue-v1.tsv']}
    all_A=list(map(json.loads,(RAW/'filter-v1/A-candidates.jsonl').read_text().splitlines()))
    start=int(datetime.datetime(2025,7,1,tzinfo=datetime.timezone.utc).timestamp());end=int(datetime.datetime(2025,8,1,tzinfo=datetime.timezone.utc).timestamp())
    selected={q['id']:q for q in all_A if start<=int(q['created_utc'])<end}
    (OUT/'candidates.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in sorted(selected.values(),key=lambda q:(q['subreddit'],int(q['created_utc']),q['id']))))
    posts={}
    for p in sorted(WINDOW.glob('*_submissions.jsonl.gz')):
        with gzip.open(p,'rt') as f:
            for line in f:
                q=json.loads(line)
                if q['id'] in selected:posts[q['id']]=(q,p)
    assert set(posts)==set(selected),'Every selected July candidate must have its full original post.'
    comments=collections.defaultdict(list);comment_sources={}
    for p in sorted(WINDOW.glob('*_comments.jsonl.gz')):
        sub=p.name.split('_comments')[0];comment_sources[sub]=p
        with gzip.open(p,'rt') as f:
            for line in f:
                c=json.loads(line);postid=c.get('link_id','').removeprefix('t3_')
                if postid in selected:comments[postid].append((c,line))
    primary_index=[];aux_index=[];card_chunks=[];primary_chunks=[];by_sub=collections.defaultdict(list)
    for id,candidate in selected.items():by_sub[candidate['subreddit']].append(candidate)
    for sub,cs in sorted(by_sub.items()):
        cs.sort(key=lambda q:(int(q['created_utc']),q['id']))
        cardbuf='';cardids=[];cardnum=1;primarybuf='';primaryids=[];primarynum=1
        def savecards(buf,ids,num):
            p=OUT/'triage-cards'/f'July-A-{sub}-{num:03d}.txt';p.write_text(buf)
            card_chunks.append({'file':rel(p),'subreddit':sub,'post_ids':ids,'cards':len(ids),'utf8_bytes':len(buf.encode()),'triage_status':'untriaged'})
        def saveprimary(buf,ids,num):
            p=OUT/'primary-chunks'/f'July-A-{sub}-{num:03d}.txt';p.write_text(buf)
            primary_chunks.append({'file':rel(p),'subreddit':sub,'post_ids':ids,'posts':len(ids),'utf8_bytes':len(buf.encode()),'oversize_single_unit':len(buf.encode())>40000,'triage_status':'untriaged','read_status':'unread'})
        for candidate in cs:
            id=candidate['id'];q,source_post=posts[id];op=q.get('author');known=bool(op and op not in ['[deleted]','[removed]']);linked=sorted(comments.get(id,[]),key=lambda pair:(int(pair[0]['created_utc']),pair[0].get('id','')))
            op_comments=[pair for pair in linked if known and pair[0].get('author')==op]
            other_comments=[pair for pair in linked if not(known and pair[0].get('author')==op)]
            available=sub in comment_sources
            auxpath=None
            if other_comments:
                auxpath=OUT/'auxiliary-comments'/f'{sub}-{id}.jsonl.gz'
                with gzip.open(auxpath,'wt',encoding='utf8',compresslevel=6) as f:
                    for c,line in other_comments:f.write(line)
            aux_index.append({'post_id':id,'subreddit':sub,'file':rel(auxpath) if auxpath else None,'comments':len(other_comments),'comment_ids':[c.get('id') for c,_ in other_comments],'compressed_bytes':auxpath.stat().st_size if auxpath else 0,'read_status':'unread','source_comment_file':rel(comment_sources[sub]) if available else None})
            meta={'post_id':id,'subreddit':sub,'url':candidate['url'],'post_date':stamp(q['created_utc']),'selection':'every tier-A post created in calendar July2025; no ranking or cap','primary_read_scope':'complete_original_post_plus_all_available_identifiable_OP_replies' if available else 'complete_original_post_only_comment_source_unavailable','source_post_file':rel(source_post),'source_comment_file':rel(comment_sources[sub]) if available else None,'source_window_end_exclusive':'2026-01-01T00:00:00+00:00','OP_identifiable':known,'OP_replies':len(op_comments),'OP_comment_ids':[c.get('id') for c,_ in op_comments],'non_OP_comments_in_separate_unread_auxiliary':len(other_comments),'auxiliary_file':rel(auxpath) if auxpath else None,'post_reported_num_comments':q.get('num_comments'),'archive_live_completeness':'unverified','tier':'A','primary_topic':candidate['primary_topic'],'topics':candidate['topics'],'safety_flag':candidate['safety_flag'],'triage_status':'untriaged','read_status':'unread'}
            text='ARCHIVED ORIGINAL — JULY CANDIDATE PRIMARY READING UNIT\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n=== COMPLETE ORIGINAL POST TITLE ===\n'+q.get('title','')+'\n\n=== COMPLETE ORIGINAL POST BODY ===\n'+q.get('selftext','')+'\n\n=== ALL AVAILABLE IDENTIFIABLE OP REPLIES ===\n'
            if not available:text+='OP follow-ups unavailable: this publisher has no comment file for this community at the pinned commit.\n'
            elif not known:text+='OP author is deleted/unknown; no comment is attributed to OP by matching deleted names. Other available comments remain unread auxiliary material.\n'
            elif not op_comments:text+='No identifiable OP replies found among the available archived comments through2025-12-31. This does not prove none existed live.\n'
            for c,_ in op_comments:
                cm={'comment_id':c.get('id'),'date':stamp(c['created_utc']),'parent_id':c.get('parent_id'),'url':f"https://www.reddit.com/r/{sub}/comments/{id}/_/{c.get('id','')}/"}
                text+='\n--- OP REPLY ---\n'+json.dumps(cm,ensure_ascii=False)+'\n'+c.get('body','')+'\n'
            p=OUT/'primary-units'/f'{sub}-{id}.txt';p.write_text(text)
            mi=dict(meta,raw_file=rel(p),utf8_bytes=len(text.encode()),post_body_bytes=len(q.get('selftext','').encode()),OP_body_bytes=sum(len(c.get('body','').encode()) for c,_ in op_comments),sha256=sha(p));primary_index.append(mi)
            body=q.get('selftext','');card=f"ID {id} | r/{sub} | {candidate['date']} | {candidate['primary_topic']} | safety_flag={candidate['safety_flag']}\nTITLE: {q.get('title','')}\nOPENING: {body[:350]}\nMATCHES: "+json.dumps(candidate['matches'],ensure_ascii=False)+'\n'
            if cardbuf and len((cardbuf+card).encode())>40000:savecards(cardbuf,cardids,cardnum);cardbuf='';cardids=[];cardnum+=1
            cardbuf+=card+'\n';cardids.append(id)
            unit='\n\n======== PRIMARY UNIT '+rel(p)+' ========\n'+text
            if primarybuf and len((primarybuf+unit).encode())>40000:saveprimary(primarybuf,primaryids,primarynum);primarybuf='';primaryids=[];primarynum+=1
            primarybuf+=unit;primaryids.append(id)
            if len(primarybuf.encode())>40000:saveprimary(primarybuf,primaryids,primarynum);primarybuf='';primaryids=[];primarynum+=1
        if cardbuf:savecards(cardbuf,cardids,cardnum)
        if primarybuf:saveprimary(primarybuf,primaryids,primarynum)
    for name,rows in [('primary-index.jsonl',primary_index),('auxiliary-index.jsonl',aux_index),('triage-cards-index.jsonl',card_chunks),('primary-chunks-index.jsonl',primary_chunks)]:
        (OUT/name).write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in rows))
    summary={'calendar_selection_start':'2025-07-01T00:00:00+00:00','calendar_selection_end_exclusive':'2025-08-01T00:00:00+00:00','source_followup_window_end_exclusive':'2026-01-01T00:00:00+00:00','all_six_month_A_candidates':len(all_A),'July_A_candidates':len(selected),'August_December_A_candidates_unselected_untriaged_unread':len(all_A)-len(selected),'ranking_or_topN_cap':False,'by_subreddit':{},'by_primary_topic':dict(collections.Counter(q['primary_topic'] for q in selected.values())),'by_any_topic':dict(collections.Counter(t for q in selected.values() for t in q['topics'])),'triage_card_chunks':len(card_chunks),'primary_reading_chunks':len(primary_chunks),'primary_reading_utf8_bytes':sum(q['utf8_bytes'] for q in primary_chunks),'complete_post_body_bytes':sum(q['post_body_bytes'] for q in primary_index),'OP_reply_body_bytes':sum(q['OP_body_bytes'] for q in primary_index),'identifiable_OP_replies':sum(q['OP_replies'] for q in primary_index),'available_non_OP_auxiliary_comments':sum(q['comments'] for q in aux_index),'auxiliary_compressed_bytes':sum(q['compressed_bytes'] for q in aux_index),'auxiliary_comment_files':sum(q['file'] is not None for q in aux_index),'human_triaged':0,'human_kept':0,'full_primary_units_read':0,'auxiliary_comments_read':0,'quotes':0}
    for sub,items in sorted(by_sub.items()):
        ps=[q for q in primary_index if q['subreddit']==sub];auxs=[q for q in aux_index if q['subreddit']==sub]
        summary['by_subreddit'][sub]={'A_candidates':len(items),'primary_topics':dict(collections.Counter(q['primary_topic'] for q in items)),'comment_source_available':sub in comment_sources,'identifiable_OP_replies':sum(q['OP_replies'] for q in ps),'non_OP_auxiliary_comments_unread':sum(q['comments'] for q in auxs),'triage_card_chunks':sum(q['subreddit']==sub for q in card_chunks),'primary_reading_chunks':sum(q['subreddit']==sub for q in primary_chunks)}
    assert set(q for x in card_chunks for q in x['post_ids'])==set(selected)
    assert len([q for x in card_chunks for q in x['post_ids']])==len(selected)
    assert set(q for x in primary_chunks for q in x['post_ids'])==set(selected)
    assert len([q for x in primary_chunks for q in x['post_ids']])==len(selected)
    for p,hash in baseline.items():assert sha(ROOT/p)==hash,f'Frozen baseline changed: {p}'
    (OUT/'six-month-baseline-hashes.json').write_text(json.dumps(baseline,indent=2)+'\n')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    with (OUT/'primary-reading-queue.tsv').open('w') as f:
        f.write('chunk\tsubreddit\tpost_count\tbytes\ttriage_status\tread_status\n')
        for q in primary_chunks:f.write(f"{q['file']}\t{q['subreddit']}\t{q['posts']}\t{q['utf8_bytes']}\tuntriaged\tunread\n")
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
