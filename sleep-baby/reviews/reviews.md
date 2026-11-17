# App and book reviews — sleep-baby, reader RV1 (2026-10-25)

Brief: `../../_shared/_tools/brief-books-apps.md`. Voice file: `../voice/reviews-rv1.jsonl` (`sbr1-0001` → `sbr1-0234`). Blocks and HTTP statuses: `reviews-not-harvested.md`. Quotes describe the selected reviewers, not the market; a count is a count of quotes chosen.

**Check:** `python3 -I _tools/verify_quotes.py voice/reviews-rv1.jsonl` → `reviews-rv1.jsonl: 234 quotes, 0 failed` (2026-10-25). A second check confirmed every App Store and B&N quote sits inside the specific review its `review_key` names.

## Method

- **App Store:** `_tools/collect_app_reviews.py` (copied from `global/_tools/`, adapted: sleep-baby app list, id-only route `https://apps.apple.com/<cc>/app/id<id>?see-all=reviews`). Each page exposes 10 Apple-selected reviews; no RSS/API (robots-disallowed). Untouched HTML `_raw/reviews/<app>-<cc>-reviews.html`, frozen `<app>-<cc>-reviews.units.json`, reading corpus `<app>-<cc>-corpus.txt`, manifest `appstore-collection-manifest-rv1.json`. Huckleberry and Napper: ca + au only (us + gb are in `global/`); 0 review ids overlap with `global/`.
- **Google Play:** one public detail page per app (`hl=en_US&gl=US`), saved by `_tools/fetch_page.py` as `_raw/reviews/_html/googleplay-<app>.html` + `.txt`; 3 review bodies each. No `/store/getreviews` or batchexecute. Huckleberry and Napper Google Play pages are already in `global/_raw/reviews-followups/`: not re-fetched.
- **Barnes & Noble:** product page by ISBN (`/w/?ean=`) saved to `_raw/books/barnes-<slug>.txt`; the public Yotpo storefront review list (the route the B&N page itself calls; `api-cdn.yotpo.com/robots.txt` allows `/v3/storefront/store/*`), 8 per page, every page fetched (No-Cry: 8 pages for 63). Raw `barnes-<slug>-yotpo-reviews*.json`; reading corpora `barnes-<book>-corpus.txt` (names omitted); units `barnes-review-units-rv1.json`.
- **Apple Books:** product pages in us/gb/ca/au saved to `_raw/books/apple-<book>-<cc>.txt`; the visible "Customer Reviews" block read. Precious Little Sleep and Cribsheet: only the gb/ca/au storefronts (us is in `global/`).

## Ledger

Units = complete original reviews. Every unit saved was read in full. `speaker` is `reviewer` throughout (brief); the role the reviewer gives (new_mother, partner, relative_caregiver…) is in `segment`.

| Source | Units saved | Read | Quotes |
|---|---:|---:|---:|
| App Store Huckleberry (ca, au) | 20 | 20 | 22 |
| App Store Napper (ca, au) | 20 | 20 | 13 |
| App Store Nara Baby (us, gb, ca, au) | 40 | 40 | 18 |
| App Store Glow Baby (us, gb, ca, au) | 40 | 40 | 26 |
| App Store Little Ones (us, gb, ca, au) | 40 | 40 | 69 |
| App Store Happy Baby – Sleep & Tracker (us, gb, ca, au) | 40 | 40 | 12 |
| App Store Smart Sleep Coach by Pampers | 0 (HTTP 404 in all 4 storefronts: delisted; closing 2026-11-30) | 0 | 0 |
| Google Play Nara Baby | 3 | 3 | 1 |
| Google Play Glow Baby | 3 | 3 | 2 |
| Google Play Smart Sleep Coach by Pampers (still listed on Play) | 3 | 3 | 2 |
| Google Play Little Ones | 3 | 3 | 2 |
| Google Play Happy Baby | 3 | 3 | 0 |
| Barnes & Noble The No-Cry Sleep Solution (paperback 9780071381390) | 63 (54 distinct texts; Yotpo lists some reviews 2–3 times under different ids) | 63 | 47 |
| Barnes & Noble Twelve Hours' Sleep by Twelve Weeks Old (hardcover 9780525949596 and ebook 9780593719398 return the same 7) | 7 (6 distinct) | 7 | 4 |
| Barnes & Noble The Happy Sleeper (9780399166020) | 2 | 2 | 2 |
| Barnes & Noble Healthy Sleep Habits, Happy Child 4th ed. (9780553394801) | 0 (list total 0) | 0 | 0 |
| Barnes & Noble The Sleep Lady's Good Night, Sleep Tight (pb 9780738286136, ebook 9780738286143) | 0 (both totals 0) | 0 | 0 |
| Barnes & Noble On Becoming Babywise (2019 ed. 9781932740509) | 0 (total 0) | 0 | 0 |
| Apple Books The Happy Sleeper (us 2, ca 1) | 3 | 3 | 3 |
| Apple Books The No-Cry Sleep Solution (us 3, gb 1, ca 1) | 5 | 5 | 4 |
| Apple Books Healthy Sleep Habits, Happy Child (gb) | 1 | 1 | 2 |
| Apple Books Moms on Call Basic Baby Care 0-6 Months (us) | 3 | 3 | 3 |
| Apple Books Twelve Hours' Sleep (us) | 1 | 1 | 1 |
| Apple Books Precious Little Sleep (au; new to global) | 1 | 1 | 1 |
| Apple Books The Sleep Lady's Good Night, Sleep Tight (us, ca) / Cribsheet (ca) / PLS (gb, ca) | 0 (no customer reviews shown) | — | 0 |
| **Total** | **301** | **301** | **234** |

