# Browser walkthrough — classic AQ assessment

Observed in the connected consumer Chrome on the user's Mac on **2026-11-02**, approximately **16:44–16:51 UTC**. Browser user agent: Chrome/156.0.0.0 on macOS. This records two completed browser runs, with real requests and normal UI clicks. No direct API probes or synthetic tracking events were sent during this phase.

**Result:** both Phase 3 predictions were confirmed. Run A returned complete / 14 months / well_ahead / P14 C16 L12 S16. Run B returned an eight-item extension, then complete / 42 months / capped. Both final response bodies are **byte-identical** to the corresponding Phase 3 files. The UI also confirms the cosmetic 88 locks and the previously inferred disagreement between the highlighted strongest area and the teaser sentence.

## Scope and evidence

The exact landing URL used for both runs was:

```text
https://webpromo.kinedu.com/aq-assessment?vid=c1991816-d75d-4e46-a05d-cc40924c2ea8&paywall=trial3&offer=p79-t7&newusers=1&placement=assessment-landing&utm_source=assessment-landing&utm_medium=partner&ui=classic&capture=0
```

README.md, STATIC-ANALYSIS.md `2 classic state machine and `3 API inventory, and SCORING.md's age-12 lookup were read before the walkthrough.

- Run A used birthdate **2025-11-02**, no name, full term, and Yes iff the **live served** rate was ≥ 0.5: **28 Yes / 11 Not yet**.
- Run B used a **new tab** created with `new_page`, the same exact URL and birthdate, no name, full term, and **47 Yes** across 39 base plus eight extension items. It shared the normal browser's cookies/localStorage; “fresh” means a fresh app instance, not an isolated identity.
- No email screen appeared in either run. No email was entered; there were **zero /api/lead and zero /api/send-reading calls**.
- One locked area tile was clicked, once, in Run A. The paywall's first screen was captured, followed by browser Back. No button on that destination was clicked. Run B stopped at its report.
- State transitions stayed on the landing URL until the one paywall navigation. State names below map the observed screens to the names in the saved state machine; they are not claims of having inspected React's private state.

**Viewport and capture details.** `resize_page(390,844)` was called first, but Chrome reported `innerWidth:500`. Applying `emulate(viewport:"390x844x1,mobile,touch")` gave an actual **390×844** CSS viewport. That initial change reloaded the app, after one preliminary hero click but before any birthdate/answers were sent. The preliminary `funnel_started` / `quiz_answer:hero` requests are recorded separately as A-16 / A-28. Completed Run A starts at document A-30 and mount A-45. Changing only the override width to 1280 and back preserved the hero; **02** is the single **1280-wide desktop-layout hero** screenshot, with mobile/touch flags retained and the ordinary desktop Chrome user agent unchanged.

Every screenshot was taken by `take_screenshot` with an absolute `filePath`. The MCP file writer rejected this project's path as outside its configured roots, so it wrote to `/tmp/kinedu-browser/screenshots/NN-state.png` and the bytes were moved unchanged into `screenshots/`. All are full-page captures except the first paywall viewport. Thus heights may exceed 844; widths are exactly 390, except desktop hero 1280. Chrome's full-page report captures retain the fixed unlock bar, which covers some intervening text in the resulting image. The saved snapshots and DOM reads supply that text without hiding or restyling the page.

Evidence:

- [Run A network list before handoff](raw/browser/A-network-prepaywall.txt), [Run A through paywall and Back](raw/browser/A-network-final.txt), [Run B through report](raw/browser/B-network-final.txt).
- [All indexed requests](raw/browser/network-inventory.json): 86 requests in A's final preserved window and 59 in B, plus the two separately indexed setup tracking calls.
- [Full track request bodies](raw/browser/track-events.json), [all third-party tracker request parameters](raw/browser/tracker-inventory.json), [decoded Facebook query parameters](raw/browser/facebook-events.json).
- [Run A report DOM](raw/browser/A-portrait.dom.json), [Run B report DOM](raw/browser/B-portrait.dom.json), and per-state `*.snapshot.txt` in [raw/browser/](raw/browser/).
- [Offline comparisons, hashes and image sizes](raw/browser/verification.json). Rebuild indexes without network traffic with `python3 scripts/build_browser_evidence.py`.

The network cutoffs are **A-115** (return from paywall) and **B-59** (report). Subsequent background recording is outside those completed-run windows. Request IDs are **tab-local**: A-45 and B-45 are different requests. The preserved pre-handoff list also retains setup requests A-1–29; they are not a third completed assessment.

## Run A: state → screenshot → copy → calls

First-party call IDs are shown below. Clarity recording continued between screens; its complete inventory is later in this document.

