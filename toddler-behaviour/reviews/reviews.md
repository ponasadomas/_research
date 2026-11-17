# App and book reviews — RV1 collection and completed recovery

**Current state — 2026-11-16:** 162 review quote records (119 app + 43 book), from 114 distinct review units. The original 121 saved review units were read in RV1; the 35 recovery review blocks have all been re-read, yielding 28 additional quotes from 26 units. Seven saved review units still yield no quote; none of the recovery blocks is unread or missing. Review age, rating, claimed outcomes and source class remain explicit. The new records are in `voice/reddit-ur*.jsonl`; all are included in `voice-merged/all.jsonl` and §15 of the findings.

**Historical RV1 collection, 2026-10-25.** Reader RV1, brief `../_shared/_tools/brief-books-apps.md`. Voice file `voice/reviews-rv1.jsonl` (ids `tbr1-0001`–`tbr1-0134`), **134 verbatim quotes from 121 complete review units, all 121 read in full**. `python3 -I _tools/verify_quotes.py voice/reviews-rv1.jsonl` → `134 quotes, 0 failed`. Unit-by-unit read status and quote ids: `_raw/reviews/reading-ledger-rv1.tsv`. Quotes are selected reviewers, not a sample of buyers; ratings and storefront selection are Apple's, Google's and Yotpo's, not ours. No purchases, no sign-ups, no logins.

## Method

- **App Store:** public app pages `https://apps.apple.com/<cc>/app/<slug>/id<id>?see-all=reviews` for us, gb, ca, au; review bodies taken from the page's `serialized-server-data` by `_tools/collect_app_reviews.py` (copied from `global/_tools/`, apps and storefronts adapted, refuses to overwrite). Raw HTML, headers, `*-reviews.units.json` and frozen `*-corpus.txt` in `_raw/reviews/`; manifests `appstore-collection-manifest*.json`. Apple caps each storefront at 10 units; small apps expose fewer.
- **Google Play:** public detail page `https://play.google.com/store/apps/details?id=<pkg>&hl=en_US&gl=US`, once per app (robots disallows `/store/getreviews`, `/store/search`, `/_`; none requested). `_tools/extract_play_reviews.py` froze the 3 exposed bodies per page into `_raw/reviews/googleplay-<app>.txt` (names dropped; developer reply kept and marked). Package ids found on third-party pages because Play search is robots-disallowed.
- **Barnes & Noble:** `https://www.barnesandnoble.com/w/?ean=<ISBN>` (robots-permitted product route; `/search` disallowed) → the page's own Yotpo product id and the other format products of the same title → public Yotpo list `https://api-cdn.yotpo.com/v3/storefront/store/<appKey>/product/<id>/reviews?page=N&perPage=8` (api-cdn robots allows `/v3/storefront/store/*`; same route as `global/sources/reviews-followups.md`). `_tools/collect_barnes_reviews.py`. Formats of one title share one review list; units are de-duplicated in `_raw/books/barnes-<title>-corpus.txt`. Every list fitted in one page.
- **Apple Books:** `https://books.apple.com/us/book/isbn<ebook ISBN>` resolves to the book id, then the same id in gb/ca/au (robots disallows only `/WebObjects/*`, `/v1/catalog/*`). About 3 visible reviews per storefront page. `_tools/collect_apple_books.py`; HTML in `_raw/books/_html/`, corpora `_raw/books/apple-<title>-corpus.txt`. Good Inside needed a second run (`good-inside-2`): the US ebook ISBN 9780063159471 and the UK Thorsons edition (gb id1611103241).
- Robots files saved: `_raw/reviews/apps-robots.txt`, `_raw/reviews/googleplay-robots.txt`, `_raw/books/barnes-robots.txt`, `_raw/books/yotpo-robots.txt`, `_raw/books/apple-books-robots.txt` (with headers).

## Historical RV1 ledger

Downloaded = complete review units exposed and frozen; all were read in full. Quotes = quotes written (several per unit allowed).

