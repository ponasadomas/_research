#!/usr/bin/env bash
# curl through the NordVPN SOCKS5 proxy. Credentials come from ~/.config/nordvpn-socks.env (never printed).
# Usage: scripts/proxy_curl.sh <any curl args>
set -euo pipefail
set -a; . "$HOME/.config/nordvpn-socks.env"; set +a
: "${NORD_USER:?}" "${NORD_PASS:?}"
HOST="${NORD_SOCKS_HOST:-amsterdam.nl.socks.nordhold.net}"
exec curl --proxy "socks5h://${NORD_USER}:${NORD_PASS}@${HOST}:1080" "$@"