| State from `2 | Screenshot | Key on-screen copy | API calls / events fired |
| --- | --- | --- | --- |
| `hero`, mobile | [01-hero.png](screenshots/01-hero.png) | “See what your baby is building right now”; “Start FREE assessment →” | Entry A-45 `funnel_started / assessment`; Start A-60 `quiz_answer / hero` |
| `hero`, 1280 wide | [02-hero-desktop.png](screenshots/02-hero-desktop.png) | Same copy and example reading | No additional first-party call from width-only changes |
| `primer` | [03-primer.png](screenshots/03-primer.png) | “Before we start”; “30 seconds that make the measurement better” | No first-party request on primer Continue |
| `child` | [04-child.png](screenshots/04-child.png) | “Tell us about your baby”; optional name; calendar; “Born before 37 weeks?” | Submit A-64 `assessment:start`, then A-65 `quiz_started / child` |
| `child`, prematurity expanded for inspection | [05-child-prematurity.png](screenshots/05-child-prematurity.png) | “Weeks of gestation: 34”; corrected age until age 2 | No first-party request from toggle. Restored unchecked before Submit |
| `area`, Physical | [06-area-physical.png](screenshots/06-area-physical.png) | “AREA 1 OF 4”; “Chosen for your baby at 12 months”; 0/10 → 10/10 | Next A-68 `quiz_answer / area_Physical`; no per-question API calls |
| `area`, Cognitive | [07-area-cognitive.png](screenshots/07-area-cognitive.png) | “AREA 2 OF 4”; 0/10 → 10/10; “‹ Back” | Next A-71 `quiz_answer / area_Cognitive` |
| `area`, Language | [08-area-language.png](screenshots/08-area-language.png) | “AREA 3 OF 4”; 0/10 → 10/10 | Next A-74 `quiz_answer / area_Language` |
| `area`, Social-Emotional | [09-area-social-emotional.png](screenshots/09-area-social-emotional.png) | “AREA 4 OF 4”; 0/9 → 9/9; “See your baby’s reading →” | A-77 `quiz_answer / area_Social-Emotional`; A-78 `assessment:result, extended:false`; A-79 `funnel_completed / celebrate` |
| `celebrate` | [10-celebrate.png](screenshots/10-celebrate.png) | “All done!”; “39 answers”; “4 areas” | Final result already received; Continue skips email with `capture=0` |
| `portrait` | [11-portrait.png](screenshots/11-portrait.png) | Typical 14-month-old at 12 months; Cognitive around 16 months; three locks | Entry A-84 `quiz_answer / portrait_shown` and Facebook A-85 `ViewContent`; no new assessment request |
| external `paywall`, not a React state | [12-paywall-first-screen.png](screenshots/12-paywall-first-screen.png) | “Know EXACTLY what to do with your baby every day”; “Try for $0” | Locked Physical tile A-87 `quiz_answer / paywall_handoff`; navigation A-88; Facebook A-89 `InitiateCheckout`. Destination requests detailed below; then Back |

The answer counters count **answered rows**, not Yes answers. The four displayed lists contain 10, 10, 10 and 9 rows. By actual API area, calibration changes that distribution to P9 C9 L10 S11. No Back button was clicked during the assessment.

## Exact copy before the questions

**Hero** — logo alt text “Kinedu”; heading “See what your baby is building right now”; paragraph “Answer about what they do today and see which skills are opening up — compared to what’s typical at their exact age.”; button “Start FREE assessment →”; “⏱ 5–10 minutes”; “📄 Free reading included”.

The example card reads “YOU’LL GET A READING LIKE THIS”; “At 6 months, showing the skills of a typical 7-month-old.”; “→ faster”; “The green zone is what we usually see at this age.” Its labels and numbers are **Physical — around 8 months; Cognitive — around 7 months; Language — around 6 months; Social-Emot. — around 7 months**. Below it: “Example — not a real child’s result.”

The remaining hero copy is: “🌱 About half the answers will be “Not yet” — and that’s fine. We ask right at the edge of what your baby is building: that’s what real measurement looks like.” The credentials paragraph reads “Created and psychometrically evaluated by Kinedu with 2,135 caregivers. Michael C. Frank, of Stanford, advised on the early review of the 0–24 month milestones.” Footer: “Development surveillance, not diagnosis.” These are recorded marketing statements, not independently verified claims. See [hero snapshot from the repeated Run B screen](raw/browser/B-hero.snapshot.txt); Run A's inline `take_snapshot` showed the same copy.

**Primer** — “Before we start”; “30 seconds that make the measurement better”; three blocks:

1. 🎯 “Questions picked for their exact age” — “A 5-month-old and a 7-month-old don’t see the same list.”
2. ✅ “There are only two answers” — `Yes — they do it consistently, not just once.` / `Not yet — they don't do it yet, or you're not sure. When in doubt, "Not yet".` / `A "Not yet" is just as useful as a "Yes". Both tell us where they are.`
3. 🌱 “About half will be “Not yet” — and that’s fine” — `Expect to answer "Not yet" about half the time. That is normal, and it is what makes the reading precise.`

Button “Start the questions →”; footer “Development surveillance, not diagnosis.” [Exact snapshot](raw/browser/A-primer.snapshot.txt).

**Child** — “Tell us about your baby”; “Name (optional)”; empty textbox; “Date of birth”; Month and Year selectors; prev/next calendar arrows; weekday initials S M T W T F S; day buttons. Initial calendar: November 2026, with future dates disabled. Year changed to 2025, November retained, day 2 selected. “Born before 37 weeks?” is initially unchecked.

For the requested slider evidence it was briefly checked: “Weeks of gestation: 34”, slider **24–36**, default **34**, and “We’ll use their corrected age, as the American Academy of Pediatrics recommends, until age 2 — and we’ll say so.” It was restored to unchecked before submitting. The CTA is “See your baby’s questions →”, disabled until a day is selected, briefly “Preparing…” during the request. Footer: “Development surveillance, not diagnosis.” [Default snapshot](raw/browser/A-child.snapshot.txt), [expanded snapshot](raw/browser/A-child-prematurity.snapshot.txt).

The actual start body, A-64, is:

```json
{"action":"start","birthdate":"2025-11-02","gestationalWeeks":null}
```

The [exact response](raw/api/browser/A-start.response.json) returns `ageMonths:12` and `corrected:false`. It is semantically identical to Phase 2's [returned-age-12 response](raw/api/start_age13_gw-null.json); that older filename's age13 is the probe's input-age label, not this response's returned age.

## Exact question order and comparison to age 12

**39/39 IDs, rates, titles and order match [questions-by-age.md, 12 months](questions-by-age.md#12-months--39-questions-rawapistart_age13_gw-nulljson)**. All titles also match the saved live area snapshots in order, with no text differences. Rates and IDs below come from A-64's response, not from the labels on the screen; the UI does not display them. Every row shows buttons “Not yet” and “Yes”.

Physical, Cognitive and Language each append the corresponding calibration item. The first two calibration items belong to Social-Emotional in the API even though shown on other area screens. Run B received a byte-identical start response and used the same ordered base list.

### Physical

| Order | ID | Rate | Run A answer | Exact on-screen question |
| --- | --- | --- | --- | --- |
| 1 | 135 | 0.98 | Yes | Lets go of things they're holding on purpose. |
| 2 | 470 | 0.5 | Yes | Can stand up from a squat all alone. |
| 3 | 309 | 0.51 | Yes | Can walk while holding a small toy. |
| 4 | 4 | 0.52 | Yes | Squats to pick things up while walking. |
| 5 | 471 | 0.52 | Yes | Descends stairs with an adult, switching feet. |
| 6 | 355 | 0.47 | Not yet | Pushes or pulls toys while walking. |
| 7 | 330 | 0.54 | Yes | Scribbles by moving their entire arm from the shoulder. |
| 8 | 538 | 0.54 | Yes | Walks up ramps. |
| 9 | 415 | 0.46 | Not yet | Takes unsteady and short steps alone. |
| 10 | 686 (calibration; API area Social-Emotional) | 0.22 | Not yet | Drinks from a cup with one hand. |

### Cognitive

| Order | ID | Rate | Run A answer | Exact on-screen question |
| --- | --- | --- | --- | --- |
| 1 | 183 | 0.97 | Yes | Looks for an item they dropped on the floor. |
| 2 | 5 | 0.51 | Yes | Imitates what friends do in play, such as building towers when they do. |
| 3 | 335 | 0.52 | Yes | Moves a body part when asked to. |
| 4 | 406 | 0.6 | Yes | Copies how adults use things (like pretending to talk on the phone after seeing mom do it). |
| 5 | 472 | 0.6 | Yes | Finds their way in familiar places, such as their parent's room. |
| 6 | 338 | 0.64 | Yes | Claps or taps an instrument to the rhythm of a song. |
| 7 | 436 | 0.35 | Not yet | Pays attention to an adult reading a book for a few minutes. |
| 8 | 19 | 0.65 | Yes | Follows simple, one-step instructions (like 'Pick up the toy'). |
| 9 | 53 | 0.32 | Not yet | Copies what caregivers do, like taking a toy phone from a purse and saying 'hello.' |
| 10 | 611 (calibration; API area Social-Emotional) | 0.02 | Not yet | Puts on a shirt without buttons. |

### Language

| Order | ID | Rate | Run A answer | Exact on-screen question |
| --- | --- | --- | --- | --- |
| 1 | 31 | 0.89 | Yes | Repeats 'baba' or 'dada' kind of sounds. |
| 2 | 368 | 0.57 | Yes | Answers simple questions with signs, actions, or words. |
| 3 | 279 | 0.42 | Not yet | Points to things they know when you say their name. |
| 4 | 360 | 0.39 | Not yet | Points to caregivers, like 'Mom' or 'Dad'. |
| 5 | 54 | 0.68 | Yes | Imitates a sound like 'pa' after you say it. |
| 6 | 126 | 0.69 | Yes | Talks to other babies with babbles. |
| 7 | 7 | 0.72 | Yes | Tries to copy the words you say. |
| 8 | 109 | 0.72 | Yes | Understands three-word phrases, like 'Look, a dog!' |
| 9 | 32 | 0.27 | Not yet | Names at least three objects correctly. |
| 10 | 688 (calibration; API area Language) | 0.37 | Not yet | Says simple words with the letter N, like 'nap' or 'banana'. |

### Social-Emotional

| Order | ID | Rate | Run A answer | Exact on-screen question |
| --- | --- | --- | --- | --- |
| 1 | 349 | 0.97 | Yes | Enjoys playing on their own. |
| 2 | 565 | 0.55 | Yes | Uses personal care tools like a hairbrush and toothbrush correctly. |
| 3 | 476 | 0.6 | Yes | Can feed independently, with or without utensils. |
| 4 | 103 | 0.71 | Yes | Can correctly use some everyday items (like sipping from a cup or dialing a phone). |
| 5 | 340 | 0.74 | Yes | Shows you things by pointing. |
| 6 | 441 | 0.24 | Not yet | Knows which things belong to family members, like Mom's purse or Dad's wallet. |
| 7 | 454 | 0.77 | Yes | Plays and has fun with other kids. |
| 8 | 308 | 0.82 | Yes | Expresses love to those familiar, like hugging them. |
| 9 | 85 | 0.85 | Yes | Helps with the dressing and undressing processes by moving the right body parts. |

For every area, the common copy is “Assessment”, “AREA N OF 4”, the area heading, “Chosen for your baby at 12 months”, and “Development surveillance, not diagnosis.” The first three forward CTAs are “Next: Cognitive ›”, “Next: Language ›” and “Next: Social-Emotional ›”; the last is “See your baby’s reading →”. “‹ Back” appears from area 2 onward. Next is disabled until all rows on the current card are answered. Buttons and counters updated locally; **no request per individual answer** was observed.

## Celebrate and report: every label, number and blur

**Celebrate** — Kinedu logo; 🎉; “All done!”; “We compared what you told us about your baby against what’s typical at their exact age. Their reading is ready.”; “✅ 39 answers”; “4 areas”; button “See your baby’s reading →”. No email intervened. [Snapshot](raw/browser/A-celebrate.snapshot.txt).

**Run A report, unblurred copy** (the full page, including content requiring scroll):

- 🎉 “The reading is ready!”
- “TODAY'S PICTURE”
- “At 12 months, Your baby is showing the skills of a typical 14-month-old.”
- “✦ A lot is already in place, and new skills keep opening up.”
- “→ faster”
- “The green zone is what we usually see at 12 months. The dot is their reading.”
- “✓ This reading is already complete — unlocking adds depth by area, it doesn’t change the number.”
- “BY AREA”
- Physical: lock icon, label “Physical”, “Tap to unlock”.
- Cognitive: label “Cognitive”, **“around 16 months”**, green mini-bar and dot.
- Language: lock icon, label “Language”, “Tap to unlock”.
- Social-Emotional: lock icon, abbreviated label **“Social-Emot.”**, “Tap to unlock”.
- “✨ Physical looks like their strongest area — unlock the full profile to see all four.”
- “WHAT’S OPENING UP FOR YOUR BABY RIGHT NOW”
- **“Stops a rolling ball with hands or body.”**, plus two locked rows.
- **“+3 more in the full profile”**
- “Every child develops at their own pace. This helps you understand their unique journey — not compare them to others.”
- “Development surveillance, not diagnosis.”
- Fixed CTA **“Unlock your baby’s full profile + daily activities →”**
- **“7 days free · no commitment”**
- “Their answers are already saved — it opens instantly.”

There is no printed percentile, numeric AQ, ratio or diagnosis. The positive band is a sentence; the literal code `well_ahead` is not printed.

**Every element with a CSS blur**, from [the DOM read](raw/browser/A-portrait.dom.json):

| Element | Literal DOM text | Computed filter | What is actually concealed |
| --- | --- | --- | --- |
| Physical number | `around 88` | `blur(6px)` | Placeholder, not API Physical 14 |
| Physical mini-bar | empty text; green zone left 38%, width 24% | `blur(3px)` | Decorative geometry, not a hidden score |
| Language number | `around 88` | `blur(6px)` | Placeholder, not API Language 12 |
| Language mini-bar | same fixed geometry | `blur(3px)` | Decorative geometry |
| Social-Emot. number | `around 88` | `blur(6px)` | Placeholder, not API Social-Emotional 16 |
| Social-Emot. mini-bar | same fixed geometry | `blur(3px)` | Decorative geometry |
| Locked milestone 1 | `Moves to the rhythm of music.` | `blur(5px)` | Real title present in the DOM |
| Locked milestone 2 | `Looks at things or people when called by name.` | `blur(5px)` | Real title present in the DOM |

The three number nodes and two title nodes have `aria-hidden="true"`. Therefore `take_snapshot` lists the lock buttons but omits those strings; `evaluate_script` reading `textContent`/`innerText` and computed styles proves their contents without removing blur. The numbers are literally **88**, not 14/12/16 behind a filter.

## What the user sees vs what the API returned

The **exact complete JSON**, including every skill, curve and item, is saved without reformatting in:

| Run | Request | Final result response | Size | Comparison |
| --- | --- | --- | --- | --- |
| A | [A-result.request.json](raw/api/browser/A-result.request.json) | [A-result.response.json](raw/api/browser/A-result.response.json) | 58,084 bytes | Byte-identical to [C_age12_rate_ge50.json](raw/api/scoring/C_age12_rate_ge50.json) |
| B | [B-result.request.json](raw/api/browser/B-result.request.json) | [B-result.response.json](raw/api/browser/B-result.response.json) | 63,263 bytes | Byte-identical to [E_age12_extension_all_one.json](raw/api/scoring/E_age12_extension_all_one.json) |

A's relevant exact response objects are:

```json
{
  "stage": "complete",
  "basic": {
    "state": "ok", "band": "well_ahead", "devAge": 14, "capped": false,
    "ageMonths": 12, "tier": "basic", "areasLocked": true, "teaserArea": "Physical"
  },
  "detail": {
    "state": "ok", "band": "well_ahead", "devAge": 14, "capped": false,
    "ageMonths": 12, "tier": "detail",
    "areas": [
      {"area":"Physical","state":"ok","months":14,"atLeast":false},
      {"area":"Cognitive","state":"ok","months":16,"atLeast":false},
      {"area":"Language","state":"ok","months":12,"atLeast":false},
      {"area":"Social-Emotional","state":"ok","months":16,"atLeast":false}
    ],
    "areasDefaultHidden": false
  }
}
```

| API value(s) | Free UI treatment |
| --- | --- |
| `ageMonths:12` and `devAge:14` | Both printed in the headline; chronological age repeated in the green-zone caption |
| `band:"well_ahead"` | Mapped to the positive sentence; code hidden |
| `capped:false` | No plus sign or cap explanation in A |
| `basic.teaserArea:"Physical"` | Printed as “Physical looks like their strongest area” |
| `detail.areas` Cognitive 16 and `atLeast:false` | Actual **around 16 months** shown; tied with Social-Emotional 16, Cognitive appears earlier |
| Physical 14, Language 12, Social-Emotional 16 | Already returned in full; visually replaced with blurred **88** |
| `areasLocked:true`, `tier`, `state`, `stage`, `areasDefaultHidden:false` | Raw values not printed; locks/layout reflect client presentation |
| `skills`, 27 records in A | One opening title visible, two real titles blurred; remaining records, item statuses, counts, `childPct` and all `curve[].age/pct/lo/hi` values hidden |
| `activity`: Language, `targetMonth:12`, English title `Hand me the toy`, Spanish/Portuguese titles | Not shown in this free report |
| `floorActivities` | Not returned in these successful numeric responses |

This is evidence of **client presentation gating**: the public result already supplies all four ages and skill detail. It does not prove what an unlock purchase would deliver; no purchase was made. The statement “Their answers are already saved — it opens instantly” is displayed copy. The observed handoff URL carries no birthdate, answer vector, report JSON or assessment ID, and destination telemetry reports `from_quiz:false` / `baby_age:null`. Those observations do not establish any unobserved server-side storage.

**Live inconsistency confirmed:** A's largest displayed area is Cognitive 16 (tied with Social-Emotional), while `basic.teaserArea` is Physical 14 and the teaser calls Physical strongest. This is exactly the separate-input mismatch anticipated as an inference in STATIC-ANALYSIS.md `5; it is now observed.

## Run B: extension and capped report

Run B's start body was identical to A's; [start response](raw/api/browser/B-start.response.json) was byte-identical. Every base row was answered Yes, then the fourth area's CTA sent B-46 with `action:"result"`, `ageMonths:12`, `extended:false` and an array of 39 `{id,y:1}` answers. [The exact request](raw/api/browser/B-base-result.request.json) contains the full array. The [exact response](raw/api/browser/B-base-result.response.json) is `stage:"extension"` with these eight items in this order:

| Order | ID | API area | Rate at age 12 | Exact question text |
| --- | --- | --- | --- | --- |
| 1 | 558 | Physical | 0.27 | Inserts things like string into a small hole. |
| 2 | 684 | Physical | 0.03 | Takes steps using heel-to-toe motion. |
| 3 | 651 | Cognitive | 0 | Mixes real and fantasy topics when talking. |
| 4 | 503 | Cognitive | 0.14 | Sorts things by their shape, like finding all the triangular blocks. |
| 5 | 695 | Language | 0.05 | Uses fingers to tell their age. |
| 6 | 566 | Language | 0.02 | Answers simple questions about a story. |
| 7 | 658 | Social-Emotional | 0.33 | Says their first and last name. |
| 8 | 612 | Social-Emotional | 0.04 | Puts their pants on. |

