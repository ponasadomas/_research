# Browser walkthrough — bare-URL AQ assessment

Observed **2026-11-03, 10:44–10:48 UTC**, with a final read-only context check at 10:49 UTC, in the connected real Chrome/156 on macOS. The existing VPN connection was left unchanged. One completed assessment was run at exactly **https://webpromo.kinedu.com/aq-assessment**, with no appended query string.

**Yes, this funnel gives a free report after the email gate.** For the same 28-Yes profile as Phase 4 Run A, it shows a typical developmental age of **14 months at chronological age 12**, the positive band sentence, an overall pace bar, and a Physical strongest-area teaser. **All four area ages are concealed using literal `●● months` placeholders.** No skill list, opening milestones or daily activity is rendered. The result API response is **byte-identical** to Phase 4 A, including the real area ages **Physical 14, Cognitive 16, Language 12, Social-Emotional 16**.

README.md, STATIC-ANALYSIS.md §2 assessment state machine, §5 assessment/list/skills portrait and §6 email capture, and BROWSER-WALKTHROUGH.md were read first. Classic comparisons below use that saved Phase 4 evidence, not another browser run. The classic URL also included the original ad attribution, `paywall=trial3` and `offer=p79-t7`; this compares the two requested URLs, not an experiment changing only `ui`.

## Classic versus bare URL, by state

| State / property | Classic (`ui=classic&capture=0`, Phase 4 A) | Bare URL (`assessment`, this run) |
| --- | --- | --- |
| Hero layout | Dense page: logo, blue headline, green pill CTA, sample report, reassurance card and credentials below | Sparse, vertically centered content: logo, new blue `KINEDU ASSESSMENT` eyebrow, navy headline, blue rounded CTA; no sample report or reassurance card; centered narrow column at 1280 wide too |
| Hero headline / paragraph | “See what your baby is building right now”; “Answer about what they do today and see which skills are opening up — compared to what’s typical at their exact age.” | Same headline; paragraph instead begins “Answer real questions from Kinedu’s developmental assessment” and includes the 2,135-caregiver claim; complete copy below |
| Hero CTA / metadata | “Start FREE assessment →”; “⏱ 5–10 minutes”; “📄 Free reading included” below CTA | “Start →”; “⏱ 5–10 min · 0–48 months · Free reading” above CTA; no document icon |
| Hero example / credentials | Six-month example with four area ages, usual-range graphic, “Example — not a real child’s result.”; half-Not-yet note; separate Kinedu/2,135-caregiver/Stanford-adviser paragraph | Entire example, its labels/numbers/graphic/disclaimer, half-Not-yet note and separate credentials paragraph absent; 2,135 retained in main paragraph, Michael C. Frank/Stanford/0–24-month advisory claim absent. Both retain “Development surveillance, not diagnosis.” |
| Primers | One “Before we start” screen, three explanatory blocks; “Start the questions →” | Three screens with `1 / 3`, `2 / 3`, `3 / 3`: “How to answer” → “You'll see things they can't do yet” → “Chosen for their exact age”; Next, Next, Start |
| Child | “Name (optional)”; custom month/year selectors and day-grid calendar; disclaimer | “Name” with placeholder “María”, left blank successfully; native `input type=date`, visibly `dd/mm/yyyy`, segmented day/month/year and picker button; no disclaimer. Same unchecked “Born before 37 weeks?” and questions CTA |
| Questions | Four area cards, 10/10/10/9 rows; answer all rows then Next; Back from area 2 | 39 individual screens, 10/10/10/9; either answer immediately advances; no Back or Next control; area icon/name, local counter and uppercase skill label. Same exact titles, order, IDs and rates |
| Celebrate | “All done!”; comparison explanation; “39 answers” and “4 areas”; “See your baby’s reading →” | “All done! 🎉”; “Thank you for getting to know your baby better. Their portrait is ready.”; “See their portrait →”; separate 🎉 decoration, no answer/area totals |
| Email gate | Bypassed by `capture=0`; zero lead calls | Required UI step, no skip control; captured exactly `incomehero@gmail.com`; `/api/lead` returned `{"ok":true}`. The already-computed result was not recalculated |
| Free report headline | “The reading is ready!”; age-14 sentence as headline; positive band as subordinate line; `→ faster` and age-specific explanation | Positive band sentence is headline, age-14 sentence below; `slower`, generic usual-range note, `faster`; no ready banner or “reading already complete” note |
| Free report areas / content | Cognitive “around 16 months” visible; other three `around 88` values blurred 6px, mini-bars blurred 3px; one opening milestone visible, two titles blurred 5px, `+3 more`; Physical teaser | All four full area names with emoji and `●● months` blurred 4px. No mini-bars or milestone block. Same Physical teaser. API still returns all four real ages, 27 skills and recommended activity |
| Report CTA | Fixed “Unlock your baby’s full profile + daily activities →”, trial/no-commitment and saved-answers lines; locked tiles also clickable | Inline “Unlock your baby’s full profile →”; area tiles are plain divs, not buttons; no trial line, fixed unlock bar or saved-answers line. Same reassurance and surveillance disclaimer |
| Paywall handoff | Trial3 URL preserves all original ad parameters, `offer=p79-t7`, `ui=classic`, `capture=0`, then adds `from=assessment` | Actual document navigation is `…/aq-paywall-trial3/index.html?from=assessment`, **no offer**. Destination then adds `offer=p79-t7` with `history.replaceState`; first screen has same trial/price copy |
| Assessment tracking | `variant:classic`, `test_id:aq-assessment`; ad UTMs; `portrait_shown` event and Meta ViewContent `assessment-classic`; no email event | `variant:assessment`, same test_id, null attribution; **no portrait_shown or ViewContent**; email_captured and Meta Lead `assessment`; same area-completion/completion/handoff events |
| Destination tracking | Two paywall_viewed events, Meta PageView, Clarity and automatic Stripe telemetry | Same categories. **Paywall track bodies reuse the earlier classic first-touch URL/referrer/UTMs from storage**, while actual navigation, document referrer and Meta `dl` identify this bare-URL run; details below |

