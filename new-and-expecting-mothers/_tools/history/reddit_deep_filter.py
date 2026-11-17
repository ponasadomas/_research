#!/usr/bin/env python3
"""Transparent artifact/buying and broader-friction tiers over the complete frozen window.

No relevance scores or top-N cap. Every tier-A card is emitted for human triage.
Filters select reading, never substitute for full original-post reads.
"""
from pathlib import Path
import collections,datetime,gzip,json,re
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'_raw/reddit-deep'
WINDOW=RAW/'windows/2025-h2-v1'
OUT=RAW/'filter-v1'

ASK=r'\b(?:need|want|looking|find|recommend|help|how|anyone|share|request|where|creat\w*|mak\w*|put together|follow\w*|suggest\w*)\b'
ARTIFACT=r'\b(?:plan(?:s|ner|ning)?|schedule(?:s)?|checklist(?:s)?|guide(?:s)?|routine(?:s)?|step.by.step|spreadsheet|template(?:s)?|personaliz\w*|personalis\w*|customiz\w*|customis\w*)\b'
TOOL=r'\b(?:app(?:s)?|course(?:s)?|book(?:s)?|program(?:me)?(?:s)?|planner(?:s)?|guide(?:s)?|consultant(?:s)?|coach(?:es|ing)?|subscription(?:s)?)\b'
DECISION=r'\b(?:paid|pay(?:ing)?|buy(?:ing)?|bought|purchas\w*|subscription|worth|price|free|refund|cost|cancel\w*|tried|use[ds]?|using|review\w*)\b'
A_PATTERNS={
 'artifact_request':re.compile(ASK+r'[\s\S]{0,110}'+ARTIFACT+'|'+ARTIFACT+r'[\s\S]{0,110}'+ASK,re.I),
 'tool_decision':re.compile(TOOL+r'[\s\S]{0,130}'+DECISION+'|'+DECISION+r'[\s\S]{0,130}'+TOOL,re.I),
}
B=re.compile(r'\b(?:overwhelm\w*|confus\w*|guilt\w*|fail(?:ing|ure)?|uncertain\w*|lost|struggl\w*|worried|worry\w*|concern\w*|exhaust\w*|logistic\w*|mental load|no idea|don.t know|not sure|how (?:do|can|should)|what (?:do|can|should)|when (?:do|can|should)|help|advice|time management|return(?:ing)? to work|back to work)\b',re.I)
TOPICS={
 'development_play':re.compile(r'\b(?:tummy time|milestone\w*|development\w*|activities|play mat|play gym|floor time|entertain\w*|play with|baby play|toys?)\b',re.I),
 'solids_food':re.compile(r'\b(?:solids?|wean\w*|pur[eé]e\w*|allergen\w*|blw|baby food|food|meals?|grocery|groceries|cooking)\b',re.I),
 'pumping_feeding':re.compile(r'\b(?:pump\w*|breastfeed\w*|breast.?milk|nurs(?:e|ing)|formula|bottles?|milk supply|latch\w*)\b',re.I),
 'sleep_routines':re.compile(r'\b(?:sleep\w*|naps?|napping|wake window\w*|bedtime|huckleberry|napper)\b',re.I),
 'household_support':re.compile(r'\b(?:post.?partum|household|partner|husband|chores?|village|support|night shifts?|division of labo[u]?r|maternity leave|paternity leave|daycare|childcare)\b',re.I),
 'pregnancy_birth':re.compile(r'\b(?:pregnan\w*|trimester|prenatal|antenatal|birth plan|birth|delivery|due date|exercise|workout\w*|pelvic|labou?r)\b',re.I),
 'registry_gear':re.compile(r'\b(?:registry|registries|baby gear|stroller\w*|pram\w*|car seat|baby carrier|babywear\w*|breast pump|travel system|checklist|hospital bag)\b',re.I),
 'work_return':re.compile(r'\b(?:return(?:ing)? to work|back to work|working|commut\w*|office|meetings?|shifts?|manager|boss|workday|teacher|work schedule)\b',re.I),
}
SAFETY=re.compile(r'kill myself|suicid|self.harm|hurt (?:myself|my baby)|abuse|hit me|shak(?:e|ing) (?:the|my) baby|miscarriage|stillbirth|infant death|\b(?:1[0-7])\s*(?:f|m)\b',re.I)

