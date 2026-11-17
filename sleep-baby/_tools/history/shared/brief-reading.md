# Reddit full reads and quote extraction — brief for every niche (2026-10-25)

First read, in full: `templates/00 - Deep Research Playbook.md` (sections 0, 2, 6, 12), the niche's `README.md` (schema and vocabulary) and `product/product-brief.md`. Your assignment names the niche, your reader name, your id prefix (e.g. `sb03`), your voice file, your scratch folder and the exact chunk ids from `<niche>/_raw/reddit/<label>/chunks.jsonl`.

Each chunk lists frozen unit files (`../_shared/_raw/reddit-2026/units/<sub>-<id>.txt`, paths relative to the niche folder). A unit holds the full post and every reply the original poster wrote in the archived thread. **Read every unit in every assigned chunk in full.** Never rewrite a unit.

## What to pull

Prefer a scene, a number, an exact sentence; one vivid quote beats five vague ones. Pull:

- the trigger scene (the night, the moment, the comment that made them post);
- the exact words others say to them (partner, mother-in-law, paediatrician, daycare, strangers) → type `others_said`;
- what they tried and how it landed, named (method, course, app, book, consultant) → `tried_failed`, `success_story`, `failure_story`;
- anything bought, cancelled, refunded, priced or called worth it / a waste → `purchase`, `price_signal`;
- the pain, fear and shame, specific not generic; what they ask strangers; what they want; what they believe went wrong;
- from the other side: why, and how it felt; from those who got through: what turned it; from those who quit: the regret;
- the niche's own jargon and the words they use for their situation (log them in your reader notes).

## Research principle

Research records what people actually say and do, in their words, whatever the subject; nothing is withheld, softened or excluded because of its subject. Readers may label material, but all quotes remain ordinary evidence and findings reproduce their words like any other quote. What is usable in copy is the owner's decision, made later; it is never a research decision.

Choose evidence for relevance and specificity. Record advice as what the speaker said; attribution is not verification of the advice.

## Record

Append only to **your own new** voice file `<niche>/voice/<file>.jsonl` (never another's). One JSON object per line: `id` (`<prefix>-NNNN`, from 0001), `source` (`reddit r/<sub>`), `url` (the post or comment permalink in the unit), `date` (that post or comment, YYYY-MM-DD), `speaker`, `stage`, `type`, `themes` (list, README seed themes first; new tags allowed, list them in your notes), `quote`, `context` (≤25 words, your words, no names), `raw_file` (the unit path exactly as in chunks.jsonl), `source_class: "reddit_archive"`, `post_id`, `comment_id` if from a reply.

Copy the literal text: typos, capitals, punctuation. Trim only with ` […] `. No usernames or names in quote or context. Speaker from what the author says about themselves; `parent_unspecified` when unsure. Stage from the text; `unknown` when unsure.

## Ledger and notes

Write `<niche>/sources/reddit-reading-<reader>.md`: chunks assigned, units in them, units read in full, units without quotes (id + reason such as duplicate, unreadable or off-topic; never subject-based exclusion), quotes written. Write `<niche>/synthesis/reader-notes-<reader>.md`: patterns you saw, each backed by quote ids, contrary evidence, new themes and jargon, product names and prices mentioned.

## Before you reply

Run `python3 -I <niche>/_tools/verify_quotes.py <niche>/voice/<file>.jsonl` until **0 failed**. Count records from disk; check ids are unique. Reply with only: units read / without selected quotes, quotes written, verify line, five strongest ids with one line each, surprises, and any unit you could not finish (exact path). Never paste quotes in bulk.
