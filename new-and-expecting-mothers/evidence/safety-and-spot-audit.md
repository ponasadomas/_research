> **Historical initial-pass audit.** This document records the earlier 418-record synthesis and source scope. The current synthesis is audited in [audit.md](audit.md); current totals and remaining work are in [session-report.md](session-report.md). Its references to “final” or “latest” apply to that earlier wave.

# Final safety and source-context audit — 2026-10-24

Scope: all **6 frozen safety hits** and the **20 frozen random spot-check records**, against their saved raw source context. No collection or sample regeneration was performed. Exact selected excerpts, surrounding original-review units or source passages, speaker, stage and neutral context were read. Every selected quote is a literal substring of its cited raw file, including its spelling and punctuation.

**Result:** all 6 safety-hit records retained; 20/20 sampled quote texts matched. Six records received conservative context/speaker/stage corrections. No quote text, id or total record count changed; the final database still contains **418 quotes**. These checks establish source fidelity and the stated exclusions for the reviewed records, not medical safety, efficacy or representative audience coverage.

## Frozen inputs

- `_raw/audit/safety-hits.jsonl`, 6 records, SHA-256 `16690b380937cb8a40fdd7c90647354d48d5acd40294eea47ef0c44fe4992ba6`.
- `_raw/audit/spot-check.jsonl`, 20 records, SHA-256 `4192f6f49f1bbd00495990ef9028e6218011c67a50a0c6fa41d363451790cdb7`.

The frozen files retain the records as sampled **before** the corrections below. The live voice files contain the corrected metadata. Do not overwrite these audit inputs to hide the differences. Source-context reading packet: `scratchpad/audience/final-audit-context-packet.txt`. Exact before/after metadata: `scratchpad/audience/final-audit-corrections.json`. The parent was notified before distribution-changing corrections and explicitly authorized them. Counts by speaker/stage must be recounted separately without drawing a new sample.

## Six safety hits: individual dispositions

| Id | Source context checked | Disposition and boundary |
|---|---|---|
| guide01-001 | CDC's milestone-checklist methodology and intended-use section, `_raw/guidance/cdc-milestones.txt` | **Retain.** The developmental-delay keyword is part of an official warning against using checklists as screening/diagnostic tools. Professional/institutional voice and unknown stage are appropriate. This limits clinical claims rather than endorsing a report diagnosis. |
| mkt01-0008 | CDC app feature list and screening disclaimer, `_raw/competitors/cdc-milestone-tracker.txt` | **Retain as official resource description.** Prematurity appears in a description of corrected-age checklists. It is not a parent's case, a diagnosis or evidence that Mamivio can assess premature babies. No efficacy or readiness claim is adopted. |
| rev01-0085 | Full original review `11492563044`, `_raw/reviews/solidstarts-us-corpus.txt` | **Retain with stage corrected to unknown.** The excerpt concerns not returning to a long purchased plan. The surrounding case includes dietary complications and a request for substitution-aware records for appointments. No allergy-exposure protocol is quoted or endorsed. Preserve this clinical context when interpreting format usability; do not recast it as proof about all ordinary first-solids parents. Exact child age is unstated. |
| rev01-0091 | Full original review `12554899373`, `_raw/reviews/solidstarts-gb-corpus.txt` | **Retain.** The mother praises understandable information and records used at an allergy clinic. The selected excerpt concerns information overload. Mother identity is explicit; stage remains unknown. This is a usability account alongside clinical care, not evidence that an app safely manages allergies or replaces a clinic. |
| rev01-0093 | Full original review `12889816220`, `_raw/reviews/solidstarts-gb-corpus.txt` | **Retain as historical workflow objection.** It specifically concerns access to allergen-introductory meals in a July 2025 version. No exposure timing, dose or clinical instruction is in the selected quote. The original reviewer describes a workaround of marking unserved meals complete; that workaround is not quoted as advice and must not be recommended. No current-app-wide defect is established. |
| rev01-0126 | Full original review `11123468172`, `_raw/reviews/wonderweeks-us-corpus.txt` | **Retain.** The source describes ordinary milestone comparisons and extra anxious searches. There is no disclosed acute crisis or self-harm, and no diagnosis is inferred. The excerpt asks for context/ranges; it does not validate scheduled leaps or indicate a child is delayed. |

