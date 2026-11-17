import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
WORK = Path(__file__).parent
MANIFEST = [json.loads(x) for x in (ROOT/'_raw/oblique-deep/mse-completion-v2/batch-02/manifest.jsonl').read_text().splitlines()]
BYID = {x['thread_id']:x for x in MANIFEST}

def read_chunk(n, start=0, stop=None):
    c = json.loads((ROOT/'_raw/oblique-deep/mse-completion-v2/batch-02/chunks.jsonl').read_text().splitlines()[n-1])
    for i in c['thread_ids']:
        dp=WORK/'decisions.json'
        prior=json.loads(dp.read_text()).get('threads',{}) if dp.exists() else {}
        if prior.get(i,{}).get('status')=='partial_safety_excluded':
            print('\nTHREAD',i,'OP screened; safety excluded; remaining posts deliberately unread')
            continue
        t=json.loads((ROOT/BYID[i]['thread_json']).read_text())
        print('\nTHREAD',i,t['title'])
        seen={}
        for p in t['posts'][start:stop]:
            body=p.get('body_with_quotes',p['body'])
            # Every unique paragraph remains verbatim. Exact paragraphs already
            # displayed in this same thread are explicit reading references.
            out=[]
            for para in body.split('\n\n'):
                if len(para)>80 and para in seen:
                    out.append('[Exact repeated paragraph already read in '+seen[para]+']')
                else:
                    out.append(para)
                    seen[para]=p['post_id']
            print('\n',p['post_id'],'OP' if p['is_op'] else 'reply','\n'+'\n\n'.join(out))

def save_update(data):
    path=WORK/'decisions.json'
    d=json.loads(path.read_text()) if path.exists() else {'threads':{},'quotes':[]}
    for t in data.get('threads',[]):
        i=t.pop('thread_id'); assert i not in d['threads'],i
        m=BYID[i]
        t.setdefault('status','full');t.setdefault('fully_read',True)
        t.setdefault('posts_read',m['posts']);t.setdefault('post_read_eligible',m['posts'])
        t['posts_total']=m['posts'];t['raw_file']=m['raw_file']
        d['threads'][i]=t
    for q in data.get('quotes',[]):
        i=q['thread_id'];m=BYID[i];t=json.loads((ROOT/m['thread_json']).read_text())
        p=next(p for p in t['posts'] if p['post_id']==q['post_id'])
        assert q['quote'] in p.get('body_with_quotes',p['body']), q
        q.update(id=f"odeep04-{len(d['quotes'])+1:04d}",source='mse-forum',url=p['url'],date=p['date'][:10],raw_file=m['raw_file'],source_class='forum_oblique',evidence_kind='original_thread_post',is_op=p['is_op'],author_id=p.get('author_id') or 'unknown')
        d['quotes'].append(q)
    path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    print('Saved threads',len(d['threads']),'quotes',len(d['quotes']))

if __name__=='__main__':
    if sys.argv[1]=='read':read_chunk(int(sys.argv[2]),int(sys.argv[3]) if len(sys.argv)>3 else 0,int(sys.argv[4]) if len(sys.argv)>4 else None)
    if sys.argv[1]=='save':save_update(json.load(sys.stdin))
