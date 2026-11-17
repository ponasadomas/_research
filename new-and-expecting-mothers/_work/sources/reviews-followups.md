# Review-source follow-ups — 2026-10-24

This is an additive follow-up to `reviews-media.md`. Original batch counts and raw corpora remain frozen. New evidence: **21 original Google Play reviews and 5 original Barnes & Noble/Yotpo book reviews, all 26 read in full and quoted** in `voice/reviews-followup-01.jsonl` (`revf01-0001` through `revf01-0026`). The written brief is `_tools/brief-reviews-followups.md`.

## Ledger and scope

| Source | Downloaded → matched → kept → read → quotes |
|---|---|
| Google Play, seven public app detail pages | 21 → 21 → 21 → 21 → 21 |
| Barnes & Noble/Yotpo, eight title/edition review lists | 5 → 5 → 5 → 5 → 5 |
| Kobo, three public product pages | HTTP 403; 0 review units |
| Amazon US | Policy inspected; review pages not requested under explicit crawler ban |
| YouTube direct watch page | 1 page, existing video metadata inspected; 0 comment bodies; 0 videos watched |

Machine-readable per-source counts and exact product URLs: `reviews-followups-ledger.json`. Individual review ids and read status: `_raw/reviews-followups/reading-ledger.tsv`. Quote counts are selected evidence, not people sampled from the market, customer prevalence or support for medical efficacy.

## Google Play — public originals accessible, bulk continuation restricted

Policy: `https://play.google.com/robots.txt`, HTTP 200, saved as `_raw/reviews-followups/googleplay-robots.txt` with headers. It permits public app detail pages but explicitly disallows `/store/getreviews`, `/store/xhr`, and `/_` routes. No prohibited backend was requested.

Explicit collection scope: every complete review body exposed by these seven public US-English detail pages, one capture per app on 2026-10-24:

| App | App id | Status | Original review bodies |
|---|---|---|---:|
| Huckleberry | `com.huckleberry_labs.app` | HTTP 200 | 3 |
| Solid Starts | `com.digitas.solidstarts` | HTTP 200 | 3 |
| Kinedu | `com.kinedu.appkinedu` | HTTP 200 | 3 |
| BabySparks | `com.babysparks.babysparks` | HTTP 200 | 3 |
| Napper | `com.napper` | HTTP 200 | 3 |
| Pathways.org | `com.pathwaysapp` | HTTP 200 | 3 |
| CDC Milestone Tracker | `gov.cdc.ncbddd.actearly.milestones` | HTTP 200 | 3 |

Exact route format: `https://play.google.com/store/apps/details?id=<app-id>&hl=en_US&gl=US`. Untouched HTML is `_raw/reviews-followups/_html/googleplay-<slug>.html`; extracted page text is `_raw/reviews-followups/googleplay-<slug>.txt`. `_raw/reviews-followups/googleplay-review-units.json` freezes all 21 original bodies, dates, platform review ids and ratings. Reviewer names are omitted from this extraction and the quote bank. Displayed developer responses were read with the reviews; resolved issues and later policy changes are preserved in context rather than treating an old complaint as current fact.

Each page exposes a “See all reviews” control, but no permitted next-page href was exposed in captured HTML. `_raw/reviews-followups/googleplay-route-audit.json` saves control fragments. We did not use internal batchexecute or review endpoints barred by the policy. This is a complete read of the 21 exposed bodies, **not a complete historical review harvest**. Google’s verification label is not treated as proof of a purchase or of a claim's accuracy.

Additional evidence, interpretation: `revf01-0003` gives a second-platform example of milestone inputs failing to alter activity recommendations; `revf01-0016` praises the free Pathways alternative over paid apps; `revf01-0019` wants the food list to reflect actual household foods; `revf01-0009` questions whether summaries improve on a spreadsheet. These are concrete objections and alternatives, not measurements of frequency.

## Amazon US — explicit policy exclusion

`https://www.amazon.com/robots.txt` returned HTTP 200. Its `User-agent: GPTBot` and `User-agent: ChatGPT-User` groups both say `Disallow: /`. Saved untouched policy and headers: `_raw/reviews-followups/amazon-robots.txt`, `amazon-robots.headers.txt`. No product/review requests or archive workarounds followed. Therefore Amazon review lists remain unharvested because of an observed policy restriction, not an assumption that there are no reviews. This probe applies to Amazon US only.

## Kobo — permitted routes return HTTP 403

`https://www.kobo.com/robots.txt` returned HTTP 200. The policy permits the English US/worldwide product routes attempted below. It is saved with headers as `_raw/reviews-followups/kobo-robots.txt`.

