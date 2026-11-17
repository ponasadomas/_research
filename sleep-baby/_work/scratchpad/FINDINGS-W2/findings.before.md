# Findings — baby and toddler sleep, 0–36 months (Mamivio)

**Date:** 2026-10-25. **Totals** (from `counts.md`): 6,659 verbatim quotes from 2,630 Reddit units read in full (a unit is a post plus the original poster's replies); 2,486 units gave at least one quote and 144 gave none (all 144 are named in a reader ledger). The quotes sit in 21 reader voice files (`voice/reddit-r01.jsonl` … `r21.jsonl`, merged in `voice-merged/all.jsonl`). Sources: r/sleeptrain 3,584 quotes, r/NewParents 1,034, r/toddlers 487, r/beyondthebump 381, r/Mommit 276, r/beyondthebumpUK 237, r/AttachmentParenting 237, r/Parenting 170, r/daddit 115, r/FirstTimeMom 74, r/sahm 27, r/workingmoms 21, r/ScienceBasedParenting 15, r/GentleParenting 1. Also used: 26 competitor teardowns (`competitors/`) and the owner's 2026-10-25 Meta Ad Library sweep (`../main/ads-running/spend-footprint-by-subniche-2026-10-25.md`). The posts date from 2026-08-25 to 2026-10-25 (tier A, wave 1; see `sources/reddit.md`).

## How to read this

- Text in double quotes followed by an id such as [sb01-0028] is the parent's exact words; look the id up in `voice-merged/all.jsonl`. Everything else is interpretation. A claim with no id says "(interpretation)".
- **Every number is a count of quotes chosen by readers. It is never a count of people and never a measure of prevalence.** Theme counts also undercount, because readers spelled some tags differently (`only_mum_settles` / `only_mum_can_settle`, `retraining_after_setback` / `retraining`, `vomiting_stop` / `vomiting_crying`) and `counts.md` counts each spelling separately.
- The corpus leans on one community: r/sleeptrain gave 3,584 of the 6,659 quotes. People go there when they are already thinking about training, so the voice leans towards parents who want a method. Parents who are content without training come in mainly through r/AttachmentParenting, r/NewParents and r/Mommit.
- Speakers: "mothers" means quotes tagged `new_mother` (2,405) or `experienced_mother` (526), where the author said she is a mother. "Parents" means `parent_unspecified` (3,364), where the author did not say. "Fathers" or "partners" means `partner` (263), which in this niche is mostly fathers writing about their own nights.
- Ids marked "(restricted)" touch a line not to cross (`restricted-ids.md`). They are cited as evidence of a pattern only; their words are never quoted here.
- Where a pattern rests on a handful of quotes, the text says so. Where readers disagreed, both sides are shown.

---

## 1. The reader in one paragraph

She is a parent, usually the mother, of a baby between about four months and two years old. She writes at 3am or 5am and posts a log of the night: "Its 545am and Ive had 14 resettles in the cot since 10pm last night" [sb06-0281]; "Last night he was up at 9,11,12,1,3 and then ready to start the day at 6" [sb06-0260] (a father). She has already tried several methods, apps and schedules, and her first question is about herself: "Can someone please help me with what I’m doing wrong? I’m so defeated." [sb04-0136]. She does not want a philosophy. She wants a plan for this child, written so a tired brain can follow it: "I need the instructions in kindergarten language right now" [sb10-0261]; "I just need a starting point, a realistic plan, and some hope" [sb17-0354]. What she wants back is small and personal: "I just want a little bit of my evening back." [sb11-0192]. Her body, her marriage and her job are paying for the nights [sb03-0102] [sb08-0261] [sb05-0056]. She is caught between crying she cannot bear and a life she cannot keep living: "But the other part of me is thinking I cannot keep living like this." [sb08-0154]. Even when something works, she expects the next tooth, cold or trip to undo it [sb05-0129]. She trusts other parents in the same situation more than any expert, and paid help has let her down by giving her the same schedule as everyone else [sb01-0028].

## 2. The arc (stages, with quotes)

The stage counts in `counts.md` show where readers found the quotes: baby_5_8_months 2,137; toddler_12_24_months 1,157; baby_9_12_months 972; regression_4_months 763; baby_2_4_months 648; toddler_24_36_months 556; newborn_0_8_weeks 281. The arc below is the shape most stories take (interpretation built from the quotes cited).

**1. Newborn: survival, contact naps, a body that gives out.** Parents hold the baby all day, bounce and use carriers: "She’s getting heavy, my back is destroyed" [sb02-0037]; "I currently have carpal tunnel in both wrists from all the rocking and holding." [sb02-0239]. What they want is tiny: "All I’m looking for is MAYBE 4 naps a day." [sb07-0113]; "I just want 20 minutes at a time to shower, eat a proper meal" [sb20-0011].

**2. The 4-month regression: the cliff.** "That was until the 4 month sleep regression hit at around 19 weeks. Then she went from one wake up a night to waking up every hour." [sb12-0035]. For some there was never a single cliff: "Everyone told me we just need to get past the 4 month regression. But there was no regression." [sb11-0060]. Being warned did not help: "Well, everyone tried to scare us, and it worked." [sb07-0138]. `regression_4_month` is tagged on 247 quotes.

**3. Five to twelve months: the search for a method.** The quote count peaks here. Parents read, track and ask which method fits: "How can I know which is the best approach for my baby ?" [sb05-0034]; "How can i know ahead of trying what suits my kid? Im unable to guess" [sb05-0278]. What tips them into training is their own state, not the baby's age: "I was completely exhausted and couldn’t function the next day" [sb10-0093]; "I don’t function well on no sleep, the whole reason why we sleep trained to start with." [sb11-0246]. The trigger is often a life event: "It was my first day back in office so idk if that messed with him." [sb07-0084], a broken wrist [sb07-0031], a husband's leave ending [sb07-0032].

**4. The attempt.** Parents keep night logs and count the minutes of crying, and the parent cries too: "He only cried for 15 minutes before falling asleep, but I cried for hours afterwards" [sb07-0198]. Some attempts work quickly [sb11-0004] [sb07-0136]; many stall or end on night one or two [sb10-0120] [sb07-0164]. Online success stories set a bar the family then misses: "I feel so duped by all of the success stories." [sb19-0256].

**5. The setback and retraining.** This is the most common story shape across readers R05–R21: it worked, then a tooth, cold, trip, move, daycare or new skill undid it. "always something happened (sickness, tooth pain, holidays) and we had to do it all over again." [sb05-0129]; "Successfully sleep trained at 6MO only to be co sleeping at 8MO" [sb12-0069]; "we have to keep doing it every now and then" [sb08-0109]; "both times it worked, life just got in the way" [sb10-0098]. `retraining_after_setback` is tagged on 264 quotes, plus quotes under other spellings. It gets harder with age: "it feels harder this time because he's older" [sb20-0248]. And they fear the chance has passed: "now I'm afraid we missed the sleep training train" [sb06-0104]; "I feel like I missed the boat and now it'll be so difficult." [sb06-0176].

**6. The toddler cliff and bedtime battles (12–36 months).** Children who slept well suddenly need a parent in the room, and crying methods feel different with an older child: "It felt more reasonable when she was 4 months old" [sb09-0082]. The longest arc in the set comes from a mother of an 11.5-month-old: "I have subjected my 11.5M baby to multiple rounds of sleep training" [sb09-0024]; "we steeled ourselves again, saying we just hadn’t been consistent or hard enough" [sb09-0026]; "I feel I have subjected her to so much" [sb09-0027].

**7. After: relief that does not quite trust itself.** "I keep waiting for the other shoe to drop" [sb02-0149]; "Is he just a unicorn meant to convince me to have a second baby?" [sb02-0104]. Where regret appears, it is about waiting too long, not about training: "Mine is that I wish I sleep trained before 7.5 months." [sb02-0081]; "I only wish I did it sooner with both kids." [sb02-0198]. (`regret` is a small type: 70 quotes.)

## 3. What others say to them

Relatives, friends, doctors, daycare staff and strangers online repeat the same few sentences. They fall into five scripts (interpretation; the quotes are the evidence).

1. **"Go with the flow" / "it gets better."** "someone proceeded to tell me that I just needed to go with the flow more" [sb04-0025]; "everyone keeps telling me to go with the flow and chill and ignore wake windows" [sb05-0200]; "People keep saying it gets easier, but when?" [sb05-0117]; and the reverse, "everyone keeps telling me it gets worse not better" [sb05-0206]. A father: "and I hate them for it, because they don’t actually know what this is like." [sb20-0274].
2. **"You made the baby this way."** "comments so I tried really hard not to use my carrier while getting ready for work" [sb05-0157]; "blame us for creating bad habits" [sb10-0005]; "I’ve been told I’m coddling him, putting him in a bubble" [sb10-0147]; "I spoil him too much" [sb03-0039]; a doctor and a receptionist told one mother it was her fault [sb06-0126].
3. **"Just let her cry."** "she will cry but eventually realize that nobody is coming" [sb03-0088]; a grandmother: "I’ve been a mother for longer than you, and I have two children." [sb03-0084]; "my mom did that to me when I was a baby and I’m not traumatized" [sb05-0141].
4. **"My babies just slept."** "my kids never did that, they would just sleep when they were tired" [sb02-0113]; "Everyone we know loves to remind us they had 1) babies that magically slept through the night" [sb11-0264]; "Every person I talk to in real life says their baby was sleeping through the night at like 2 months" [sb15-0096].
5. **The doctor's shrug, or the doctor's push with no how.** The shrug: "toddlers will be toddlers, it's probably just a phase" [sb04-0141]; "They say it’s all normal, everything, normal" [sb07-0111]; "Dr says it’s just his temperament" [sb09-0053]; "So dismissive" [sb10-0251]; from specialists, a verdict that he is "just a hard baby" [sb08-0260]. The push with no method: "we need to phase out the comfort nursing. My question is: HOW??" [sb08-0169]. (Medical advice reported second-hand is restricted and never repeated as guidance, e.g. [sb08-0165] [sb11-0089] [sb11-0216] (restricted).)

The sharpest line in the set holds both contradictory answers in one breath: "Everyone is either ‘you can’t spoil a baby, she just wants mom it’s ok’ or ‘let her cry you set her up to only want you’." [sb15-0291]. Comparison is a theme of its own (`comparison_other_babies` 249 quotes; `social_media_pressure` 44): "Every post on Reddit is about good sleepers." [sb21-0337]; "Social media, such as Taking Cara Babies totally gaslights me" [sb17-0172].

**Readers disagreed on doctors.** Doctors who brush parents off or push them appear in R04, R05, R07–R11, R13 and R15–R20. R12 found no brush-off at all in its 70 units (`reader-notes-r12.md`). The pattern is real but not universal.

## 4. What they try, and how it lands

Counts: `tried_failed` 767 quotes, `failure_story` 309, `success_story` 357; themes `cry_it_out` 767, `ferber` 560, `gentle_method` 272, `chair_method` 109, `pick_up_put_down` 62, `sleep_consultant` 277, `course_purchase` 141, `app_tracking` 267.

### 4.1 Sleep consultants: the most common complaint is a plan that was not personal

- **The same plan for everyone.** "These are her standard wake windows she suggests for all clients." [sb01-0028]. A mother sending daily logs after filling in "a pretty extensive questionnaire" [sb05-0226]: "So far, the only thing she’s really changed is her wake windows." [sb05-0225]; "I don’t know if she gives the same general plan to everyone or if it’s actually personalized" [sb05-0226]. "She basically parroted what people say on here with a few tweaks" [sb01-0124].
- **Support that ends, or turns to blame, at the worst moment.** "the support is over because of that, and that I basically undid everything" [sb01-0111]; "said I can pay for an additional week of her services" [sb01-0029]; "basically abandoned us after three days" [sb13-0053]; "he probably is not sleep trainable so we cut our contract" [sb13-0054]; "I wanted to absolutely scream when she said that because I need help." [sb01-0139]; "she isnt available for my ongoing questions" [sb01-0093].
- **Free advice beats the consultant in the same thread.** "My sleep consultant was leaning towards shortening them and I’m so glad I listened to you all first." [sb05-0175]; "succumbed to hiring a sleep consultant but didn't expect to get such bad advice" [sb10-0143]; after five days of paid coaching [sb15-0132], a commenter was "kind of ridiculously right" [sb15-0136]. A father counts "15-20 sleep trainings" (in [sb05-0302]) and a trainer who "didn't even send us the invoice" [sb05-0301].
- **When it works, the consultant listened or used the family's own logs.** "I hired a different sleep consultant right away who listened to me about his tendencies" [sb13-0025]; "We tracked his sleep for a week and she calculated it based on that." [sb13-0192]; "something about getting a personalized schedule and the science behind baby sleep really helped" [sb02-0006]; "I didn’t have confidence that my random internet schedule would work so I never fully tried." [sb02-0007]. Other praise tends to be short-lived: "It was the best 2 weeks." [sb01-0306]; "A good week, back to 30-40 min go downs." [sb01-0201].
- **Readers disagreed.** R13 found consultants praised (the ones who listened, above). R17 and R18 found no quote praising a consultant in 257 units between them (`reader-notes-r17.md`, `reader-notes-r18.md`).

### 4.2 Courses and books (Taking Cara Babies is the name that comes up most)

- **The rules collide with the baby or with life.** One parent ran a course's night-weaning plan to the letter: "he cried for 2h SOLID!" [sb11-0069], then had "no idea how to continue the plan or timings of feeds now" [sb11-0070]. "I bought the taking Cara babies course on napping and it just doesn’t seem align with daycare at all." [sb18-0046]; "I have the taking cara babies 3/4 month course and have been trying to follow SETBACK but it really isn’t working." [sb18-0354]; "We use huckleberry , tried moms on call, and TCB and I just do not understand." [sb08-0054].
- **It worked for the first child and fails for the second.** Parents make the personalisation argument themselves: "taking Cara babies wake windows worked very well for her" [sb13-0156] (the first child); "I have two older kids that I did taking Cara babies with and they slept through the night." [sb17-0336]; "with high hopes since our oldest took to it really well" [sb13-0134].
- **Seen as generic:** "Even with Taking Cara Babies, it is essentially CIO with timed checks" [sb10-0045]; Precious Little Sleep "feels like CIO with more steps" [sb01-0128].
- **Contrary cases:** a consult added to a course was "really helpful" [sb13-0021]. A father given a neighbour's free copy of a TCB document [sb21-0050] wrote "We did the ABC of sleep and followed it to a tee." [sb21-0053], and it worked. One parent committed to Precious Little Sleep's fuss-it-out "for a full week rather than chopping and changing methods" [sb02-0116]. For another, the same method "was a complete failure" [sb15-0091].
- **Residential and hospital programmes:** after two sleep-school stays, "Once again, improvements until sickness/teething." [sb15-0086]; "We did a hospital stay at 3.5 months for sleep and settling etc but it was terrible" [sb19-0254]. These rest on a handful of quotes.

### 4.3 Apps and AI: a lifeline and a source of anxiety at once

- **Lifeline:** "Huckleberry is keeping me sane right now because I’m too tired to remember when I last did things" [sb01-0244]; "he gives me the notifications and I don’t have to do math" [sb01-0099]; "he almost always falls asleep exactly when the app predicts" [sb07-0131].
- **Anxiety and dependence:** "it involves being glued to my house and my phone. It's not sustainable." [sb01-0168]; stopping tracking "was a fucking disaster" [sb01-0169]; "the more exact the data is, the more anxious I get." [sb01-0282]; automatic tracking to the minute "is 100% toxic for me." [sb07-0068]; "I'm so scared to step away from the apps and tracking" [sb07-0210]; "Other days I lie awake at 3am staring at the app." [sb19-0212].
- **The app's plan is not personal either:** "We’ve paid huckleberry to make a sleep schedule but its all out the door" [sb13-0225]; the app's gentle training plan became "more physically and mentally exhausting than rocking her ever was." [sb20-0372]; "Huckleberry's Berry AI isn't very accurate." [sb16-0275]. A free tool went paid: "Looks like thats no longer free, need to upgrade to create a custom schedule" [sb16-0191]. After a commenter's free breakdown, one parent wrote "Proper chuckle on the subscription cancellation!" [sb19-0145].
- **AI chatbots: readers disagreed on how common.** They are present in R04, R06, R09, R10, R17, R20 and R21: "In my desperation, I consulted Chatgpt." [sb06-0330]; "ChatGPT tells me he’s overtired, so then I tried longer morning nap. That made it worse." [sb10-0177]; "Used it every day for about 9 months before I got fed up." [sb20-0350]; and a sleep trainer, ChatGPT and "everyone" giving three answers at once [sb21-0231]. They are absent in R11, R14, R15, R16 and R18, where Google stands in: "everything I Google says he would be overeating by a lot." [sb11-0065]. Each reader found only a handful of these quotes.

### 4.4 Free advice: it wins with exact numbers and fails when followed to the letter

- **It wins, often overnight, when a stranger does the maths for this baby:** "8 mins tonight! Mild fussing!" [sb17-0039]; "Extending the wake windows has changed everything." [sb17-0284]; "She slept through!" [sb21-0075] after counting from lights-out instead [sb21-0074]; "The specific rules you give are so much more actionable for me" [sb10-0133]. `free_advice_wins` 81 quotes.
- **It fails, as parents report in follow-ups:** "and then woke up 14 times more overnight" [sb10-0037]; "Tried this yesterday and had even more wake ups last night." [sb11-0106]; on the sub's schedule, "she’s miserable like 90% of the day every day." [sb12-0078]. One mother on two days: "she was asleep in 2 minutes!" [sb20-0309], then "it was the single worst night we have had since the 4 month regression" [sb20-0310]. `free_advice_fail` 38 quotes. R20 notes that nobody posted a follow-up a week later, so nobody knows which fixes lasted.
- **The undertired/overtired puzzle sits under all of it:** "if she is undertired she will scream forever and if she is overtired she will scream forever." [sb04-0097]; "Is my baby undertired or overtired or still adjusting?" [sb11-0007]; "It seems every wake window i try is wrong" [sb19-0036]. Opposite fixes worked for different babies: "Turns out he was overtired." [sb16-0259] versus "we were trying to make him sleep before he was truly tired" [sb16-0262]. `undertired_overtired` 53 quotes, plus other spellings. The standard reply has itself become a complaint: "More wake time, more wake time, more wake time." [sb19-0272]; "how much I appreciate any solution other than" more tiredness [sb08-0073].
- **What the maths costs them:** "I feel like I spend my entire day calculating wake windows" [sb16-0183]; "And honestly, I just want to stop doing math." [sb16-0186]; "it has become my entire identity almost." [sb17-0171].

### 4.5 Why attempts stop

- **The parent's limit, more often than the baby's:** "Lasted approximately 11 minutes before I started questioning all my life choices." [sb07-0164]; "like it legit hurts my chest" [sb06-0191]; "I mentally can't let my child cry another night" [sb10-0120].
- **Vomiting or gagging from crying.** "Within 5 minutes she would scream so hard she would make herself vomit." [sb03-0233]; "if he cries for too long after being put down in the crib (even just 20 seconds of crying), he gags and vomits." [sb08-0066] (a father); "We've resorted to rocking him to sleep because I can't clean up puke again" [sb11-0008]; "after the 3rd or 4th check she will start puking" [sb20-0054]. `vomiting_stop` 43 quotes, plus other spellings. **Readers disagreed on how often this happens:** R03 called it the most common named reason an attempt ended, while R06 found one instance in 122 units. Distress images of this kind are restricted for ads (e.g. [sb13-0145] [sb18-0207] [sb20-0279] (restricted)).
- **Check-ins escalate some babies.** Their parents go to full extinction, or the other way, to gentler methods: "he doesn’t calm down, he escalates." [sb09-0128]; "he does not have a Ferber temperament" [sb10-0238].
- **Walls and rooms.** Neighbours "have been banging on the wall because his crying wakes them up" [sb17-0350]; a hotel room booked so the baby could be trained there [sb15-0150]; "i literally bought our neighbor a starbucks gift card bc i feel so bad." [sb20-0208]; "for formal sleep training she needs to be on a separate bedroom and at the moment we only have one" [sb12-0163]; "it has really limited our sleep training options" [sb19-0107].

### 4.6 Buying one fix at a time

Sleepwear and gear become a money pit (interpretation, from R01, R05, R10, R11 and R13): "I feel like I keep wasting money playing around with different sleep sacks" [sb01-0014]; "bought the expensive woolino to solve this issue but" [sb05-0296]; "Spend over £150 on different types of sleeping bags" [sb15-0210]; a glider that was a "waste of $180" [sb13-0013]; a bedside crib "useful only to store things in it" [sb13-0081]; "I would normally never go for the SNOO but I’m so desperate for anything to work." [sb05-0284]. Section 8 has the money detail.

## 5. The other side of the door

### 5.1 Partners: the fight over method runs both ways

- **The father who wants to train and the mother who refuses.** "Tried showing her research but it was never something she'd entertain." [sb02-0174]; "Our pediatrician told us multiple times to do this and wife didn't want to." [sb02-0184]; "I've resorted to buying a couch for my shop and sleeping at work" [sb03-0003]; "Obviously she found out but she's been sleeping through the night and doesn't even mind I did it." [sb02-0177]; "She adamantly refused sleep training but I had finally decided we were at our limit." [sb13-0241].
- **The mother who wants to train and the father who cannot or will not.** "And I couldn't win him so we never sleep trained." [sb06-0181]; "I can't listen to her yell Dada from her crib through tears. I'm not strong enough" [sb06-0075] (a father). The roles can flip: a husband who first "suggested sleep training and I said a hard no" [sb20-0289] later became the one who could not go through with it: "My husband is now the one who says he can’t do it." [sb20-0291].
- **The fight itself:** "We fight daily about sleep training and it’s harming our relationship." [sb03-0285]; "I do not recommend having this conversation at 3am." [sb02-0143]; "I wanted to go in after 15 but my husband kept saying to give her more time." [sb11-0189]; "My husband thinks I’m partially to blame because I’ve never let her cry it out" [sb11-0266].
- **The fight over who carries the load is sharper than the fight over method** (R07, R08, R10): "He checks his phone for the time and rolls back over to go back asleep." [sb06-0319]; "I don’t want to have to manage him as well as the baby." [sb06-0320]; "he thinks the nights are my responsibility because he wakes up at 5am." [sb10-0229]; "My husband has of course suggested that I live a nocturnal life" [sb10-0140]; "I’m basically a single mom who’s married." [sb11-0185]; "My husband refuses to help because this is my job" [sb12-0136]. Some mothers take the nights by choice because of his job: he works "in a job where sleep deprivation could put both his own life and other people’s lives at risk" [sb17-0129]; "my husband has to be up for work at 4am he cannot do this." [sb21-0270].
- **Fathers write in the first person** (`partner` 263 quotes). On their own sleep: "the first ten months I got an average of 2,5 hours of sleep every night." [sb06-0052]. On work: "I am a literal zombie at work." [sb11-0255]. A father rejected at bedtime reads mom subs telling dads to "man up and push through" [sb18-0305] and writes "I’m afraid if I keep trying he’s going to associate me with bad times." [sb18-0307]. A father who shares the nights is told that is unusual: "Everyone else seems to have a setup where the wife does almost all night feeds" [sb14-0071]; "We are all a team or at least that’s how we view it" [sb14-0072]. Another writes "I’m mad at mom because she hasn’t figured this out" [sb12-0043] and "I also deeply empathize with her not being able to do it." [sb12-0044].

### 5.2 "Only mum can settle", and the reverse

`only_mum_settles` 133 quotes (plus other spellings). "husband is useless except for an occasional diaper change." [sb07-0203]; "he can’t settle because she only wants mom" [sb07-0182]. In a couple that splits childcare 50:50, the night-time rejection "is absolutely **brutal** for my partner" [sb09-0217]. The reverse is just as vivid. After a night away with his father, "HE SLEPT THROUGH THE NIGHT. IN A HOME HE DOESNT KNOW." [sb10-0196], and the mother asks "Why is it so easy for my husband and horribly hard for me????" [sb10-0197]. A father: "And I’m the only one that can effectively put her down." [sb12-0043]. A mother: "LO is 100x more intense for me than my husband." [sb15-0242].

### 5.3 Grandparents and relatives

`relative_caregiver_conflict` 88 quotes. A mother-in-law said the 8-month-old had told her she wanted to sleep, and napped her late [sb02-0221]; "My MIL actually came in and told me to" come and socialise at 11pm [sb02-0273]; "well we have people coming over just keep him up" [sb02-0276]; a grandmother said a newborn cannot have a schedule [sb14-0019], and "she continues to tell me that I’m making things too complicated." [sb14-0020]; "If I mention that she can’t leave lights on right outside the bedroom" [sb03-0057]; a grandmother gave the bottle "after I told her not to" [sb11-0119], and "That brought us back to square one." [sb11-0119]; "My MIL watches her during the day and often rocks her to sleep" [sb18-0338]. Grandparents also rescue: in R07 and R09 a grandmother can settle the baby when the parents cannot [sb09-0217].

### 5.4 Daycare: the place where naps "just work", or fall apart

`daycare_naps` 244 quotes, in two voices. Where it works: "they follow her wake windows and put her in a dark room with white noise" [sb02-0278]; "Daycare helped us establish a really good schedule for him." [sb02-0151]; "His daycare teachers say he’s the easiest one" [sb15-0189]; a switch to one nap "made everything so much better" [sb15-0269]. Where it breaks: "As soon as daycare started, sleep went to hell in a hand basket." [sb02-0105]; "4 months ago we started daycare and I truly think it’s ruined our lives." [sb12-0196]; "the daycare wouldn’t be adapting to her, she needs to adapt to them." [sb02-0260]; "I should pick her up at noon because she's disruptive" [sb03-0009]; "I’m paying for a full day’s worth of childcare." [sb14-0075]; "Unfortunately daycare won’t change nap policy" [sb19-0298]; one daycare's whole answer on how babies get to sleep [sb18-0047]. Readers disagreed on the "disruptive" call home: R03 and R14 found it, R18 found none.

### 5.5 Parents who refuse sleep training, and the content ones

- **Content:** "I breastfeed on demand, we cosleep, and we immediately respond to cries. And it's been working great for us" [sb04-0121]; "I don't plan on stopping because that works for our family" [sb04-0140]; "Sleep training wasn’t a good fit for our family" [sb06-0286]; "I truly don’t mind waking up 1-2 or even 3 times a night with my baby." [sb20-0193]; "I'm just not a zombie anymore." [sb02-0129].
- **Refusing while worn out:** "I’m not in favour of harsh sleep training methods but at the same time I just want him to sleep through the night." [sb04-0200]; "I never liked that method. I'd rather soothe my baby." [sb04-0032]. Loving and resenting contact naps in the same line: "I actually love the contact naps 90% of the time but I would also like to enjoy the outside world some days too." [sb07-0003].
- **People change their minds in both directions:** "I was always part of the 'it's abusive' crowd until now" [sb02-0200]; "I was sold on the idea that sleep training caused attachment issues." [sb13-0302]; and a mother who now thinks she was talked into the idea of independent sleep [sb21-0349]. Beliefs that training harmed a child are restricted as claims ([sb21-0377] [sb21-0378] [sb21-0379] (restricted)).
- **Strangers online:** the judgement can be extreme ([sb02-0166] (restricted)), and parents push back: "comes across patronizing on a new parent forum." [sb07-0147].

## 6. What they ask, want and fear

Counts: `question` 622 quotes, `desire` 265, `fear` 345; themes `personalization` 153, `which_method_fits` 54 (plus other spellings), `information_overload` 254, `conflicting_advice` 267.

### 6.1 The exact asks for a plan

They ask for a plan for this child, written as steps, with a rule for when things go wrong. In their words:

- **A plan, not tips:** "We just desperately need a plan that actually works." [sb06-0089]; "I just need a plan that has a reasonable chance of working because I cannot keep doing 12am–4am every single night." [sb09-0291]; "I just need a starting point, a realistic plan" [sb17-0354].
- **Steps a tired brain can follow:** someone to explain exactly what they did, in kindergarten language [sb10-0261]; "really need someone to explain sleep training to me like I’m 5" [sb10-0259]; "can you write step by step what you did bc I’m neurodivergent and get overwhelmed without a protocol" [sb08-0188]; "Could you please suggest a routine with time stamps for me?" [sb05-0313]; specific transitional and target schedules for a 7am wake [sb21-0286]; "Can you please tell me what version of Ferber are you doing? Time intervals and everything" [sb20-0366].
- **The order of attack:** "What do you tackle FIRST: bedtime, night wakings, or naps?" [sb17-0355]; "Would you work on the rocking association first, the overnight nursing first, or both together?" [sb17-0116].
- **What to do in the moment, and when it goes wrong:** "I'm not sure if I should pick her up, leave her, talk to her, touch her, how long for, when to give up" [sb17-0209]; "we really need a clear plan for what to do when things don’t go as expected." [sb19-0104]; "how long is too long for the crying during CIO? I can never find a straight answer for that." [sb19-0101]; "how long do i let it regress before sleeping training again? and how do i pick a program?" [sb17-0213].
- **Too tired to work it out:** "i’m just to exhausted and deprived to try and work it out myself anymore." [sb04-0115]; "I have read Precious Little Sleep but just can't figure out where to start with this situation." [sb05-0086].
- **A guideline, not a cage:** "that I use as a guideline, while equally knowing that she’s a baby not a robot." [sb05-0204].

### 6.2 "For a baby like mine": personalisation, asked for in so many words

"I am specifically looking for advice from someone who has a baby with a similar temperament/situation to mine." [sb04-0020]; "What method of sleep training have you found is best for this type of child?" [sb06-0135]; "No one ever encountered a baby like mine" [sb10-0267]; "Well I’m asking you for sleep advice and you’ve never met my kid" [sb10-0180]; "I’m hoping that I will read something that might resonate with my daughter’s temperament." [sb19-0087]; "I was looking for advice from parents that have navigated a similar situation." [sb15-0113]. Specific situations come up again and again. A reflux baby: "I feel like all the usual sleep training advice assumes your baby has predictable wake windows" [sb19-0252]. A single mother working from home [sb15-0105]. No room of the baby's own: "that's not an option in our current living situation." [sb21-0115]. No partner: "I’m not looking for advice that assumes I have someone else available to take over at night" [sb20-0234]. Twins with opposite results [sb09-0128]. Second children who break the first child's method [sb18-0148] [sb16-0044] [sb20-0270]. And the cause matters to the method: "I’m not going to do a CIO method if this is driven by separation anxiety." [sb11-0290].

**Low sleep needs** (`low_sleep_needs` 74 quotes) is the label parents reach for when a schedule fails, and strangers both apply it and take it back: "She's a pretty happy baby though generally so I think she's just low sleep needs." [sb05-0294]; "I guess my friends all have high sleep needs kids" [sb07-0070]; and the reversal, "Oo then he is not low sleep need." [sb05-0279].

### 6.3 Posts that rule out the usual answers in advance

This is a post genre of its own (R14–R21): "Pls don’t mention sleep training, I don’t have it in me." [sb06-0080]; "Please use kind words and don’t bully me." [sb06-0131]; "I too need sleep and I do NOT want to keep cosleeping." [sb09-0141]; "Please do not make any recommendations involving CIO sleep training." [sb14-0176]; "I’m not looking for any tips on sleep / telling me to sleep train." [sb09-0005]. Interpretation: they have already heard the standard advice and want to be met where they are.

### 6.4 Fears

- **Hurting the bond by letting the baby cry:** "I feel like I’m torturing him by not comforting him as soon as he cries." [sb07-0078]; "I never thought I’d let my baby cry and am ashamed to tell anyone" [sb07-0048]; "am I teaching her I’m not coming to save you?" [sb13-0141]. `guilt` 654 quotes.
- **That nothing will work for this baby:** "What are signs that sleep training won't work for him?" [sb10-0046]; "Are there babies that can’t be sleeptrained" [sb10-0266]; "I just don’t want to put him through this unless I KNOW he’s on a correct schedule" [sb19-0274].
- **That it will have to be done again:** "have to do it all over again in a few months in case he has another regression." [sb10-0027]; "I really don’t think I can go home and retrain for that long." [sb12-0081]; "I’m afraid it’s going to take at least a good week if not more of insane crying" [sb06-0134].
- **That the window has closed:** "I’m afraid that we missed the window on sleep training" [sb05-0181]; "I don’t wanna waste my time trying to sleep train again if I already confused him." [sb05-0140].
- **For themselves:** "I’m scared it will traumatize me." [sb11-0272]; "I feel like I need to fully be at my breaking point to earn sleep training" [sb13-0049]. Fears for the baby's safety in the night and about the parent's own mental state are present but restricted (e.g. [sb04-0152] [sb11-0054] [sb10-0231] (restricted)).

## 7. What everyone else is telling them (advice they have already heard)

By the time they post, they have heard (interpretation, from the quotes cited): extend the wake windows [sb19-0272]; drowsy but awake (mocked in R16 and R20); go with the flow [sb04-0025]; wait out the regression [sb05-0213]; the first two or three days are hard [sb16-0099]; Ferber works in three nights [sb11-0264]; sleep when the baby sleeps (mocked in R07). They have read the books and the wiki: "I have read Precious Little Sleep" [sb05-0086]; "I feel like I’ve followed all the sleep advice and methods and nothing actually sticks with this baby." [sb12-0193]; "but 7mo baby still waking three times nightly" [sb18-0123]; "Wake windows are perfect. Naps are perfect. Bedtime routine is perfect. but still waking every 2 hours." [sb17-0225]. The advice contradicts itself: "My head is just spinning from all the differing information I’m getting online." [sb06-0068]; "everyone preaches wake windows as gospel when they aren’t mentioned by actual health authorities!" [sb06-0149]; "they all want me to buy their online course!" [sb21-0135]. And they meet success stories they cannot match: "I feel like I've read countless stories about the first few nights being the hardest" [sb04-0093]; "all success stories I see online say, that kids start sleeping for extra long stretches starting from the first night" [sb21-0153].

## 8. Money

> **Corrected 2026-10-25 by section 15:** the Reddit corpus has no refund quotes and no priced digital plan, but the book and app reviews do — refund and cancellation complaints and stated prices (£60 for pre-written schedules, $150 a year for a nap-timing feature). Read section 15 with this section.

Counts: `purchase` 149 quotes, `price_signal` 94; themes `price_value` 170, `course_purchase` 141, `sleep_consultant` 277. **Stated amounts are rare. By the regex in the appendix, 26 of the 6,659 quotes contain a currency amount, and several of those have nothing to do with sleep.** The table below lists every stated amount that is about sleep.

### 8.1 Every stated amount

| what | amount, in their words |
|---|---|
| Consultant, individualised plan | "$550 for 1 week of an individualized plan and 24/7 communication and $850 for a 2 week plan" [sb07-0135] |
| Consultant, two months | "I paid 1k for one for two months LOL he was trained a few weeks then reverted back" [sb08-0160] |
| Consultant, personalised plan | "the cost was close to $1,000.00. I decided to break the sleep to feed habit myself." [sb13-0064] |
| In-home programme | "One program I saw charges $1,000 for 2 weeks of hardcore sleep help" [sb13-0170] |
| Programme found through an ad | "3 tiers ranging from $2,000-$4,000" [sb18-0242] |
| Consultants, in total | "We’ve spent thousands of dollars on sleep consultants who haven’t been able to help" [sb01-0239] |
| 1:1 guidance seen in Facebook reels | "it's hundreds of dollars and we can't afford it. I'm desperate." [sb15-0200] |
| Wish-list ceiling | "Anyone have a sleep consultant they recommend under $500?" [sb13-0061] |
| Tracking app subscription | "$6.99/mo for existing users or $69.99 for lifetime membership" [sb01-0215] |
| Monitor membership | "I can’t come to the idea of paying another 120$ membership per year for an already expensive camera" [sb13-0128] |
| Book / video | "HBBOTB cost me $6. Definitely worth seeing if it makes a difference for $6" [sb01-0090] |
| Sleepwear | "at almost $100 I'm leery if it's not worth the hype." [sb01-0148] |
| Sleepwear | "So guess I’ll be biting the $109 bullet" [sb01-0221] |
| Sleepwear | "it's $55+ here and the reviews are mixed" [sb01-0161] |
| Sleepwear | "you might be able to get one for around $57!" [sb13-0165] |
| Sleepwear, in total | "Spend over £150 on different types of sleeping bags" [sb15-0210] |
| Smart bassinet, second-hand | "I can get a second hand snoo £450-500." [sb13-0112] |
| Smart bassinet, rental | "renting is looking about £125/m for my location" [sb13-0115] |
| Smart bassinet, second-hand | "mine was less than $400 in great condition" [sb01-0228] |
| Glider | "waste of $180, only works 20% of the time" [sb13-0013] |
| Hotel suite to keep a toddler's bedtime | "was about $200 more per night" [sb07-0276] |
| Bed frame | "for only $40 that we got for her nursery" [sb19-0232] |

**No parent in the corpus states a price for a course, a book bundle or a digital plan, and no quote describes a refund or a money-back claim** (searches in the appendix). Readers R05, R09, R10, R11, R12, R14, R16, R17, R19, R20 and R21 each report no price for sleep help anywhere in their slices. Interpretation: this corpus neither accepts nor refuses the $17.95–$49.95 band; nobody talks about it at all. That is a gap in the evidence, not a sign of acceptance.

### 8.2 What they say help is worth, and what they call a waste or a scam

- **Worth it:** "Yes it was worth it." for a personalised schedule [sb02-0006]; "there is no price I would not have paid in that first year for more sleep" [sb13-0112]; "I would rather pay for childcare than do 6 months of this type of sleep." [sb07-0030]; "We’re on a budget but I’m willing to pay at this point bc this is unbearable." [sb13-0228].
- **Afraid it won't be worth it:** "I know it’s a lot of money and don’t know if it will be worth it." [sb01-0066]; "I don’t want to pay a ton just to basically hear that she’s just not a good sleeper" [sb07-0307]; "i worry they will just tell me everything that i already know and offer no meaningful help" [sb10-0058]; "they’re expensive and no guarantee it will work." [sb13-0202]; "not sure I want to waste money on information I already know" [sb17-0337]; "this isn’t something we can financially do right now, especially if it ends up not working." [sb14-0128]; "I have the money to spend, just feel so stupid spending it on this." [sb07-0135].
- **Can't afford it:** "I can’t afford a sleep consultant" [sb10-0132]; "Idk if I can afford a sleep consultant but I wish I could because I just need some help." [sb01-0043]; "I wish I could afford something like that" [sb21-0007]; "I can’t spend another cent on another sleep consultant.. the first one was extortionate" [sb14-0137].
- **Scam and predatory:** "Are all these paid programs a scam? Is there any that actually work?" [sb13-0170]; "This is real or a scam?" [sb01-0165], about a programme whose reviews looked too good; "They are trying to take as much money from exhausted parents as possible." [sb18-0241]; "it just felt extremely predatory." [sb18-0242] (that programme's guarantee claim is restricted, [sb18-0240] (restricted)); "preying on the exhaustion and desperation of new parents to sell them overpriced PDFs and courses." [sb02-0235]; "All these companies are money hungry monsters." [sb01-0219], about a tracker going paid; "I really don’t want to pay money to track sleep and feeds." [sb01-0222].
- **Sharing instead of buying:** asking for a photo of the next Moms on Call schedule because "I’m not sure it’s worth the full price." [sb11-0037]; a neighbour's TCB document [sb21-0050]; a friend's consultant plan reused (R18).
- **Who paid:** a health plan, "covered under extended health benefits" [sb01-0058].
- **Ads follow them:** "all I see is ads for sleep programs" [sb13-0168].
- **Buying at night: readers disagreed.** R01 found course purchases described as panic buys: "I panic bought in the middle of the night" [sb01-0055]; "so my husband panic bought Taking Cara Babies" [sb01-0075]. R05, R07, R08 and R09 found no night-time course purchase. R14 found one product bought from a Facebook ad during a 1:45am feed and later regretted [sb14-0204] [sb14-0205]. This is a small, real pattern that rests on a handful of quotes.

### 8.3 Against what competitors charge (`competitors/README.md`)

| offer | price observed | note |
|---|---|---|
| Calmer Nights (UK) | £9.99, refund if not useful | questionnaire → AI 7-day plan; the closest analogue |
| BedtimeCoach | $19; $4.99/month support | questionnaire → printable plan; no ads |
| Wannabe Diary | $27 course; $37 tool | two answers select a pre-written plan |
| Baby Sleep Miracle (ClickBank) | $37 | VSL guide |
| Let's Sleep | AUD 37 + $15 PDF bump | the top single advertiser (50 active ads); no refund |
| Taking Cara Babies | US$39 eBook; $79–$99 newborn; $129–$249 5–24 months; $199 toddler | 96 active ads; refunds |
| Moms on Call | $32.99 books; $99 course | |
| Just Chill (UK) | £49 (£39 with code) | age-band courses |
| Dawnly | $67 | assessment → 14-day PDF; no ads |
| Betteroo | "from $1/day", tiers not seen | quiz → adapting app plan + human chat; 30-day money-back; 39 active ads |
| Huckleberry | $5.74 / $9.99 a month, billed yearly | app |
| Napper | US$69.99/year | app |
| Precious Little Sleep | $23/month; $285 / $695 consults | |
| Consultants | $150 per 30 min (DG); £98/h (Sleep Nanny); €525 (3 weeks); $750 (two weeks); up to $5,997 | |

Interpretation: the consultant prices parents state ($550 to $4,000: [sb07-0135] [sb08-0160] [sb13-0064] [sb18-0242]) match the sellers' own anchors, and Betteroo already anchors against the "$500–2,000 that sleep consultants typically charge" (`competitors/betteroo.md`). Mamivio's $17.95 / $29.95 / $49.95 ladder sits between the AI plan (£9.99) and the courses ($79–$249), well below any consultant. The parents here pay most readily for a person who adapts the plan to their logs, and complain most about paying for the plan everyone else gets (section 4.1).

## 9. Segments that sound different

### 9.1 The exhausted parent as the buyer ("get yourself back", the Betteroo angle)

Betteroo's quiz spends about a third of its questions on the mother's own state, and its promise is "get yourself back" (`competitors/betteroo.md`). The corpus supports the idea that the parent's own life is what they are trying to rescue (`maternal_exhaustion` 808 quotes; `parent_work_impact` 176; `resentment` 109; `marriage_strain` 75; `parent_identity` 72; `parent_body` 71; `parent_mental_health` 61, mostly restricted). What they say, by area:

**Their own sleep.** They count their own hours the way they count the baby's: "I only get any actual sleep between 9pm-12am ish so those are the golden hours" [sb09-0050]; "I haven’t had a decent nights sleep since I was around 3 months pregnant" [sb18-0369]; "it's almost been a year and I haven't had a single full nights rest since" [sb06-0179]; "not having slept one night thru solid in 4 years" [sb02-0211]. The body stays on alert after the baby improves: "My body still naturally wakes up every hour" [sb02-0092]; "my brain is so wired for waking constantly that I can’t sleep anymore." [sb20-0137]; "Even on the rare occasion where he sleeps 4+ hour stretches i usually wake up with anxiety anticipating his next wake." [sb04-0113]; "most nights I'm awake for 3-4hrs in the middle of the night. Then have to go to work the next day." [sb04-0143]; "And now I'M overtired and cant sleep when she finally does" [sb21-0348]; "I can’t sleep deeply because I’m on high alert waiting for him to wake up." [sb09-0136]; "as 7pm draws closer I feel my anxiety go through the roof." [sb08-0137]. (Interpretation: this overlaps the sleep-mother niche. A baby-sleep plan alone may not fix the parent's own sleep, and [sb02-0092] says so outright.)

**Their body.** "I have 24/7 sleep deprivation headaches. I’m constantly nauseous and spacey." [sb03-0102]; "my hair is falling out in handfuls, I’m gaining weight." [sb03-0167]; "My back, shoulders, wrists and hands all hurt so much because I can barely put baby down." [sb05-0115]; "I currently have carpal tunnel in both wrists" [sb02-0239]; "holding her for 12+ hours a day has taken its toll!" [sb07-0124]; "I can feel the wear on my joints" [sb07-0320]; "like years are just falling off my life." [sb07-0143]; "I’m so sleep deprived that i always feel like fainting." [sb06-0145]; "I am so tired I can feel my body starting to give up." [sb05-0056]. Restricted quotes also tie weight and health to sleep loss ([sb09-0052] [sb21-0058] [sb18-0113] (restricted)).

**Who they are.** "I love my baby so much but I feel like a shell of a person." [sb03-0167]; "I feel like a completely different person with 0 sleep." [sb03-0180]; "I am a shell of a person. I walk around half dead" [sb08-0275]; "And I feel like I’m disappearing." [sb08-0153]; "I thought I would be better at this. I didn’t expect sleep to consume me the way it has." [sb06-0032]; "I miss my old life where I slept." [sb04-0252]; "I am a sleeper, I love sleep" [sb06-0333]; "I feel like the worst version of myself." [sb09-0119]; "I’m not living." [sb21-0367]; "I have about three brain cells left, and two of them are crying." [sb21-0364]; "She’s doing so great! But i’m not" [sb20-0269]. A mother who is a sleep coach for adults: "so it’s a very cruel joke" [sb10-0090].

**Who they are as a parent.** They feel the exhaustion as the loss of the good parts of parenting: "the sleep deprivation is stealing happier experiences between me and my baby." [sb04-0111]; "I can not be the mother my baby needs" [sb10-0228]; "I feel like it’s impacting my ability to show up as a mother for her too" [sb12-0022]; "I’m just so, so tired to even play with her." [sb12-0161]; "I feel like her childhood is passing me by because of how tired I always am" [sb08-0092]; "neither of our children (or each other) are getting great versions of us." [sb04-0310]. Some train for this reason: "So I’m sleep training to better my mental health" [sb06-0290]; "we need her to sleep so we can all sleep and I can be a better mom." [sb12-0187]. Anger and resentment are present ("and so much resentment" [sb12-0144]); the sharper anger quotes are restricted ([sb07-0173] [sb18-0001] [sb18-0157] (restricted)).

**The marriage.** "I miss my baby and I miss my husband." [sb03-0102]; "im just exhausted and miss my husband" [sb03-0022]; "Our marriage has become a transaction of passing the baby back and forth with blood-shot eyes" [sb08-0261]; "We’re at each other’s throats in the middle of the night because we’re so tired." [sb07-0197]; "meaning we don't even sleep in the same bed anymore." [sb07-0006]; "we basically haven’t shared a bed in three years" [sb03-0063] (a father); "If my son keeps waking us like this our marriage will continue to suffer." [sb06-0288]; "It’s ruining my marriage, my career, obviously my mental health." [sb12-0131]; "I feel such rage at my husband who peacefully sleeps next to me." [sb17-0324]; "He gets to come and go as he pleases he can shit in peace" [sb19-0159]; "the last time we got to partake in grown up activities in our OWN bed" [sb19-0234]; "I feel like I haven't seen her in a week." [sb06-0272] (a father). Plans for more children: "Honestly we've sworn off another kid ONLY because of the sleep." [sb02-0178]; "it’s also making me question if I can have more children" [sb12-0145]; "another baby is certainly not in the cards" [sb09-0139].

**Work.** "I’m getting maybe four hours of broken sleep before shifts." [sb03-0103]; "I work full time and my work is suffering severely." [sb05-0056]; "I get to go teach kindergarten on 4 hours of sleep for probably the 37th day in a row." [sb17-0066], with a plan to nap "on the yucky rug in my classroom" [sb17-0068]; "waking up 5 times a night has become entirely unsustainable." [sb12-0053]; "I even started a new job and then got fired bc the second day of daycare he got rsv." [sb17-0363]; "I keep making small mistakes I would never have made before." [sb09-0119]; "Can I get signed off by a doctor for 'too tired to function'?" [sb09-0215]. Fathers: "But sometimes I can only give my full 70 percent at work" [sb04-0279]; "I had to take a step back at work." [sb06-0046]; "I'm tired and need to keep my job." [sb05-0300]. Some see going back to work as relief: "work would feel like a break at this point" [sb04-0307]; "I am going back to work soon because I am exhausted at home." [sb17-0089]. For others the return to work is the deadline: "I go back to work in a few weeks and im panicking bad." [sb10-0202]. Exhaustion as a danger on the road or at work is restricted ([sb07-0224] [sb12-0186] [sb10-0255] [sb18-0210] (restricted)).

**Time back, in their words (what "getting yourself back" means to them).** It is modest: "I just want a little bit of my evening back." [sb11-0192]; "all i want is the extra 2 hours at night to decompress." [sb07-0215]; "a momma who just wants an hour to an 1 1/2 hrs of alone time at the end of the day" [sb03-0220]; "I want my bed back, I want my baby to sleep safely, I want to be free while she naps." [sb03-0295]; "that tiny little window where I can just sit down and breathe." [sb11-0053]; the autumn candle she never gets to enjoy [sb11-0158]; "Haven’t left the house in almost 5 months" [sb19-0253]; "I really want my life back. I want to get a solid 7 hours of sleep." [sb04-0098]. And this is how relief sounds when it comes: "Even just these first few nights of better sleep have made me feel like a new person." [sb14-0008]; "I feel like a different person from getting a longer stretch of sleep." [sb11-0004]; "my husband and I finally had a few hours together at night" [sb03-0020]; "My husband and I truly didn't know what to do with all that free time." [sb03-0293]; "We have our room back, don’t have to tip toe around" [sb13-0315]; "being able to sit down and have dinner with my wife at night" [sb13-0248] (a father).

**Guilt for wanting it.** "I know it sounds selfish but my personal time is at an absolute 0." [sb07-0215]; "To be fair, we do have support, which only makes me feel guilty for drowning." [sb07-0007]; "selfishly I am so tired." [sb07-0063].

Interpretation for this segment: the evidence supports leading with the parent's own state (body, marriage, evenings, work) as the reason to act, and it gives the exact scale of what they want: an evening, a bed, 20 minutes. It does not support promising that the parent's own sleep will come back when the baby's does; [sb02-0092] [sb20-0137] [sb04-0113] say it may not. Mental-health content sits close to this angle, and much of it is restricted.

### 9.2 Fathers

Fathers (`partner`, 263 quotes) write success stories as process reports with numbers [sb13-0248]. They frame the pain through the wife: "that is killing my wife waking up 6-8 time a night sometimes more." [sb13-0195]. They describe their own sleep and work [sb06-0052] [sb11-0255], they are hurt by what mom forums tell them [sb18-0305], and several trained alone against the mother's wishes [sb02-0177] [sb13-0241]. Interpretation: a plan a father can follow on his own speaks to them. R14 reports a husband who does better with very clear instructions, and R18 counted 16 father quotes in its core chunks.

### 9.3 Parents of a second child

The first child set the bar: "since my first baby was a trick baby and such a good sleeper." [sb20-0270]; "I have already sleep trained a baby before and it was absolutely nothing like this." [sb20-0256]; "but this time around I have no idea what im doing wrong!" [sb18-0148]; "I expected something similar with my 2nd one." [sb16-0044]. They know the methods. What failed is the fit.

### 9.4 Toddler parents (12–36 months)

They describe bedtime battles, climbing out of the cot, a parent stuck in the room, and crying methods that feel wrong at this age [sb09-0082] [sb20-0248] (`toddler_12_24_months` 1,157 quotes, `toddler_24_36_months` 556). Fewer methods are written for them: "the information online doesn't apply to us/him." [sb17-0261]; "none of them seem to fit our girls personality" [sb09-0092].

### 9.5 Responsive and cosleeping parents

They want a middle ground (R14), longer stretches without training, or nothing fixed at all [sb04-0121] [sb20-0193]. A product framed as fixing sleep will not speak to the content ones (R03). The tired but committed ones ask for gentle steps [sb08-0188] [sb04-0200].

### 9.6 Constrained households

These are single parents [sb20-0234] [sb06-0080], families in one-bedroom flats or behind thin walls [sb12-0163] [sb19-0107], shift workers [sb06-0145], and families whose naps daycare decides [sb18-0046]. Their posts open by ruling out the standard advice, which assumes space, a partner or control of the schedule [sb21-0115].

### 9.7 UK and Australia

r/beyondthebumpUK gave 237 quotes. UK words (cot, dummy, health visitor, nursery, Next to Me) and residential sleep school (Tresillian; two sleep-school stays in [sb15-0086]) show up. The corpus is not tagged by country, so this was not analysed further (interpretation).

## 10. Does the evidence support the Mamivio product?

The candidate product: a quiz on the baby's age, wakings, feeding, where the baby sleeps and the parent's values on crying → a personalised plan → a day-by-day programme, at $17.95 / $29.95 / $49.95 for 1 / 3 / 6 months.

### For

- **They ask for exactly this shape:** a plan, steps, time stamps and the order to tackle things, for their child (sections 6.1–6.2) [sb06-0089] [sb10-0261] [sb17-0355] [sb04-0020] [sb05-0034].
- **A personal plan is what got a full trial.** "I didn’t have confidence that my random internet schedule would work so I never fully tried. Once I got her sleep plan it felt like all pieces came together." [sb02-0007]; "that there was a chance it could work for me to feel confident enough to stick it out" [sb02-0005]; "The specific rules you give are so much more actionable for me" [sb10-0133].
- **The most common complaint about paid help is an opening for a better plan:** the same schedule for every client [sb01-0028] [sb05-0226], and parents who want to be told what to do: "I think my husband and I just need a coach to follow there instructions" [sb13-0062].
- **Price:** consultants at $550 to $4,000 are out of reach or distrusted [sb15-0200] [sb13-0064] [sb18-0242]. One parent did it herself rather than pay close to $1,000 for a personalised plan [sb13-0064]. A low price partly removes the "afraid it won't work" barrier [sb14-0128] (interpretation).
- **A day-by-day programme matches how they already talk:** night logs, night 3 named as the turn, and sticking to one method for a fixed stretch [sb02-0116].
- **The parent's values on crying belong in the quiz.** Whether they will use a crying method is the most loaded question in the corpus [sb04-0200] [sb04-0032] [sb08-0154], and parents state their limit before asking for any advice [sb14-0176] [sb08-0188].
- **So does the parent's own state** (section 9.1).

### Against

- **Free advice already delivers exact numbers, overnight, for nothing** [sb17-0039] [sb21-0075] [sb05-0175] (`free_advice_wins` 81 quotes). A paid plan has to be better than r/sleeptrain's commenters, not just tidier.
- **Scepticism of the format and of the industry:** "overpriced PDFs and courses." [sb02-0235]; "Many voices online sell the illusion that if you just adopt their Ten Step Plan" [sb02-0034]; "I am also skeptical of the sleep training industry/influencers" [sb02-0164]; "not sure I want to waste money on information I already know" [sb17-0337]. Betteroo, with 39 active ads, already defines itself against "a PDF you'll never open" and against generic PDFs with the baby's name inserted (`competitors/betteroo.md`). A static plan advertised next to it will be read through that frame (interpretation).
- **A one-shot plan goes stale.** Retraining after a setback is the most common arc (`retraining_after_setback` 264 quotes) [sb05-0129] [sb08-0109] [sb10-0027]. The 1/3/6-month tiers only make sense if the plan changes with setbacks, ages and nap transitions.
- **Age alone is not enough.** The same symptom has opposite fixes [sb16-0259] [sb16-0262], and "It seems every wake window i try is wrong" [sb19-0036]. A plan that ignores the baby's actual sleep repeats the consultants' failure [sb13-0225] [sb01-0028].
- **Plans fail on night one** at the parent's limit or when the baby vomits [sb07-0164] [sb11-0008] [sb20-0054], or because of walls and a shared room [sb12-0163]. A plan without branches for these cases will be abandoned (interpretation).
- **Some parents want company, not a plan** [sb09-0005] [sb01-0123]. Content cosleepers want nothing fixed [sb04-0121].
- **No parent names a price for a document or course**, so there is no evidence about the $17.95–$49.95 band itself (section 8.1).
- **The format is cheap to copy.** Calmer Nights sells the same shape for £9.99 with a refund (`competitors/calmer-nights.md`).

### What it must do to be believed (from the complaints; interpretation)

1. **Show that the answers changed the plan.** Ask for the baby's real day (wake time, nap lengths, wakings, how the baby falls asleep), not only the age, and show which answer changed which part. The complaint about consultants is exactly that this did not happen [sb05-0225] [sb05-0226].
2. **Give the steps in plain language with times:** the order to tackle things, and what to do minute by minute at a waking [sb10-0261] [sb17-0209] [sb05-0313].
3. **Branch on the hard cases:** check-ins that escalate, a baby who vomits, a parent who cannot take the crying, no separate room, no partner, naps set by daycare [sb09-0128] [sb20-0054] [sb12-0163] [sb20-0234] [sb18-0046].
4. **Plan for the setback before it happens:** illness, teeth, travel, nap transitions, and how to restart [sb17-0213] [sb19-0104].
5. **Match the method to the parent's stated values**, without making claims either way about crying [sb04-0200] [sb08-0188].
6. **Speak to the parent's own state** without promising to fix it (section 9.1).
7. **Never promise a timeline or a result.** "I feel so duped by all of the success stories." [sb19-0256]. A programme that guaranteed results was called predatory [sb18-0241] [sb18-0242]. The README forbids such promises anyway.
8. **Be usable by the other caregiver:** the father doing night one [sb02-0177], the grandparent who undoes the schedule [sb11-0119].

## 11. Objections to expect

- **"It's just the same advice I've already read."** [sb10-0058] [sb17-0337] [sb01-0124]
- **"Generic plans don't fit my baby."** [sb10-0180] [sb10-0267] [sb19-0252]
- **"It's cry-it-out in disguise."** "I feel ferber is low key CIO in disguise" [sb05-0278]; [sb10-0045]; "it feels like CIO with more steps." [sb01-0128]
- **"It won't work for my baby; my baby can't be trained."** [sb10-0266] [sb10-0046] [sb13-0054]
- **"It will undo itself at the next regression."** [sb10-0027] [sb05-0216]
- **"Is it a scam?"** [sb13-0170] [sb01-0165] [sb18-0241]
- **"I can't afford it, not if it might not work."** [sb14-0128] [sb15-0200] [sb13-0202]
- **"I don't want to track more."** [sb01-0282] [sb07-0068]
- **"Don't tell me to sleep train."** [sb06-0080] [sb09-0005] [sb14-0176]
- **"My partner won't do it."** [sb06-0181] [sb20-0291]
- **"We have no room, or thin walls."** [sb12-0163] [sb19-0107]
- **"Is it too late?"** [sb06-0104] [sb05-0181]

## 12. Lines not to cross

`counts.md` lists 159 quotes flagged restricted in the merged file, and `restricted-ids.md` names 5 more from the orchestrator's sweep (sb02-0166, sb04-0067, sb06-0025, sb06-0228, sb07-0130): 164 in all. `counts.md` also records 29 safety-regex hits inspected by hand, 26 of them not on the restricted list. The counts by category below are my own hand classification of the 164 ids, using the reasons in `restricted-ids.md` and the reader-notes tables (script in the appendix). Each id is counted once.

| category | ids | why excluded |
|---|---:|---|
| Safe sleep (unsafe sleep scenes, bedsharing out of exhaustion, dozing while holding the baby, infant-death fears, safe-sleep products) | 42 | README: safe-sleep statements only from AAP / NHS / Red Nose; never an ad scene |
| Parent mental health (depressive or crisis wording, panic, PPD/PPA, "can't live like this") | 42 | mental-health content; research only |
| Doctor or professional advice reported second-hand; medication; infant medical history | 29 | never repeated as guidance; medical causes are noted, never diagnosed |
| Beliefs that crying, or training, harms the child | 11 | README: no claims either way about crying |
| Exhaustion as a danger (driving, "can't safely carry on") | 7 | road and safety incidents |
| Distress images (vomiting from crying, a lost voice, an ER visit) | 6 | never in ads |
| Parent anger or harshness toward a child | 4 | never an ad scene |
| Reader lists with mixed reasons (R09: unsafe sleep, dreams, mental health; R15: bedsharing, "nervous system is shot") | 13 | safe-sleep or mental-health caution |
| Other (strangers saying the child should be taken, fear of police, a custody threat, a programme's guarantee claim, sleepwear brand switches, ids the orchestrator restricted after the reader had left them usable) | 10 | case by case |

Other lines held by rule: no infant-sleep guarantees, timelines or success rates (the night-3 turns in section 2 are what parents report, not a claim); minors are never quoted as customers; usernames are never recorded. Readers also excluded whole units for safety without quoting them (e.g. an infant breathing emergency while cosleeping, T5; a vomiting-plus-breathing scare, R21).

## 13. What's missing

- **Reddit tier A outside wave 1:** 11,102 posts from 2026-04-01 to 2026-08-24, unread; ids in `_raw/reddit/filter-v1/wave1/unread-rest.jsonl` (`sources/reddit.md`). Wave 2 would cover 2026-06-25 → 08-24.
- **Reddit tiers B and C:** 27,352 and 7,324 posts on disk, unread; 1,641 safety-flagged posts not yet triaged (`sources/reddit.md`).
- **Triage drops never read:** about 30 postpartum and burnout vents where baby sleep is a passing mention (T2), candidates for the sleep-mother niche (`reader-notes-triage.md`).
- **Sources not harvestable, or not tried** (`sources/not-harvested.md`): Goodreads, Amazon reviews, BabyCenter, What to Expect, BabyandBump, Mothering, Mumsnet, Netmums, HealthUnlocked, YouTube search and comments, Facebook groups, TikTok and Instagram comments, Discord. The owner was asked for Facebook group access and has not given it.
- **Empty folders:** `books/`, `_raw/books/`, `_raw/reviews/` (no app-store reviews of Huckleberry, Napper, Nara or Betteroo), `_raw/youtube/`, `ads-running/` (no niche-level Ad Library write-up beyond the main sweep), `_raw/owner/` (no owner data; `sources/owner-data.md`).
- **Browser walks pending** (`sources/competitors-not-harvested.md`, `reader-notes-market.md`): the Betteroo quiz and paywall tiers (quiz.betteroo.ai / .co), the Good Inside checkout price, Calmer Nights questionnaire pages 2–13 and a sample plan, Just Chill and Happy Sleep (403), the Sleep Nanny main site (403), jessiemartin.teachable.com, a Gumroad custom plan, Etsy printables (403).
- **Ad Library searches not yet run** (`reader-notes-market.md`, spend-footprint caveats): Calmer Nights, Actually Sleeping, Nara Baby, Sleep Wave / Happy Sleeper, Happy Little Sleeper, Possums Sleep, Sleepy Stars, Moms on Call; plus the phrases "baby schedule" and "newborn course", and non-English phrases.
- **Competitors found but not torn down** (`competitors/README.md`): Lullaby Academy, Sleep Retreat / Mama Sleep Club, Pocket Sleep Doc (its onboarding quiz includes the mother's sleep), the Happy Baby app, Susie Menkes, The Snooze Nurse, Asleep in 12, Tinyhood, Dorothy Waide, Heidi Holvoet; and the programmes parents named: Actually Sleeping, Nara Baby, Sleep Wave, Happy Little Sleeper, Possums, Sleepy Stars.
- **Not done in synthesis:** a quote index / language bank (`synthesis/quote-index.md`), a success-stories table, and a country split. No thread was followed beyond its end, so how long free or paid fixes lasted is unknown (R20).

---

## Appendix: counts I made myself

All commands run from `mamivio.com/research/sleep-baby/`. Helper: `scratchpad/FINDINGS/q.py`, which reads `voice-merged/all.jsonl`. Its restricted set is the merged `restricted` flag plus every id in the table cells of `synthesis/restricted-ids.md`.

1. **Quotes with a currency amount (26):** `python3 -I scratchpad/FINDINGS/q.py grep '[$£€]\s?\d|\d\s?(k|K)\b|\d+\s?(dollars|pounds|euros|bucks)|thousands? of dollars|hundreds of dollars' --n 200 | grep -c '^\['` → 26 (output in `scratchpad/FINDINGS/money.txt`). Not all 26 are about sleep (e.g. a $30k kitchen, body weight in pounds). Amounts written like "120$" and "£150", which this pattern missed, were found with the pattern `'\d\s?\$|\d\s?(€|£)|£|€'`.
2. **Refund or money-back quotes (0):** `python3 -I scratchpad/FINDINGS/q.py grep 'refund|money back|money-back' --n 30` → no records.
3. **Course prices named by a parent (0):** I read the 26 records from item 1 by hand. None prices a course, book bundle or digital plan. The only programme prices are for consultants and in-home or ad-found programmes; the only book or video price is $6 for Happiest Baby on the Block [sb01-0090].
4. **Restricted union (164):** `python3 -I scratchpad/FINDINGS/q.py restricted | head -1` → 164. The merged flag alone gives 159, which matches `counts.md`.
5. **Restricted categories (section 12):** `python3 -I scratchpad/FINDINGS/restricted_categories.py` (hand classification of all 164 ids; the script checks that every restricted id is classified exactly once).

## 15. What the book and app reviews added (2026-10-25)

301 public review units (App Store ca/au for Huckleberry and Napper; us/gb/ca/au for Nara Baby, Glow Baby, Little Ones, Happy Baby; Google Play; Barnes & Noble; Apple Books), 234 quotes in `voice/reviews-rv1.jsonl`; ledger `sources/reviews.md`, blocks `sources/reviews-not-harvested.md`. Public routes show about 10 reviews per app storefront, so these are what the stores display, not a sample of buyers; Happy Baby's reviews look solicited. **Two statements earlier in this document are corrected here.**

- **Correction to sections 8 and 10: refunds and cancellation do appear, in reviews.** A "30 day money back guarantee" with fine print that blocks refunds [sbr1-0098]; "no refunds for subscriptions" with no renewal reminder [sbr1-0115]; charged "£25" after cancelling a free trial [sbr1-0154]; a refund through the App Store that "wasn’t easy" [sbr1-0079]. A Mamivio guarantee must be simple to claim.
- **Correction to section 8: parents do price digital sleep help.** "£60 for pre written schedules and troubleshooting advice" called too much [sbr1-0121]; a nap-timing feature at "$150 a year! Are they nuts?" [sbr1-0006]; an app "a fraction of the price compared to 1-1 sleep consultants" [sbr1-0111]. When a free tracker turned paid, users wanted the basic feature kept free or said they would delete it [sbr1-0042] [sbr1-0161]. This supports a one-time price over a subscription (interpretation).
- **A rigid schedule becomes the parent's guilt, and paid support only repeats it.** "if the schedule isn’t working it’s my fault" [sbr1-0123]; support that will "parrot the same schedule" [sbr1-0101]; replies "almost copy and paste" [sbr1-0117]; a programme that "only works 100%" if followed 100%, impossible with a toddler too [sbr1-0112]; regret after buying at three months [sbr1-0100]. This matches the Reddit complaint about consultants (section 4.1) from paying app users.
- **What parents want the plan to do when things go off-script:** notice short naps and suggest an extra catnap or earlier bedtime [sbr1-0150]; prompt the nap transition with a gradual plan [sbr1-0028]; make troubleshooting easy to find at the moment it is needed [sbr1-0109].
- **Format: a document can work if it is short, sectioned by age and editable.** A paying user wanted the programme's PDF back to make notes [sbr1-0119]; readers praise sections by age so "you only need to read the section" for their child [sbr1-0215] and being able to start without much reading [sbr1-0132]; complaints are too many options for sleep-deprived parents [sbr1-0202], information too hard to find [sbr1-0224], and "words on a page" as weak support [sbr1-0189]. This qualifies Betteroo's "a PDF you'll never open" line (section 8.3).
- **Shared use across caregivers** is paid for and resented when it costs extra: night-shift handover between parents [sbr1-0054]; a premium plan that covers only one parent [sbr1-0058].
