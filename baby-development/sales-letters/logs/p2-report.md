# Phase 2 — archived sales-letter fetch report

Run date: 2026-11-03. Read the sales-letter README, both candidate TSVs and both Phase 1 reports.

**Result: 12 confirmed target letters, each with at least two qualifying captures from different years: 3 core development/play, 4 early-learning or infant-activity adjacent, and 5 sleep-adjacent.** 32 qualifying target captures saved. One further therapeutic/older-child letter has two qualifying-format captures but is excluded from the target count. 83 text captures across 37 fetched slugs are preserved, including rejected landings and extraction failures. No remaining Wayback work was performed after confirming the twelve-letter stopping condition.

## Request accounting and method

- **136 of 220 requests used: 53 CDX calls + 83 capture fetches.** Audit contains 136 request events, 135 response events (133 HTTP 200, two HTTP 503), one transport/read-timeout error, zero followed redirects and zero retry attempts. All 83 saved fetch headers are HTTP 200; HTTP success does not imply a usable letter.
- All archive traffic used `python3 -I _tools/wayback.py` over HTTPS; no live seller pages were fetched. The helper’s shared four-second request-start throttle remained active. A run-specific request log and hard cap were set before the first request. One attempt per invocation bounded failed lookups; failed CDX results are distinguished from successful empty results.
- **Process deviation:** the slow Active Babies sales-path CDX invocation briefly overlapped the following Play, Develop, Thrive CDX invocation before a whole-process lock was added. This violated the no-two-copies rule despite the helper’s shared request-start throttle. Both requests are included in the 136 total. All subsequent helper invocations were serialized with the whole-process lock. No live-site request resulted.
- Followed the ranked core queue, then early-learning queue, then ranked sleep queue. After these were exhausted, used remaining Phase 1 candidates: Teach Baby To Swim, two Montessori offers, Baby Acrobatics, Massage for Happy Babies, Magic Lullabies, Instant Baby Sleep and The Baby Sleep Site’s archive-linked Mastering Naps offer. Stopped at twelve; the last-priority app/physical-kit landings were not fetched.
- CDX window 2005–2024, limit 40, HTML filter. Exact histories normally collapsed by calendar year so early captures did not crowd out later years; path discovery used prefix matching and URL-key collapse where appropriate. CDX index rows are not page word counts. Captures use exact timestamp/original-URL pairs.
- Maximum four fetches per letter/slug. A short first page generally received one other year or linked path. Montessori Babies Course has only 2023 and 2024 capture years in the queried window, so two captures rather than a third year. Several other offers have three or four saved attempts but only two qualify. The unresolved-offer probe had its stricter six-request stop.
- Raw captures were never edited or overwritten. One 2023 Play, Develop, Thrive response was gzip-compressed and originally decoded as garbage (header says 585 words, not a meaningful count). Added gzip decoding to the helper’s text/link extraction, verified locally against plain HTML, and saved a separate March 2023 capture as its fourth attempt. Original raw text and served payload remain unchanged.
- `WORDS` below is the immutable helper total, not an asserted clean-body count. Qualification removes menus, footers, platform controls, blog/catalogue material and auto customer-review lists. Seller-written feature/curriculum lists and selected testimonial proof within a coherent sales letter count as body. Baby Sign Language Deluxe was rejected despite 5,109 total words because only 1,039 are seller description/guarantee. Montessori Babies Course retains 1,329 / 1,496 meaningful sales words after conservative cleanup. Sleep Baby Sleep 2006/07 retains 1,467 / 1,364 after removing the embedded nap-tip section.
- Price means what the saved text says in that year. Currency signs are preserved; no inferred current prices. Hidden HTML checkout values are not substituted for visible text prices. Captures show versions, not proof of split tests, purchases, sales volume or efficacy. Claims are preserved for Phase 3 tagging, not endorsed.

Evidence: [HTTP audit](p2-wayback-requests.jsonl), [command log](p2-commands.jsonl), [CDX results](p2-cdx/), [run state](p2-run-state.json), [capture inventory](p2-captures.tsv), [classification](p2-classification.json), [independent local evidence review](p2-evidence-review.md), [raw checksums](p2-raw-sha256.txt), [local validation](p2-validation.json), and [append-only source ledger](../../sources/sales-letters.md).

Local validation passed for every capture: raw header/body word counts, ledger fields, exact replay timestamps, raw hashes, report links, request totals, the four-capture limit, two qualifying years per target and the five-letter sleep cap.

## Confirmed target letters

Capture-level `yes` means that saved version qualifies; `landing`/`no` attempts do not contribute to the two-year minimum. Slug rows count offers once.