def main():
    if OUT.exists():raise SystemExit('Frozen filter output exists; bump version rather than overwrite.')
    OUT.mkdir();(OUT/'cards').mkdir()
    index=(OUT/'posts-index.jsonl').open('w');tierfiles={k:(OUT/(k+'-candidates.jsonl')).open('w') for k in ['A','B','C','unavailable']}
    totals=collections.Counter();by_sub=collections.defaultdict(collections.Counter);by_topic=collections.defaultdict(collections.Counter);a_cards=[]
    for p in sorted(WINDOW.glob('*_submissions.jsonl.gz')):
        with gzip.open(p,'rt') as f:
            for line in f:
                q=json.loads(line);body=q.get('selftext','');title=q.get('title','');text=title+'\n'+body
                unavailable=body in ['', '[removed]','[deleted]']
                am={k:m.group(0) for k,pat in A_PATTERNS.items() if (m:=pat.search(text))}
                bm=B.search(text);topics={k:len(pat.findall(text)) for k,pat in TOPICS.items() if pat.search(text)}
                tier='unavailable' if unavailable else 'A' if am else 'B' if bm else 'C'
                primary=max(topics,key=topics.get) if topics else 'other'
                rec={'id':q['id'],'subreddit':q['subreddit'],'created_utc':q['created_utc'],'date':datetime.datetime.fromtimestamp(int(q['created_utc']),datetime.timezone.utc).isoformat(),'title':title,'body_chars':len(body),'tier':tier,'primary_topic':primary,'topics':list(topics),'matches':am,'friction_match':bm.group(0) if bm else '', 'safety_flag':bool(SAFETY.search(text)),'source_file':str(p.relative_to(ROOT)),'url':'https://www.reddit.com'+q.get('permalink',f"/r/{q['subreddit']}/comments/{q['id']}/"),'author':q.get('author',''),'num_comments_reported':q.get('num_comments',None),'body_status':body if unavailable else 'present'}
                index.write(json.dumps(rec,ensure_ascii=False)+'\n');tierfiles[tier].write(json.dumps(rec,ensure_ascii=False)+'\n')
                totals[tier]+=1;by_sub[q['subreddit']][tier]+=1;by_topic[primary][tier]+=1
                if tier=='A':
                    card=f"ID {q['id']} | r/{q['subreddit']} | {rec['date']} | {primary} | safety_flag={rec['safety_flag']}\nTITLE: {title}\nOPENING: {body[:350]}\nMATCHES: "+json.dumps(am,ensure_ascii=False)+'\n'
                    a_cards.append((q['subreddit'],q['id'],card))
    index.close()
    for f in tierfiles.values():f.close()
    # Fixed chronological source order; every A card included, never ranked/capped.
    chunks=[]
    for sub in sorted(by_sub):
        batch=[x for x in a_cards if x[0]==sub];buf='';ids=[];i=1
        for _,id,card in batch:
            if buf and len((buf+card).encode())>40000:
                name=f'A-{sub}-{i:03d}.txt';(OUT/'cards'/name).write_text(buf);chunks.append({'file':str((OUT/'cards'/name).relative_to(ROOT)),'ids':ids,'cards':len(ids)});buf='';ids=[];i+=1
            buf+=card+'\n';ids.append(id)
        if buf:
            name=f'A-{sub}-{i:03d}.txt';(OUT/'cards'/name).write_text(buf);chunks.append({'file':str((OUT/'cards'/name).relative_to(ROOT)),'ids':ids,'cards':len(ids)})
    (OUT/'cards-index.jsonl').write_text(''.join(json.dumps(x)+'\n' for x in chunks))
    summary={'window':'2025-07-01 inclusive to2026-01-01 exclusive','total_posts':sum(totals.values()),'tiers':dict(totals),'by_subreddit':{k:dict(v) for k,v in by_sub.items()},'by_primary_topic':{k:dict(v) for k,v in by_topic.items()},'tier_A_card_chunks':len(chunks),'tier_A_cards':len(a_cards),'safety_flags_are_review_flags_not_automatic_drops':True,'relevance_ranking_or_topN_cap':False,'triaged':0,'kept_after_human_triage':0,'full_posts_read':0,'original_comments_read':0}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
