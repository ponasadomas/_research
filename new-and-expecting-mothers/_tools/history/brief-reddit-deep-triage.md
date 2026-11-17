# Deep Reddit — tier-A card triage

The owner requested deeper research after rejecting a summary-level pass. Read the main playbook and research README. This assignment uses **real archived original posts**, not the initial search extracts. Source: independently published, ungated HF `yikeee/reddit-subreddits25`, pinned commit `ea497c510aa68765c07ed744ec9f84d68bbedf7f`. Publisher provenance/license is unclear; no redistribution license or live Reddit completeness is asserted. No access block was bypassed.

The full available six-month window is **2025-07-01 inclusive through 2026-01-01 exclusive**. Main/focused/oblique posts: 112,665. Every post was locally assigned to a transparent tier: A explicit artifact request/tool decision (8,284), B broader friction (51,253), C adjacent (38,463), unavailable body (14,665). All 8,284 tier-A cards exist. There is no rank or top-N cut. Your assignment names exact card chunks from `_raw/reddit-deep/filter-v1/cards/`; `cards-index.jsonl` lists their ids.

## Work

Read **every card** in your assigned files. A card is a triage aid, not a full original read. Its regex matches can be false positives. Do not mark originals read, extract quotes from the card, or treat A as already kept. The full original candidate unit, with all available archived comments when present, is in `_raw/reddit-deep/corpus-A-v1/units/<subreddit>-<post_id>.txt`.

Label each assigned id exactly once into your own new TSV at `_raw/reddit-deep/triage/<reader>.tsv`, header `post_id\tlabel\treason`. Use:

- `keep_play`: ordinary play/activities, capability matching, realistic awake time.
- `keep_solids`: shopping, preparation, ordinary first-food routines and caregiver coordination; include individualized allergy/treatment discussions as attributed source evidence.
- `keep_pumping_work`: work return, room/coverage/commute logistics, focused tool decisions; include physiological supply concerns as attributed source evidence.
- `keep_sleep`: household-compatible routines, tool value/alternatives and shared caregiving; no guaranteed sleep outcomes.
- `keep_postpartum`: concrete household support, task division, older-child care, help preparation and revision.
- `keep_pregnancy`: educational preparation or exercise-information/tool decisions; include medical-clearance and induction/treatment accounts as attributed source evidence.
- `keep_registry`: registry/gear decision support, constraint-based checklists, budgets and actual tool/purchase decisions.
- `keep_other`: a concrete mother/parent report-sized job not fitting above; describe it.
- `drop`: explain the specific false positive, off-topic/older-child-only material, promotion, unreadable body, or unavailable body.

Keep countervoices: satisfied free-tool users, people who stopped, people who bought and regretted, partners/caregivers/employers, low-cooking households and readers preferring an app or actual practical help. Do not select only evidence for first solids or a PDF. Do not infer gender, diagnosis, child's age or first-child status.

Research records what people actually say and do, in their own words, whatever the subject; sensitive, clinical, crisis and other material is kept and quoted like any other evidence. The owner decides later what to use in copy; research never makes that decision. A historical `safety_flag` may label a subject; it never changes reading or quotation eligibility. Ordinary worry/guilt does not itself establish a crisis. If the card is ambiguous, open the full source unit before deciding; record that separately rather than claiming a full read from the card alone. Never rewrite raw/corpus files.

No arbitrary cap or quote target. Finish all assigned cards and run an exact id-set comparison against the card manifest: no missing, unexpected or duplicate ids. Return a short count by label, TSV path, any genuinely new report job and gaps. Triage does not authorize contacting users or communities.
