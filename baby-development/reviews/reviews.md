# App and book reviews — RV1 ledger (2026-10-25)

Reader RV1, brief `../../_shared/_tools/brief-books-apps.md`. Voice file `voice/reviews-rv1.jsonl` (ids `dvr1-0001`–`dvr1-0164`): **164 verbatim quotes from 182 complete review units, all 182 read in full; 130 units gave at least one quote, 52 none.** `python3 -I _tools/verify_quotes.py voice/reviews-rv1.jsonl` → `164 quotes, 0 failed`. Unit-by-unit read status and quote ids: `_raw/reviews/reading-ledger-rv1.tsv`. 19 quote ids are restricted (below). Quotes are from selected reviewers, not a sample of buyers. Apple, Google and Yotpo choose which reviews show. No purchases, no sign-ups, no logins. Blocks and empty pages: `reviews-not-harvested.md`.

## Method

Collectors copied from `../toddler-behaviour/_tools/` into `_tools/` and adapted. They refuse to overwrite a capture or corpus.
- **App Store:** `_tools/collect_app_reviews.py`. Each app has its own storefront list: Kinedu, BabySparks and The Wonder Weeks get **ca + au only**, because global/ holds us + gb. Every other app gets us/gb/ca/au. Public route `https://apps.apple.com/<cc>/app/<slug>/id<id>?see-all=reviews`, which returns at most 10 units per storefront. Raw HTML, headers, `*-reviews.units.json` and frozen `*-corpus.txt` are in `_raw/reviews/`. No Kinedu/BabySparks/Wonder Weeks unit duplicates a global/ unit (checked by id and text).
- **Google Play:** each detail page fetched once (`?id=<pkg>&hl=en_US&gl=US`) and saved as `_raw/reviews/_html/googleplay-<app>.html`. `_tools/extract_play_reviews.py` froze the 3 exposed bodies into `_raw/reviews/googleplay-<app>.txt`. Reviewer names are dropped; developer replies are kept and marked. Kinedu, BabySparks, Pathways and CDC were skipped because global/ already holds their Play pages.
- **Barnes & Noble:** `_tools/collect_barnes_reviews.py` follows the robots-permitted product route `/w/?ean=` to the page's Yotpo product ids, then to the public `api-cdn.yotpo.com/v3/storefront/store/<key>/product/<id>/reviews` list.
- **Apple Books:** `_tools/collect_apple_books.py` uses `books.apple.com/us/book/isbn<EAN>` to find the book's id, then fetches the same id in gb/ca/au. For The Montessori Baby, The Wonder Weeks and The Simplest Baby Book, the script (`KNOWN`) takes the US id from `global/_raw/books/*.txt` and fetches only gb/ca/au. What to Expect the First Year had no Apple Books page in global/, so its us page is new.
- The Whole-Brain Child was skipped (toddler-behaviour has it). ISBNs came from publisher, library and retailer pages found by web search. None were guessed.

## Ledger

| Source | Units saved | Read | Quotes |
|---|---:|---:|---:|
| App Store Kinedu (id741277284), ca 10, au 10 | 20 | 20 | 21 |
| App Store BabySparks (id794574199), ca 10, au 10 | 20 | 20 | 17 |
| App Store The Wonder Weeks (id529815782), ca 10, au 10 | 20 | 20 | 23 |
| App Store Pathways.org (id1630421307), us 10, gb 4, ca 5, au 2 | 21 | 21 | 13 |
| App Store CDC's Milestone Tracker (id1232718688), us 10, gb 2, ca 4, au 2 | 18 | 18 | 16 |
| App Store Lovevery (id1556748552), us 10, gb 3, ca 5, au 0 | 18 | 18 | 20 |
| App Store Bloomie (id6787718356), us 3, gb 6, ca 1, au 1 | 11 | 11 | 10 |
| App Store Little Steps (id1210116232), us 2, gb 1, ca/au 0 | 3 | 3 | 2 |
| App Store Sprouty (id1662980687), us/gb/ca/au 10 each | 40 | 40 | 30 |
| App Store BabyDone (id6770622579), RealPlay (id6749885609), all storefronts | 0 | 0 | 0 |
| Google Play The Wonder Weeks (org.twisevictory.apps.ex) | 3 | 3 | 5 |
| Google Play Sprouty (happy.mom.android) | 3 | 3 | 2 |
| Google Play Lovevery, Bloomie, Little Steps | not found | — | — |
| Barnes & Noble The Wonder Weeks (pb + ebook, one shared review) | 1 | 1 | 2 |
| Barnes & Noble Brain Rules for Baby, Your Baby's First Year (AAP), The Montessori Toddler, How to Raise an Amazing Child the Montessori Way, What to Expect the First Year | 0 | 0 | 0 |
| Barnes & Noble Baby Play (Gymboree) | 404 | — | — |
| Apple Books Brain Rules for Baby (id861741153), us 2 | 2 | 2 | 1 |
| Apple Books The Montessori Baby (id6443052178), ca 1 | 1 | 1 | 1 |
| Apple Books What to Expect the First Year (id6443120813), us 1 | 1 | 1 | 1 |
| Apple Books The Montessori Toddler, The Wonder Weeks gb/ca, The Simplest Baby Book gb/ca/au | 0 | 0 | 0 |
| **Total** | **182** | **182** | **164** |

By class: App Store 171 units / 152 quotes; Google Play 6 / 7; Barnes & Noble 1 / 2; Apple Books 4 / 3. The 52 units read and not quoted were one-line praise, bug reports with nothing beyond the bug, two French-language Sprouty reviews (ca), a CDC review about breastfeeding resources, a pronoun-setting review, and parts already covered by another quote.

