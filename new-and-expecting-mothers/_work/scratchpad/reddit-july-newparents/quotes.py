import json
from work import R,W,M
F=R/'voice/reddit-july-newparents.jsonl'
def q(pid,quote,stage,typ,themes,speaker='parent_unspecified',context=''):
    old=[json.loads(x) for x in F.read_text().splitlines()] if F.exists() else []
    assert quote in (R/M[pid]['raw_file']).read_text(),pid
    assert len(context.split())<=25
    d=dict(id=f'rjnp01-{len(old)+1:04}',source='r/NewParents',url=M[pid]['url'],date=M[pid]['post_date'],speaker=speaker,stage=stage,type=typ,themes=themes.split(','),quote=quote,context=context,raw_file=M[pid]['raw_file'],source_class='reddit_archive',evidence_kind='archived_original',archive_dataset='yikeee/reddit-subreddits25',archive_commit='ea497c510aa68765c07ed744ec9f84d68bbedf7f',post_id=pid,read_scope='full_post')
    with F.open('a') as out:out.write(json.dumps(d,ensure_ascii=False)+'\n')