| Slug / product | Letter? / fit | Captures saved: filename — year, helper words, verdict | Price seen | Description / guarantee |
|---|---|---|---|---|
| `baby-milestones` — A Practical Guide to Baby Milestones | yes / core | [baby-milestones--20100117074328.txt](../../_raw/sales-letters/baby-milestones--20100117074328.txt) — 2010, 1,359 words, **yes**<br>[baby-milestones--20130131124554.txt](../../_raw/sales-letters/baby-milestones--20130131124554.txt) — 2013, 1,373 words, **yes**<br>[baby-milestones--20160114023855.txt](../../_raw/sales-letters/baby-milestones--20160114023855.txt) — 2016, 1,373 words, **yes** | 2010 $10; 2013/16 $14.70 | 0–24-month milestone ebook; changed headline and price; 8-week/56-day refund. |
| `play-develop-thrive` — Play, Develop, Thrive / Bright Beginnings | yes / core | [play-develop-thrive--20220926061658.txt](../../_raw/sales-letters/play-develop-thrive--20220926061658.txt) — 2022, 2,574 words, **yes**<br>[play-develop-thrive--20230301115112.txt](../../_raw/sales-letters/play-develop-thrive--20230301115112.txt) — 2023, 585 words, **no**<br>[play-develop-thrive--20230322062000.txt](../../_raw/sales-letters/play-develop-thrive--20230322062000.txt) — 2023, 2,278 words, **yes**<br>[play-develop-thrive--20240421112446.txt](../../_raw/sales-letters/play-develop-thrive--20240421112446.txt) — 2024, 2,278 words, **yes** | Buy/join CTA; numeric price absent | Infant care/play/development course; 30-day refund. 2022 FAQ says 0–6 months despite 12-month headline; later copy says 0–12. One gzip extraction failed. |
| `childs-genius` — How to Develop Your Child’s Genius | yes / adjacent | [childs-genius--20080112011131.txt](../../_raw/sales-letters/childs-genius--20080112011131.txt) — 2008, 1,859 words, **yes**<br>[childs-genius--20100123001342.txt](../../_raw/sales-letters/childs-genius--20100123001342.txt) — 2010, 1,951 words, **yes**<br>[childs-genius--20120126082931.txt](../../_raw/sales-letters/childs-genius--20120126082931.txt) — 2012, 1,951 words, **yes** | $67 all years | Birth/age-two origin story through school/university giftedness; broad early-learning adjacent, not a baby-only programme; 60-day refund. |
| `children-learning-reading` — Children Learning Reading | yes / adjacent | [children-learning-reading--20120114194846.txt](../../_raw/sales-letters/children-learning-reading--20120114194846.txt) — 2012, 9,802 words, **yes**<br>[children-learning-reading--20150102045337.txt](../../_raw/sales-letters/children-learning-reading--20150102045337.txt) — 2015, 17,075 words, **yes**<br>[children-learning-reading--20180105210614.txt](../../_raw/sales-letters/children-learning-reading--20180105210614.txt) — 2018, 6,381 words, **yes** | 2012 $37 promo / $57 regular; 2015/18 $49.95 | Age-two-and-older reading programme; speaking ability required; 60-day refund. Long testimonials are integrated in the letter. |
| `signing-for-babies` — Sign Language for Babies and Beyond | yes / adjacent | [signing-for-babies--20080105074350.txt](../../_raw/sales-letters/signing-for-babies--20080105074350.txt) — 2008, 2,638 words, **yes**<br>[signing-for-babies--20120101164146.txt](../../_raw/sales-letters/signing-for-babies--20120101164146.txt) — 2012, 2,627 words, **yes**<br>[signing-for-babies--20160111012429.txt](../../_raw/sales-letters/signing-for-babies--20160111012429.txt) — 2016, 2,586 words, **yes** | 2008 $33.52; 2012/16 $15; regular $49.95 | Infant-signing ebook/video offer with 250-sign demonstration and bonuses; 60-day refund. |
| `sleep-baby-sleep` — Sleep Baby Sleep | yes / sleep | [sleep-baby-sleep--20060221101036.txt](../../_raw/sales-letters/sleep-baby-sleep--20060221101036.txt) — 2006, 1,628 words, **yes**<br>[sleep-baby-sleep--20070104173058.txt](../../_raw/sales-letters/sleep-baby-sleep--20070104173058.txt) — 2007, 1,524 words, **yes**<br>[sleep-baby-sleep--20080131132622.txt](../../_raw/sales-letters/sleep-baby-sleep--20080131132622.txt) — 2008, 956 words, **landing**<br>[sleep-baby-sleep--20120103223147.txt](../../_raw/sales-letters/sleep-baby-sleep--20120103223147.txt) — 2012, 970 words, **landing** | 2006 $29.95 ebook; 2007 price absent in text | 2006/07 long infant-sleep letters; 30-day refund; later 2008/12 roots short. Separate 2006 consultation $60/hour; not ebook price. |
| `baby-sleep-solution` — The Baby Sleep Solution | yes / sleep | [baby-sleep-solution--20080107101232.txt](../../_raw/sales-letters/baby-sleep-solution--20080107101232.txt) — 2008, 2,141 words, **yes**<br>[baby-sleep-solution--20100104140714.txt](../../_raw/sales-letters/baby-sleep-solution--20100104140714.txt) — 2010, 2,608 words, **yes**<br>[baby-sleep-solution--20120105012544.txt](../../_raw/sales-letters/baby-sleep-solution--20120105012544.txt) — 2012, 2,630 words, **yes** | 2012 $26.97; 2008/10 base price absent in text | Downloadable infant/toddler sleep-audio letter; 8-week refund. $19 refers to future extra-audio charge, not main programme. |
| `five-minute-sleep` — The Five Minute Sleep Method | yes / sleep | [five-minute-sleep--20161031080226.txt](../../_raw/sales-letters/five-minute-sleep--20161031080226.txt) — 2016, 5,032 words, **yes**<br>[five-minute-sleep--20170105120427.txt](../../_raw/sales-letters/five-minute-sleep--20170105120427.txt) — 2017, 5,032 words, **yes**<br>[five-minute-sleep--20180109175826.txt](../../_raw/sales-letters/five-minute-sleep--20180109175826.txt) — 2018, 5,081 words, **yes** | $29.99 promo / $89.99 regular | Baby/toddler downloadable sleep programme; founder story, mechanism, bonus stack; 60-day refund. |
| `teach-baby-to-swim` — Teach Baby To Swim | yes / adjacent | [teach-baby-to-swim--20140518233807.txt](../../_raw/sales-letters/teach-baby-to-swim--20140518233807.txt) — 2014, 290 words, **landing**<br>[teach-baby-to-swim--20160111232548.txt](../../_raw/sales-letters/teach-baby-to-swim--20160111232548.txt) — 2016, 3,375 words, **yes**<br>[teach-baby-to-swim--20170405031826.txt](../../_raw/sales-letters/teach-baby-to-swim--20170405031826.txt) — 2017, 3,383 words, **yes** | $37 sale / $47 anchor (2016/17); 2014 $37 | Infant motor/activity adjacent how-to; 2016/17 long letters; contradictory 30-/60-day refunds. 2014 VSL/DVD wrapper short. |
| `montessori-babies-course` — The Montessori Babies Course | yes / core | [montessori-babies-course--20230531002658.txt](../../_raw/sales-letters/montessori-babies-course--20230531002658.txt) — 2023, 1,694 words, **yes**<br>[montessori-babies-course--20240226044259.txt](../../_raw/sales-letters/montessori-babies-course--20240226044259.txt) — 2024, 1,955 words, **yes** | $252 both years | Infant Montessori environment, materials and activities; meaningful curriculum features included in body; no guarantee found. Only 2023/24 years returned. |
| `magic-lullabies` — Magic Lullabies | yes / sleep | [magic-lullabies--20110923162615.txt](../../_raw/sales-letters/magic-lullabies--20110923162615.txt) — 2011, 1,054 words, **landing**<br>[magic-lullabies--20130104183624.txt](../../_raw/sales-letters/magic-lullabies--20130104183624.txt) — 2013, 3,190 words, **yes**<br>[magic-lullabies--20140103015343.txt](../../_raw/sales-letters/magic-lullabies--20140103015343.txt) — 2014, 3,187 words, **yes** | 2013/14 $28; $47 discussed anchor | Womb-sound audio plus baby-care ebooks; full-refund promise without stated period in long versions. Earlier 2011 offer short, with 60-day promise. |
| `mastering-naps` — Mastering Naps and Schedules | yes / sleep | [mastering-naps--20100108062253.txt](../../_raw/sales-letters/mastering-naps--20100108062253.txt) — 2010, 3,338 words, **yes**<br>[mastering-naps--20110201000529.txt](../../_raw/sales-letters/mastering-naps--20110201000529.txt) — 2011, 1,840 words, **yes**<br>[mastering-naps--20140131003250.txt](../../_raw/sales-letters/mastering-naps--20140131003250.txt) — 2014, 1,965 words, **yes** | 2010 Silver $28 / Gold $39; 2011 Silver $27 / Gold $47; 2014 Silver $27 / Gold $97 | ~4 months through toddler years; standalone ebook/case study/audio Silver tier; Gold adds personal help. Refund promise, no term found. 2014 Gold expands to plan/bundle. |