The email difference is explained by `capture=0` versus the default gate; static analysis says classic can also show email when capture is enabled. Styling uses DM Sans in the assessment wrapper versus the classic Plus Jakarta Sans wrapper; the live network loaded those respective font families. This run's report heading computed to DM Sans; the root body itself computed to Inter.

## Per-state detail: screen → screenshot → copy → calls

Request numbers are local to the single tab, **not Phase 4 request IDs**. The network window is requests **4–85** inclusive: 82 requests. Requests 1–3 belong to the pre-existing ipinfo tab and are excluded. Clarity recording traffic is inventoried separately; this table identifies the assessment operations and named first-party events.

| State | Screenshot | On-screen copy / behavior | API calls |
| --- | --- | --- | --- |
| `hero`, mobile | [01-hero.png](screenshots/funnel2/01-hero.png) | “KINEDU ASSESSMENT”; unchanged headline; new paragraph; “Start →” | Mount **19**, funnel_started / assessment; Start **31**, quiz_answer / hero |
| `hero`, desktop width | [02-hero-desktop.png](screenshots/funnel2/02-hero-desktop.png) | Same complete copy; centered single column | No additional first-party request from width changes |
| `primer`, n=1 | [03-primer-1.png](screenshots/funnel2/03-primer-1.png) | `1 / 3`; “How to answer”; Yes / Not yet definitions; “Next” | None on entry/Next |
| `primer`, n=2 | [04-primer-2.png](screenshots/funnel2/04-primer-2.png) | `2 / 3`; “You'll see things they can't do yet”; deliberate difficulty; “Next” | None |
| `primer`, n=3 | [05-primer-3.png](screenshots/funnel2/05-primer-3.png) | `3 / 3`; “Chosen for their exact age”; more than 400 milestones; “Start” | None |
| `child` | [06-child.png](screenshots/funnel2/06-child.png) | “Tell us about your baby”; native date field; full term | Submit **37**, assessment:start; success **38**, quiz_started / child |
| `area`, Physical first question | [07-area-physical.png](screenshots/funnel2/07-area-physical.png) | 👣 Physical; `1/10`; “DEVELOPING HAND COORDINATION”; “Lets go of things they're holding on purpose.” | No request per answer; final Physical answer **41**, quiz_answer / area_Physical |
| `area`, Cognitive first question | [08-area-cognitive.png](screenshots/funnel2/08-area-cognitive.png) | 🧩 Cognitive; `1/10`; “EARLY KNOWLEDGE AND CURIOSITY”; “Looks for an item they dropped on the floor.” | Final area answer **43**, quiz_answer / area_Cognitive |
| `area`, Language first question | [09-area-language.png](screenshots/funnel2/09-area-language.png) | 💬 Language; `1/10`; “BABBLING”; “Repeats 'baba' or 'dada' kind of sounds.” | Final area answer **45**, quiz_answer / area_Language |
| `area`, Social-Emotional first question | [10-area-social-emotional.png](screenshots/funnel2/10-area-social-emotional.png) | 🙂 Social-Emotional; `1/9`; “DEVELOPING INDEPENDENCE”; “Enjoys playing on their own.” | Final area answer **47**, quiz_answer / area_Social-Emotional |
| `area`, last question | [11-last-question.png](screenshots/funnel2/11-last-question.png) | Social-Emotional `9/9`; “SELF-CARE AND AUTONOMY”; “Helps with the dressing and undressing processes by moving the right body parts.”; Yes | Last click also sends **48**, assessment:result, extended:false; completion **49**, funnel_completed / celebrate |
| `celebrate` | [12-celebrate.png](screenshots/funnel2/12-celebrate.png) | “All done! 🎉”; portrait-ready sentence; “See their portrait →” | Result already received; CTA enters email, no scoring call |
| `email`, before typing | [13-email-empty.png](screenshots/funnel2/13-email-empty.png) | “Where should we save your baby’s portrait?”; return/remeasure promise; empty `you@example.com`; disabled results CTA | None merely for entering email screen |
| `email`, filled | [14-email-filled.png](screenshots/funnel2/14-email-filled.png) | Exactly `incomehero@gmail.com`; “See your baby's results” enabled | Submit **52**, lead; then **53**, quiz_answer / email_captured; Meta **54**, Lead |
| `portrait` | [15-portrait.png](screenshots/funnel2/15-portrait.png), full page | Positive headline; age 12 / developmental age 14; four blurred placeholders; Physical teaser; inline unlock CTA | **No new assessment, portrait_shown or Meta ViewContent request** |
| External `paywall` | [16-paywall-first-screen.png](screenshots/funnel2/16-paywall-first-screen.png), viewport | “Know EXACTLY what to do with your baby every day”; “Try for $0”; $79.99/year after 7 days | One report CTA click: **57**, quiz_answer / paywall_handoff; document **58**; Meta **59**, InitiateCheckout; destination price **70**, track **71/72** |
| Browser Back | [saved snapshot](raw/browser2/after-back.snapshot.txt) | Returned to the same portrait at the exact bare assessment URL | Meta **84**, PageView; Clarity; no assessment restart or new funnel_started event |