Exactly **two per area**, with no repeated base IDs. The IDs match SCORING.md `E's first age-12 extension. All eight live question texts match the response.

| State from `2 | Screenshot | Exact / changed copy | Calls |
| --- | --- | --- | --- |
| `hero → primer → child → area` | Same layouts as A's 01, 03, 04, 06–09; no redundant B screenshots | Same copy and base list; birthdate 2025-11-02, full term | B-16 mount, B-28 hero, B-31 start, B-32 quiz started, B-36/39/42/45 area completion |
| `extension` | [13-extension.png](screenshots/13-extension.png) | “Assessment”; “GOING FURTHER”; “More detail by area”; “Your baby passed everything we asked. These run a bit ahead of their age, to see just how far along they are.”; 0/8 → 8/8; Yes / Not yet; “See your baby’s reading →”; footer disclaimer; **no Back button** | Entry B-47 `extension_started / extension` after B-46; submit B-50 result with `extended:true`, all 47 answers; B-51 completion |
| `celebrate` | [14-celebrate-extension.png](screenshots/14-celebrate-extension.png) | Same celebrate copy, now **47 answers**, **4 areas** | `funnel_completed / celebrate` already fired; skips email again |
| `portrait` | [15-portrait-extension.png](screenshots/15-portrait-extension.png) | Typical **42+-month-old** at 12 months; Social-Emot. **at least 40 months** | B-57 `quiz_answer / portrait_shown`; Facebook B-58 `ViewContent`. Stopped here |