Unquoted units were short generic praise ("Love it", "Helped me"), interface bugs with no situation, duplicates, or feeding/medical stories outside sleep (NICU, reflux, weight). Happy Baby: most of the 40 App Store units are short, polished 5-star texts clustered Sept–Dec 2024 (one calls the app "SleepWell Baby"); they read as solicited and were mostly not quoted. No-Cry B&N reviews date 2008–2015.

## Not reachable / not found

Smart Sleep Coach App Store (404 ×4). Taking Cara Babies: no app found (course only). Betteroo: web app, no store listing (`competitors/betteroo.md`). "Sleep Wave": the Little Ones method, collected as Little Ones. Pocket Sleep Doc: a studio.com app, no store page found. Moms on Call and Babywise (other editions), Precious Little Sleep paperback, Cribsheet paperback, No-Cry 2nd ed. and HSHHC ebook: B&N 404 by ISBN. HSHHC on Apple Books us/ca and Happy Sleeper, Sleep Lady on Apple Books gb/au: 404. Goodreads and Amazon not fetched (robots). Full detail: `reviews-not-harvested.md`.

## Restricted ids

Quoted for the record, never for ads or findings without review. Reason: unsafe sleep, mental health, or a health/crying-harms claim (README lines not to cross).

| id | source | reason |
|---|---|---|
| `sbr1-0002` | App Store ca Huckleberry | unsafe sleep (cosleeping out of desperation, felt unsafe) |
| `sbr1-0016` | App Store au Huckleberry | mental health (psychologist as next step) |
| `sbr1-0050` | App Store us Nara Baby | mental health (postpartum depression) |
| `sbr1-0066` | App Store gb Glow Baby | unsafe sleep (cosleeping / SIDS) |
| `sbr1-0088` | App Store au Little Ones | mental health (self-reported ADHD) |
| `sbr1-0124` | App Store gb Little Ones | mental health (near-breakdown, severe stress) |
| `sbr1-0141` | App Store us Little Ones | mental health (maternal bonding / distress) |
| `sbr1-0175` | Barnes & Noble The No-Cry Sleep Solution | mental health (bedtime anxiety) and bedsharing |
| `sbr1-0180` | Barnes & Noble The No-Cry Sleep Solution | mental health (maternal distress) |
| `sbr1-0183` | Barnes & Noble The No-Cry Sleep Solution | mental health (low mood) |
| `sbr1-0184` | Barnes & Noble The No-Cry Sleep Solution | mental health (mood) |
| `sbr1-0195` | Barnes & Noble The No-Cry Sleep Solution | unsafe sleep (bedsharing from exhaustion) |
| `sbr1-0214` | Barnes & Noble The No-Cry Sleep Solution | unsafe sleep (co-sleeping adopted from a book) |
| `sbr1-0217` | Barnes & Noble Twelve Hours' Sleep by Twelve Weeks Old | health claim (feeding schedules and failure to thrive) |
| `sbr1-0223` | Apple Books us The Happy Sleeper | crying-harms claim |
| `sbr1-0227` | Apple Books us Moms on Call Basic Baby Care 0-6 Months | health claim (infant weight gain) |

## Continuing

Do not overwrite any capture or corpus; new captures get new names and a new prefix (`sbr2`). Remaining permitted gaps: other B&N editions (need exact ISBNs), Google Play other countries, Apple Books audiobook pages.
