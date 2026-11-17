# Funnel inventory

2026-10-24. Homepage → `/baby-development-guide/` → on-page order selection → account details → payment. Source HTML: `_raw/product/guide.html`; visible server text: `_raw/product/guide.txt`.

The saved HTML includes a plan-length selector, a born/expecting age state, digital format options, order additions, name and email fields, an optional tips subscription, a payment selector and an order summary. These are implementation observations; hidden markup is not proof that all branches work. No customer identity or payment has been submitted.

Initial real-browser tool attempt failed: Chrome DevTools connection to `127.0.0.1:9225` was refused. Browser access was subsequently restored using an isolated headless Chromium profile. Static sales content is saved verbatim in `sales-letter.md`.

## Rendered walkthrough

Sources: `_raw/product/browser-guide.json`, `browser-guide-snapshot.json`, `browser-step2.json`, `browser-step3.json`, `browser-checkout.json`. These are exact browser-tool responses containing rendered text; step 2 also preserves the DOM HTML. This is an observed sample path, not a test of payment or fulfillment.

1. The homepage points to the development guide. The order selector offers pregnant/already-born states.
2. Born branch: selected 2 months and 2 weeks. The observed selector accepts months 0–12 and extra weeks 0–3. No questions on observed skills, prematurity, tummy-time tolerance, household circumstances or medical concerns appeared on this path.
3. One month: $17.95, comparison $35.90; three months: $29.95, comparison $59.90; six months: $49.95, comparison $99.90. Currency was displayed as dollar signs on the English page; no geolocation conversion or tax checkout was tested. Three months was preselected. Sleep and speech guides each appeared as +$9.95 add-ons, comparison +$19.90; neither was selected.
4. Digital PDF included; printed or digital-plus-printed each displayed +$34.00 and free delivery. Selected digital. Shipping eligibility, delivery timing and print fulfillment were not verified.
5. Reached the email/payment selection screen showing card, PayPal, Google Pay and Apple Pay options. No real or invented customer identity was entered; no account, opt-in or payment was submitted. Provider availability, final charge and post-purchase report are unverified.

The rendered path demonstrates age-and-duration selection, not a validated assessment. The promised 48-hour turnaround is a seller statement, not an observed delivery time. A summer-sale message appeared on an October capture; the promotion's schedule and price history are unverified. Pregnant branch and every format/locale/payment branch remain untested.
