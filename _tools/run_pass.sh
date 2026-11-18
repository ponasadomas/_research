#!/usr/bin/env bash
# Run a whole read-and-sort pass, block by block. Safe to stop; run the same command again to
# go on where it stopped (readers whose output already passes the check are skipped).
#   _tools/run_pass.sh <niche> <dir> <quotes dir> <prefix> <highest pattern> <model> <effort> \
#                      <posts per reader> <readers at a time> <seed> [most readers to send]
# (run from ~/GitHub/_research, in a terminal a person can watch)
# - Model and effort have no default: they are what the owner agreed to for this run.
# - <dir> holds sample.tsv and brief.md ({NN} {PREFIX} {DIR} {QUOTES} are filled in).
# - BLOCKS_AT_A_TIME=n in the environment runs n blocks side by side (default 1).
# - WITHOUT_REPLIES_OK=1 reads a post without its poster's replies when those are not
#   fetched yet, instead of waiting for them.
# - Each block is checked and committed when it finishes. The first reader of each block
#   is shown live; the others write to <dir>/logs/.
# - It stops by itself when: a reader dies within 3 minutes with nothing written (usage has
#   run out, or Codex cannot start); three readers have failed the check twice; the replies
#   for the next block are not fetched and nothing is fetching them; or the cap is reached.
set -u
[ $# -ge 10 ] || { sed -n '2,6p' "$0"; exit 1; }
NICHE="$1"; D="${2%/}"; Q="${3%/}"; PREFIX="$4"; TOP="$5"; MODEL="$6"; EFFORT="$7"; PER="$8"; K="$9"; SEED="${10}"; CAP="${11:-100000}"
CODEX="${CODEX_BIN:-codex}"; LOGS="$D/logs"; mkdir -p "$LOGS" "$Q"
echo "$(date "+%Y-%m-%d %H:%M") start | codex $($CODEX --version 2>/dev/null | tail -1) | model $MODEL | effort $EFFORT | $PER posts per reader | $K at a time | cap $CAP readers" >> "$D/sent.txt"
ok() { python3 -I _tools/verify_pass.py "$D" "$Q" "$PREFIX" "$1" "$TOP"; }
run() { sed -e "s/{NN}/$1/g" -e "s/{PREFIX}/$PREFIX/g" -e "s|{DIR}|$D|g" -e "s|{QUOTES}|$Q|g" "$D/brief.md" | $CODEX exec -m "$MODEL" -c model_reasoning_effort="\"$EFFORT\"" -s workspace-write -C "$PWD" -o "$LOGS/$PREFIX$1.last.md" - 2>&1; }
timed() { local t0=$(date +%s); if [ "$2" = live ]; then run "$1" | tee "$LOGS/$PREFIX$1.log"; else run "$1" > "$LOGS/$PREFIX$1.log"; fi; echo $(( $(date +%s) - t0 )) > "$LOGS/$PREFIX$1.secs"; }
stop() { echo; echo "STOPPED $(date "+%Y-%m-%d %H:%M"): $1"; echo "Everything finished before this is committed. Run the same command again to go on."; echo "$(date "+%Y-%m-%d %H:%M") stopped: $1" >> "$D/sent.txt"; exit 2; }
SENT=0; FAILED=""; NFAILED=0; B=0; PAR="${BLOCKS_AT_A_TIME:-1}"
while :; do
  GROUP=""; TODO=""; WAITING=0
  while [ "$(echo $GROUP | wc -w)" -lt "$PAR" ]; do
    READERS=$(python3 -I _tools/make_block.py "$D" "$B" "$PER" "$K" "$SEED" ${WITHOUT_REPLIES_OK:+without-replies-ok}); RC=$?
    [ $RC -eq 3 ] && break
    if [ $RC -eq 2 ]; then WAITING=1; break; fi
    T=""; for nn in $READERS; do ok "$nn" >/dev/null 2>&1 || T="$T $nn"; done
    [ -n "$T" ] && { GROUP="$GROUP $B"; TODO="$TODO$T"; }
    B=$((B + 1))
  done
  if [ -z "$TODO" ]; then
    [ $WAITING -eq 0 ] && break
    pgrep -f "fetch_replies.py $D|fetch_sub_comments.py|index_own_replies.py" >/dev/null || stop "replies for block $B are not fetched and nothing is fetching them"
    echo "  $(date +%H:%M:%S) block $B: waiting for its replies to be fetched"; sleep 60; continue
  fi
  [ $((SENT + $(echo $TODO | wc -w))) -gt "$CAP" ] && stop "cap of $CAP readers reached"
  echo; echo "=== blocks$GROUP: sending readers$TODO ($(date +%H:%M)); shown live: reader $(echo $TODO | cut -d' ' -f1) ==="
  FIRST=1; for nn in $TODO; do if [ $FIRST = 1 ]; then LIVE=$nn; FIRST=0; else timed "$nn" log & fi; done
  timed "$LIVE" live; echo "=== reader $LIVE has stopped ($(date +%H:%M)); waiting for the rest of blocks$GROUP ==="; wait
  SENT=$((SENT + $(echo $TODO | wc -w)))
  for nn in $TODO; do
    if ! ok "$nn"; then
      if [ "$(cat "$LOGS/$PREFIX$nn.secs" 2>/dev/null || echo 0)" -lt 180 ] && [ ! -s "$D/posts-$PREFIX$nn.tsv" ]; then
        tail -5 "$LOGS/$PREFIX$nn.log"; stop "reader $nn ended within 3 minutes with nothing written (usage run out, or Codex could not start)"; fi
      echo "redoing reader $nn whole ($(date +%H:%M))"; mkdir -p "$LOGS/failed-first-try"
      mv -f "$Q/reddit-$PREFIX$nn.jsonl" "$D/posts-$PREFIX$nn.tsv" "$D/notes-$PREFIX$nn.md" "$LOGS/failed-first-try/" 2>/dev/null
      timed "$nn" log; SENT=$((SENT + 1))
      if ! ok "$nn"; then
        [ "$(cat "$LOGS/$PREFIX$nn.secs")" -lt 180 ] && [ ! -s "$D/posts-$PREFIX$nn.tsv" ] && stop "reader $nn ended within 3 minutes with nothing written (usage run out, or Codex could not start)"
        FAILED="$FAILED $nn"; NFAILED=$((NFAILED + 1)); mkdir -p "$LOGS/failed-twice"
        mv -f "$Q/reddit-$PREFIX$nn.jsonl" "$D/posts-$PREFIX$nn.tsv" "$D/notes-$PREFIX$nn.md" "$LOGS/failed-twice/" 2>/dev/null
      fi
    fi
  done
  if [ -z "${NO_COMMIT:-}" ]; then git add -A "$NICHE" new-and-expecting-mothers/reddit/raw/reddit-2026 >/dev/null 2>&1 && git commit -q -m "$NICHE: read-and-sort blocks$GROUP, readers$TODO" && echo "committed blocks$GROUP ($(date +%H:%M))"; fi
  [ $NFAILED -ge 3 ] && stop "three readers failed the check twice:$FAILED"
done
echo; echo "PASS-DONE $(date "+%Y-%m-%d %H:%M") readers sent $SENT, failed twice=[${FAILED# }]"; echo "$(date "+%Y-%m-%d %H:%M") done | sent $SENT | failed twice [${FAILED# }]" >> "$D/sent.txt"
