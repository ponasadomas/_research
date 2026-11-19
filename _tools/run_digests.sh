#!/usr/bin/env bash
# Send digest readers over the shares of an evidence folder. Safe to stop; run the same
# command again to go on (shares whose digest already passes the check are skipped).
#   _tools/run_digests.sh <niche> <work dir> <evidence dir> <model> <effort> <readers at a time>
# (run from ~/GitHub/_research, in a terminal a person can watch)
# - Model and effort have no default: they are what the owner agreed to for this run.
# - <work dir> holds brief-digest.md ({NN} {P} {PNAME} {SHARE} are filled in), share-NN.md
#   and shares.tsv, made by make_digest_shares.py.
# - The first reader of each group is shown live; the others write to <work dir>/logs/.
# - Each group is checked and committed. A digest that fails is redone whole, once.
# - It stops by itself when a reader ends within 3 minutes with nothing written (usage has
#   run out, or Codex cannot start).
set -u
[ $# -ge 6 ] || { sed -n '2,5p' "$0"; exit 1; }
NICHE="$1"; W="${2%/}"; EV="${3%/}"; MODEL="$4"; EFFORT="$5"; K="$6"
CODEX="${CODEX_BIN:-codex}"; LOGS="$W/logs"; mkdir -p "$LOGS"
echo "$(date "+%Y-%m-%d %H:%M") start | codex $($CODEX --version 2>/dev/null | tail -1) | model $MODEL | effort $EFFORT | $K at a time" >> "$W/sent.txt"
ok() { python3 -I _tools/verify_digest.py "$W" "$EV" "$1"; }
field() { awk -F'\t' -v n="$1" -v c="$2" '$1==n{print $c}' "$W/shares.tsv"; }
run() { sed -e "s/{NN}/$1/g" -e "s/{P}/$(field "$1" 2)/g" -e "s|{PNAME}|$(field "$1" 3)|g" -e "s|{SHARE}|$W/share-$1.md|g" "$W/brief-digest.md" | $CODEX exec -m "$MODEL" -c model_reasoning_effort="\"$EFFORT\"" -s workspace-write -C "$PWD" -o "$LOGS/digest-$1.last.md" - 2>&1; }
timed() { local t0=$(date +%s); if [ "$2" = live ]; then run "$1" | tee "$LOGS/digest-$1.log"; else run "$1" > "$LOGS/digest-$1.log"; fi; echo $(( $(date +%s) - t0 )) > "$LOGS/digest-$1.secs"; }
stop() { echo; echo "STOPPED $(date "+%Y-%m-%d %H:%M"): $1"; echo "Everything finished before this is committed. Run the same command again to go on."; echo "$(date "+%Y-%m-%d %H:%M") stopped: $1" >> "$W/sent.txt"; exit 2; }
dead() { [ "$(cat "$LOGS/digest-$1.secs" 2>/dev/null || echo 0)" -lt 180 ] && [ ! -s "$EV/digest-$1.md" ]; }
TODO=""; for nn in $(tail -n +2 "$W/shares.tsv" | cut -f1); do ok "$nn" >/dev/null 2>&1 || TODO="$TODO $nn"; done
SENT=0; FAILED=""
set -- $TODO
while [ $# -gt 0 ]; do
  GROUP=""; i=0; while [ $# -gt 0 ] && [ $i -lt "$K" ]; do GROUP="$GROUP $1"; shift; i=$((i + 1)); done
  echo; echo "=== sending digest readers$GROUP ($(date +%H:%M)); shown live: reader $(echo $GROUP | cut -d' ' -f1) ==="
  FIRST=1; for nn in $GROUP; do if [ $FIRST = 1 ]; then LIVE=$nn; FIRST=0; else timed "$nn" log & fi; done
  timed "$LIVE" live; echo "=== reader $LIVE has stopped ($(date +%H:%M)); waiting for the rest of$GROUP ==="; wait
  SENT=$((SENT + $(echo $GROUP | wc -w)))
  for nn in $GROUP; do
    if ! ok "$nn"; then
      if dead "$nn"; then tail -5 "$LOGS/digest-$nn.log"; stop "reader $nn ended within 3 minutes with nothing written (usage run out, or Codex could not start)"; fi
      echo "redoing digest $nn whole ($(date +%H:%M))"; mkdir -p "$LOGS/failed-first-try"; mv -f "$EV/digest-$nn.md" "$LOGS/failed-first-try/" 2>/dev/null
      timed "$nn" log; SENT=$((SENT + 1))
      if ! ok "$nn"; then
        dead "$nn" && stop "reader $nn ended within 3 minutes with nothing written (usage run out, or Codex could not start)"
        FAILED="$FAILED $nn"; mkdir -p "$LOGS/failed-twice"; mv -f "$EV/digest-$nn.md" "$LOGS/failed-twice/" 2>/dev/null
      fi
    fi
  done
  if [ -z "${NO_COMMIT:-}" ]; then git add "$W" $(ls "$EV"/digest-*.md 2>/dev/null) >/dev/null 2>&1 && git commit -q -m "$NICHE: digests$GROUP" && echo "committed digests$GROUP ($(date +%H:%M))"; fi
done
echo; echo "DIGESTS-DONE $(date "+%Y-%m-%d %H:%M") readers sent $SENT, failed twice=[${FAILED# }]"; echo "$(date "+%Y-%m-%d %H:%M") done | sent $SENT | failed twice [${FAILED# }]" >> "$W/sent.txt"
