# Phase 3 — extract one note per sales letter

You are a research agent working in `/home/thinkpad/GitHub/ads/mamivio.com/research/development/`. Read `sales-letters/README.md` and `sales-letters/logs/p2-report.md`. You will be given a list of slugs (below, under ASSIGNED). For each slug read every `_raw/sales-letters/<slug>--*.txt` in full. No network is needed or allowed.

## Write `sales-letters/<slug>.md` with these sections
1. **Header line:** product, seller/vendor, format (ebook/course/DVD/membership), years of captures, price(s) seen with the capture year, guarantee, raw files read.
2. **Who it speaks to** (2–4 lines, your words): the mother, the baby's age, the moment.
3. **Headline(s)** — every main headline and pre-headline across the captures, verbatim, one per `>` line, each followed by `(YYYY)` and a tag.
4. **Sub-heads** — verbatim `>` lines, in page order, tagged.
5. **Bullets / benefits** — every benefit bullet or promise, verbatim `>` lines, tagged. Do not paraphrase; trim with ` […] ` only.
6. **Mechanism** — how the page says the product works (your words, with 1–3 verbatim `>` lines).
7. **Proof** — credentials, numbers, studies, testimonials (verbatim `>` lines for the headline-level ones; count the testimonials).
8. **Offer structure** — price, anchor price, bonuses, guarantee, urgency, order of the page (your words, verbatim for price and guarantee lines).
9. **Objections handled** — each objection and the page's answer (verbatim where short).
10. **Lines not to cross** — list the claims on the page that Mamivio could not use: diagnosis, "behind", earlier-milestone promises, outcome guarantees, unsupported statistics, day counts, fear hooks (owner brief §8). Verbatim `>` lines.
11. **What changed between captures** — headline or price changes across years.

## Tags
Every `>` line in sections 3–5 ends with one of: `#usable` (fits Mamivio's lines as written), `#adjacent` (fits with rewording or a different angle), `#outside-lines` (cannot be used: fear, behind, outcome promise, unsupported stat, diagnosis). Be strict: "boost your baby's development" is `#adjacent` (implies acceleration); "your baby could be falling behind" is `#outside-lines`; "know exactly what to do with your baby today" is `#usable`.

## Rules
- A `>` line must be a substring of a raw file (case/punctuation ignored). Run `python3 -I _tools/verify_sales_letters.py <slug>` before you finish each note and fix any failure.
- Everything that is not a `>` line is your interpretation and must not be in blockquote form.
- No usernames, no personal names of testimonial givers beyond first name + initial as printed.

## Output
The notes, plus `sales-letters/logs/p3-<yourtag>-report.md`: slugs done, verifier result per slug, and three observations about what these letters have in common.

ASSIGNED:
