"""Freeze whole-thread reading units for every as-yet unread retained MSE thread.

Does not modify original captures or the first reader's frozen corpus. Allocation is
deterministic greedy balancing by whole-unit bytes, not relevance/outcome selection.
"""
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parents[1]
D=R/'_raw/oblique-deep'
OUT=D/'mse-completion-v1'
if OUT.exists(): raise SystemExit('Frozen output exists; refusing to overwrite')
OUT.mkdir(); (OUT/'units').mkdir()
items=[]
for row in map(json.loads,(D/'unread-threads.jsonl').read_text().splitlines()):
    if row['host_group']!='mse':continue
    obj=json.loads((R/row['thread_json']).read_text())
    assert obj['complete_visible_pagination'] and not obj['errors']
    text=f"THREAD MSE-{row['thread_id']}: {obj['title']}\nURL {obj['url']}\nPages {len(obj['pages'])}; posts {len(obj['posts'])}. Full visible discussion; repeated blockquotes/signatures omitted, native originals preserved.\n"
    for post in obj['posts']:
        text+=f"\nPOST {post['post_id']} | {'OP' if post['is_op'] else 'reply'} | author_id={post['author_id']} | {post['date']}\n{post['url']}\n{post['body']}\n"
    p=OUT/'units'/f"mse-{row['thread_id']}.txt";p.write_text(text)
    items.append({**row,'raw_file':str(p.relative_to(R)),'utf8_bytes':len(text.encode()),'sha256':hashlib.sha256(text.encode()).hexdigest()})
assert len(items)==313
groups=[[],[],[]];sizes=[0,0,0]
for x in sorted(items,key=lambda x:(-x['utf8_bytes'],x['thread_id'])):
    slot=min(range(3),key=lambda i:(sizes[i],i));groups[slot].append(x);sizes[slot]+=x['utf8_bytes']
summary=[]
for slot,rows in enumerate(groups,1):
    folder=OUT/f'batch-{slot:02}';folder.mkdir();rows.sort(key=lambda x:x['thread_id'])
    (folder/'manifest.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in rows))
    chunks=[];pending=[];size=0
    def flush():
        global pending,size
        if not pending:return
        p=folder/f'chunk-{len(chunks)+1:03}.txt'
        body='\n\n'+'\n\n'.join((R/x['raw_file']).read_text() for x in pending)
        p.write_text(body);chunks.append({'file':str(p.relative_to(R)),'thread_ids':[x['thread_id'] for x in pending],'utf8_bytes':len(body.encode())});pending=[];size=0
    for x in rows:
        if pending and size+x['utf8_bytes']>42000:flush()
        pending.append(x);size+=x['utf8_bytes']
        if size>=35000:flush()
    flush();(folder/'chunks.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in chunks))
    summary.append({'batch':slot,'threads':len(rows),'posts':sum(x['posts'] for x in rows),'pages':sum(x['pages'] for x in rows),'bytes':sizes[slot-1],'chunks':len(chunks)})
(OUT/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2))