The final B response returns `stage:"complete"`, `basic.state:"ok"`, `band:"well_ahead"`, `devAge:42`, `capped:true`, `ageMonths:12`, `tier:"basic"`, `areasLocked:true`, `teaserArea:"Language"`. All four detail records are ok and `atLeast:true`: **P32+ C34+ L26+ S40+**.

Run B's report retains A's labels, positive sentence, completion sentence, CTA, “7 days free · no commitment”, saved-answers claim, footer, visible opening “Stops a rolling ball with hands or body.”, and “+3 more in the full profile”. The changed headline is exactly **“At 12 months, Your baby is showing the skills of a typical 42+-month-old.”** It adds:

> A “+” means they passed every question in that area: their level is above what these questions can reach, so the number is a floor, not a ceiling.

Social-Emot. is exposed as **“at least 40 months”**. Physical, Cognitive and Language each still have **“around 88”** with 6px blur and decorative 3px-blurred mini-bars. The 5px-blurred titles are **“Moves to the rhythm of music.”** and **“Says hello or goodbye with hand movements.”** The teaser is **“Language looks like their strongest area — unlock the full profile to see all four.”** This repeats the mismatch: exposed Social-Emotional 40 versus teaser Language 26. B's **30 skills** and recommended Language activity, targetMonth 26, English title **“The Letter T I”**, are already in the free response but not rendered as a daily activity. [Exact report snapshot](raw/browser/B-portrait.snapshot.txt).

Only one extension round was shown. Completion on `extended:true` matches the client behavior; this run does not independently test additional server-side extension chains.

## Network audit: every first-party assessment/lead/reading call

All five assessment calls were POSTs with `Content-Type:application/json`, returning HTTP **200**. They contained no marketing query fields or email. The observed browser automatically added ordinary request headers/cookies; that does not conflict with the source having no explicit Cookie header.

| Request | Action / payload | Response | Saved exact bodies |
| --- | --- | --- | --- |
| A-64 | start, birthdate 2025-11-02, gestationalWeeks null | ageMonths 12, corrected false, 4 sections + 3 calibration | [request](raw/api/browser/A-start.request.json), [response](raw/api/browser/A-start.response.json) |
| A-78 | result, ageMonths 12, extended false, 39 answers / 28 Yes | complete, devAge 14, uncapped, well_ahead | [request](raw/api/browser/A-result.request.json), [response](raw/api/browser/A-result.response.json) |
| B-31 | same start as A | same start response, byte-identical | [request](raw/api/browser/B-start.request.json), [response](raw/api/browser/B-start.response.json) |
| B-46 | result, ageMonths 12, extended false, 39 answers / 39 Yes | extension, 8 items | [request](raw/api/browser/B-base-result.request.json), [response](raw/api/browser/B-base-result.response.json) |
| B-50 | result, ageMonths 12, extended true, 47 answers / 47 Yes | complete, devAge 42, capped, well_ahead | [request](raw/api/browser/B-result.request.json), [response](raw/api/browser/B-result.response.json) |
| Both runs | /api/lead | **0 calls** | No email state or submission |
| Both runs | /api/send-reading | **0 calls** | No email attempt; no reading_email_sent event |
| Paywall only, A-100 | GET /api/localized-price?offer=p79-t7 | HTTP 200; body no longer available in DevTools | [metadata](raw/browser/A-100.network.txt); no response body fabricated |

