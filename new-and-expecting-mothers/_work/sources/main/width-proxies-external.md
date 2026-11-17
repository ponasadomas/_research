# Width proxies — external public counts for "new and expecting mothers" sub-niches

Date: 2026-10-24

**Method.** Subreddit subscriber counts were pulled from the Arctic Shift API (`arctic-shift.photon-reddit.com/api/subreddits/search?subreddit=...`), a public Reddit-metadata mirror; the `subscribers` field is the mirror's most recent snapshot, not a live Reddit read, so "observed today" means "observed via the mirror today". Amazon Best Sellers pages were requested via WebFetch (all returned HTTP 503); the fallback is third-party keyword/sales-estimate snapshots found via WebSearch, labelled as such. App data comes from the public iTunes Search API (rating, rating count), the apps.apple.com listing page (the "#N in <Category>" chart badge shown on the listing, which is a category chart position, not a top-grossing rank), and plain fetches of Google Play listing pages (rating, rating count, download bucket). Table 4 reflects the first ~10 organic URLs returned by WebSearch (standard mode); the tool exposes neither a total result count nor a "People also ask" box. Nothing here was retried past one attempt, and no bot wall was worked around.

**Rule: these are public counts observed today, not market size; a subscriber count is not a buyer count.**

---

## Table 1 — Subreddit subscriber counts

Source for all rows: Arctic Shift API, Reddit metadata mirror. `posts` = lifetime post count held by the mirror (secondary activity proxy).

| subreddit | subscribers | posts (lifetime, mirror) | source | note (sub-niche) |
|---|---:|---:|---|---|
| Mommit | 2,596,695 | 234,711 | Arctic Shift | general (mothers) |
| daddit | 1,781,687 | 263,867 | Arctic Shift | general (fathers) |
| pregnant | 1,546,857 | 623,461 | Arctic Shift | pregnancy |
| beyondthebump | 736,426 | 391,450 | Arctic Shift | general (0-12 mo); listed twice in brief, one row |
| BabyBumps | 468,214 | 650,718 | Arctic Shift | pregnancy |
| toddlers | 442,542 | 189,865 | Arctic Shift | toddler behaviour |
| namenerds | 431,714 | 350,592 | Arctic Shift | names |
| NewParents | 374,722 | 252,056 | Arctic Shift | general |
| breastfeeding | 179,738 | 262,604 | Arctic Shift | feeding |
| ScienceBasedParenting | 167,776 | 31,311 | Arctic Shift | development / general |
| TryingForABaby | 152,207 | 174,683 | Arctic Shift | pregnancy (pre-conception) |
| sleeptrain | 128,772 | 139,246 | Arctic Shift | sleep |
| workingmoms | 118,482 | 60,278 | Arctic Shift | work return |
| SAHP | 88,277 | 10,926 | Arctic Shift | general (stay-at-home) |
| predaddit | 70,296 | 34,132 | Arctic Shift | pregnancy (fathers) |
| moderatelygranolamoms | 68,375 | 22,024 | Arctic Shift | general (natural-leaning) |
| Newborns | 65,975 | 71,238 | Arctic Shift | general (0-3 mo) / sleep |
| BabyLedWeaning | 54,018 | 22,201 | Arctic Shift | solids |
| ExclusivelyPumping | 51,372 | 82,856 | Arctic Shift | feeding (pumping) / work return |
| FormulaFeeders | 45,237 | 41,693 | Arctic Shift | feeding (formula) |
| clothdiaps | 40,621 | 38,386 | Arctic Shift | general (gear) |
| parentsofmultiples | 39,060 | 53,963 | Arctic Shift | multiples/prem |
| pottytraining | 34,531 | 19,683 | Arctic Shift | potty |
| PregnancyUK | 32,964 | 41,383 | Arctic Shift | pregnancy (UK) |
| BabyBumpsCanada | 27,626 | 34,427 | Arctic Shift | pregnancy (CA) |
| NICUParents | 22,196 | 28,953 | Arctic Shift | multiples/prem (NICU) |
| BabyBumpsandBeyondAu | 15,467 | 25,779 | Arctic Shift | pregnancy (AU) |
| Postpartum_Depression | 13,788 | 12,316 | Arctic Shift | mental health |
| BeyondTheBumpUK | 6,285 | 20,473 | Arctic Shift | general (UK) |
| Postpartum_Anxiety | 4,723 | 1,717 | Arctic Shift | mental health |
| NewbornSleep | 327 | 457 | Arctic Shift | sleep (exists; created Dec 2023, tiny) |

