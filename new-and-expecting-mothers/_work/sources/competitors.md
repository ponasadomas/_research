# Competitor source ledger — 2026-10-24

Method: buyer-query discovery, then first-party public offer-page capture. This is not a bulk market census. Saved HTML is untouched response content; text is mechanically extracted with the copied SYD `fetch_page.py`. Robots responses and exact access statuses are retained. The reader read every retained successful extracted page in full, including the displayed review/version sections on the two App Store pages; customer reviews were not quoted into the market file. No account, purchase or consultation was submitted.

Collection manifest: `scratchpad/market/manifest.json` and `manifest-extra.json`; wrapper: `scratchpad/market/capture.py`. Curated facts: `scratchpad/market/notes.json`; renderer: `_tools/build_market_notes.py`. Never overwrite cited captures when refreshing; use a new dated suffix.

## Totals — original wave

39 page targets across 32 origin hosts; 30 successful offer/support page responses; 1 HTTP 404 body; 8 page targets not fetched after robots/access checks. HTTP 404 is an access record, not an offer-page read. Successful-page count includes three supplementary pages (Pathways app, Napper pricing, Every Mother recovery), so it differs from the 27 individual notes.

| Source class | Downloaded valid pages | Matched | Triaged | Kept | Read in full | Excerpts |
|---|---:|---:|---:|---:|---:|---:|
| First-party offers, official free substitutes, and developer App Store descriptions | 30 | 30 | 30 | 30 | 30 | 27 |

The 27 excerpts are all offer statements; they are **not 27 customer voices**. Source class `competitor`, evidence kind `seller_claim` except the official CDC resource description. Counts describe this selected corpus only.

## Per-page ledger

| Raw text (relative to research) | Downloaded | Matched | Kept | Read | Excerpts |
|---|---:|---:|---:|---:|---:|
| `_raw/competitors/pirmi-zingsniai.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/pirmi-pregnancy.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/kinedu.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/kinedu-assessment.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/babysparks.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/pathways.txt` | 1 | 1 | 1 | 1 | 0 |
| `_raw/competitors/lovevery.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/cdc-milestone-tracker.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/huckleberry.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/taking-cara-babies.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/smart-sleep-coach.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/napper.txt` | 1 | 1 | 1 | 1 | 0 |
| `_raw/competitors/boob-to-food.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/101-before-one.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/latch-on-to-me.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/honey-and-milk.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/udder-love.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/wellspring.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/postpartum-plan.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/expecting-empowered.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/every-mother.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/expect.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/modern-motherhood.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/beyond-birthing.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/rooted-birth.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/solid-starts-appstore.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/blw-social-appstore.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/napper--pricing.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/every-mother--postpartum.txt` | 1 | 1 | 1 | 1 | 0 |
| `_raw/competitors/pathways--app.txt` | 1 | 1 | 1 | 1 | 1 |

## Read and unread

All 30 successful page text captures listed above were read in full. Raw HTML, JavaScript/bootstrap content, images and videos were saved or linked but not line-by-line interpreted as content; only extracted public text is counted as read. The eight `_raw/competitors/discovery-*.txt` search-response captures are discovery artifacts, not original-page full reads or an independently sampled market. Source access records, robots files and the mothers-plan 404 response were inspected for access/freshness rather than counted as audience/offer evidence.

The paid resources linked by every offer, all account-only content and any consultation deliverables remain unread/unpurchased; no files for those contents exist locally. Follow-up candidates are listed in `competitors/README.md`. No valid retained page is silently waiting to be read.

## Verification

`market-01.jsonl: 27 quotes, 0 failed`

`TOTAL 27 quotes, 0 failed`

`TOTAL 27 verbatim lines, 0 failed` (competitor verifier).

## Continue

Inspect fresh public pages for access-limited offers when access permits; do not change agents/cookies or solve walls to get around a restriction. Verify applicable plan and availability in a real browser without submitting personal/payment data. Interview parents about an actual report preview rather than interpreting price pages as willingness to pay. A further 20–30 permitted offer pages would be roughly 3–5 reading chunks of 45 KB; the current note corpus has no unread successful pages.

## Follow-up wave and cumulative ledger

The initial wave above is preserved as history. All five named first-solids follow-ups were inspected in a second wave; details and per-page read paths are in `competitors-wave2.md`. New material is in `voice/market-02.jsonl`, with fresh mkt02 ids.

| Wave | Downloaded valid pages | Matched | Kept | Read | Offer excerpts | Individual notes |
|---|---:|---:|---:|---:|---:|---:|
| Original | 30 | 30 | 30 | 30 | 27 | 27 |
| First-solids follow-up | 11 | 11 | 11 | 11 | 16 | 7 |
| **Cumulative** | **41** | **41** | **41** | **41** | **43** | **34** |

Affiliate marketplace URLs/robots were actually probed in the follow-up wave. None produced a full relevant inventory; see `marketplaces.md`. These access-only captures are excluded from offer-page counts.
