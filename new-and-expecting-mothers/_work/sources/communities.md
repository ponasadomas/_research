# Community audience evidence

Captured and read 2026-10-24. **155 verified excerpts from 61 indexed thread units.** This is discovery evidence from search-index extracts, not the playbook's requested date-bounded community harvest. There are **0 complete original-thread reads**. All 62 kept *available extract units* were read in full; one produced no suitable quote. Do not promote this source into a representative audience study or a complete Reddit dataset.

The owner selected English-speaking markets as likely initial launch markets. US/UK/CA/AU are not measured separately here. Country is unknown in 153 quote records; one commenter explicitly describes Australia and one describes France. Country-specific community membership is stored separately as `community_market`; it is not proof of residence. France is contrast evidence, not part of the proposed English-market launch.

## How the material was obtained

1. Probed public robots files, direct Reddit JSON, and Arctic Shift. Saved every response/status to `_raw/communities/probes/` and `sources/community-access.jsonl`.
2. Direct Reddit returned HTTP 403. Reddit robots disallows all paths. Arctic Shift returned HTTP 403 with Cloudflare error code 1010. No alternate host, proxy, cookie, login, user-agent workaround or captcha was used.
3. Forum probes either explicitly prohibited automated/AI collection or failed. No forum board was harvested. See access table below.
4. As the written brief permits, used ordinary web search as a **clearly limited fallback**. Ten saved tool responses cover fourteen queries, retrieving 100 indexed Reddit result occurrences. These are search-selected and often partial or missing the opening post.
5. Deduped the same Reddit thread id, retaining the longest available returned extract: 92 unique units, preserved individually in `_raw/communities/corpus-index/001.txt` through `092.txt`. Original response files remain untouched. Two cross-posted discussions were also set aside during card triage.
6. Read all 92 cards. Retained 62 units for cross-segment discovery, dropped 30 with a written reason. Frozen triage: `_raw/communities/triage-01.tsv`, `triage-02.tsv`. Frozen index: `discovery-index.jsonl`, `discovery-index-02.jsonl`.
7. Read all nine frozen chunks in `_raw/communities/reading-chunks/` in full. Every kept extract appears in those chunks. Quotes cite individual unit files, which will not be rebuilt.
8. Selected 155 excerpts, preserving exact spelling and grammar. Verified against raw with `verify_quotes.py`. Dates come from visible post/comment timestamps; absent timestamps stay blank. No usernames in quotes or context.

This collection spans visible quote dates **2019-07-09 through 2026-10-21**, plus unknown dates. It is not limited to the attempted archive window 2026-04-24 through 2026-10-24. Older app and price experiences are historical accounts, not current product specifications. Query wording deliberately sought problems, value objections and planning examples, so the sample is biased toward those topics.

## Ledger

`matched` is not a locally filtered bulk count: queries selected the initial results. `read` below means the entire **available index unit**, never the original thread. Counts describe selected evidence, not people or prevalence.

| Source | Unique index units saved | Cards triaged | Kept | Extracts read | Original threads read | Quotes |
|---|---:|---:|---:|---:|---:|---:|
| BabyBumps | 7 | 7 | 4 | 4 | 0 | 9 |
| BabyBumpsCanada | 2 | 2 | 2 | 2 | 0 | 5 |
| BabyBumpsandBeyondAu | 2 | 2 | 2 | 2 | 0 | 8 |
| BabyLedWeaning | 4 | 4 | 2 | 2 | 0 | 8 |
| BeyondTheBumpUK | 2 | 2 | 2 | 2 | 0 | 6 |
| ExclusivelyPumping | 12 | 12 | 8 | 8 | 0 | 17 |
| HuckleberryParents | 1 | 1 | 1 | 1 | 0 | 3 |
| MomsWorkingFromHome | 1 | 1 | 1 | 1 | 0 | 2 |
| Nanny | 1 | 1 | 1 | 1 | 0 | 3 |
| NewParents | 29 | 29 | 19 | 19 | 0 | 50 |
| November2026Bumpers | 1 | 1 | 1 | 1 | 0 | 1 |
| November25babybump | 1 | 1 | 1 | 1 | 0 | 2 |
| Postpartum_Depression | 1 | 1 | 0 | 0 | 0 | 0 |
| PregnancyUK | 1 | 1 | 1 | 1 | 0 | 1 |
| Samesexparents | 1 | 1 | 1 | 1 | 0 | 4 |
| ScienceBasedParenting | 1 | 1 | 1 | 1 | 0 | 3 |
| breastfeeding | 1 | 1 | 1 | 1 | 0 | 3 |
| fitpregnancy | 2 | 2 | 2 | 2 | 0 | 4 |
| moderatelygranolamoms | 1 | 1 | 1 | 1 | 0 | 4 |
| newborns | 2 | 2 | 2 | 2 | 0 | 3 |
| pregnant | 10 | 10 | 3 | 3 | 0 | 5 |
| workingmoms | 9 | 9 | 6 | 6 | 0 | 14 |
| **Total** | **92** | **92** | **62** | **62** | **0** | **155** |

Machine-readable ledger: `sources/communities-ledger.json`. The entire audience file is one source class, `community_index`; different subreddits do not satisfy the requirement for multiple source classes.

## Access and exclusions

