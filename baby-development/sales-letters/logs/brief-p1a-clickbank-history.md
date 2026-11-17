# Phase 1A — discover historical baby-development info products via ClickBank marketplace history

You are a research agent working in `/home/thinkpad/GitHub/ads/mamivio.com/research/development/`. Read `sales-letters/README.md` first.

## Goal
Produce a candidate list of info products (ebooks, courses, DVDs, memberships) that were sold to mothers of babies 0–24 months on the topics: baby development, milestones, play/activities, "what to do with your baby", tummy time, early stimulation, baby brain development, and the adjacent early-learning offers (teach your baby to read / math / signs / music). Years of interest: roughly 2005–2022. English-language offers only.

## Route
ClickBank's marketplace and the aggregator sites that mirrored it listed these products with their sales-page links. Use the Wayback Machine through the helper only:
- `python3 -I _tools/wayback.py cdx '<url>' --from 2008 --to 2020 --limit 40` (add `--match prefix` with a trailing slash to list a site's pages)
- `python3 -I _tools/wayback.py fetch <timestamp> '<url>' --out _raw/sales-letters/_discovery/<name>.txt`
Targets to try (check CDX first; pick 2–4 captures per target spread across years): `clickbank.com/marketplace` category pages for "Parenting & Families" (sub-categories like Pregnancy & Childbirth, Parenting, Special Needs, Education); `cbengine.com` and `cbtrends.com` category/product pages; `cb-analytics.com`; `clickbank-marketplace` style lists; `jvzoo.com` marketplace captures; also `warriorforum.com` and `affiliate` directories if CDX shows category pages. If a captured page is a JS app with no product names, note it and move on. Follow hop links to the product's own domain and record the domain; do not fetch the sales pages themselves (Phase 2 does that).

## Hard limits
- Never call web.archive.org except through `_tools/wayback.py`. It throttles to one request per 4 s; do not run it in parallel with itself.
- At most 120 Wayback requests in this run. Prefer CDX listings over fetches. Stop and write output when you reach the cap.
- No live site visits; everything comes from Wayback captures saved under `_raw/sales-letters/_discovery/`.

## Output
1. `sales-letters/candidates-A.tsv` with columns: `domain`, `product_name`, `topic` (development|play|milestones|early-learning|sleep-adjacent|other), `years_seen`, `lead_source` (the discovery capture file), `hop_or_sales_url`, `price_if_shown`, `note`. Aim for 25+ rows; mark duplicates of domains you already listed.
2. `sales-letters/logs/p1a-report.md`: what you fetched (with capture file names), what worked, what was empty, the request count used, and the ten candidates you think are most likely to have a long-form sales letter.
Append one row per fetch to `sources/sales-letters.md` (slug `_discovery/<name>`, letter? = no).
