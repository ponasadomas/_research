# Independent advertiser source-context audit — wave 04

Completed and frozen 25 October 2026 Europe/Vilnius. **20 stratified random records plus 5 targeted cases; 23 distinct native IDs re-inspected; 0 material interpretation errors in the inspected set. 0 new unique-reading credit.** Images, video and audio remain unviewed.

The sample was saved before native inspection in `random-sample-seed2026102504.json`, seed **2026102504**, SHA256 `b19751fac1e665680256200216867e1af0cfcebc2b7c7e3595e511554b489924`. Python random.Random selected 2 rows from each lexicographically sorted ledger, then 8 uniformly from the pooled remainder in ledger/line order. The six ledgers contain 604 rows and 604 distinct ad IDs. Final sample allocation: advertiser04-coordination-registry-reading.jsonl: 3, advertiser04-direct-discovery-reading.jsonl: 2, advertiser04-food-safety-reading.jsonl: 4, advertiser04-meal-guides-reading.jsonl: 2, advertiser04-root-safety-reading.jsonl: 3, advertiser04-sleep-play-reading.jsonl: 6.

Every selected original Page capture was parsed directly from its fenced Chrome response. Complete native body, top headline/description/caption, CTA, all supplied cards and extra texts/links/destinations were read. Native advertiser identity, snapshot identity, branded creator, active flag and start timestamp were checked. Saved source hashes matched where provided; the root-safety ledger has no saved source-capture hash, so its current immutable capture hash is recorded in audit.json. No superseded 008 / 013 / 017 / 047 capture was used.

| # | Ad ID | Native capture (queries/) | Cards read | Independent interpretation |
|---|---|---|---:|---|
|1|1792875188650830|029-nugget-savings-page.json|0|subscription_trial_bundle|
|2|28813767631596028|025-babylist-page.json|0|free_registry_registration_giveaway|
|3|1642161400900265|069-goodinside-baby-page.json|4|general_sleep_program_support_bundle|
|4|2922599128112033|069-goodinside-baby-page.json|0|general_sleep_program_support_bundle|
|5|962828846373103|053-tiny-hearts-page.json|2|paid_general_first_aid_course|
|6|1648415323628975|053-tiny-hearts-page.json|0|paid_general_first_aid_course|
|7|3468043670033767|070-happy-eaters-page.json|0|app_acquisition|
|8|1733523184315673|070-happy-eaters-page.json|0|app_acquisition|
|9|1337246441579212|072-pom-babyproofing-page.json|0|physical_babyproofing_goods|
|10|1923060102437580|073-safetots-page.json|3|physical_pet_gate_goods_other_subject|
|11|1634740090828783|003-babysparks-page.json|0|app_acquisition|
|12|1494752132484861|020-napper-page.json|0|app_acquisition|
|13|1825779965438706|006-solid-starts-page.json|0|app_trial_subscription|
|14|940553628854291|046c-wonder-weeks-page.json|2|app_acquisition|
|15|2961899827485513|004-kinedu-english-page.json|0|app_trial_subscription_with_optional_coaching|
|16|1605977997612916|004-kinedu-english-page.json|0|app_acquisition|
|17|1434028511628039|048b-emeals-page.json|2|general_meal_planning_app_subscription|
|18|2118641622369025|005-lovevery-page.json|6|physical_play_learning_goods_mixed_cards|
|19|4375379902726299|042-familywall-page.json|0|family_organizer_app_acquisition|
|20|1110469378139358|072-pom-babyproofing-page.json|6|physical_babyproofing_goods|

All 20 saved classifications are acceptable at their stated scope. Full per-ID reasoning, complete retained text context, pointers, source hashes, identities, dates and destinations are in `audit.json`. The 25 card records in the random set were read, including repeat-text cards and mismatched product destinations. With the targeted Safetots ad there are 28 card records across 23 distinct ads.

The five targeted checks preserve these necessary boundaries:

- **Master Maternity Leave 1804441577549614:** full ad is an application for 3 one-to-one support spots, with no fee or written deliverable. The $17,376 headline is an advertised possible benefit. The saved Blueprint page separately asks USD 997 in full or 3 × USD 347; it cannot price this colorado-plan ad.
- **Nugget 2045675566116239:** native body explicitly offers the 17 November, 7.30pm Zoom webinar plus recording for GBP 14.99 one-off, or included in GBP 29.99/year Platinum. Paid webinar classification is correct.
- **Babylist:** source025 reports 534 active Page results (UI ~530), 26 retained groups and 30 retained IDs, with more pages available. This is brand-wide; sampled 28813767631596028 recruits free registry signups with a possible USD 250 giveaway. Neither number measures a paid registry report.
- **Good Inside Baby:** ads 1642161400900265 and 2922599128112033 land on the program bundle. Saved raw landing includes a 40-minute human session and 3 months app. Checkout item, public amount 17500 and client USD cents formatter support a USD 175 base bundle asking price. The USD 125 and USD 84 labels describe component values. Official footer identity links to drbeckyatgoodinside establish the landed brand; they do not independently establish corporate ownership of exact advertiser Page 482750678569835.
- **Safetots 1079293854792431:** full body plus 3 cards explicitly say FREE consultation with home-tailored advice and product recommendations. Book Now leads to the safety-expert destination. Preserve this free human-personalization funnel alongside the retail ads.

Two optional precision edits would improve exact-ad scope without changing classification:

- Nugget 1792875188650830: “This ad states a 7-day free trial and no post-trial fee; GBP 29.99/year and planner RRP GBP 14.99 belong to the separately identified sibling creative.” The saved note already says “first ID”; avoid silently converting its sibling evidence into price text for this ad.
- eMeals 1434028511628039: “Native cards advertise free easy meal plans as a meal-kit replacement; the app-subscription category uses broader offer context, with no subscription fee in this exact native copy.”

No required correction was identified in the inspected set. No file owned by a prior reader or root was changed. `synthesis/advertiser-money-map.md` appeared during final validation and was then read in full. Its five targeted claims preserve the audited distinctions; no material correction was found within this audit scope. This does not independently verify every other report claim.

A zero-error result is limited to these checks. Full-Page counts cannot establish niche/English-market totals or spend; active flags/start dates cannot prove continuous delivery; asking prices do not prove accepted prices, transactions or profit. Media, unretained variants, budgets, revenue, conversions, CAC, efficacy and independent ownership of the Good Inside Baby Page remain unresolved.
