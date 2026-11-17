# Phase 1 — Static analysis of the Kinedu "AQ assessment" quiz front-end

You are analysing a public marketing quiz at https://webpromo.kinedu.com/aq-assessment (a Next.js app).
Work ONLY inside this folder. Do NOT open a browser, do NOT call the live site. Everything you need is in raw/js/:
- raw/js/aq-assessment.html — the served HTML
- raw/js/page-5f182d70f1f24a3d.js — the page chunk (the quiz itself)
- raw/js/562-f8a0c4482aa81c7b.js — shared chunk (likely contains helpers; check whether it has quiz data)
- raw/js/3-0b860339fe270cd0.js, raw/js/layout-*.js — small chunks

Goal: a precise, evidence-backed description of how the quiz UI works, so we can later tell whether
there is one question tree or many, whether questions depend on earlier answers, and how the report is built.

Steps:
1. Beautify the bundles into raw/js/beautified/ (use `npx -y js-beautify` or python; keep originals untouched).
2. Read the page chunk thoroughly. Document in STATIC-ANALYSIS.md (in this folder):
   a. URL parameters read by the code and what each does (ui / v / paywall / offer / capture / lang / env / test_id / newusers / placement / vid / utm_* / fbclid / gclid). Quote the code line for each.
   b. UI variants: which values of ui/v select which React component / layout (we saw "assessment" default, "classic", "list", "skills"). For each variant: list the screen states (the `s:` state machine values, e.g. "hero", "age_range", "celebrate", ...) and the transitions between them, as a mermaid stateDiagram.
   c. Every call to /api/assessment, /api/lead, /api/send-reading, /api/track: the full request body fields, where in the flow it fires, and every response field the client reads. Specifically document the `action` values ("start", "result", any others) and all `stage` values the client checks and what it does with each.
   d. Question rendering: how the client builds the flat list of questions from `sections`, `calibration`, `anchor`, `items`. Is the order fixed? Is there ANY client-side skip/branch logic (e.g. a question shown only if a previous answer was X)? Quote the code. What answer values exist (we saw `{id, y}` — is y boolean, 0/1, scale?).
   e. The `result` call: when does it fire (debounce 800ms while answering?), with `extended:true` — what does extended mean, and what does the client do with `basic` and `skills` on the report screen. Document exactly what is rendered in the report (fields, labels, charts, percentages) and which of those are computed client-side vs taken from the API verbatim. Quote code.
   f. Email capture: in which variant / state is the email asked, what `capture=0` does, and whether the report is reachable without an email in each variant.
   g. Any hard-coded content that looks like question text, section names, skill names, score thresholds, copy for the report ("your baby is ahead/on track/..."), or percentile numbers — list them all with the exact strings. Note the localisation table (en/es/pt) if present.
   h. Anything suspicious about the scoring being fake/cosmetic: random numbers, fixed percentages, Math.random, animation-only counters, hard-coded "87%"-style figures.
3. Also list in STATIC-ANALYSIS.md the exact `fetch` body you would send with curl to reproduce `action:"start"` and `action:"result"`, including any required headers/cookies you can infer (we will use that in the next phase).

Rules: quote code with line numbers from raw/js/beautified/. Separate "observed in code" from "inferred". Be exhaustive on (c), (d), (e) — those decide the whole investigation. Finish by printing a 15-line summary of the key findings.
