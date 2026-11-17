# Phase 1B — seeds, historical brands and web-search candidates

Run date: 2026-11-03. Discovery only; no archived pages fetched and no live sales pages opened or scraped.

**Result:** 75 CDX-backed candidate rows in [candidates-B.tsv](../candidates-B.tsv), from 97 unique domain/seller-host queries. 42 topical candidates have at least one successful capture in 2008–2022; this verifies archive presence, not that their named offer or a qualifying letter existed then. 22 queries returned no matching captures. No row is yet confirmed to meet the ≥1,200-word letter definition.

## Method and coverage

1. Read [sales-letter rules](../README.md), [development competitor index](../../competitors/README.md) and its linked seller notes, [sleep competitor index](../../../sleep-baby/competitors/README.md), [global competitor index](../../../global/competitors/README.md), and [sub-niche map §0](../../../main/synthesis/sub-niche-map.md). A background researcher traced the sleep/global sellers to the existing first-party capture notes; its [inventory](p1b-seed-inventory.md) records service and topic exclusions.
2. Queried the seed sellers first, including broader document/course references as `other`. Then checked recalled historical brands, then used live search queries and checked newly discovered domains or exact product URLs. Repeated sellers were deduplicated by domain; a separate hosted sales domain is distinguishable from a parent seller domain.
3. Every archive request went through `python3 -I _tools/wayback.py cdx`, with `--from 2008 --to 2024 --limit 30`. Queries ran sequentially, using the helper’s shared four-second throttle. There were no `fetch` commands, archive page opens, or alternative archive APIs.
4. Except for the first Baby Acrobatics query, added the backward-compatible helper option `--collapse timestamp:4`, retaining one successful capture per calendar year instead of the first 30 distinct digests. This prevents the row limit from truncating later years. All queries use exact matching: homepages for ordinary domains, and seller-specific URLs for selected hosted/product pages. None returned 30 rows.
5. `first_capture` and `last_capture` mean the first/last **HTTP-200 capture years of the queried URL within 2008–2024**, not the domain’s first-ever/last-ever capture, product launch or sales dates. The requested command does not cover 2005–2007. A homepage query does not establish the capture history of a guessed product path or every URL on that domain.
6. All retained names have a positive saved CDX result. App/subscription and physical-product landing references are explicitly separated from prospective letters. Current 2026 prices and refund language are dated leads, not historical observations. No archived headlines, claims, price or guarantee are quoted.

## Request accounting

- **97 CDX invocations**: one initial successful query plus 96 instrumented HTTP requests. The initial invocation preceded request instrumentation; its saved stdout is [001-babyacrobatics.com.tsv](p1b-cdx/001-babyacrobatics.com.tsv), and it emitted no retry diagnostic. Its transport redirects were not logged, so the nominal total is 97 and three requests were left unused as budget reserve.
- Instrumented audit: 96 request events, 96 response events, all HTTP 200; 0 redirects and 0 errors. There were no retry attempts in the audit. [HTTP audit](p1b-wayback-requests.jsonl).
- **0 archive page fetches; 0 live sales-page fetches.** Live web research used 20 search queries in five batches. Search-indexed text was used for lead discovery; it was not saved or represented as an archived capture. [Search ledger](p1b-web-searches.json).
- Reproducible evidence: [query plan](p1b-query-plan.json), [results with exact timestamp/original-URL pairs](p1b-query-results.json), and individual CDX TSV/stderr files in [p1b-cdx/](p1b-cdx/).

| Route | Queries | Positive rows | No matching captures |
|---|---:|---:|---:|
| Existing research seeds | 69 | 49 | 20 |
| Brand recall | 18 | 18 | 0 |
| Web-search leads | 10 | 8 | 2 |

| Topic | Positive rows |
|---|---:|
| development | 10 |
| play | 1 |
| milestones | 3 |
| early-learning | 16 |
| sleep-adjacent | 21 |
| landing-page-only | 5 |
| other | 19 |

## Ten first-fetch priorities

