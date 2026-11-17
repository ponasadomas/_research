R=[]
def Q(u,c,sp,st,ty,th,q,cx,r=None): R.append(dict(u=u,c=c,sp=sp,st=st,ty=ty,th=th,q=q,cx=cx,r=r))
EM='expecting_mother'; XM='experienced_mother'; PU='parent_unspecified'
Q('pregnant-1uzjlrf',None,XM,'second_pregnancy','question',['second_pregnancy','glider','what_to_buy','over_consumerism'],
 "I really want a glider, it would have to be placed in the living room due to limited space. Do you guys things it’s worth it or just over consumerism?","Pregnant with her second in a two-bedroom New York apartment.")
Q('BabyBumps-1uzmrua',None,XM,'looking_back','failure_story',['what_to_buy','second_pregnancy','not_worth_it','stokke'],
 "I got the Stokke Sleepi Mini for my second baby.. and she's too big for it at 14 weeks!","Post titled 'Save money - don't bother with the mini crib'.")
Q('BabyBumps-1uzmrua',None,XM,'looking_back','price_signal',['comparison_other_pregnancies','price_value','what_to_buy'],
 "With my first we just got a crib where you could adjust the height of the mattress and it worked better and was cheaper by a ridiculous amount.","Same post.")
Q('BabyBumps-1uzmrua',None,XM,'looking_back','price_signal',['not_worth_it','price_value'],
 "It's pretty but so not worth it!","Same post, her verdict.")
Q('BabyBumps-1v0atyk',None,XM,'second_pregnancy','purchase',['postpartum_doula','employer_benefit','partner_role','money'],
 "My husband’s work gives us up to $10,000 for a postpartum doula, but it has to be used before our baby is 6 weeks old.","Planning how to use the hours for her second baby.")
Q('BabyBumps-1v0atyk',None,XM,'second_pregnancy','desire',['postpartum_doula','sleep','first_two_weeks'],
 "We were thinking mostly 8-hour overnight shifts since a full night of sleep seems invaluable, but now I’m wondering if a 4-hour daytime shift each week would be helpful too.","Same post.")
Q('BabyBumps-1v0atyk',None,XM,'second_pregnancy','desire',['pregnancy_with_toddler','older_child_care','postpartum_doula'],
 "We’ll also have a 2.5-year-old, so daytime help could let me spend more time with him.","Same post.")
Q('BabyBumps-1v0axx0',None,EM,'third_trimester','trigger_moment',['birth_course','late_preparation','youtube'],
 "I’m super late to the game on this… I’m 37.5 weeks pregnant and I need to watch a birth class of some sort.","Looking for a free online birth class.")
Q('BabyBumps-1v0axx0',None,EM,'third_trimester','price_signal',['birth_course','price_value','hsa','maternity_leave','unpaid_leave','usa'],
 "I didn’t do the one through my hospital for a few reasons: 1) I’ve heard mixed things on the actual helpfulness of these classes, 2) they were $175 for 1 session, 3) I have a high deductible health care plan that didn’t cover the class and I didn’t want to use my HSA (and my other income - I don’t get any pay for my maternity leave) on it if there are free resources online.","Same post; why she skipped the hospital class.")
Q('BabyBumps-1v0axx0',None,EM,'third_trimester','question',['birth_course','who_to_believe','quality'],
 "I’ve done a quick search but I’m not sure which one will actually be quality and informative.","Same post.")
Q('NewParents-1v0bv12',None,EM,'third_trimester','purchase',['momcozy','gift','nesting'],
 "I was gifted the momcozy bottle washer and I’m obsessed. I did two loads today while I’m nesting.","At eight months; the washer needs distilled water for each cycle.")
Q('NewParents-1v0bv12',None,EM,'third_trimester','price_signal',['momcozy','running_costs','price_value'],
 "I would love to go this direction to save money and trips to the grocery store. My only concern is that making the distilled water myself will take too much time and be unrealistic for my needs. For reference, I’m looking at a $70 model from Amazon.","Same post; considering a home water distiller.")
Q('PregnancyUK-1v0k14p',None,EM,'unknown','belief',['private_care','uk_nhs','choosing_provider','first_pregnancy'],
 "Pregnant with my first baby and considering private maternity in London, albeit live 1 hour outside of London but local NHS has very bad reputation.","Has looked at the Lindo Wing.")
Q('PregnancyUK-1v0k14p',None,EM,'unknown','price_signal',['private_care','birth_cost','uk'],
 "How much are you expecting to pay / have paid? We have been told it will be between £20,000 and £30,000.","Same post.")
