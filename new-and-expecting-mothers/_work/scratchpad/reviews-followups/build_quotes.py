from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[2]
raw=ROOT/'_raw/reviews-followups'
units=json.loads((raw/'googleplay-review-units.json').read_text())
selections=[
('a7c50452-6a1e-4bc3-b8bf-9f3bee441fd7',"I am always trying to figure out what me and my child can do together that doesn't include toys, TV or tablet.",'desire',['floor_play','free_alternatives'],'Parent values ordinary activity ideas, used free access and later paid for more.'),
('b4872611-6080-42b3-8450-f4f5075d24cf','They emailed me right away and fixed the problems!','success_story',['price_value'],'Updated caregiver review praises resolution of lost milestone progress after an initial complaint.'),
('2159065e-df98-4235-a498-9bfc795b2a3d',"I chose not to buy the app since it didn't respond to baby's growth",'objection',['personalization','price_value'],'Parent says completed milestone inputs did not advance activity recommendations.'),
('388b454f-34d1-43fb-8cad-67a160d405c1','it seems to not use accounts, period.','objection',['privacy','personalization'],'Reviewer lost records after changing phones; developer explains local storage is intentional for privacy.'),
('23a7169f-9343-46fd-add0-0a4343fe0871',"I definitely can't recommend it to the families I work with since it's unusable for me.",'objection',['free_alternatives'],'Reviewer testing the free CDC app for client families reports repeated crashes; role is self-described.'),
('7e692358-c80f-4072-8094-8b13b00592d8','the day my baby turned two months, it started crashing.','objection',['free_alternatives'],'Historical reviewer reports crashes; developer reply says a corrective update was subsequently released.'),
('9ceae0a9-fb8b-4b73-9081-2884b3489ffa','the constant, annoying pop ups and notifications to upgrade to premium are obnoxious.','objection',['subscription_fatigue','not_enough_time'],'Reviewer values overnight memory support but wants control of promotional prompts.'),
('fb1eb9a4-b20a-408a-8d35-fbfe48de507e','Love the ability to track feeds and whatnot free of charge.','success_story',['free_alternatives','price_value'],'Reviewer also alleges an accidental attempted charge from a popup and plans to uninstall; allegation unverified.'),
('640035f5-2326-4989-a81b-acdfc9cfcc57',"it doesn't really present data any better than a spreadsheet would.",'objection',['price_value','daycare_handoff'],'Reviewer wants better daycare-log integration and finds current summaries insufficiently useful.'),
('8f2d4398-d4d7-4049-bd17-5f7aca999a12','Too expensive for me... Deleting now.','objection',['subscription_fatigue','price_value'],'Historical Kinedu reviewer says an update restricted access to accumulated milestones.'),
('2413929e-c033-4253-8be8-accd788cf0d1','Even clicking on a milestone to see more detail on what is considered "met" is for subscription only!','objection',['milestone_comparison','price_value'],'Historical reviewer objects to subscription gating and repeated trial prompts.'),
('8f9ccb09-c20f-41ae-92c2-83b180925612',"having to subscribe for it just isnt what I'm looking for",'objection',['free_alternatives','price_value'],'Reviewer wants ad-supported free resources instead of paid access; this is preference, not universal price sensitivity.'),
('1bb7217d-e4ae-4b0a-b0a1-61c9bb3a7937','It was great during the free trial, so I bought it.','trigger_moment',['price_value','personalization'],'Reviewer reports later predictions lost accuracy while appreciating limited promotional notifications.'),
('bdf453bb-b3e2-4aad-b1cb-057ef33c9654',"If it had all the features of my current free baby tracker app I use, I'd potentially think about moving over to the premium.",'objection',['free_alternatives','price_value'],'Reviewer wants broad tracking features before replacing an existing free app.'),
('c0d59aef-6e52-40e5-9b5a-fcbdce62d3ad',"You also can't differentiate between bottle feeding formula and pumped milk.",'objection',['personalization','pumping_schedule'],'Historical reviewer wants more precise feeding categories and entry controls.'),
('13c682e9-3265-4ff6-8680-f902a41ba7ac','I\'ve tried out a few other apps, some slicker and "prettier," but none have the functionally of this one','success_story',['free_alternatives','floor_play'],'Parent values Pathways videos and explanations over paid alternatives; perceived research quality is not independently validated.'),
('59090bfc-8119-4ed6-bcf1-cb6034707ef7','You can also look ahead and see what milestones and abilities will come up next for your little one','success_story',['milestone_comparison','free_alternatives'],'Reviewer values free activity ideas, explanatory videos and visibility ahead.'),
('3ff3f9fa-9f74-463b-9f3d-fe5e0d778b57',"you can't track other games that aren't in the suggested four.",'objection',['personalization','floor_play'],'Reviewer likes free Pathways suggestions but wants credit for additional activities; claimed massage effects not endorsed.'),
('481a4064-6c6f-4784-b6ab-118ba74f5ed6','It should just list your recent foods instead of random things we will never eat.','desire',['personalization','meal_planning'],'Paying reviewer values content but wants food tracking organized around actual household choices.'),
('eaabf004-9227-4b03-966d-8ed9e964b218','I am not able to spend that much on an app subscription.','objection',['price_value','free_alternatives'],'Historical paywall complaint has a developer reply announcing the database would become free again.'),
('21f7c862-ea60-49e9-815d-b6a92a16d699',"Otherwise, don't require an account to access what little content is free.",'objection',['privacy','free_alternatives'],'Reviewer objects to account gating; developer replies the food database is free and explains dismissing the paywall.'),
]