`resize_page(390,844)` was called first. It reported a 500px inner width, so `emulate(viewport:"390x844x1,mobile,touch")` was applied **before the assessment navigation**. Unlike Phase 4, no preliminary assessment start or reset was needed. Width alone was changed to 1280 and back for the desktop-width hero, retaining mobile/touch flags and the normal desktop UA. All 16 PNGs are exactly 844px high; mobile captures are 390px wide, desktop hero 1280px. All use `fullPage:true` except the first paywall viewport; the portrait fits in one viewport.

Every screenshot used `take_screenshot` with an absolute path. The MCP writer rejected the project path as outside its own configured roots, so captures and tool-exported bodies were staged under `/tmp/kinedu-browser/` and **moved byte-for-byte into this folder**. The original export paths remain in raw tool metadata; the indexes link the final project paths. No other project was edited.

## Exact copy before and after the questions

The browser title throughout the assessment is “Kinedu — Your baby’s development, right now”; logo alt text is “Kinedu”. [Hero snapshot](raw/browser2/hero.snapshot.txt) and [DOM copy/viewport](raw/browser2/hero.dom.json).

**Hero, complete text:**

- “KINEDU ASSESSMENT”
- “See what your baby is building right now”
- “Answer real questions from Kinedu’s developmental assessment — created and psychometrically evaluated by Kinedu with 2,135 caregivers — and see your baby’s developmental picture today.”
- “⏱ 5–10 min · 0–48 months · Free reading”
- “Start →”
- “Development surveillance, not diagnosis.”

The psychometric/caregiver language is recorded marketing copy, not an independently verified scientific claim. The desktop-width hero has the same text, no extra sections. Compared with [classic hero](screenshots/01-hero.png), it leaves substantially more empty vertical space, changes the blue headline to navy, and changes the green pill CTA to a blue rounded rectangle. The removed sample block includes all classic example numbers (6, 7, 8/7/6/7), pace labels, per-area labels and example disclaimer; none is reproduced elsewhere on this hero.

**Primer 1**, [snapshot](raw/browser2/primer-1.snapshot.txt): `1 / 3`; heading “How to answer”; paragraph “There are only two answers and neither is a bad one. What matters is that everyone answers by the same rule — that is what makes your child's reading comparable.” Definitions: “Yes — they do it consistently, not just once.”; “Not yet — they don't do it yet, or you're not sure. When in doubt, "Not yet".”; “A "Not yet" is just as useful as a "Yes". Both tell us where they are.” Button “Next”.

**Primer 2**, [snapshot](raw/browser2/primer-2.snapshot.txt): `2 / 3`; heading “You'll see things they can't do yet”; paragraph “That's on purpose. We ask right at the edge of what your baby is learning, because that is where progress shows. A question every child their age already passes tells us nothing.” Then “Expect to answer "Not yet" about half the time. That is normal, and it is what makes the reading precise.”; “A few will sound far too old for them. Those are deliberate too.” Button “Next”.

**Primer 3**, [snapshot](raw/browser2/primer-3.snapshot.txt): `3 / 3`; heading “Chosen for their exact age”; paragraph “These aren't a generic list: they were picked for your baby at their exact age, from a catalogue of more than 400 milestones.”; “It takes 5 to 10 minutes.” Button “Start”. The three primers have the logo but no surveillance footer.

**Child**, [empty snapshot](raw/browser2/child.snapshot.txt), [filled snapshot](raw/browser2/child-filled.snapshot.txt), [input DOM](raw/browser2/child.dom.json): “Tell us about your baby”; “Name”; placeholder “María”; “Date of birth”; native date presentation `dd/mm/yyyy`; “Born before 37 weeks?”; “See your baby’s questions →”. The date input has `type:"date"`, no minimum, `max:"2026-11-03"`; accessibility exposes Day, Month, Year spinbuttons and “Show date picker”. Classic instead rendered its own visible Month/Year controls, weekday headings and day buttons. The name was left empty and the full-term checkbox unchecked. No prematurity expansion was opened in this pass.

The MCP fill initially changed the native date's displayed value without enabling the React CTA. Keyboard ArrowUp then ArrowDown on the month committed the change and restored exactly **2025-11-02**; only then was the start submitted. An earlier attempted click on the disabled CTA timed out without an API call. This is an automation interaction detail, not evidence of a user-facing age/scoring defect. The successful body was exactly:

```json
{"action":"start","birthdate":"2025-11-02","gestationalWeeks":null}
```

**Common question copy:** area emoji/name; current question index / total for that area; uppercase skill label; the question title; buttons **“Not yet”** and **“Yes”**; “A “Not yet” is as useful as a “Yes.” Both tell us where your baby is.” No age label, surveillance footer, Back, explicit Next or area-completion interstitial appeared. Clicking an answer immediately replaced the question, including at area boundaries.

**Celebrate**, [snapshot](raw/browser2/celebrate.snapshot.txt): logo; separate “🎉”; heading “All done! 🎉”; “Thank you for getting to know your baby better. Their portrait is ready.”; button “See their portrait →”. No 39-answer or four-area badges.

