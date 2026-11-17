R=[]
def Q(u,c,sp,st,ty,th,q,cx,r=None): R.append(dict(u=u,c=c,sp=sp,st=st,ty=ty,th=th,q=q,cx=cx,r=r))
EM='expecting_mother'; XM='experienced_mother'; PU='parent_unspecified'
CR='unit has hopelessness wording; whole unit restricted'
Q('BabyBumps-1v77lxx',None,EM,'unknown','belief',['hand_me_down','registry','what_to_buy'],
 "Obviously, the pro of using hand me downs are they they're free and it means fewer things to store. If I wait and buy more later once the baby is born, I'll have clutter to manage and no one buying it off my registry.","A friend gave her a pile of baby gear; deciding what to keep off her registry.")
Q('BabyBumps-1v77lxx',None,EM,'unknown','pain',['work_in_pregnancy','return_to_work','feeding','maternity_leave'],
 "I plan to mostly breastfeed on mat leave but will need to go back to work part-time at 8 weeks.","Same post; why bottles matter.")
Q('PregnancyUK-1v7bwsp',None,EM,'third_trimester','pain',['loneliness','birth_course','nct','price_value','uk_nhs','no_village'],
 "We both don't have any friends that have babies which can feel quite isolating, the NHS antenatal classes were fully booked in our area and we can't afford the NCT classes.","Due in early October in Manchester; looking for other parents-to-be.")
Q('PregnancyUK-1v7bwsp','p01nm8l',EM,'third_trimester','success_story',['community','meeting_parents'],
 "we have made a group chat if you're interested! ive private messaged you ☺️","Her reply a day later.")
Q('PregnancyUK-1v7lz3d',None,EM,'second_trimester','question',['hospital_bag','feeding','what_to_buy','first_pregnancy'],
 "I’ve come across the Aptamil ready to feed (with teat/ nipple) that alot of mums pack in their hospital bag. Is this necessary? Shall I also buy it?","First-time mother who has bought almost everything on her list.")
Q('PregnancyUK-1v80vao',None,PU,'unknown','desire',['birth_course','meeting_parents','uk'],
 "Looking for some recs for the best antenatal classes in east/north London. I'm primarily there to meet some friends in the area","Due mid-December; the class is mainly for friends.")
Q('pregnant-1v838af',None,EM,'second_trimester','price_signal',['doula','postpartum_doula','price_value','first_pregnancy'],
 "The investments in any of these resources are (justifiably!) quite high, so we need to pick and choose where we want and need the most support.","Halfway through her first pregnancy, choosing between birth, postpartum and overnight doulas.")
Q('pregnant-1v838af',None,EM,'second_trimester','belief',['what_eased_fear','similar_stories','lived_experience'],
 "I find hearing other people's lived experiences and points of view often offers new perspectives through which to consider my own.","Same post.")
U='pregnant-1v84prn'
Q(U,None,EM,'third_trimester','trigger_moment',['ob_prepayment','global_fee','dropped_from_care','usa'],
 "My OBs office requires payment in full by 24 weeks. I owed about $4k, which included the delivery. I was able to get them to extend the deadline and was hopeful that I could pay it in time.","At 35 weeks, her OB stops seeing her over the unpaid balance.",CR)
Q(U,None,EM,'third_trimester','others_said',['ob_prepayment','dropped_from_care','money_worry'],
 "They told me at my appointment last week that due to my remaining balance, they would have to stop seeing me until I paid in full (yeah right, like 1.8k is just going to magically fall into my lap..)","Same post.",CR)
Q(U,None,EM,'third_trimester','others_said',['medicaid','insurance','usa','wrong_information'],
 "Everyone told me I would automatically qualify due to pregnancy but apparently that's not the case.","Same post; told she earns too much for Medicaid.",CR)
Q(U,None,EM,'third_trimester','pain',['work_in_pregnancy','working_until_labour','money_worry'],
 "I'll be working until delivery most likely because I obviously cant afford to take time off.","Same post.",CR)
Q(U,'p03y6tm',EM,'third_trimester','price_signal',['insurance','birth_cost','usa'],
 "I do have insurance through my workplace, thats the worst part is this is the price WITH insurance. I feel like it would have been cheaper not to have insurance.","Her reply.",CR)
Q(U,'p0493gb',EM,'third_trimester','pain',['short_term_disability','maternity_leave','usa'],
 "I am but at a reduced pay rate and I only get 6 weeks if vaginal birth and 8 weeks for c section. Ideally i want those to be when my son is here so I can spend as much time as possible with him.","Her reply about paid leave.",CR)
Q(U,'p04o3fx',EM,'third_trimester','price_signal',['birth_cost','prenatal_bills','usa'],
 "Its multiple bills totalling up from basically my emtire pregnancy, the ultrasounds, prenatal care, extra testing, etc","Her reply on what the $4k covers.",CR)
