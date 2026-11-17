# Reopened oblique original communities — capture and reading boundary

**Current reading update — 2026-10-24:** all eligible kept material is now read. MoneySavingExpert totals **328 complete visible discussions / 4,423 posts**, plus **15 partial safety inspections / 82 records inspected or read**, with **231 later posts deliberately unread**. Its four reading waves produced **297 excerpts**. GeoBaby totals **183 complete visible captures / 1,422 posts**, including quoted context, with **111 excerpts** and 14 post-read exclusions. Three GeoBaby original-question contexts are uncertain; this is not a claim of complete live discussions.

The initial 29 MSE discussions received a full quoted-context supplement after extraction loss was found. Every later MSE and GeoBaby unit used corrected whole-context corpora. See [MSE completion 1](mse-completion-01.md), [2](mse-completion-02.md), [3](mse-completion-03.md), [GeoBaby](geobaby-deep-reading.md), [audit](../synthesis/audit.md), and [final coverage](../synthesis/coverage.json). The 29-read/496-unread counts below are a **historical handoff**, not current status.

## Historical first-reader handoff

Capture and reading are separate. The complete finite listing/thread capture contains526 discussions,871 discussion pages and6158 original visible posts. Only29 discussions/46pages/307posts were fully read in this branch;57 exact excerpts from24 discussions are frozen in `voice/oblique-deep-01.jsonl`. One acute-crisis discussion was excluded after inspecting its OP; its27posts/3pages are not full-read marketing material. The remaining496discussions/822pages/5824posts are explicitly unread. No prevalence or recommendation is inferred from unread captures.

## Public access and policies

Exact paths, statuses and evidence files are in `oblique-deep-access.json`. Untouched probe HTML, extracted text, robot bodies and response headers are in `_raw/oblique-deep/probes/`.