| Source | Units saved | Read | Quotes |
|---|---:|---:|---:|
| App Store Good Inside: Parenting (id6463803046), us/gb/ca/au 10+10+10+10 | 40 | 40 | 46 |
| App Store Potty Whiz (id1493987452), us 10, gb 9, ca 5, au 3 | 27 | 27 | 27 |
| App Store POTTR (id6757593828), us 1 (gb/ca/au 0) | 1 | 1 | 3 |
| App Store Potty Training App, Tuncer Tirnavali (id6760347375), us 1, ca 1 | 2 | 2 | 2 |
| App Store Potty Path (id6782207608), all four storefronts | 0 | 0 | 0 |
| App Store RootWise (id6751473328), us/gb/ca 0, au HTTP 404 | 0 | 0 | 0 |
| App Store LittlePath (id6761305309), us 2 | 2 | 2 | 3 |
| App Store AI Parenting Coach (id6451044904), us 1, gb 2, ca 1 | 4 | 4 | 1 |
| App Store ParentPal (id6463043510) | 0 | 0 | 0 |
| App Store Granny: AI Parenting Coach (id6466166824), us 3, gb 1 | 4 | 4 | 3 |
| Google Play Good Inside (com.goodinside.gimobile) | 3 | 3 | 5 |
| Google Play Potty Whiz (app.kidplay.pottywhiz) | 3 | 3 | 5 |
| Apple Books Oh Crap! Potty Training (id979258666), us 3, ca 3, au 3, gb 0 | 9 | 9 | 13 |
| Apple Books Good Inside (us/ca id1592814326, gb id1611103241), us 2, gb 1, ca 1, au 404 | 4 | 4 | 7 |
| Apple Books How to Talk So Little Kids Will Listen (id1091029280), us 2 | 2 | 2 | 2 |
| Apple Books The Whole-Brain Child (id422546879), us 3 | 3 | 3 | 3 |
| Apple Books The Happiest Toddler on the Block (id419970256), us 2 | 2 | 2 | 1 |
| Apple Books Hunt, Gather, Parent (id1521391809), us 3 | 3 | 3 | 2 |
| Apple Books No Bad Kids (id6477836596), Potty Training in 3 Days (id6756086855) | 0 | 0 | 0 |
| Barnes & Noble Good Inside (hardcover + audio CD list) | 2 | 2 | 3 |
| Barnes & Noble Oh Crap! Potty Training (2015 pb, ebook, new edition: one shared list) | 1 | 1 | 1 |
| Barnes & Noble The Happiest Toddler on the Block (pb + ebook) | 5 | 5 | 4 |
| Barnes & Noble Hunt, Gather, Parent (hc + pb) | 1 | 1 | 2 |
| Barnes & Noble The Whole-Brain Child (pb + ebook) | 2 | 2 | 0 |
| Barnes & Noble Hands Are Not for Hitting (board book) | 1 | 1 | 1 |
| Barnes & Noble How to Talk So Little Kids Will Listen, No Bad Kids, Potty Training in 3 Days (pb + ebook each) | 0 | 0 | 0 |
| **Total** | **121** | **121** | **134** |

By class: App Store 80 units / 85 quotes; Google Play 6 / 10; Apple Books 23 / 28; Barnes & Noble 12 / 11. At the RV1 stage, 31 units were read and not quoted (one-word praise, adult self-tracking reviews of Potty Whiz, an adult's own medical condition, older-child or custody detail, professional endorsements with nothing new). The POTTR and Potty Training App units are also in `competitors/potty-apps-more.md`; only parts not already quoted there were taken.

## Not reachable or not existing

Full log with HTTP statuses: `reviews-not-harvested.md`. In short: no Big Little Feelings app exists (its courses play in the Kajabi app; a third-party analytics page that may describe a BLF app returned 403); no Google Play listing was found for POTTR, Potty Path, Potty Training App, RootWise or LittlePath; Hands Are Not for Hitting has no Apple Books page at any ISBN tried; several Apple Books ids 404 in gb/au because those storefronts sell another edition under a different id (only Good Inside's UK id was resolved); B&N's 2014 self-published No Bad Kids ISBN 404s. Goodreads and Amazon were not fetched (robots ban). Complete review histories are not reachable on any of these routes.

## Quote notes

- Speaker is `reviewer` throughout; no names. Stage is `unknown` unless the review gives the child's age.
- Themes added beyond the README seeds: `oh_crap` (as the Reddit readers used it). App features (paywall, sync, AI chat) sit under `price_value`, `partner_disagreement` and `personalization`; the `context` field names the feature.
- LittlePath's only two reviews (5★, 2026) and Granny's three 5★ reviews from two days in 2023 read like launch reviews; their independence is unknown, and the context says so.
- tbr1-0076 is a reviewer's own "in just 4 weeks" result. Its exact words remain ordinary evidence about one family; any later copy decision belongs to the owner.

## Historical marking list — retired 2026-11-16

The following old reasons are preserved as history. They impose no current restriction on research, quotation or access; the owner makes later copy decisions. All five full saved quotations remain in the findings.

| id | why |
|---|---|
| tbr1-0058 | from a review that names the child's autism diagnosis (the quote itself is about a paid subscription) |
| tbr1-0059 | medical treatment detail (supplements for withholding) and the review names the child as autistic |
| tbr1-0076 | reviewer's own day-count result ("in just 4 weeks"); not for copy |
| tbr1-0128 | about forcing a child onto the potty (harshness frame) |
| tbr1-0134 | child anxiety, counselling and therapy history (clinical frame) |

## How to continue

Do not re-run the collectors on existing names (they refuse). New storefronts or titles: add keys and pass them as arguments (`collect_app_reviews.py <app>`, `collect_apple_books.py <title>`), then a new reader prefix. Worth trying: gb/au Apple Books ISBNs for Oh Crap, No Bad Kids (Vermilion 9781785045981 / ebook 9781529959796), Hunt Gather Parent and Whole-Brain Child UK editions; Oh Crap! I Have a Toddler and Janet Lansbury's other titles; Moms on Call and BLF's Kajabi-hosted course pages have no public reviews.


## Completed recovery — 2026-11-16

UR01–UR09 found and read all 35 queued review blocks. They added 24 app-review and four book-review quotes, verified as literal contiguous excerpts in the individual REVIEW blocks. This changes the review total from 134 to 162; it does not add new downloaded units or claim a representative buyer sample. Twenty-four previously unquoted units now contribute quotes; two previously quoted units contribute additional passages. The nine other queued blocks add no new quote, as explained in the UR ledgers. Original RV1 and UR voice files and reader ledgers were not modified during synthesis integration.
