# Book and app reviews — brief for every niche (2026-10-25)

Read first: `templates/00 - Deep Research Playbook.md` (sections 2, 5 rules of access, 7 Books), the niche's `README.md`, `sources/source-map.md` ("Adjacent books", "Apps"), and how `global/` did this: `mamivio.com/research/global/sources/reviews-media.md`, `reviews-followups.md`, `reviews-media-not-harvested.md`, `global/_tools/collect_app_reviews.py` and `brief-reviews-media.md`.

## Access (unchanged from global/)
- Apple App Store public app pages `https://apps.apple.com/<cc>/app/<slug>/id<id>?see-all=reviews` expose 10 reviews per storefront; use storefronts **us, gb, ca, au**. No RSS or API routes (robots-disallowed).
- Google Play public detail pages expose about 3 reviews; robots restrict continuation endpoints.
- Barnes & Noble public edition review lists; Apple Books public pages. **Goodreads and Amazon are robots-banned: do not fetch.**
- Save every page untouched under `<niche>/_raw/reviews/` or `<niche>/_raw/books/` before quoting; log every block with HTTP status in `<niche>/sources/reviews-not-harvested.md`.
- **Do not re-harvest** what global/ already holds (Huckleberry, Napper, Kinedu, BabySparks, Wonder Weeks, Solid Starts, BLW Meals, Pump Log, Baby Daybook in us+gb; the 13 Apple Books titles in `global/_raw/books/`). For those, add only the ca and au storefronts.

## Read and quote
Every review unit saved is read in full. Quote into your own new voice file `<niche>/voice/reviews-<reader>.jsonl` with the niche schema (`source`: "App Store <cc> <app>" / "Google Play <app>" / "Barnes & Noble <title>"; `source_class`: `app_review` or `book_review`; `speaker`: `reviewer`; `raw_file` the saved text file; verbatim, trims only with ` […] `). Pull what the 1–3★ reviews say the product missed, what 4–5★ praise, paywall and price complaints, cancellation, "generic" vs "personal", and anything about their own situation. Research principle: Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.

## Ledger and checks
Write `<niche>/sources/reviews.md` with a ledger table (source · units saved · read · quotes) and what was not reachable. Run `python3 -I <niche>/_tools/verify_quotes.py <niche>/voice/reviews-<reader>.jsonl` to 0 failed. No purchases, no sign-ups. Reply with only: units read per source, quotes written, verify line, blocks, and the five things the reviews add that Reddit did not.