### Every /api/track call

All **24** observed /api/track calls below returned **200**: ten for completed A's assessment/handoff, two from the destination, ten for B, and two setup-prelude calls. There was no per-answer track call.

| Tab-request ID | event_name | screen | Exact request body |
| --- | --- | --- | --- |
| A-16 (setup) | funnel_started | assessment | [body](raw/api/browser/A-16.request.json) |
| A-28 (setup) | quiz_answer | hero | [body](raw/api/browser/A-28.request.json) |
| A-45 | funnel_started | assessment | [body](raw/api/browser/A-45.request.json) |
| A-60 | quiz_answer | hero | [body](raw/api/browser/A-60.request.json) |
| A-65 | quiz_started | child | [body](raw/api/browser/A-65.request.json) |
| A-68 | quiz_answer | area_Physical | [body](raw/api/browser/A-68.request.json) |
| A-71 | quiz_answer | area_Cognitive | [body](raw/api/browser/A-71.request.json) |
| A-74 | quiz_answer | area_Language | [body](raw/api/browser/A-74.request.json) |
| A-77 | quiz_answer | area_Social-Emotional | [body](raw/api/browser/A-77.request.json) |
| A-79 | funnel_completed | celebrate | [body](raw/api/browser/A-79.request.json) |
| A-84 | quiz_answer | portrait_shown | [body](raw/api/browser/A-84.request.json) |
| A-87 | quiz_answer | paywall_handoff | [body](raw/api/browser/A-87.request.body) |
| A-101 | paywall_viewed | paywall_early | [body](raw/api/browser/A-101.request.body) |
| A-102 | paywall_viewed | paywall_1 | [body](raw/api/browser/A-102.request.body) |
| B-16 | funnel_started | assessment | [body](raw/api/browser/B-16.request.body) |
| B-28 | quiz_answer | hero | [body](raw/api/browser/B-28.request.body) |
| B-32 | quiz_started | child | [body](raw/api/browser/B-32.request.body) |
| B-36 | quiz_answer | area_Physical | [body](raw/api/browser/B-36.request.body) |
| B-39 | quiz_answer | area_Cognitive | [body](raw/api/browser/B-39.request.body) |
| B-42 | quiz_answer | area_Language | [body](raw/api/browser/B-42.request.body) |
| B-45 | quiz_answer | area_Social-Emotional | [body](raw/api/browser/B-45.request.body) |
| B-47 | extension_started | extension | [body](raw/api/browser/B-47.request.body) |
| B-51 | funnel_completed | celebrate | [body](raw/api/browser/B-51.request.body) |
| B-57 | quiz_answer | portrait_shown | [body](raw/api/browser/B-57.request.body) |

The completed assessment sequence in **A exactly matches STATIC-ANALYSIS.md `3**:

```text
funnel_started:assessment
quiz_answer:hero
quiz_started:child
quiz_answer:area_Physical
quiz_answer:area_Cognitive
quiz_answer:area_Language
quiz_answer:area_Social-Emotional
funnel_completed:celebrate
quiz_answer:portrait_shown
quiz_answer:paywall_handoff
```

B substitutes `extension_started:extension` between the final area event and completion, and stops after `portrait_shown`. `funnel_completed` fires on receipt of the final response, **before** the report Continue click. Primer, date editing, prematurity toggle, individual answers and celebrate Continue have no additional first-party tracking event in these runs. Expected absent branches: age_range, email_captured, reading_email_sent, skill_* and hook-specific events.

Every assessment track body has the exact `3 field set:

```text
event_name, screen, environment, language, test_id, variant, session_id,
utm_source, utm_medium, utm_campaign, utm_content, utm_term,
fbclid, gclid, ttclid, landing_url, referrer, user_agent
```

Common live values are `environment:"prod"`, `language:"en"`, `test_id:"aq-assessment"`, `variant:"classic"`, `utm_source:"assessment-landing"`, `utm_medium:"partner"`. Both tabs use `session_id:"c1c2c937-4c7e-4bd1-afa6-9976eda2d178"`. Campaign/content/term, fbclid/gclid/ttclid and assessment referrer are **null**. `landing_url` is the complete supplied URL, including vid, paywall, offer, newusers, placement, ui and capture. Those parameters have **no standalone fields** in the assessment track body. User agent is the macOS Chrome string recorded above. No birthdate, answers, rate, devAge or per-area scores appear in these tracking bodies.

The two destination-only `paywall_viewed` events add `winback:false` and `properties`, use `test_id:"aq-paywall-trial3"` / `variant:"trial3"`, the paywall landing URL and assessment referrer:

- A-101, `screen:"paywall_early"`: `properties:{"phase":"early","offer":"p79-t7","trial":true}`.
- A-102, `screen:"paywall_1"`: `properties:{"screen":1,"offer":"p79-t7","trial":true,"from_quiz":false,"baby_age":null}`.

These extra events originate on a different page; they are outside the assessment bundle call-site inventory, rather than missing assessment events. Full per-request metadata and all bodies are linked in the [track index](raw/browser/track-events.json). The two setup responses are marked unavailable by DevTools after navigation; their **request bodies and 200 status** were still recoverable. No response was invented.

## Full third-party tracker/event inventory

The [tracker inventory JSON](raw/browser/tracker-inventory.json) contains **each request's complete URL, decoded query values (including blank values), fragment, request headers and saved body path**. [Facebook events JSON](raw/browser/facebook-events.json) supplies every decoded per-event parameter, including all experiment flags; the lists below identify the events and their meaningful fields.

