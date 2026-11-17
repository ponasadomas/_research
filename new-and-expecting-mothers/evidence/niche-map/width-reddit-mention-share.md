# Width proxy — share of harvested Reddit posts mentioning each sub-niche

Generated 2026-10-24 by `_tools/subniche_mention_share.py` over `global/_raw/reddit-deep/windows/2025-h2-v1/` (July–December 2025 submissions, nine communities). **Read this as the share of available post bodies whose title+text matches a wide regex, not as the prevalence of people or problems.** One post can match several rows. Removed/deleted/empty bodies are excluded from the denominator. Regexes favour recall; each is printed at the bottom so you can judge the noise.

## Posts per community

| community | downloaded | available bodies | months | any sub-niche match |
|---|---:|---:|---:|---:|
| r/BabyBumpsCanada | 3,924 | 3,528 | 6 | 2,734 (77%) |
| r/BabyBumps | 30,806 | 26,987 | 6 | 19,092 (71%) |
| r/BabyBumpsandBeyondAu | 4,902 | 4,839 | 6 | 3,497 (72%) |
| r/BabyLedWeaning | 1,996 | 1,981 | 6 | 1,450 (73%) |
| r/BeyondTheBumpUK | 3,976 | 3,940 | 6 | 2,991 (76%) |
| r/ExclusivelyPumping | 11,445 | 11,232 | 6 | 10,389 (92%) |
| r/NewParents | 32,170 | 29,065 | 6 | 24,477 (84%) |
| r/beyondthebump | 18,838 | 18,005 | 6 | 15,371 (85%) |
| r/workingmoms | 4,608 | 4,142 | 6 | 3,449 (83%) |
| **all** | **112,665** | **103,719** | | **83,450** |

## Mention share by sub-niche (all nine communities), sorted

| sub-niche | posts matching | share of available | top communities by share |
|---|---:|---:|---|
| partner_mental_load | 18,472 | 17.8% | r/workingmoms 34%, r/beyondthebump 23%, r/NewParents 20% |
| baby_minor_health | 15,980 | 15.4% | r/NewParents 20%, r/beyondthebump 19%, r/BabyLedWeaning 16% |
| breastfeeding_supply | 14,907 | 14.4% | r/ExclusivelyPumping 43%, r/beyondthebump 17%, r/BabyLedWeaning 16% |
| gear_registry_money | 14,236 | 13.7% | r/BabyBumpsCanada 24%, r/NewParents 20%, r/workingmoms 16% |
| pumping | 13,101 | 12.6% | r/ExclusivelyPumping 83%, r/beyondthebump 6%, r/NewParents 4% |
| sleep | 12,794 | 12.3% | r/NewParents 25%, r/beyondthebump 17%, r/BeyondTheBumpUK 17% |
| return_to_work_childcare | 10,609 | 10.2% | r/workingmoms 47%, r/BabyBumpsCanada 13%, r/BeyondTheBumpUK 12% |
| pregnancy_symptoms | 10,123 | 9.8% | r/BabyBumps 29%, r/BabyBumpsCanada 13%, r/BabyBumpsandBeyondAu 7% |
| reflux_colic_fussy | 9,081 | 8.8% | r/NewParents 15%, r/beyondthebump 11%, r/BeyondTheBumpUK 10% |
| birth_prep_labour | 8,410 | 8.1% | r/BabyBumps 17%, r/BabyBumpsCanada 14%, r/BabyBumpsandBeyondAu 10% |
| maternal_mental_health | 7,291 | 7.0% | r/workingmoms 14%, r/beyondthebump 10%, r/ExclusivelyPumping 8% |
| formula_bottle | 7,071 | 6.8% | r/ExclusivelyPumping 19%, r/BabyLedWeaning 9%, r/NewParents 9% |
| postpartum_body | 6,949 | 6.7% | r/beyondthebump 15%, r/ExclusivelyPumping 8%, r/BabyBumps 5% |
| travel_outings | 5,874 | 5.7% | r/workingmoms 12%, r/BabyBumpsCanada 9%, r/BeyondTheBumpUK 7% |
| what_to_do_all_day | 5,810 | 5.6% | r/workingmoms 10%, r/NewParents 8%, r/beyondthebump 7% |
| milestones_development | 5,256 | 5.1% | r/NewParents 10%, r/beyondthebump 7%, r/BeyondTheBumpUK 7% |
| solids | 4,907 | 4.7% | r/BabyLedWeaning 55%, r/NewParents 7%, r/BeyondTheBumpUK 5% |
| second_baby_twins_prem | 4,440 | 4.3% | r/ExclusivelyPumping 7%, r/beyondthebump 5%, r/BabyBumps 4% |
| mom_fitness_weight | 4,050 | 3.9% | r/workingmoms 8%, r/beyondthebump 5%, r/NewParents 4% |
| family_inlaws_visitors | 3,810 | 3.7% | r/beyondthebump 7%, r/workingmoms 6%, r/BeyondTheBumpUK 6% |
| information_overload | 3,206 | 3.1% | r/NewParents 4%, r/BeyondTheBumpUK 4%, r/ExclusivelyPumping 3% |
| relationship_intimacy | 3,030 | 2.9% | r/workingmoms 5%, r/beyondthebump 5%, r/BabyBumps 4% |
| toddler_behaviour | 2,216 | 2.1% | r/NewParents 4%, r/workingmoms 3%, r/beyondthebump 3% |
| speech_language | 1,048 | 1.0% | r/NewParents 2%, r/beyondthebump 1%, r/BeyondTheBumpUK 1% |
| social_eye_contact | 837 | 0.8% | r/workingmoms 2%, r/beyondthebump 1%, r/NewParents 1% |
| potty | 352 | 0.3% | r/workingmoms 1%, r/beyondthebump 1%, r/BeyondTheBumpUK 0% |
| baby_names | 203 | 0.2% | r/BabyBumps 1%, r/BabyBumpsandBeyondAu 0%, r/BabyBumpsCanada 0% |
| memory_keeping | 186 | 0.2% | r/BabyBumpsandBeyondAu 0%, r/BeyondTheBumpUK 0%, r/NewParents 0% |