**Email**, [before](raw/browser2/email-empty.snapshot.txt) / [after typing](raw/browser2/email-filled.snapshot.txt): logo; heading **“Where should we save your baby’s portrait?”**; **“We’ll keep the reading linked to your email so you can come back to it — and re-measure later, which is where the real story shows.”**; placeholder **“you@example.com”**; CTA **“See your baby's results”**. That is all the screen copy: no skip link, consent checkbox, privacy link or surveillance disclaimer. CTA was disabled empty and enabled after typing exactly **incomehero@gmail.com**. No second email or other spelling was entered.

## Every question in observed on-screen order

**39/39 IDs, rates, titles and order match [questions-by-age.md age 12](questions-by-age.md#12-months--39-questions-rawapistart_age13_gw-nulljson)** and Phase 4 A. Each question was checked against the latest snapshot before its real UI answer click. Snapshots **q01–q39** preserve every screen, not just the five question screenshots. [Machine-readable order, titles, skill labels and snapshot links](raw/browser2/question-order.json); [full comparison table with skill labels](raw/browser2/question-comparison.md).

IDs/rates below are from **the live start response exported with get_network_request**, not exposed on screen. Rates ≥0.5 received Yes, everything else Not yet. Calibration IDs 686 and 611 are Social-Emotional in the API but shown at the ends of Physical and Cognitive; 688 is Language. This is the same flattening as classic.

| # | Displayed area / counter | ID | Rate | Answer | Exact on-screen question |
| --- | --- | --- | --- | --- | --- |
| 1 | Physical 1/10 | 135 | 0.98 | Yes | Lets go of things they're holding on purpose. |
| 2 | Physical 2/10 | 470 | 0.5 | Yes | Can stand up from a squat all alone. |
| 3 | Physical 3/10 | 309 | 0.51 | Yes | Can walk while holding a small toy. |
| 4 | Physical 4/10 | 4 | 0.52 | Yes | Squats to pick things up while walking. |
| 5 | Physical 5/10 | 471 | 0.52 | Yes | Descends stairs with an adult, switching feet. |
| 6 | Physical 6/10 | 355 | 0.47 | Not yet | Pushes or pulls toys while walking. |
| 7 | Physical 7/10 | 330 | 0.54 | Yes | Scribbles by moving their entire arm from the shoulder. |
| 8 | Physical 8/10 | 538 | 0.54 | Yes | Walks up ramps. |
| 9 | Physical 9/10 | 415 | 0.46 | Not yet | Takes unsteady and short steps alone. |
| 10 | Physical 10/10 | 686 | 0.22 | Not yet | Drinks from a cup with one hand. |
| 11 | Cognitive 1/10 | 183 | 0.97 | Yes | Looks for an item they dropped on the floor. |
| 12 | Cognitive 2/10 | 5 | 0.51 | Yes | Imitates what friends do in play, such as building towers when they do. |
| 13 | Cognitive 3/10 | 335 | 0.52 | Yes | Moves a body part when asked to. |
| 14 | Cognitive 4/10 | 406 | 0.6 | Yes | Copies how adults use things (like pretending to talk on the phone after seeing mom do it). |
| 15 | Cognitive 5/10 | 472 | 0.6 | Yes | Finds their way in familiar places, such as their parent's room. |
| 16 | Cognitive 6/10 | 338 | 0.64 | Yes | Claps or taps an instrument to the rhythm of a song. |
| 17 | Cognitive 7/10 | 436 | 0.35 | Not yet | Pays attention to an adult reading a book for a few minutes. |
| 18 | Cognitive 8/10 | 19 | 0.65 | Yes | Follows simple, one-step instructions (like 'Pick up the toy'). |
| 19 | Cognitive 9/10 | 53 | 0.32 | Not yet | Copies what caregivers do, like taking a toy phone from a purse and saying 'hello.' |
| 20 | Cognitive 10/10 | 611 | 0.02 | Not yet | Puts on a shirt without buttons. |
| 21 | Language 1/10 | 31 | 0.89 | Yes | Repeats 'baba' or 'dada' kind of sounds. |
| 22 | Language 2/10 | 368 | 0.57 | Yes | Answers simple questions with signs, actions, or words. |
| 23 | Language 3/10 | 279 | 0.42 | Not yet | Points to things they know when you say their name. |
| 24 | Language 4/10 | 360 | 0.39 | Not yet | Points to caregivers, like 'Mom' or 'Dad'. |
| 25 | Language 5/10 | 54 | 0.68 | Yes | Imitates a sound like 'pa' after you say it. |
| 26 | Language 6/10 | 126 | 0.69 | Yes | Talks to other babies with babbles. |
| 27 | Language 7/10 | 7 | 0.72 | Yes | Tries to copy the words you say. |
| 28 | Language 8/10 | 109 | 0.72 | Yes | Understands three-word phrases, like 'Look, a dog!' |
| 29 | Language 9/10 | 32 | 0.27 | Not yet | Names at least three objects correctly. |
| 30 | Language 10/10 | 688 | 0.37 | Not yet | Says simple words with the letter N, like 'nap' or 'banana'. |
| 31 | Social-Emotional 1/9 | 349 | 0.97 | Yes | Enjoys playing on their own. |
| 32 | Social-Emotional 2/9 | 565 | 0.55 | Yes | Uses personal care tools like a hairbrush and toothbrush correctly. |
| 33 | Social-Emotional 3/9 | 476 | 0.6 | Yes | Can feed independently, with or without utensils. |
| 34 | Social-Emotional 4/9 | 103 | 0.71 | Yes | Can correctly use some everyday items (like sipping from a cup or dialing a phone). |
| 35 | Social-Emotional 5/9 | 340 | 0.74 | Yes | Shows you things by pointing. |
| 36 | Social-Emotional 6/9 | 441 | 0.24 | Not yet | Knows which things belong to family members, like Mom's purse or Dad's wallet. |
| 37 | Social-Emotional 7/9 | 454 | 0.77 | Yes | Plays and has fun with other kids. |
| 38 | Social-Emotional 8/9 | 308 | 0.82 | Yes | Expresses love to those familiar, like hugging them. |
| 39 | Social-Emotional 9/9 | 85 | 0.85 | Yes | Helps with the dressing and undressing processes by moving the right body parts. |

Totals: **28 Yes, 11 Not yet; no extension**. Display grouping is 10/10/10/9; by the items' actual API areas it is P9/C9/L10/S11. The result request's answers array also matches Phase 4 A byte-for-byte.

## Email submission: full request and response

Request **52**, POST `/api/lead`, HTTP **200**. Exported with `get_network_request`, bytes retained in [lead.request.json](raw/api/browser2/lead.request.json) and [lead.response.json](raw/api/browser2/lead.response.json); [headers/status](raw/browser2/52.network.txt). Full body:

```json
{"email":"incomehero@gmail.com","name":"","environment":"prod","language":"en","test_id":"aq-assessment","variant":"assessment","session_id":"c1c2c937-4c7e-4bd1-afa6-9976eda2d178","utm_source":null,"utm_medium":null,"utm_campaign":null,"landing_url":"https://webpromo.kinedu.com/aq-assessment"}
```

Full response:

```json
{"ok":true}
```

No birthdate, age, gestation, answer array or computed report was in this request. **Zero `/api/send-reading` calls** occurred, including after the successful lead. There was also no `reading_email_sent` event. `sessionStorage.kinedu_email` contained the exact entered address after Back. The page's promise about linking and returning to a reading is copy; this run did not verify inbox delivery or a later-session restoration workflow. Absence of a browser send-reading request does not establish whether the lead backend has other side effects.

## Portrait: every visible label, number and sentence

[Full-page screenshot](screenshots/funnel2/15-portrait.png), [accessibility snapshot](raw/browser2/portrait.snapshot.txt), [DOM/text/computed styles](raw/browser2/portrait.dom.json). The complete report content, in order:

1. Kinedu logo.
2. **“TODAY'S PICTURE”**.
3. **“A lot is already in place, and new skills keep opening up.”**
4. **“At 12 months, your baby is showing the skills of a typical 14-month-old.”**
5. Horizontal overall pace bar with green usual-range zone and a dot. Under it: **“slower”**, **“the green band is the usual range for this age”**, **“faster”**.
6. **“BY AREA”**.
7. **“👣 Physical”**, blurred **“●● months”**.
8. **“🧩 Cognitive”**, blurred **“●● months”**.
9. **“💬 Language”**, blurred **“●● months”**.
10. **“🙂 Social-Emotional”**, blurred **“●● months”**.
11. **“✨ Physical looks like their strongest area — unlock the full profile to see all four.”**
12. **“Unlock your baby’s full profile →”** button.
13. **“Every child develops at their own pace. This helps you understand their unique journey — not compare them to others.”**
14. **“Development surveillance, not diagnosis.”**

The only printed score numbers are **12** and **14** in the age sentence. There is no numeric AQ, percentile, percent-ahead number, diagnostic label, visible area age, skill count or activity. The code `well_ahead` is not printed. The strongest-area sentence names Physical despite the response giving Cognitive and Social-Emotional higher ages (16 versus 14); the teaser comes from `basic.teaserArea`. Classic showed the same teaser mismatch, with Cognitive 16 exposed; here every numeric tile is concealed.

**Every blur/hidden element**, confirmed without changing CSS or revealing anything through a UI click:

| Area tile | Literal DOM value | Computed filter | Real API age, absent from tile |
| --- | --- | --- | --- |
| Physical | `●● months` | `blur(4px)` | 14 |
| Cognitive | `●● months` | `blur(4px)` | 16 |
| Language | `●● months` | `blur(4px)` | 12 |
| Social-Emotional | `●● months` | `blur(4px)` | 16 |

These four spans are the **only CSS-blurred elements**. Their `aria-hidden` attributes are absent, so the accessibility snapshot actually includes the placeholders, unlike classic's aria-hidden `88` and locked milestone titles. The tile parents are plain divs; the page has exactly one button, the main unlock CTA. No other report element was found with `hidden`, `aria-hidden=true`, `display:none`, `visibility:hidden` or zero opacity, excluding script/style/metadata infrastructure. There are **no hidden real area numbers or blurred milestone titles in the rendered report DOM**. The API's 27 skills, curves and “Hand me the toy” activity are available in the response but not rendered in this variant.

The DOM shows the green zone fixed at `left:28%; right:28%` and the score dot at `left:62.963%`. Static analysis explains the former as cosmetic fixed geometry and the latter as derived from devAge/age; this single run observes those styles, not independent validation of the whole positioning formula.

## Assessment API evidence and byte comparison

Both assessment requests were POST JSON with **200** responses. They were the only `/api/assessment` requests in the window; none was fired by individual answers, email submission or report display.

| Request | Exact saved request / response | Observed result |
| --- | --- | --- |
| **37**, start | [request](raw/api/browser2/start.request.json), [response](raw/api/browser2/start.response.json), [metadata](raw/browser2/37.network.txt) | birthdate 2025-11-02, gestationalWeeks null → ageMonths 12, corrected false, four sections and three calibration items |
| **48**, result | [request](raw/api/browser2/result.request.json), [response](raw/api/browser2/result.response.json), [metadata](raw/browser2/48.network.txt) | ageMonths 12, extended false, 39 answers / 28 Yes → stage complete, basic.state ok, band well_ahead, devAge 14, capped false, tier basic, areasLocked true, teaserArea Physical |

Result `detail` also has state ok, band well_ahead, devAge 14, capped false, ageMonths 12, tier detail, and P14/C16/L12/S16, all state ok and atLeast false; `areasDefaultHidden:false`. That field does not make the area ages visible in this UI. The full response includes **27 skills** and activity **Language / targetMonth 12 / “Hand me the toy”** (also translated es/pt), despite rendering none of them.

Executed offline:

```sh
cmp raw/api/browser2/result.response.json raw/api/browser/A-result.response.json
```

**Exit 0, no difference; 58,084 bytes**, SHA-256 `3377816538b9c46300b5ce85cd856246a1163d7baa41c25604e0b0aae635d36d` for both. The start request (67 bytes), start response (5,332 bytes) and result request (714 bytes) are also byte-identical to their Phase 4 A counterparts. [All comparisons and image hashes/dimensions](raw/browser2/verification.json). The different landing/report/email experience therefore did not change the assessment payloads or returned scoring data on this path.

## One report CTA click: navigation versus destination URL

One click on **“Unlock your baby’s full profile →”** produced document request **58**:

```text
https://webpromo.kinedu.com/aq-paywall-trial3/index.html?from=assessment
```

This is the actual handoff URL: default trial3 path, `from=assessment`, **no offer or original ad parameters**. Request 58 returned **200**, with no HTTP redirect listed. [Exact request headers/status](raw/browser2/58.network.txt), [saved response HTML](raw/browser2/paywall-document.html).

By the first page snapshot/DOM read, the browser address was:

```text
https://webpromo.kinedu.com/aq-paywall-trial3/index.html?from=assessment&offer=p79-t7
```

This second URL is also observed, not inferred from the previous run. The saved destination HTML at lines 390–400 sets `DEFAULT_OFFER='p79-t7'`, adds it to the query if missing/unrecognized, and calls `history.replaceState`. That source explains the runtime URL change; it is **destination behavior**, not an offer appended by the assessment handoff. Its Meta PageView and `/api/localized-price?offer=p79-t7` use the amended URL/offer.

First viewport copy: Kinedu logo; **“Know EXACTLY what to do with your baby every day”**; product artwork; **“No Payment Due Now”**; **“Try for $0”**; **“By tapping Start Free Trial, you agree to be charged $79.99/year after your 7-day trial unless you cancel.”**; **“Restore Purchase”**; separators; **“Terms & Conditions”**; **“Privacy Policy”**. This matches the Phase 4 first-screen price/copy.

As in Phase 4, snapshot/DOM also exposes a dialog named **“Checkout”** with **“Start your free trial”**, close glyph/Close button, **“Kinedu Premium · 1 year”**, **“7 days free, cancel anytime”**, **“$79.99”**, **“after the trial”**. The screenshot shows the landing artwork/CTA, with no visible card-entry form. The DOM's display/visibility values do not establish that a usable payment form was visually open. No paywall button, dialog control, purchase, checkout, subscribe or trial control was clicked. Browser Back returned to the existing portrait; no second assessment was run.

## Network audit and Phase 4 comparison

The [pre-handoff list](raw/browser2/network-prepaywall.txt), [paywall list](raw/browser2/network-paywall.txt) and [final preserved list](raw/browser2/network-final.txt) retain the capture chronology. The [network inventory](raw/browser2/network-inventory.json) indexes all **82 requests**, full retrieved URLs/query/fragment, request headers, actual final status where retrieved, and saved body paths. The final listing caught request 85 pending; its later get_network_request metadata confirms **204**. Background traffic after request 85 is outside this defined window.

### Every first-party track event

All **12** `/api/track` calls returned **200**; all exact request bodies are saved and linked below and in [track-events.json](raw/browser2/track-events.json). Assessment has ten events, destination two. Primer advancement, date editing, individual answers, celebrate Continue and report entry emitted no additional first-party event in this run.

| Request | event_name | screen | variant | test_id | Exact body |
| --- | --- | --- | --- | --- | --- |
| 19 | funnel_started | assessment | assessment | aq-assessment | [JSON](raw/api/browser2/19.request.json) |
| 31 | quiz_answer | hero | assessment | aq-assessment | [JSON](raw/api/browser2/31.request.json) |
| 38 | quiz_started | child | assessment | aq-assessment | [JSON](raw/api/browser2/38.request.json) |
| 41 | quiz_answer | area_Physical | assessment | aq-assessment | [JSON](raw/api/browser2/41.request.json) |
| 43 | quiz_answer | area_Cognitive | assessment | aq-assessment | [JSON](raw/api/browser2/43.request.json) |
| 45 | quiz_answer | area_Language | assessment | aq-assessment | [JSON](raw/api/browser2/45.request.json) |
| 47 | quiz_answer | area_Social-Emotional | assessment | aq-assessment | [JSON](raw/api/browser2/47.request.json) |
| 49 | funnel_completed | celebrate | assessment | aq-assessment | [JSON](raw/api/browser2/49.request.json) |
| 53 | quiz_answer | email_captured | assessment | aq-assessment | [JSON](raw/api/browser2/53.request.json) |
| 57 | quiz_answer | paywall_handoff | assessment | aq-assessment | [JSON](raw/api/browser2/57.request.json) |
| 71 | paywall_viewed | paywall_early | trial3 | aq-paywall-trial3 | [JSON](raw/api/browser2/71.request.json) |
| 72 | paywall_viewed | paywall_1 | trial3 | aq-paywall-trial3 | [JSON](raw/api/browser2/72.request.json) |

Every assessment track body has the same field set as Phase 4:

```text
event_name, screen, environment, language, test_id, variant, session_id,
utm_source, utm_medium, utm_campaign, utm_content, utm_term,
fbclid, gclid, ttclid, landing_url, referrer, user_agent
```

Common values here: `environment:"prod"`, `language:"en"`, `test_id:"aq-assessment"`, **`variant:"assessment"`**, `session_id:"c1c2c937-4c7e-4bd1-afa6-9976eda2d178"`, `landing_url:"https://webpromo.kinedu.com/aq-assessment"`, all five UTMs and fbclid/gclid/ttclid **null**, referrer **null**. UA is `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36`. No birthdate, answers, rate, devAge, area ages or email appears in these track bodies.

Compared with Phase 4 A's ten assessment events, **email_captured replaces portrait_shown**; the remaining event_name/screen pairs match. `funnel_completed` is sent on receipt of the final result, **before the email gate and report view**. No extension_started, portrait_shown, reading_email_sent, skill_* or age_range event occurred. This is consistent with the `_` component's inventory, including its deliberate lack of a portrait_shown effect.

Destination events add `winback:false` and `properties`:

- **71**, paywall_early: `{"phase":"early","offer":"p79-t7","trial":true}`.
- **72**, paywall_1: `{"screen":1,"offer":"p79-t7","trial":true,"from_quiz":false,"baby_age":null}`.

**Observed attribution carryover:** those two destination bodies report `utm_source:"assessment-landing"`, `utm_medium:"partner"`, the **old full classic paywall landing_url**, and the **old full classic assessment referrer**—the exact Phase 4 URLs—rather than this run's URLs. The actual paywall `document.referrer`, HTTP navigation referrer and Meta PageView `rl` are the bare assessment URL. The [read-only storage check](raw/browser2/context-after-back.json) found `kinedu_first_touch` with those old URLs and `landed_at:"2026-11-02T16:48:48.065Z"`. Saved paywall HTML lines 866–893 reads that localStorage object and retains it when the current query contains no campaign/placement/click identifiers. This directly explains the carryover for this reused browser session; a fresh browser's attribution was not tested. Phase 4's session ID is also reused. `from_quiz:false` and `baby_age:null` repeat the Phase 4 destination metadata mismatch, despite arriving from the completed quiz.

### Meta / Facebook: every event and parameter export

Pixel **2089634224620932**, with `connect.facebook.net/en_US/fbevents.js` (17/67) and pixel configuration (23/68). Loader config includes `v=2.9.433`, `r=stable`, `domain=webpromo.kinedu.com`, `hme`, `ex_m`; exact full URLs are in the [tracker inventory](raw/browser2/tracker-inventory.json). They are configuration requests, not named conversion events.

| Request | Event (`ev`) | Observed event-specific parameters |
| --- | --- | --- |
| 24 | PageView | `dl` exact bare assessment URL; `rl` empty; sw=390, sh=844 |
| 54 | Lead | `dl` bare assessment; `cd[content_category]=acquisition`, `cd[content_name]=assessment`; `eid=7d5baa9c-07bc-4d61-bd69-62b3f4aa35e6`; emitted after lead submission |
| 59 | InitiateCheckout | `dl` bare assessment; same category/name; `eid=c29663be-95cd-4c81-86f7-4fb61daddecf`; emitted by the one report CTA click |
| 69 | PageView | `dl` paywall URL **with offer=p79-t7**; `rl` bare assessment |
| 84 | PageView | `dl` bare assessment on Back; `rl` empty |

All five GET event requests returned **200**. **No ViewContent** occurred. Phase 4 A instead had ViewContent `assessment-classic` and no Lead; its handoff used content_name `assessment-classic`, whereas this run's Lead/handoff use `assessment`.

The [Facebook events JSON](raw/browser2/facebook-events.json) saves **every exact decoded parameter for each event**, including blank values and all `expv2[n]` flags. Across the five requests, field names are `id, ev, dl, rl, if, ts, iw, sw, sh, v, r, ec, o, aems, fbp, cs_est, ler, cdl, plt, tz, it, coo, eid, cd[content_category], cd[content_name], expv2[n], rqm` (not every field is on every event). Common values include `if=false`, `iw=false`, `v=2.9.433`, `r=stable`, `aems=0;0`, `fbp=fb.1.1793637782396.52484787607683365`, `ler=empty`, `cdl=API_unavailable`, `tz=120`, `coo=false`, `rqm=GET`. The actual email string does not appear in these five event URLs; this audit does not infer what the pixel might do outside the captured requests.

### Microsoft Clarity

Same project **x8ou6ay6eb** as Phase 4. Tag requests **16/66** loaded `https://www.clarity.ms/tag/x8ou6ay6eb`; runtime requests **22/73** loaded **`scripts.clarity.ms/0.8.77-beta/clarity.js`**, versus Phase 4's `0.8.72`.

All **20** collector requests went to **`https://k.clarity.ms/collect`**, with no query parameters, and returned **204**:

```text
25,28,29,30,32,33,35,36,39,40,42,44,46,51,55,56,74,76,83,85
```

Requests through 56 precede the handoff; 74/76/83 are at the paywall/Back boundary; 85 follows the return PageView. These are request-order groupings, not decoded recording-event attribution. Phase 4 used other Clarity collector subdomains (n/b/r and setup f), not k. `Accept:application/x-clarity-gzip` and compressed bodies are observed. Tool-exported body files contain replacement characters and are **lossy UTF-8 representations, not usable lossless gzip archives**; no internal Clarity event names, recorded input values or session-replay fields are claimed. Exact request metadata and available body exports are indexed.

### Stripe and other external resources

The first paywall page automatically loaded the same Stripe resource families as Phase 4, without a paywall click:

- **60** `https://js.stripe.com/v3/`.
- **75** `js.stripe.com/v3/m-outer-3437aaddcdf6922d623e172c2d6f9278.html` with context fragment, including current paywall URL/title/referrer; **77** its fingerprinted JS.
- **79** `https://m.stripe.network/inner.html` with context fragment; **81** `out-4.5.45.js`.
- **82** POST `https://m.stripe.com/6`, HTTP **200**, text/plain body. [Exact body](raw/api/browser2/82.request.body), [decoded JSON](raw/browser2/82.stripe-decoded.json).

The telemetry body is Base64 of percent-encoded JSON with top-level fields **v2, id, t, tag, src, a, b, h**. It has `v2:1`, `src:"js"`, browser/device values in a, opaque context in b, and no human-readable purchase `event_name`. Opaque fields are left uninterpreted. This observed telemetry and the Meta event named InitiateCheckout do **not** establish that a purchase or payment submission occurred. There is no create-checkout/payment/session API request in the captured list.

Google Fonts loaded Inter and **DM Sans** CSS/font resources (14/18/21/27); classic loaded Plus Jakarta Sans instead of DM Sans. Google font hosts are resources, not observed Analytics collectors. The existing Tag Assistant extension injected `chrome-extension://kejbdjndbnbjgmefkgdddjlbokphdefk/cs/ta/tag_assistant_api_bin.js` (15/65/78/80), as in Phase 4; that is not a page GTM request. The native date picker also requested an inline `data:image/svg+xml` icon (34). The first-party favicon returned 404 (26); no resulting flow failure was observed.

**No Google Analytics/GA4, Google Tag Manager, Google Ads collection, TikTok or additional third-party tracker host** appears in requests 4–85. This is a captured-network statement, not a claim about server-side tracking or later traffic.

Response bodies that DevTools had already discarded are explicitly marked unavailable in the inventory, including localized-price 70 and the later paywall track responses. Their request bodies/status/headers were recoverable; no response payload was invented. The three required lead/start/result response bodies were all exported successfully. In total: **2 assessment, 12 track, 1 lead, 0 send-reading, 5 Facebook events, 20 Clarity collects**.

## What went beyond STATIC-ANALYSIS.md

No contradiction was found in the assessment state machine, email behavior, question construction, report placeholders or assessment event inventory. The observed additions below concern runtime services or the destination, outside that static assessment scope:

- **The initial offer-free paywall URL becomes `offer=p79-t7` on the destination.** Both URLs were captured; saved destination source explains its replaceState default. Thus “no offer” is true of the assessment navigation, not the final address bar.
- **Stored attribution survives into this paywall's track bodies.** In this reused browser, two current paywall events carry Phase 4's old classic URLs/UTMs; source and storage reads explain why. Assessment events and lead use this run's bare URL/null UTMs.
- **Clarity runtime changed** to `0.8.77-beta` and the k collector; actual runtime requests, Stripe telemetry and the first paywall screen extend the assessment-only static evidence. Automatic Stripe/dialog behavior was already seen in Phase 4.

The report's strongest-area inconsistency is reproduced, not a new scoring difference: API teaser Physical versus P14/C16/L12/S16. Browser Back preserved this portrait without a fresh start; that observation alone does not demonstrate saved-report retrieval after reload or a later visit.

All comparisons can be rebuilt **offline**, without repeating the email or browser run, using `python3 scripts/build_browser2_evidence.py`. It checks all 39 snapshot titles/order against the live response and age-12 reference, submitted answers against the rate rule, exact classic body bytes, four DOM placeholders, and PNG dimensions/hashes.

## 12-line summary

1. Walked the exact bare URL once in real Chrome through the existing VPN, at 390×844 plus one 1280-wide hero capture.
2. Saved 16 ordered screenshots and snapshots of all 39 question screens, with the report captured full-page.
3. The sparse hero replaces classic's sample report with new assessment/caregiver copy and a blue Start CTA.
4. Three primers lead to a native date input; blank name, birthdate 2025-11-02 and full term returned ageMonths 12.
5. All 39 question IDs, rates, titles and order match questions-by-age.md age 12 and Phase 4 A.
6. The live rate≥0.5 rule submitted 28 Yes and 11 Not yet, with no extension.
7. The email gate captured exactly incomehero@gmail.com; lead returned ok:true and no send-reading request fired.
8. The free portrait shows typical age 14 at age 12, the positive band sentence, pace bar and Physical teaser.
9. All four area tiles are literal ●● months with 4px blur; no skill, opening-milestone or activity content is rendered.
10. The complete result response is byte-identical to Phase 4 A, including real area ages P14/C16/L12/S16.
11. One report CTA click navigated without offer; the paywall added p79-t7, was captured, and Back returned to the portrait.
12. Tracking adds Lead/email_captured, omits ViewContent/portrait_shown, and exposes inherited classic attribution on the paywall.