Q('PregnancyUK-1v0m9db',None,'new_mother','newborn_0_2_weeks','price_signal',['stretch_marks','skincare','price_value','uk'],
 "The pai stuff was expensive but was given as a gift, otherwise the other stuff is pretty affordable I think.","Two weeks postpartum, listing the Superdrug products she used.")
Q('PregnancyUK-1v0m9db','oyiv1mr','new_mother','newborn_0_2_weeks','belief',['stretch_marks','skincare','no_promise'],
 "I wouldnt want to suggest these products would magically solve anything, just wanted to share incase useful x","Her reply to a commenter questioning the post.")
Q('PregnancyUK-1v0mmc7',None,EM,'second_trimester','pain',['uk_nhs','paperwork','no_one_told_me','inconsistent_care'],
 "It's so frustrating how inconsistent this approach is within the NHS!","Never offered the maternity exemption certificate for free prescriptions.")
Q('PregnancyUK-1v0mmc7',None,EM,'second_trimester','pain',['uk_nhs','paperwork','no_one_told_me','midwife'],
 "I am 22 weeks now and not a single midwife even mentioned about that.","Same post.")
Q('PregnancyUK-1v0mmc7',None,EM,'second_trimester','others_said',['uk_nhs','paperwork','gp','waiting'],
 "The GP didnt even know the timeline for me to get the actual certificate nor the process. When I asked about ETA, he told me it can take between 3-5 WEEKS to have it processed?!","Same post.")
Q('PregnancyUK-1v0mmc7',None,EM,'second_trimester','belief',['uk_nhs','paperwork','hidden_entitlements'],
 "I had the impression they dont want you to know about it in London.","Same post.")
Q('PregnancyUK-1v0mmc7','oyhe654',EM,'second_trimester','price_signal',['uk','prescription_cost','shortage'],
 "Aspirin became so expensive this year! One box with 28 capsules are costing around £6. Boots and Amazon are even limiting the number of boxes you can buy.","Her reply.","medication")
Q('PregnancyUK-1v0mmc7','oyheblw',EM,'second_trimester','pain',['uk_nhs','dental_care','access'],
 "I am still trying to book dental care but all 8 places I've called so far don't have \"NHS slots\" anymore... 🥲","Her reply; free NHS dental care in pregnancy she can't use.")
Q('PregnancyUK-1v0mmc7','oyhfrwh',EM,'second_trimester','pain',['paperwork','deadlines','no_one_told_me','matb1'],
 "I didn't know I had to present it before 25 weeks! Good i already filled that in, together with the exemption certificate!","Her reply about another form from the GP.")
Q('PregnancyUK-1v0mmc7','oyhhous',EM,'second_trimester','belief',['uk_nhs','proactive_care','money'],
 "I am more frustrated about not being a consistent and proactive approach, than the money spent so far.","Her reply.")
Q('PregnancyUK-1v0mmc7','oyhi84u',EM,'second_trimester','pain',['mental_load','paperwork','chasing'],
 "So much to plan already, having to chase for something like this shouldn't even be on your plate, right?!","Her reply.")
Q('PregnancyUK-1v0mmc7','oyi69it',EM,'second_trimester','belief',['first_pregnancy','not_knowing_what_to_expect'],
 "It's all so new for me with the first baby!","Her reply.")
Q('PregnancyUK-1v0mmc7','oynauno',EM,'second_trimester','success_story',['uk_nhs','midwife_helpline','paperwork'],
 "I've called Midwife helpline and she had it sorted and sent via email in seconds 🥹🥲","Her update the next day.")
Q('Mommit-1v0nrfd',None,XM,'second_pregnancy','question',['second_pregnancy','pregnancy_with_toddler','paid_help','money'],
 "I’m pregnant with #2 (our oldest will be just under 2 when she’s born), and we’re trying to decide where to invest our money to reduce stress.","Lists night nanny, au pair, cleaner, meal service, laundry and more.")
Q('Mommit-1v0nrfd',None,XM,'second_pregnancy','desire',['paid_help','sleep','mental_load','not_products'],
 "I’m especially interested in things that gave you more time, sleep, or mental bandwidth—not products.","Same post.")
Q('NewParents-1v0o968',None,EM,'third_trimester','trigger_moment',['first_pregnancy','late_preparation','what_to_buy'],
 "I haven’t really considered the whole diaper situation yet and I’m realizing I probably should get it figured out.","At 39+5 with her first; the baby will share a room with her stepson.")