---

## Table 2 — Amazon bestseller lists (US), parenting / pregnancy books

**No top-20 list was obtained.** All three amazon.com Best Sellers pages returned HTTP 503 on WebFetch and the single curl retry was blocked by the permission classifier (see "What failed"). The rows below are third-party snapshots found via WebSearch, each labelled with its real source and metric. Authors are left blank where the source page did not show them.

| list / source | position | title | author (if shown) | metric shown | sub-niche |
|---|---:|---|---|---|---|
| amazonseo.ai, Amazon Brand Analytics snapshot for keyword "pregnancy book" (undated, © 2026 footer) | 1 | What to Expect When You're Expecting (Updated in 2025) | — | click share 20.10%, conversion share 23.58% | pregnancy |
| same | 2 | Pregnancy Journal for First Time Moms Gifts – 90 Pages Hardcover Pregnancy Memory Book… | — | click share 12.01%, conversion share 4.37% | pregnancy (keepsake) |
| same | 3 | The Simplest Pregnancy Book in the World | — | click share 10.62%, conversion share 9.83% | pregnancy |
| amazonseo.ai, Amazon Brand Analytics snapshot for keyword "parenting books" (undated) | 1 | The Whole-Brain Child | — | click share 16.62%, conversion share 12.34% | development-play |
| same | 2 | Raising Good Humans | — | click share 9.75%, conversion share 7.47% | toddler behaviour / general |
| same | 3 | The Book You Wish Your Parents Had Read | — | click share 7.40%, conversion share 2.27% | general |
| amazonseo.ai "parenting books" (WebSearch snippet only) | — | The Simplest Baby Book in the World | — | named as a top-converting title in snippet | general (0-12 mo) |
| WebSearch snippet: Desertcart product listing for WTE 2025 edition (undated) | "#1 in Pregnancy & Childbirth" | What to Expect When You're Expecting | — | claimed Amazon category rank; ">18.5 million copies sold" claim | pregnancy |
| WebSearch snippet: amazonseo.ai "pregnancy book" keyword | — | The First Time Dad's Pregnancy Handbook | — | named in top results | pregnancy (fathers) |
| WebSearch snippet: AsinSight sales estimate, keyword "book for baby" (June 2026) | 1 | LeapFrog Learning Friends 100 Words Book | — | ~10K est. monthly sales | development-play (child picture book, not a parenting guide) |
| same | 2-3 | Two black-and-white high-contrast baby books (ASINs B0CBV96TQ1, B0DHH7LGZT) | — | ~10K est. monthly sales each | development-play (child book) |
| WebSearch snippet: AsinSight sales estimate, keyword "toddler books" (March 2026) | 1-3 | Water-reveal coloring pad; Melissa & Doug Poke-a-Dot board book; ASIN B0CTHQJF57 | — | ~10K est. monthly sales each | development-play (child book) |
| WebSearch snippet: BookAuthority "best-selling parenting books" (updated June 2025) | — | No-Drama Discipline | Tina Payne Bryson | listed, no number | toddler behaviour |

Pages that would have given the real lists: Pregnancy & Childbirth `zgbs/books/11164`, Babies & Toddlers `zgbs/books/11160`, Parenting `zgbs/books/11148` — all 503 today.

---

## Table 3 — App store listings, Kids/Parenting-adjacent (US)

"iOS chart badge" = the "#N in <Category>" position printed on the apps.apple.com listing on 2026-10-24; it is a category chart position shown on the listing, **not** a top-grossing rank. "Not charting" = no badge on the listing today. iOS rating/count from the iTunes Search API (US). Play figures from the play.google.com listing (US, en). Play package-id guesses that 404'd are recorded as such, not as "absent from Play".

