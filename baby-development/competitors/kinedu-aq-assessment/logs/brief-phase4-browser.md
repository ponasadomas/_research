# Phase 4 — Browser walkthrough of the Kinedu "classic" funnel (confirm Phases 1–3 live)

Read README.md, then STATIC-ANALYSIS.md §2 (classic state machine), §3 (API calls) and SCORING.md "age-12 lookup" first.
You drive a real Chrome through the chrome-devtools MCP (already connected; the browser runs on the user's Mac,
so it is a normal consumer browser). Work only in this folder. Save screenshots into screenshots/ via take_screenshot
filePath (absolute path), named `NN-<state>.png` in order (01-hero.png, 02-primer.png, ...). Prefer a mobile viewport:
resize_page to 390x844 first (this is a paid-social mobile funnel); take ONE desktop (1280 wide) hero screenshot too.

Funnel URL (use exactly this, it is the real ad landing):
https://webpromo.kinedu.com/aq-assessment?vid=c1991816-d75d-4e46-a05d-cc40924c2ea8&paywall=trial3&offer=p79-t7&newusers=1&placement=assessment-landing&utm_source=assessment-landing&utm_medium=partner&ui=classic&capture=0

Rules: never enter an email (capture=0 should skip it; if an email screen appears anyway, screenshot it and STOP that run).
Never click buy/checkout/subscribe buttons or pass through to a payment page; capture the paywall URL only from the
link href or from the navigation that starts (then go back). Keep clicking minimal; every click fires their real analytics.

Run A — "typical" child:
1. Open URL. Screenshot hero. take_snapshot and record all copy on the hero.
2. Click Start. Screenshot every distinct screen (primer, birthdate screen incl. the prematurity toggle/slider, each area list,
   celebrate, report). Record the on-screen copy of each state in the markdown.
3. Birthdate: enter 2025-11-02 (returns ageMonths 12 — verify in the network response). gestational: leave "no / full term".
4. Answer the questions: use the served list from the network response (get_network_request on /api/assessment start);
   answer YES for items with rate >= 0.5 and NOT YET for the rest (this is the Phase 3 "C_age12_rate_ge50" profile,
   expected result: stage complete, devAge 14, well_ahead, areas P14 C16 L12 S16). Record for each area screen the exact
   question texts in order and compare with questions-by-age.md age 12 — report any difference.
5. On the report screen: screenshot the full page (fullPage true) and record every visible number/label and every blurred
   element. Compare to the /api/assessment result response (get_network_request): list which API values are shown,
   which are hidden, and confirm the blurred tiles are literal "88" (take_snapshot / evaluate_script to read DOM text).
6. Click one locked tile / the main unlock CTA ONCE: record where it goes (URL incl. query params — paywall=trial3, offer=p79-t7
   should appear). Screenshot the destination's first screen if it loaded, then navigate back. Do not interact there.
7. Network audit for the whole run: list_network_requests; record every call to /api/assessment, /api/track (event_name + screen
   fields of each), /api/lead, /api/send-reading, and any third-party trackers (facebook.com/tr, google-analytics, gtm, tiktok,
   etc.) with the event names/parameters they carried. Compare the /api/track sequence with STATIC-ANALYSIS §3.

Run B — extension screen: open the URL fresh (new_page), same birthdate, answer YES to everything. Expected: after the 4th
area a stage:"extension" response and an extra screen with 8 questions (2 per area). Screenshot it, record the 8 question
texts + ids from the network response, answer them all YES, screenshot the report (expect devAge 42+, capped). Stop there.

Write BROWSER-WALKTHROUGH.md: per-state table (state name from the state machine → screenshot → key copy → API calls fired),
the live-vs-static comparison (any discrepancy with STATIC-ANALYSIS.md / questions-by-age.md / SCORING.md predictions),
the full tracker/event inventory, the paywall URL, and a short "what the user sees vs what the API returned" section with
the exact JSON of the final result response saved to raw/api/browser/ (write the response bodies you read into files there).
Observed vs inferred, no fabrication. Finish with a 12-line summary.
