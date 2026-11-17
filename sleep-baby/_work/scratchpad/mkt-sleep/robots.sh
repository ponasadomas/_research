#!/bin/bash
# usage: robots.sh domain...   prints status and AI-bot related lines + Disallow for *
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
for d in "$@"; do
  out=$(curl -sS -L --max-time 20 -A "$UA" -w "\n__HTTP %{http_code}" "https://$d/robots.txt" 2>&1)
  code=$(echo "$out" | tail -1)
  echo "### $d $code"
  echo "$out" | head -c 20000 | grep -iE "^(user-agent|disallow|content-signal)" | grep -iE -B0 "gpt|claude|anthropic|ai|ccbot|user-agent: \*|disallow: /$|content-signal" | head -25
done
