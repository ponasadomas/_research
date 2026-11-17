# CDC milestone benchmark: primary-source method notes

Retrieved 2026-11-03, using only `scripts/proxy_curl.sh`. These are current CDC pages explaining the February 2022 revision, not a frozen capture of the 2022 website.

## Findings

- CDC milestones are placed at checklist ages by which about 75% or more of children would be expected to exhibit the behavior. CDC describes the aim as making a missing milestone actionable rather than waiting when an average-age milestone is absent. The 75% threshold is a floor, not a claim that exactly 75% do each behavior. [CDC key points, items 4–5](https://www.cdc.gov/act-early/milestones/key-points.html); local capture: [methodology-key-points.html](methodology-key-points.html).
- CDC states that the revision used a published literature review conducted in 2019, together with the authors’ clinical judgment, to place evidence-informed milestones at well-child visit ages. Inclusion was limited by the available published evidence. Therefore these checklists are not a complete item-by-item empirical prevalence table. [CDC key points, items 4 and 6](https://www.cdc.gov/act-early/milestones/key-points.html).
- The revised checklists were released in February 2022. CDC contrasts the revision with 50% milestones, which leave half of children reasonably expected not yet to exhibit a behavior. It is safer to describe this as a shift from average-age/50% expectations to a 75%-or-more selection rule, without asserting that every pre-2022 item had a measured 50th-percentile placement. [CDC key points, items 5 and 8](https://www.cdc.gov/act-early/milestones/key-points.html).
- CDC explicitly says the checklists are communication tools, are not developmental guidelines or standards, and must not be used as screening or diagnostic tools. [CDC key points, items 1–3](https://www.cdc.gov/act-early/milestones/key-points.html). CDC also states its resources do not substitute for standardized, validated screening tools. [CDC milestone index](https://www.cdc.gov/act-early/milestones/index.html).
- The current overview independently repeats the 75%-or-more expectation and links the evidence paper. [CDC about LTSAE](https://www.cdc.gov/act-early/about/index.html). CDC distinguishes everyday developmental monitoring from formal validated developmental screening. [CDC monitoring and screening](https://www.cdc.gov/act-early/about/developmental-monitoring-and-screening.html).

## Implications for this comparison (analytical inferences)

- A well-matched Kinedu share below 75% at the CDC age is lower than the CDC checklist’s expected floor, conditional on interpreting Kinedu `rate` as a share and on comparable populations and wording. The calculation alone cannot establish misrepresentation or an item’s true population prevalence.
- A Kinedu share at or above 75% is compatible with CDC’s placement. CDC does not supply an exact percentage against which to estimate Kinedu inflation.
- A share above 95% **at** the CDC age alone does not demonstrate that most children attained the skill **before** the CDC age, or that Kinedu exaggerates population prevalence. It is a user-requested high-share flag. Actual earlier-month observations may support a claim that Kinedu assigns high shares at those earlier months, but CDC provides no earlier-month curve to validate them.
- It is not required that a share before a listed CDC age be below 75%. Checklist ages are discrete, and a milestone can become widespread between checklist ages; the CDC placement does not identify its exact 75th-percentile crossing.
- Linear interpolation supplies an estimate conditional on local linearity, not another observation. A one-sided nearby observation does not support interpolation or a numerical verdict at an unobserved CDC age.
- Semantic matching matters especially for support, number of words, task complexity, and conjunctions. A harder Kinedu behavior can have a lower share without contradicting the CDC item.

## Fetch provenance

All response bodies obtained are saved in this directory; response header files share their basename. The failed PubMed connection produced no response body; the status and failure are recorded in `methodology-fetches.json`. The AAP article is linked by CDC but its 403 response is not used as evidence. A guessed CDC Stacks locator returned 404 and is not used as evidence.
