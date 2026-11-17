# App and book reviews — blocked, missing or not attempted (RV1, 2026-10-25)

| Source / route | Status | Decision |
|---|---|---|
| `https://apps.apple.com/robots.txt` | 200; disallows API/RSS/search routes | Only public app pages used. `_raw/reviews/apps-robots.txt` |
| App Store, 9 listings (34 routes) | 32 × 200; Sleepio UK id1538191784 ca 404, au 404 | All exposed units frozen. Sleepio 3.0 ca/au and Blissful (4 storefronts) expose 0 reviews. Manifest `_raw/reviews/appstore-collection-manifest.json` |
| Sleepio 3.0 id6698893964 gb | 404 (probe) | Not sold in gb; gb covered by the UK/NHS listing id1538191784 |
| Sleepio older ids 910208298 (us, gb) | 404, 404 (probe) | Retired listing |
| SleepioRx id6742593878 | us 200, gb 404 (probe) | Prescription-only build; not harvested |
| Expectful (pregnancy/postpartum meditation and sleep; id1173564771 from expectful.com) | 404 (us) | Listing gone; Play package com.expectful.meditationapp also 404 |
| Positive Pregnancy with AJ id349477846 | 200 (probe) | Pregnancy relaxation/hypnosis, not built for sleep; not harvested |
| Other postpartum/pregnancy sleep apps | none found by web search (App Store search is robots-disallowed) | Peanut's Oura sleep feature and a studio.com coach app have no App Store review pages |
| Apple continuation / RSS | robots-disallowed | Not requested; 10 units per storefront is the ceiling |
| `https://play.google.com/robots.txt` | 200; disallows `/store/search`, `/store/getreviews`, `/_` | Detail pages only. `_raw/reviews/googleplay-robots.txt` |
| Google Play Calm, Headspace, BetterSleep, Slumber, Rise, Stellar Sleep | 200 × 6 | 3 bodies each frozen |
| Google Play Sleepio, Blissful, Slumber guesses (fm.slumber.sleep, fm.slumber.app, com.slumber.app), Sleepio guesses (com.bighealth.*), Stellar guesses (com.stellarsleep*), Rise guesses (com.risescience.*) | 404 (probe) | Correct Slumber, Rise and Stellar packages found on the developers' sites / analytics page; Sleepio and Blissful not found |
| `https://www.barnesandnoble.com/robots.txt` | 200; disallows `/search` | Product pages by `/w/?ean=` only. `_raw/books/barnes-robots.txt` |
| `https://api-cdn.yotpo.com/robots.txt` | 200; `Allow: /v3/storefront/store/*` | Review lists via the allowed route. `_raw/books/yotpo-robots.txt` |
| B&N Hello Sleep (hc 9781250828408, pb 9781250347428), The Sleep Solution 9780399583612, The Fourth Trimester 9781611804003, Sleep Deprived No More 9780738215044 | 200; Yotpo totals 0 | No units |
| B&N The Sleep Solution hc 9780399583605 | 404 (probe) | pb used |
| B&N 9781611803488, 9781611804713 (wrong Fourth Trimester guesses) | 200, unrelated books (probe) | Dropped; 9781611804003 used |
| B&N The First Forty Days 9781617691836 | 200 (probe only) | Not collected: `global/` holds its list |
| `https://books.apple.com/robots.txt` | 200; disallows `/WebObjects/*`, `/v1/catalog/*` | Product pages only. `_raw/books/apple-books-robots.txt` |
| Apple Books print ISBNs (Hello Sleep, Sleep Solution, First Forty Days hc) | 404 (probe) | Ebook ISBNs resolved: 9781250828415, 9780399583629, 9781613129418 |
| Apple Books gb/au: Say Good Night to Insomnia, The Sleep Solution, Sleep Deprived No More | 404 | Other regional ids; not resolved |
| Apple Books Hello Sleep (4 storefronts), Sleep Deprived No More, Fourth Trimester gb/ca/au | 200, 0 written reviews shown | — |
| Goodreads, Amazon | robots ban (see `../../global/_raw/books/goodreads-robots.txt`) | Not fetched |

Probe requests were not saved to `_raw/`; only the collectors' captures are there.
