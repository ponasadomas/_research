# Competitor pages not harvested — sleep-baby

2026-10-25. Every block or failure from the competitor wave, with HTTP status and what was used instead. No captcha, bot-wall or login workaround was attempted.

| site / URL | status | why / what was used instead |
|---|---|---|
| justchillbabysleep.co.uk (all pages, robots.txt) | 403 | bot wall. Used the owner's Ad Library capture (copied to `_raw/competitors/just-chill--meta-ads-2026-10-25.txt`) and a Wayback capture of /our-courses/ dated 2024-06-15. Two further Wayback URLs returned 429 (rate limit). Needs a browser walk. |
| thehappysleepcompany.com (site, robots.txt) | 403 | bot wall. Used Wayback home capture 2025-08-19 + ad copy. Needs a browser walk. |
| www.sleepnanny.co.uk | 403 | used site.melaniehastings.sleepnanny.co.uk (200) instead |
| trybetteroo.com, betteroo-sleep.com | 000 | no response (ad display URLs); betteroo.ai and quiz domains used |
| quiz.betteroo.ai, quiz.betteroo.co | 200, JS shell | quiz is a JavaScript app; static JS bundles saved and their strings extracted. Prices behind paywall API not called. Needs a browser walk. |
| goodinside.com/purchase/checkout/?id=baby-sleep-bundle-20260827 | 200, JS shell (15 words) | price not observed. Needs a browser walk. |
| tally.so/r/680M8P (Calmer Nights questionnaire) | 200, page 1 of 13 only | JS form. Needs a browser walk (no personal data). |
| jessiemartin.teachable.com/courses/1944467 | 200, 38 words | JS shell; not torn down |
| davisjohnson7.gumroad.com/l/custom-sleep-plan | 200, 0 visible words | JS; embedded strings saved (`gumroad-custom-plan-ot--embedded.txt`); listed, not torn down |
| Amazon (Smart Starts book, Precious Little Sleep book) | not fetched | robots bans GPTBot / ChatGPT-User (inherited rule) |
| stan.store | not fetched | robots.txt `User-Agent: GPTBot` `Disallow: /` — AI-crawler ban respected |
| Etsy search (baby sleep schedule) | 403 | bot wall; Etsy listings not harvested |
| littleslumberstars.thinkific.com/robots.txt | 403 | robots file itself 403; course page returned 200 and was saved (4xx robots read as no restriction) |
| letssleep.com.au /shop, /faq | 404 | pages do not exist; captures deleted |
| huckleberrycare.com/sweetspot | 404 | deleted; pricing page used |
| goodinside.com/baby/sleep/ | 404 | deleted |
| norababysleep.gumroad.com/l/BabySleepTrainingPack | 404 | deleted |
| Instagram (dgsleepconsulting, thesnoozenurse), Facebook (susiemenkessleep) | not fetched | no permitted public route |