Q('NewParents-1v0o968',None,EM,'third_trimester','price_signal',['diaper_pail','running_costs','blended_family'],
 "I don’t really want a diaper genie or anything with expensive bag refills..","Same post.")
Q('NewParents-1v0o968','oygl76i',EM,'third_trimester','question',['diaper_pail','worth_it'],
 "Does the diaper genie actually stop the smell? Do you feel like it’s worth it?","Her reply.")
Q('Mommit-1v0smx9',None,XM,'second_pregnancy','question',['third_pregnancy','car_seats','pregnancy_with_toddler','school_run'],
 "I’m pregnant with my 3rd and trying to figure out how I want to configure the car seats in our van when the time comes and what will work best for car rider line especially.","Children will be nearly 7 and 4 when the baby arrives.")
Q('Mommit-1v0smx9',None,XM,'second_pregnancy','belief',['third_pregnancy','overthinking'],
 "I’m probably way overthinking this 😅","Same post, closing line.")
Q('pregnant-1v0z8l8',None,EM,'second_trimester','price_signal',['maternity_clothes','body_changes','waste_money'],
 "So far, I haven't bought any new clothes during pregnancy because I have no idea what will fit me.","At 18 weeks, wants outfits for a trip at 23 weeks.")
Q('pregnant-1v0z8l8',None,EM,'second_trimester','price_signal',['maternity_clothes','waste_money'],
 "lol I want to shop but don't want to waste money on things that won't end up fitting right.","Same post.")
Q('pregnant-1v1iihv',None,XM,'second_pregnancy','desire',['solo_mother','pregnancy_with_toddler','paid_help','first_two_weeks'],
 "Ideally, I'd love help with things like, watching my toddler so I could shower, shopping, meal prep, help around the house, and especially extra help after the baby arrives for the first 6 months postpartum.","Newly single at six months pregnant, eastern US.")
Q('pregnant-1v1iihv',None,XM,'second_pregnancy','price_signal',['postpartum_nanny','price_value','solo_mother'],
 "I looked into Asian postpartum nannies, but the cost for about 90 days of care was around $50,000, which is WAAAY beyond my budget. I wish I was loaded like that.","Same post; hoping to trade room and board for help.")
Q('pregnant-1v1jdmp',None,PU,'unknown','success_story',['nausea','vomit_bags','humour'],
 "Since then I’ve used 40-50 vomit bags and I just love them. I vomit in the car, in bed, at bingo, on the move. I just feel so free.","Humorous post, first written for a sickness subreddit.")
Q('pregnant-1v1jdmp',None,PU,'unknown','others_said',['nausea','partner_role','embarrassment'],
 "My boyfriend tells me to put them away cause they’re embarrassing, whereas to me it’s the same as a Birkin, I carry it with pride.","Same post.")
Q('PregnancyUK-1v1jq5l',None,EM,'second_trimester','question',['hospital_bag','postpartum_recovery','what_to_buy','first_pregnancy'],
 "Have bought the bulk of things I need. I’m torn between 2 items. Which did you get on with better and would recommend in my hospital bag or to aid in postpartum recovery?","At 20 weeks, Frida Mom witch hazel pads or Expert Midwife spritz.")
Q('BabyBumps-1v1lg1a',None,EM,'unknown','pain',['doula','choosing_provider','virtual_meetings'],
 "We met with a few doulas and don’t feel like we click with any of them. It’s all through zoom. Is this normal?","Looking for an experienced doula in the Boston area.")
Q('BabyBumps-1v1lg1a',None,EM,'unknown','price_signal',['doula','price_value','hospital_connections'],
 "She’s about $1k more expensive than other doulas but wondering if you think the connections and familiarity she has with the hospital are worth it","Same post; the doula also works as a nurse at her OB's office.")
Q('BabyBumps-1v1lg1a','oyon9mv',EM,'unknown','question',['continuity_of_care','choosing_provider'],
 "Did you feel like it was ok that the OB you saw for prenatal visits wasn’t the one who delivered the baby?","Her reply.")
Q('pregnant-1v1t7gh',None,XM,'second_pregnancy','success_story',['maternity_clothes','comparison_other_pregnancies','tried_products'],
 "I have these leggings that I purchased when I was pregnant with my first and I literally swear by them they are buttery soft they looked amazing while I was pregnant. They actually grew with me and I got to wear them after I gave birth too.","Asks what brands others still vouch for; names no brand.")