## Format-qualified reference outside the target audience

| Slug / product | Letter? / fit | Captures saved | Price seen | Description |
|---|---|---|---|---|
| `help-your-child-speak` — How to Help Your Child Learn to Talk Better | yes in 2010/12; outside target | [help-your-child-speak--20100131081101.txt](../../_raw/sales-letters/help-your-child-speak--20100131081101.txt) — 2010, 3,324 words, **yes**<br>[help-your-child-speak--20120213155002.txt](../../_raw/sales-letters/help-your-child-speak--20120213155002.txt) — 2012, 3,324 words, **yes**<br>[help-your-child-speak--20160110055329.txt](../../_raw/sales-letters/help-your-child-speak--20160110055329.txt) — 2016, 167 words, **landing** | $39 (2010/12) | YES in letter format, excluded from target count: therapeutic speech-difficulty pitch explicitly for 2½–3+ years; 56-day/8-week refund. 2016 root short. |

## Captured, not qualifying letters

| Slug / product | Letter? | Captures saved | Price seen | Description |
|---|---|---|---|---|
| `babypillars` — BabyPillars | landing | [babypillars--20160504183614.txt](../../_raw/sales-letters/babypillars--20160504183614.txt) — 2016, 745 words, **landing**<br>[babypillars--20190201123302.txt](../../_raw/sales-letters/babypillars--20190201123302.txt) — 2019, 188 words, **landing** | No numeric programme price in saved text | 2016 video-programme homepage and 2019 quiz opt-in; neither is long form. Stopped after second year. |
| `active-babies` — Active Babies Smart Kids | landing | [active-babies--20160101144840.txt](../../_raw/sales-letters/active-babies--20160101144840.txt) — 2016, 3,349 words, **landing** | Free series | Free registration/video-series page; duplicate episode descriptions inflate WORDS. No paid CTA. Sales-path discovery CDX failed with 503. |
| `baby-massage` — baby-massage.com | no | [baby-massage--20110201170058.txt](../../_raw/sales-letters/baby-massage--20110201170058.txt) — 2011, 639 words, **no**<br>[baby-massage--20211126195014.txt](../../_raw/sales-letters/baby-massage--20211126195014.txt) — 2021, 574 words, **no** | No baby-offer price | Domain parking in both years. $2,910 / minimum offers are domain ownership amounts, not an infant-massage programme. |
| `milestones-motherhood` — Milestones & Motherhood | landing | [milestones-motherhood--20220414165451.txt](../../_raw/sales-letters/milestones-motherhood--20220414165451.txt) — 2022, 632 words, **landing**<br>[milestones-motherhood--20221119032454.txt](../../_raw/sales-letters/milestones-motherhood--20221119032454.txt) — 2022, 684 words, **landing** | No numeric course price in saved text | 0–36-month guide homepage and short class catalogue. Found tummy-time/roll-sit/crawling/walking ThriveCart checkout paths; not long letters. |
| `how-to-play` — How To Play With Your Baby | landing | [how-to-play--20230603182551.txt](../../_raw/sales-letters/how-to-play--20230603182551.txt) — 2023, 388 words, **landing**<br>[how-to-play--20240414015448.txt](../../_raw/sales-letters/how-to-play--20240414015448.txt) — 2024, 388 words, **landing** | $19 both years | Newborn–3-month ebook; 388-word sales landing in 2023/24; no guarantee found. |
| `your-child-development` — Your Child Development System | landing | [your-child-development--20121012022705.txt](../../_raw/sales-letters/your-child-development--20121012022705.txt) — 2012, 503 words, **landing** | No price in saved text | 503-word opt-in page confirms identity. Combined unresolved-offer probe ended at six requests; no further fetch. |
| `mommy-jingles` — Mommy Jingles Musical Parenting Program | landing | [mommy-jingles--20141013172835.txt](../../_raw/sales-letters/mommy-jingles--20141013172835.txt) — 2014, 120 words, **landing**<br>[mommy-jingles--20160204203121.txt](../../_raw/sales-letters/mommy-jingles--20160204203121.txt) — 2016, 224 words, **landing** | 2014 $47; 2016 $27 | Short video/offer wrapper for eight musical-parenting videos plus cards/lyrics/audio. |
| `your-baby-can-read` — Your Baby Can Read | landing | [your-baby-can-read--20090221201037.txt](../../_raw/sales-letters/your-baby-can-read--20090221201037.txt) — 2009, 83 words, **landing**<br>[your-baby-can-read--20120104191207.txt](../../_raw/sales-letters/your-baby-can-read--20120104191207.txt) — 2012, 263 words, **landing** | 2012 $14.95 trial + 2 × $67.50 = $149.95 before tax | 2009 image wrapper / 2012 payment disclosures; conditional 30-day return/refund; shipping/processing exclusions; not long form. |
| `little-reader` — BrillKids Little Reader | landing | [little-reader--20110113193546.txt](../../_raw/sales-letters/little-reader--20110113193546.txt) — 2011, 855 words, **landing**<br>[little-reader--20110208174417.txt](../../_raw/sales-letters/little-reader--20110208174417.txt) — 2011, 866 words, **landing** | Basic from US$149; Deluxe US$399 | Root catalogue plus /teach-reading/ sales path; 855/866 total words with large menus. Little Math US$119 is a different product. |
| `gentle-revolution` — Gentle Revolution / Doman books | landing | [gentle-revolution--20080112014029.txt](../../_raw/sales-letters/gentle-revolution--20080112014029.txt) — 2008, 157 words, **landing**<br>[gentle-revolution--20160105021216.txt](../../_raw/sales-letters/gentle-revolution--20160105021216.txt) — 2016, 356 words, **landing** | 2008 VHS liquidation $15 per listed title | Publisher/store homepages; no single long letter. 2016 links many books/courses. |
| `reading-head-start` — Reading Head Start | landing | [reading-head-start--20170713100440.txt](../../_raw/sales-letters/reading-head-start--20170713100440.txt) — 2017, 142 words, **landing**<br>[reading-head-start--20190118035236.txt](../../_raw/sales-letters/reading-head-start--20190118035236.txt) — 2019, 861 words, **landing** | $297 lifetime; $197 annual; $1 trial then $37/month | VSL/pricing wrappers; 2019 has 365-day refund but only 861 total words. |
| `wink-to-learn` — Wink to Learn | landing | [wink-to-learn--20120112094939.txt](../../_raw/sales-letters/wink-to-learn--20120112094939.txt) — 2012, 897 words, **landing** | Selected 4-DVD programmes S$88 | Multilingual-DVD catalogue; 897 words including repeated navigation/Flash placeholders; not one letter. |
| `intellectual-baby` — Intellectual Baby domain | no | [intellectual-baby--20130917185154.txt](../../_raw/sales-letters/intellectual-baby--20130917185154.txt) — 2013, 186 words, **no**<br>[intellectual-baby--20211208031117.txt](../../_raw/sales-letters/intellectual-baby--20211208031117.txt) — 2021, 0 words, **no** | No baby-offer price | 2013 registrar parking; 2021 zero-word JavaScript advertising shell. MonkiSee identity not evidenced. |
| `baby-genius` — Baby Genius | landing | [baby-genius--20110111072822.txt](../../_raw/sales-letters/baby-genius--20110111072822.txt) — 2011, 480 words, **landing**<br>[baby-genius--20160116231623.txt](../../_raw/sales-letters/baby-genius--20160116231623.txt) — 2016, 217 words, **landing** | No numeric product price | Toy/CD/DVD/book catalogue and later brand landing; short, no one-page long letter. |
| `brainy-baby` — Brainy Baby | landing | [brainy-baby--20080513222954.txt](../../_raw/sales-letters/brainy-baby--20080513222954.txt) — 2008, 715 words, **landing**<br>[brainy-baby--20110128184233.txt](../../_raw/sales-letters/brainy-baby--20110128184233.txt) — 2011, 107 words, **landing** | No numeric product price; $49 is shipping threshold | Brand/catalogue pages, 715/107 words; not long form. |
| `baby-sign-language` — Baby Sign Language guide / Deluxe Kit | landing | [baby-sign-language--20210419062700.txt](../../_raw/sales-letters/baby-sign-language--20210419062700.txt) — 2021, 663 words, **landing**<br>[baby-sign-language--20211021152944.txt](../../_raw/sales-letters/baby-sign-language--20211021152944.txt) — 2021, 5,109 words, **landing** | 2021 Deluxe $57.95 sale / $98.95 list | Guide short; Deluxe page totals 5,109 but only 1,039 seller-description/guarantee words, bulk is auto customer reviews/navigation. No-time-limit return/refund promise. |
| `baby-sleep-miracle` — Baby Sleep Miracle | landing | [baby-sleep-miracle--20170101164901.txt](../../_raw/sales-letters/baby-sleep-miracle--20170101164901.txt) — 2017, 862 words, **landing**<br>[baby-sleep-miracle--20220125035827.txt](../../_raw/sales-letters/baby-sleep-miracle--20220125035827.txt) — 2022, 1 words, **no** | 2017 $37 | 2017 VSL/comments wrapper, 862 words; 2022 one-word JavaScript index shell. |
| `baby-sleep-answers` — Baby Sleep Answers / The Baby Sleep System | landing | [baby-sleep-answers--20100224021641.txt](../../_raw/sales-letters/baby-sleep-answers--20100224021641.txt) — 2010, 851 words, **landing**<br>[baby-sleep-answers--20100725024839.txt](../../_raw/sales-letters/baby-sleep-answers--20100725024839.txt) — 2010, 540 words, **landing** | 2010 book £9.99 | Book/forum homepage plus 540-word product page; no long letter. Historical seller identity differs from current brand. |
| `sleep-lady` — The Sleep Lady / Good Night Sleep Tight | landing | [sleep-lady--20080103092748.txt](../../_raw/sales-letters/sleep-lady--20080103092748.txt) — 2008, 380 words, **landing**<br>[sleep-lady--20080205073133.txt](../../_raw/sales-letters/sleep-lady--20080205073133.txt) — 2008, 344 words, **landing** | Downloadable book $9.95 | 2008 short homepage and linked 380-word product description; not a long letter. |
| `montessori-babies` — Montessori Notebook: Montessori for Babies | landing | [montessori-babies--20170603201410.txt](../../_raw/sales-letters/montessori-babies--20170603201410.txt) — 2017, 400 words, **landing**<br>[montessori-babies--20220527052241.txt](../../_raw/sales-letters/montessori-babies--20220527052241.txt) — 2022, 600 words, **landing** | US$29 | 400/600-word workshop page; sidebar US$79 belongs to a different home-setup course. |
| `baby-acrobatics` — Baby Acrobatics 2024 presale | landing | [baby-acrobatics--20241114085435.txt](../../_raw/sales-letters/baby-acrobatics--20241114085435.txt) — 2024, 1,003 words, **landing** | $29.99 early / $49.99 later / $69.99 release | Core 3–12-month movement PDF presale, 1,003 words; only 2024 root year returned and no linked sales subpath. |
| `massage-happy-babies` — Massage for Happy Babies | landing | [massage-happy-babies--20110624011535.txt](../../_raw/sales-letters/massage-happy-babies--20110624011535.txt) — 2011, 667 words, **landing**<br>[massage-happy-babies--20130111055425.txt](../../_raw/sales-letters/massage-happy-babies--20130111055425.txt) — 2013, 545 words, **landing** | Digital £14.99 (2011), £7.99 (2013); DVD £19.99 + £1.45 UK postage | 545/667-word massage-video shop pages; 2011 basket £29.99 + £2.99 postage; no long letter. |
| `instant-baby-sleep` — Instant Baby Sleep | landing | [instant-baby-sleep--20100615191729.txt](../../_raw/sales-letters/instant-baby-sleep--20100615191729.txt) — 2010, 1,049 words, **landing**<br>[instant-baby-sleep--20170228232559.txt](../../_raw/sales-letters/instant-baby-sleep--20170228232559.txt) — 2017, 1,189 words, **landing** | 2010 US$19.97; 2017 $29.97 | Audio plus implementation guide; 1,049/1,189 total words, strictly below 1,200; stopped after second page/year. |
| `baby-sleep-site` — The Baby Sleep Site homepage | landing | [baby-sleep-site--20110111163438.txt](../../_raw/sales-letters/baby-sleep-site--20110111163438.txt) — 2011, 1,142 words, **landing** | No single primary price | 1,142-word service/product homepage; archive links trace Mastering Naps to babynapswell.com; not itself a letter. |

