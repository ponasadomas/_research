#!/usr/bin/env bash
# Send one findings-section writer per pattern, each merging that pattern's digests. Safe to
# stop; run the same command again to go on (patterns whose section passes are skipped).
#   _tools/run_sections.sh <niche> <work dir> <digest work dir> <evidence dir> <out dir> <quotes dir> <model> <effort> <writers at a time>
# (run from ~/GitHub/_research, in a terminal a person can watch)
# - Model and effort have no default: they are what the owner agreed to for this run.
# - <work dir> holds brief-section.md ({P} {PP} {PNAME} {DIGESTS} {EVARGS} {YES} {NEAR} are
#   filled in); <digest work dir> holds shares.tsv; sections go to <out dir>/pattern-PP.md.
# - The first writer of each group is shown live; the others write to <work dir>/logs/.
# - Each group is checked and committed. A section that fails is redone whole, once.
# - It stops by itself when a writer ends within 3 minutes with nothing written.
set -u
[ $# -ge 9 ] || { sed -n '2,5p' "$0"; exit 1; }
NICHE="$1"; W="${2%/}"; DW="${3%/}"; EV="${4%/}"; OUT="${5%/}"; Q="${6%/}"; MODEL="$7"; EFFORT="$8"; K="$9"
CODEX="${CODEX_BIN:-codex}"; LOGS="$W/logs"; mkdir -p "$LOGS" "$OUT"; CHECK="$HOME/GitHub/_home/.agents/skills/write-findings/check_findings.py"
echo "$(date "+%Y-%m-%d %H:%M") start | codex $($CODEX --version 2>/dev/null | tail -1) | model $MODEL | effort $EFFORT | $K at a time" >> "$W/sent.txt"
sum() { awk -F'\t' -v p="$1" -v c="$2" '$2==p{s+=$c} END{print s+0}' "$DW/shares.tsv"; }
pname() { awk -F'\t' -v p="$1" '$2==p{print $3; exit}' "$DW/shares.tsv"; }
digests() { awk -F'\t' -v p="$1" -v e="$EV" '$2==p{printf "%s%s/digest-%s.md", s, e, $1; s=" "}' "$DW/shares.tsv"; }
evargs() { for d in $(digests "$1"); do printf -- "--evidence %s " "$d"; done; }
pp() { printf "%02d" "$1"; }
ok() { python3 -I "$CHECK" "$OUT/pattern-$(pp "$1").md" --quotes "$Q" $(evargs "$1") && python3 -I _tools/verify_section.py "$OUT/pattern-$(pp "$1").md" "$(sum "$1" 4)" "$(sum "$1" 5)"; }
run() { sed -e "s/{PP}/$(pp "$1")/g" -e "s/{P}/$1/g" -e "s|{PNAME}|$(pname "$1")|g" -e "s|{DIGESTS}|$(digests "$1")|g" -e "s|{EVARGS}|$(evargs "$1")|g" -e "s/{YES}/$(sum "$1" 4)/g" -e "s/{NEAR}/$(sum "$1" 5)/g" "$W/brief-section.md" | $CODEX exec -m "$MODEL" -c model_reasoning_effort="\"$EFFORT\"" -s workspace-write -C "$PWD" -o "$LOGS/section-$1.last.md" - 2>&1; }
timed() { local t0=$(date +%s); if [ "$2" = live ]; then run "$1" | tee "$LOGS/section-$1.log"; else run "$1" > "$LOGS/section-$1.log"; fi; echo $(( $(date +%s) - t0 )) > "$LOGS/section-$1.secs"; }
stop() { echo; echo "STOPPED $(date "+%Y-%m-%d %H:%M"): $1"; echo "Everything finished before this is committed. Run the same command again to go on."; echo "$(date "+%Y-%m-%d %H:%M") stopped: $1" >> "$W/sent.txt"; exit 2; }
dead() { [ "$(cat "$LOGS/section-$1.secs" 2>/dev/null || echo 0)" -lt 180 ] && [ ! -s "$OUT/pattern-$(pp "$1").md" ]; }
TODO=""; for p in $(tail -n +2 "$DW/shares.tsv" | cut -f2 | sort -n | uniq); do ok "$p" >/dev/null 2>&1 || TODO="$TODO $p"; done
SENT=0; FAILED=""
set -- $TODO
while [ $# -gt 0 ]; do
  GROUP=""; i=0; while [ $# -gt 0 ] && [ $i -lt "$K" ]; do GROUP="$GROUP $1"; shift; i=$((i + 1)); done
  echo; echo "=== sending section writers for patterns$GROUP ($(date +%H:%M)); shown live: pattern $(echo $GROUP | cut -d' ' -f1) ==="
  FIRST=1; for p in $GROUP; do if [ $FIRST = 1 ]; then LIVE=$p; FIRST=0; else timed "$p" log & fi; done
  timed "$LIVE" live; echo "=== writer $LIVE has stopped ($(date +%H:%M)); waiting for the rest of$GROUP ==="; wait
  SENT=$((SENT + $(echo $GROUP | wc -w)))
  for p in $GROUP; do
    if ! ok "$p"; then
      if dead "$p"; then tail -5 "$LOGS/section-$p.log"; stop "writer $p ended within 3 minutes with nothing written (usage run out, or Codex could not start)"; fi
      echo "redoing section $p whole ($(date +%H:%M))"; mkdir -p "$LOGS/failed-first-try"; mv -f "$OUT/pattern-$(pp "$p").md" "$LOGS/failed-first-try/" 2>/dev/null
      timed "$p" log; SENT=$((SENT + 1))
      if ! ok "$p"; then
        dead "$p" && stop "writer $p ended within 3 minutes with nothing written (usage run out, or Codex could not start)"
        FAILED="$FAILED $p"; mkdir -p "$LOGS/failed-twice"; mv -f "$OUT/pattern-$(pp "$p").md" "$LOGS/failed-twice/" 2>/dev/null
      fi
    fi
  done
  if [ -z "${NO_COMMIT:-}" ]; then git add "$W" "$OUT" >/dev/null 2>&1 && git commit -q -m "$NICHE: findings sections, patterns$GROUP" && echo "committed sections$GROUP ($(date +%H:%M))"; fi
done
echo; echo "SECTIONS-DONE $(date "+%Y-%m-%d %H:%M") writers sent $SENT, failed twice=[${FAILED# }]"; echo "$(date "+%Y-%m-%d %H:%M") done | sent $SENT | failed twice [${FAILED# }]" >> "$W/sent.txt"
