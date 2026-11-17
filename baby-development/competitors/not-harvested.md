# Competitor pages not harvested — development, 2026-10-25

Every block, refusal or unreadable page from the competitor wave. robots.txt files checked first are in `../scratchpad/mkt-dev/robots/`; the checker is `../scratchpad/mkt-dev/robots.py`. No captcha, bot wall or login was worked around.

| site / page | status | what happened | consequence |
|---|---|---|---|
| etsy.com/search?q=baby+activities+by+month+printable | 403 | DataDome bot wall ("Please enable JS and disable any ad blocker", captcha-delivery.com) | Etsy printables not inventoried; capture deleted. Needs a browser walk if wanted |
| payhip.com/b/6zgFc (0–12 m sensory play cards) and other Payhip listings (Gemma Hepburn "The Baby Development Guide" A$39.99, motor-milestones journal $7, Newborn Play Guide £5) | 403 | Cloudflare challenge ("Just a moment...") | Payhip sellers listed in `../competitors/README.md` from search snippets only, not torn down |
| happity.co.uk (Bloom Sheffield class listing with prices) | 403 | Cloudflare challenge | Bloom prices not verified |
| courses.kinedu.com/course/e-book | none (curl 000) | TLS handshake failure | Kinedu e-book not seen |
| babyacrobatics.com /start, /course, /checkout, /guide | not requested | Disallowed in robots.txt for `*` and for named AI crawlers | No order page, onboarding or quiz entry for Baby Acrobatics |
| thewonderweeks.com/getthebook | 200 after redirect | Redirects to amazon.com; Amazon is robots-restricted for this research (`not-harvested.md`) | Capture deleted; book price not recorded |
| webpromo.kinedu.com/p/assessment-landing | 200, 0 words | Next.js app, nothing in static HTML (`_raw/competitors/kinedu-2026--assessment-landing.txt`) | Needs a browser walk |
| kiaram.gumroad.com/l/newborn (0–12 m milestones & activities e-book, price €0+) | 200, 0 words of text | Product rendered by script; only JSON (name, price 0) in HTML | Not torn down; needs a browser walk if wanted |
| gumroad.com/discover?query=baby%20activities | 200, 0 words | Script-rendered; product links in HTML were off-niche (Sunday school, Notion templates, Bali travel) | Gumroad treated as low-yield for this niche |
| montessori-at-home.teachable.com | 200 | "This school is offline" | Montessori at Home ($45/$55 courses in search snippets) no longer sells |
| mumsnet.com "Ages and Stages" emails | not requested | robots.txt disallows GPTBot; Mumsnet already excluded (`not-harvested.md`) | Listed only |
| stan.store | fetched | robots.txt disallows GPTBot only; `*` and ClaudeBot allowed for product pages | Our Playfull Home captured; flagged here for consistency review |
| ClickBank | on disk | 2026-10-01 snapshot read; 1 on-niche offer (Motherhood Unleashed, gravity 0) | See `../competitors/motherhood-unleashed.md` |