## Unresolved-offer probe and path-discovery limits

The combined **six-request** probe was requests 33–38: CDX `raisingsmarterbabies.com` (empty), CDX `yourchilddevelopmentsystem.com` (positive), HTML CDX of `sustab.hop.clickbank.net` (archived `CBRehoppp2` target `educatingbabies.com`), HTML CDX of `ycds1.hop.clickbank.net` (target `brightkidstoyguide.com` for the later toy-guide product), CDX `educatingbabies.com` (positive 2008–2015), and the 2012 Your Child Development System root fetch (503 words). Then stopped this branch. Neither educatingbabies.com nor brightkidstoyguide.com was page-fetched. These URLs are historical metadata/identity leads, not confirmed letters.

The Active Babies filtered sales-path lookup returned 503, the Milestones Kajabi prefix lookup returned 503, and the BrillKids prefix lookup timed out. These are not negative archive-existence findings. Exact BrillKids `/teach-reading/` then succeeded and was fetched. Milestones `/classes` exposed `https://milestones-and-motherhood.thrivecart.com/tummy-time-masterclass/` and related checkout paths, but the two short-page limit ended that branch. BabyPillars’ 2016 sidecar preserves pricing/book/age-course links; after the second-year short root the branch stopped.

## Candidates not fetched in this phase

