# YouTube — discovery metadata and unmet top-200 target

Captured 2026-10-24. **Four on-topic instructional video metadata rows were retained from one initial five-result probe. There is no top-200 inventory and no comment corpus.** The videos themselves, their transcripts and their comments were not watched/read. Metadata is discovery evidence, not validation of medical guidance, purchase demand or advertiser profitability.

## What was attempted

Executed query: `ytsearch5:tummy time baby hates tummy time`, with flat-playlist metadata printed by yt-dlp. The process exited 0; individual HTTP status codes were not captured. Untouched output: `_raw/youtube/probe-search.tsv`; diagnostic output: `_raw/youtube/probe-search.stderr.txt`. Five returned rows were read in full as metadata units. One personal baby clip was excluded from the instructional shortlist.

The probe preceded reading `https://www.youtube.com/robots.txt`. That policy returned HTTP 200 and disallows `/results`, `/youtubei/`, `/comment` and several other search/API/continuation paths for general crawlers. The saved policy is `_raw/youtube/robots.txt`. Further yt-dlp search/comment collection was therefore not run. No bot wall, login, captcha or alternate-host workaround was attempted. Copied SYD video/comment scripts remain available but were not run as a bulk pipeline.

## Observed view ranking within this four-video discovery set

| Rank | Observed views | Title returned by yt-dlp | Channel | Video |
|---|---:|---|---|---|
| 1 | 867,897 | Baby Hates Tummy Time? Try These Tummy Time Positions Instead!!(Tummy Time How To) | Emma Hubbard | [Watch page](https://www.youtube.com/watch?v=377j05F4edY) |
| 2 | 149,449 | This Is Why Your Baby Hates Tummy Time (And How To Fix It) | Emma Hubbard | [Watch page](https://www.youtube.com/watch?v=L4j34KDdx0Y) |
| 3 | 59,864 | 4 Reasons Your Baby HATES Tummy Time | Nekole Amber | [Watch page](https://www.youtube.com/watch?v=pDC7ifNMQbk) |
| 4 | 440 | Baby Hates Tummy Time? A Pediatric Therapist Explains What to Do | Rookie Parent Roadmap | [Watch page](https://www.youtube.com/watch?v=R5JJPE60SQI) |

Excluded row: video `llJbIyyAOe0`, title “Josephine Hates Tummy Time”, 99,048 observed views, channel chefelf; a personal short clip rather than an instructional result. This is a classification by title/duration, not a full-video review. Upload dates were not returned by this flat probe and are unknown here. View counts are only those observed during collection and are not a current live ranking.

## What is missing and how to continue

The reopened pass also saved an ordinary public Emma Hubbard channel page sorted by popularity: `_raw/media-deep/youtube-emma-popular.txt`, with untouched HTML and initial JSON alongside it. The initial JSON contains 30 `lockupViewModel` objects. This is a captured single-channel probe, not 30 fully reviewed videos, an independent cross-channel ranking, or a comment corpus. No continuation or bulk comment request followed.

The playbook's 200 most-viewed on-target videos is **unmet**. The following source-map topics were planned but not searched here: baby wake-window routines; developmental play; first solids; allergen introduction; preparation and grocery planning; return-to-work pumping; postpartum support; pregnancy exercise; partner/caregiver handoffs. No query history is claimed for them. The source map describes intent, not execution.

Continue only through an authorized/permitted discovery route, such as official access to the YouTube Data API, owner-provided exports or manual public-page review within site rules. Then save original metadata, deduplicate video ids, disclose the search pool and rank observed views without calling it an exhaustive census. Comments need their own raw saves, full-read ledger, safety exclusions and quote verification. No API credentials or owner exports were supplied for this session.

## Permitted direct-page follow-up

`sources/reviews-followups.md` records an HTTP 200 public `/watch?v=377j05F4edY` capture. Its metadata repeats the observed 867,897 views and gives upload date 2021-01-07. This is one already listed video, not a fifth new instructional item. No original comment bodies appeared in the returned HTML; the video, transcript, full description and remaining player data were not watched/read. No prohibited continuation route was used. The top-200/comment gaps remain.
