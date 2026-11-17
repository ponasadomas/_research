# Competitor follow-up source ledger — 2026-10-24

Brief: `_tools/brief-market-followups.md`, written before collection. Manifest and wrapper: `scratchpad/market-wave2/manifest.json`, `capture.py`; access log: `sources/competitor-access-wave2.jsonl`. Original-wave manifests/raw/market-01 ids remain unchanged.

12 target pages: 11 captured successfully (HTTP 200), one original-domain target excluded after robots denied GPTBot. The five named follow-up offers were all inspected, with Annabel Karmel covered through its permitted App Store developer listing. These yield seven individual notes, including the additional 28-day guide and Orango chosen-duration plan app.

| Class | Downloaded valid pages | Matched | Triaged | Kept | Full reads | Offer excerpts |
|---|---:|---:|---:|---:|---:|---:|
| First-party offers and developer listings | 11 | 11 | 11 | 11 | 11 | 16 |

| Frozen raw text | Downloaded | Matched | Kept | Read | Offer excerpts |
|---|---:|---:|---:|---:|---:|
| `_raw/competitors/starting-solids-baltsevich.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/my-little-food-critic.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/my-little-food-critic--appstore.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/my-little-food-critic-28day.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/babyplate.txt` | 1 | 1 | 1 | 1 | 3 |
| `_raw/competitors/little-lunches.txt` | 1 | 1 | 1 | 1 | 2 |
| `_raw/competitors/little-lunches--pricing.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/little-lunches--grocery.txt` | 1 | 1 | 1 | 1 | 0 |
| `_raw/competitors/little-lunches--appstore.txt` | 1 | 1 | 1 | 1 | 1 |
| `_raw/competitors/orango-blw-recipes.txt` | 1 | 1 | 1 | 1 | 3 |
| `_raw/competitors/annabel-karmel--appstore.txt` | 1 | 1 | 1 | 1 | 2 |

## Reading method and what is not read

Six page texts were read directly in full: Starting Solids, Orango, Little Lunches mealplans/pricing/grocery and MLFC 28-day plan. The other five were read through `scratchpad/market-wave2/*-reading-view.txt`. Those views retain every exact distinct line not already read in those six texts or an earlier view; repeated country/navigation lines and duplicated reviews are folded, not selected by theme. Thus all substantive extracted text was read, while original captures remain frozen and every quote points to its original raw text. Views are reading aids, not original-source provenance.

`_raw/competitors/little-lunches--browser.json` is a supplementary real-browser capture of the public mealplans page; it corroborates visible marketing content and does not count as a twelfth independent page read. No signup or generated plan was submitted. The chat subdomain query/signup branch was not followed after its robots file disallowed query-based crawling.

Search-response captures `followup-discovery-1.txt` through `followup-discovery-5.txt` are discovery artifacts and do not count as original-page reads or representative market samples. Exact title/url linkage for Annabel Karmel came from the existing permitted MLFC App Store page. The unsuccessful exact-name search is recorded in `_raw/marketplaces/market-followup-discovery-6.txt`.

All eleven retained successful page texts have been read. Paid contents, generated meal plans, actual checkout options, true subscription counts and outcomes are unexamined. Related-app recommendations remain non-exhaustive discovery; no claim of every serious current app covered is justified.

## Access gap

`https://www.annabelkarmel.com/the-ultimate-baby-toddler-recipe-app/` was not fetched after its robots response (HTTP 200) disallowed GPTBot. Saved policy: `_raw/competitors/robots/www.annabelkarmel.com.txt`. The permitted App Store listing was a separate first-party developer source, not a workaround to access the blocked domain.

## Verification

`market-02.jsonl: 16 quotes, 0 failed`

Cumulative market records: 43. Cumulative individual notes: 34. Cumulative successful offer/support page reads: 41. Marketplace probes are logged separately and excluded from these totals.

## Continuation

The named follow-up assignment has no retained successful page left unread. A concrete next step is evaluation of generated outputs for shortlisted apps if separately authorized; until then reported functionality remains seller description. New related apps exposed include Tummi, Starting Solids & Baby Food, BabyEatGood and Tocomo; they are leads, not claims of proven commercial significance.