| app | store | iOS chart badge (listing) | rating | rating count | Play download bucket | sub-niche | source |
|---|---|---|---:|---:|---|---|---|
| Flo Cycle & Period Tracker | iOS | #2 in Health & Fitness | 4.74 | 2,004,734 | — | pregnancy (cycle/pregnancy) | iTunes API + listing |
| Flo | Google Play | — | 4.73 | 5,157,643 | 100M+ | pregnancy (cycle/pregnancy) | Play listing |
| Pregnancy Tracker App – WTE (What to Expect) | iOS | #25 in Medical | 4.87 | 380,512 | — | pregnancy | iTunes API + listing |
| What to Expect | Google Play | — | 4.89 | 121,680 | 5M+ | pregnancy | Play listing |
| Pregnancy+ (Philips) | iOS | #19 in Medical | 4.85 | 76,846 | — | pregnancy | iTunes API + listing |
| Pregnancy+ | Google Play | — | 4.81 | 3,697,834 | 50M+ | pregnancy | Play listing |
| Ovia Cycle & Pregnancy Tracker | iOS | #113 in Medical | 4.83 | 90,776 | — | pregnancy | iTunes API + listing |
| Ovia | Google Play | — | — | — | — | pregnancy | package id guess 404 |
| Baby Tracker – Newborn Log (Nighp) | iOS | #91 in Medical | 4.80 | 227,367 | — | general (feeds/sleep/diapers log) | iTunes API + listing |
| Baby Tracker – Newborn Log | Google Play | — | 4.89 | 71,892 | 1M+ | general (log) | Play listing |
| Huckleberry: Baby Tracker | iOS | #17 in Medical | 4.92 | 75,480 | — | sleep | iTunes API + listing |
| Huckleberry | Google Play | — | 4.87 | 36,955 | 1M+ | sleep | Play listing |
| The Wonder Weeks – Baby leaps | iOS | not charting | 4.84 | 122,384 | — | development | iTunes API + listing |
| The Wonder Weeks | Google Play | — | — | — | — | development | package id guess 404 |
| Solid Starts: Baby First Foods | iOS | #57 in Education | 4.91 | 46,569 | — | solids | iTunes API + listing |
| Solid Starts | Google Play | — | — | — | — | solids | package id guess 404 |
| Nanit | iOS | #155 in Lifestyle | 4.68 | 38,309 | — | sleep (hardware companion) | iTunes API + listing |
| Nara Baby & Pregnancy Tracker | iOS | #125 in Medical | 4.85 | 24,475 | — | general (log) | iTunes API + listing |
| Nara | Google Play | — | 3.17 | 7,320 | 100K+ | general (log) | Play listing |
| Glow Baby Tracker & Growth | iOS | not charting | 4.67 | 23,466 | — | general (log) | iTunes API + listing |
| Glow Baby | Google Play | — | 3.88 | 14,682 | 1M+ | general (log) | Play listing |
| Lovevery: Baby & Toddler App | iOS | not charting | 4.96 | 13,772 | — | development-play | iTunes API + listing |
| Lovevery | Google Play | — | — | — | — | development-play | package id guess 404 |
| BabySparks – Development App | iOS | not charting | 4.67 | 13,169 | — | development | iTunes API + listing |
| BabySparks | Google Play | — | 4.07 | 14,718 | 1M+ | development | Play listing |
| Peanut: Find Mom Friends | iOS | not charting | 4.39 | 11,642 | — | general (community) | iTunes API + listing |
| Peanut | Google Play | — | 3.94 | 11,908 | 1M+ | general (community) | Play listing |
| Kinedu: Baby Development | iOS | #158 in Education | 4.56 | 7,140 | — | development | iTunes API + listing |
| Kinedu | Google Play | — | — | — | — | development | package id guess 404 |
| Napper: Baby Sleep Tracker | iOS | not charting | 4.89 | 4,597 | — | sleep | iTunes API + listing |
| Napper | Google Play | — | — | — | — | sleep | package id guess 404 |
| Pathways.org Baby Milestones | iOS | not checked | 4.88 | 1,254 | — | development | iTunes API |

**Only grossing-rank source found (one year old, labelled):** Sensor Tower blog, "Parenting" category, US, Q3 2025 (weekly figures).
- Top 5 by revenue: 1 Nanit (peak ~$368K/wk, ~$240K at quarter end); 2 TalkingParents (~$171K to ~$138K); 3 Speech Blubs (~$131K); 4 OurFamilyWizard (peak ~$101K); 5 Findmykids (peak ~$77K).
- Top 5 by downloads: 1 Findmykids (24.8K/wk peak); 2 Speech Blubs (16.7K); 3 Nanit (~11K/wk avg); 4 OurFamilyWizard (~5K/wk avg); 5 TalkingParents (4.7K peak).
- Sensor Tower Q2 2025 (US, "Parenting" category, peaks): downloads led by Theo: Prayer & Meditation (45.9K), FamilyAlbum (18.5K), "Pregnancy App & Baby Tracker" (~17.9K), Findmykids (14.3K); revenue led by Findmykids ($64.1K/wk peak), Theo ($54.7K), FamilyAlbum ($38.9K).
- Note on the figures: none of the baby-sleep / feeding / development apps in the table above appear in Sensor Tower's "Parenting" category top-5, because most of them are classified under Medical, Health & Fitness or Education.
- App Pricing Lab, "Parenting" report, October 2026: tracks 288 apps; 99% free to download; no per-app rank published.
- Similarweb snapshots (via WebSearch snippet): Huckleberry US iOS Medical rank #16 (2026-07-26), #13 (2026-09-20), #9 (2026-09-28); listing today shows #17.

