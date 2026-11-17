# Missing, restricted and deliberately separate sources

2026-10-24. An access failure is not evidence that a community or business does not exist. No bot-wall/captcha workaround, cookie extraction, alternate proxy or private-group access was used. Exact URLs, HTTP statuses, response files and policy reasons are recorded in the linked ledgers below; this is the cross-source index.

| Source | Observed outcome | Detailed evidence / continuation |
|---|---|---|
| Live Reddit routes | Direct JSON 403 and crawler restrictions remain. A separate public publisher archive now supplies 112,665 dated posts across nine communities | `reddit-deep.md`; original post collection is no longer missing. Seven main/country comment archives remain unavailable; current live threads not collected |
| Direct Arctic Shift host | HTTP 403 / error 1010 remains | `_raw/communities/probes/arctic-newparents.txt`; no direct-host archive access. Independent published source files are documented separately in `reddit-deep.md` |
| BabyCenter, What to Expect, BabyandBump, PregnancyForum, Mothering | Saved robots/terms restrict automated/AI/commercial collection | `communities.md`; not harvested |
| Mumsnet, Netmums, HealthUnlocked | Robots/access 403 | `community-access.jsonl`; not harvested |
| Parenting Stack Exchange website | Site crawler route restricted; documented official API separately inspected and used | `qa-deep.md`: 1,155 dated questions, 248 candidates with 514 answers / 1,356 comments collected via the official API; 119 kept threads fully read. No restricted website crawl |
| Apple full review history | Public pages 200, but only 10 app reviews per storefront and no exposed continuation | `reviews-media.md`, `_raw/reviews/public-route-audit.json`; exposed units read, history missing |
| Apple RSS/API | Saved robots restrictions | `reviews-media-not-harvested.md`; no prohibited RSS/private API requests |
| Goodreads | Robots explicitly bans GPTBot | `reviews-media-not-harvested.md`; original review lists uncollected |
| Trustpilot | Solid Starts page returned 403 bot/terms response | `_raw/reviews/solidstarts-trustpilot-page1.html`; no archive |
| YouTube search/comments | Initial metadata probe worked; subsequent policy inspection disallowed search/internal/comment routes | `../synthesis/youtube-top-videos.md`; four instructional metadata entries and a later 30-item channel-page probe, no top-200/videos/comments corpus |
| Restricted competitor domains | Robots/access errors or prohibitions; some public App Store descriptions used instead | `competitors-not-harvested.md`; no claim of original-domain checkout/contents access |
| Marketplace parenting inventories | Wave-two probes and outcomes are in the competitor ledger | Session/login shells or unavailable public routes do not establish zero offers |
| Google Play full review history | Seven public app detail pages returned 200 and exposed three original reviews each; all 21 read; robots restrict review/internal continuation endpoints | `reviews-followups.md`, `_raw/reviews-followups/googleplay-route-audit.json`; full history remains uncollected |
| Amazon US | Saved robots policy explicitly bans both GPTBot and ChatGPT-User; no review-page request followed | `_raw/reviews-followups/amazon-robots.txt` and headers; review lists uncollected under policy restriction |
| Kobo | Three permitted public book routes returned 403 and exposed no review bodies | `reviews-followups.md`; exact routes and saved response/header paths recorded; no workaround |
| Barnes & Noble book-review archives | Eight current public edition lists returned 200; all five exposed reviews read, all five-star and unverified purchases; five lists reported zero | `reviews-followups.md`, `reviews-followups-ledger.json`; no claim of a complete historical archive or accessible low-star material |
| Full books, paid courses/reports, consultations, post-purchase delivery | Not purchased or accessed | Public descriptions are not full-content reads or efficacy evaluation |
| Owner customers, private groups, Discord, TikTok/Instagram comments | No owner data/access supplied; private sources not accessed, social comment archives not collected | `owner-data.md`; obtain consented material or a permitted public route rather than infer its contents |

The source map records actual access and reading outcomes, with remaining gaps; it is not a completion claim. Publication rankings, complete historical archives, clinical outcomes, market size, launch-country purchasing behavior and Mamivio sales economics remain unmeasured. The saved public evidence can support testable product hypotheses; it cannot fill these gaps by inference.

## Reopened forum sweep

The original broad forum row is supplemented by 54 candidate URL/host probes (51 after www collapse): `forums-deep-discovery.md` and `forums-deep-access.jsonl`. JustParents supplies 505 complete visible thread captures; the retained reading state is in `forums-deep.md`. Saved canonical content/policy responses distinguish explicit bans, challenges, login walls and unknown policies. An inaccessible robots file is not itself called a ban.

Additional oblique probes and actual source outcomes: `oblique-deep-access.json`, `oblique-deep.md`. MSE supplies 343 captured threads; the publisher-redirected GeoBaby archive supplies 183. DCUrbanMom’s explicit reuse-permission requirement, CityData/ExpatForum AI bans, other host/robot/challenge failures are recorded separately. Neither historical forum advice nor public access supplies legal, safety or medical validation. No denied host was bypassed.

Uncollected main communities include r/pregnant, r/Mommit, r/breastfeeding and r/sleeptrain as dated bulk corpora; any old indexed extracts are not such a harvest. These are source gaps, not empty communities. Nine collected Reddit communities and the exact unread six-month tiers remain in `reddit-deep.md`.

Newly probed Nappy Lady: robots 200 allows normal routes; homepage 403, no bypass or current questionnaire capture (`market-deep.md`). Historical forum mentions are not proof of its current terms or offer. Seven new report/registry offer pages were fully read; one further captured page was held unread after a linked agent policy required unavailable authentication. See `market-deep.md`.
