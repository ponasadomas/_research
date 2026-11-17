#!/usr/bin/env python3
"""Freeze full tier-A original posts and all available same-window comments.

This is a candidate corpus, not a claim that any item has been human-triaged/read.
Main-community comment absence is explicit in every affected unit. No thread is truncated.
"""
from pathlib import Path
import collections,datetime,gzip,hashlib,json

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/reddit-deep'
WINDOW=RAW/'windows/2025-h2-v1'
FILTER=RAW/'filter-v1'
OUT=RAW/'corpus-A-v1'

def stamp(t):return datetime.datetime.fromtimestamp(int(t),datetime.timezone.utc).isoformat()

def main():
    if OUT.exists():raise SystemExit('Frozen corpus exists: select a new version rather than rebuilding.')
    OUT.mkdir();(OUT/'units').mkdir();(OUT/'chunks').mkdir()
    candidates={q['id']:q for q in map(json.loads,(FILTER/'A-candidates.jsonl').read_text().splitlines())}
    comments=collections.defaultdict(list);commentfiles={};relation_stats={}
    for p in sorted(WINDOW.glob('*_comments.jsonl.gz')):
        sub=p.name.split('_comments')[0];commentfiles[sub]=str(p.relative_to(ROOT));n=matched=orphans=0
        with gzip.open(p,'rt') as f:
            for line in f:
                c=json.loads(line);n+=1;link=c.get('link_id','');postid=link.removeprefix('t3_')
                if postid in candidates:comments[postid].append(c);matched+=1
                else:orphans+=1
        relation_stats[sub]={'window_comments':n,'comments_joined_to_A_posts':matched,'comments_for_non_A_or_outside_window_posts':orphans}
    index=[];by_sub=collections.defaultdict(list)
    for p in sorted(WINDOW.glob('*_submissions.jsonl.gz')):
        with gzip.open(p,'rt') as f:
            for line in f:
                q=json.loads(line);id=q['id']
                if id not in candidates:continue
                cmeta=candidates[id];cs=sorted(comments.get(id,[]),key=lambda c:(int(c['created_utc']),c.get('id','')))
                sub=q['subreddit'];path=OUT/'units'/f'{sub}-{id}.txt'
                available=sub in commentfiles;op=q.get('author');op_known=bool(op and op not in ['[deleted]','[removed]']);opreplies=sum(1 for c in cs if op_known and c.get('author')==op)
                cids={c.get('id') for c in cs};missing_parent=sum(1 for c in cs if c.get('parent_id','').startswith('t1_') and c['parent_id'][3:] not in cids)
                meta={'post_id':id,'subreddit':sub,'url':cmeta['url'],'date':stamp(q['created_utc']),'title':q.get('title',''),'window':'2025-07-01 to2026-01-01 exclusive','source_post_file':str(p.relative_to(ROOT)),'source_comment_file':commentfiles.get(sub),'archive_comment_records':len(cs),'op_reply_records_identifiable':opreplies,'post_reported_num_comments':q.get('num_comments'),'comment_source_available':available,'comment_completeness':'all available archive comments within frozen window; live completeness unverified' if available else 'comment archive file absent at pinned publisher commit (404)','missing_referenced_comment_parents':missing_parent,'primary_topic':cmeta['primary_topic'],'topics':cmeta['topics'],'safety_flag':cmeta['safety_flag'],'triage_status':'untriaged','reading_status':'unread'}
                text='REDDIT ARCHIVED ORIGINAL POST AND AVAILABLE COMMENTS\n'+json.dumps(meta,ensure_ascii=False,indent=2)+'\n\n=== ORIGINAL POST TITLE ===\n'+q.get('title','')+'\n\n=== ORIGINAL POST BODY ===\n'+q.get('selftext','')+'\n\n=== COMMENTS ===\n'
                if not available:text+='COMMENT SOURCE UNAVAILABLE. Do not describe this unit as a complete original thread.\n'
                elif not cs:text+='No comments linked to this post in the available frozen archive window.\n'
                for c in cs:
                    isop=bool(op_known and c.get('author')==op)
                    cm={'id':c.get('id'),'created':stamp(c['created_utc']),'parent_id':c.get('parent_id'),'link_id':c.get('link_id'),'is_identifiable_OP_reply':isop,'score':c.get('score'),'url':f"https://www.reddit.com/r/{sub}/comments/{id}/_/{c.get('id','')}/"}
                    text+='\n--- ARCHIVED COMMENT ---\n'+json.dumps(cm,ensure_ascii=False)+'\n'+c.get('body','')+'\n'
                path.write_text(text)
                meta.update(raw_file=str(path.relative_to(ROOT)),utf8_bytes=len(text.encode()),sha256=hashlib.sha256(text.encode()).hexdigest())
                index.append(meta);by_sub[sub].append((meta,text))
    (OUT/'index.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in index))
    chunks=[]
    for sub,items in by_sub.items():
        buf='';ids=[];i=1
        def save(buf,ids,i):
            path=OUT/'chunks'/f'A-{sub}-{i:04d}.txt';path.write_text(buf)
            chunks.append({'file':str(path.relative_to(ROOT)),'post_ids':ids,'posts':len(ids),'utf8_bytes':len(buf.encode()),'oversize_single_thread':len(buf.encode())>40000,'triaged':False,'read':False})
        for meta,text in items:
            unit='\n\n======== SOURCE UNIT '+meta['raw_file']+' ========\n'+text
            if buf and len((buf+unit).encode())>40000:save(buf,ids,i);buf='';ids=[];i+=1
            buf+=unit;ids.append(meta['post_id'])
            if len(buf.encode())>40000:save(buf,ids,i);buf='';ids=[];i+=1
        if buf:save(buf,ids,i)
    (OUT/'chunks-index.jsonl').write_text(''.join(json.dumps(c)+'\n' for c in chunks))
    summary={'candidate_posts':len(index),'available_comments_in_units':sum(q['archive_comment_records'] for q in index),'identifiable_OP_replies':sum(q['op_reply_records_identifiable'] for q in index),'units_with_comment_source':sum(q['comment_source_available'] for q in index),'units_without_comment_source':sum(not q['comment_source_available'] for q in index),'units_with_missing_comment_parents':sum(q['missing_referenced_comment_parents']>0 for q in index),'reading_chunks':len(chunks),'reading_bytes':sum(c['utf8_bytes'] for c in chunks),'oversize_untruncated_thread_chunks':sum(c['oversize_single_thread'] for c in chunks),'by_subreddit':{s:{'posts':len(items),'comments':sum(q['archive_comment_records'] for q,_ in items),'chunks':sum(c['file'].split('/')[-1].startswith('A-'+s+'-') for c in chunks)} for s,items in by_sub.items()},'comment_relationships':relation_stats,'human_triaged':0,'kept_after_human_triage':0,'read':0,'quotes':0}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
