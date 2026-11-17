# Competitor teardowns — brief for every niche (2026-10-25)

First read: `templates/00 - Deep Research Playbook.md` (sections 2, 5 "rules of access", 7), the niche's `README.md`, `product/product-brief.md` and `sources/source-map.md` (its "Competitors to tear down" list). Format reference: `mamivio.com/research/global/competitors/README.md` and `global/competitors/taking-cara-babies.md`. The owner's Ad Library sweep with active-ad counts: `mamivio.com/research/main/ads-running/spend-footprint-by-subniche-2026-10-25.md` (read it: the sellers with active ads matter most).

## Goal

Every serious offer in this niche, not the top five: each competitor on the source-map list, plus every further one you find by searching as the buyer would (e.g. "4 month sleep regression course", "potty training program", "baby activities by month pdf", "hypnobirthing course online"), on Etsy, Gumroad, Stan Store, SamCart, Kajabi and Teachable storefronts, ClickBank (`~/GitHub/tools/scrapers/clickbank-marketplace-scraper/snapshots/`, latest file), and names that turn up along the way. Sellers that `global/competitors/` already tore down: link that note and only add what changed or what this niche needs; do not duplicate.

## Per competitor

1. Check robots.txt first; respect AI-crawler bans; no captcha or bot-wall workarounds. Log every block with HTTP status in `sources/competitors-not-harvested.md`.
2. Save each page untouched before quoting: `python3 -I <niche>/_tools/fetch_page.py <slug>[--page] <url> --dir competitors` (sales page, pricing, FAQ, quiz entry, order page, guarantee terms, about page). One slug per seller.
3. Write `<niche>/competitors/<slug>.md`: title, captured date, URLs and raw files; **buyer/trigger · mechanism (≤8 words) · promise · proof · price (exact, with currency and anchor) · format · personalization (what is asked, what changes) · guarantee · angles and hooks · objections answered**; then 3–10 verbatim lines as `> ` blockquotes (only verbatim text may be a blockquote); then a separate, labelled "Comparison with Mamivio — interpretation"; then "Gaps".
4. Quiz funnels and JavaScript apps you cannot read with fetch_page (e.g. quiz.betteroo.ai): save what loads, mark the note "needs a browser walk", and list them in your reply. The orchestrator walks them in Chrome with the owner watching.

## Index and checks

Write or extend `<niche>/competitors/README.md`: a table of every note (seller, category, price observed, personalization mechanism, active Meta ads from the sweep if known) and a list of offers found but not torn down, with why. Run `python3 -I <niche>/_tools/verify_competitors.py` until **0 failed**. No purchases, no sign-ups with personal data, no contacting sellers.

Reply with only: notes written, pages saved, verify line, offers needing a browser walk, blocked sites, and the five most important things a copywriter should know about this niche's market. Never paste page text back.