Q('BabyBumps-1v88rr2',None,EM,'unknown','fear',['doula','perineal_prep','tearing_fear','birth_fear'],
 "I am wondering if a doula would be worth it for me in particular. I am absolutely terrified of tearing.","Her first midwife appointment is a month away.")
Q('BabyBumps-1v88rr2',None,EM,'unknown','pain',['waiting','first_appointment','midwife'],
 "Just hoping to get some advice since my first appt with my midwife is not for another month.","Same post.")
Q('pregnant-1v8aw4e',None,EM,'second_trimester','question',['pelvic_floor_physio','worth_it','friends'],
 "Currently approaching third trimester and a few friends have recommended it but not sure how mandatory it is","Asks whether pelvic floor therapy in pregnancy was worth it.")
U='BabyBumps-1v97sk5'
Q(U,None,EM,'unknown','failure_story',['book','information_overload','alarmist_content','first_pregnancy'],
 "I bought a book as soon as I found out I was pregnant (Nurture by Erica Chidi) and it’s really not what I was looking for. Example: the book pretty immediately goes into checking your household for toxic and harmful chemicals, which led me down a slippery slope of wanting to throw out all of my personal care products.","Asks for a pregnancy book that won't make her more anxious.")
Q(U,None,EM,'unknown','objection',['book','alarmist_content','diet_rules'],
 "Surely there are more important things for me to worry about than sulfates!","Same post.")
Q(U,None,EM,'unknown','desire',['book_request','low_stress','body','decisions','guide_request'],
 "Is there a book you recommend for people who want a really low-stress, common-sense approach to learning about what’s happening in my body, preparing for parenthood, and making important decisions about pregnancy/birthing?","Same post.")
Q(U,'p0cmem2',EM,'unknown','pain',['information_overload','alarmist_content','filtering'],
 "there’s just so much pregnancy info out there that feels alarmist and constantly trying to filter it out is exhausting.","Her reply.")
Q(U,'p0d2qy5',EM,'unknown','question',['book','week_by_week','timing'],
 "is it something you’d read in the first trimester or is it super focused on birth and maybe a 2nd/3rd trimester read?","Her reply about a recommended book.")
Q('pregnant-1v9bjdr',None,EM,'unknown','failure_story',['keepsake_scan','boutique_scan','billing_dispute'],
 "I scheduled the gender reveal scan, but I was apparently charged for the early pregnancy scan.","A boutique scan studio later called asking her to buy a gift card to cover the difference.")
Q('pregnant-1v9bjdr','p0chmmt',EM,'unknown','price_signal',['boutique_scan','gift_card','price_value'],
 "require me to pay at least $100 more to use it since the scans cost more the farther along you are.","Her reply on why a gift card would be wasted.")
Q('pregnant-1v9bjdr','p0d4iyt',EM,'unknown','price_signal',['boutique_scan','customer_loyalty'],
 "It seems silly to potentially lose a repeat customer over $30. Because I definitely don’t want to go back now. 🥴","Her reply.")
U='pregnant-1v9fbc3'
Q(U,None,'new_mother','looking_back','price_signal',['ob_prepayment','induction','birth_cost','usa'],
 "I prepaid for my scheduled induction about $1k. The finance department at the hospital said there was no downside to doing this.","Post titled 'Do not prepay the hospital for your scheduled labor'.","induction (medical procedure)")
Q(U,None,'new_mother','looking_back','failure_story',['ob_prepayment','deductible','insurance','usa'],
 "The issue is this payment is never recorded by your insurance and does not go to your deductible or out of pocket max.","Same post.")
Q(U,None,'new_mother','looking_back','success_story',['ob_prepayment','refund','insurance'],
 "Somehow, my insurance was able to call the hospital and have them reimburse me for the $1k prepayment (it’s been 5 months). The hospital showed it as a surplus credit on my account, although they did not say this to me once after many calls.","Same post.")
Q(U,None,'new_mother','looking_back','pain',['confusing_rules','insurance','fsa','usa'],
 "I’m continuously confused and frustrated by the medical system.","Same post; also can't use a dependent spending account for the birth.")
Q(U,'p0dh8tx','new_mother','looking_back','pain',['ob_prepayment','contradictory_advice','opaque_billing'],
 "My insurance told me not to prepay but it seems like it is sometimes required based on this thread. Why is it all so opaque!? 😭","Her reply.")
Q(U,'p0gdzpw','new_mother','looking_back','belief',['ob_prepayment','refund'],
 "It should be illegal for them not to refund. If I didn’t ask I would have never saw that money again.","Her reply.")