## Share by community (rows = sub-niche, columns = community)

| sub-niche | r/BabyBumpsCanada | r/BabyBumps | r/BabyBumpsandBeyondAu | r/BabyLedWeaning | r/BeyondTheBumpUK | r/ExclusivelyPumping | r/NewParents | r/beyondthebump | r/workingmoms |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| partner_mental_load | 12.0% | 16.4% | 11.8% | 8.4% | 15.3% | 8.6% | 19.8% | 22.9% | 34.0% |
| baby_minor_health | 13.5% | 13.0% | 13.3% | 15.9% | 14.6% | 7.4% | 19.6% | 19.2% | 11.3% |
| breastfeeding_supply | 6.5% | 4.5% | 8.8% | 16.1% | 15.3% | 42.7% | 14.3% | 16.6% | 4.7% |
| gear_registry_money | 24.1% | 9.2% | 14.5% | 2.0% | 13.8% | 5.6% | 19.6% | 14.4% | 16.2% |
| pumping | 3.7% | 2.4% | 3.5% | 1.7% | 3.7% | 83.4% | 4.5% | 6.3% | 4.4% |
| sleep | 3.4% | 1.9% | 7.8% | 5.1% | 16.6% | 2.6% | 25.2% | 16.9% | 8.4% |
| return_to_work_childcare | 13.1% | 4.1% | 11.2% | 4.6% | 12.1% | 9.2% | 10.7% | 10.1% | 47.3% |
| pregnancy_symptoms | 12.7% | 28.7% | 7.5% | 0.2% | 1.5% | 1.4% | 1.4% | 4.5% | 3.4% |
| reflux_colic_fussy | 3.2% | 4.0% | 6.0% | 6.2% | 9.6% | 4.2% | 15.5% | 11.3% | 2.3% |
| birth_prep_labour | 14.3% | 16.7% | 9.9% | 0.2% | 5.6% | 2.7% | 2.6% | 8.4% | 3.3% |
| maternal_mental_health | 3.9% | 4.6% | 4.7% | 2.2% | 6.9% | 8.1% | 7.5% | 9.5% | 13.9% |
| formula_bottle | 2.9% | 1.2% | 4.9% | 8.9% | 8.6% | 18.7% | 8.8% | 6.7% | 1.0% |
| postpartum_body | 4.6% | 5.5% | 3.8% | 0.3% | 4.5% | 7.5% | 4.6% | 14.7% | 3.0% |
| travel_outings | 8.5% | 4.4% | 6.4% | 2.8% | 7.4% | 4.7% | 5.9% | 5.5% | 11.7% |
| what_to_do_all_day | 2.2% | 3.2% | 3.3% | 2.4% | 6.4% | 2.7% | 8.1% | 7.4% | 10.3% |
| milestones_development | 1.9% | 1.2% | 3.2% | 3.0% | 6.5% | 1.0% | 10.1% | 6.8% | 2.5% |
| solids | 1.6% | 0.6% | 3.2% | 55.1% | 5.2% | 3.1% | 6.5% | 5.0% | 2.3% |
| second_baby_twins_prem | 2.6% | 4.4% | 3.0% | 2.6% | 2.2% | 7.4% | 3.2% | 5.4% | 4.1% |
| mom_fitness_weight | 2.0% | 3.5% | 3.5% | 0.7% | 3.2% | 3.0% | 3.8% | 5.4% | 7.8% |
| family_inlaws_visitors | 2.3% | 3.5% | 2.1% | 1.6% | 6.0% | 1.0% | 2.9% | 6.7% | 6.1% |
| information_overload | 2.4% | 2.6% | 2.7% | 1.2% | 3.7% | 3.2% | 3.9% | 3.1% | 1.6% |
| relationship_intimacy | 0.9% | 4.5% | 1.1% | 0.3% | 1.8% | 0.5% | 1.8% | 4.9% | 5.2% |
| toddler_behaviour | 0.5% | 0.7% | 1.4% | 1.7% | 1.9% | 0.9% | 3.5% | 3.2% | 3.3% |
| speech_language | 0.4% | 0.2% | 0.6% | 0.4% | 1.0% | 0.1% | 2.0% | 1.5% | 0.8% |
| social_eye_contact | 0.4% | 0.6% | 0.7% | 0.2% | 0.8% | 0.2% | 1.0% | 1.2% | 1.7% |
| potty | 0.2% | 0.1% | 0.3% | 0.0% | 0.5% | 0.0% | 0.4% | 0.6% | 0.7% |
| baby_names | 0.2% | 0.6% | 0.3% | 0.0% | 0.1% | 0.0% | 0.0% | 0.1% | 0.0% |
| memory_keeping | 0.2% | 0.2% | 0.4% | 0.0% | 0.2% | 0.0% | 0.2% | 0.2% | 0.1% |