Kinedu 2014/2018, BabySparks 2014 and Lovevery 2018 were ranked last and not reached because the twelve-letter stop triggered. Their requested years were not verified or silently replaced with other years. The table also inventories the remaining original TSV offer rows; a Phase 1 domain query is not a Phase 2 sales-page fetch.

| Phase 1 list | Offer | Domain | Topic | Status |
|---|---|---|---|---|
| A | Baby Can Read | unresolved | early-learning | Not reached before twelve-letter stop. |
| A | Raising Smarter Babies - How To Raise Smart, ... | unresolved | development | Six-request probe reached educatingbabies.com via archived sustab hop metadata; seller page not fetched. |
| A | Baby Sign Language | unresolved | early-learning | Not reached before twelve-letter stop. |
| A | Discover How Baby Sign Language Can Help You? | unresolved | early-learning | Not reached before twelve-letter stop. |
| A | The Smart Parents Guide To Choosing The Best Toys For Bright Kids | unresolved | play | ycds1 hop metadata traced brightkidstoyguide.com during shared probe; separate product not fetched. |
| A | Thriving Babies | unresolved | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| A | Toddler Talk: Techniques & Games | speechtherapytalk.com | milestones | Not reached before twelve-letter stop. |
| A | Imagination Suitcase: Dramatic Play, Music, Dance For Young Children | unresolved | play | Not reached before twelve-letter stop. |
| A | Essential Baby Sleep | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | MP3 & PDF - Sleep Through Baby (tm) System | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | Stop Feeding, Start Sleeping: Teach Your Baby To Sleep Thru The Night | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | Your Baby Will Sleep | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | My Baby Sleeps Through The Night | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | Get Your Baby To Sleep | unresolved | sleep-adjacent | Not reached before twelve-letter stop. |
| A | Toddler Speech Delay: Get Them Talking Now | toddlerspeechboost.com | milestones | Not reached before twelve-letter stop. |
| B | The Infant and Toddler Handbook | yourtherapysource.com | milestones | Not reached before twelve-letter stop. |
| B | CanDo Kiddo Baby's Best Tummy Time | candokiddo.com | development | Not reached before twelve-letter stop. |
| B | Your Guide to Tummy Time | pathways.org | development | Not reached before twelve-letter stop. |
| B | Early Intervention Blueprint: Infant Sensory Development | harkla.co | milestones | Not reached before twelve-letter stop. |
| B | Motherhood Unleashed | motherhood-unleashed.com | development | Not reached before twelve-letter stop. |
| B | First Step Method infant development workshops | firststepmethod.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Bloom Baby Classes | bloombabyclasses.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Baby Sensory / Hello Baby | babysensory.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | The Wonder Weeks | thewonderweeks.com | landing-page-only | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Kinedu early landing pages | kinedu.com | landing-page-only | Ranked last landing-page capture; not reached because twelve-letter stop triggered. |
| B | BabySparks early landing pages | babysparks.com | landing-page-only | Ranked last landing-page capture; not reached because twelve-letter stop triggered. |
| B | Lovevery launch / Play Kits | lovevery.com | landing-page-only | Ranked last landing-page capture; not reached because twelve-letter stop triggered. |
| B | Taking Cara Babies — newborn / 5–24 Month Collection | takingcarababies.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Let's Sleep — 7 Day Self-Settling Course | letssleep.com.au | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Just Chill Baby Sleep — Foundations / Sleep Success | justchillbabysleep.co.uk | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Good Inside — Baby Sleep Program | goodinside.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Sleep Nanny Melanie Hastings — progression guides | sleepnanny.co.uk | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Little Slumber Stars — Thriving Babies | littleslumberstars.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Baby Sleep Consultant — age-banded programs | babysleepconsultant.co | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Sleep Well With Hannah — C.A.L.M course | sleepwellwithhannah.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | BedtimeCoach — personalized printable plan | bedtimecoach.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Precious Little Sleep — book / SNOO Guide | preciouslittlesleep.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | My Sweet Sleeper — 4–12 Month Sleep Class | my-sweet-sleeper.teachable.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Moms on Call — books / 6–15 Month Video Course | momsoncall.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Lullaby Academy — Newborn / Naptime Guides | lullaby-academy.teachable.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Sweet Siestas | sweetsiestasllc.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Nested Sleep | nestedsleep.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | Riverbend Birth | pittsburghbirthservices.com | sleep-adjacent | Not reached before twelve-letter stop. |
| B | 101 Before One — PDF meal plans | 101beforeone.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Boob to Food — classes/books/downloads | boobtofood.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | My Little Food Critic — 28 Day Meal Plan | mylittlefoodcritic.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Postpartum Plan — recovery membership | postpartumplan.co.uk | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | MyMatLeave — personalized leave strategy PDF | mymatleave.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Planned — business maternity task plan | mastermaternityleave.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Modern Motherhood — tailored postpartum plan/guides | modernmotherhoodbirth.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Lotus & Luna — curated written registry lists | lotusandluna-atx.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Madam Doula — registry creation/audit | madamdoula.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | The Starter Set — personalized registry picks | thestarterset.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Baby Chick — written Registry Review | baby-chick.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | The Baby Planner — registry written summary | thebabyplanner.co | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Stress Less Mom — preparation toolkit/goal plan | stresslessmom.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Curated to Grow — individualized toy/gift lists | curatedtogrow.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Genius Babies | geniusbabies.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Baby Signs | babysigns.com | early-learning | Not reached before twelve-letter stop. |
| B | Baby Signing Time | babysigningtime.com | early-learning | Not reached before twelve-letter stop. |
| B | Baby Einstein | babyeinstein.com | other | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Monti Kids | montikids.com | landing-page-only | Not reached; Phase 1 already labels outside primary letter scope or landing-only. |
| B | Your Baby Can Learn | yourbabycanlearn.com | early-learning | Not reached before twelve-letter stop. |
| B | Institutes for the Achievement of Human Potential / Doman parent programmes | iahp.org | early-learning | Not reached before twelve-letter stop. |
| B | Doman Learning infant movement / reading / math courses | domanlearning.com | early-learning | Not reached before twelve-letter stop. |
| B | MySmartBaby whole-brain early-learning programme | mysmartbaby.in | early-learning | Not reached before twelve-letter stop. |