| Public product route | Status | Saved response |
|---|---|---|
| `https://www.kobo.com/us/en/ebook/precious-little-sleep-1` | HTTP 403 | `kobo-pls.html`, `.headers.txt` |
| `https://www.kobo.com/ww/en/ebook/baby-led-weaning` | HTTP 403 | `kobo-blw.html`, `.headers.txt` |
| `https://www.kobo.com/us/en/ebook/simple-safe-baby-led-weaning-1` | HTTP 403 | `kobo-simple.html`, `.headers.txt` |

Responses reference Kobo maintenance assets and expose no original review bodies. We did not infer an empty review history or retry through alternate hosts/cookies. No original Kobo reviews were read or quoted. Search-index descriptions were discovery only.

## Barnes & Noble — rendered public widget and permitted review lists

`https://www.barnesandnoble.com/robots.txt` returned HTTP 200 and permits the public product routes used. The saved policy is `_raw/reviews-followups/barnes-robots.txt`. We opened the Precious Little Sleep product page in a real browser and saved the rendered review widget as `barnes-rendered-review-widget.json`. That edition displayed an empty-review state.

The browser's own network traffic exposed the public Yotpo review-list URL. `https://api-cdn.yotpo.com/robots.txt` returned HTTP 200 and expressly allows `/v3/storefront/store/*`. Its policy and headers are saved. We used the same public route and page size observed in the rendered page, with product ids exposed in each saved public product page. No private credentials, login or hidden backend were used. Review-list response names end `-yotpo-reviews.json`; headers are also saved.

Explicit scope: all reviews currently returned for eight observed title/edition ids, using page 1, eight reviews per page. Each response's `pagination.total` was at most two, so there was no additional review page to fetch within these lists.

| Title/edition capture | Current reported list total | Stars represented | Full-read |
|---|---:|---|---:|
| `barnes-pls` — Precious Little Sleep ebook | 0 | none | 0 |
| `barnes-montessori` — The Montessori Baby | 0 | none | 0 |
| `barnes-blw` — Baby-Led Weaning | 0 | none | 0 |
| `barnes-first40` — The First Forty Days | 2 | five stars | 2 |
| `barnes-workpump` — Work. Pump. Repeat. | 0 | none | 0 |
| `barnes-cribsheet` — Cribsheet | 2 | five stars | 2 |
| `barnes-simplest` — The Simplest Baby Book | 1 | five stars | 1 |
| `barnes-baby-led-feeding` — Baby-Led Feeding | 0 | none | 0 |

All five exposed review units were read in full, saved in `book-review-units.json`, and quoted as `revf01-0022` through `revf01-0026`. All have `verifiedBuyer: false`, `syndicationData: null`; no verified-purchase claim is made. They add observations about acknowledged uncertainty, clear explanations, illustrations and another reader's understanding of new mothers. They do not provide the requested low-star book counterevidence. **No low-star book reviews are exposed in these eight current lists.** Zero totals are only what the current public widgets reported for these edition ids, not proof of no reviews elsewhere or historically.

## YouTube — permitted direct watch route checked

The saved YouTube policy in `_raw/youtube/robots.txt` allows `/watch` while restricting search/internal continuation routes. `https://www.youtube.com/watch?v=377j05F4edY` returned HTTP 200. Raw HTML: `_raw/reviews-followups/_html/youtube-watch.html`; derived embedded player JSON: `youtube-watch-player.json`. Read metadata fields: title, author, video id, duration, observed view count and upload date. The view count is 867,897, matching the earlier probe; the embedded upload date is 2021-01-07. This is an already known video, not a new discovery.

No `commentRenderer`, `commentViewModel` or `commentThreadRenderer` bodies occurred in the returned HTML. The description and remaining player payload were not fully read; the video itself was not watched. No transcript/comment continuation was requested. The top-200 and comment-corpus targets remain unmet; a permitted direct page does not turn the prohibited bulk pipeline into an authorized route.

## Verification and unread inventory

`reviews-followup-01.jsonl: 26 quotes, 0 failed`. After source-exact apostrophe corrections, the original and follow-up branches together also pass strict whitespace-only containment: **206 quotes, 0 failed**. Ids and counts were preserved. Selection/build literals were corrected so regenerated quotes retain source typography.

No retained follow-up review unit remains unread: all 21 Google Play bodies and all five retailer-book reviews were fully read. App descriptions/release histories and Barnes product sections outside the review units were not comprehensively read; their captured HTML remains on disk. Kobo error responses and robots policies were inspected. YouTube description/player fields beyond the listed metadata remain unread at the paths above. Complete historical Google Play/Apple/Amazon/Kobo review archives and full books remain uncollected.

Continuation: seek permitted original low-rating book lists or owner-supplied licensed exports. Recheck public retailer widgets if access or exposed data changes; preserve this snapshot under fresh filenames. With supplied bulk exports, budget one reader task per roughly 35–45 KB corpus chunk plus capture/triage/audit. Do not treat these source-access limits as demonstrated thematic saturation.
