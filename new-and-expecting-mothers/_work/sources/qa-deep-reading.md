# Parenting Stack Exchange — original API reading pass

Completed 2026-10-24. Reader prefix `qdeep01-`; evidence file `voice/qa-deep-01.jsonl`. This pass read local saved material only. No network requests, website crawl, accounts, outreach or global synthesis edits.

The collection method, API-route policies and pagination remain documented in `sources/qa-deep.md`; the native responses and license fields were preserved before this reading. Those earlier collection notes describe the pre-reading state. This document records the completed reading state.

## Exact coverage

| Step | Questions/threads | Answers | Comments | Meaning |
|---|---:|---:|---:|---|
| Downloaded questions created 2020-01-01 through 2026-10-24 | 1,155 | — | — | Exhaustive available year/date API question pagination in the saved collection |
| Infant/pregnancy local candidates | 248 | 514 | 1,356 | Every saved candidate card human-triaged |
| Excluded at card triage | 129 | 216 | 643 | Cards read; originals and their relations **not** claimed read |
| Initially human-kept, fully read | 119 | 298 | 713 | Whole question, every saved answer/comment, including OP follow-ups; 135,288 whitespace-delimited words including source headers |
| Excluded after full contextual read | 13 | Included above | Included above | Clinical or physical-harm-centered context became clear in full thread |
| Retained after full read | 106 | Included above | Included above | Zero retained originals unread |
| Retained questions supplying excerpts | 104 | — | — | 134 excerpt records from 132 individual original posts/comments |
| Retained without an excerpt | 2 | — | — | Q43078 and Q44197; read fully, no distinctive nonclinical excerpt selected |

The other 907 downloaded questions were filter-unmatched and were not human-read. The 129 card exclusions also remain original-unread. That material is not audience evidence. Full reading here always means `full_available_API_thread`, not deleted/private posts, site-wide history, external links, linked older questions, moved-to-chat conversations or image pixels. Saved image alternative text was read; linked images and their unsaved contents were not inspected. No claim of reading cited books, studies, videos or linked advice follows from reading a community answer that mentions them.

## Disposition and continuation files

- `_raw/qa-deep/human-triage.tsv`: all 248 IDs exactly once, keep/drop, practical job and exclusion rationale.
- `_raw/qa-deep/read-ledger-qdeep01.jsonl`: all 119 full reads exactly once, per-thread answer/comment counts, scope, exclusions and quote outcomes.
- `_raw/qa-deep/reconciliation-qdeep01.tsv`: all 248 candidates with original-read status, final disposition, quote IDs and neutral reasons.
- `_raw/qa-deep/reader-state-qdeep01.json`: completed kept/read/excluded ID sets.
- `_raw/qa-deep/attribution-qdeep01.jsonl`: original author object, native question/post/comment IDs, exact source URL/date, native license and native JSON path for each excerpt.
- `_raw/qa-deep/quote-budget-qdeep01.tsv`: aggregate quoted words per individual original post/comment.
- `synthesis/qa-deep-verification.json`: strict machine verification and file hash.
- `synthesis/reader-notes-qa-deep.md`: evidence interpretation and contrary/free alternatives.

Full-read exclusions: Q39801, Q39955, Q40051, Q40206, Q40613, Q42177, Q42397, Q43330, Q43347, Q43424, Q43932, Q44105 and Q44312. Their neutral reasons are in the ledger. No excerpt from an excluded thread is retained. Sensitive clinical, violence, crisis, minor, loss and personal reproductive-choice material was excluded without republishing its identifying details in these notes.

The 106 final retained jobs are registry/household equipment 19; travel 4; sleep 31; work/daycare 5; awake play/language activities 19; postpartum/sibling/household support 8; solids/mealtimes 14; weaning boundaries 1; caregiver/home adaptation 4; newborn administration 1. These are selected-thread counts, not people or market prevalence. `other_*` labels describe concrete task categories for this triage, not new README quote vocabulary. No new quote themes, speaker values, stage values or type values were added.

## Voice, attribution and limits

Every excerpt uses `source_class=qa_community`, `evidence_kind=original_api_post`, the individual preserved thread text and original API identifiers. Dates refer to the quoted author’s post/comment, not the question by default and not this capture date. All selected works carry native `CC BY-SA 4.0`; the author/license provenance is retained separately and linked from each voice record. General content-reuse rights or permission for commercial reuse are not implied by the saved API response. Missing/deleted author identity remains unknown; an advisor’s title or claimed qualification is not verified professional authority.

No names/usernames appear in excerpts or contexts. Speaker tags preserve uncertainty: having a spouse or breastfeeding alone was not used to assign a mother identity. Explicit pregnancy/first-time-mother statements, partner roles and self-described caregiver roles are retained where supported. One post explicitly distinguishes six months chronological from four-and-a-half months adjusted age; its context preserves both. Infant behavior and age do not establish diagnosis, cause, safety or an expected result.

There are 77 known native author IDs among the selected excerpts, with three additional excerpt records whose original author identity is unavailable. These are not 80 independently confirmed people. One known author supplies 19 excerpts and asks 15 of the 104 quoted questions. Repeated questions/follow-ups from the same household must not be counted as separate customers. Several accounts span baby-to-toddler years, which helps inspect changing constraints but reduces independence.

The Q&A format favors problems that can receive answers and explicitly discourages localized shopping recommendations. The corpus includes pandemic restrictions, several countries, fathers/partners, carers and non-parent advisors. It is not a current representative sample of mothers in an English-speaking launch country. Questions dated 2020 cannot be presented as current demand or current guidance. No willingness to buy a Mamivio report, tested price, transaction, report outcome, prevalence or efficacy estimate was observed.

## Verification and resume rule

`python3 mamivio.com/research/global/_tools/verify_quotes.py mamivio.com/research/global/voice/qa-deep-01.jsonl`

`python3 mamivio.com/research/global/_tools/verify_qa_deep.py`

Both pass with **0 failed**. Strict checks include original-author body text excluding third-party blockquotes; exact preserved-text case/punctuation; URL, timestamp, author/license provenance; README vocabulary; aggregate maximum **25 quoted words per individual original post/comment**; maximum context 18 words; all candidate/kept/read/exclusion ID sets; and global quote-ID uniqueness. No safety-sensitive peer treatment or technique is promoted as clinical guidance.

This assignment is finished: 248/248 cards and 119/119 initially retained originals. Do not append-rerun this reader or reuse its IDs. A new scope requires a new prefix, explicit provenance and a separate ledger. The 907 unmatched questions and 129 card-excluded originals are documented exclusions/unread inventory, not a deferred remainder of the kept assignment.
