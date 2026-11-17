# Kinedu "AQ assessment" quiz — teardown

Target: `https://webpromo.kinedu.com/aq-assessment` (Next.js app, Vercel). Investigated 2026-11-02.
Funnel under study first: `?ui=classic&paywall=trial3&offer=p79-t7&capture=0&...` (the "classic" variant).
Scope: landing → questions → first report. Paywall/checkout is out of scope for now.

## One-paragraph answer

The quiz is **not** a single hard-coded tree with a fake report. It is one shared bank of **408 yes/no
milestone questions**, served by the Kinedu API. The server picks **22–39 questions by the baby's age in
months** (0–48, corrected for prematurity under 24 months). Each age has its own list; neighbouring ages
share about half their questions, so there are effectively **49 overlapping question sets**, not one tree
and not a few age buckets. No question depends on an earlier answer **inside** the initial list. After the
last base question the server may return an **extension round** (8 harder questions) depending on the
answers given, so the full path is answer-dependent at exactly one point. The report numbers
(developmental age, band, per-area months) come from the API, not the browser. The server calculation
is **real but crude**: it is a yes-count lookup against age norms, deterministic, with visible defects at
low scores. Details below and in [SCORING.md](SCORING.md).

## The two landing pages are one app

Both URLs serve byte-identical HTML. The URL parameter `ui` (alias `v`) picks the React component:

| `ui=` | What the user sees | Report |
|---|---|---|
| absent / `assessment` (the bare URL) | hero → 3 primer screens → birthdate → one question per screen | "portrait", English only, 4 area values hidden |
| `list` | same but all questions of an area on one card | same |
| `skills` | same flow, report adds skill cards, chart, editable milestones | same + skills |
| `classic` (**our funnel**) | hero → 1 primer → birthdate → area lists with Back, en/es/pt | strongest area shown, other 3 blurred ("88") behind paywall |
| `classic-steps` | classic, one question per screen | identical to classic |
| `hook` (`h=1..3`) | marketing hero question first → why → quiz | identical to classic |

Other parameters: `capture=0` skips the email screen in every variant; `paywall`/`offer` only choose the
checkout page after the report; `lang=es|pt` translates (client-side); `test_id`, `vid`, `placement`,
`utm_*` only go to `/api/track`. None of these are sent to `/api/assessment`, so **they cannot change the
questions**. Email is never required to see the report when `capture=0`, so no email was entered.

## How the question flow works (observed)

1. Browser POSTs `{"action":"start","birthdate":"YYYY-MM-DD","gestationalWeeks":null|24..36}`.
2. Server replies with `ageMonths`, `corrected`, 4 `sections` (Physical, Cognitive, Language,
   Social-Emotional; each with optional `anchor` + `items`) and up to 3 `calibration` items.
   Each item: `id, area, skill, title, rate` (rate = share of babies that age who already do it, 0–0.98).
3. Client flattens: per section anchor → items → one calibration item. Order fixed. Answers are `y: 0|1`.
   **No client-side skip/branch logic exists** (checked every path in the bundle).
4. After the last question the client POSTs `{"action":"result","ageMonths":N,"extended":false,"answers":[{id,y},...]}`.
   Server answers either `stage:"extension"` with 8 more items, or `stage:"complete"` with the report.
5. Extension answered → same call with `extended:true` → `stage:"complete"`.
6. Report = `basic` (state, band, devAge, capped, tier, areasLocked, teaserArea) + `detail.areas[]`
   (months per area) + `skills[]` (curves) + `activity` / `floorActivities`.

Ages ≥ 49 months get HTTP 422 `age_range` and a "too old" screen that goes straight to the paywall.

## Age → question set

- 49 lists, one per returned age 0–48. 39 questions for ages 0–36, 36 for 37–44, then 33/27/24/22.
- Adjacent ages share 16–35 IDs (sliding window). Age 12 vs 24 share 1.
- Prematurity: gestational weeks 24–36 subtract 1–4 whole months from age (only while chronological age < 24).
  Same effective age → identical list. There is no separate preterm bank.
- All-yes answers trigger the extension round at ages 0–41 (never at 42–48). All-no completes as `below_floor`.

Full tables: [age-map.md](age-map.md) (ordered IDs per age, raw file links), [questions.csv](questions.csv)
(all 408 questions with text, area, skill, rate, ages at which each appears), [ENUMERATION.md](ENUMERATION.md).

## Is the report real? (Phase 3, 348 controlled API calls)

**Verdict: partly real.** The numbers are computed from the answers, not random or fixed, but the model is
simple and has defects. Evidence:

- **Deterministic.** Same answers → byte-identical response. Answer order does not matter.
- **Only the yes-count matters for the headline.** For a fixed question set, the developmental age depends
  only on how many answers are "yes", not which ones. Flipping answers in ascending-rate order and in
  descending-rate order gives the same devAge at every count (40/40). Which answers are yes only changes
  the per-area months and the skills list.
