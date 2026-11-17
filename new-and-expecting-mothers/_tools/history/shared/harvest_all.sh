#!/usr/bin/env bash
# Window 2026-04-01 -> 2026-10-25 for every sub the five niche folders use. Resumable.
cd "$(dirname "$0")"
for s in sleeptrain toddlers pottytraining pregnant BabyBumps PregnancyUK Doulas NewParents beyondthebump beyondthebumpUK FirstTimeMom Mommit Parenting sahm workingmoms Montessori GentleParenting ScienceBasedParenting AttachmentParenting daddit postpartumprogress Postpartum_Depression; do
  python3 -I harvest_reddit.py "$s" 2026-04-01 2026-10-25 || echo "FAILED $s"
done
echo HARVEST DONE
