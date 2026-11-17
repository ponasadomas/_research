# App and book reviews — RV1 ledger (2026-10-25)

Reader RV1, brief `../_shared/_tools/brief-books-apps.md`. Voice file `voice/reviews-rv1.jsonl` (ids `smr1-0001`–`smr1-0044`): **44 verbatim quotes from 26 review units; all 279 saved units read in full**. `python3 -I _tools/verify_quotes.py voice/reviews-rv1.jsonl` → `44 quotes, 0 failed`. Unit-by-unit status, quote ids and the reason for every unquoted unit: `_raw/reviews/reading-ledger-rv1.tsv`. Quote builder: `scratchpad/RV1/build_quotes.py`. Quotes are selected reviewers, not a sample of buyers; which reviews show is Apple's, Google's and Yotpo's choice. No purchases, sign-ups or logins.

**App filter (from the brief for this niche):** app reviews were quoted only when they mention pregnancy, a baby, a newborn, night feeds, postpartum, being a parent, or a partner. Every app review was read; the rest are counted below and marked "no pregnancy/baby/parent/partner mention" in the ledger. Reviews by children or teens (several on Calm, Slumber, Rise) were read and not quoted (README: never quote minors). Books were quoted on merit.

## Method

- **App Store:** public pages `https://apps.apple.com/<cc>/app/<slug>/id<id>?see-all=reviews`, us/gb/ca/au; bodies from the page's `serialized-server-data` via `_tools/collect_app_reviews.py` (copied from `toddler-behaviour/_tools/`; apps and per-app storefronts adapted; refuses to overwrite). Sleepio has two listings: Sleepio 3.0 (id6698893964; us/ca/au, gb 404) and the UK/NHS listing (id1538191784; gb only, ca/au 404). Raw HTML, headers, `*-reviews.units.json`, frozen `*-corpus.txt` and `appstore-collection-manifest.json` in `_raw/reviews/`. Apple caps each storefront at 10 units.
- **Google Play:** detail page `https://play.google.com/store/apps/details?id=<pkg>&hl=en_US&gl=US` once per app (robots disallows `/store/getreviews`, `/store/search`, `/_`; none requested). HTML in `_raw/reviews/_html/`; `_tools/extract_play_reviews.py` froze the 3 exposed bodies into `_raw/reviews/googleplay-<app>.txt` (names dropped, developer replies marked). Packages: com.calm.android, com.getsomeheadspace.android, ipnossoft.rma.free, fm.slumber.sleep.meditation.stories, com.risesci.nyx, one.slumber.client (Stellar Sleep).
- **Barnes & Noble:** `https://www.barnesandnoble.com/w/?ean=<ISBN>` → page's Yotpo product ids → public `https://api-cdn.yotpo.com/v3/storefront/store/<appKey>/product/<id>/reviews` (allowed by api-cdn robots `/v3/storefront/store/*`). `_tools/collect_barnes_reviews.py`. The First Forty Days left out: `global/` already holds its B&N list (`barnes-first40`).
- **Apple Books:** `https://books.apple.com/us/book/isbn<ebook ISBN>` → book id → same id in gb/ca/au. `_tools/collect_apple_books.py`. The Fourth Trimester us page is already in `global/_raw/books/fourth-trimester.txt`, so only gb/ca/au were fetched (id1244462612, `KNOWN` override). The First Forty Days had no Apple Books capture in `global/` (it used the Abrams page), so all four storefronts were fetched.
- Robots saved with headers: `_raw/reviews/apps-robots.txt`, `_raw/reviews/googleplay-robots.txt`, `_raw/books/barnes-robots.txt`, `_raw/books/yotpo-robots.txt`, `_raw/books/apple-books-robots.txt`.

## Ledger

Units saved = complete review units exposed and frozen; all were read in full. Quotes = quotes written (several per unit allowed).