- **Norm lookup.** Answering exactly `round(sum of rates)` questions yes gives devAge = chronological age and
  band `on_pace` at ages 3, 12, 24, 36 (4/4). So the server compares the yes-count with the expected count
  for each age and picks the closest age. Age-12 lookup: 0–16 yes → below floor; 17–20 → 11 mo;
  21–24 → 12; 25–27 → 13; 28–29 → 14; 30 → 15; 31 → 16; 32 → 17; 33 → 19; 34 → 21; 35+ → 33 capped.
- **Band is a fixed ratio** `r = devAge / ageMonths`: `> 1.15` well_ahead, `> 1.05` little_ahead,
  `≥ 0.95` on_pace, else building. Exact on 227/227 reports. Below about 85% → `below_floor` (no number shown).
- **Extension round** = the server noticed saturation of the answered set (for the full age-12 list that
  is any 35 of 39 yes; other sets saturate at other counts) and serves 8 harder unseen items, max 2 per area. The client allows one round; the API allows chains of up
  to 7 rounds (age 3). `extended:true` is just a "stop asking" switch sent by the client.
- **Defects.** Age 1 with all 39 answers "no" returns `on_pace`, devAge 1 (age 0 and 2 correctly return
  below floor). Per-area months are non-monotonic at low counts (Cognitive 1→2→3→4 yes gives 8→2→0→12 months).
  Unasked milestones are counted as "typical" in skill percentages.
- **No session binding.** The API accepts any known question ID at any age, unknown IDs are ignored,
  as few as 8 answers produce a report. Scoring is a per-ID bank lookup, not tied to the served list.
- **Paywall gating is client-side only.** The free response already contains all four area values, the
  skills curves and the recommended activity. The locked tiles show the literal string "88" blurred.

## Live confirmation in Chrome (Phase 4, classic funnel, 12-month-old)

Two real runs on the ad URL, mobile viewport 390×844, screenshots `screenshots/01…15`, every request body
saved in `raw/api/browser/`. Everything predicted by Phases 1–3 held:

- Flow: hero → primer → name + birthdate (calendar, "Born before 37 weeks?" box) → 4 area lists with
  Back → celebrate → report. No email screen (`capture=0`). Questions, order and rates identical to
  `questions-by-age.md` age 12.
- Run A (28 yes of 39) → report "At 12 months, showing the skills of a typical 14-month-old", band
  well_ahead. The server response was byte-identical to the Phase 3 probe with the same answers.
- Run B (all yes) → extra screen "Going further · More detail by area", exactly the 8 predicted
  extension items, then "42+ months" capped report.
- Report shows one area with a real number (Cognitive 16) while the teaser text calls Physical
  (14) the strongest: the two come from different API fields and disagree. The other three tiles are
  blurred literal "88". All four real values were in the response.
- Unlock CTA → `https://webpromo.kinedu.com/aq-paywall-trial3/index.html?...&from=assessment`
  (all URL params preserved, adds `from=assessment`). Paywall: "Try for $0", $79.99/year after a 7-day
  trial, Stripe checkout dialog loads immediately. Not clicked further.
- Trackers: Meta Pixel `2089634224620932` (PageView, ViewContent `assessment-classic`,
  InitiateCheckout on the unlock click), Microsoft Clarity `x8ou6ay6eb`, first-party `/api/track`
  events per screen. No GTM, GA, or TikTok. Full inventory in `BROWSER-WALKTHROUGH.md`.

## The second landing page, live (Phase 7, bare URL, Amsterdam exit)

One run of `https://webpromo.kinedu.com/aq-assessment` (no parameters) with the same 12-month-old and the same 28-yes
answers; screenshots in `screenshots/funnel2/`, report in `BROWSER-WALKTHROUGH-FUNNEL2.md`. Same app, same questions,
same API, same score (the result response is byte-identical to the classic run). What differs is the wrapper:

| | classic (`ui=classic&capture=0`) | bare URL ("assessment") |
|---|---|---|
| Hero | sample report + reassurance + credentials | sparse: eyebrow "KINEDU ASSESSMENT", short pitch, "Start →" |
| Primer | 1 screen | 3 screens ("How to answer", "You'll see things they can't do yet", "Chosen for their exact age") |
| Birthdate | custom calendar | native date input |
| Questions | 4 area lists, Back button | 39 single-question screens, auto-advance, no Back |
| Email | skipped by `capture=0` | required: "Where should we save your baby's portrait?", posts `/api/lead` (email + session, no answers); no reading email is ever sent |
| Report | one real area number, three blurred "88", one milestone | headline only (band sentence + "typical 14-month-old"); all four area tiles blurred "●● months"; no milestones, no activities |
| Unlock → | `/aq-paywall-trial3/…` with all ad params + `from=assessment` | `/aq-paywall-trial3/index.html?from=assessment`; the paywall page itself then adds `offer=p79-t7` |
| Tracking | Meta ViewContent + InitiateCheckout, `variant:classic` | Meta Lead on email, no ViewContent, `variant:assessment`, no UTMs |