## Regexes used

- `sleep`: `\b(sleep regress\w*|sleep[- ]train\w*|naps?\b|napping|wake windows?|bedtime|night ?wak\w*|contact naps?|won'?t sleep|cry it out|ferber|sleep schedule|short naps?|false start|split nights?)`
- `breastfeeding_supply`: `\b(breast ?fe\w+|nursing|latch\w*|milk supply|low supply|oversupply|mastitis|clogged duct|nipples?|wean\w*)\b`
- `pumping`: `\b(pump(s|ed|ing)?|exclusive(ly)? pump\w*|freezer stash|haakaa|flange)\b`
- `formula_bottle`: `\b(formula|bottle[- ]refus\w*|bottle[- ]fe\w+|combo[- ]fe\w+|paced feed\w*|how (much|many) (oz|ounces|ml))\b`
- `reflux_colic_fussy`: `\b(reflux|colic\w*|gassy|gas pain|spit(s|ting)? up|weight gain|not gaining|percentiles?|witching hour|fussy|screaming)\b`
- `solids`: `\b(solids?|baby[- ]led weaning|blw|pur[eé]es?|first foods?|allergens?|starting solids|finger foods?|picky eat\w*)\b`
- `milestones_development`: `\b(milestones?|tummy time|roll(s|ed|ing)? over|crawl(s|ed|ing)?|sit(s|ting)? up (on|un|by)|pull(s|ing)? (himself|herself|themselves|up)|development(al)?|early intervention|motor skills?|head control|head lag)\b`
- `speech_language`: `\b(babbl\w*|first words?|speech|not talking|talking yet|say(s|ing)? (mama|dada)|language delay|words? yet|speech therap\w*)\b`
- `social_eye_contact`: `\b(eye contact|autis\w*|respond(s|ing)? to (his|her|their) name|social smile|not smiling|pointing|wav(e|es|ing) bye|red flags?)\b`
- `toddler_behaviour`: `\b(tantrums?|meltdowns?|hitting|biting|discipline|time[- ]?outs?|gentle parenting|terrible twos|whining|defian\w*|big feelings)\b`
- `potty`: `\b(potty|toilet[- ]train\w*|pull-?ups|diaper[- ]free)\b`
- `pregnancy_symptoms`: `\b(nausea|morning sickness|hyperemesis|heartburn|braxton|contractions?|weeks pregnant|trimesters?|ultrasound|anatomy scan|glucose test|gestational|round ligament|swelling)\b`
- `birth_prep_labour`: `\b(birth plan|hospital bag|induction|induced|c-?sections?|epidural|labou?r\b|due date|doula|midwi(fe|ves)|birth(ing)? class|hypnobirth\w*|delivery)\b`
- `postpartum_body`: `\b(postpartum|post-?partum|pelvic floor|diastasis|stitches|tear(ing)?|incontinen\w*|leak(ing|s)? (pee|urine)|hair loss|night sweats|lochia|bleeding after)\b`
- `maternal_mental_health`: `\b(ppd|ppa|postpartum (depression|anxiety|rage)|baby blues|intrusive thoughts|touched out|lost myself|identity|lonely|isolat\w*|mom guilt|guilt|overwhelm\w*|burn(t|ed)? ?out)\b`
- `partner_mental_load`: `\b(mental load|my husband|my partner|my wife|resent\w*|default parent|division of labou?r|he doesn'?t|doesn'?t help)\b`
- `family_inlaws_visitors`: `\b(in-?laws?|mother-?in-?law|\bmil\b|\bfil\b|grandparents?|grandmas?|grandmothers?|visitors?|boundar(y|ies)|unsolicited)\b`
- `return_to_work_childcare`: `\b(maternity leave|parental leave|mat leave|return(ing)? to work|back to work|daycare|day care|nursery|childcare|child care|nann(y|ies)|fmla|pump(ing)? at work)\b`
- `gear_registry_money`: `\b(registry|strollers?|car seats?|cribs?|bassinets?|snoo|baby monitors?|budget\w*|afford\w*|expensive|cost(s|ly)?|worth it|babylist|must[- ]haves?)\b`
- `travel_outings`: `\b(flights?|flying|airplane|plane|road trips?|travel\w*|vacation|holiday|restaurants?|outings?|leave the house|getting out of the house)\b`
- `baby_names`: `\b(baby names?|name (ideas|suggestions|help)|middle names?|first names?)\b`
- `memory_keeping`: `\b(baby book|photo ?books?|albums?|keepsakes?|newborn (photos?|shoot|session)|milestone (cards|photos?)|scrapbook\w*)\b`
- `second_baby_twins_prem`: `\b(second baby|baby #? ?2|age gap|two under (two|2)|twins?|nicu|premature|preemie|corrected age|adjusted age|siblings?)\b`
- `mom_fitness_weight`: `\b(lose (the )?weight|baby weight|work ?outs?|exercis\w*|gym|running|prenatal (yoga|pilates)|bounce back|body after)\b`
- `relationship_intimacy`: `\b(sex|intimacy|libido|marriage|relationship)\b`
- `baby_minor_health`: `\b(rash|eczema|cradle cap|baby acne|fever|sick|a cold|teething|vaccin\w*|pediatrician|paediatrician|gp\b|doctor)\b`
- `what_to_do_all_day`: `\b(what (do|should) (i|we|you) do with|all day|bored|entertain\w*|activities|play ideas|screen time|\btv\b|overstimulat\w*)\b`
- `information_overload`: `\b(conflicting (advice|info\w*)|so much (advice|information)|googl\w*|2 ?am|3 ?am|overwhelm\w* (by|with) (advice|info)|every(one|body) says|too much information)\b`

Caveats: r/ExclusivelyPumping, r/BabyLedWeaning and r/workingmoms are topic communities, so their own topic dominates their column and inflates the all-communities total for pumping, solids and work return. Pregnancy communities (r/BabyBumps, r/BabyBumpsCanada, r/BabyBumpsandBeyondAu, r/BeyondTheBumpUK in part) inflate pregnancy rows. The useful comparison is within the general communities r/NewParents and r/beyondthebump. No sleep, breastfeeding, toddler, potty or mental-health community was harvested; those rows are therefore lower bounds for width.