### Facebook / Meta

Pixel ID **2089634224620932**. Loader `https://connect.facebook.net/en_US/fbevents.js` and pixel configuration `https://connect.facebook.net/signals/config/2089634224620932` loaded for assessment and paywall. Config query includes `v=2.9.433`, `r=stable`, `domain=webpromo.kinedu.com`, `hme` and `ex_m`; these are loader/configuration requests, not named conversion events.

| Request | Destination / ev | Event parameters observed |
| --- | --- | --- |
| A-53 | www.facebook.com/tr/ — **PageView** | `dl` = exact assessment URL, `sw=390`, `sh=844` |
| A-85 | same — **ViewContent** | `cd[content_category]=acquisition`, `cd[content_name]=assessment-classic`, `eid=83a681ea-5324-42a6-bdc5-189b3db2168c` |
| A-89 | same — **InitiateCheckout** | Same category/name, `eid=b59034b2-1743-4305-98b6-6262b47ae023`; `dl` still assessment URL; emitted from the one locked-tile click |
| A-99 | same — **PageView** | `dl` = full paywall URL, `rl` = assessment URL |
| A-114 | same — **PageView** | `dl` = assessment URL on browser Back |
| B-24 | same — **PageView** | `dl` = exact assessment URL, 390×844 |
| B-58 | same — **ViewContent** | `cd[content_category]=acquisition`, `cd[content_name]=assessment-classic`, `eid=3e67df57-d2a3-42f4-91ce-33ed1b8ff6c0` |

The request query fields across these events are: **id, ev, dl, rl, if, ts, iw, sw, sh, v, r, ec, o, aems, fbp, cs_est, ler, cdl, plt, tz, it, coo, eid, cd[content_category], cd[content_name], expv2[n], rqm** (some only on particular events). The full exact values and individual `expv2` indexes are preserved in the JSON, not summarized away. Examples of common observed values: `if=false`, `iw=false`, `v=2.9.433`, `r=stable`, `aems=0;0`, `fbp=fb.1.1793637782396.52484787607683365`, `ler=empty`, `cdl=API_unavailable`, `tz=120`, `coo=false`, `rqm=GET`. Empty `rl` is preserved, even though parsers that discard blanks would omit it. No **Lead** event was observed.

A's preliminary viewport-setup navigation also had a PageView (A-24) and Facebook loaders in the [pre-handoff preserved list](raw/browser/A-network-prepaywall.txt); it is excluded from the seven completed-window events above. Its full request detail had fallen out of the final three-navigation window; no parameters beyond the preserved listing are claimed for it.

### Microsoft Clarity

Project tag **x8ou6ay6eb**. Loaded `www.clarity.ms/tag/x8ou6ay6eb` and `scripts.clarity.ms/0.8.72/clarity.js`. These are active in a normal Chrome browser here; they were not merely static references.

| Phase | Actual collector / requests | Status |
| --- | --- | --- |
| A assessment before handoff | `https://n.clarity.ms/collect` — A-55, 56, 58, 59, 61, 62, 63, 66, 67, 70, 73, 76, 83, 86 | All 204 |
| A paywall | `https://b.clarity.ms/collect` — A-104, 106, 113 | All 204 |
| A browser Back | `https://n.clarity.ms/collect` — A-115 | 204 |
| B assessment through report | `https://r.clarity.ms/collect` — B-26, 29, 30, 34, 35, 38, 41, 44, 49, 56, 59 | All 204 |

No query parameters are present on these /collect URLs. The requests carry `Accept:application/x-clarity-gzip` and compressed bodies. The tool exported gzip bytes through text, with replacement characters; these body files are **not lossless compressed archives** and cannot be used to recover reliable event names or internal payload parameters. Accordingly **Clarity's individual recording events/fields are unobserved**, not inferred from click timing or the script's capabilities. All observed headers, body exports and empty 204 responses are saved and indexed. The setup prelude also used `f.clarity.ms/collect` at A-26 and A-29, visible in the pre-handoff list.

### Stripe, loaded automatically by the first paywall screen

No purchase/checkout/subscribe button was pressed. Nevertheless the destination loaded:

- A-90 `https://js.stripe.com/v3/`.
- A-105 `js.stripe.com/v3/m-outer-3437aaddcdf6922d623e172c2d6f9278.html`, with a fragment carrying encoded paywall `url`, `title`, `referrer` and other Stripe context (all exact fields in the index).
- A-107 `js.stripe.com/v3/fingerprinted/js/m-outer-15a2b40a058ddff1cffdb63779fe3de1.js`.
- A-109 `https://m.stripe.network/inner.html` with its context fragment; A-111 `https://m.stripe.network/out-4.5.45.js`.
- A-112 **POST `https://m.stripe.com/6`**, status 200, `Content-Type:text/plain;charset=UTF-8`.

A-112's body is Base64 of percent-encoded JSON. [Decoded local copy](raw/browser/A-112.stripe-decoded.json) has exact top-level fields **v2, id, t, tag, src, a, b, h**, with `v2:1`, `id:"f437dfdb95adb37c5914f995c8079c73"`, `t:79.7`, `tag:"$npm_package_version"`, `src:"js"` and `h:"908c2cd774864c291d71"`. Object `a` has keys a–o containing browser/device values and timing; `b` contains opaque context including `u`/`v:"webpromo.kinedu.com"`. There is **no event_name or human-readable purchase event** in that payload. It is classified as Stripe browser telemetry from its endpoint and contents; opaque fields are left uninterpreted. The exact encoded body and decoded object are both saved. No create-checkout/payment/session API request appears in the captured list.

### Other external resources / absences

