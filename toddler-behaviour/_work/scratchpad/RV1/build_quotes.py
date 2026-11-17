#!/usr/bin/env python3
"""RV1: build voice/reviews-rv1.jsonl from hand-selected quotes. Run once."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'voice/reviews-rv1.jsonl'
if OUT.exists(): sys.exit('refusing to overwrite')
AS = {'goodinside':('Good Inside','good-inside-parenting/id6463803046'),'pottywhiz':('Potty Whiz','-/id1493987452'),
      'pottr':('POTTR','potty-training-pottr/id6757593828'),'pottytrainingapp':('Potty Training App','potty-training-app/id6760347375'),
      'littlepath':('LittlePath','-/id6761305309'),'aiparentingcoach':('AI Parenting Coach','-/id6451044904'),'granny':('Granny: AI Parenting Coach','-/id6466166824')}
GP = {'goodinside':('Good Inside','com.goodinside.gimobile'),'pottywhiz':('Potty Whiz','app.kidplay.pottywhiz')}
BN = {'good-inside':('Good Inside','https://www.barnesandnoble.com/w/good-inside-becky-kennedy/1140501121?ean=9780063159488'),
      'oh-crap':('Oh Crap! Potty Training','https://www.barnesandnoble.com/w/oh-crap-potty-training-jamie-glowacki/1121494738?ean=9781501122989'),
      'happiest-toddler':('The Happiest Toddler on the Block','https://www.barnesandnoble.com/w/the-happiest-toddler-on-the-block-harvey-karp/1100277257?ean=9780553384420'),
      'hunt-gather-parent':('Hunt, Gather, Parent','https://www.barnesandnoble.com/w/hunt-gather-parent-michaeleen-doucleff/1138418941?ean=9781982149680'),
      'whole-brain-child':('The Whole-Brain Child','https://www.barnesandnoble.com/w/the-whole-brain-child-daniel-j-siegel-md/1114977784?ean=9780553386691'),
      'hands-not-for-hitting':('Hands Are Not for Hitting','https://www.barnesandnoble.com/w/hands-are-not-for-hitting-board-book-martine-agassi/1144436442?ean=9781575422008')}
AB = {'oh-crap':'Oh Crap! Potty Training','good-inside-2':'Good Inside','how-to-talk-little-kids':'How to Talk So Little Kids Will Listen',
      'whole-brain-child':'The Whole-Brain Child','happiest-toddler':'The Happiest Toddler on the Block','hunt-gather-parent':'Hunt, Gather, Parent'}
def unit(key):
    """key forms: as:<app>-<cc>-<id> | gp:<app>-<n> | bn:<book>:<id> | ab:<book>:<cc>-<we id>"""
    kind, rest = key.split(':',1)
    if kind=='as':
        app, cc, rid = rest.split('-'); name, path = AS[app]
        raw=f'_raw/reviews/{app}-{cc}-corpus.txt'; txt=(ROOT/raw).read_text()
        m=re.search(rf'REVIEW {app}-{cc}-{rid} \| (\d) stars \| (\S{{10}})',txt)
        return dict(source=f'App Store {cc} {name}',url=f'https://apps.apple.com/{cc}/app/{path}?see-all=reviews',date=m.group(2),raw_file=raw,source_class='app_review',review_id=f'{app}-{cc}-{rid}',engagement=f'{m.group(1)} stars')
    if kind=='gp':
        app, n = rest.split('-'); name, pkg = GP[app]; raw=f'_raw/reviews/googleplay-{app}.txt'; txt=(ROOT/raw).read_text()
        m=re.search(rf'REVIEW googleplay-{app}-{n} \| (\d) stars \| ([^|]+) \| ([^\n]*)',txt)
        from datetime import datetime
        d=datetime.strptime(m.group(2).strip(),'%B %d, %Y').strftime('%Y-%m-%d')
        return dict(source=f'Google Play {name}',url=f'https://play.google.com/store/apps/details?id={pkg}&hl=en_US&gl=US',date=d,raw_file=raw,source_class='app_review',review_id=f'googleplay-{app}-{n}',engagement=f'{m.group(1)} stars; {m.group(3).strip()}')
    if kind=='bn':
        book, rid = rest.split(':'); name, url = BN[book]; raw=f'_raw/books/barnes-{book}-corpus.txt'; txt=(ROOT/raw).read_text()
        m=re.search(rf'REVIEW barnes-{rid} \| (\d) stars \| (\S+)',txt)
        return dict(source=f'Barnes & Noble {name}',url=url,date=m.group(2),raw_file=raw,source_class='book_review',review_id=f'barnes-{rid}',engagement=f'{m.group(1)} stars')
    if kind=='ab':
        book, rid = rest.split(':'); raw=f'_raw/books/apple-{book}-corpus.txt'; txt=(ROOT/raw).read_text()
        m=re.search(rf'REVIEW apple-{rid} \| (\d) stars \| (\S+) \| (\S+)',txt)
        d=m.group(2)
        if '/' in d:
            a,b,c=d.split('/'); cc=rid.split('-')[0]
            d=f'{c}-{b}-{a}' if cc=='au' else f'{c}-{a}-{b}'
        return dict(source=f'Apple Books {rid.split("-")[0]} {AB[book]}',url=m.group(3),date=d,raw_file=raw,source_class='book_review',review_id=f'apple-{rid}',engagement=f'{m.group(1)} stars')
Q = []
def q(key, stage, typ, themes, quote, context, restricted=None):
    Q.append((key, stage, typ, themes, quote, context, restricted))
exec(open(Path(__file__).with_name('quotes.py')).read())
n=0; restricted=[]
with OUT.open('w') as f:
    for key, stage, typ, themes, quote, context, r in Q:
        n+=1; rec={'id':f'tbr1-{n:04d}'}; u=unit(key)
        rec.update(source=u['source'],url=u['url'],date=u['date'],speaker='reviewer',stage=stage,type=typ,themes=themes,quote=quote,context=context,raw_file=u['raw_file'],source_class=u['source_class'],engagement=u['engagement'],review_id=u['review_id'])
        assert len(context.split())<=25, context
        if r: restricted.append((rec['id'], r))
        f.write(json.dumps(rec,ensure_ascii=False)+'\n')
(Path(__file__).with_name('restricted.tsv')).write_text(''.join(f'{i}\t{r}\n' for i,r in restricted))
print(n,'quotes;',len(restricted),'restricted')