## Full raw text list for Phase 3

All 83 Phase 2 text files are listed below, including landings, failures and the outside-audience reference. Use the verdict table / [TSV inventory](p2-captures.tsv) to select the 32 qualifying target captures. `.html`, `.headers.json` and `.links.json` sidecars are preserved beside their text where the helper emitted them; [the checksum inventory](p2-raw-sha256.txt) lists all raw artifacts. The one corrupt gzip text is excluded from quoting.

```text
_raw/sales-letters/baby-milestones--20100117074328.txt
_raw/sales-letters/baby-milestones--20130131124554.txt
_raw/sales-letters/baby-milestones--20160114023855.txt
_raw/sales-letters/babypillars--20160504183614.txt
_raw/sales-letters/babypillars--20190201123302.txt
_raw/sales-letters/active-babies--20160101144840.txt
_raw/sales-letters/play-develop-thrive--20220926061658.txt
_raw/sales-letters/play-develop-thrive--20230301115112.txt
_raw/sales-letters/play-develop-thrive--20240421112446.txt
_raw/sales-letters/play-develop-thrive--20230322062000.txt
_raw/sales-letters/childs-genius--20080112011131.txt
_raw/sales-letters/childs-genius--20100123001342.txt
_raw/sales-letters/childs-genius--20120126082931.txt
_raw/sales-letters/baby-massage--20110201170058.txt
_raw/sales-letters/baby-massage--20211126195014.txt
_raw/sales-letters/milestones-motherhood--20220414165451.txt
_raw/sales-letters/milestones-motherhood--20221119032454.txt
_raw/sales-letters/how-to-play--20230603182551.txt
_raw/sales-letters/how-to-play--20240414015448.txt
_raw/sales-letters/your-child-development--20121012022705.txt
_raw/sales-letters/mommy-jingles--20160204203121.txt
_raw/sales-letters/mommy-jingles--20141013172835.txt
_raw/sales-letters/your-baby-can-read--20090221201037.txt
_raw/sales-letters/your-baby-can-read--20120104191207.txt
_raw/sales-letters/little-reader--20110113193546.txt
_raw/sales-letters/little-reader--20110208174417.txt
_raw/sales-letters/gentle-revolution--20080112014029.txt
_raw/sales-letters/gentle-revolution--20160105021216.txt
_raw/sales-letters/children-learning-reading--20120114194846.txt
_raw/sales-letters/children-learning-reading--20150102045337.txt
_raw/sales-letters/children-learning-reading--20180105210614.txt
_raw/sales-letters/reading-head-start--20170713100440.txt
_raw/sales-letters/reading-head-start--20190118035236.txt
_raw/sales-letters/wink-to-learn--20120112094939.txt
_raw/sales-letters/intellectual-baby--20130917185154.txt
_raw/sales-letters/baby-genius--20110111072822.txt
_raw/sales-letters/brainy-baby--20110128184233.txt
_raw/sales-letters/intellectual-baby--20211208031117.txt
_raw/sales-letters/baby-genius--20160116231623.txt
_raw/sales-letters/brainy-baby--20080513222954.txt
_raw/sales-letters/signing-for-babies--20080105074350.txt
_raw/sales-letters/signing-for-babies--20120101164146.txt
_raw/sales-letters/signing-for-babies--20160111012429.txt
_raw/sales-letters/baby-sign-language--20210419062700.txt
_raw/sales-letters/baby-sign-language--20211021152944.txt
_raw/sales-letters/help-your-child-speak--20100131081101.txt
_raw/sales-letters/help-your-child-speak--20120213155002.txt
_raw/sales-letters/help-your-child-speak--20160110055329.txt
_raw/sales-letters/baby-sleep-miracle--20170101164901.txt
_raw/sales-letters/baby-sleep-miracle--20220125035827.txt
_raw/sales-letters/sleep-baby-sleep--20120103223147.txt
_raw/sales-letters/sleep-baby-sleep--20070104173058.txt
_raw/sales-letters/sleep-baby-sleep--20060221101036.txt
_raw/sales-letters/sleep-baby-sleep--20080131132622.txt
_raw/sales-letters/baby-sleep-solution--20080107101232.txt
_raw/sales-letters/baby-sleep-solution--20100104140714.txt
_raw/sales-letters/baby-sleep-solution--20120105012544.txt
_raw/sales-letters/baby-sleep-answers--20100224021641.txt
_raw/sales-letters/baby-sleep-answers--20100725024839.txt
_raw/sales-letters/five-minute-sleep--20170105120427.txt
_raw/sales-letters/five-minute-sleep--20161031080226.txt
_raw/sales-letters/five-minute-sleep--20180109175826.txt
_raw/sales-letters/sleep-lady--20080205073133.txt
_raw/sales-letters/sleep-lady--20080103092748.txt
_raw/sales-letters/teach-baby-to-swim--20160111232548.txt
_raw/sales-letters/teach-baby-to-swim--20140518233807.txt
_raw/sales-letters/teach-baby-to-swim--20170405031826.txt
_raw/sales-letters/montessori-babies--20220527052241.txt
_raw/sales-letters/montessori-babies--20170603201410.txt
_raw/sales-letters/montessori-babies-course--20230531002658.txt
_raw/sales-letters/montessori-babies-course--20240226044259.txt
_raw/sales-letters/baby-acrobatics--20241114085435.txt
_raw/sales-letters/massage-happy-babies--20130111055425.txt
_raw/sales-letters/massage-happy-babies--20110624011535.txt
_raw/sales-letters/magic-lullabies--20130104183624.txt
_raw/sales-letters/magic-lullabies--20110923162615.txt
_raw/sales-letters/magic-lullabies--20140103015343.txt
_raw/sales-letters/instant-baby-sleep--20100615191729.txt
_raw/sales-letters/instant-baby-sleep--20170228232559.txt
_raw/sales-letters/baby-sleep-site--20110111163438.txt
_raw/sales-letters/mastering-naps--20100108062253.txt
_raw/sales-letters/mastering-naps--20110201000529.txt
_raw/sales-letters/mastering-naps--20140131003250.txt
```