byid={q['review_id']:q for q in units}
rows=[]
for rid,excerpt,typ,themes,context in selections:
 q=byid[rid]
 rows.append(dict(id=f'revf01-{len(rows)+1:04}',source=q['source'],url=q['url'],date=q['date'],speaker='reviewer',stage='unknown',type=typ,themes=themes,quote=excerpt,context=context,raw_file=q['raw_file'],source_class='app_review',evidence_kind='original_review',review_id=rid,rating=q['rating'],storefront='US English'))

bookselections={
 850986867:('Really well done!','success_story','Unverified-purchase reviewer offers brief praise for The First Forty Days.'),
 904367339:('Very useful for moms-to-be and others to understand women.','success_story','Unverified-purchase reviewer values The First Forty Days as an explanation for others as well as expecting mothers.'),
 902923880:('I especially appreciated when the data was unclear or there was no settled guidance.','success_story','Unverified-purchase Cribsheet reviewer values acknowledgement of uncertainty and choice.'),
 904270202:('clearly written for the lay person.','success_story','Unverified-purchase Cribsheet reviewer praises accessibility and works with new families; professional credentials not established.'),
 902883672:('It is fully illustrated, straight to the point and a pleasure to read.','success_story','Unverified-purchase Simplest Baby Book reviewer values illustrations and direct explanations.'),
}
for p in sorted(raw.glob('barnes-*-yotpo-reviews.json')):
 j=json.loads(p.read_text())
 for q in j.get('reviews',[]):
  excerpt,typ,context=bookselections[q['id']]
  product=next(iter(j.get('products',[])),{})
  slug=p.stem.removesuffix('-yotpo-reviews')
  if slug=='barnes-first40':url='https://www.barnesandnoble.com/w/?ean=9781617691836'
  else:url=(raw/(slug+'.txt')).read_text().splitlines()[0].split(': ',1)[1]
  rows.append(dict(id=f'revf01-{len(rows)+1:04}',source=slug,url=url,date=q['createdAt'][:10],speaker='reviewer',stage='unknown',type=typ,themes=['information_overload','price_value'],quote=excerpt,context=context,raw_file=str(p.relative_to(ROOT)),source_class='book_review',evidence_kind='original_review',review_id=str(q['id']),rating=q['score'],verified_purchase=q['verifiedBuyer'],syndication=q['syndicationData']))
assert len({q['id'] for q in rows})==len(rows)
assert max(len(q['quote'].split()) for q in rows)<=25
assert max(len(q['context'].split()) for q in rows)<=25
(ROOT/'voice/reviews-followup-01.jsonl').write_text(''.join(json.dumps(q,ensure_ascii=False)+'\n' for q in rows))
print(len(rows),'follow-up quotes')
