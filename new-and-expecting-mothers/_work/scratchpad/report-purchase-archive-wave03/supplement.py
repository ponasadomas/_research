"""Additive recall scan; never rewrites initial 72 candidates or frozen units."""
import collections,gzip,json,re
from pathlib import Path
from capture import ART,PAY,R,S,W,sha,dump
PAY2=re.compile(PAY.pattern+r'|\b(?:spent|spend(?:ing)?|charg(?:e|ed|es|ing)|order(?:ed|ing)?|invest(?:ed|ing)?|subscrib(?:ed|e)|subscription)\b|[$£€]\s*\d[\d,.]*|\b(?:USD|GBP|CAD|AUD|NZD|EUR)\s*\d|\b\d[\d,.]*\s*(?:USD|GBP|CAD|AUD|NZD|EUR|dollars?|pounds?|euros?)\b',re.I)
ART2=re.compile(ART.pattern+r'|\b(?:baby\W*sleep\W*made\W*simple|happy\W*hive|blissful\W*baby\W*expert|pampers\W*sleep\W*coach|gerber\W*sleep\W*coach|napper|cara(?:\W*s)?\W*(?:course|program|guide)|full\W*feedings?|little\W*[zw]\W*sleep|sleep\W*training\W*(?:course|program))\b',re.I)
def main():
 target=W/'supplement-v1';assert not target.exists();target.mkdir();(target/'cards').mkdir();ix={x['post_id']:x for x in map(json.loads,(W/'native-index.jsonl').read_text().splitlines())};old={x['post_id'] for x in map(json.loads,(W/'commercial-candidates.jsonl').read_text().splitlines())};found=[];scanned=0
 for p in sorted((W/'window').glob('*.gz')):
  with gzip.open(p,'rt') as f:
   for line in f:
    n=json.loads(line);scanned+=1;u=ix[n['id']]
    if n['id'] in old or u['body_status']!='present':continue
    combined=n['title']+'\n'+n['selftext'];pm=list(PAY2.finditer(combined));am=list(ART2.finditer(combined))
    if not pm or not am:continue
    snippets=[]
    for m in pm+am:
     s=combined[max(0,m.start()-85):min(len(combined),m.end()+100)].replace('\n',' ')
     if s not in snippets:snippets.append(s)
    text='ID '+n['id']+' | '+n['subreddit']+' | '+u['date']+'\nTITLE '+n['title']+'\nOPENING '+n['selftext'][:500].replace('\n',' ')+'\nPAYMENT_MATCHES '+json.dumps(sorted({m.group(0) for m in pm}),ensure_ascii=False)+'\nARTIFACT_MATCHES '+json.dumps(sorted({m.group(0) for m in am}),ensure_ascii=False)+'\nMATCH_CONTEXTS\n'+'\n'.join(snippets)+'\n';cp=target/'cards'/f'{n["id"]}.txt';cp.write_text(text);found.append({**u,'card_file':str(cp.relative_to(R)),'card_sha256':sha(cp)})
 (target/'commercial-candidates.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in found));dump(target/'summary.json',{'window_records_rescanned':scanned,'initial_frozen_candidates':len(old),'additional_disjoint_candidates':len(found),'community_counts':dict(collections.Counter(u['subreddit'] for u in found)),'payment_regex':PAY2.pattern,'artifact_regex':ART2.pattern,'no_initial_file_or_unit_rewritten':True});print(json.dumps({'initial':len(old),'supplement':len(found),'communities':dict(collections.Counter(u['subreddit'] for u in found))}))
 base=(S/'reader.py').read_text();base=base.replace("S=Path(__file__).parent;W=", "S=Path(__file__).parent/'supplement-v1';S.mkdir(exist_ok=True);W=")
 base=base.replace("jl(W/'commercial-candidates.jsonl')","jl(W/'supplement-v1/commercial-candidates.jsonl')")
 (S/'reader_supplement.py').write_text(base)
if __name__=='__main__':main()