| URL or source | Observed status | Result |
|---|---|---|
| `https://www.reddit.com/robots.txt` | 200 | `User-agent: *`, `Disallow: /`; no automated bulk collection |
| `https://www.reddit.com/r/NewParents/new.json?limit=100` | 403 | No posts downloaded from JSON |
| `https://arctic-shift.photon-reddit.com/robots.txt` | 403 | Access denied; raw body saved |
| Arctic Shift NewParents API, after 2026-04-24, before 2026-10-24 | 403 | Body: error code 1010; no archive harvest |
| `https://community.babycenter.com/robots.txt` | 200 | Explicitly prohibits automated scraping, AI databases and commercial use; not harvested |
| `https://community.whattoexpect.com/robots.txt` | 200 | Explicit automated collection/commercial-use prohibition; not harvested |
| `https://babyandbump.momtastic.com/robots.txt` | 200 | GPTBot prohibited; reference-only content signal; not harvested |
| `https://pregnancyforum.momtastic.com/robots.txt` | 200 | Same restrictive policy; not harvested |
| `https://www.netmums.com/robots.txt` | 403 | Policy inaccessible; not harvested |
| `https://www.mumsnet.com/robots.txt` | 403 | Policy inaccessible; not harvested |
| `https://www.mothering.com/robots.txt` | 200 | Explicit AI-bot prohibition; not harvested |
| `https://healthunlocked.com/robots.txt` | 403 | Access-block page; not harvested |
| `https://parenting.stackexchange.com/robots.txt` | 418 | Body disallows all paths and reserves search/AI-training rights |
| Stack Exchange public Parenting questions API, date-bounded probe | 200 | 17 question records, `has_more=false`; saved as a probe but not used as audience corpus because site policy is restrictive and the material is mostly older-child questions |
| `https://api.stackexchange.com/robots.txt` | 400 | API returns no-method error; does not resolve the site's policy restriction |

Access notes contain 15 saved probe responses. Raw Reddit forbidden HTML is a block page, not a 190KB post corpus. The Stack Exchange probe is `_raw/communities/probes/stackexchange-api.txt`; its 17 question bodies were **not fully read**, matched, quoted or included in the ledger. No private Facebook/Discord groups, direct messages, accounts or owner credentials were available or used.

## What has and has not been read

All 62 kept extract units in all nine `audience-index-NN.txt` chunks were read completely. **No kept extract chunk remains unread.** Individual reading status and exact paths for all 92 units are in `sources/community-reading-manifest.md`.

The 30 dropped units were card-triaged only and remain unread in full: `001`, `002`, `004`, `005`, `008`, `009`, `011`, `012`, `016`, `021`, `022`, `023`, `030`, `033`, `037`, `039`, `042`, `046`, `047`, `049`, `050`, `051`, `069`, `072`, `075`, `077`, `079`, `082`, `086`, `087`, each at `_raw/communities/corpus-index/<NNN>.txt`. Do not read unsafe/excluded units for marketing just to increase volume.

The original linked threads remain unread as originals, even when an extract looks complete. Missing OP follow-up, deleted material, context, comment ordering and authorship are unresolved. Search-index citations link to thread permalinks because comment permalinks were not returned. Multiple excerpts can come from one person; unique people cannot be counted.

## Language and balance

Jargon in this corpus: FTM = first-time mother; SAHM = stay-at-home mother; LO = little one; PP/WPP = postpartum/weeks postpartum; EBF/EP = exclusively breastfeeding/exclusively pumping; BLW = baby-led weaning; MOTN = middle of the night; ppd = pumps per day when used in pumping context, **not** automatically postpartum depression; LC = lactation consultant; NK = nanny kid. SweetSpot refers to an app feature, not a clinical measurement. A quote saying an app helped does not prove it changed sleep or development.

155 selected quotes include 109 `parent_unspecified`, 13 `new_mother`, 9 `gave_up_parent`, 7 `advisor`, 6 `partner`, 3 `skeptic`, 3 `expecting_mother`, 2 `experienced_mother`, 2 `relative_caregiver`, 1 `reviewer`. Gender is not inferred from breastfeeding, pregnancy, a husband or subreddit membership. These conservative labels explain the large unspecified category. Professionals, verified purchasers, recovered clinical cases and toddlers have no deliberate coverage. Prematurity/corrected age, twins, fathers, caregivers and country-specific constraints remain thin.

## Verification and continuation

`audience-01.jsonl: 155 quotes, 0 failed`

`TOTAL 155 quotes, 0 failed`

A safety regex found no quote text matching self-harm, abuse, pregnancy loss, infant death, choking or suffocation terms. Readers separately excluded medical prescriptions, unsafe sleep setups, pump-cleaning hacks, formula shaming, diagnostic claims and acute distress. Raw sources still contain such material; a clean quote bank does not certify the source advice. Some positive app replies offer referral codes; source notes and contexts preserve that bias. A billing allegation is marked unverified.

Continue with consented adult interviews or permitted exports and a new written brief/new quote prefix, preserving this corpus. To close the playbook's bulk requirement, obtain an authorized dated archive/export rather than relabeling these search results. Reading the 30 dropped extracts would take roughly one reader × three 26KB chunks, but it is not the useful next step: most were excluded for duplication, partial openings, clinical focus or poor fit. The missing full originals are not saved on disk and cannot be costed as completed reading work.
