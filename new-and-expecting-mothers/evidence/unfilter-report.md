# Global unfilter report — 2026-11-16 ruling; executed 2026-11-17

**Current state:** the later re-reading and merge are complete; see [Re-reading complete — 2026-11-17](#re-reading-complete--2026-11-17). The inventory, outstanding-queue figures and restoration-only checks below describe the earlier step and are superseded by that closing section.

Initial inventory written before changing instructions, tools, indices or findings. Scope: `global/` and `../main/`; no network, git, raw writes or source-unit re-reading. Historical source ledgers and reader notes are preserved. The inventory was refined using metadata during verification; no queued source was research-re-read. Counts describe selected quote records and logged decisions, never people or prevalence.

## Verified baseline and where the filter acted

- **Intake:** `_tools/reddit_deep_filter.py` assigns A/B/C by artifact/tool/friction regex and unavailable-body status; its safety regex only adds `safety_flag`. It emitted all 8,284 A cards, not a separate safety tier. Frozen B/C bodies remain a topic-selection backlog, not proven subject exclusions.
- **Triage:** `_tools/brief-reddit-deep-triage.md` says “Drop accounts centered on self-harm, violence/coercive control, infant death, pregnancy loss, minors or clinical crisis.” JustParents scripts additionally exclude clinical feeding, symptoms, injury, medication, atypical development, distress, and personal reproductive subjects as outside a practical report. The per-ledger table and exact decision reasons below distinguish subject/mixed reasons from ordinary scope/duplicate decisions.
- **Reading:** augmented reader briefs say “A crisis boundary may require stopping” and require `partial_safety`/`excluded_after_read` statuses. Fifteen MSE discussions have explicit partial boundaries and 231 unread tail posts; these were withheld, not full-read. Complete but excluded originals and incidentally omitted passages also remain outside the voice database.
- **Extraction:** clinical, safety, loss, coercion and other passages were withheld even inside otherwise quoted threads. The inventory records named omissions; general statements without unit ids cannot establish how many passages were lost. Raw re-reading is needed to recover their words.
- **Marking:** exactly **141** of **2,162** immutable voice records have `marketing_eligible=false`. Reasons mix subject restrictions with provenance/payment caution and ordinary adjacent topics. `evidence_use` is not a uniform category; every original reason is retained in the restoration manifest.
- **Language bank:** `_tools/build_index.py` explicitly skips `marketing_eligible=false`; `_tools/query.py --exclude-restricted` removes them and labels other query output “RESEARCH BOUNDARY ONLY”. The baseline bank contains **1,144** distinct ids, **zero** of the 141. The 80/section, 520-character, one/URL and source-balancing limits also omit ordinary records; removal of the subject filter alone would not ensure all 141 appear.
- **Findings:** `synthesis/findings.md` §13 says “No crisis, abuse, loss, infant death or minor-centered marketing” and repeats bank exclusion. Many marked ids were already cited, with summaries of their commercial relevance, but their words were largely withheld. `../main/synthesis/sub-niche-map.md` ranks clinical-adjacent jobs by compliance risk and calls some “not products”; that is an owner copy/product decision, not grounds to exclude research.
- **Tooling:** briefs repeat subject exclusions and marking rules; two native verifiers require a false eligibility flag to quote an excluded source. Renderers regenerate the bank-exclusion prose. Audit scripts count flags and search for sensitive terms; keyword hits alone are not errors. Structural/provenance checks must remain.

## Decision inventory and recovery queue

[Every logged drop/omission and the agent’s exact reason](../scratchpad/unfilter-reread/decisions.tsv) is grouped below. `subject_or_mixed` means the recorded reason names a sensitive/clinical subject, including mixed off-topic/duplicate reasons; it is a review set, not a claim that every such unit is on-topic. `off_topic_or_repetition` and `duplicate` are allowed decisions as recorded; no source bodies were rejudged. `provenance_review` records promotional/authenticity exclusions: provenance must be labelled, and relevant words retained. Broad mixed boilerplate prevents an honest exact count of censorship alone.

**“Off-topic” did hide subjects:** forum defaults explicitly put “Clinical symptom/care, miscarriage/loss, surrogacy/adoption” outside household-report needs, and feeding defaults reject clinical topics as “unsuitable for report targeting/medical instructions”. These decisions cannot be accepted as ordinary irrelevant-topic drops without re-reading.

The [queue](../scratchpad/unfilter-reread/queue.tsv) names units and raw paths for subject/mixed and provenance reassessment, including omitted passages in quoted units. Ordinary off-topic/duplicate decisions stay in the inventory. A queue row may have multiple historical stages/reasons; overlapping ledger entries are not independent units. No queued unit has been re-read in this pass. Missing words never reached `voice/*.jsonl`; restoring 141 stored records cannot recover them.

| Stage | Ledger | Subject or mixed | Provenance review | Duplicate | Off-topic or repetition |
|---|---|---:|---:|---:|---:|
| quote_extraction | `_raw/qa-deep/read-ledger-qdeep01.jsonl` | 14 | 0 | 0 | 0 |
| quote_extraction | `sources/community-reading-manifest.md` | 1 | 0 | 0 | 0 |
| quote_extraction | `sources/forums-deep-baby-final.jsonl` | 3 | 0 | 0 | 0 |
| quote_extraction | `sources/forums-deep-feeding-final.jsonl` | 2 | 0 | 0 | 0 |
| quote_extraction | `sources/forums-deep-preparation-final.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `sources/geobaby-deep-reading.jsonl` | 36 | 0 | 0 | 0 |
| quote_extraction | `sources/mse-completion-01.md` | 7 | 0 | 0 | 0 |
| quote_extraction | `sources/mse-completion-02.md` | 27 | 0 | 0 | 0 |
| quote_extraction | `voice/oblique-deep-02.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `voice/qa-deep-01.jsonl` | 6 | 0 | 0 | 0 |
| quote_extraction | `voice/reddit-augdec-01.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `voice/reddit-augdec-02.jsonl` | 2 | 0 | 0 | 0 |
| quote_extraction | `voice/reddit-augdec-03.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `voice/reddit-country-B-02.jsonl` | 2 | 0 | 0 | 0 |
| quote_extraction | `voice/reddit-july-pregnancy.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `voice/report-purchase-supplement-04.jsonl` | 1 | 0 | 0 | 0 |
| quote_extraction | `voice/report-purchase-supplement-05.jsonl` | 1 | 0 | 0 | 0 |
| reading | `_raw/oblique-deep/post-triage-exclusions.tsv` | 1 | 0 | 0 | 0 |
| reading | `_raw/qa-deep/read-ledger-qdeep01.jsonl` | 13 | 0 | 0 | 0 |
| reading | `_raw/qa-deep/reconciliation-qdeep01.tsv` | 13 | 0 | 0 | 0 |
| reading | `_raw/reddit-deep/information-payment-v1/reading-ledger.jsonl` | 8 | 2 | 0 | 12 |
| reading | `scratchpad/reddit-july-newparents/reading-ledger.tsv` | 23 | 5 | 0 | 2 |
| reading | `sources/geobaby-deep-reading.jsonl` | 11 | 1 | 0 | 2 |
| reading | `sources/mse-completion-02-reading.jsonl` | 3 | 0 | 0 | 1 |
| reading | `sources/mse-completion-03-reading.jsonl` | 1 | 0 | 0 | 0 |
| reading | `sources/oblique-deep-reading-ledger.jsonl` | 1 | 0 | 0 | 2 |
| reading | `sources/reddit-augdec-01-reading.jsonl` | 130 | 8 | 9 | 20 |
| reading | `sources/reddit-augdec-02-reading.jsonl` | 402 | 16 | 4 | 13 |
| reading | `sources/reddit-augdec-03-reading.jsonl` | 138 | 8 | 2 | 56 |
| reading | `sources/reddit-augdec-04-reading.jsonl` | 6 | 0 | 1 | 5 |
| reading | `sources/reddit-augdec-05-reading.jsonl` | 146 | 4 | 0 | 8 |
| reading | `sources/reddit-augdec-06-reading.jsonl` | 54 | 0 | 1 | 13 |
| reading | `sources/reddit-augdec-07-reading.jsonl` | 17 | 4 | 0 | 4 |
| reading | `sources/reddit-augdec-08-reading.jsonl` | 0 | 0 | 1 | 3 |
| reading | `sources/reddit-country-B-01-reading.jsonl` | 39 | 0 | 0 | 1 |
| reading | `sources/reddit-country-B-02-reading.jsonl` | 20 | 0 | 0 | 14 |
| reading | `sources/reddit-country-B-03-reading.jsonl` | 32 | 0 | 0 | 0 |
| reading | `sources/reddit-index-leads-wave03-reading.jsonl` | 1 | 0 | 0 | 0 |
| reading | `sources/reddit-july-B-solids-reading.jsonl` | 9 | 0 | 0 | 9 |
| reading | `sources/reddit-july-focused-post-read-exclusions.jsonl` | 20 | 0 | 1 | 15 |
| reading | `sources/reddit-july-pregnancy-fullread-outcomes.jsonl` | 10 | 6 | 12 | 4 |
| reading | `sources/reddit-report-purchases-v2-reading.jsonl` | 7 | 1 | 0 | 2 |
| reading | `sources/report-purchase-archive-wave03-reading.jsonl` | 10 | 0 | 0 | 1 |
| reading | `sources/report-purchase-supplement-04-reading.jsonl` | 1 | 0 | 0 | 0 |
| reading | `sources/report-purchase-supplement-05-reading.jsonl` | 3 | 0 | 0 | 0 |
| reading_partial | `_raw/oblique-deep/final-safety-unread-tails.jsonl` | 15 | 0 | 0 | 0 |
| reading_partial | `sources/mse-completion-01-reading.jsonl` | 7 | 0 | 0 | 0 |
| reading_partial | `sources/mse-completion-02-reading.jsonl` | 4 | 0 | 0 | 0 |
| reading_partial | `sources/mse-completion-03-reading.jsonl` | 3 | 0 | 0 | 0 |
| triage | `_raw/communities/triage-01.tsv` | 3 | 0 | 2 | 19 |
| triage | `_raw/communities/triage-02.tsv` | 2 | 0 | 0 | 4 |
| triage | `_raw/oblique-deep/agent-geo-triage.tsv` | 14 | 3 | 0 | 1024 |
| triage | `_raw/oblique-deep/agent-mse-triage01.tsv` | 4 | 0 | 0 | 34 |
| triage | `_raw/oblique-deep/agent-mse-triage02.tsv` | 12 | 3 | 0 | 18 |
| triage | `_raw/oblique-deep/parent-mse-triage03.tsv` | 5 | 6 | 0 | 13 |
| triage | `_raw/oblique-deep/parent-mse-triage04.tsv` | 7 | 2 | 1 | 32 |
| triage | `_raw/qa-deep/human-triage.tsv` | 109 | 0 | 0 | 20 |
| triage | `_raw/reddit-deep/triage/augdec-01.tsv` | 436 | 32 | 3 | 82 |
| triage | `_raw/reddit-deep/triage/augdec-02.tsv` | 451 | 31 | 1 | 220 |
| triage | `_raw/reddit-deep/triage/augdec-03.tsv` | 270 | 23 | 0 | 171 |
| triage | `_raw/reddit-deep/triage/augdec-04.tsv` | 86 | 11 | 0 | 91 |
| triage | `_raw/reddit-deep/triage/country-B-01.tsv` | 53 | 0 | 0 | 15 |
| triage | `_raw/reddit-deep/triage/country-B-02.tsv` | 86 | 0 | 0 | 21 |
| triage | `_raw/reddit-deep/triage/country-B-03.tsv` | 50 | 0 | 0 | 38 |
| triage | `_raw/reddit-deep/triage/july-B-solids.tsv` | 30 | 0 | 0 | 22 |
| triage | `_raw/reddit-deep/triage/july-focused.tsv` | 127 | 8 | 13 | 143 |
| triage | `_raw/reddit-deep/triage/july-newparents.tsv` | 68 | 16 | 3 | 30 |
| triage | `_raw/reddit-deep/triage/july-pregnancy.tsv` | 166 | 9 | 0 | 47 |
| triage | `_raw/reddit-deep/triage/report-purchases-v2.tsv` | 28 | 6 | 1 | 63 |
| triage | `_raw/reddit-deep/triage/sleep-purchases-v3.tsv` | 2 | 0 | 1 | 8 |
| triage | `_raw/report-purchase-archive-wave03/supplement-v1/triage-04.tsv` | 15 | 0 | 0 | 112 |
| triage | `_raw/report-purchase-archive-wave03/supplement-v1/triage-05.tsv` | 10 | 0 | 0 | 68 |
| triage | `scratchpad/report-purchase-archive-wave03/supplement-v1/triage.tsv` | 2 | 0 | 0 | 45 |
| triage | `scratchpad/report-purchase-archive-wave03/triage.tsv` | 4 | 0 | 0 | 13 |
| triage | `sources/forums-deep-feeding-triage.jsonl` | 43 | 5 | 0 | 17 |
| triage | `sources/forums-deep-followup-triage.jsonl` | 138 | 192 | 0 | 16 |

Inventory summary: `{"categories": {"duplicate": 56, "off_topic_or_repetition": 2573, "provenance_review": 402, "subject_or_mixed": 3476}, "decision_rows": 6507, "missing_paths": 0, "queue_stages": {"quote_extraction": 76, "quote_extraction;reading": 19, "quote_extraction;reading_partial": 11, "reading": 1131, "reading;reading_partial": 1, "reading;triage": 7, "reading_partial": 3, "triage": 2559}, "queue_units": 3807}`.

## Recorded reasons: what was withheld and why

The exact original words and paths are in [decisions.tsv](../scratchpad/unfilter-reread/decisions.tsv), [instruction-changes.tsv](../scratchpad/unfilter-reread/instruction-changes.tsv), and [restored-records.tsv](../scratchpad/unfilter-reread/restored-records.tsv). The first inventories decisions, the second preserves replaced rules, and the third preserves all 141 marking reasons. These are separate denominators; do not add them.

| Stage/rule | Agent’s original words | Effect and interpretation |
|---|---|---|
| Reddit triage — `_tools/brief-reddit-deep-triage.md` | “Drop accounts centered on self-harm, violence/coercive control, infant death, pregnancy loss, minors or clinical crisis.” | Subject exclusions before full reading, despite the intake safety flag itself not dropping records. |
| MSE triage — `_tools/brief-triage-oblique-mse.md` | “Card evidence is sufficient to exclude these without reading the full account for marketing.” | Clinical diagnosis/treatment, IVF, crises, self-harm, abuse, loss and minors lost full-thread reading. |
| JustParents feeding — `_tools/triage_forums_deep.py` | “Clinical feeding, anatomy, medication, pain, insufficient intake, illness or treatment-oriented question; unsuitable for report targeting/medical instructions.” | Explicit subject rejection justified by copy/report suitability, not ordinary relevance. |
| JustParents pregnancy — `_tools/triage_forums_deep_followups.py` | “Clinical symptom/care, miscarriage/loss, surrogacy/adoption, announcement or due-date/gender chat outside concrete household-report needs.” | Mixed boilerplate combines subjects and potentially ordinary irrelevant chat; its individual effects require source review. |
| Reading — `_tools/brief-reddit-augdec-01.md` and siblings | “A crisis boundary may require stopping” | A subject could interrupt reading. MSE has 15 precise interrupted discussions and 231 unread tail posts. |
| Extraction — `sources/mse-completion-02.md` | “Incidental clinical, loss, child-safety and abusive passages were excluded from extraction in otherwise practical discussions.” | Missing words cannot be restored from existing voice excerpts, even where that thread already has quotes. |
| Extraction — `voice/report-purchase-supplement-05.jsonl`, rpa05-0009 context | “Positioning advice omitted; research-only clinical boundary.” | A specific retained record documents omitted source words; the raw unit is queued. |
| Marking — `_tools/brief-reddit-augdec-01.md` and siblings | “flag `marketing_eligible=false` and explain `evidence_use`” | A copy-use gate was attached to stored research. Reasons also cover commercial provenance, uncertainty and adjacent ordinary jobs; not all 141 were clinically sensitive. |
| Bank/query — `_tools/build_index.py`, `_tools/query.py` | “Records explicitly marked research-only are excluded”; “RESEARCH BOUNDARY ONLY” | All 141 were hidden from the bank; the query switch could hide them on demand. |
| Findings — `synthesis/findings.md` §13 | “No crisis, abuse, loss, infant death or minor-centered marketing.” | Synthesis repeated copy prohibitions as research rules. |
| Main map — `../main/synthesis/sub-niche-map.md` | “not a product”; “research only as a branch of D1 or C2” | Clinical and diagnosis-adjacent topics were closed/demoted using commercial risk, despite missing research. |

All those rules now give the owner’s two-sentence principle instead of a subject gate. Pure source-class distinctions remain: a seller is still a seller, a fee for care is still not a fee for a document, and an allegation is still unverified.

There are **6,507 recorded decision/omission rows**: **3,476 subject-or-mixed** (3,406 distinct named ids), **402 provenance-review** (401 ids), **2,573 ordinary-scope/repetition** (2,569 ids), and **56 explicit duplicate** (56 ids). Stages and historical ledgers overlap. Categories reflect the recorded reason, not a new source-body judgment.

Ordinary decisions were human card/full-read judgments, with exact-body/author flags used for human duplicate review. Examples of ordinary scope decisions include older-child-only school/career matters, “in order” false matches and spending time rather than buying written guidance. Exact crossposts/repeated bodies were represented once rather than counted as independent buyers. The scope bucket is not a certification that every old “no report job” decision was justified: commercial-job narrowness and mixed boilerplate can conceal further omissions. Only a later full reading can settle ambiguous cases.

## The outstanding raw re-read queue

**3,807 distinct queued units; every raw path resolves; no duplicate unit ids.** The queue contains known subject omissions plus explicitly labelled mixed/provenance review candidates. It is not a claim that 3,807 on-topic units were all censored, nor a count of missing quotations.

| Stage combination | Unique queued units |
|---|---:|
| quote_extraction | 76 |
| quote_extraction;reading | 19 |
| quote_extraction;reading_partial | 11 |
| reading | 1,131 |
| reading;reading_partial | 1 |
| reading;triage | 7 |
| reading_partial | 3 |
| triage | 2,559 |

Including overlapping stages: **106 quote_extraction**, **1,158 reading**, **15 reading_partial**, **2,566 triage**. The 15 partial units exactly match `_raw/oblique-deep/final-safety-unread-tails.jsonl`; their 231 remaining posts are still unread.

Thirty July BabyLedWeaning card drops have no individual frozen unit; their queue path is the saved submissions gzip, with the post id identifying the row to extract later. Seventeen GeoBaby and 39 MSE drops point to the saved listing/card JSONL because no complete local thread was captured for them; re-reading their saved excerpts alone cannot recover absent full discussions. Future collection would be a separate task. Other rows point to existing individual units or native originals.

The main A/B/C and unmatched-question backlogs are separately recorded in existing coverage files and are not all newly called censorship. Missing comment sources, unavailable bodies, unviewed media and unharvested originals remain missing. General reader statements about omitted clinical/safety/legal passages without unit ids cannot supply an honest exact unit/quote count; the queue covers named evidence, not an invented exhaustive recovery count. No research re-reading or new quote extraction was performed. Source access during verification was mechanical matching of already stored quotations.

## Restoration and resulting conclusions

All **141** marked records are ordinary research in both `synthesis/quote-index.md` and `synthesis/quote-catalogue.jsonl`. All **2,162** stored records now appear once in the bank and catalogue: the bank grows by **1,018 ids**, comprising the 141 restored and 877 unmarked records previously omitted by length/source/section/URL sampling. The complete bank removes those display caps for everyone, rather than retaining a second eligibility class. Scoring/theme order and context/provenance links remain; duplicate-id, source, vocabulary and attribution checks remain.

Original finished voice files are immutable under `~/GitHub/_research/README.md` and remain byte-for-byte unchanged. Their old eligibility metadata documents the historical run; it is ignored by query/index code. The generated ordinary-record catalogue strips `marketing_eligible` and `evidence_use`, retaining every other field unchanged. `counts.json` now reports zero active research-only exclusions and 141 historically marked records. The deprecated query switch is a no-op and returns all 141 in a direct comparison.

| Original voice file | Restored records |
|---|---:|
| `voice/oblique-deep-05.jsonl` | 1 |
| `voice/offer-followups-wave03.jsonl` | 4 |
| `voice/reddit-augdec-01.jsonl` | 8 |
| `voice/reddit-augdec-02.jsonl` | 4 |
| `voice/reddit-augdec-03.jsonl` | 39 |
| `voice/reddit-augdec-05.jsonl` | 2 |
| `voice/reddit-augdec-06.jsonl` | 1 |
| `voice/reddit-augdec-07.jsonl` | 9 |
| `voice/reddit-country-B-01.jsonl` | 8 |
| `voice/reddit-country-B-02.jsonl` | 3 |
| `voice/reddit-country-B-03.jsonl` | 15 |
| `voice/reddit-july-B-solids.jsonl` | 1 |
| `voice/reddit-july-newparents.jsonl` | 2 |
| `voice/report-buyers-wave03.jsonl` | 7 |
| `voice/report-purchase-archive-wave03.jsonl` | 12 |
| `voice/report-purchase-supplement-04.jsonl` | 13 |
| `voice/report-purchase-supplement-05.jsonl` | 9 |
| `voice/reviews-wave-03.jsonl` | 3 |

The initial findings cited 28 of the marked ids (113 not cited), the niche ranking 14, the purchase table 9 and the main map 2. Citation alone did not show the words: all 141 now have complete stored quotations under nine substantive themes in `synthesis/evidence.md`, and the strongest quotations appear in the existing findings/ranking/purchase/country/success documents and main map. No restored class is relegated to a restricted appendix. The evidence layer is allowed to be long; the findings select their strongest examples on repetition and usefulness.

- **Sleep:** still leads on observed paid tailoring, but repeat spending, unresolved support dependence, AI failures and tracking distress sharpen the limit of a static report. Positive and mixed outcomes remain beside the failures.
- **Pumping/feeding:** a paid calculator, paper rejection, human demonstration requests and opting out of pumping weaken a universal paper-logistics assumption. Allergy-input failure and a reported clinician finding remain full evidence alongside course spending.
- **Development:** wanting structure without believing the baby is behind is a distinct motive; difficulty talking to the baby is retained without making it an inferred diagnosis or excluding it.
- **Handoff/leave/help:** ignored apps, refusal to create more lists, preference for paid physical help and a lost prepaid childcare place make participation/capacity separate from planning.
- **Clinical/emotional subjects:** the main map no longer closes them as “not products” because of advertising risk. Information-product fit and post-use/purchase evidence remain unresolved; product/copy decisions belong to the owner.
- **Provenance:** promotion, hosted testimony and incentive allegations are quoted with uncertainty, rather than hidden or upgraded to independent buyer proof.

Each revised main findings document ends with **“What the 2026-11-16 unfilter changed”**, giving before/after conclusions and supporting ids. Product-brief conclusions link to that record. The ranking remains conditional; restoration adds no verified standalone-report purchase, receipt, clinical effect, prevalence or launch-country result.

## Instructions and tooling

[Instruction changes](../scratchpad/unfilter-reread/instruction-changes.tsv) preserve **135 exact replaced clauses across 83 files**; the changed-file list also includes README, renderer and other tool changes. Forty-two reader/triage/audit briefs now retain every subject.

`build_index.py` emits the complete thematic bank, ordinary JSONL catalogue and bank counts. `query.py` never excludes or warns on old eligibility fields. `audit_database.py` separates historical marking from active exclusion, and writes new audit artifacts outside `_raw/`. The two native quote verifiers, July quote helper and scratch verifiers now test actual completed reading/provenance instead of requiring eligibility flags. Existing word budgets, quote exactness, native body/date/URL/author, vocabulary, duplicate, hash and completeness checks remain.

JustParents triage defaults now keep previously subject/mixed default cases pending full human topic/duplicate review, rather than silently reclassifying them as ordinary off-topic drops. Earlier one-off reader helpers no longer generate subject-excluded statuses or stamp new research-only flags; unreviewed old exception lists remain pending topic review. Their frozen source ledgers and outcomes were not rewritten. Renderers and templates no longer regenerate the subject rule.

Historical notes/logs remain history, including old counts/restrictions in `synthesis/audit.md`, `session-report.md`, `research-wave-03.md`, `continuation-2026-10-24.md`, `advertiser-wave04-session-report.md`, `_tools/STATE-deep-pass.md`, and the data-only `scratchpad/reddit-augdec-01/semantic20_audit.py` replay. These are not current rules. Old replay builders/audits were not executed: several write frozen raw artifacts or invoke git, and snapshot-specific totals describe earlier waves. The current read-only/rebuilt-index checks below verify this change without doing either.

## Verification output

All Python commands used `python3 -I`. No git or network was used. Raw and historical data were never regenerated. `verify_findings.py` was extended to read the requested id-before-blockquote layout, because its former inline-only parser reported zero pairs for those quotes.

```text
$ python3 -I mamivio.com/research/global/_tools/build_index.py
sections 18 | records 2162 | duplicate ids 0

$ python3 -I mamivio.com/research/global/_tools/audit_database.py --as-of=2026-11-17 --counts-only --audit-dir=scratchpad/unfilter-reread/checks
TOTAL 2162 quotes; 0 structural errors; 57 safety hits in review queue; 20 spot-check records
Counts-only: keyword matches and sample were counted, not written as a new subject gate or a manual review.

$ python3 -I mamivio.com/research/global/_tools/verify_quotes.py
ads-01.jsonl: 4 quotes, 0 failed
ads-deep-01.jsonl: 2 quotes, 0 failed
audience-01.jsonl: 155 quotes, 0 failed
forums-deep-01.jsonl: 11 quotes, 0 failed
forums-deep-02.jsonl: 15 quotes, 0 failed
guidance-01.jsonl: 8 quotes, 0 failed
guidance-02.jsonl: 2 quotes, 0 failed
market-01.jsonl: 27 quotes, 0 failed
market-02.jsonl: 16 quotes, 0 failed
market-03.jsonl: 5 quotes, 0 failed
market-04.jsonl: 2 quotes, 0 failed
market-05.jsonl: 6 quotes, 0 failed
oblique-deep-01.jsonl: 57 quotes, 0 failed
oblique-deep-02.jsonl: 111 quotes, 0 failed
oblique-deep-03.jsonl: 106 quotes, 0 failed
oblique-deep-04.jsonl: 81 quotes, 0 failed
oblique-deep-05.jsonl: 53 quotes, 0 failed
offer-followups-wave03.jsonl: 4 quotes, 0 failed
qa-deep-01.jsonl: 134 quotes, 0 failed
reddit-augdec-01.jsonl: 102 quotes, 0 failed
reddit-augdec-02.jsonl: 134 quotes, 0 failed
reddit-augdec-03.jsonl: 207 quotes, 0 failed
reddit-augdec-04.jsonl: 27 quotes, 0 failed
reddit-augdec-05.jsonl: 49 quotes, 0 failed
reddit-augdec-06.jsonl: 44 quotes, 0 failed
reddit-augdec-07.jsonl: 22 quotes, 0 failed
reddit-augdec-08.jsonl: 16 quotes, 0 failed
reddit-country-B-01.jsonl: 31 quotes, 0 failed
reddit-country-B-02.jsonl: 47 quotes, 0 failed
reddit-country-B-03.jsonl: 39 quotes, 0 failed
reddit-july-B-solids.jsonl: 47 quotes, 0 failed
reddit-july-focused.jsonl: 97 quotes, 0 failed
reddit-july-newparents.jsonl: 142 quotes, 0 failed
reddit-july-pregnancy.jsonl: 42 quotes, 0 failed
reddit-payment-01.jsonl: 17 quotes, 0 failed
reddit-purchase-followups-wave03.jsonl: 3 quotes, 0 failed
reddit-report-purchases-v2.jsonl: 3 quotes, 0 failed
report-buyers-wave03.jsonl: 7 quotes, 0 failed
report-purchase-archive-wave03.jsonl: 21 quotes, 0 failed
report-purchase-supplement-04.jsonl: 13 quotes, 0 failed
report-purchase-supplement-05.jsonl: 22 quotes, 0 failed
reviews-books-01.jsonl: 9 quotes, 0 failed
reviews-followup-01.jsonl: 26 quotes, 0 failed
reviews-media-01.jsonl: 171 quotes, 0 failed
reviews-registry-01.jsonl: 3 quotes, 0 failed
reviews-wave-03.jsonl: 22 quotes, 0 failed
TOTAL 2162 quotes, 0 failed
exit_code=0

$ python3 -I mamivio.com/research/global/_tools/verify_findings.py
TOTAL 2640 id references, 2335 exact quote pairs, 0 failed
exit_code=0

$ python3 -I mamivio.com/research/_shared/_tools/check_ids.py global
2162 records, 2162 distinct ids, 0 duplicated
exit_code=0

$ python3 -I mamivio.com/research/_shared/_tools/verify_findings_ids.py mamivio.com/research/global/synthesis/findings.md global
111 distinct ids cited, 0 unresolved
0 verbatim fragments paired with an id, 0 failed
exit_code=0

$ python3 -I mamivio.com/research/main/_tools/verify_map_ids.py mamivio.com/research/main/synthesis/sub-niche-map.md
79 distinct ids cited, 0 unresolved
23 verbatim fragments paired with an id, 0 failed
exit_code=0

$ python3 -I mamivio.com/research/global/_tools/verify_unfilter.py
{
  "records": 2162,
  "catalogue_records": 2162,
  "bank_ids": 2162,
  "restored": 141,
  "themed_restored_quotes": 141,
  "query_compatibility": "141 of 141; no exclusions",
  "revised_markdown_check": "TOTAL 2926 id references, 2368 exact quote pairs, 0 failed",
  "changed_python_syntax_checked": 59,
  "exact_inline_fragments": 23,
  "partial_MSE_units": 15,
  "unread_MSE_tail_posts": 231,
  "preserved": {
    "reader_notes_and_run_logs": 47,
    "source_files": 172,
    "voice_files": 46
  },
  "queue_units": 3807,
  "queue_stage_combinations": {
    "reading": 1131,
    "triage": 2559,
    "quote_extraction;reading": 19,
    "reading;triage": 7,
    "quote_extraction": 76,
    "reading_partial": 3,
    "quote_extraction;reading_partial": 11,
    "reading;reading_partial": 1
  },
  "errors": [],
  "failed": 0
}
exit_code=0
```

All **46 voice files**, **172 source files**, and **47 reader-note/run-log files** checked against the pre-edit SHA256 manifest are unchanged. All **43,113 raw-file paths/sizes/mtimes** match the pre-edit inventory: zero additions, deletions or size/mtime changes. This raw preservation check is metadata equality, not a newly claimed full raw-content hash audit. The full command output and structured results are in [checks/](../scratchpad/unfilter-reread/checks/).

## Remaining uncertainty

Mixed reasons, generic marking labels and unlogged passage omissions prevent a precise count of subject-only censorship or missing quotes. The 3,807-unit queue includes review candidates; genuinely off-topic or duplicate material may remain unquoted after a later full review. Fifty-six listing-only units lack complete local originals, and some available units have missing comments. None of these gaps has been filled by inference or by relabelling an unread source as read.

## Every changed file

**130 files created or changed**, all under the two authorized folders. No existing file was deleted. Temporary execution helpers are outside the repository in `/tmp`; they are not deliverables.

- `mamivio.com/research/global/README.md`
- `mamivio.com/research/global/_tools/audit_database.py`
- `mamivio.com/research/global/_tools/brief-audience.md`
- `mamivio.com/research/global/_tools/brief-continuation-semantic20.md`
- `mamivio.com/research/global/_tools/brief-country-B-01.md`
- `mamivio.com/research/global/_tools/brief-country-B-02.md`
- `mamivio.com/research/global/_tools/brief-country-B-03.md`
- `mamivio.com/research/global/_tools/brief-deep-forums.md`
- `mamivio.com/research/global/_tools/brief-deep-oblique.md`
- `mamivio.com/research/global/_tools/brief-deep-reddit.md`
- `mamivio.com/research/global/_tools/brief-final-safety-audit.md`
- `mamivio.com/research/global/_tools/brief-forum-feeding-kept.md`
- `mamivio.com/research/global/_tools/brief-forum-kept-activities.md`
- `mamivio.com/research/global/_tools/brief-forum-kept-baby.md`
- `mamivio.com/research/global/_tools/brief-forum-kept-preparation.md`
- `mamivio.com/research/global/_tools/brief-forum-kept-work.md`
- `mamivio.com/research/global/_tools/brief-geobaby-deep-reader.md`
- `mamivio.com/research/global/_tools/brief-mse-completion-01.md`
- `mamivio.com/research/global/_tools/brief-mse-completion-02.md`
- `mamivio.com/research/global/_tools/brief-mse-completion-03.md`
- `mamivio.com/research/global/_tools/brief-offer-followups-wave03.md`
- `mamivio.com/research/global/_tools/brief-qa-deep-reader.md`
- `mamivio.com/research/global/_tools/brief-reader-oblique.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-01.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-02.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-03.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-04.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-05.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-06.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-07.md`
- `mamivio.com/research/global/_tools/brief-reddit-augdec-08.md`
- `mamivio.com/research/global/_tools/brief-reddit-deep-reading.md`
- `mamivio.com/research/global/_tools/brief-reddit-deep-triage.md`
- `mamivio.com/research/global/_tools/brief-reddit-july-focused.md`
- `mamivio.com/research/global/_tools/brief-reddit-july-newparents.md`
- `mamivio.com/research/global/_tools/brief-reddit-july-pregnancy-fullreads.md`
- `mamivio.com/research/global/_tools/brief-reddit-july-pregnancy.md`
- `mamivio.com/research/global/_tools/brief-reddit-july-wave.md`
- `mamivio.com/research/global/_tools/brief-report-buyers-wave03.md`
- `mamivio.com/research/global/_tools/brief-report-purchase-archive-wave03.md`
- `mamivio.com/research/global/_tools/brief-report-purchase-supplement-04.md`
- `mamivio.com/research/global/_tools/brief-report-purchase-supplement-05.md`
- `mamivio.com/research/global/_tools/brief-reviews-media.md`
- `mamivio.com/research/global/_tools/brief-triage-oblique-mse.md`
- `mamivio.com/research/global/_tools/build_forums_deep_source.py`
- `mamivio.com/research/global/_tools/build_index.py`
- `mamivio.com/research/global/_tools/build_july_pregnancy_ledger.py`
- `mamivio.com/research/global/_tools/build_july_pregnancy_quotes.py`
- `mamivio.com/research/global/_tools/final_continuation_consistency.py`
- `mamivio.com/research/global/_tools/finish_payment_ledger.py`
- `mamivio.com/research/global/_tools/finish_wave03_docs.py`
- `mamivio.com/research/global/_tools/integrate_continuation.py`
- `mamivio.com/research/global/_tools/integrate_wave03_root_evidence.py`
- `mamivio.com/research/global/_tools/july_focused_reader.py`
- `mamivio.com/research/global/_tools/log_oblique_read.py`
- `mamivio.com/research/global/_tools/query.py`
- `mamivio.com/research/global/_tools/render_wave03_synthesis.py`
- `mamivio.com/research/global/_tools/templates/findings-wave03-body.md`
- `mamivio.com/research/global/_tools/triage_forums_deep.py`
- `mamivio.com/research/global/_tools/triage_forums_deep_followups.py`
- `mamivio.com/research/global/_tools/verify_continuation_native.py`
- `mamivio.com/research/global/_tools/verify_findings.py`
- `mamivio.com/research/global/_tools/verify_reddit_july_b.py`
- `mamivio.com/research/global/_tools/verify_unfilter.py`
- `mamivio.com/research/global/product/product-brief.md`
- `mamivio.com/research/global/scratchpad/country-comparison-wave03/verify.py`
- `mamivio.com/research/global/scratchpad/mse-completion-02/audit.py`
- `mamivio.com/research/global/scratchpad/odeep03/audit.py`
- `mamivio.com/research/global/scratchpad/odeep05/audit.py`
- `mamivio.com/research/global/scratchpad/odeep05/finalize.py`
- `mamivio.com/research/global/scratchpad/offer-followups-wave03/audit.py`
- `mamivio.com/research/global/scratchpad/offer-followups-wave03/record.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-01/full_reader.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-01/verify.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-02/finalize.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-02/read.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-03/audit.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-03/full_reader.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-04/record.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-05/finalize.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-05/read.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-06/finalize.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-06/read.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-06/record.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-07/audit.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-07/full_reader.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-08/reader.py`
- `mamivio.com/research/global/scratchpad/reddit-augdec-08/verify.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-01/reader.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-01/verify.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-02/finalize.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-02/read.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-03/audit.py`
- `mamivio.com/research/global/scratchpad/reddit-country-B-03/full_reader.py`
- `mamivio.com/research/global/scratchpad/reddit-july-B-solids/record.py`
- `mamivio.com/research/global/scratchpad/report-buyers-wave03/prepare.py`
- `mamivio.com/research/global/scratchpad/report-buyers-wave03/verify.py`
- `mamivio.com/research/global/scratchpad/report-purchase-archive-wave03/reader.py`
- `mamivio.com/research/global/scratchpad/report-purchase-archive-wave03/reader_supp_own.py`
- `mamivio.com/research/global/scratchpad/report-purchase-archive-wave03/reader_supplement.py`
- `mamivio.com/research/global/scratchpad/report-purchase-archive-wave03/verify.py`
- `mamivio.com/research/global/scratchpad/report-purchase-supplement-04/audit.py`
- `mamivio.com/research/global/scratchpad/report-purchase-supplement-04/finalize.py`
- `mamivio.com/research/global/scratchpad/unfilter-reread/baseline-manifest.json`
- `mamivio.com/research/global/scratchpad/unfilter-reread/checks/final-check-output.txt`
- `mamivio.com/research/global/scratchpad/unfilter-reread/checks/initial-check-output.txt`
- `mamivio.com/research/global/scratchpad/unfilter-reread/checks/raw-preservation.json`
- `mamivio.com/research/global/scratchpad/unfilter-reread/checks/structural-errors.json`
- `mamivio.com/research/global/scratchpad/unfilter-reread/checks/unfilter-verification.json`
- `mamivio.com/research/global/scratchpad/unfilter-reread/decisions.tsv`
- `mamivio.com/research/global/scratchpad/unfilter-reread/instruction-changes.tsv`
- `mamivio.com/research/global/scratchpad/unfilter-reread/inventory.json`
- `mamivio.com/research/global/scratchpad/unfilter-reread/inventory.py`
- `mamivio.com/research/global/scratchpad/unfilter-reread/queue.tsv`
- `mamivio.com/research/global/scratchpad/unfilter-reread/restored-records.tsv`
- `mamivio.com/research/global/scratchpad/unfilter-reread/unresolved-paths.json`
- `mamivio.com/research/global/synthesis/country-comparison-wave03.md`
- `mamivio.com/research/global/synthesis/counts.json`
- `mamivio.com/research/global/synthesis/counts.md`
- `mamivio.com/research/global/synthesis/evidence.md`
- `mamivio.com/research/global/synthesis/findings.md`
- `mamivio.com/research/global/synthesis/language-bank-counts.json`
- `mamivio.com/research/global/synthesis/niche-opportunities.md`
- `mamivio.com/research/global/synthesis/purchase-evidence.md`
- `mamivio.com/research/global/synthesis/quote-catalogue.jsonl`
- `mamivio.com/research/global/synthesis/quote-index.md`
- `mamivio.com/research/global/synthesis/success-stories.md`
- `mamivio.com/research/global/synthesis/unfilter-report.md`
- `mamivio.com/research/main/README.md`
- `mamivio.com/research/main/synthesis/sub-niche-map.md`

## Re-reading complete — 2026-11-17

All **3,807 assigned recovery units** now have a disposition in `sources/reddit-reading-ur01.md` through `reddit-reading-ur13.md`. The readers processed all surviving assigned text and available saved replies; **3,747 units produced 4,829 new quotes**, while **60 produced none**: 49 off-topic units, five duplicate/already-covered units and six with no usable text. Missing paths: zero. Assigned surviving text still unread: zero. This closes the named re-reading queue, including units selected for mixed/provenance reasons; it does not declare every historical exclusion relevant or every original available.

All four `unfilter-digest-NN.md` files are integrated by common theme. `synthesis/evidence.md` reproduces every new quote field once, with source provenance and the requested id-before-blockquote layout. Together with the 141 earlier restored quotations it contains **4,970 distinct reproduced ids**. All **1,017 money-index ids** and **2,038 request-index ids** are carried into theme registers, preserving amounts, payment/consideration/refusal, format, free alternatives, questions and creator provenance. Repeated/cross-posted texts and follow-ups remain dependent records rather than extra people or buyers.

The database, rebuilt catalogue and language bank contain **6,991 distinct quote ids** (2,162 earlier + 4,829 new); 6,729 carry community/review source-class tags. Those platform classes include listing fragments and second-hand or creator/commercial speech, distinguished by evidence kind and reading scope rather than promoted to independent original testimony. The four conclusion documents retain every id they previously cited and use selected new examples with evidence-theme pointers. Their exact distinct-id totals are generated in `counts.md` and `counts.json`. The completed change record is [What the 2026-11-17 re-reading changed](findings.md#what-the-2026-11-17-re-reading-changed).

Sleep retains the strongest observed paid-tailoring position, with clearer distinctions between infant settling, adult sleep and possible/acceptable execution. Play now includes adult capacity and clinical uncertainty; leave/handoff includes authority, solvency and trusted care; food includes texture, allergies, fear and preparation. Recovery, distress/identity, loss, reproductive autonomy, consent, care access and coercion have substantive findings. The main map’s incompatible order, sales inference and universal cheap-selector/paper-fit claims are withdrawn. No recovered account establishes a separately priced materially personalized written report plus independent post-use evidence.

**Still unread or unavailable:**

- **56 full forum discussions remain unavailable:** only saved listing records exist for 17 GeoBaby and 39 MSE units. Their surviving titles/excerpts were read; absent text and truncated endings were not reconstructed. Four empty GeoBaby listings and two deleted/removed JustParents units account for the six zero-quote unavailable units; other listing titles can still contain quotable words. Saved extracts with abrupt gaps, absent images and linked pages remain incomplete.
- **The 231 formerly unread MSE tail posts are now read, across all 15 partial discussions; none remains unread in that named tail queue.** The 411 formerly card-dropped JustParents discussions are also read to the saved end. The captured saved-text inventory is now accounted for across 505 JustParents, 343 MSE and 183 GeoBaby discussions, without claiming deleted text or live completeness.
- **Main archived Reddit unread bodies:** 801 A, 50,286 B and 38,459 C; 14,665 bodies remain unavailable. The recovery closes 1,730 A, 244 B and four C unread originals. The separate commercial extension closes 31, leaving 14,935 readable originals unread (238 card drops and 14,697 unmatched), plus 138 unavailable bodies. The union with the earlier original-post inventory is **8,614 distinct full post ids**, an increase of 2,009 rather than 3,807. Exact set differences are in [reread-coverage.json](reread-coverage.json); frozen `_raw/` inventories are unchanged.
- **Comments:** seven main and two extension comment sources are absent. Saved identifiable replies inside assigned units were read, but auxiliary comment inventories were not reconciled by native comment id. The October figure of 145,386 unread available comments remains a historical snapshot, not a new exact remainder; neither reading a parent post nor a listing recovers absent buyer comments.
- **Q&A:** 109 formerly card-dropped questions add to 119 earlier full reads, giving 228. Twenty ordinary card drops and 907 unmatched questions remain outside this recovery. No unrelated backlog was silently promoted to a full read.
- Review histories, unviewed videos/comments and media, private/social sources, current market performance, independent report buyers, delivered paid outputs and owner customer data remain gaps recorded in source ledgers and `sources/not-harvested.md`. Source claims about treatment, law, safety, alleged harm, payment and commercial affiliation retain their uncertainty.

Only derived evidence, conclusions, records and checks were changed in this merge. No network or git was used. No `_raw/`, voice JSONL, reading ledger or digest was edited. `_tools/build_index.py` rebuilt the catalogue/language bank; `_tools/audit_database.py` rebuilt counts. The source verifier now decodes JSON and compressed native archives instead of comparing encoded bytes; the cited post is selected for structured post records. The Markdown verifier accepts a contiguous quoted fragment, while `_tools/verify_reread_merge.py` separately requires every recovered evidence block to equal its entire stored quote field. This also handles the immutable digest’s split quotation containing nested Markdown without changing its words.

The final `python3 -I` checks and protected-file hashes are in `scratchpad/unfilter-reread/checks-merge/`. These are new merge checks; the preceding restoration logs remain historical. No subject-based exclusions or hidden quote classes were introduced.
