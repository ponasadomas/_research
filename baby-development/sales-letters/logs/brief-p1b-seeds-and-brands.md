# Phase 1B — discover candidates from known sellers, brand names and web search

You are a research agent working in `/home/thinkpad/GitHub/ads/mamivio.com/research/development/`. Read `sales-letters/README.md` first.

## Goal
A candidate list of info products sold to mothers of babies 0–24 months (development, milestones, play, "what to do with your baby", tummy time, early stimulation, brain development) and adjacent early-learning offers (teach your baby to read / math / sign / music), 2005–2022, English, that are likely to have had a long-form sales letter (one page, headline, ≥1,200 words, price, guarantee).

## Routes (in this order)
1. **Seeds already in this research.** Read `competitors/README.md` and the notes it lists, `../sleep-baby/competitors/README.md`, `../global/competitors/README.md`, and `../main/synthesis/sub-niche-map.md` §0 (ClickBank notes). Every document-shaped or course seller there is a candidate; record its domain. For each, run one CDX query (`python3 -I _tools/wayback.py cdx '<domain>' --from 2008 --to 2024 --limit 30`) and note the first and last capture years.
2. **Brand recall.** Known historical names in this space and the names you can recall of products sold on ClickBank, infomercials, JVZoo, Amazon-adjacent sites: e.g. Your Baby Can Read, BrillKids Little Reader, Baby Genius / Genius Babies, Doman-style "teach your baby math", Baby Signs / Baby Signing Time, Active Babies Smart Kids, Brainy Baby, Baby Einstein (product, not letter), Monti Kids, Lovevery launch pages, BabySparks and Kinedu early landing pages (landing pages, not letters: list them as "captured, not letter" candidates), tummy-time and baby-massage courses, "baby milestones" ebooks, "smart baby" / "bright baby" programmes, baby sleep ClickBank offers (Baby Sleep Miracle etc., sleep-adjacent). Verify each name exists via one CDX query; do not list names you cannot find a capture for.
3. **Web search** (you have network): queries like `"baby development" ebook clickbank`, `"teach your baby" sales page`, `"tummy time" course`, `"baby milestones" ebook`, `"your baby can" program`, `jvzoo baby`, `warriorforum baby niche product`, `"baby brain development" program download`. Record domains, then verify with one CDX query each.

## Hard limits
- Never call web.archive.org except through `_tools/wayback.py` (one request per 4 s; never in parallel with itself). At most 100 Wayback requests in this run; CDX queries only, no page fetches (Phase 2 fetches).
- Live web search is fine; do not scrape live sales pages.

## Output
1. `sales-letters/candidates-B.tsv` with columns: `domain`, `product_name`, `topic` (development|play|milestones|early-learning|sleep-adjacent|landing-page-only|other), `first_capture`, `last_capture`, `lead_source`, `likely_sales_url`, `price_if_known`, `note`. Aim for 30+ verified rows.
2. `sales-letters/logs/p1b-report.md`: method, request count, dead ends, and the ten candidates most likely to be long-form letters, with the exact Wayback timestamp you'd fetch first for each.
