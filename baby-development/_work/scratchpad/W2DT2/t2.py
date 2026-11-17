from build import build
k={
'1ulgd6b':('keep_core','father on leave, 4-month-old, how to entertain him all day'),
'1up34sw':('keep_core','delay worry, near-2-year-old speech and play, father comparing with peers'),
'1uxhuvm':('keep_core','delay worry, 4-month-old tummy time head lift, early intervention referral'),
'1v7r1wi':('keep_core','18-month-old, Ms Rachel on long flight, couple debates screens'),
'1v9wffg':('keep_core','15-month-old after heavy screen time, plays less with toys, needs activities'),
}
d={
'1ueus8i':'gamer dad marriage, off-topic','1ugt7n2':'supporting a new father, not development','1uhj8fg':'fall injury of 8-month-old','1uict0g':'3-year-old tablet, over 24 months',
'1un930m':'travel crib safety incident','1uo8rjp':'3.9-year-old behaviour','1ur87b5':'pregnancy announcement reactions','1us16gz':'3-year-old clingy, older child',
'1uult35':'almost-5-year-old screen tantrums','1uzxhw6':'long flight tips, development passing mention','1v1moyd':'5 and 3-year-olds school choice','1v1s1bx':'baby gate installation, safety gear',
'1v3imiu':'husband working hours, relationship','1v4u6ps':'encouragement post to new fathers','1v5ju0c':'a father own feelings about becoming a parent',
'1v6zh2u':'4.5-year-old co-sleep','1v83dqe':'game console for 7-year-old','1vel65l':'safety: prenatal screening worry','1vgyniv':'work travel and presence, 9.5-month-old',
'1vh3sxr':'father exhaustion, daily routine','1vi7qg8':'toddler injury','1vjw8mt':'partner dropped baby, trust','1vkgxnc':'update on couple conflict','1vklnld':'unwanted gifts from in-laws',
'1vly2mm':'grandparent habit with 4 and 2-year-olds','1vmo020':'birth experience memory','1vnr2no':'guilt over daycare for 3-month-old','1vohnzk':'10-year-old and family conflict',
'1vum3r4':'sleep-only, 9-month-old','1vuvrxh':'taking down crib, nostalgia',
}
ids=[l.split(' | ')[0] for l in open('A-daddit-001.txt')]
build('A-daddit-001.txt','m7.tsv',{i:(k[i] if i in k else ('drop',d[i])) for i in ids})
w={
'1uq07bq':'postpartum mood and return to work','1uq5vty':'daycare incident, 5-month-old','1ur981l':'8-month-old crying at daycare','1urv65d':'chaotic morning vent',
'1uvamhz':'career change','1uwnr50':'daycare reassurance for 4-month-old','1v0rm1v':'overwhelm, 3 and 1-year-olds, medication','1v2soak':'childcare choice with grandmother',
'1v3qyxg':'daycare search anxiety','1v887wc':'deciding on a third child','1v8zbec':'car accident stress','1va2ry4':'schedule with stay-at-home father',
'1vaarta':'nanny vs group care at 2.5 years','1vebx7i':'maternity leave eligibility','1vew6bg':'daycare turnover, 2.5-year-old twins','1vfatmz':'4-year-old school choice',
'1vflj1n':'work and childcare dilemma','1vgbjzf':'bored on summer at home with toddler, child age unstated','1vjvhav':'isolation and no village','1vk22a6':'burnout after return to work',
'1vkkvmp':'daycare switch for 2 and 4-year-olds','1vr0mog':'4-year-old pre-k encouragement','1vrf1i6':'safety: therapy appointments and diagnosis for older child','1vrxqjc':'juggling jobs and volunteering',
'1vtylwh':'daycare disagreement with husband',
}
w['1vlizqb']=None
rows={i:('drop',w[i]) for i in w if w[i]}
rows['1vlizqb']=('keep_core','14-month-old cries unless held, will not play alone, guilt toward 3-year-old')
build('A-workingmoms-001.txt','m9.tsv',rows)
