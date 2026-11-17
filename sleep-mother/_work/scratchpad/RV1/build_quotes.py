#!/usr/bin/env python3
"""RV1: write voice/reviews-rv1.jsonl from hand-selected quotes (verbatim, trims with ' […] ')."""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
R = ROOT / '_raw/reviews'; B = ROOT / '_raw/books'
APPURL = {}
for m in R.glob('appstore-collection-manifest*.json'):
    for r in json.loads(m.read_text()):
        APPURL[(r['app'], r['country'])] = r['url']
NAMES = {'sleepio3':'Sleepio 3.0','sleepiouk':'Sleepio (UK)','stellarsleep':'Stellar Sleep','bettersleep':'BetterSleep','calm':'Calm','headspace':'Headspace','slumber':'Slumber','rise':'Rise'}
def dates(path):
    d = {}
    for line in path.read_text().splitlines():
        m = re.match(r'REVIEW (\S+) \| .*? \| (\S+)', line)
        if m: d[m.group(1)] = m.group(2)[:10]
    return d
Q = []  # (unit, type, themes, quote, context, stage, restricted_reason)
def a(unit, typ, themes, quote, context, stage='unknown', restricted=None):
    Q.append((unit, typ, themes, quote, context, stage, restricted))

a('stellarsleep-ca-13882718619','success_story',['partner_sleeps_through','cbti'],"Going to bed has become a joy, and my husband now joins me on the couch every morning to share quiet coffee time.","5-star review after 70 days of the CBT-I program; ten years of about 5.5 hours a night; husband now shares mornings.")
a('stellarsleep-ca-13882718619','pain',['cumulative_deprivation','early_waking_mum'],"Prior to this I was averaging about 5.5 hours a night. This had been the case for more than 10 years. A combination of being unable to get to sleep to mid-sleep wakings sometimes left me with less than 5 hours - usually at least once a week.","Same reviewer describing a decade of short sleep before the program.")
a('stellarsleep-us-11316861661','trigger_moment',['partner_sleeps_through','anxiety_at_night','sleep_aids_question'],"the new dr diagnosed me with anxiety due to being a caregiver for my husband fighting stage 4 cancer and was prescribed medication for anxiety and Temazepam for sleep, which usually worked, but I didn’t want to get addicted.","Caregiver for a husband with cancer; medication history before using the app.",restricted='diagnosis, anxiety and sleep medication')
a('bettersleep-au-10165987256','price_signal',['white_noise_for_mum','price_value'],"Even my kids can find combinations they don’t mind to help get them to sleep (and that’s saying a lot!).","Parent using the sound mixer for herself and her children; 4 stars.")
a('bettersleep-au-10165987256','objection',['price_value'],"And no - I’m not a fan of “free 7-day trials” - as I inevitably forget to unsubscribe and feel duped. Would be better if there was a very cheap level of subscription to unlock a few more noises or noise sets","Same parent on the trial model and wanting a cheap tier.")
a('bettersleep-au-13638041546','pain',['white_noise_for_mum','price_value'],"I’m trying to put toddler down and it suddenly stops and the takes minutes to get back working if at all","Paying subscriber whose sounds keep cutting out at the toddler's bedtime.", stage='toddler')
a('bettersleep-ca-5934431361','success_story',['white_noise_for_mum'],"the baby shusher literally cut my time in half putting my son to sleep, before the I rocked, I let him cry it out, I sang and nothing worked or if any of them worked it would take an hour for him to settle it was a fight maybe 90 percent of the time.","Mother on using the app's shush sound for her son; the hour of rocking before it.")
a('bettersleep-ca-5934431361','belief',['maternal_guilt'],"You are that child’s mother nobody knows better then you","Same mother, in a long aside telling other mothers to trust themselves over the doctor.")
a('bettersleep-gb-3229433593','pain',['partner_sleeps_through','white_noise_for_mum'],"My husband has a snoring issue, which we’ve done everything we can to solve, including surgery.","1-star review: lifelong poor sleeper; the app's looping sounds did not mask the husband's snoring.")
a('bettersleep-gb-3229433593','price_signal',['price_value'],"Plus a monthly Audible subscription or a 30 hour long book on CD is so much cheaper than the subscriptions offered in this app.","Same reviewer: only audiobooks put her to sleep, and they cost less.")
a('calm-au-1752389939','trigger_moment',['cumulative_deprivation','return_to_work_exhausted'],"I'm also a parent of a child with special needs so life is very busy. In 2014, when work and family life did not shape up the way I had planned, I reached the lowest point of my life. I wasn't able to sleep and couldn't function normally.","Executive parent describing the point sleep collapsed; the rest of the review is a diagnosis and supplements story.",restricted='same review names an anxiety diagnosis, anti-anxiety supplements and a recovery outcome')
a('calm-au-10527608469','pain',['cant_sleep_when_baby_sleeps','no_village'],"I’m a single mother and my kids have a terrible case of insomnia.","Single mother complaining the kids' sleep stories are rarely updated.")
a('calm-au-10527608469','pain',['cant_sleep_when_baby_sleeps'],"this makes bedtime a struggle to the point where I can’t sleep until they sleep","Same mother: her own sleep waits on the children's.")
a('calm-au-10527608469','desire',['no_village'],"Please make my life easier.","Same mother, asking the app for more children's content.")
a('calm-gb-5122654239','trigger_moment',['racing_mind'],"Lying awake that night,  I found myself searching for a tool to help me sleep. Thoughts bouncing and body restless. I replayed and relived the events if the day that troubled me.","Reviewer (later mentions her husband) on the night she first downloaded Calm during wedding stress.")
a('calm-gb-9642009284','desire',['night_feeds_split','personalization'],"i am using it mostly for sleep, and going back to sleep after my baby has woken me up.","Parent asking for a separate narrator volume slider; the narrator's voice wakes her.")
a('calm-gb-9642009284','pain',['night_feeds_split','white_noise_for_mum'],"when I have insomnia and use those long sessions to go back to sleep, it does allow me to sleep but I’d like the contrast between the scene and narrator to be not that distant, so when the narrator comes after a pause it doesn’t wake me up.","Same parent explaining how the volume mix breaks her return to sleep after the baby wakes her.")
a('calm-gb-9642009284','objection',['personalization'],"It’s a very low hanging fruit for a feature improvement and would have such a profound impact on those of us using to go back to sleep.","Same parent; says she has asked for years.")
a('headspace-gb-8810328384','trigger_moment',['return_to_work_exhausted','cumulative_deprivation'],"Working long hours, stress at work, family life with kids, both working parents…. It all became to much and I reached burnout.","5-star review from a parent in a two-working-parent household; the rest describes therapy.",restricted='same paragraph continues into CBT and burnout treatment')
a('headspace-us-6968402734','success_story',['partner_sleeps_through'],"My partner and I enjoy doing meditations and Move exercises together.","Reviewer using Headspace with a partner; also asks to rewind sleepcasts.")
a('headspace-us-6968402734','desire',['racing_mind','personalization'],"it would be nice if I could rewind the sleepcast, as sometimes I miss the beginning or certain parts while I’m settling in, or still have stuff on my mind from the day","Same reviewer on missing the start of sleep audio while settling.")
a('headspace-us-6953395230','purchase',['family_help'],"My son bought me Headspace for my birthday 🥳 last year after I had talked with him about a perceived crisis I was having.","68-year-old mother whose adult son gifted a year's subscription; she now sleeps to a sleepcast.")
a('headspace-us-6953395230','success_story',['white_noise_for_mum'],"I use to have a difficult time getting to sleep and now I put on Rainday Antiques to help me sleep and I have yet to hear it to the end... I am sleeping very well.","Same mother on the sleepcast she falls asleep to.")
a('headspace-gb-3705554438','others_said',['apps_meditation'],"There are mediations that cover topics that range from pregnancy to coping with cravings, sleeping better to waking up early.","Reviewer listing Headspace topics; pregnancy appears as a general category.")
a('slumber-au-3813306332','success_story',['partner_sleeps_through','white_noise_for_mum'],"I have found the right mix to drown hubby snoring.","Subscriber using the background mixer to mask her husband's snoring.")
a('slumber-ca-14412446378','success_story',['white_noise_for_mum'],"This helps me and my child so much.","Short 4-star review: parent and child both use it.")
a('slumber-us-12756272139','trigger_moment',['baby_in_room','white_noise_for_mum'],"After my son was born and he was in our room in a bassinet, I realized very quickly I needed to make a change as I didn’t want him exposed to the tv’s blue light all night.","Lifelong poor sleeper who needed the TV on; the baby in the room made her change.", stage='looking_back')
a('slumber-us-12756272139','success_story',['baby_in_room'],"Sure, I was exhausted from having a newborn, but it was so much more than that! This app truly calmed me enough to fall asleep and stay asleep.","Same mother on her first night with the app.", stage='looking_back')
a('slumber-us-12756272139','success_story',[],"My son is now almost 3 years old and I still use the app every single night.","Same mother three years later.", stage='toddler')
a('slumber-us-2247469098','success_story',['partner_sleeps_through'],"My spouse listens with me and has also gotten used to it in a good way and finds it soothing and comforting.","Former Calm subscriber who switched to Slumber; spouse shares the stories.")
a('slumber-us-2247469098','price_signal',['price_value'],"I got used to going to sleep to stories with that other app and tried this just before that renewed, which is more expensive than this app.","Same reviewer switching from Calm before renewal.")
a('rise-au-9805555871','objection',['personalization','cumulative_deprivation'],"It told me i need to sleep 9 hours which is true, but the sleep window ideal for me it gave me is just not viable with small children.","3-star review: parent of small children finds the app's sleep window impossible.")
a('rise-au-9805555871','objection',['personalization'],"The quiz is not overly comprehensive and didn’t give the option to include some of the critical factors affecting your sleep, like sleep apnea and children","Same parent: the onboarding quiz has no option for children.")
a('rise-au-9805555871','tried_failed',['price_value'],"The app told me that I have a sleep debt but no solution for fixing it other than sleeping 9 hours + per day between certain hours.","Same parent; decided not to subscribe.")
a('rise-us-7219610139','purchase',['family_help'],"I realized that my teenage daughter needs this more than I do.","Parent who started Rise and then put her teenage daughter on the trial.")
a('rise-us-7219610139','price_signal',['price_value'],"If this app helps my teenager feel rested and more motivated to get to bed at a decent hour than shut up and take my money!","Same parent on what she would pay for.")

