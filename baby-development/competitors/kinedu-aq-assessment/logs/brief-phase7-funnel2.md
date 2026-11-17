# Phase 7 — Browser walkthrough of the SECOND landing page (bare URL, "assessment" variant)

Read README.md, STATIC-ANALYSIS.md §2 ("assessment" state machine), §5 ("_: assessment/list/skills portrait, exactly what is rendered"),
§6 (email capture) and BROWSER-WALKTHROUGH.md (Phase 4, the classic funnel, to compare against). You drive the real Chrome via the
chrome-devtools MCP (already connected; it exits through a VPN, do not change that). Work only in this folder.
Screenshots: take_screenshot with filePath absolute, into screenshots/funnel2/, named NN-<state>.png in order. Mobile viewport
390x844 (resize_page first); one desktop 1280-wide hero screenshot too.

Funnel URL (exactly this, nothing appended): https://webpromo.kinedu.com/aq-assessment

Rules: the email screen WILL appear in this variant (no capture=0). When it does, screenshot it, then enter exactly
incomehero@gmail.com and continue. Never click buy/checkout/subscribe/"start trial" or anything on the paywall page; capture the
paywall URL from the navigation that starts after ONE click on the report's main CTA, screenshot the first paywall screen, go back.
Keep clicks minimal.

Run (one pass, "typical" child):
1. Hero: screenshot (mobile + desktop), take_snapshot, record all copy. Note every difference from the classic hero.
2. Click Start. Expect THREE primer screens: screenshot each, record copy.
3. Child screen: screenshot; birthdate 2025-11-02 (→ ageMonths 12), full term. Record how the date input differs from classic.
4. Questions: expect one question per screen. Screenshot the first screen of each area and the last question. Answer YES for
   items with rate >= 0.5 and NOT YET otherwise (use the /api/assessment start response via get_network_request to know rates;
   this is the same 28-yes profile as Phase 4 Run A, expected devAge 14 well_ahead). Record the on-screen question order and
   compare with questions-by-age.md age 12.
5. Celebrate screen: screenshot, copy.
6. Email screen: screenshot BEFORE typing; record all copy; enter incomehero@gmail.com; screenshot; continue. Capture the
   /api/lead request body in full (get_network_request) and the response, save to raw/api/browser2/lead.request.json / .response.json.
   Check whether /api/send-reading fires (expected: never in this variant).
7. Report ("portrait"): full-page screenshot. Record every visible number/label/sentence and every hidden/blurred element.
   Read the DOM (evaluate_script) to confirm what the four area tiles show (expected literal "●● months" placeholders).
   Save the /api/assessment result response to raw/api/browser2/result.response.json; compare with Phase 4's A-result.response.json
   (cmp) — expect byte-identical, since same age + answers.
8. One click on the main CTA → record the destination URL (expect /aq-paywall-trial3/... with from=assessment and no offer
   param), screenshot first screen, go back.
9. Network audit: every /api/assessment, /api/track (event_name + screen + variant + test_id fields), /api/lead, /api/send-reading,
   and third-party trackers (facebook.com/tr events + params, clarity, anything else). Compare with Phase 4's inventory.

Write BROWSER-WALKTHROUGH-FUNNEL2.md: a side-by-side table "classic (ui=classic&capture=0) vs bare URL" per state (screens, copy,
email gate, report content, paywall URL, tracking), then the per-state detail table (state → screenshot → copy → API calls),
the answer to "does this funnel give a report, and what does it show?", and a short list of anything not predicted by
STATIC-ANALYSIS.md. Observed vs inferred, no fabrication. Finish with a 12-line summary.
