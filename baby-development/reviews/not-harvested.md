# App and book reviews — not harvested or empty (RV1, 2026-10-25)

Every request below was a public, robots-permitted route (robots files saved: `_raw/reviews/apps-robots.txt`, `_raw/reviews/googleplay-robots.txt`, `_raw/books/barnes-robots.txt`, `_raw/books/yotpo-robots.txt`, `_raw/books/apple-books-robots.txt`, each with `.headers.txt`, all HTTP 200). Goodreads and Amazon were not fetched (robots ban, `../../global/sources/reviews-followups.md`). No logins, sign-ups or purchases. Manifests: `_raw/reviews/appstore-collection-manifest.json`, `_raw/books/barnes-collection-manifest.json`, `_raw/books/apple-books-manifest.json`.

## Skipped on purpose (held elsewhere)

| what | where it already is |
|---|---|
| App Store us + gb for Kinedu, BabySparks, The Wonder Weeks | `../../global/_raw/reviews/` (only ca + au collected here) |
| Google Play Kinedu, BabySparks, Pathways.org, CDC Milestone Tracker | `../../global/_raw/reviews-followups/googleplay-*.txt` |
| Apple Books us for The Montessori Baby, The Wonder Weeks, The Simplest Baby Book | `../../global/_raw/books/` (only gb/ca/au collected here) |
| Barnes & Noble The Montessori Baby, The Simplest Baby Book | `../../global/_raw/reviews-followups/barnes-*` |
| The Whole-Brain Child (Apple Books and B&N) | `../../toddler-behaviour/_raw/books/` |

## App Store — HTTP 200 but 0 visible reviews

| app (id) | storefronts with 0 |
|---|---|
| Lovevery (id1556748552) | au |
| Little Steps (id1210116232) | ca, au |
| BabyDone (id6770622579) | us, gb, ca, au (no ratings; competitors README) |
| RealPlay (id6749885609) | us, gb, ca, au (no ratings; competitors README) |

Apple shows at most 10 units per storefront; it selects them. There is no permitted continuation route (`../../global/sources/reviews-media.md`).

## Google Play

| app | result |
|---|---|
| The Wonder Weeks `org.twisevictory.apps.ex` | HTTP 200, 3 bodies (package id from a third-party listing; Play search is robots-disallowed) |
| Sprouty `happy.mom.android` | HTTP 200, 3 bodies (package id from chrome-stats / AppBrain listings) |
| Lovevery | package id not found. Lovevery's help centre says an Android app exists; guesses `com.lovevery.app`, `com.lovevery`, `com.lovevery.android`, `com.lovevery.mobile` all HTTP 404 (not saved). The blog's onelink redirect gave no store URL. |
| Bloomie, Little Steps | no Android listing found by web search (iOS only, as far as seen) |
| BabyDone, RealPlay | not searched (no App Store reviews either) |

## Barnes & Noble (product page → Yotpo list)

| title | EANs tried | page | Yotpo total |
|---|---|---|---|
| Brain Rules for Baby | 9780983263388, 9780983263395 | 200, 200 | 0, 0 |
| Your Baby's First Year (AAP, 6th and 5th ed.) | 9780593983874, 9780593158289 | 200, 200 | 0, 0 |
| The Montessori Toddler | 9781523506897, 9781523507900 | 200, 200 | 0, 0 |
| Baby Play (Gymboree) | 9780865734340, 9780760758984 | **404, 404** | — |
| How to Raise an Amazing Child the Montessori Way | 9781465462305 (US), 9780241286265 (UK) | 200, **404** | 0 |
| The Wonder Weeks (6th ed.) | 9781682684276, 9781682684283 | 200, 200 | 1 (one shared review on both formats) |
| What to Expect the First Year (3rd ed.) | 9780761181507, 9780761183174 | 200, 200 | 0, 0 |

B&N's Yotpo lists are short for every title tried here and in toddler-behaviour; older B&N reviews do not appear on these lists. Empty means empty on this route, not that nobody reviewed the book.

## Apple Books

| title | result |
|---|---|
| Brain Rules for Baby (id861741153) | us 200 (2 reviews), gb 200 (0 written, 2 ratings), ca 200 (0 written, 5 ratings), au **404** |
| The Montessori Toddler (id6443053599) | us 200 (0 written, 14 ratings), ca 200 (0), gb **404**, au **404** |
| What to Expect the First Year (id6443120813) | us 200 (1), ca 200 (0 written), gb **404**, au **404** |
| The Montessori Baby (id6443052178) | ca 200 (1), gb **404**, au **404** |
| The Wonder Weeks (id1451744965) | gb 200 (0 written), ca 200 (0 written), au **404** |
| The Simplest Baby Book (id1597514453) | gb, ca, au all **404** |
| Your Baby's First Year (AAP) | isbn9780593983874, isbn9780593158289 → us **404**; ebook ISBN not found |
| Baby Play (Gymboree) | isbn9780865734340 → us **404** (print-only, 2001) |
| How to Raise an Amazing Child the Montessori Way | isbn9781465462305, isbn9780241286265 → us **404**; ebook ISBN not found |

gb/au 404s mean those storefronts sell another edition under a different id; the ids were not chased.
