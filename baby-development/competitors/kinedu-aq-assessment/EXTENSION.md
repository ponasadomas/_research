# Extension ("Going further") trigger — measured for every age (2026-11-03)

Probe: for ages 0–41, `action:result, extended:false` with K = capped_from and K = capped_from − 1 (ascending-rate order,
served list of that age), via the SOCKS proxy, 2 s pacing. 84 calls, all HTTP 200. Script: `scripts/probe_extension_threshold.py`,
raw: `raw/api/extension-probe/`.

Result: **the extension stage starts exactly at the K where the headline result first becomes `capped` (scoring-table.csv,
"Capped from"), at all 42 ages, no exceptions.** One Yes fewer → `stage:complete`. Ages 42–48 never cap and never extend.
The first extension batch per age (8 items, 2 per area) is in `raw/api/result_age{AA}_all_yes_numeric.json` (Phase 2).