| Source | Units saved | Read | Units quoted | Quotes |
|---|---:|---:|---:|---:|
| App Store Sleepio 3.0 (id6698893964), us 10, ca 0, au 0 | 10 | 10 | 0 | 0 |
| App Store Sleepio UK/NHS (id1538191784), gb 10 | 10 | 10 | 0 | 0 |
| App Store Stellar Sleep (id1602312365), us 10, gb 10, ca 6, au 7 | 33 | 33 | 2 | 3 |
| App Store BetterSleep (id314498713), 10 × 4 | 40 | 40 | 4 | 7 |
| App Store Calm (id571800810), 10 × 4 | 40 | 40 | 4 | 8 |
| App Store Headspace (id493145008), 10 × 4 | 40 | 40 | 4 | 6 |
| App Store Slumber (id1109543953), 10 × 4 | 40 | 40 | 4 | 7 |
| App Store Rise (id1453884781), 10 × 4 | 40 | 40 | 2 | 5 |
| App Store Blissful: Self Care for Moms (id6739263953), all four storefronts | 0 | 0 | 0 | 0 |
| Google Play Calm, Headspace, BetterSleep, Slumber, Rise, Stellar Sleep (3 each) | 18 | 18 | 0 | 0 |
| Apple Books Say Good Night to Insomnia (id450549995), us 0, ca 1, gb/au 404 | 1 | 1 | 1 | 2 |
| Apple Books The Sleep Solution (id1144323075), us 1, ca 0, gb/au 404 | 1 | 1 | 1 | 1 |
| Apple Books The First Forty Days (id6443286931), us 1, gb/ca/au 0 | 1 | 1 | 1 | 2 |
| Apple Books Hello Sleep (id1624502387), Sleep Deprived No More (id1210030219), The Fourth Trimester gb/ca/au | 0 | 0 | 0 | 0 |
| Barnes & Noble Say Good Night to Insomnia (pb + ebook, one list) | 5 | 5 | 3 | 3 |
| Barnes & Noble Hello Sleep, The Sleep Solution, The Fourth Trimester, Sleep Deprived No More | 0 | 0 | 0 | 0 |
| **Total** | **279** | **279** | **26** | **44** |

By class: App Store 253 units / 36 quotes; Google Play 18 / 0; Apple Books 3 / 5; Barnes & Noble 5 / 3. Of the 271 app units, 20 passed the parent/partner filter and were quoted; 13 more mention a family member but come from a minor, a professional caregiver, a grandparent or an adult child (read, not quoted, reason in the ledger); 238 had no such mention. All 18 Google Play bodies are price, bug or paywall complaints with no parent mention. Two book units (B&N generic praise, a one-line complaint) were read and not quoted.

## Not reachable or not existing

Full log with HTTP statuses: `reviews-not-harvested.md`. In short: no App Store listing of a postpartum- or pregnancy-sleep app with public reviews was found (Expectful id1173564771 returns 404; Blissful shows 0 reviews; Positive Pregnancy with AJ is a pregnancy relaxation app, not built for sleep, and was not harvested); no Google Play package found for Sleepio, Expectful or Blissful; Apple Books gb/au 404 for Say Good Night to Insomnia, The Sleep Solution and Sleep Deprived No More (other regional ids, not resolved); Hello Sleep and Sleep Deprived No More show star ratings but no written reviews on Apple Books; B&N Yotpo lists are empty for every title except Say Good Night to Insomnia. Goodreads and Amazon were not fetched (robots ban). No route exposes the full review history.

## Quote notes

- Speaker is `reviewer` throughout; no names. Stage is `unknown` unless the review gives it (Slumber newborn story `looking_back`/`toddler`; BetterSleep toddler bedtime `toddler`).
- Every quote carries an extra `review_unit` field (the ledger key).
- After the builder ran, `context` fields were edited in `voice/reviews-rv1.jsonl` to drop gender the reviewer did not state (README: no inference of gender); `voice/` is the source of truth, not `scratchpad/RV1/build_quotes.py`. Only calm-au-10527608469 says "I'm a single mother".
- Partner mentions are mostly snoring (BetterSleep, Slumber) or sharing the habit (Headspace, Slumber, Stellar). No app review mentioned night feeds, pumping or postpartum by name; the closest are Calm gb ("going back to sleep after my baby has woken me up") and Slumber us (newborn in the room).
- Headspace gb lists "pregnancy" only as a topic in the library; it is not a pregnant reviewer.

## Restricted ids

Research only, never in ads (README: no insomnia, anxiety or depression treatment claims; no medication or supplement advice):

| id | why |
|---|---|
| smr1-0001 | success outcome of an insomnia (CBT-I) program |
| smr1-0003 | diagnosis, anxiety and sleep medication |
| smr1-0011 | same review names an anxiety diagnosis, anti-anxiety supplements and a recovery outcome |
| smr1-0019 | same paragraph continues into CBT and burnout treatment |
| smr1-0039 | same review describes recovery from medical procedures and a treatment outcome |
| smr1-0040 | reassurance framed as a health claim; the review describes recovery from medical procedures |
| smr1-0042 | medication outcome ("get off sleeping pills") |
| smr1-0043 | mental-health and medication frame |

## How to continue

Do not re-run the collectors on existing keys (they refuse). New apps or titles: add keys and pass them as arguments, then use a new reader prefix. Worth trying: UK editions of The Sleep Solution (Scribe 9781911344315) and Say Good Night to Insomnia on Apple Books gb/au; audiobook pages for Hello Sleep; Sleepio's Play listing if a package id turns up; Peanut and Expectful successors if a postpartum sleep feature gets its own listing.
