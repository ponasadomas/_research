# Sales letters — historical swipe file for the development niche (Wayback Machine)

Started 2026-11-03. Owner's ask: find at least ten long-form sales letters that were sold to this audience in the past (mothers of 0–24-month babies: development, play, milestones, "what to do with your baby"), plus adjacent early-learning offers ("teach your baby to read" style, labelled *adjacent*), so we have headlines, benefits, mechanisms, proof and offer structures others have used. English only unless the owner says otherwise.

**What counts as a long-form sales letter:** one page, a headline, body of ≥1,200 words, a price or buy call-to-action, usually a guarantee. App-store pages, SaaS landing pages, blog posts and catalogue pages are *captured, not letters* and go in a separate list.

## Layout

- `_tools/wayback.py` — the only permitted way to touch web.archive.org (4 s between requests, backoff on 429). `cdx` lists captures, `fetch` saves a raw `id_` capture as text with a header.
- `_raw/sales-letters/<slug>--<timestamp>.txt` — raw captures, header lines SOURCE / WAYBACK / TIMESTAMP / HTTP / WORDS, then the page text. Never edited.
- `sales-letters/candidates-*.tsv` — discovery output (Phase 1).
- `sales-letters/<slug>.md` — one note per letter (Phase 3): product, seller, years seen, price seen, headline(s) verbatim, subheads, bullets/benefits, mechanism, proof, guarantee, objections handled, each verbatim line a substring of a raw file; every headline/benefit tagged `usable` / `adjacent` / `outside-lines` against the owner brief §8 (no diagnosis, no "behind", no earlier-milestone promise, no outcome claims, no day counts).
- `sales-letters/index.md` — the swipe bank across letters (Phase 4).
- `sales-letters/logs/` — Codex briefs and run logs.
- `sources/sales-letters.md` — ledger: every capture tried, status, words, kept or not.

## Rules

Raw first; quote only from a saved raw file. Counts are counts of captures, not sales. A page being archived proves it existed, not that it sold. Record prices and claims as what the page said on that date.
