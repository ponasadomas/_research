# App and book reviews — blocks, 404s and exclusions (RV1, 2026-10-25)

Companion to `reviews.md`. Policies saved untouched in `_raw/reviews/robots-*.txt` (+ `.headers.txt`), all HTTP 200: apps.apple.com, books.apple.com, play.google.com, www.barnesandnoble.com, api-cdn.yotpo.com. No AI-crawler ban in any of them; only their disallowed paths were avoided. No captcha, login, cookie or alternate-host workaround.

| Source / route | HTTP / observation | Decision, raw evidence |
|---|---|---|
| `https://apps.apple.com/{us,gb,ca,au}/app/id1616824897?see-all=reviews` (Smart Sleep Coach by Pampers) | 404 in all four storefronts | Delisted from the App Store (seller closing 2026-11-30, see `competitors/smart-sleep-coach.md`). `_raw/reviews/smartsleepcoach-<cc>-reviews.html` + headers; 0 units |
| Apple App Store RSS / `/api/*` / `*/search?*` | Disallowed by saved robots | Not requested. App ids found by web search instead |
| App Store review shelf beyond 10 units | No continuation URL in `serialized-server-data` (same as `global/`) | 10 Apple-selected units per storefront; not a full archive |
| Google Play `/store/getreviews`, `/store/xhr`, `/_/` | Disallowed (see `global/_raw/reviews-followups/googleplay-robots.txt`) | Not requested; 3 bodies per detail page only. Play developer page `/store/apps/developer?id=Aumio` (allowed) used once to find `com.aumio.baby` |
| Google Play Huckleberry, Napper | Already captured in `global/` (2026-10-24) | Not re-harvested per brief |
| Taking Cara Babies app | No App Store or Play listing found by web search | Course/web only |
| Betteroo | Web app (quiz.betteroo.ai), no store listing | `competitors/betteroo.md` |
| "Sleep Wave" | Is the Little Ones method | Collected as Little Ones (id1382444112, `nz.co.littleones.prod`) |
| Pocket Sleep Doc | studio.com app; no App Store page found | Not collected |
| `https://www.barnesandnoble.com/w/?ean=9781260460582` (No-Cry 2nd ed.) | 404 | `_raw/books/barnes-nocry2.txt` |
| `…?ean=9781932740139`, `9781932740226`, `9781932740127` (Babywise editions) | 404 | `barnes-babywise*.txt`; the 2019 edition `9781932740509` loaded (200) with 0 reviews |
| `…?ean=9780985411428` (Moms on Call 0-6) | 404 | `barnes-momsoncall.txt`; no other ISBN found |
| `…?ean=9780525559283` (Cribsheet pb), `9781732930503` (PLS pb) | 404 | Only new storefronts were sought for these two |
| `…?ean=9781101965597` (HSHHC ebook), `9780525634706` (Happy Sleeper audio) | 404 | ISBN guesses from publisher listings |
| B&N Yotpo lists with total 0 | HSHHC 4th ed., Sleep Lady pb + ebook, Babywise 2019 | `barnes-<slug>-yotpo-reviews.json`; 0 is the current widget total for that edition id only |
| `https://books.apple.com/us/book/isbn<ISBN>` probes | 404 for HSHHC 9780553394801 / 9781101965597, Twelve Hours hardcover, Babywise 2019, Sleep Lady pb | Probe HTML in `_raw/books/_probes/ab-*.html`; editions found via ebook ISBNs instead |
| `books.apple.com/{gb,au}` Happy Sleeper; `{gb,au}` Sleep Lady; `{us,ca}` HSHHC (id437844439); `{gb,au}` Cribsheet | 404 (not sold in that storefront) | `_raw/books/apple-<book>-<cc>.txt` |
| Apple Books pages with no Customer Reviews block | Sleep Lady us/ca, Twelve Hours gb/ca/au, Moms on Call gb/ca/au, No-Cry au, HSHHC au, PLS gb/ca, Cribsheet ca | Saved, 0 units |
| Goodreads, Amazon | Robots ban (recorded in `global/`) | Not fetched |