Google Fonts CSS and font files loaded from **fonts.googleapis.com** and **fonts.gstatic.com** for Inter / Plus Jakarta Sans. These are font resources, with family/weight/display query parameters, not observed Analytics events. Chrome's existing Tag Assistant extension injected `chrome-extension://kejbdjndbnbjgmefkgdddjlbokphdefk/cs/ta/tag_assistant_api_bin.js`; this is a browser extension resource, not evidence that the page loaded Google Tag Manager.

**No google-analytics, googletagmanager/GTM, Google Ads collection, TikTok, or other third-party tracker host appears in either completed-window network list.** This is a statement about the captured browser requests only. It does not exclude server-side tracking behind /api/track or traffic outside the observed window.

## Paywall URL and first-screen boundary

The locked Physical tile is a **button**, not an anchor; the report DOM has no link href to read. One click initiated this exact navigation:

```text
https://webpromo.kinedu.com/aq-paywall-trial3/index.html?vid=c1991816-d75d-4e46-a05d-cc40924c2ea8&paywall=trial3&offer=p79-t7&newusers=1&placement=assessment-landing&utm_source=assessment-landing&utm_medium=partner&ui=classic&capture=0&from=assessment
```

The handoff preserves every supplied query parameter and adds **from=assessment**; **paywall=trial3** and **offer=p79-t7** are present.

The first viewport shows the Kinedu logo, “Know EXACTLY what to do with your baby every day”, product artwork, “No Payment Due Now”, “Try for $0”, “By tapping Start Free Trial, you agree to be charged $79.99/year after your 7-day trial unless you cancel.”, “Restore Purchase”, “Terms & Conditions”, and “Privacy Policy”.

The immediate snapshot/DOM text additionally exposed a **dialog named “Checkout”** with “Start your free trial”, a Close button, “Kinedu Premium · 1 year”, “7 days free, cancel anytime”, “$79.99”, and “after the trial”. The saved viewport screenshot shows the landing screen rather than a visible card-entry form. These are separate observations; no claim is made that a usable payment form was visible. No dialog control was clicked. After the passive URL/snapshot/screenshot capture, browser Back returned to the assessment. Stripe loading and the named InitiateCheckout pixel are automatic consequences of this handoff; neither demonstrates that a payment attempt was made.

## Live vs static / prior scoring comparison

| Prediction or inference | Live observation | Verdict |
| --- | --- | --- |
| Classic has one primer, then child, area lists, celebrate and portrait; capture=0 skips email | Exactly that path in A; B inserts extension; no lead/reading request | Confirmed |
| API start sends only action/birthdate/gestation | Exact three-field bodies, full term null; returned age 12 and corrected false | Confirmed |
| Fixed base list, anchor → items → one calibration item for first three areas | All 39 IDs/rates/titles/order equal age 12; live snapshots equal too | Confirmed, no question differences |
| No per-answer /api/assessment or per-answer /api/track | 2 assessment calls in A; 3 in B; area-completion tracking only | Confirmed for these runs |
| C_age12_rate_ge50: 28 Yes → complete / devAge14 / well_ahead / P14 C16 L12 S16 | All values match; complete response byte-identical | Confirmed |
| 39 base Yes produces first extension IDs 558,684,651,503,695,566,658,612 | Exact same eight, 2 per area | Confirmed |
| All eight extension Yes, extended:true → 42+, capped | devAge42/cappedtrue and UI 42+; complete response byte-identical | Confirmed |
| Strongest-area card derives from detail; teaser independently uses basic.teaserArea | A Cognitive16 shown vs Physical14 teaser; B Social40 shown vs Language26 teaser | Previously inferred UI inconsistency now observed |
| Locked numbers are literal 88; fixed blurred bars | DOM around88×3, 6px blur; empty 3px-blurred bars with 38%/24% zone | Confirmed |
| Full detail/skills/activity already in the free result | 4 areas, 27/30 skills and recommended activity returned | Confirmed |
| Assessment track event sequence and metadata in `3 | Exact sequence and field set, with extension event only in B | Confirmed |
| Facebook portrait/handoff events; Clarity runtime was not established statically | ViewContent and InitiateCheckout sent; Clarity loaders and collectors active | Runtime uncertainty resolved for this browser |
| Paywall/offer choose post-report destination | Exact trial3 path and p79-t7 query; destination auto-loads price/Stripe and emits two paywall_viewed events | Confirmed handoff; destination behavior extends static assessment scope |

**No discrepancy was found in the question list or either Phase 3 scoring prediction.** Observed product inconsistencies are the two strongest-area teaser mismatches, and the paywall telemetry's `from_quiz:false` / `baby_age:null` despite arriving through the assessment handoff. The latter is an observed field mismatch, not proof of missing backend storage.

The exercise does not retest all age bands, prematurity scoring, invalid/old dates, lead delivery, alternate languages, other UI variants, purchase behavior or clinical validity. It establishes these two live paths and their captured traffic.

## 12-line summary

1. Walked the exact ad URL in normal Mac Chrome at 390×844, plus one 1280-wide hero capture.
2. Saved 15 ordered screenshots, state snapshots, request metadata and exact JSON response bodies.
3. Both starts sent birthdate 2025-11-02/full term and returned ageMonths 12, corrected false.
4. All 39 question IDs, rates, texts and order match the documented age-12 list.
5. Run A submitted 28 Yes and 11 Not yet, with no extension.
6. Run A returned complete, devAge14, well_ahead and area ages P14 C16 L12 S16.
7. Its free report showed Cognitive16 while calling Physical the strongest area.
8. Three locked numbers are literal around88; real milestone titles are also blurred in the DOM.
9. One locked-tile click preserved trial3/p79-t7, captured the first paywall screen, then went Back.
10. Run B served the predicted eight-item extension and finished at capped 42+ after 47 Yes.
11. Tracking matched the static sequence; Meta and Clarity sent traffic, and the paywall loaded Stripe.
12. No email or purchase control was used; both final response bodies exactly match Phase 3.
