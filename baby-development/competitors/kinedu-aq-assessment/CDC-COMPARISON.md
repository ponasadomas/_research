# Kinedu rates versus CDC milestones (Phase 9)

**The usable comparisons lean toward making children look ahead, conditional on `rate` meaning “share already doing it.”** Of 20 matched pairs with a share available at the CDC age, 11 are below CDC's 75% floor, seven are 75–95%, and two exceed 95%. The median is 73.75%. Restricting to the 14 directly observed values gives a 67.50% median, with nine below 75%. This is evidence of lower Kinedu expectations in this selected subset, not proof of dishonesty or a bank-wide bias.

## Method and sources

Retrieved **2026-11-03**. All HTTP used `scripts/proxy_curl.sh`; no browser was used. The 11 requested ages are 2, 4, 6, 9, 12, 15, 18, 24, 30, 36 and 48 months. Ten legacy checklist URLs redirected successfully. The legacy 15-month URL and legacy index returned 404; the [current CDC index](https://www.cdc.gov/act-early/milestones/index.html) links the working [15-month checklist](https://www.cdc.gov/act-early/milestones/15-months.html). Every fetched response body, including failed HTTP responses, is saved under [raw/cdc/](raw/cdc/). [Fetch provenance](raw/cdc/fetch-manifest.json), [checklist counts and SHA-256 hashes](raw/cdc/checklist-manifest.json), and [methodology source notes](raw/cdc/methodology-notes.md) preserve the audit trail.

CDC's February 2022 revision places milestones at checklist ages by which **about 75% or more** of children would be expected to do them. It shifted the selection rule away from average-age/50% expectations, using a literature review and clinical judgment. These are communication and developmental-monitoring checklists, not item-by-item empirical prevalence curves, developmental standards, or validated screening/diagnostic tools. [CDC's explanation of the revision](https://www.cdc.gov/act-early/milestones/key-points.html) supports these distinctions. The captures are current pages implementing that revision, not a frozen copy of the February 2022 website; page-update dates are later.

**Extraction.** We extracted only the milestone bullet sentences under the four developmental headings, excluding parenting tips, doctor questions and duplicate media-modal captions. The result is **144 milestones** in [cdc-milestones.csv](raw/cdc/cdc-milestones.csv), with CDC age, normalized domain, original sentence, source URL and local capture path. The requested ages stop at four years; five-year milestones are excluded.

| CDC age (months) | Extracted milestones | Matched | Observed at age | Interpolated at age |
| --- | --- | --- | --- | --- |
| 2 | 11 | 6 | 1 | 0 |
| 4 | 13 | 6 | 2 | 0 |
| 6 | 12 | 6 | 1 | 1 |
| 9 | 13 | 9 | 1 | 2 |
| 12 | 10 | 8 | 0 | 2 |
| 15 | 13 | 6 | 2 | 1 |
| 18 | 15 | 4 | 0 | 0 |
| 24 | 13 | 5 | 0 | 0 |
| 30 | 15 | 9 | 2 | 0 |
| 36 | 12 | 4 | 3 | 0 |
| 48 | 17 | 8 | 2 | 0 |

**Semantic matching.** The 408 Kinedu questions were read against the CDC sentences; no text-similarity score was used as a substitute for matching the behavior and difficulty. We retained **71 pairs: 53 exact and 18 close**. “Exact” means the essential behavior and threshold agree, even if wording differs. “Close” preserves the core task/level with a narrower example or a small contextual qualification; the reason is stated for every pair. These remain human judgments, so the exact-only result is also reported. “Loose” candidates have a material difference or uncertainty in support, gesture cues, word count, task, reliability or complexity and are excluded from all numeric summaries. For example, a chuckle is not matched to a full laugh, trying a spoon is not matched to independent spoon feeding, and asking questions is not matched to answering them. Two tempting vocal-response pairs (143 and 23) are also excluded: Kinedu specifies babbling, which could be harder than CDC's unspecified sounds. Each CDC milestone and Kinedu question is counted at most once. Alternative hidden-toy, first-step, color and dressing questions are not multiplied into additional votes. The complete decisions are in [matches.json](raw/cdc/matches.json) and [unmatched-reasons.json](raw/cdc/unmatched-reasons.json).

**Rates and estimates.** Inputs are [questions.csv](questions.csv), specifically `rate_by_age_months` and `raw_observations`, with [questions-by-age.md](questions-by-age.md) as the base-question presentation record. All rates in the CSV agree with the raw observations: 2,173 rate-bearing observation objects, with no conflicting rates at the same question/age. We use numeric rates from both base and extension questions; report-only `status` values are not converted to rates. Thirty-five questions have no rate observations, including three of the matched questions.

For each pair, every available age-specific rate is listed in the table, sorted by month. An observed value at the CDC month takes precedence. Otherwise, we show the nearest observed month on each side and calculate `p(X) = p(L) + (X − L) × [p(U) − p(L)] / (U − L)` only when `L < X < U`. Interpolation is an inference, not an observation. All six interpolation gaps are 4–8 months, so these estimates are weak, especially near 75%. If only one side exists, or neither exists, the CDC-age value is **not estimable**: we do not carry a rate forward, extrapolate, treat a missing rate as zero, or substitute a report's `typical` status. We preserve non-monotonic rates without smoothing: for example, the approximately-50-word item (373) drops from 67% at 30 months to 64% at 33 months. Thresholds use unrounded values; percentages are rounded only for display.

**Verdict rules (mutually exclusive).** “Consistent” is 75% through 95%; “stricter/later” is 50% through less than 75%; “clearly later” is below 50%; and “high >95%” is above 95%. Exactly 50% belongs to stricter/later and exactly 75% to consistent. The high group is also compatible with the CDC floor and is separated only to implement the requested high-share flag. Lower Kinedu shares would tend to make the same achievements look better; high shares could make a missing skill look worse. These are interpretations of expectations, not measured changes to an individual child's AQ result.

**The CDC floor is one-sided.** A rate above 95% at the CDC age does **not** establish earlier attainment or inflation: CDC allows any share at or above 75%. Nor does a CDC placement imply every earlier month's true share must be below 75%; checklist ages are discrete and do not identify an exact 75th-percentile crossing. Thus the requested “nearly all do it earlier / parents look worse” verdict is shown as a **high-share flag**, with actual earlier observations discussed separately. A “consistent” rate is compatible with the floor, not validated as the true population rate.

## Summary

| Verdict | Observed | Interpolated | Total | Meaning |
| --- | --- | --- | --- | --- |
| consistent | 3 | 4 | 7 | 75–95%; compatible with the CDC floor |
| stricter/later | 9 | 2 | 11 | 50–<75%; lower share, tending to make children look ahead |
| clearly later | 0 | 0 | 0 | <50%; substantially below the CDC floor |
| high >95% | 2 | 0 | 2 | >95%; floor-compatible high flag, not proof of inflation |
| not estimable | 0 | 0 | 51 | No observed value or two-sided bracket at the CDC age |

The 20 numeric comparisons are **14 observed + 6 interpolated**. Of the **51 unestimable** pairs, 47 have rates only before the CDC age, one only after it, and three have no numeric rates. Missing-age pairs remain in the matched table and denominator for coverage, but are excluded from medians and numeric verdict percentages. Below-floor pairs are **11/20 (55.0%)** with interpolation or **9/14 (64.3%)** observed only. Nine of 20 meet the floor, including both high flags. No retained strict pair is below 50%.

### By CDC domain

| Group | CDC items | Matched | Observed | Interpolated | Consistent | 50–<75% | <50% | >95% | No estimate | Median of numeric shares |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Social/Emotional | 39 | 14 | 3 | 2 | 3 | 1 | 0 | 1 | 9 | 86.80% |
| Language/Communication | 36 | 17 | 5 | 3 | 3 | 5 | 0 | 0 | 9 | 72.25% |
| Cognitive | 27 | 15 | 1 | 1 | 1 | 1 | 0 | 0 | 13 | 69.71% |
| Movement/Physical | 42 | 25 | 5 | 0 | 0 | 4 | 0 | 1 | 20 | 57.00% |

Domain follows the **CDC heading**, even when Kinedu assigns the question to a different area. The numeric sample sizes are only 5 social/emotional, 8 language, 2 cognitive and 5 movement/physical; the domain medians should not be read as population estimates.

### By CDC age band

| Group | CDC items | Matched | Observed | Interpolated | Consistent | 50–<75% | <50% | >95% | No estimate | Median of numeric shares |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0–12 | 59 | 35 | 5 | 5 | 5 | 3 | 0 | 2 | 25 | 83.21% |
| 13–24 | 41 | 15 | 2 | 1 | 2 | 1 | 0 | 0 | 12 | 86.80% |
| 25–48 | 44 | 21 | 7 | 0 | 0 | 7 | 0 | 0 | 14 | 58.00% |

Band membership uses CDC's milestone age. The 13–24-month numeric results are all at **15 months**: there are no estimable pairs at 18 or 24 months. The 25–48-month band has seven numeric pairs and all are below 75%; its two 48-month points are close matches. Uneven coverage prevents a claim about every age in a band.

### Sensitivity to matching and interpolation

| Selection | Matched/selected rows | Numeric | Below 75% | 75–95% | >95% | Median |
| --- | --- | --- | --- | --- | --- | --- |
| Exact + close; observed + interpolation | 71 | 20 | 11 | 7 | 2 | 73.75% |
| Exact + close; observed only | 14 | 14 | 9 | 3 | 2 | 67.50% |
| Exact only; observed + interpolation | 53 | 14 | 8 | 5 | 1 | 72.25% |
| Exact only; observed only | 9 | 9 | 6 | 2 | 1 | 67.00% |

The direction survives both restrictions: the **nine exact, directly observed** pairs have a 67% median, with six below 75%. This is a descriptive sensitivity check, not independent replication: items and developmental skills are correlated.

## Matched pairs

Each heading gives the CDC age in months; every CDC sentence links to its captured source page. In “all rates,” `m:value` means month `m` and the Kinedu rate as a percentage. For missing-age rows, “before” and “after” are the nearest rate-bearing months; `—` means none was observed. The CSV retains unrounded estimates and individual endpoint columns: [matched-pairs.csv](raw/cdc/matched-pairs.csv).

### CDC age 2 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-02-SE-01 · Social/Emotional · [Calms down when spoken to or picked up](https://www.cdc.gov/act-early/milestones/2-months.html#calmsDown) | **122** · Becomes calm when hearing voices they know. | 0:77%; 1:88% | **Not estimable**; before 1m:88%; after — | not estimable | **close** — Same calming response to speech; Kinedu specifies familiar voices, one ordinary instance of CDC's spoken-to alternative. |
| CDC-02-SE-02 · Social/Emotional · [Looks at your face](https://www.cdc.gov/act-early/milestones/2-months.html#looksFace) | **240** · Stares at people's faces. | 0:73%; 2:94% | **94% observed** at 2m | consistent | **exact** — Both describe looking at people's faces; no extra task or achievement threshold. |
| CDC-02-SE-04 · Social/Emotional · [Smiles when you talk to or smile at her](https://www.cdc.gov/act-early/milestones/2-months.html#smilesTalk2) | **283** · Smiles when people make eye contact. | 0:36%; 1:65% | **Not estimable**; before 1m:65%; after — | not estimable | **close** — Both describe an elicited social smile; Kinedu specifies eye contact rather than speech or an adult smile. |
| CDC-02-LC-02 · Language/Communication · [Reacts to loud sounds](https://www.cdc.gov/act-early/milestones/2-months.html#Reactstoloudsounds) | **38** · Gets startled by loud sounds. | No numeric rates | **Not estimable**; before —; after — | not estimable | **exact** — Both describe a response to loud sounds; Kinedu specifies the startle response. This question has no numeric rate observations. |
| CDC-02-CO-01 · Cognitive · [Watches you as you move](https://www.cdc.gov/act-early/milestones/2-months.html#watchesYouMove) | **281** · Turns their head to follow objects with their eyes. | 0:37%; 1:65% | **Not estimable**; before 1m:65%; after — | not estimable | **close** — Same visual tracking of a moving target; CDC uses a person and Kinedu an object. |
| CDC-02-MP-01 · Movement/Physical · [Holds head up when on tummy](https://www.cdc.gov/act-early/milestones/2-months.html#holdsHeadUp) | **75** · When lying on their tummy, they lift their head for a short time. | 0:70% | **Not estimable**; before 0m:70%; after — | not estimable | **exact** — Both describe lifting/holding the head up while prone; CDC sets no longer duration requirement. |

### CDC age 4 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-04-SE-03 · Social/Emotional · [Looks at you, moves, or makes sounds to get or keep your attention](https://www.cdc.gov/act-early/milestones/4-months.html#looks_you) | **108** · Repeats sounds or actions to get people to look. | 5:21%; 6:36%; 7:52%; 8:78%; 9:84% | **Not estimable**; before —; after 5m:21% | not estimable | **close** — Same use of sounds or actions to get attention; Kinedu describes repeating the attention bid. |
| CDC-04-LC-01 · Language/Communication · [Makes sounds like “oooo”, “aahh” (cooing)](https://www.cdc.gov/act-early/milestones/4-months.html#makes_sounds) | **197** · Makes vowel sounds like 'eh' or 'ah'. | 0:37%; 1:49%; 2:80%; 4:92% | **92% observed** at 4m | consistent | **exact** — Both describe open-vowel cooing, with equivalent ah/eh examples. |
| CDC-04-CO-02 · Cognitive · [Looks at her hands with interest](https://www.cdc.gov/act-early/milestones/4-months.html#looks_at_hands) | **81** · Stares at their hands for a few seconds. | 2:52% | **Not estimable**; before 2m:52%; after — | not estimable | **exact** — Both describe looking at one's own hands for a short time. |
| CDC-04-MP-02 · Movement/Physical · [Holds a toy when you put it in his hand](https://www.cdc.gov/act-early/milestones/4-months.html#holds_toy) | **294** · Grabs a small object placed in their hands. | 0:31%; 2:53% | **Not estimable**; before 2m:53%; after — | not estimable | **close** — Both describe grasping/holding an object placed in the hand; Kinedu calls it a small object rather than a toy. |
| CDC-04-MP-04 · Movement/Physical · [Brings hands to mouth](https://www.cdc.gov/act-early/milestones/4-months.html#brings_hands) | **41** · Brings their hands to their mouth. | 0:88%; 1:92%; 2:96%; 3:98%; 4:97%; 5:97%; 6:98% | **97% observed** at 4m | high >95% | **exact** — Same hand-to-mouth behavior. |
| CDC-04-MP-05 · Movement/Physical · [Pushes up onto elbows/forearms when on tummy](https://www.cdc.gov/act-early/milestones/4-months.html#pushes_up) | **115** · Props up their upper body with their elbows and forearms when they're on their belly. | 3:57% | **Not estimable**; before 3m:57%; after — | not estimable | **exact** — Same prone upper-body support on elbows and forearms. |

### CDC age 6 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-06-SE-01 · Social/Emotional · [Knows familiar people](https://www.cdc.gov/act-early/milestones/6-months.html#knows_familiar) | **97** · Recognizes caregivers. | 0:56%; 1:73%; 6:98% | **98% observed** at 6m | high >95% | **close** — Same recognition of familiar people; Kinedu names the familiar caregivers. |
| CDC-06-SE-03 · Social/Emotional · [Laughs](https://www.cdc.gov/act-early/milestones/6-months.html#Laughs_id) | **112** · Laughs out loud. | 3:38%; 4:68%; 9:98% | **80.00% interpolated**; before 4m:68%; after 9m:98% | consistent | **exact** — Same audible laugh; unlike CDC's earlier four-month chuckle, this item requires laughter. |
| CDC-06-CO-01 · Cognitive · [Puts things in her mouth to explore them](https://www.cdc.gov/act-early/milestones/6-months.html#puts_things) | **73** · Grabs objects and puts them in their mouth. | 2:42% | **Not estimable**; before 2m:42%; after — | not estimable | **exact** — Same exploration by putting objects in the mouth. |
| CDC-06-CO-02 · Cognitive · [Reaches to grab a toy she wants](https://www.cdc.gov/act-early/milestones/6-months.html#reaches_grab) | **153** · Reaches for something and grabs it. | 4:59% | **Not estimable**; before 4m:59%; after — | not estimable | **exact** — Both describe reaching for an object and grasping it. |
| CDC-06-MP-01 · Movement/Physical · [Rolls from tummy to back](https://www.cdc.gov/act-early/milestones/6-months.html#rolls_tummy) | **151** · Rolls from tummy to back. | 1:54%; 5:55% | **Not estimable**; before 5m:55%; after — | not estimable | **exact** — Same tummy-to-back roll; not the harder roll-both-ways question. |
| CDC-06-MP-03 · Movement/Physical · [Leans on hands to support herself when sitting](https://www.cdc.gov/act-early/milestones/6-months.html#leans_hands) | **272** · Uses their arms and hands to help them sit without falling over. | 5:57% | **Not estimable**; before 5m:57%; after — | not estimable | **exact** — Same hand/arm support to remain seated: supported or tripod sitting, not independent sitting. |

### CDC age 9 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-09-SE-01 · Social/Emotional · [Is shy, clingy, or fearful around strangers](https://www.cdc.gov/act-early/milestones/9-months.html#is_shy) | **186** · Feels shy or anxious when meeting new adults. | 6:27%; 7:41%; 8:55%; 9:68%; 10:81% | **68% observed** at 9m | stricter/later | **exact** — Both describe shyness or anxiety around unfamiliar adults. |
| CDC-09-SE-03 · Social/Emotional · [Looks when you call her name](https://www.cdc.gov/act-early/milestones/9-months.html#looks_when_called) | **110** · When they hear their name, they move toward the person by crawling, walking, or turning in their direction. | 1:39%; 2:26%; 3:25%; 4:35%; 5:60%; 6:75%; 7:88% | **Not estimable**; before 7m:88%; after — | not estimable | **close** — Both include orienting when the child's name is called; Kinedu explicitly allows turning, so crawling/walking is not required. |
| CDC-09-LC-01 · Language/Communication · [Makes a lot of different sounds like “mamamama” and “bababababa”](https://www.cdc.gov/act-early/milestones/9-months.html#makes_different) | **31** · Repeats 'baba' or 'dada' kind of sounds. | 2:9%; 3:15%; 4:15%; 5:27%; 6:51%; 12:89% | **70.00% interpolated**; before 6m:51%; after 12m:89% | stricter/later | **exact** — Same repeated consonant-vowel babbling, with baba/dada equivalents to CDC's examples. |
| CDC-09-LC-02 · Language/Communication · [Lifts arms up to be picked up](https://www.cdc.gov/act-early/milestones/9-months.html#lifts_arms) | **20** · Lifts their arms to be carried. | 4:21%; 5:51%; 6:72%; 7:83%; 8:92% | **Not estimable**; before 8m:92%; after — | not estimable | **exact** — Same raising the arms to be picked up/carried. |
| CDC-09-CO-01 · Cognitive · [Looks for objects when dropped out of sight (like his spoon or toy)](https://www.cdc.gov/act-early/milestones/9-months.html#looks_objects) | **183** · Looks for an item they dropped on the floor. | 2:60%; 3:54%; 4:56%; 5:63%; 12:97% | **82.43% interpolated**; before 5m:63%; after 12m:97% | consistent | **close** — Same search for a dropped object; CDC explicitly says out of sight, while Kinedu says looking for the dropped item on the floor. |
| CDC-09-CO-02 · Cognitive · [Bangs two things together](https://www.cdc.gov/act-early/milestones/9-months.html#bangs_two) | **217** · Hits two things together. | 4:28%; 5:57% | **Not estimable**; before 5m:57%; after — | not estimable | **exact** — Same banging/hitting two objects together. |
| CDC-09-MP-01 · Movement/Physical · [Gets to a sitting position by herself](https://www.cdc.gov/act-early/milestones/9-months.html#gets_sitting) | **270** · Goes from lying to sitting without help. | 8:56% | **Not estimable**; before 8m:56%; after — | not estimable | **exact** — Same independent transition into sitting from lying down. |
| CDC-09-MP-02 · Movement/Physical · [Moves things from one hand to her other hand](https://www.cdc.gov/act-early/milestones/9-months.html#moves_things) | **165** · Switches things between their hands. | 5:50% | **Not estimable**; before 5m:50%; after — | not estimable | **exact** — Same hand-to-hand object transfer. |
| CDC-09-MP-04 · Movement/Physical · [Sits without support](https://www.cdc.gov/act-early/milestones/9-months.html#sits_without) | **118** · Sits independently. | 6:59% | **Not estimable**; before 6m:59%; after — | not estimable | **exact** — Same unsupported, independent sitting. |

### CDC age 12 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-12-LC-01 · Language/Communication · [Waves “bye-bye”](https://www.cdc.gov/act-early/milestones/1-year.html#bye_bye) | **22** · Says hello or goodbye with hand movements. | 1:13%; 8:47%; 9:63%; 13:91% | **84.00% interpolated**; before 9m:63%; after 13m:91% | consistent | **exact** — Both include a conventional goodbye hand wave; Kinedu also permits the equivalent hello wave. |
| CDC-12-LC-02 · Language/Communication · [Calls a parent “mama” or “dada” or another special name](https://www.cdc.gov/act-early/milestones/1-year.html#calls_parent) | **249** · Refers to caregivers as 'mama' or 'papa.' | 6:65%; 8:57%; 9:58%; 10:65% | **Not estimable**; before 10m:65%; after — | not estimable | **exact** — Same meaningful name for a caregiver, with mama/papa examples. |
| CDC-12-LC-03 · Language/Communication · [Understands “no” (pauses briefly or stops when you say it)](https://www.cdc.gov/act-early/milestones/1-year.html#understands_no) | **67** · Knows what 'no' means. | 6:54%; 7:54%; 8:57%; 16:92% | **74.50% interpolated**; before 8m:57%; after 16m:92% | stricter/later | **exact** — Same understanding of the word no; Kinedu omits CDC's explanatory pause/stop example. |
| CDC-12-CO-01 · Cognitive · [Puts something in a container, like a block in a cup](https://www.cdc.gov/act-early/milestones/1-year.html#puts_something) | **172** · Puts things into containers. | 9:43% | **Not estimable**; before 9m:43%; after — | not estimable | **exact** — Same placing objects into a container. |
| CDC-12-CO-02 · Cognitive · [Looks for things he sees you hide, like a toy under a blanket](https://www.cdc.gov/act-early/milestones/1-year.html#looks_things) | **206** · Looks for a toy that was just hidden. | 3:44%; 4:34%; 5:45%; 6:64%; 7:69%; 8:82% | **Not estimable**; before 8m:82%; after — | not estimable | **close** — Same search for a just-hidden toy; CDC makes watching the hiding explicit. Other hidden-toy questions are not counted again. |
| CDC-12-MP-01 · Movement/Physical · [Pulls up to stand](https://www.cdc.gov/act-early/milestones/1-year.html#pulls_up) | **113** · Goes from sitting to standing with the aid of a large object, like furniture. | 7:61% | **Not estimable**; before 7m:61%; after — | not estimable | **close** — Same supported transition to standing using furniture; Kinedu specifies a sitting start. |
| CDC-12-MP-02 · Movement/Physical · [Walks, holding on to furniture](https://www.cdc.gov/act-early/milestones/1-year.html#walks_holding) | **15** · Walks or cruises while holding onto big furniture. | 6:41%; 8:51%; 9:61% | **Not estimable**; before 9m:61%; after — | not estimable | **exact** — Same cruising/walking while holding furniture. |
| CDC-12-MP-04 · Movement/Physical · [Picks things up between thumb and pointer finger, like small bits of food](https://www.cdc.gov/act-early/milestones/1-year.html#picks_things) | **378** · Holds small objects using their thumb and forefinger. | No numeric rates | **Not estimable**; before —; after — | not estimable | **exact** — Same thumb-and-index-finger pincer grasp; no numeric rate observations are available for this question. |

### CDC age 15 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-15-SE-01 · Social/Emotional · [Copies other children while playing, like taking toys out of a container when another child does](https://www.cdc.gov/act-early/milestones/15-months.html#copies_other) | **5** · Imitates what friends do in play, such as building towers when they do. | 11:33%; 12:51%; 13:63% | **Not estimable**; before 13m:63%; after — | not estimable | **exact** — Same imitation of another child's actions during play; tower-building and taking toys out are examples, not added requirements. |
| CDC-15-SE-05 · Social/Emotional · [Shows you affection (hugs, cuddles, or kisses you)](https://www.cdc.gov/act-early/milestones/15-months.html#shows_affection) | **308** · Expresses love to those familiar, like hugging them. | 9:46%; 10:58%; 11:72%; 12:82%; 17:90%; 18:91% | **86.80% interpolated**; before 12m:82%; after 17m:90% | consistent | **exact** — Same affection toward familiar people, including hugging. |
| CDC-15-LC-02 · Language/Communication · [Looks at a familiar object when you name it](https://www.cdc.gov/act-early/milestones/15-months.html#looks_familiar) | **27** · Looks at things or people when called by name. | 6:66%; 7:59%; 14:91%; 15:92% | **92% observed** at 15m | consistent | **close** — Same looking toward the named referent; Kinedu permits a named thing or person rather than only a familiar object. |
| CDC-15-LC-04 · Language/Communication · [Points to ask for something or to get help](https://www.cdc.gov/act-early/milestones/15-months.html#points_help) | **278** · Points to objects they want. | 10:48%; 11:67% | **Not estimable**; before 11m:67%; after — | not estimable | **exact** — Same pointing to request an object; CDC also permits a request for help. |
| CDC-15-CO-02 · Cognitive · [Stacks at least two small objects, like blocks](https://www.cdc.gov/act-early/milestones/15-months.html#stacks_small) | **179** · Stacks two or more blocks to make a tower. | 14:42%; 15:57% | **57% observed** at 15m | stricter/later | **exact** — Both set the same minimum of two stacked objects/blocks. |
| CDC-15-MP-01 · Movement/Physical · [Takes a few steps on his own](https://www.cdc.gov/act-early/milestones/15-months.html#takes_steps) | **16** · Takes a couple of steps on their own. | 11:43% | **Not estimable**; before 11m:43%; after — | not estimable | **exact** — Same first few independent steps; not sustained walking. |

### CDC age 18 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-18-SE-02 · Social/Emotional · [Points to show you something interesting](https://www.cdc.gov/act-early/milestones/18-months.html#points_show) | **340** · Shows you things by pointing. | 9:20%; 10:44%; 11:64%; 12:74%; 13:77%; 14:80%; 15:82%; 16:83% | **Not estimable**; before 16m:83%; after — | not estimable | **exact** — Same declarative pointing to show another person something. |
| CDC-18-SE-05 · Social/Emotional · [Helps you dress him by pushing arm through sleeve or lifting up foot](https://www.cdc.gov/act-early/milestones/18-months.html#helps_dress) | **85** · Helps with the dressing and undressing processes by moving the right body parts. | 7:86%; 8:88%; 9:70%; 10:74%; 11:80%; 12:85%; 16:95%; 17:96% | **Not estimable**; before 17m:96%; after — | not estimable | **exact** — Same active assistance with dressing by moving the appropriate body parts. |
| CDC-18-CO-02 · Cognitive · [Plays with toys in a simple way, like pushing a toy car](https://www.cdc.gov/act-early/milestones/18-months.html#plays_toys) | **310** · Moves toys with wheels. | 9:41%; 16:95% | **Not estimable**; before 16m:95%; after — | not estimable | **close** — Same simple functional toy play; moving a wheeled toy is CDC's pushing-a-car example. |
| CDC-18-MP-02 · Movement/Physical · [Scribbles](https://www.cdc.gov/act-early/milestones/18-months.html#scribbles) | **330** · Scribbles by moving their entire arm from the shoulder. | 11:44%; 12:54%; 13:61%; 14:52%; 15:63% | **Not estimable**; before 15m:63%; after — | not estimable | **exact** — Same early scribbling; Kinedu specifies the early whole-arm form, not later wrist-only drawing. |

### CDC age 24 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-24-LC-02 · Language/Communication · [Says at least two words together, like “More milk.”](https://www.cdc.gov/act-early/milestones/2-years.html#says_words) | **419** · Puts two words together to make a brief phrase, like 'more cookie'. | 21:45%; 22:54% | **Not estimable**; before 22m:54%; after — | not estimable | **exact** — Same two-word combination, with equivalent more-cookie/more-milk examples. |
| CDC-24-CO-01 · Cognitive · [Holds something in one hand while using the other hand; for example, holding a container and taking the lid off](https://www.cdc.gov/act-early/milestones/2-years.html#holds_something) | **298** · Uses both hands together to manipulate objects, like opening a box. | 7:50% | **Not estimable**; before 7m:50%; after — | not estimable | **close** — Same coordinated use of both hands to manipulate an object, illustrated by opening a box/container; Kinedu does not spell out each hand's role. |
| CDC-24-CO-02 · Cognitive · [Tries to use switches, knobs, or buttons on a toy](https://www.cdc.gov/act-early/milestones/2-years.html#tries_switches) | **633** · Turns things that spin, like toy knobs or faucets. | 15:47%; 16:60% | **Not estimable**; before 16m:60%; after — | not estimable | **exact** — Both include turning toy knobs; Kinedu also permits turning a faucet. |
| CDC-24-MP-01 · Movement/Physical · [Kicks a ball](https://www.cdc.gov/act-early/milestones/2-years.html#kicks_ball) | **528** · Kicks a ball while standing. | 10:41%; 11:56%; 14:60% | **Not estimable**; before 14m:60%; after — | not estimable | **exact** — Same basic stationary ball kick, without added aiming, running or a moving target. |
| CDC-24-MP-04 · Movement/Physical · [Eats with a spoon](https://www.cdc.gov/act-early/milestones/2-years.html#eats_spoon) | **306** · Can use a spoon independently. | 13:19%; 14:28%; 15:39%; 16:52%; 17:64%; 18:72%; 19:79%; 22:86% | **Not estimable**; before 22m:86%; after — | not estimable | **exact** — Same functional independent eating with a spoon; not merely trying to use it. |

### CDC age 30 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-30-LC-01 · Language/Communication · [Says about 50 words](https://www.cdc.gov/act-early/milestones/30-months.html#says_about) | **373** · Speaks around 50 words. | 14:3%; 25:48%; 26:53%; 27:58%; 28:60%; 29:64%; 30:67%; 33:64%; 35:66% | **67% observed** at 30m | stricter/later | **exact** — Same approximate expressive vocabulary of 50 words. |
| CDC-30-LC-02 · Language/Communication · [Says two or more words together, with one action word, like “Doggie run”](https://www.cdc.gov/act-early/milestones/30-months.html#says_more) | **696** · Combines nouns and verbs, like 'mommy go'. | 21:88%; 22:92% | **Not estimable**; before 22m:92%; after — | not estimable | **exact** — Same two-word noun-plus-verb phrase, with mommy-go/doggie-run equivalents. |
| CDC-30-LC-04 · Language/Communication · [Says words like “I,” “me,” or “we”](https://www.cdc.gov/act-early/milestones/30-months.html#says_words) | **621** · Uses words like 'I,' 'me,' and 'you'. | 26:58%; 27:55%; 28:60%; 29:64%; 30:67%; 31:68% | **67% observed** at 30m | stricter/later | **exact** — Same personal pronouns, with overlapping I/me examples. |
| CDC-30-CO-03 · Cognitive · [Follows two-step instructions like “Put the toy down and close the door.”](https://www.cdc.gov/act-early/milestones/30-months.html#follows_two) | **421** · Completes tasks with two steps, like 'Find your toy, bring it here.' | 13:34%; 14:44%; 15:57%; 22:87% | **Not estimable**; before 22m:87%; after — | not estimable | **exact** — Same two-step instruction. Both examples require two linked actions, even when Kinedu puts them in two short clauses. |
| CDC-30-CO-04 · Cognitive · [Shows he knows at least one color, like pointing to a red crayon when you ask, “Which one is red?”](https://www.cdc.gov/act-early/milestones/30-months.html#shows_color) | **398** · Points to a red object when you ask. | 0:60% | **Not estimable**; before 0m:60%; after — | not estimable | **exact** — Same requested pointing to a red object. Selecting red is one valid instance of knowing at least one color. |
| CDC-30-MP-01 · Movement/Physical · [Uses hands to twist things, like turning doorknobs or unscrewing lids](https://www.cdc.gov/act-early/milestones/30-months.html#uses_hands) | **47** · Screws and unscrews a bottle cap. | 15:44%; 16:57%; 17:68%; 18:73% | **Not estimable**; before 18m:73%; after — | not estimable | **exact** — Same manual twisting to unscrew a lid; CDC gives unscrewing lids as an example. |
| CDC-30-MP-02 · Movement/Physical · [Takes some clothes off by himself, like loose pants or an open jacket](https://www.cdc.gov/act-early/milestones/30-months.html#takes_clothes) | **609** · Knows how to take off their shoes. | 15:47%; 16:54%; 17:62%; 18:68%; 19:72%; 20:76%; 23:86%; 25:90% | **Not estimable**; before 25m:90%; after — | not estimable | **close** — Same independent removal of an item of clothing/attire; Kinedu uses shoes instead of CDC's loose-pants/open-jacket examples and specifies no fastener task. |
| CDC-30-MP-03 · Movement/Physical · [Jumps off the ground with both feet](https://www.cdc.gov/act-early/milestones/30-months.html#jumps_off) | **681** · Jumps in place with both feet. | 20:65% | **Not estimable**; before 20m:65%; after — | not estimable | **exact** — Same two-footed jump up from the ground; no forward/backward distance is required. |
| CDC-30-MP-04 · Movement/Physical · [Turns book pages, one at a time, when you read to her](https://www.cdc.gov/act-early/milestones/30-months.html#turns_pages) | **631** · Turns book pages one by one. | No numeric rates | **Not estimable**; before —; after — | not estimable | **exact** — Same turning book pages one at a time; no numeric rate observations are available for this question. |

### CDC age 36 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-36-LC-05 · Language/Communication · [Talks well enough for others to understand, most of the time](https://www.cdc.gov/act-early/milestones/3-years.html#talks_understand) | **622** · Most people understand them when they speak. | 9:45%; 10:45%; 11:45%; 16:45%; 19:45%; 20:45%; 32:64%; 33:57%; 34:55%; 35:56%; 36:58%; 37:65%; 38:64%; 39:65%; 40:69%; 41:72%; 42:72%; 43:73%; 44:78%; 45:78% | **58% observed** at 36m | stricter/later | **exact** — Same speech intelligibility to other people most of the time. |
| CDC-36-MP-01 · Movement/Physical · [Strings items together, like large beads or macaroni](https://www.cdc.gov/act-early/milestones/3-years.html#strings_items) | **558** · Inserts things like string into a small hole. | 8:27%; 9:27%; 11:27%; 12:27%; 16:27%; 17:27%; 19:27%; 32:43%; 33:49%; 34:51%; 35:57%; 36:56%; 37:57%; 38:61%; 39:63%; 40:65%; 41:66% | **56% observed** at 36m | stricter/later | **close** — Same threading action: inserting string through a hole, as in CDC's beads/macaroni. Kinedu does not require a counted chain of beads. |
| CDC-36-MP-02 · Movement/Physical · [Puts on some clothes by himself, like loose pants or a jacket](https://www.cdc.gov/act-early/milestones/3-years.html#puts_clothes) | **612** · Puts their pants on. | 8:2%; 9:1%; 11:0%; 12:4%; 15:1%; 16:1%; 17:1%; 19:3%; 32:38%; 33:43%; 34:47%; 35:51%; 36:52%; 37:57%; 38:63%; 39:65%; 40:68%; 41:70%; 42:73%; 43:75%; 44:75%; 45:78% | **52% observed** at 36m | stricter/later | **exact** — Same putting on pants independently, one of CDC's explicit examples; neither requires fastening them. |
| CDC-36-MP-03 · Movement/Physical · [Uses a fork](https://www.cdc.gov/act-early/milestones/3-years.html#uses_fork) | **675** · Feeds independently with a fork, using the whole hand. | 2:5%; 19:59%; 20:67%; 21:77%; 23:74%; 24:79%; 26:90%; 27:90%; 28:92%; 29:94%; 31:94% | **Not estimable**; before 31m:94%; after — | not estimable | **exact** — Same independent fork feeding; Kinedu's whole-hand grip adds no advanced utensil requirement. |

### CDC age 48 months

| CDC milestone and domain | Kinedu id + question | All Kinedu shares by month | Share at CDC age / nearest months | Verdict | Confidence and reason |
| --- | --- | --- | --- | --- | --- |
| CDC-48-SE-01 · Social/Emotional · [Pretends to be something else during play (teacher, superhero, dog)](https://www.cdc.gov/act-early/milestones/4-years.html#pretends_something) | **475** · Engages in pretend play, like dressing up or acting like a firefighter. | 4:3%; 26:38%; 27:44%; 28:51%; 29:58%; 36:79% | **Not estimable**; before 36m:79%; after — | not estimable | **exact** — Same pretending to be a role/character during play, with firefighter versus teacher/superhero examples. |
| CDC-48-SE-03 · Social/Emotional · [Comforts others who are hurt or sad, like hugging a crying friend](https://www.cdc.gov/act-early/milestones/4-years.html#comforts_others) | **602** · Shows empathy when they see a crying friend (e.g., will try to comfort them). | 20:64%; 21:66%; 22:69%; 23:72%; 24:74%; 25:70%; 26:76%; 27:74%; 28:76%; 30:82% | **Not estimable**; before 30m:82%; after — | not estimable | **exact** — Same active comforting of an upset person, including a crying friend; stronger than CDC's separate two-year noticing item. |
| CDC-48-LC-01 · Language/Communication · [Says sentences with four or more words](https://www.cdc.gov/act-early/milestones/4-years.html#says_four) | **617** · Talks in sentences with four to five words. | 36:75%; 37:78%; 38:80%; 39:79%; 40:85%; 41:84% | **Not estimable**; before 41m:84%; after — | not estimable | **exact** — Same minimum four-word sentence level; Kinedu describes four-to-five-word sentences. |
| CDC-48-LC-02 · Language/Communication · [Says some words from a song, story, or nursery rhyme](https://www.cdc.gov/act-early/milestones/4-years.html#says_story) | **537** · Sings a few words from a song. | 23:86%; 24:87%; 26:84%; 28:84%; 29:86%; 30:88%; 31:88%; 32:90% | **Not estimable**; before 32m:90%; after — | not estimable | **exact** — Same saying/singing a few words of a song; CDC's story/rhyme alternatives are not additional requirements. |
| CDC-48-LC-03 · Language/Communication · [Talks about at least one thing that happened during her day, like “I played soccer.”](https://www.cdc.gov/act-early/milestones/4-years.html#talks_happened) | **698** · Talks about their day. | 33:63%; 34:62%; 35:64%; 36:64%; 37:67%; 38:69%; 39:70%; 40:74%; 41:76%; 42:77%; 43:77% | **Not estimable**; before 43m:77%; after — | not estimable | **exact** — Same talking about events from one's day. |
| CDC-48-CO-01 · Cognitive · [Names a few colors of items](https://www.cdc.gov/act-early/milestones/4-years.html#names_colors) | **660** · Names two or more colors. | 5:73%; 6:73%; 27:86%; 34:86%; 35:85% | **Not estimable**; before 35m:85%; after — | not estimable | **close** — Same expressive naming of multiple colors; Kinedu specifies two or more and CDC uses the imprecise a few. |
| CDC-48-MP-02 · Movement/Physical · [Serves herself food or pours water, with adult supervision](https://www.cdc.gov/act-early/milestones/4-years.html#serves_herself) | **674** · Pours water from a pitcher into a cup with both hands. | 10:1%; 18:4%; 20:6%; 21:9%; 26:20%; 39:61%; 40:62%; 41:64%; 42:65%; 43:64%; 44:64%; 45:71%; 46:72%; 47:74%; 48:73% | **73% observed** at 48m | stricter/later | **close** — Same pouring water into a cup; Kinedu specifies a pitcher and two hands, CDC allows adult supervision. |
| CDC-48-MP-03 · Movement/Physical · [Unbuttons some buttons](https://www.cdc.gov/act-early/milestones/4-years.html#unbuttons_buttons) | **607** · Can undo a big button on their clothes. | 19:3%; 22:8%; 23:10%; 24:11%; 25:9%; 26:10%; 27:12%; 28:14%; 29:14%; 30:15%; 31:17%; 32:21%; 33:21%; 34:24%; 35:25%; 36:27%; 37:29%; 38:32%; 39:36%; 40:36%; 41:41%; 42:43%; 43:45%; 44:47%; 45:52%; 46:54%; 47:55%; 48:57% | **57% observed** at 48m | stricter/later | **close** — Same unbuttoning action; Kinedu specifies a large button, one instance of CDC's some buttons without a specified size. |

## What is observed, and what is inferred

**Observed in the API data:** Kinedu assigns 68% at nine months to shyness around strangers (186), 57% at 15 months to stacking two blocks (179), 67% at 30 months to about 50 words (373), and 58% at 36 months to being understood by most people (622). These are exact matches below the CDC floor. The recorded values establish what the API returned, not real-world prevalence. The tempting 26% vocal-response rate at four months (143) and 40% turn-taking rate at six months (23) are also observed, but their babbling-versus-any-sounds ambiguity prevents a strict comparison; they receive no verdict and do not enter the counts.

**Observed high cases:** hand-to-mouth (41) is 97% at CDC's four-month checkpoint, with 96% at two months and 98% at three months. Familiar-caregiver recognition (97, close match) is 98% at six months, with 56% at birth-month zero and 73% at one month. These are the only two >95% checkpoint flags. Earlier high hand-to-mouth values are real API observations; CDC supplies no earlier prevalence curve against which to call them inflated. Other matched items also exceed 75% before their CDC checkpoint—such as noun-plus-verb phrases (696), 88–92% at 21–22 months versus CDC's 30 months—but have no measurable checkpoint share. They cannot be assigned a checkpoint verdict.

**Interpolation assumptions:** the six estimates below connect observations separated by 4–8 months. In particular, understanding no is estimated at **74.50%**, only half a percentage point below the cutoff; that classification is fragile. No uncertainty interval is available from the API.

| CDC age | Question | Before | After | Gap (months) | Interpolated share | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 6 | 112 | 4m:68% | 9m:98% | 5 | 80.00% | consistent |
| 9 | 31 | 6m:51% | 12m:89% | 6 | 70.00% | stricter/later |
| 9 | 183 | 5m:63% | 12m:97% | 7 | 82.43% | consistent |
| 12 | 22 | 9m:63% | 13m:91% | 4 | 84.00% | consistent |
| 12 | 67 | 8m:57% | 16m:92% | 8 | 74.50% | stricter/later |
| 15 | 308 | 12m:82% | 17m:90% | 5 | 86.80% | consistent |

**Inference about how parents look:** if `rate` is the proportion of children already achieving the skill, then a lower expected share generally makes a given child's achievements look more advanced. The checkpoint subset therefore leans **ahead**, especially in the usable older language and motor comparisons. Early-age comparisons are mixed, and many later checkpoints are missing. The data do not establish a systematic pattern of inflated shares designed to make parents feel behind.

**What this cannot establish:** the meaning of `rate` remains our interpretation, not a verified Kinedu definition or a documented population dataset. CDC's thresholds mix published evidence with expert placement and are not exact norms for estimating inflation. Population, wording and reporting conditions could differ. The 71 semantic pairs are selected from 408 questions, and only 20/71 have a usable checkpoint value; these are not a random, independent sample. The comparison does not reconstruct or measure a parent's final AQ score. Consequently, “lower than CDC's floor in this subset” is supported; “dishonest,” “universally deflated,” or “all babies will look ahead” is not.

## Unmatched CDC milestones

**73 of 144** CDC milestones lack a strict counterpart. This includes 66 with only loose candidates and seven without a relevant candidate. They are distinct from the 51 matched pairs with missing checkpoint rates. All rejected candidates below have confidence **loose**, receive no rate verdict, and are excluded from summaries; “none” means no candidate. The full CDC sentences are retained so omissions can be reviewed.

### Unmatched at 2 months

- **Social/Emotional · CDC-02-SE-03** — [Seems happy to see you when you walk up to her](https://www.cdc.gov/act-early/milestones/2-months.html#seemsHappy). Rejected: loose candidates 252. Smiling/talking with familiar people does not require a happy reaction when someone approaches.
- **Language/Communication · CDC-02-LC-01** — [Makes sounds other than crying](https://www.cdc.gov/act-early/milestones/2-months.html#Makessoundsotherthancrying). Rejected: loose candidates 197, 247. Vowel cooing and guttural syllables are specific vocal forms; the broader any-noncry-sound threshold is not separately asked.
- **Cognitive · CDC-02-CO-02** — [Looks at a toy for several seconds](https://www.cdc.gov/act-early/milestones/2-months.html#looksToy). Rejected: loose candidates 89. Kinedu requires one minute of attention, rather than several seconds looking at a toy.
- **Movement/Physical · CDC-02-MP-02** — [Moves both arms and both legs](https://www.cdc.gov/act-early/milestones/2-months.html#Movesbotharms). Rejected: loose candidates 3, 86. Separate arm and leg items do not require movement of both arms and both legs in one question.
- **Movement/Physical · CDC-02-MP-03** — [Opens hands briefly](https://www.cdc.gov/act-early/milestones/2-months.html#openshandsbriefly). Rejected: loose candidates 146. Palm-touch-elicited opening and closing is a different task from briefly opening the hands.

### Unmatched at 4 months

- **Social/Emotional · CDC-04-SE-01** — [Smiles on his own to get your attention](https://www.cdc.gov/act-early/milestones/4-months.html#smiles_attention). Rejected: loose candidates 283, 108. A responsive eye-contact smile or a generic attention bid does not establish a spontaneous attention-seeking smile.
- **Social/Emotional · CDC-04-SE-02** — [Chuckles (not yet a full laugh) when you try to make him laugh](https://www.cdc.gov/act-early/milestones/4-months.html#chuckles_laugh). Rejected: loose candidates 112. Laughing out loud is a higher threshold than CDC's explicitly not-yet-full chuckle; paired with the six-month laugh instead.
- **Language/Communication · CDC-04-LC-02** — [Makes sounds back when you talk to him](https://www.cdc.gov/act-early/milestones/4-months.html#talk_him). Rejected: loose candidates 143. Responding with babbles has the same conversational function, but babbling may require a harder vocal form than CDC's unspecified sounds. The level cannot be equated strictly.
- **Language/Communication · CDC-04-LC-03** — [Turns head towards the sound of your voice](https://www.cdc.gov/act-early/milestones/4-months.html#turns_head). Rejected: loose candidates 145. Looking toward a noise does not specify a head turn toward a person's voice.
- **Cognitive · CDC-04-CO-01** — [If hungry, opens mouth when he sees breast or bottle](https://www.cdc.gov/act-early/milestones/4-months.html#if_hungry). Rejected: no candidate. No question specifies opening the mouth on seeing breast or bottle when hungry.
- **Movement/Physical · CDC-04-MP-01** — [Holds head steady without support when you are holding him](https://www.cdc.gov/act-early/milestones/4-months.html#holds_head). Rejected: loose candidates 30, 130, 132. Holding the head up without a specified posture is ambiguous; the other items add standing torso control or still require support.
- **Movement/Physical · CDC-04-MP-03** — [Uses his arm to swing at toys](https://www.cdc.gov/act-early/milestones/4-months.html#uses_arm). Rejected: loose candidates 153. Reaching and grasping is a more directed action than swinging the arm at a toy.

### Unmatched at 6 months

- **Social/Emotional · CDC-06-SE-02** — [Likes to look at self in a mirror](https://www.cdc.gov/act-early/milestones/6-months.html#likes_to_look). Rejected: loose candidates 95, 120. Reacting to a reflection does not establish liking to look; recognizing oneself is a different, more advanced claim.
- **Language/Communication · CDC-06-LC-01** — [Takes turns making sounds with you](https://www.cdc.gov/act-early/milestones/6-months.html#takes_turns). Rejected: loose candidates 23. Both involve vocal turn-taking, but Kinedu specifies babbling rather than any sounds. Whether that adds a phonological requirement is unknown; excluded conservatively.
- **Language/Communication · CDC-06-LC-02** — [Blows “raspberries” (sticks tongue out and blows)](https://www.cdc.gov/act-early/milestones/6-months.html#blows_raspberries). Rejected: no candidate. No raspberry/tongue-blowing question.
- **Language/Communication · CDC-06-LC-03** — [Makes squealing noises](https://www.cdc.gov/act-early/milestones/6-months.html#makes_squealing). Rejected: no candidate. No squealing question; general babbling does not specify squeals.
- **Cognitive · CDC-06-CO-03** — [Closes lips to show she doesn’t want more food](https://www.cdc.gov/act-early/milestones/6-months.html#closes_lips). Rejected: no candidate. No lip-closing refusal-of-food question.
- **Movement/Physical · CDC-06-MP-02** — [Pushes up with straight arms when on tummy](https://www.cdc.gov/act-early/milestones/6-months.html#pushes_up). Rejected: loose candidates 9, 158. Lifting the upper body or extending arms forward does not specify weight-bearing on straight arms.

### Unmatched at 9 months

- **Social/Emotional · CDC-09-SE-02** — [Shows several facial expressions, like happy, sad, angry, and surprised](https://www.cdc.gov/act-early/milestones/9-months.html#shows_several). Rejected: loose candidates 79. Likes/dislikes expressed facially do not establish CDC's wider set of several expressions.
- **Social/Emotional · CDC-09-SE-04** — [Reacts when you leave (looks, reaches for you, or cries)](https://www.cdc.gov/act-early/milestones/9-months.html#reacts_when_leave). Rejected: no candidate. No specific response-to-caregiver-departure question.
- **Social/Emotional · CDC-09-SE-05** — [Smiles or laughs when you play peek-a-boo](https://www.cdc.gov/act-early/milestones/9-months.html#smiles_laughs). Rejected: loose candidates 354, 112. Enjoying adult play or laughing generally does not specify peek-a-boo.
- **Movement/Physical · CDC-09-MP-03** — [Uses fingers to “rake” food towards himself](https://www.cdc.gov/act-early/milestones/9-months.html#uses_fingers). Rejected: loose candidates 251. Holding an object with the fingers is not the finger-raking motion that brings food toward the child.

### Unmatched at 12 months

- **Social/Emotional · CDC-12-SE-01** — [Plays games with you, like pat-a-cake](https://www.cdc.gov/act-early/milestones/1-year.html#plays_games). Rejected: loose candidates 354, 363. Enjoying play or copying a clapping gesture does not require reciprocal games such as pat-a-cake.
- **Movement/Physical · CDC-12-MP-03** — [Drinks from a cup without a lid, as you hold it](https://www.cdc.gov/act-early/milestones/1-year.html#drinks_cup). Rejected: loose candidates 103, 686. General correct cup/item use omits adult holding and lid status; one-handed drinking adds a different motor requirement.

### Unmatched at 15 months

- **Social/Emotional · CDC-15-SE-02** — [Shows you an object she likes](https://www.cdc.gov/act-early/milestones/15-months.html#shows_object). Rejected: loose candidates 340. Pointing to show is a different gesture from showing an object; the pointing question is paired with CDC's eighteen-month pointing item.
- **Social/Emotional · CDC-15-SE-03** — [Claps when excited](https://www.cdc.gov/act-early/milestones/15-months.html#claps_excited). Rejected: loose candidates 363, 338. Imitating clapping or keeping a beat does not establish spontaneous clapping when excited.
- **Social/Emotional · CDC-15-SE-04** — [Hugs stuffed doll or other toy](https://www.cdc.gov/act-early/milestones/15-months.html#hugs_doll). Rejected: loose candidates 308, 551. Affection to people and pretending to feed a doll do not require hugging a toy.
- **Language/Communication · CDC-15-LC-01** — [Tries to say one or two words besides “mama” or “dada,” like “ba” for ball or “da” for dog](https://www.cdc.gov/act-early/milestones/15-months.html#tries_say). Rejected: loose candidates 24. At least one meaningful word can include a parent name; Kinedu does not state CDC's besides-mama/dada exclusion.
- **Language/Communication · CDC-15-LC-03** — [Follows directions given with both a gesture and words. For example, he gives you a toy when you hold out your hand and say, “Give me the toy.”](https://www.cdc.gov/act-early/milestones/15-months.html#follows_directions). Rejected: loose candidates 258, 19. Giving an object on request/one-step instructions leave gesture support unspecified; CDC explicitly provides both a gesture and words.
- **Cognitive · CDC-15-CO-01** — [Tries to use things the right way, like a phone, cup, or book](https://www.cdc.gov/act-early/milestones/15-months.html#tries_use). Rejected: loose candidates 103. Can correctly use everyday items is a success criterion; CDC only requires trying to use them appropriately.
- **Movement/Physical · CDC-15-MP-02** — [Uses fingers to feed herself some food](https://www.cdc.gov/act-early/milestones/15-months.html#uses_fingers). Rejected: loose candidates 476. Independent feeding with or without utensils does not establish feeding with fingers specifically.

### Unmatched at 18 months

- **Social/Emotional · CDC-18-SE-01** — [Moves away from you, but looks to make sure you are close by](https://www.cdc.gov/act-early/milestones/18-months.html#moves_away). Rejected: loose candidates 461. Exploration near a caregiver omits looking back to check the caregiver's location.
- **Social/Emotional · CDC-18-SE-03** — [Puts hands out for you to wash them](https://www.cdc.gov/act-early/milestones/18-months.html#puts_hands). Rejected: no candidate. No offering-hands-for-washing question.
- **Social/Emotional · CDC-18-SE-04** — [Looks at a few pages in a book with you](https://www.cdc.gov/act-early/milestones/18-months.html#looks_pages). Rejected: loose candidates 436. Sustained attention for a few minutes while an adult reads is not the same minimal shared-looking-at-a-few-pages threshold.
- **Language/Communication · CDC-18-LC-01** — [Tries to say three or more words besides “mama” or “dada”](https://www.cdc.gov/act-early/milestones/18-months.html#tries_words). Rejected: loose candidates 375, 32. Four words total or three named objects do not unambiguously require three words besides parent names.
- **Language/Communication · CDC-18-LC-02** — [Follows one-step directions without any gestures, like giving you the toy when you say, “Give it to me.”](https://www.cdc.gov/act-early/milestones/18-months.html#follows_directions). Rejected: loose candidates 19, 258. Kinedu does not explicitly rule out gesture cues; CDC's no-gesture requirement materially affects difficulty.
- **Cognitive · CDC-18-CO-01** — [Copies you doing chores, like sweeping with a broom](https://www.cdc.gov/act-early/milestones/18-months.html#copies_chores). Rejected: loose candidates 241, 464. Helping with chores need not be imitation; general family imitation need not involve chores.
- **Movement/Physical · CDC-18-MP-01** — [Walks without holding on to anyone or anything](https://www.cdc.gov/act-early/milestones/18-months.html#walks_without). Rejected: loose candidates 16, 415, 309. A few first unsteady steps are earlier than established walking; walking while carrying a toy adds a task. No plain sustained-walking counterpart.
- **Movement/Physical · CDC-18-MP-03** — [Drinks from a cup without a lid and may spill sometimes](https://www.cdc.gov/act-early/milestones/18-months.html#drinks_cup). Rejected: loose candidates 686, 103. One-handed cup drinking adds a motor constraint; general everyday-item use omits the open-cup and assistance conditions.
- **Movement/Physical · CDC-18-MP-04** — [Feeds himself with his fingers](https://www.cdc.gov/act-early/milestones/18-months.html#feeds_himself). Rejected: loose candidates 476. The question permits utensil feeding and does not require fingers.
- **Movement/Physical · CDC-18-MP-05** — [Tries to use a spoon](https://www.cdc.gov/act-early/milestones/18-months.html#tries_spoon). Rejected: loose candidates 306. Independent successful spoon use is harder than trying; paired with CDC's two-year spoon-eating item instead.
- **Movement/Physical · CDC-18-MP-06** — [Climbs on and off a couch or chair without help](https://www.cdc.gov/act-early/milestones/18-months.html#climbs_couch). Rejected: loose candidates 641, 39. Sitting in a small chair or climbing generally does not require independently climbing both on and off furniture.

### Unmatched at 24 months

- **Social/Emotional · CDC-24-SE-01** — [Notices when others are hurt or upset, like pausing or looking sad when someone is crying](https://www.cdc.gov/act-early/milestones/2-years.html#notices_others). Rejected: loose candidates 602. Actively comforting an upset person is a higher threshold than merely noticing; paired with CDC's four-year comforting item.
- **Social/Emotional · CDC-24-SE-02** — [Looks at your face to see how to react in a new situation](https://www.cdc.gov/act-early/milestones/2-years.html). Rejected: loose candidates 26, 240. Looking at faces does not establish using another person's expression to guide a response to a new situation.
- **Language/Communication · CDC-24-LC-01** — [Points to things in a book when you ask, like “Where is the bear?”](https://www.cdc.gov/act-early/milestones/2-years.html#points_things). Rejected: loose candidates 627, 478. Matching items to pictures or identifying story characters omits the requested pointing response to a named book picture.
- **Language/Communication · CDC-24-LC-03** — [Points to at least two body parts when you ask him to show you](https://www.cdc.gov/act-early/milestones/2-years.html#points_body). Rejected: loose candidates 307, 573, 702. One pointed body part is too few; naming three or smaller parts uses a different response and higher threshold.
- **Language/Communication · CDC-24-LC-04** — [Uses more gestures than just waving and pointing, like blowing a kiss or nodding yes](https://www.cdc.gov/act-early/milestones/2-years.html#uses_gestures). Rejected: loose candidates 189, 363. Gesture imitation can be only waves/points; CDC requires additional communicative gestures.
- **Cognitive · CDC-24-CO-03** — [Plays with more than one toy at the same time, like putting toy food on a toy plate](https://www.cdc.gov/act-early/milestones/2-years.html#plays_toys). Rejected: loose candidates 329, 551. Pretend feeding does not explicitly require coordinating two toys; neither question specifies CDC's multi-toy action.
- **Movement/Physical · CDC-24-MP-02** — [Runs](https://www.cdc.gov/act-early/milestones/2-years.html#runs). Rejected: loose candidates 637, 727, 726. Similar-to-running acceleration is ambiguous; directed running or confident running across surfaces adds requirements.
- **Movement/Physical · CDC-24-MP-03** — [Walks (not climbs) up a few stairs with or without help](https://www.cdc.gov/act-early/milestones/2-years.html#walks_climbs). Rejected: loose candidates 639, 676, 72. Alternating feet or no hand support is harder; crawling stairs is a different action. No basic stair-walking question at the same level.

### Unmatched at 30 months

- **Social/Emotional · CDC-30-SE-01** — [Plays next to other children and sometimes plays with them](https://www.cdc.gov/act-early/milestones/30-months.html#plays_next). Rejected: loose candidates 1147, 454. Parallel play explicitly without interaction misses sometimes playing together; general social play omits the combined pattern.
- **Social/Emotional · CDC-30-SE-02** — [Shows you what she can do by saying, “Look at me!”](https://www.cdc.gov/act-early/milestones/30-months.html#shows_saying). Rejected: loose candidates 108. Attention-seeking sounds/actions do not require verbally showing one's achievement with a look-at-me statement.
- **Social/Emotional · CDC-30-SE-03** — [Follows simple routines when told, like helping to pick up toys when you say, “It’s clean-up time.”](https://www.cdc.gov/act-early/milestones/30-months.html#follows_simple). Rejected: loose candidates 241, 148. Chore participation or rule understanding does not require following a familiar routine after a spoken cue.
- **Language/Communication · CDC-30-LC-03** — [Names things in a book when you point and ask, “What is this?”](https://www.cdc.gov/act-early/milestones/30-months.html#names_things). Rejected: loose candidates 437, 614. Naming familiar/everyday objects does not specify naming a book picture after a pointed what-is-this prompt.
- **Cognitive · CDC-30-CO-01** — [Uses things to pretend, like feeding a block to a doll as if it were food](https://www.cdc.gov/act-early/milestones/30-months.html#uses_things). Rejected: loose candidates 329, 551, 707. Generic make-believe, feeding a doll, or making toys talk does not require object substitution, such as a block standing for food.
- **Cognitive · CDC-30-CO-02** — [Shows simple problem-solving skills, like standing on a small stool to reach something](https://www.cdc.gov/act-early/milestones/30-months.html#shows_problem). Rejected: loose candidates 185. Moving an obstacle to reach something is not the same means-to-an-end level as using a stool/tool to extend one's reach.

### Unmatched at 36 months

- **Social/Emotional · CDC-36-SE-01** — [Calms down within 10 minutes after you leave her, like at a childcare drop off](https://www.cdc.gov/act-early/milestones/3-years.html#calms_leave). Rejected: loose candidates 122. Calming to a voice does not require independent recovery within ten minutes after separation.
- **Social/Emotional · CDC-36-SE-02** — [Notices other children and joins them to play](https://www.cdc.gov/act-early/milestones/3-years.html#notices_children). Rejected: loose candidates 454, 648. Enjoying/prefering play with peers does not explicitly require noticing and joining them.
- **Language/Communication · CDC-36-LC-01** — [Talks with you in conversation using at least two back-and-forth exchanges](https://www.cdc.gov/act-early/milestones/3-years.html#talks_you). Rejected: loose candidates 623, 699. A count of sentences is not a count of reciprocal conversational exchanges; the turn-taking threshold is unspecified.
- **Language/Communication · CDC-36-LC-02** — [Asks “who,” “what,” “where,” or “why” questions, like “Where is mommy/daddy?”](https://www.cdc.gov/act-early/milestones/3-years.html#asks_who). Rejected: loose candidates 700. Answering who/what/where questions is a different behavior from asking them.
- **Language/Communication · CDC-36-LC-03** — [Says what action is happening in a picture or book when asked, like “running,” “eating,” or “playing”](https://www.cdc.gov/act-early/milestones/3-years.html#says_running). Rejected: loose candidates 703. Receptively understanding action words is different from expressively naming a pictured action.
- **Language/Communication · CDC-36-LC-04** — [Says first name, when asked](https://www.cdc.gov/act-early/milestones/3-years.html#says_name). Rejected: loose candidates 618, 658. Name plus age/gender or first-and-last name adds requirements to CDC's first name alone.
- **Cognitive · CDC-36-CO-01** — [Draws a circle, when you show him how](https://www.cdc.gov/act-early/milestones/3-years.html#draws_circle). Rejected: loose candidates 519. Circular scribbling does not require an intentional closed circle copied after demonstration.
- **Cognitive · CDC-36-CO-02** — [Avoids touching hot objects, like a stove, when you warn her](https://www.cdc.gov/act-early/milestones/3-years.html#avoids_touching). Rejected: loose candidates 243. Reacting differently to hot/cold things does not require avoiding a hot object after a warning.

### Unmatched at 48 months

- **Social/Emotional · CDC-48-SE-02** — [Asks to go play with children if none are around, like “Can I play with Alex?”](https://www.cdc.gov/act-early/milestones/4-years.html#asks_children). Rejected: loose candidates 648, 694, 619. Preferring peers or naming friends does not require asking to play with an absent child.
- **Social/Emotional · CDC-48-SE-04** — [Avoids danger, like not jumping from tall heights at the playground](https://www.cdc.gov/act-early/milestones/4-years.html#avoids_danger). Rejected: no candidate. No danger-avoidance question at this level.
- **Social/Emotional · CDC-48-SE-05** — [Likes to be a “helper”](https://www.cdc.gov/act-early/milestones/4-years.html#likes_helper). Rejected: loose candidates 241. Actually helping with chores does not specifically measure liking the helper role.
- **Social/Emotional · CDC-48-SE-06** — [Changes behavior based on where she is (place of worship, library, playground)](https://www.cdc.gov/act-early/milestones/4-years.html#changes_behavior). Rejected: loose candidates 569. Adjusting voice volume is one narrow part of behavior; the question does not require broader setting-dependent behavior.
- **Language/Communication · CDC-48-LC-04** — [Answers simple questions like “What is a coat for?” or “What is a crayon for?”](https://www.cdc.gov/act-early/milestones/4-years.html#answers_questions). Rejected: loose candidates 574, 564. Knowing body-part functions or answering a color question does not ask about everyday objects' purposes.
- **Cognitive · CDC-48-CO-02** — [Tells what comes next in a well-known story](https://www.cdc.gov/act-early/milestones/4-years.html#tells_story). Rejected: loose candidates 524, 664. Filling a familiar line's blank or recalling yesterday's story does not necessarily predict the next event in a known story.
- **Cognitive · CDC-48-CO-03** — [Draws a person with three or more body parts](https://www.cdc.gov/act-early/milestones/4-years.html#draws_person). Rejected: loose candidates 704. Naming/describing a drawing does not require a person with three body parts.
- **Movement/Physical · CDC-48-MP-01** — [Catches a large ball most of the time](https://www.cdc.gov/act-early/milestones/4-years.html#catches_ball). Rejected: loose candidates 717, 718, 672. Catching a large ball while steady, hands-only catching, or catching a bounced ball does not establish CDC's most-of-the-time reliability at the same task.
- **Movement/Physical · CDC-48-MP-04** — [Holds crayon or pencil between fingers and thumb (not a fist)](https://www.cdc.gov/act-early/milestones/4-years.html#holds_fingers). Rejected: loose candidates 377. A whole-hand crayon grip is the opposite of CDC's specified finger-and-thumb grip.

## Reproduction

Run `python3 scripts/extract_cdc_milestones.py` then `python3 scripts/build_cdc_comparison.py` from this folder. Both operate offline on the saved HTML, curated match decisions and Kinedu CSV; they perform no network calls. [comparison-summary.json](raw/cdc/comparison-summary.json) contains the summary counts and medians, and [comparison-validation.json](raw/cdc/comparison-validation.json) records input hashes and coverage/rate checks.

## 12-line summary

1. CDC's 2022 framework places milestones where about 75% or more are expected to do them.
2. All 11 requested checklists were saved through the proxy; 144 milestone sentences were extracted.
3. There are 71 retained pairs: 53 exact and 18 close; loose candidates are excluded.
4. Seventy-three CDC milestones have no strict Kinedu counterpart.
5. Only 14 pairs have an observed rate at the CDC age; six more permit interpolation.
6. Fifty-one matched pairs have no estimable checkpoint rate; none was extrapolated.
7. Of 20 numeric pairs, 11 are 50–<75% and none is below 50%.
8. Seven are 75–95%; two exceed 95%, which remains compatible with CDC's floor.
9. The overall median is 73.75%; the directly observed median is 67.50%.
10. Exact, observed matches alone still lean low: six of nine below 75%, with a 67% median.
11. Conditional on the rate interpretation, this subset tends to make children look ahead, not behind.
12. Sparse coverage, uncertain rate meaning and CDC's floor prevent bank-wide or dishonesty claims.
