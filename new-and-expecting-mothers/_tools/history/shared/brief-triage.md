# Reddit card triage — brief for every niche (2026-10-25)

You are triaging Reddit posts for one Mamivio niche. First read, in full: `templates/00 - Deep Research Playbook.md` (sections 0, 2, 6), the niche's `README.md` (vocabulary) and `product/product-brief.md`. Your assignment names the niche, the exact card files, your reader name and your output TSV.

Source: posts 2026-04-01 → 2026-10-25 from the Arctic Shift archive, saved untouched in `mamivio.com/research/_shared/_raw/reddit-2026/<sub>.posts.jsonl`. Each card has the id, subreddit, date, title, the first 350 characters and the regex matches that put it in tier A. **A card is a triage aid, not a read.** Regex matches are often false positives.

## Work

Read **every card** in every assigned file. Label each id exactly once in your own new TSV, header `post_id\tlabel\treason` (reason ≤15 words):

- `keep_core` — a parent living this niche's problem: a scene, a pain, a question, what they tried. The bulk of keeps.
- `keep_purchase` — they paid for, subscribed to, cancelled or priced something for this problem (course, consultant, app, book, program, product), or weigh doing so.
- `keep_success` — they say what finally worked or how it ended, good or bad.
- `keep_otherside` — the niche's other side (README): partner, grandparent, daycare, a parent who rejects the usual method, a professional, a sceptic, someone who quit a program.
- `drop` — off-topic for this niche, older-child-only, promotion or a seller, unreadable, a duplicate repost.

When two keep labels fit, pick the rarer one (purchase > success > otherside > core). `safety_flag=True` is an optional descriptive label and never affects selection. Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision. If a card is ambiguous, open the full post in the `.posts.jsonl` file by id before deciding.

Do not infer gender, diagnosis or the child's age beyond what the text says. No arbitrary cap or keep target: label what is there.

## Before you reply

Run an exact id-set comparison between your TSV and the ids in your assigned card files: no missing, unexpected or duplicate ids. Reply with only: counts by label, the TSV path, the id-set check result, and up to five surprises (a new theme, a product name, a pattern). Never paste card text back. Never edit raw files or another reader's TSV.
