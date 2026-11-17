from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2]
units=json.loads((ROOT/'_raw/books/review-units.json').read_text())
choices={
 ('cribsheet-apple','we-customer-review-1589'):('Examples are often random and vague.','objection',['skepticism','information_overload'],'Reviewer wanted stronger decision support and disputed the mixture of evidence and personal opinion.'),
 ('expecting-better','we-customer-review-1251'):('Such useful information that have helped me navigate all the choices I am making in my first time pregnancy.','success_story',['birth_preparation','first_time_parent'],'Reviewer values decision support during a first pregnancy.'),
 ('expecting-better','we-customer-review-1252'):('clear and informative so you can take the best decision bad on your preferences','success_story',['personalization','conflicting_advice'],'Reviewer values clear data and decisions aligned with preferences.'),
 ('expecting-better','we-customer-review-1253'):('Data driven perspectives and personal anecdotes made this book insightful, interesting, and incredibly helpful.','success_story',['conflicting_advice'],'Reviewer praises the combination of data and personal narrative.'),
 ('montessori-baby','we-customer-review-1256'):('It truly shows you other ways to do things and gave me the confidence as a new mom','success_story',['floor_play','first_time_parent'],'New mother reports gaining alternative approaches and confidence; child outcomes are not established.'),
 ('precious-little-sleep','we-customer-review-1247'):('As far as naps go, she will only nap on someone.','pain',['contact_naps','sleep_routines'],'Parent reports choosing a method based on tolerance and current sleep, with an early positive impression.'),
 ('precious-little-sleep','we-customer-review-1248'):('definitely and must read for any tired parent!','success_story',['sleep_routines'],'Reviewer reports satisfaction after changing sleep associations; causation and method suitability are not established.'),
 ('precious-little-sleep','we-customer-review-1249'):('Good information surrounded by filler.','objection',['information_overload','not_enough_time'],'Reviewer finds useful advice too slow to access with a crying, sleepless infant.'),
 ('wonder-weeks','we-customer-review-2901'):('my download was only the cover art.','objection',['price_value'],'Reviewer reports a failed digital delivery, not dissatisfaction with the unread book content.'),
}
rows=[]
for q in units:
 if (q['book'],q['review_id']) not in choices: continue
 text,typ,themes,context=choices[q['book'],q['review_id']]
 source=(ROOT/q['raw_file']).read_text().splitlines()[0].split(': ',1)[1]
 assert len(text.split())<=25
 rows.append(dict(id=f'revb01-{len(rows)+1:04}',source='applebooks-'+q['book'],url=source,date=q['date'],speaker='new_mother' if q['book']=='montessori-baby' else 'reviewer',stage='unknown',type=typ,themes=themes,quote=text,context=context,raw_file=q['raw_file'],source_class='book_review',evidence_kind='original_review',review_id=q['review_id'],rating=q['rating']))
(ROOT/'voice/reviews-books-01.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in rows))
print(len(rows),'book review quotes')