BOOKQ = [
 ('apple-first-forty-days','apple-us-we-customer-review-6520','Apple Books The First Forty Days','objection',['information_overload'],"The book has good bits of information. However, the same bits of information are repeated throughout the entire book.","2-star Apple Books review of the postpartum book; says it is repetitive.",None),
 ('apple-first-forty-days','apple-us-we-customer-review-6520','Apple Books The First Forty Days','objection',['information_overload'],"The tone and language are also very juvenile and the advice: common sense.","Same reviewer.",None),
 ('apple-say-good-night-insomnia','apple-ca-we-customer-review-5615','Apple Books Say Good Night to Insomnia','tried_failed',['cbti','racing_mind'],"I did find though the amount of information required to complete in the sleep diary only added to my stress.","4-star review: the sleep diary added stress; the reviewer was recovering from medical procedures.",'same review describes recovery from medical procedures and a treatment outcome'),
 ('apple-say-good-night-insomnia','apple-ca-we-customer-review-5615','Apple Books Say Good Night to Insomnia','belief',['cbti'],"I found this book helped me to understand that if I was not getting 6 or 7 hours sleep it was not critical to my health.","Same reviewer on the reassurance she took from the book.",'reassurance framed as a health claim; the review describes recovery from medical procedures'),
 ('apple-sleep-solution','apple-us-we-customer-review-6072','Apple Books The Sleep Solution','belief',['personalization'],"There were times I thought he was discussing my sleep problems/patterns and answering my sleep questions.","Short 5-star Apple Books review.",None),
 ('barnes-say-good-night-insomnia','barnes-842730104','Barnes & Noble Say Good Night to Insomnia','purchase',['sleep_aids_question','cbti'],"I wanted to get off sleeping pills and this helped me.","Reader sent by a sleep clinic nurse.",'medication outcome'),
 ('barnes-say-good-night-insomnia','barnes-902926800','Barnes & Noble Say Good Night to Insomnia','objection',['cbti'],"This book likely won't work if you have complex mental health or physical health issues that could contribute to your inability to sleep.","1-star review from a reader whose doctor recommended the book.",'mental-health and medication frame'),
 ('barnes-say-good-night-insomnia','barnes-837075252','Barnes & Noble Say Good Night to Insomnia','belief',['cbti'],"Tools for application are easy to use, with step-by-step instruction in how to apply concepts and use the recommended journaling for tracking of progress.","5-star verified-buyer review praising the structure.",None),
]

