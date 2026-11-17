# Quiz question-selection spec (for the agent building the quiz in MySlider)

Scope: everything between "the parent has entered the baby's details" and "every answer is in MySQL".
Not in scope: the report, scoring, paywall. Those come later and depend only on what this spec stores.

This folder is self-contained. Copy it into the quiz project as is.

| File | What it holds |
|---|---|
| `questions.json` | all 408 questions: id, area, skill, English text, Kinedu's Spanish and Portuguese texts (reference only), share-by-age, roles |
| `batches-by-age.json` | for every effective age 0–48: the ordered list of base questions to show (positions, screens, roles, rate at that age), the extension threshold |
| `extension-by-age.json` | for every age 0–41: the 8 "Going further" questions and the Yes-count that triggers them; 42–48: none |
| `batches-by-age.csv` | the same as the two JSON files flattened, one row per shown question, for humans |

**The batch files are lookups, not formulas. Never reconstruct a batch from `questions.json`.** The lists were captured from the
source quiz and encode choices (which question, which screen, which position) that no rule reproduces.

---

## 1. Inputs the quiz already has

From the child screen (already built): optional name, date of birth, "Born before 37 weeks?" checkbox and, when ticked, gestational
weeks 24–36 (slider, default 34).

## 2. Effective age in months (the only key that selects questions)

Compute **server-side at submission**, in one fixed timezone, from the date of birth and "today". Do not trust the browser clock for
the stored value (it may be used for the live screen, but the server recomputes).

1. **Chronological age** = completed calendar months between DOB and today. The same day-of-month counts as completed:
   DOB 2024-11-02 on 2026-11-02 is 24 months; DOB 2024-11-03 on 2026-11-02 is 23 months. Today's DOB is 0 months.
   Month-end convention (decided): a month is completed on the same day-of-month as the birthday; when that day does not
   exist in the month, on its last day. In code: effective months = the largest N such that `addMonths(DOB, N)` (day clamped to
   the last day of the target month) is not after today. DOB 31 Jan 2026: 0 months on 27 Feb, 1 month on 28 Feb, 2 on 31 Mar,
   3 on 30 Apr. The source quiz never exposed this case; this is our rule.
2. **Prematurity correction**, applied only when the box is ticked **and chronological age < 24**:

   | Gestational weeks | Subtract |
   |---|---|
   | 34, 35, 36 | 1 month |
   | 30, 31, 32, 33 | 2 months |
   | 25 … 29 | 3 months |
   | 24 | 4 months |
   | 37+ or box unticked | nothing |

   Clamp the result at 0. Set `corrected = true` whenever a subtraction was applied, even if clamped to 0.
   At chronological age 24 or more, no correction and `corrected = false`, even if the box is ticked.
3. **Effective age** = the result. Valid range 0–48.
4. **49 months or more**: no questions. Show the "too old" screen (already specified elsewhere) and stop.

Store both the chronological and the effective age (section 7).

## 3. Base questions: what to show, in what order

Look up `batches-by-age.json` → `batches[<effective age>]`.

- **Four screens, always, in this fixed order**: Physical, Cognitive, Language, Social-Emotional (`screens`).
- `questions[]` is the complete on-screen order. `position` is 1-based across the whole quiz; `screen` (1–4) and `screen_area` say
  on which screen the question appears. Render the questions of one screen in ascending `position`.
- `role` is `anchor`, `item` or `calibration`. **All three render identically to the parent.** The role only matters for storage.
  A calibration question appears at the end of screens 1–3 and often belongs to a different area than the screen it sits on
  (`question_area` ≠ `screen_area`), which is intended. Ages 37–48 have no calibration questions; age 45 has one anchor; 46–48 none.
  Nothing to do about any of this: the file already encodes it.
- Count per age: 39 questions for ages 0–36, 36 for 37–44, 33 at 45, 27 at 46, 24 at 47, 22 at 48. 1,837 base slots in total.
- Text: `questions.json` → `text_en` by `question_id`. Show it verbatim as a statement; it is already phrased as one
  ("Can walk while holding a small toy.").
- `rate_at_age` is a hidden number per question per age. **Never display it.** Store it with the answer (section 7).

## 4. Answering and navigation

- Exactly two answers per question: **"Not yet" = 0** and **"Yes" = 1**. No skip, no "not sure".
- Display mode: the live winner on the source quiz shows **one screen per area with all its questions as rows**, each row with
  the two buttons, and a Next button that stays disabled until every row on the screen is answered. Build that. (The data also
  supports one question per slide if a later test wants it.)
- Screen header copy: `AREA 1 OF 4` … `AREA 4 OF 4`, the area name, the line `Chosen for your baby at {effective age} months`, and a
  counter `{answered}/{on this screen}`. Next button: `Next: {next area} ›`; on the last area `See {name}'s results →`
  (`See your baby's results →` when no name).
- **After the last question** (base screen 4, or the extra screen when shown) there is **no celebration screen**. Submit the
  remaining answers, mark the session complete in MySQL, show a "Calculating…" page, and redirect automatically to the report
  URL. Until the report exists, the redirect target is a placeholder page that says the answers are saved. No button, no email.
