# Findings synthesis — brief for every niche (2026-10-25)

You write `<niche>/synthesis/findings.md`, the document a copywriter and the owner will live in. Read first, in full: `templates/00 - Deep Research Playbook.md` (sections 0, 9, 12), the niche's `README.md` and `product/product-brief.md`, `synthesis/counts.md` (the only source of numbers), `synthesis/restricted-ids.md` (historical labels only), every `synthesis/reader-notes-*.md` (triage, market and each reader), `competitors/README.md`, `sources/reddit.md`, and `mamivio.com/research/main/ads-running/spend-footprint-by-subniche-2026-10-25.md`.

## Rules

- **Every claim cites quote ids** as `[sb01-0028]`. A claim without ids says "(interpretation)". Look ids up in `voice/*.jsonl` before citing; never cite from a reader's report alone.
- **Quoted fragments must be exact**: write `"exact words" [id]`; the fragment must be a substring of that record's quote. Prefer short fragments (12–120 characters).
- Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.
- **Numbers come only from counts.md**, labelled as counts of quotes chosen, never of people or prevalence. If you count something yourself from the merged file, show the command in an appendix.
- Where a pattern rests on a handful of quotes, say so. Where readers disagreed, show both sides with ids.
- No ad copy, no headlines. Research only.

## Sections (adapt titles to the niche)

Header: date, totals (quotes, units read, sources), "How to read this".
1. The reader in one paragraph. 2. The arc (stages, with quotes). 3. What others say to them. 4. What they try and how it lands (methods, apps, courses, consultants, free advice). 5. The other side (partners, relatives, daycare, refusers, fathers). 6. What they ask, want and fear — including the exact asks for a plan. 7. What everyone else tells them. 8. **Money**: what they bought, paid, priced, refused, called a waste or a scam, with every stated amount and its id; set against the competitor prices in `competitors/`. 9. Segments that sound different. 10. **Does the evidence support the Mamivio product** (a quiz-built personalized plan at $17.95 / $29.95 / $49.95)? For and against, with ids; what it must do to be believed. 11. Objections to expect. 12. Research principle (record words without subject-based exclusions; copy decisions belong to the owner later). 13. **What's missing**: every source not harvested (see `sources/not-harvested.md`, `sources/reddit.md` for tier A outside wave 1 and tiers B/C, books, app reviews, YouTube, Ad Library searches not yet run, browser walks pending), with paths.

## Before you reply

Run `python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py <niche>/synthesis/findings.md <niche>` until 0 unresolved and 0 failed fragments; check that historical labels have not withheld any relevant evidence. Reply with only: word count, ids cited, the verify line, the five findings you think matter most to the owner (one line each), and anything you could not support.