**Books are thin.** B&N's Yotpo lists and Apple's visible reviews give 5 book units across 9 titles. For this niche, books add almost nothing on these routes. Apple Books shows star counts with no text (Montessori Toddler us: 14 ratings, 0 written reviews).

## Quote notes

- Speaker is always `reviewer`; no names. Developer replies that address reviewers by first name were not quoted. Stage is `unknown` unless the review gives the child's age.
- Themes added beyond the README seeds: `cancellation` (trial→charge, refunds, losing access after cancelling), `review_incentive` (a review solicited or rewarded), `leaps`, `partner` (sharing the app with a second caregiver), `skeptic`, `grandparent_buyer`.
- **Review independence.** Kinedu offered an e-book for a review (dvr1-0007). A Bloomie reviewer writes "They told me to write review once" (dvr1-0119). Bloomie's 5-star reviews all fall in Aug–Oct 2026, just after launch. Pathways us/ca/au 5-star reviews cluster on 7–15 Aug 2023. Two Lovevery 5-star reviews fall on the app's launch day (28 Oct 2021). Each context says so where it applies.
- Several 5-star Pathways/BabySparks/CDC reviews come from people who say they are professionals (home visitor, paediatric PT, early intervention therapist, family doctor, Ages and Stages assessor). Their role is self-described and unverified.

## Restricted ids

Research only, never in ads (README lines not to cross: no condition names, no delay/"behind" or milestone-worry framing, no earlier-milestone promises, referral questions not used as hooks):

| id | unit | why |
|---|---|---|
| dvr1-0023 | `babysparks-ca-12928527708` | milestone-worry frame |
| dvr1-0025 | `babysparks-ca-12203933919` | names premature birth (medical) |
| dvr1-0029 | `babysparks-au-9597810721` | ahead-of-age result credited to the app (earlier-milestone promise) |
| dvr1-0031 | `babysparks-au-5648176042` | referral/extra-support frame |
| dvr1-0038 | `babysparks-au-7887318009` | review names a condition, delays and disability |
| dvr1-0052 | `wonderweeks-au-12628149796` | names premature birth (medical) |
| dvr1-0076 | `cdc-us-6205150601` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0077 | `cdc-us-6205150601` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0078 | `cdc-us-6205150601` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0079 | `cdc-us-11615938831` | names preterm birth (medical) |
| dvr1-0081 | `cdc-us-9506559576` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0083 | `cdc-us-12828098300` | doctor-concerns frame |
| dvr1-0086 | `cdc-ca-7392383180` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0088 | `cdc-ca-6945134204` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0089 | `cdc-ca-6945134204` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0099 | `lovevery-us-10522019637` | milestone-worry frame (missing/delayed milestones, evaluation) |
| dvr1-0120 | `bloomie-au-14639425612` | review names neonatal intensive care and a struggling baby (medical) |
| dvr1-0146 | `sprouty-au-14412818263` | review names a premature baby (medical) |
| dvr1-0149 | `sprouty-au-14227192500` | names preterm birth (medical) |

The pattern behind the CDC and BabySparks restricted quotes can be described: checklists that flag "not yet" answers and push evaluation are what reviewers call stressful or worry-making. Those quotes may not be used as hooks.

## What the reviews add that Reddit did not (interpretation, from the ids)

1. **Real paid-app buying, and how it goes wrong.** Reddit has no development-app purchase. Here, people are charged after trials (dvr1-0001, dvr1-0013, dvr1-0015, dvr1-0139) and pay CA$100 / $109 a year. Sprouty puts its paywall after a long questionnaire (dvr1-0137, dvr1-0138, dvr1-0141, dvr1-0142). After cancelling, Lovevery cut off the activity notes for kits already bought (dvr1-0097), and Sprouty locked the milestone dates a parent had logged (dvr1-0129).
2. **People ask for a one-off price.** "I would absolutely have paid a one time cost", against "information published in a $10 book" (dvr1-0156, dvr1-0157). "I'm not interested in paying for your content twice" (dvr1-0155). "I only intend on using it for a few months" (dvr1-0125). Lifetime buyers are the happy ones (dvr1-0037).
3. **"Personalised" breaks in practice.** Milestone inputs do not change the activities: a 14-month-old who is running is still offered sitting (dvr1-0008, dvr1-0009); suggestions look random (dvr1-0026); the age is a month out (dvr1-0020); the content reads as "generic and seems AI-generated" (dvr1-0136). Praise goes to the opposite: "instead of just assuming all 10 month olds are the same" (dvr1-0030), "The answers are not generic" (dvr1-0107).
4. **What 4–5★ reviewers pay for is reassurance and "what do I do with him".** Leaps explain fussiness: "know it is just a phase" (dvr1-0134, dvr1-0040, dvr1-0056). Parents say they were "clueless on things to do with my baby" (dvr1-0071) and that "It gets exhausting thinking of new activities" (dvr1-0098). One app "help[s] to sift through" the overload (dvr1-0061). The free Pathways app is pushed over paid apps, even by professionals (dvr1-0068, dvr1-0069).
5. **Format objections a document answers.** Video-led activities don't work for a no-screens family (dvr1-0010). Bright redesigns pull the baby to the screen (dvr1-0143). Parents have to pay extra so a partner can see the same plan (dvr1-0130, dvr1-0145, dvr1-0148), and tracking at 3am is hard work (dvr1-0126).

## How to continue

Don't re-run the collectors on names they have already captured; they refuse. Still worth trying:
- Lovevery's Google Play package id, from a browser walk of its onelink.
- gb/au Apple Books edition ids for Montessori Baby, Wonder Weeks, What to Expect and Montessori Toddler.
- An ebook ISBN for the AAP's *Your Baby's First Year*.
- Kinedu's and BabySparks' own review widgets, if they have any.