- **Back** between the four base screens is allowed and keeps answers. Changing an answer overwrites the previous value.

## 5. The extra screen ("Going further"), shown at most once

After the fourth base screen is complete:

1. Count the Yes answers **among the base questions only**. Call it `K`.
2. Read `extension-by-age.json` → `extension[<effective age>]`.
3. Show the extra screen **only if** `K >= shown_when_base_yes_count_at_least` **and** that age's `questions[]` is non-empty.
   Ages 42–48 have an empty list and a `null` threshold: never show it there. Thresholds by age:

   | Age | 0–3 | 4–9 | 10 | 11 | 12 | 13 | 14–15 | 16–17 | 18 | 19 | 20–21 | 22 | 23 | 24–25 | 26–29 | 30–32 | 33–36 | 37 | 38–41 |
   |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
   | Yes needed | 37 | 36 | 35 | 36 | 35 | 34 | 35 | 34 | 33 | 32 | 33 | 32 | 33 | 32 | 31 | 32 | 31 | 29 | 28 |

   (The file is authoritative; this table is for reading.)
4. The extra screen shows the age's 8 questions in file order (`position` 1–8), same two buttons, all must be answered.
   Header copy: eyebrow `GOING FURTHER`, title `More detail by area`, intro sentence
   `Your baby passed everything we asked. These run a bit ahead of their age, to see just how far along they are.`,
   counter `0/8`, button `See {name}'s results →` (`See your baby's results →` when no name).
5. The 8 questions depend on the age only, not on which base answers were Yes (verified for all 42 ages).
6. No Back from the extra screen into the base screens (matches the source). One extra screen only, never a second.
7. Store these answers with `role = "extension"` and `screen = 5`, `screen_area = "Going further"`.

## 6. Locales

`text_es` and `text_pt` in `questions.json` are the source quiz's own translations, kept for reference. Our rule for new locales is
English placeholders for human translators; do not ship those texts as ours.

## 7. What to write to MySQL

One row per **session**:

| Column | Value |
|---|---|
| session_id | uuid, created when the quiz starts |
| name | as typed, may be empty |
| birthdate | YYYY-MM-DD |
| gestational_weeks | 24–36, or NULL when the box was unticked |
| chronological_months | section 2 step 1 |
| effective_months | section 2 step 3 |
| corrected | true/false |
| locale | the UI language shown |
| landing_url, utm_* | whatever the landing captured |
| bank_version | the `generated` value from the JSON files (`2026-11-10`) |
| extension_shown | true/false |
| started_at, completed_at | timestamps |

One row per **answer** (insert as soon as the screen is submitted, so partial sessions keep their answers):

| Column | Value |
|---|---|
| session_id | |
| question_id | from the batch file |
| position | from the batch file (1–39 base; 1–8 for extension) |
| screen | 1–4, or 5 for extension |
| screen_area | Physical / Cognitive / Language / Social-Emotional / Going further |
| question_area | the question's own area (can differ from screen_area) |
| skill | from the batch file |
| role | anchor / item / calibration / extension |
| rate_at_age | from the batch file, never displayed |
| y | 1 = Yes, 0 = Not yet |
| answered_at | timestamp of the last change |

Overwrite on re-answer (unique key `session_id + question_id`). `rate_at_age` and `bank_version` are what make old sessions
scorable later if the bank changes; do not drop them.

## 8. Ignore

- The 35 questions whose only role is `report_only` in `questions.json`. They are never shown in the quiz.
- `rate_by_age` in `questions.json` is reference data for the report work; the quiz only needs `rate_at_age` from the batch file.

## 9. Self-check before declaring done

Run these against the built quiz (a script that walks every age is enough):

- For every effective age 0–48, the generated slide list equals `batches[age].questions` in position order. 49 ages, 1,837 base slots.
- Age 12: 39 questions, four screens of 10/10/10/9 rows, first question id 135 ("Lets go of things they're holding on purpose."),
  last id 85; extension threshold 35; the extension screen's first question id is 558 ("Inserts things like string into a small hole.").
- Age 0: 39 questions, first id 285; extension at 37 Yes, first extension id 680.
- Age 48: 22 questions, no calibration, no anchors, no extension at any Yes count.
- Age 45: exactly one anchor (Social-Emotional screen).
- Calibration rows sit on screens 1–3 only, never on screen 4, for ages 0–36.
- Prematurity: DOB giving chronological 6 months with 28 weeks → effective 3 (corrected true); with 37 weeks → 6 (corrected false);
  chronological 24 with 28 weeks → 24 (corrected false); chronological 1 with 30 weeks → 0 (corrected true).
- 49 months → too-old screen, no questions, no session answers.
- Month-end: DOB 2026-01-31 is 0 months on 2026-02-27, 1 month on 2026-02-28, 2 months on 2026-03-31, 3 months on 2026-04-30.
- Submitting the fourth screen with 35 Yes at age 12 shows the extra screen; with 34 Yes it does not.

Note on content: the question texts are the source quiz's own wording, kept as is for now while everything is being built and tested.