def main():
    out = []; restricted = []; n = 0
    cache = {}
    for unit, typ, themes, quote, ctx, stage, rr in Q:
        app, cc = unit.split('-')[0], unit.split('-')[1]
        corpus = R / f'{app}-{cc}-corpus.txt'
        cache.setdefault(corpus, dates(corpus))
        n += 1; qid = f'smr1-{n:04d}'
        out.append({'id': qid, 'source': f'App Store {cc} {NAMES[app]}', 'url': APPURL[(app, cc)], 'date': cache[corpus][unit], 'speaker': 'reviewer', 'stage': stage, 'type': typ, 'themes': themes, 'quote': quote, 'context': ctx, 'raw_file': str(corpus.relative_to(ROOT)), 'source_class': 'app_review', 'review_unit': unit})
        if rr: restricted.append((qid, rr))
    for slug, unit, src, typ, themes, quote, ctx, rr in BOOKQ:
        corpus = B / f'{slug}-corpus.txt'
        txt = corpus.read_text()
        m = re.search(r'REVIEW ' + re.escape(unit) + r' \| [^|]*\| (\S+)(?: \| (\S+))?', txt)
        date = m.group(1)
        url = m.group(2) if slug.startswith('apple') else None
        if slug.startswith('barnes'):
            man = json.loads((B / 'barnes-collection-manifest.json').read_text())
            url = next(x['url'] for x in man if x.get('title_slug') == slug[7:] and 'url' in x)
        if '/' in date:
            mm, dd, yy = date.split('/'); date = f'{yy}-{mm}-{dd}'
        n += 1; qid = f'smr1-{n:04d}'
        out.append({'id': qid, 'source': src, 'url': url, 'date': date, 'speaker': 'reviewer', 'stage': 'unknown', 'type': typ, 'themes': themes, 'quote': quote, 'context': ctx, 'raw_file': str(corpus.relative_to(ROOT)), 'source_class': 'book_review', 'review_unit': unit})
        if rr: restricted.append((qid, rr))
    vf = ROOT / 'voice/reviews-rv1.jsonl'
    if vf.exists(): raise SystemExit('refusing to overwrite ' + str(vf))
    vf.write_text(''.join(json.dumps(o, ensure_ascii=False) + '\n' for o in out))
    (Path(__file__).parent / 'restricted.tsv').write_text(''.join(f'{i}\t{r}\n' for i, r in restricted))
    print(len(out), 'quotes', len(restricted), 'restricted')
main()