No reviewed hit contains a selected account centered on violence, self-harm, pregnancy loss, infant death or a minor as the target buyer. The presence of clinical material elsewhere in a raw source does not convert its ordinary usability excerpt into clinical guidance.

## Twenty random source-context spot checks

All entries below passed literal text/spelling/punctuation and source-file checks. “Unknown” means the source does not establish that attribute. Community entries remain **index extracts**, with original-thread full-read status false; reading surrounding saved index text does not change that status.

| # | Id | Speaker/stage and surrounding context | Result |
|---:|---|---|---|
| 1 | rev01-0055 | Full Huckleberry GB review `7451826944`. The author is one first-time mother **working as a nanny**, returned to work and then stopped app use after a reported paywall change. | **Context corrected.** “Mother and nanny” incorrectly suggested two people. `gave_up_parent` and `return_to_work` are supported. Historical 2021 pricing and the author's billing allegations are not current verified facts. A retrospective PND reference is outside the quoted billing objection; no clinical claim adopted. |
| 2 | aud01-0087 | Saved community unit `056.txt`: commenter describes setting private recurring pumping blocks as unavailable time on a work calendar. Gender and baby age are not supplied. | **Context corrected.** Changed implied successful protection of breaks to the reported action of reserving breaks. Parent unspecified/return-to-work supported. No employer-compliance outcome established. |
| 3 | rev01-0125 | Full Wonder Weeks US review `10003809993`: author says fourth baby and retrospectively wonders what they were doing wrong; praises explanatory forecasts. | **Speaker/context corrected.** Fourth child does not establish the author's gender. Changed `experienced_mother` to `parent_unspecified` and “Mother of four” to “Parent of four.” Unknown stage remains. Perceived forecast accuracy is not scientific validation. |
| 4 | aud01-0035 | Saved community unit `020.txt`: parent says five-month-old received an individual pediatrician's go-ahead and asks how to begin. | **Retain.** Parent unspecified and 4–6 month stage explicit. Context correctly reports a clinician conversation, not a universal age recommendation. Other saved replies include food-serving instructions; none is adopted as advice. |
| 5 | aud01-0154 | Saved community unit `092.txt`: author refers to “fellow FTM,” a baby born six weeks earlier, and a checklist shared retrospectively. | **Retain.** New-mother identity and looking-back stage supported. Country limits are stated in the source. Sharing a free list is not proof of paid-report demand. |
| 6 | rev01-0086 | Full Solid Starts US review `14046454009`: objects to completing account/profile questions before discovering paid access. | **Retain.** Reviewer/unknown stage conservative. Context preserves the onboarding objection without adopting allegations about the seller's motives. |
| 7 | aud01-0006 | Saved community unit `003.txt`: retrospective commenter describes asking relatives for specific chores and needs. Visible timestamp is 2026-08-16. | **Retain.** Parent unspecified/looking-back/date supported. AU is community context, not established residence. The source does not establish that relatives always help. |
| 8 | aud01-0095 | Saved community unit `060.txt`: worker counts walking to a separate room, pumping, cleanup and return travel. | **Retain.** Parent unspecified/return-to-work and 35–40 minute total supported. This is one person's reported time, not a physiological interval or universal planning estimate. |
| 9 | rev01-0023 | Full BabySparks US review `9298047241`: author self-identifies as a pediatric nurse recommending a free resource to patient families. | **Retain.** `reviewer` avoids credential verification; unknown stage appropriate. Context identifies the credential as self-described. No inference that “my parents” means the author's own parents. |
| 10 | rev01-0147 | Full Pump Log GB review `13986062259`: “tired mama” values simple records, reminders and a calculator. | **Retain.** Mother identity explicit, stage unknown. Broader supply-management claims are the author's perception and excluded from the selected excerpt/context as guidance. |
| 11 | aud01-0028 | Saved community unit `017.txt`: commenter says solids started that week, tried the app, values free serving lookup and would not pay. | **Stage corrected to unknown.** The commenter's baby age is unstated; the thread opening parent's age must not transfer to this commenter. The excerpt supports trial/value objection, not nonpayment or today's offer terms. General-purpose AI and Australian-food references remain separate contextual observations. |
| 12 | rev01-0134 | Full Wonder Weeks GB review `9461607597`: parent says activities often confirm things they already do instinctively. | **Retain.** Parent unspecified/unknown stage supported. Reassurance is a reported experience; exact leap timing claimed elsewhere in the review is not validated. |
| 13 | rev01-0089 | Full Solid Starts US review `13852876795`: paying reviewer describes inconsistent logging and unclear next meals. | **Retain.** Reviewer/unknown stage conservative. The source includes allergen workflow details, but the selected quote asks for next-meal guidance and contains no clinical protocol. Payment is self-report, not verified transaction evidence. |
| 14 | rev01-0040 | Full BabySparks GB review `7164790078`: content ideas praised but paid access/support failure and cancellation planned. | **Retain.** Reviewer/unknown stage supported. Context preserves the complaint and planned cancellation, preventing a positive excerpt from becoming a misleading positive testimonial. |
| 15 | aud01-0041 | Saved community unit `026.txt`: “Signed, concerned Dad,” six-day-old infant, premium-value question. | **Retain.** Partner/father and newborn stage explicit. The question is not evidence of a premium purchase or a claim about current pricing. |
| 16 | mkt01-0005 | BabySparks saved server text: weekly development reports listed in a premium-package section alongside pricing/form markup. | **Retain as seller claim with visibility caveat.** Advisor/unknown stage and seller provenance appropriate. Markup includes legacy/conflicting offer fields; the quote establishes captured copy, not current rendered availability, functioning reports or efficacy. |
| 17 | rev01-0016 | Full Kinedu GB review `14587131927`: explicitly using pregnancy-app Master Classes, reports black-screen, caption and interface faults. | **Retain.** Reviewer/unknown stage conservative; no trimester inferred. Context correctly identifies pregnancy usage and multiple technical issues. |
| 18 | rev01-0087 | Full Solid Starts US review `12072522073`: initial complaint followed by an update praising a reported rollback to a free database. | **Stage corrected to unknown.** Starting solids a month earlier does not supply exact baby age. The selected phrase occurs in the final update, and context correctly preserves that final outcome rather than presenting the superseded paywall complaint alone. |
| 19 | rev01-0011 | Full Kinedu GB review `6104535698`: “new mum on maternity pay,” wants monthly payment rather than a large upfront amount. | **Retain.** Mother identity explicit, stage unknown. The 2020 amount has no stated currency in the selected text and is not current-price evidence. |
| 20 | rev01-0067 | Full Napper US review `11414028860`: ordinary predictions praised, disrupted-sleep help found lacking, reviewer still uses the tracker. | **Retain.** Parent unspecified/unknown stage appropriate. Objection is feature fit, not proof the product universally fails; context avoids clinical endorsement or implying complete abandonment. |