These are editorial priorities, not ten validated letters. Every timestamp and exact original URL below is copied from a saved CDX row and falls within 2008–2022. The timestamp belongs to the URL shown, not automatically to `likely_sales_url`. Ranks 8–10 are weaker seller-discovery entries. CDX `length` is an archive-record byte length and was never treated as a word count. Phase 2 must confirm one page, headline, body word count, price/buy CTA, guarantee, language and historical product identity.

| Rank | Candidate | First-fetch timestamp | Exact captured original URL | Fit / confidence | Why inspect it | CDX evidence |
|---:|---|---|---|---|---|---|
| 1 | Play, Develop, Thrive (Emma Hubbard) | `20220926061658` | `https://brightestbeginning.com/courses/play-develop-thrive/` | Core development; strong page-specific lead | Exact Play, Develop, Thrive sales path exists in 2022. The current search-indexed seller page presents a paid 0–12-month programme and a 30-day refund. [Seller source](https://brightestbeginning.com/courses/play-develop-thrive/). | [CDX](p1b-cdx/089-brightestbeginning.com.tsv) |
| 2 | BabyPillars Baby Development System 0-24 Months | `20160504183614` | `http://www.babypillars.com:80/?` | Core development; strong product-domain lead | 0–24-month development video programme; early homepage capture is a useful first version to inspect. Current seller index shows a paid programme and annual-plan refund, not historical proof. [Seller source](https://www.babypillars.com/). | [CDX](p1b-cdx/088-babypillars.com.tsv) |
| 3 | Children Learning Reading | `20150102045337` | `http://www.childrenlearningreading.com:80/?` | Adjacent older-child reading; strong hypothesis | Known reading info-product domain with multiple pre-2023 captures. The 2015 original URL is preserved exactly, including port and query marker. Offer/letter identity is still untested. | [CDX](p1b-cdx/084-childrenlearningreading.com.tsv) |
| 4 | Baby Sign Language Kit | `20210419062700` | `https://www.babysignlanguage.com/basic-full-screen/` | Adjacent infant signing; strong page-specific lead | Exact full-screen kit-sales path captured in 2021; current indexed seller copy includes a satisfaction/refund promise. Physical/video hybrid, so format must be checked. [Seller source](https://babysignlanguage.com/basic-full-screen/). | [CDX](p1b-cdx/090-babysignlanguage.com.tsv) |
| 5 | Reading Head Start | `20190118035236` | `https://www.readingheadstart.com/` | Adjacent age-2+ reading; strong hypothesis | ClickBank reading offer named in the seed research. This is an actual 2019 homepage record, not an invented timestamp for a guessed product path. [Seed](../../competitors/README.md). | [CDX](p1b-cdx/068-readingheadstart.com.tsv) |
| 6 | Baby Sleep Miracle | `20170101164901` | `http://babysleepmiracle.com:80/?` | Sleep-adjacent; text/VSL ambiguity | ClickBank ebook/guide in the existing sleep research. Inspect this older root before the smaller later roots; a VSL wrapper remains possible. [Seed](../../../sleep-baby/competitors/baby-sleep-miracle.md). | [CDX](p1b-cdx/036-babysleepmiracle.com.tsv) |
| 7 | Sleep Baby Sleep ebook | `20120103223147` | `http://www.sleepbabysleep.com:80/` | Sleep-adjacent; promising older ebook lead | Seller search index explicitly identifies an ebook and a 30-day refund; many old homepage captures are available. The index crawl is old, not a new live-page inspection. [Seller source](https://www.sleepbabysleep.com/). | [CDX](p1b-cdx/091-sleepbabysleep.com.tsv) |
| 8 | Active Babies Smart Kids | `20160101144840` | `http://activebabiessmartkids.com.au/` | Core development; exploratory | Historical infant movement/early-stimulation programme domain; 2016 root is a first discovery fetch. No specific sales path, price or guarantee has been verified. | [CDX](p1b-cdx/077-activebabiessmartkids.com.au.tsv) |
| 9 | Milestones and Motherhood Tummy Time / Milestone Masterclasses | `20220414165451` | `https://www.milestonesandmotherhood.com/` | Core milestones; exploratory | Known parent masterclass seller with a 2022 homepage capture. Fetch to locate historical course links; the homepage itself may be a short landing page. [Current course index](https://www.milestonesandmotherhood.com/courses). | [CDX](p1b-cdx/095-milestonesandmotherhood.com.tsv) |
| 10 | BrillKids Little Reader / Little Math / Little Musician | `20110113193546` | `http://www.brillkids.com:80/` | Adjacent infant reading/math/music; exploratory | Little Reader/Little Math seller domain captured in 2011. Use the homepage to discover product sales links; it may be a catalogue rather than a letter. | [CDX](p1b-cdx/071-brillkids.com.tsv) |

The preferred fetch syntax is `python3 -I _tools/wayback.py fetch <timestamp> <exact-original-URL> --out <raw-file>`, but **none was executed in Phase 1B**. Catalogue/blog homepages may first reveal a better historical sales path; that later lookup belongs to Phase 2.

## Dead ends and limitations

All no-result queries below returned HTTP 200 with no matching HTTP-200 captures for the exact queried URL in the chosen window. This is not proof that the seller never existed, that a parent host had no captures, or that a differently spelled/path/versioned URL was not archived. No alternate-path retry was made, preserving the one-query-per-domain rule.

| Route | Domain / seller host | Exact query target | Evidence |
|---|---|---|---|
| 1 | `wannabediary.samcart.com` | `wannabediary.samcart.com/products/how-to-raise-a-genius-guide` | [CDX stderr](p1b-cdx/004-wannabediary.samcart.com.stderr) |
| 1 | `stan.store` | `stan.store/Ourplayfullhome/p/get-my-02-play-guide-now` | [CDX stderr](p1b-cdx/005-stan.store.stderr) |
| 1 | `fitfamilypt.sellfy.store` | `fitfamilypt.sellfy.store/p/developmental-milestone-play-guide/` | [CDX stderr](p1b-cdx/006-fitfamilypt.sellfy.store.stderr) |
| 1 | `selar.com` | `selar.com/1r42728p7o` | [CDX stderr](p1b-cdx/008-selar.com.stderr) |
| 1 | `tummy-time.teachery.co` | `tummy-time.teachery.co/tummy-time` | [CDX stderr](p1b-cdx/010-tummy-time.teachery.co.stderr) |
| 1 | `pirmizingsniai.lt` | `pirmizingsniai.lt` | [CDX stderr](p1b-cdx/018-pirmizingsniai.lt.stderr) |
| 1 | `elsolepesekmama.com` | `elsolepesekmama.com` | [CDX stderr](p1b-cdx/019-elsolepesekmama.com.stderr) |
| 1 | `smartstartsforparents.com` | `smartstartsforparents.com` | [CDX stderr](p1b-cdx/027-smartstartsforparents.com.stderr) |
| 1 | `calmer-nights.com` | `calmer-nights.com` | [CDX stderr](p1b-cdx/032-calmer-nights.com.stderr) |
| 1 | `dawnlysleep.com` | `dawnlysleep.com` | [CDX stderr](p1b-cdx/033-dawnlysleep.com.stderr) |
| 1 | `baby-sleep-course.teachable.com` | `https://baby-sleep-course.teachable.com/p/fromcontacttothecot` | [CDX stderr](p1b-cdx/038-baby-sleep-course.teachable.com.stderr) |
| 1 | `thesleepretreatsleepschool.teachable.com` | `https://thesleepretreatsleepschool.teachable.com/p/responsiveparentsleepsolutionbaby` | [CDX stderr](p1b-cdx/042-thesleepretreatsleepschool.teachable.com.stderr) |
| 1 | `davisjohnson7.gumroad.com` | `https://davisjohnson7.gumroad.com/l/custom-sleep-plan` | [CDX stderr](p1b-cdx/043-davisjohnson7.gumroad.com.stderr) |
| 1 | `babysleepandsmile.com` | `babysleepandsmile.com` | [CDX stderr](p1b-cdx/047-babysleepandsmile.com.stderr) |
| 1 | `beyondbirthing.ca` | `beyondbirthing.ca` | [CDX stderr](p1b-cdx/056-beyondbirthing.ca.stderr) |
| 1 | `rootedbirthabq.wixsite.com` | `https://rootedbirthabq.wixsite.com/rooted-birth-service/services` | [CDX stderr](p1b-cdx/057-rootedbirthabq.wixsite.com.stderr) |
| 1 | `byhads.com` | `byhads.com` | [CDX stderr](p1b-cdx/061-byhads.com.stderr) |
| 1 | `thevillageparentcommunity.com` | `thevillageparentcommunity.com` | [CDX stderr](p1b-cdx/065-thevillageparentcommunity.com.stderr) |
| 1 | `nestingnotesco.com` | `nestingnotesco.com` | [CDX stderr](p1b-cdx/067-nestingnotesco.com.stderr) |
| 1 | `familymoneyhelper.co.uk` | `familymoneyhelper.co.uk` | [CDX stderr](p1b-cdx/069-familymoneyhelper.co.uk.stderr) |
| 3 | `ontrackbabycourses.com` | `https://www.ontrackbabycourses.com/setup-the-nursery` | [CDX stderr](p1b-cdx/092-ontrackbabycourses.com.stderr) |
| 3 | `learnwithless.com` | `https://learnwithless.com/product/understanding-your-baby-multimedia-course-package/` | [CDX stderr](p1b-cdx/094-learnwithless.com.stderr) |

**Only post-2022 captures returned:** `babyacrobatics.com`, `babytourguide.teachable.com`, `motherhood-unleashed.com`, `littleslumberstars.com`, `sleepwellwithhannah.com`, `bedtimecoach.com`, `my-sweet-sleeper.teachable.com`, `lullaby-academy.teachable.com`, `thestarterset.com`, `curatedtogrow.com`, `healthiest-baby.com`. These are retained as clearly labelled later leads, not counted among the 42 topical pre-2023 candidates.

**Captured, not letter:** Kinedu, BabySparks and Lovevery early landing pages, Monti Kids and The Wonder Weeks are `landing-page-only`. Baby Einstein and Genius Babies are `other` physical-product/catalogue references. Videos/DVDs/flashcard kits can still have long-form selling pages, but the products themselves are not written info products.

**Scope controls:** the source indexes contain feeding books, maternity/registry planners, written consultation bundles, local classes and professional training. Broader seed sellers were checked and labelled `other` or explicitly described as human-service bundles; they are not used to substantiate the development/early-learning letter shortlist. Lithuanian/Hungarian Pirmi/Elso references returned no captures and do not enter the English candidate TSV. Exercise-only app memberships, free public guidance and pure app-store listings were not converted into document sellers.

**Web-search dead ends:** JVZoo/Warrior queries mostly yielded general niche discussion or unrelated material, with no additional named historical baby-development offer suitable for this shortlist. Milestone-ebook searches included 2023/2025 retail titles, which do not establish 2005–2022 sales letters. Generic “smart baby” results included CPR software, insurance programmes and apps; those were discarded. The October 2015 [MySmartBaby advertisement](https://jfwonline.com/emag/JFWOct2015.pdf) supplied a genuine historical domain lead, but its archived homepage identity and letter format still need inspection.

**Unqueried follow-ups:** current Kinedu ebook host `courses.kinedu.com/ebook-landing`, the Strength in Words legacy domain, Therapy Stars and Movement Lesson appeared during discovery but were not given additional queries after the selected ten web leads. The Kinedu seller itself was already checked as a landing-page seed; this does not verify its ebook subdomain. Search-only names lacking traceable domains (Dorothy Waide, Jessie Martin, Heidi Holvoet, Asleep in 12 in the original notes) remain unresolved, rather than guessed into the verified TSV.

**What remains for Phase 2:** fetch the exact captured URLs above, save raw text, and reject short landings, blogs, catalogues, VSL-only shells, unrelated historical owners and post-window offer launches. Confirm prices and guarantees from the historical page itself. Archive presence proves existence of an archived URL, never sales, revenue, conversions, efficacy, or that the current offer existed in that year.