So the bare URL does give a report, just a thinner one, and only after an email.

## Is it a live split test? (2026-11-03)

No randomisation on the site; the wrapper is chosen by the link. `webpromo.kinedu.com/p/assessment-landing` is Kinedu's
entry redirector: it mints a `vid` and 302s to the classic URL with `placement=assessment-landing&utm_medium=partner&ui=classic&capture=0`
(same set in a Wayback copy from 2026-08-30). `/p/landing-kinedu` redirects to a different product, `aq-quiz-storytelling-short`.
Meta Ad Library (logged out, top 29 of ~460 active ads worldwide and of ~100 US, by impressions): all app-store links, none to the quiz;
ad-text searches for assessment/quiz wording found nothing. Saved pages: `raw/js/p_p_assessment-landing.html`, `raw/js/p_p_landing-kinedu.html`,
screenshots `screenshots/adlibrary-*.png`.

## What is cosmetic in the UI (from the code)

- Classic locked area numbers are the literal string "88" under CSS blur; the bare-URL portrait
  uses "●● months" for all four areas. Neither conceals the real API value inside the tile.
- The green "usual range" bar is fixed geometry; only the dot position uses API devAge/age.
- The sample report on the landing (6-month example, 90/78/50/78 dots) is hard-coded and labelled as example.
- No `Math.random` in scoring; randomness is only for session/event IDs. No count-up animations.

## Files

| File | What |
|---|---|
| `STATIC-ANALYSIS.md` | Phase 1: every URL param, state machine per variant (Mermaid), every API call, report rendering, hard-coded strings, all 408 question translations |
| **`questions-by-age.md`** | **Start here**: every question a baby of each age (0–48 months) is asked, in on-screen order, with text and rate |
| `ENUMERATION.md`, `age-map.md`, `questions.csv` | Phase 2: question bank from the API, age mapping, correction formula |
| `SCORING.md` | Phase 3: is the report real? formula fit, extension rules, validation, anomaly |
| `SCORING-TABLE.md`, `scoring-table.csv` | Phase 5: full Yes-count → headline result for every age 0–48 (1,886 calls) |
| `EXTENSION.md` | extension trigger = capped-from K, verified at all ages 0–41 (84 calls) |
| `EXTENSION-TABLE.md`, `extension-table.csv` | Phase 8: post-extension scoring grid, every age 0–41 × base K × extension K (2,502 calls via proxy); total Yes count is sufficient |
| **`quiz-spec/`** | **Build hand-off**: `QUIZ-QUESTION-SPEC.md` + `questions.json`, `batches-by-age.json`, `extension-by-age.json`, `batches-by-age.csv`. Self-contained; copy into the quiz project. |
| `raw/css/` | the site's stylesheet + font links (for the rebuild's look) |
| `CDC-COMPARISON.md`, `raw/cdc/` | Phase 9: Kinedu shares vs CDC 2022 milestone ages (75% floor): 20 comparable pairs, median 0.68, lenient not inflated |
| `AREA-TABLE.md`, `area-table.csv` | Phase 6: per-area Yes-count → area months for every age (via proxy) |
| `BROWSER-WALKTHROUGH.md`, `screenshots/` | Phase 4: classic funnel walked once in Chrome, network calls confirmed |
| `BROWSER-WALKTHROUGH-FUNNEL2.md`, `screenshots/funnel2/` | Phase 7: bare-URL funnel walked once (via VPN), compared state by state with classic |
| [BROWSER-WALKTHROUGH-FUNNEL2.md](BROWSER-WALKTHROUGH-FUNNEL2.md), `screenshots/funnel2/` | Phase 7: bare-URL assessment, email gate, four concealed area values, classic comparison; exact API bodies in `raw/api/browser2/`, audit in `raw/browser2/` |
| `raw/js/` | served HTML + bundles (+ `beautified/`) |
| `raw/api/` | one JSON (+ headers) per API call, `requests.jsonl` manifest; `scoring/` for Phase 3 |
| `scripts/` | reproducible collectors (`enumerate_api.py`, `probe_api.py`, `probe_scoring.py`, `build_enumeration.py`, `build_questions_by_age.py`) |
| `logs/` | Codex briefs and run logs per phase |

Status: Phase 1 ✅ · Phase 2 ✅ · Phase 3 ✅ · Phase 4 ✅ · Phase 5 ✅ · Phase 6 ✅ · Phase 7 ✅ ([classic walkthrough](BROWSER-WALKTHROUGH.md), 2026-11-02; [bare-URL walkthrough](BROWSER-WALKTHROUGH-FUNNEL2.md), 2026-11-03).
