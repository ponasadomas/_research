# Reviews: not harvested or blocked — RV1, 2026-10-25

Every route attempted for `reviews.md` that returned an error or no review bodies. Inherited bans (global/): Goodreads (robots bans GPTBot) and Amazon (robots bans GPTBot and ChatGPT-User) — not requested.

| route | status | what was done |
|---|---|---|
| App Store `ovia` id570244389 — gb, au | HTTP 404 | not listed in those storefronts; us and ca captured |
| App Store `thebump` id568940747 — gb, au | HTTP 404 | us and ca captured |
| App Store Expectful id1173564771 — us, gb, ca, au | HTTP 404 all four | app not available on 2026-10-25 (search results that showed ca/au listings were stale) |
| App Store Expect id1523369578 — gb, ca, au | HTTP 200, 0 review units | us captured (3 units) |
| App Store Every Mother id1369750567 — gb, au | HTTP 200, 8 and 3 units (fewer than 10) | all read |
| Google Play `com.whattoexpect.ui` | HTTP 404 (capture deleted before refetch) | correct id `com.wte.view` captured |
| Google Play `com.ovuline.pregnancy` | HTTP 404 (capture deleted before refetch) | combined Ovia app `com.ovuline.fertility` captured instead |
| Google Play `com.expectful.meditationapp` | HTTP 404 | `_raw/reviews/googleplay-expectful.txt` |
| Google Play `fit.expect.expect` | HTTP 200, no review section on page | `_raw/reviews/googleplay-expect.txt` |
| Google Play Every Mother: `com.everymother.app`, `com.sustainablefitness.everymother`, `com.everymother.android` | HTTP 404 (probes only, not saved) | `com.everymother` HTTP 200 captured |
| B&N `/w/?ean=` for Real Food for Pregnancy (9780986295034, 9780986295041), The Fourth Trimester (9781611804331, 9781611803556), The Positive Birth Book (9781780666327), Hypnobirthing (9781785042881) | HTTP 404 | captures kept as `_raw/books/barnes-*-ean404.txt`, `-ean2-404`, `-url404`; Fourth Trimester, Positive Birth Book and Hypnobirthing then found by product URL |
| B&N Real Food for Pregnancy `/w/real-food-for-pregnancy-lily-nichols/1128083206` | HTTP 404 | no B&N reviews for this title; Apple Books audiobook used |
| Yotpo lists for B&N Birth Partner 5th, Positive Birth Book, Hypnobirthing, Fourth Trimester | HTTP 200, total 0 | empty lists only for these edition ids; not proof of no reviews elsewhere |
| Apple Books Ina May — gb, au | HTTP 404 | us and ca captured |
| Apple Books Hypnobirthing (Siobhan Miller) ebook — gb, au | HTTP 404 | us and ca captured (0 reviews); audiobook gb has 1 |
| Apple Books Expecting Better — gb, au | HTTP 404 | ca captured |
| Apple Books The Birth Partner 6th — au; What to Expect — au | HTTP 404 | other storefronts captured |
| Apple Books Mama Natural and Real Food for Pregnancy ebooks | not found in search; only audiobook pages exist | audiobook pages captured in us/ca/gb(/au) |