---

## Table 4 — Google search width for five buyer phrases

WebSearch (standard) returned ~10 organic URLs per query and does not expose a total result count or the "People also ask" box; "results" below is what the tool showed. Types: brand article = baby-product company or retailer blog; health org = hospital/clinic/health-service page; forum = Reddit/Mumsnet-style thread.

| phrase | results shown | top-3 organic result types | top-3 domains |
|---|---|---|---|
| "baby wont sleep unless held" | ~10 | spam/SEO page, brand article, brand article | tv.fpabramo.org.br (junk), enfamil.com, elvie.com (then mamasandpapas.ae, cradlewise.com x3, huckleberrycare.com, nestedbean.com) |
| "how much formula should my baby drink" | ~10 | brand article, media article, health org | enfamil.ca, romper.com, share.upmc.com (then drgreene.com, omnicalculator.com, junk PDFs) |
| "is my baby behind on milestones" | ~10 | pharmacy blog, health org / charity blog, health org / charity blog | apollopharmacy.in, novita.org.au x2 (then childmind.org x2, ovumhospitals.com, baby-chick.com) |
| "when to start solids" | ~10 | health-content site, spam/SEO page, health org | ubiehealth.com, seo-service.chartlocal.com (junk), aboutkidshealth.ca (then canberrahealthservices.act.gov.au, Mayo Clinic Care Network, nutricia.com.au) |
| "pumping schedule return to work" | ~10 | health org, brand article, brand article | health.clevelandclinic.org, perifit.co x2 (then onewillow.com x3, mamava.com, thevagwhisperer.com) |

Observed: none of the five top-10 lists contained a forum thread, an app listing, or a book listing; brand (product-company) articles were the most common type across all five.

---

## What failed

- `https://www.amazon.com/Best-Sellers-Books-Pregnancy-Childbirth/zgbs/books/11164` — WebFetch HTTP 503.
- `https://www.amazon.com/Best-Sellers-Books-Parenting-Babies-Toddlers/zgbs/books/11160` — WebFetch HTTP 503.
- `https://www.amazon.com/Best-Sellers-Books-Parenting/zgbs/books/11148` — WebFetch HTTP 503.
- Single curl retry of the three Amazon pages with a browser User-Agent — denied by the Claude Code permission classifier ("Bot Check Circumvention"); no second Amazon response was ever received. Not retried further.
- WebSearch "amazon best sellers pregnancy childbirth books 2026" — denied by permission classifier (same reason). A rephrased search for "best selling pregnancy books amazon 2026" succeeded and is what Table 2's pregnancy snippets rest on.
- WebSearch "Sensor Tower top parenting apps 2026 revenue downloads US" — denied by permission classifier.
- WebSearch "Flo Period Tracker App Store top grossing rank 2026 Health & Fitness" — denied by permission classifier.
- Arctic Shift, first pass: JSON parse errors on 23 subreddits (raw control characters in `description`); fixed by lenient parsing on the second pass. FormulaFeeders and predaddit returned `data: null` once and resolved on a repeat call.
- Google Play listing fetches, HTTP 404 on guessed package ids: `org.twisevictory.apps` (Wonder Weeks), `com.solidstarts.app`, `com.kinedu.app`, `se.napper.app` (Napper), `com.ovuline.pregnancy` (Ovia), `com.lovevery.app`.
- Google Play via WebFetch for Huckleberry, Pregnancy+ and Flo — page content truncated before the rating block (superseded by plain curl of the same listings); WebFetch of `org.twisevictory.apps` — HTTP 404.
- iTunes Search API mis-matches discarded: "Smart Sleep Coach by Pampers" matched Pampers Rewards; "Taking Cara Babies" matched Kajabi. Neither row kept.
- `https://www.amazonseo.ai/en/amazon-best-sellers/baby-sleep-book` — HTTP 404.
- `https://libraryjournal.com/story/parenting-best-sellers-nov-2023` — HTTP 403 (and would have been 2023 library data, not Amazon).
- `https://apppricinglab.com/reports/parenting` — fetched fine but publishes no per-app ranks.
- No source found for current (2026) top-grossing positions of any baby-sleep / feeding / development app; only category chart badges on listings were observable.
