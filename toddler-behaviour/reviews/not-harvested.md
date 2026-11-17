# App and book reviews — blocked, missing or not attempted (RV1, 2026-10-25)

| Source / route | Status | Decision |
|---|---|---|
| `https://apps.apple.com/robots.txt` | 200; disallows `/api/*`, `/v1/*`, `*/search?*`, `/WebObjects/*` | Only public app pages used. `_raw/reviews/apps-robots.txt` |
| App Store, 10 apps × us/gb/ca/au (40 routes) | 39 × 200; RootWise au 404 | All exposed units frozen. Potty Path (4 storefronts), RootWise (3), ParentPal (4) expose 0 reviews; POTTR, Potty Training App, LittlePath, AI Parenting Coach, Granny expose 0–3 per storefront. Manifests `_raw/reviews/appstore-collection-manifest*.json` |
| Apple continuation / RSS (`itunes.apple.com/*/rss/*`) | robots-disallowed (see `../../global/_raw/reviews/apple-robots.txt`) | Not requested. 10 units per storefront is the ceiling |
| Big Little Feelings app | no App Store or Play listing found by search; BLF FAQ says courses play in the Kajabi app | Nothing to harvest. `https://marlvel.ai/apps/big-little-feelings` (third-party app report) returned 403 via WebFetch; not retried |
| `https://play.google.com/robots.txt` | 200; disallows `/store/search`, `/store/getreviews`, `/store/xhr`, `/_` | Detail pages only. `_raw/reviews/googleplay-robots.txt` |
| Google Play Good Inside, Potty Whiz detail pages | 200, 200 | 3 bodies each frozen; "See all reviews" continuation not used |
| Google Play POTTR, Potty Path, Potty Training App, RootWise, LittlePath | no package id found (Play search disallowed; web search found none) | Not harvested; possibly iOS-only |
| `https://www.barnesandnoble.com/robots.txt` | 200; disallows `/search` | Product pages reached by `/w/?ean=` only. `_raw/books/barnes-robots.txt` |
| `https://api-cdn.yotpo.com/robots.txt` | 200; `Disallow: /` but `Allow: /v3/storefront/store/*` | Review lists via the allowed route. `_raw/books/yotpo-robots.txt` |
| B&N `/w/?ean=9780988527509` (No Bad Kids, 2014 JLML) | 404 | Edition not sold; Rodale 2024 pb + ebook used (0 reviews) |
| B&N How to Talk So Little Kids Will Listen, No Bad Kids, Potty Training in 3 Days | 200; Yotpo totals 0 for both formats | No units. Zero = current widget, not proof of no reviews elsewhere |
| ISBN probes that resolved to unrelated books or 404 | `_raw/books/barnes-collection-manifest.json` lists the used seeds; probe pages kept in `scratchpad/RV1/probe/` | Wrong ISBNs dropped before collection |
| `https://books.apple.com/robots.txt` | 200; disallows `/WebObjects/*`, `/v1/catalog/*` | Product pages only. `_raw/books/apple-books-robots.txt` |
| Apple Books `isbn` route: Good Inside 9780063159501 / 9780063159495 / 9780063159488 | 404 ×3 | Resolved on second run with 9780063159471 (us) and 9780008505554 (gb) |
| Apple Books Hands Are Not for Hitting 9781575422008, 9781631985300 | 404, 404 | No Apple Books page found |
| Apple Books gb/au for How to Talk…, No Bad Kids, Whole-Brain Child, Hunt Gather Parent; au for Good Inside | 404 (id not sold in that storefront) | Regional editions have other ids; not resolved in this pass |
| Apple Books Oh Crap gb | 200, 0 reviews shown | — |
| Goodreads, Amazon | robots ban AI crawlers (`../../global/_raw/books/goodreads-robots.txt`, `../../global/_raw/reviews-followups/amazon-robots.txt`) | Not fetched |
