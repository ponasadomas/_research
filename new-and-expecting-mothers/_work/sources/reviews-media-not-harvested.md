# Review and media access limits — 2026-10-24

| Source / exact route | HTTP/access observation | Decision and raw evidence |
|---|---|---|
| `https://itunes.apple.com/robots.txt` | HTTP 200; `User-agent: *`, `Disallow: /*/rss/*` | Apple customer-review RSS was not requested. `_raw/reviews/apple-robots.txt` and headers |
| `https://apps.apple.com/robots.txt` | HTTP 200; APIs restricted, public app paths permitted | Used only public app pages. `_raw/reviews/apps-robots.txt` |
| `https://apps.apple.com/us/app/huckleberry-baby-tracker/id1169136078?see-all=reviews` and corresponding 17 app/storefront routes | HTTP 200; 10 user reviews each; shelf continuation fields null | Captured every exposed review unit; no whole-history claim. Exact per-page fields in `_raw/reviews/public-route-audit.json` |
| `https://www.goodreads.com/robots.txt` | HTTP 200; `User-agent: GPTBot`, `Disallow: /` | No original book/review pages harvested. `_raw/books/goodreads-robots.txt`. Discovery search results were not quoted or treated as original review reads |
| `https://www.trustpilot.com/review/solidstarts.com` | HTTP 403; response says request identified as a bot against terms | No further direct harvesting. `_raw/reviews/solidstarts-trustpilot-page1.html`. Policy saved in `_raw/reviews/trustpilot-robots.txt` |
| YouTube `ytsearch5:tummy time baby hates tummy time` | yt-dlp initial probe exited 0 and returned five metadata rows; no per-request HTTP status captured | Probe preceded policy inspection. Raw `_raw/youtube/probe-search.tsv` and stderr. Further search stopped after reading robots |
| `https://www.youtube.com/robots.txt` | HTTP 200; generic crawler group disallows `/results`, `/youtubei/`, `/comment` and multiple API/continuation paths | Bulk search/comment pipeline not run. `_raw/youtube/robots.txt`. No captcha, cookies or alternative-host workaround |
| Amazon customer review archives | Not requested | Still uncollected; no claim that Amazon is blocked or empty |
| Google Play, Kobo and other retailer review archives | Not probed in this branch | Explicit continuation gap; public Apple originals supplied this batch, but five review source classes were not achieved here |

Search-index snippets are useful discovery pointers. They are not substitutes for original review lists and are not mixed into this branch's original-review quote counts.
