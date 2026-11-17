# Original reviews, books and YouTube — collection and reading ledger

Captured 2026-10-24. This branch contributes **171 App Store review quotes and 9 Apple Books review quotes**, from **190 complete original review units read**. Quotes describe selected reviewers, not the customer population, market share, causal efficacy, conversion or willingness to buy Mamivio. All excerpts have a source URL, review id and saved raw source.

## Method and access

The original brief is `_tools/brief-reviews-media.md`. `_tools/collect_app_reviews.py` was adapted around the copied source-capture pipeline. The public Apple app page route `https://apps.apple.com/<us|gb>/app/<slug>/id<id>?see-all=reviews` returned HTTP 200 for every one of 18 app/storefront combinations. Untouched HTML is under `_raw/reviews/`; complete review bodies were extracted from its `serialized-server-data` into immutable `*-corpus.txt` and `*-reviews.units.json`. Original bodies are present in the public HTML, not fetched through a private API. Names were not included in quote/context fields.

**The full-review route was explicitly probed.** Despite the `see-all=reviews` parameter, each captured `allProductReviews` shelf exposes exactly 10 user review units. Its `url`, `seeAllAction` and `footerAction` are null, `fetchStrategy` is `onPageLoad`, and `itemCount` says `all`. `_raw/reviews/public-route-audit.json` preserves these exact fields for all 18 routes. There is no visible continuation URL. We did not treat the UI's word “all” as the entire historical review archive. Ratings in these 10 units can range from 1 to 5 stars; selection is Apple's, not a recent-date or random sample. Some reviews are many years old. The captures establish what reviewers said then, not current product behavior.

Apple's `apps.apple.com/robots.txt` permits these app pages but disallows its API routes. `itunes.apple.com/robots.txt` disallows `/*/rss/*`; therefore RSS was not harvested. Both policies are saved. We did not invent a review pagination endpoint or bypass that restriction. Unrestricted review archives remain a gap.

Apple Books public product pages similarly permit retrieval; `_raw/books/apple-books-robots.txt` is saved. Fourteen product captures cover 13 distinct books (Cribsheet has two source pages). Ten visible original customer-review units were saved in `_raw/books/review-units.json`; all ten were read, nine selected. The omitted unit is a two-word Spanish review. Publisher descriptions, editorial reviews and seller-selected endorsements are kept separate from buyer evidence. We read product description/price sections, not the books themselves.

## Ledger

Units are complete original reviews, except the last two rows. “Kept” here means retained in the frozen reading corpus; every retained review was read. Nine app reviews and one book review produced no selected quote. All 180 App Store review ids were unique, including across storefronts. Detailed review-by-review status: `_raw/reviews/reading-ledger.tsv`.

| Source | Downloaded | Matched | Triaged | Kept | Full-read | Quotes |
|---|---:|---:|---:|---:|---:|---:|
| Kinedu, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| BabySparks, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| Huckleberry, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| Napper, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| Solid Starts, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| BLW Meals, US + GB | 20 | 20 | 20 | 20 | 20 | 20 |
| The Wonder Weeks, US + GB | 20 | 20 | 20 | 20 | 20 | 16 |
| Pump Log, US + GB | 20 | 20 | 20 | 20 | 20 | 16 |
| Baby Daybook, US + GB | 20 | 20 | 20 | 20 | 20 | 19 |
| Apple Books visible customer reviews | 10 | 10 | 10 | 10 | 10 | 9 |
| Book product-description units | 13 titles / 14 pages | 13 titles | 13 titles | 13 titles | 13 product units | 0 buyer quotes from descriptions |
| YouTube initial metadata probe | 5 metadata rows | 4 instructional | 5 | 4 | 4 title/metadata units | 0 comment quotes |

Two Pump Log reviews centered on acute/very-premature NICU experiences were read but excluded from marketing evidence. Other unquoted app reviews were redundant interface complaints, generic short praise or outside the narrower decision need. No raw file was removed to hide omissions. No review was screened only by title and then reported as a full read.

## What was read and what remains unread

| Material | Status |
|---|---|
| `_raw/reviews/{kinedu,babysparks,huckleberry,napper,solidstarts,blwmeals,wonderweeks,pumplog,babydaybook}-{us,gb}-corpus.txt` | All 18 corpora read in full; all 180 complete original reviews |
| `_raw/books/review-units.json` | All 10 original review bodies read in full |
| Thirteen book product-description/price units referenced in `books/README.md` | Read as product units; the books themselves were not read |
| `_raw/books/cribsheet.txt` | Parent completed the full 833-line supplementary publisher capture during final audit, including unrelated embedded promotional material. No new title or buyer quote; primary book note still uses `cribsheet-apple.txt` |
| App descriptions, release histories and privacy details outside the review shelves | Not comprehensively read. Captured HTML includes them; no completion claim |
| Complete historical Apple review archives | Not downloaded; no permitted continuation route found |
| `_raw/youtube/probe-search.tsv` | All five title/metadata rows read; one personal baby clip excluded from instructional shortlist |
| YouTube full videos/transcripts/comments | None collected or read |
| Books in full, licensed ebooks, Amazon historical reviews | Not downloaded/read |

## Source-specific limitations and continuation

See `reviews-media-not-harvested.md` for robots and HTTP failures, and `synthesis/youtube-top-videos.md` for the unmet top-200 target. Goodreads bans GPTBot; Trustpilot direct collection returned a bot/terms 403; YouTube robots prohibits search/internal continuation routes. No circumvention was attempted.

To extend permissible Apple coverage: inspect new public UI routes if Apple exposes them, retain new captures under new names, then build new corpus chunks and a new quote prefix. Do not overwrite this batch. Other English-speaking storefronts can add geographic voices but will still be Apple-selected lists, not exhaustive data. Google Play, Kobo/other original retailer lists and licensed books remain unprobed continuation sources. One reader can process one 35–45 KB chunk per task; an additional 200 reviews of similar length would require about 4–6 such chunks plus capture/triage and audit. Capture volume does not determine saturation.

## Jargon and interpretation boundaries

FTM = first-time mother; BLW = baby-led weaning; EP = exclusive pumping; “stash” = stored expressed milk; “wake window” = waking interval used in sleep planning; “leap” = The Wonder Weeks' proposed explanatory schedule, not a validated mechanism in this research. Reviewers' use of scientific language is not proof of credentials or clinical correctness. A child's diagnosis appears only as context where necessary; treatment and feeding schedules were not quoted as instructions.