| Host | Observation and resulting scope |
|---|---|
| MoneySavingExpert forums | Robots200 explicitly permits ChatGPT-User. Canonical categories and discussions/pagination200. Search, RSS, profiles, private routes and discussion/comment endpoints avoided. Main-site terms route403 challenge, so terms are unknown, not asserted permissive. |
| DCUrbanMom | Robots/index/boards/FAQ200. FAQ footer says site content needs explicit permission for any purpose. No thread harvest or marketing excerpts. |
| City-Data | Robots200 with GPTBot Disallow:/; stopped. |
| ExpatForum | Robots200 explicitly disallows ChatGPT-User/GPTBot/OAI group; stopped. |
| TwinsStuff | Legacy forum host failed DNS; main homepage/robots200, ordinary /forums/403. No forum content harvested. |
| SingaporeExpats | Robots403 alone was unknown; normal public index also403 challenge. No bypass. |
| EnglishForum.ch | Connection failure; policy/content unknown. |
| Expat.com | Robots200 disallows the standard /forum/*.html topic path. No topic harvest. |
| ExpatWoman | Robots200 allows the ordinary forum route, with10second crawl delay; public forum403 challenge. No bypass. |
| GeoBaby / GeoClicks archive | Original host normally redirects to publisher's read-only archive. Original /robots.txt redirects to category HTML and is not treated as policy. Canonical archive robots200 has only content-signal explanatory comments, no restrictive directive/signal; terms200 standard user-content terms. Ordinary board and thread paths200. |

The archive terms retain authors' copyright; accessibility does not transfer copyright. Excerpts total at most25words per individual original non-Reddit post. No login, private group, captcha workaround, proxy, prohibited API or comment route was used.

## Finite scope, listings and local triage

MSE: every exposed listing page of MoneySaving Mums and MoneySaving Dads,68pages,1356unique discussion cards. Broad practical-pregnancy/baby/childcare title-and-excerpt filter produced480cards (375primary keyword matches,105adjacent). All480cards were manually triaged:343keeps,137drops. Other876listing records were not manually read as discussion sets. All343kept discussions were captured across every exposed canonical /pN page:620pages/4736posts. Each captured post count exactly equals its listing comment count plus the OP; zero discrepancies or capture failures. The kept discussions were created2012-10-18 through2026-08-06, latest visible reply2026-08-27. Historical purchases/rules are not current recommendations.

MSE triage01–02 belongs to reviews_media,03–04 to parent, saved separately as TSVs with explicit reasons. Clinical, crisis, minor or off-scope card exclusions remain card-only. A further reading-stage exclusion is logged in `post-triage-exclusions.tsv`; it does not silently change the original capture denominator.

GeoBaby archive: every listing page of Preparing for the Arrival (59pages/1161threads), Twins and Multiples (1page/14threads) and Pregnant with Multiples (3pages/49threads), totaling63pages/1224unique cards. A broad practical-title filter matched594. Before reading discussion outcomes, full-thread scope was declared as PreparingArrival created2010 onward, plus both whole multiples boards at all dates. This yields231title cards:183keeps and48clinical/promotional title exclusions. The363older matched PreparingArrival records are explicitly out of the declared full-thread window;630titles did not match the practical filter. All1224cards have a scope/decision row in `agent-geo-triage.tsv`.

All183GeoBaby keeps were captured:251pages/1422posts, zero capture failures. Kept thread dates span2004-09-22 through2021-06-09 (older dates from the entire multiples boards), latest visible reply2022-08-04. These are historical English-language Hong Kong/expat discussions, not present-day local availability, law, medical or price evidence. **No GeoBaby discussion has yet been manually read in this branch.**

## Immutable corpus and exact unread inventory

Raw-first pipeline: `_tools/harvest_oblique_mse.py`, `harvest_oblique_geo.py`, `harvest_oblique_threads.py`, `harvest_oblique_geo_threads.py`. Untouched responses are gzip HTML with HTTP sidecars; per-thread JSON preserves every extracted body plus body_with_quotes, dates, original identifiers and OP followups. Nothing was quoted from listing snippets. Display names are not added to selected evidence.

Frozen corpus:100MSE chunks/3333499bytes plus30GeoBaby chunks/856894bytes (4190393bytes combined). Files target35–45KB while retaining discussion/post boundaries; some are smaller because of whole-thread boundaries and initial batch tails. Index files record exact sizes/parts. The initial reading text omitted ALL blockquotes and signatures, an overbroad extraction choice. Every body_with_quotes with omitted material in the29read discussions has now been read in full using the48-post supplement; future parent completion-v2 packets include quoted context. The original HTML/JSON were preserved throughout. The initial index `reading_status` field records status at capture and is not updated by rewriting immutable files. The separate reading ledger is authoritative.

MSE001–009 were assigned to reviews_media. All permitted discussions in that allocation are now read, including every OP follow-up and page. MSE008 is mixed: three permitted discussions fully read, one acute-crisis discussion deliberately not read beyond eligibility inspection. The29read IDs and all496unread IDs have explicit manifests:

- `sources/oblique-deep-reading-ledger.jsonl`: nine allocation records with actual read counts, exclusions and quote IDs.
- `_raw/oblique-deep/read-thread-ids.txt`:29fully read discussion IDs.
- `_raw/oblique-deep/thread-reading-inventory.jsonl`: all526discussion statuses, original URLs, page/post counts and corpus filenames.
- `_raw/oblique-deep/unread-threads.jsonl`:496unread discussions,313MSE and183GeoBaby.
- `_raw/oblique-deep/unread-chunks.txt`:121fully unread chunk paths, MSE010–100 and GeoBaby001–030.
- `_raw/oblique-deep/post-triage-exclusions.tsv`: one safety exclusion, MSE6189328, not a completed full read.

The read allocation also contains several fully read but unquoted discussions: IVF-centered uncertainty, infant symptoms, developmental/attachment speculation and audience-stage ambiguity. Reading does not make those suitable marketing evidence. Complete practical reader notes, purchases versus free substitutes, and OP changes of mind are in `synthesis/reader-notes-oblique-deep.md`.

## Quote freeze and audit

`sources/oblique-deep-audit.json` records57quotes from24threads, voice-file SHA256, exact read/unread counts and zero strict failures. The copied verifier also reports57quotes/0failed. Strict audit normalizes whitespace only, preserves typography/case, checks the actual original-post body and frozen corpus, enforces25quoted words per individual post, and verifies the quoted discussion was fully read. Contexts are at most25words. Source class is forum_oblique; evidence kind original_thread_post. No selected excerpt is a medical/benefits/safety recommendation or evidence that a customized report was purchased.

Metadata vocabulary was corrected after parent audit, retaining the initial richer reader labels in original_reader_speaker/type. IDs, excerpts, source paths, URLs, dates and contexts are unchanged. `oblique-deep-metadata-corrections.json` records each grounded role/type correction and the final hash; both verifiers remain at zero failures.

Parent subsequent20-record audit changed odeep01-0031 type fromsuccess_story tobelief: purchased/startedtools is not itself demonstrated improvement. Literalquote/id/raw/context unchanged. Readerfreezehash remains historical; latest before/after hashes: `_raw/audit/deep-wave/parent-metadata-corrections.json`.

The48-post full-context supplement was completely read and audited after the blockquote-filter issue was identified. No interpretation of the57selected excerpts changes. One initially empty-looking post, MSE6094838/Comment_76875955, actually contains a personal weekday/babysitting statement entirely inside blockquote markup; reader notes correct that description. `oblique-deep-quoted-context-audit.json` records every supplemented post and completion. It adds context to the same29discussions/307posts, not48new posts or voices.