Q(U,'p0gf857','new_mother','looking_back','regret',['ob_prepayment','itemised_bill','not_understanding'],
 "I asked for an itemized receipt before paying and I STG it said labor and that’s it. I asked a million questions and came to the conclusion of prepaying. But I really didn’t understand it at the time.","Her reply.")
U='pregnant-1v9harg'
Q(U,None,EM,'first_trimester','pain',['sleep_in_pregnancy','back_pain','first_pregnancy'],
 "have been having a heck of a time sleeping and have really bad back pain because I literally toss and turn all night, front, side, back, round and round like a freaking rotisserie chicken.","At 9+3, first pregnancy.")
Q(U,None,EM,'first_trimester','question',['pregnancy_pillow','what_to_buy','too_early'],
 "I'm contemplating buying a pregnancy pillow, but I don't know if it's stupid because I don't even have a bump yet.","Same post; signs off 'my back hurts so bad and it's still way too early for this'.")
Q(U,'p0dsgeb',EM,'first_trimester','purchase',['pregnancy_pillow'],
 "🙌🙌 I just ordered one. Hooray!!","Her reply after commenters said it isn't too early.")
Q('BabyBumps-1v9m4r9',None,EM,'unknown','purchase',['travel_cot','first_pregnancy','sizing_confusion'],
 "I am currently pregnant with my first baby and have just purchased the moose emmet travel cot with bassinet insert.","Bundled sheets don't fit the thin mattress.")
U='BabyBumps-1v9zwoy'
Q(U,None,EM,'second_trimester','others_said',['midwife','doula','hypnobirthing','epidural_decision'],
 "She said she’s never seen anyone with a doula, doing hypnobirthing classes and still getting an epidural.","At her 18-week check, her midwife was surprised by her plan.","epidural (medical procedure decision)")
Q(U,None,EM,'second_trimester','fear',['doing_too_much','birth_course','second_guessing'],
 "I just explained I wanted my bases covered, but now I feel kind of crazy? Midwife was very nice, but now I’m worried I’m doing too much/ taking the wrong classes?","Same post.")
Q(U,'p0j6os1',EM,'second_trimester','belief',['hypnobirthing','calm'],
 "I also hate the idea of baby being born in a stressed-out environment and thought hypnobirthing would help keep me calm.","Her reply.")
Q('Doulas-1vacl1q',None,EM,'second_trimester','price_signal',['doula','birth_course','partner_role','price_value'],
 "but cannot afford to hire a doula. Looking for classes focused on unmedicated birth prep that include partners.","Six months pregnant, asking doulas for birth-prep classes.")
U='pregnant-1vawhz6'
Q(U,None,XM,'second_pregnancy','price_signal',['registry','gifts','price_value','luxury'],
 "But the registry minimum for 1 item is $40…and the maximum is $1800 for a travel system. And I’m talking $40 for 2 pacifiers that have rubber imported from Africa and are made with bamboo imported from Beijing.","Pregnant herself, shopping a family friend's registry.")
Q(U,None,XM,'second_pregnancy','pain',['registry','gifts','budget_gap'],
 "I’m not trying to shame anyone for their preference, but it’s very clear that we are not operating in the same budget. I feel lame only purchasing 2 pacifiers.","Same post.")
Q(U,'p0oupdf',XM,'second_pregnancy','advice_given',['registry','completion_discount'],
 "I also had larger items on my registry that I put on there to get the 15% off discount!","Her reply.")
Q(U,'p0org9k',XM,'second_pregnancy','belief',['first_two_weeks','what_to_buy','last_minute'],
 "I know my husband and I had a lot of Amazon packages coming in the first days home 😅","Her reply on gifting first-week things instead.")
Q(U,'p0pi19h',XM,'second_pregnancy','price_signal',['gifts','budget','registry'],
 "My budget is $40-50. I think it’s completely silly to wrap one single pacifier to unwrap as a gift 😅","Her reply; will send cash or a gift card.")
Q(U,'p0p6dlx',XM,'second_pregnancy','pain',['rural','food_delivery','access'],
 "We are 40 minute drive to the grocery store rural 😅 and if we do try and use food delivery apps usually it’s 2-3 hours wait time for someone to pick up from the restaurant and the food is cold lol","Her reply to a meal-delivery suggestion.")
Q('BabyBumps-1vb74xk',None,XM,'second_pregnancy','question',['double_stroller','pregnancy_with_toddler','babywearing'],
 "I’m trying to decide whether it makes sense to purchase a double stroller since I’ll probably be baby wearing the first few months while pushing my then-2 year old.","Second baby due in February.")
Q('BabyBumps-1vb74xk',None,XM,'second_pregnancy','belief',['mother_in_law','family_support','double_stroller'],
 "We currently have two travel strollers and my MIL is generally around to help, so we could also just push two strollers once the baby gets big enough to sit in one.","Same post.")
