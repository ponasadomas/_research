from pathlib import Path
import json,sys
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'_tools'))
from fetch_page import extract
D=R/'_raw/audit/deep-wave'
qs={q['id']:q for f in (R/'voice').glob('*.jsonl') for q in map(json.loads,f.read_text().splitlines())}
sample=[json.loads(l) for l in (D/'spot-check-later-originals.jsonl').read_text().splitlines()]
outs=[]
for frozen in sample+[qs['qdeep01-0025'],qs['qdeep01-0087']]:
    q=qs[frozen['id']]
    txt='AUDIT '+json.dumps({k:q.get(k) for k in ['id','speaker','stage','type','context','quote','url']},ensure_ascii=False)+'\n'
    if q['source_class']=='reddit_archive':
        src=(R/q['raw_file']).read_text();txt+=src.split('=== COMPLETE ORIGINAL POST BODY ===',1)[-1]
    elif q['source_class']=='forum_oblique':
        pref='geo' if 'geoclicks' in q['url'] else 'mse'
        n=json.loads((R/'_raw/oblique-deep/threads'/f"{pref}-{q['thread_id']}.json").read_text())
        p=next(p for p in n['posts'] if p['post_id']==q['post_id'])
        txt+='FULL QUOTED AUTHOR POST\n'+p['body_with_quotes']+'\nSOURCE_META '+json.dumps({k:p[k] for k in ['date','is_op','url']})
        if p!=n['posts'][0]:txt+='\nFIRST VISIBLE POST (provenance may be uncertain, as source note records)\n'+n['posts'][0]['body_with_quotes']
    elif q['source_class']=='qa_community':
        n=json.loads((R/'_raw/qa-deep/threads'/f"{q['question_id']}.json").read_text())
        p=next(p for p in n['comments'] if p['comment_id']==q['comment_id']) if q.get('comment_id') is not None else (n['question'] if q['post_id']==q['question_id'] else next(p for p in n['answers'] if p['answer_id']==q['post_id']))
        txt+='FULL QUOTED AUTHOR POST\n'+extract(p['body'])[2]+'\nSOURCE_META '+json.dumps({'date':p['creation_date'],'is_op':q['is_op'],'native_author_id':p.get('owner',{}).get('user_id')})
        if p!=n['question']:txt+='\nORIGINAL QUESTION\n'+extract(n['question']['body'])[2]
    outs.append(txt)
for batch in range(3):
    chunk=outs[batch*10:(batch+1)*10]
    if chunk:(D/f'spot-check-later-view-{batch+1:02}.txt').write_text('\n\n==========\n\n'.join(chunk))
print('Prepared',len(outs),'source-context checks')