## Corrections and effect on counts

| Record | Before | After |
|---|---|---|
| rev01-0055 | Context says “Mother and nanny stopped…” | Context says “Mother working as a nanny stopped…” |
| aud01-0087 | Context asserts a tool “helped protect work breaks” | Context reports recurring blocks “used to reserve workplace pumping breaks” |
| rev01-0125 | `speaker=experienced_mother`; context “Mother of four…” | `speaker=parent_unspecified`; context “Parent of four…” |
| rev01-0085 | `stage=baby_6_12_months` | `stage=unknown` |
| rev01-0087 | `stage=baby_6_12_months` | `stage=unknown` |
| aud01-0028 | `stage=baby_4_6_months` | `stage=unknown`; the quoted commenter does not give the child's age |

The speaker distribution moves one record from experienced mother to unspecified parent. Stage distribution moves two records from 6–12 months and one from 4–6 months to unknown. Record totals, source classes, evidence kinds and quote texts are unchanged. Original selection definitions were updated to prevent future regeneration from restoring the old metadata; no quote generator was rerun.

Full quote-verification result after corrections:

`TOTAL 418 quotes, 0 failed`

No removal was indicated. Raw source material can still contain unsafe or unsupported advice; this audit is not approval to reuse all raw passages, design clinical recommendations, or claim validated results. The sampled review and community claims remain self-reports with the source/version limits stated above.
