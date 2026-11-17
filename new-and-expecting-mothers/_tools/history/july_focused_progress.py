from july_focused_reader import *

def record(number, note, exclusions=None):
    exclusions=exclusions or {}
    index=[json.loads(x) for x in (ROOT/'_raw/reddit-deep/july-focused-reading-v1/index.jsonl').read_text().splitlines()]
    chunk=index[number-1]
    ids=chunk['post_ids']
    assert all(x in ids for x in exclusions)
    accepted=[x for x in ids if x not in exclusions]
    mark_read(accepted, f'Complete primary reading view {number:03}; '+note)
    for tid, reason in exclusions.items():
        mark_read([tid],f'Complete primary reading view {number:03}; '+note,excluded=reason)
    path=ROOT/'sources/reddit-july-focused-chunk-notes.jsonl'
    rec={'chunk':number,'file':chunk['file'],'post_ids':ids,'all_primary_text_and_available_OP_replies_read':True,'post_read_exclusions':exclusions,'note':note,'read_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
    with path.open('a') as f:f.write(json.dumps(rec,ensure_ascii=False)+'\n')
    print('Completed view',number,'units',len(ids),'accepted',len(accepted),'post-read exclusions',len(exclusions))
