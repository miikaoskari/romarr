#!/usr/bin/env bash

set -euo pipefail

CONFIG_PATH=${1:-config.json}
OUT_PATH=${2:-src/token_response.json}

cleanup() {
    [[ -n "${TMPFILE:-}" && -f "$TMPFILE" ]] && rm -f "$TMPFILE"
}
trap cleanup EXIT

# Check dependencies
command -v jq >/dev/null 2>&1 || { echo "jq is required but not installed" >&2; exit 2; }
command -v curl >/dev/null 2>&1 || { echo "curl is required but not installed" >&2; exit 2; }

if [[ ! -f "$CONFIG_PATH" ]]; then
    echo "Config file not found: $CONFIG_PATH" >&2
    exit 3
fi

client_id=$(jq -r '.client_id // empty' "$CONFIG_PATH")
client_secret=$(jq -r '.client_secret // empty' "$CONFIG_PATH")

if [[ -z "$client_id" || -z "$client_secret" ]]; then
    echo "client_id or client_secret missing in $CONFIG_PATH" >&2
    exit 4
fi

# Ensure output directory exists
mkdir -p "$(dirname "$OUT_PATH")"

# Use a temp file to capture body and the status code
TMPFILE=$(mktemp)
STATUS=$(curl -sS -w "%{http_code}" -o "$TMPFILE" -X POST \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "client_id=$client_id" \
  --data-urlencode "client_secret=$client_secret" \
  --data "grant_type=client_credentials" \
  https://id.twitch.tv/oauth2/token)

if [[ "$STATUS" -ne 200 ]]; then
    echo "Failed to get token: HTTP $STATUS" >&2
    echo "Response body:" >&2
    sed -n '1,200p' "$TMPFILE" >&2 || true
    exit 5
fi

# Add client_id into the JSON response for convenience
jq --arg cid "$client_id" '. + {client_id: $cid}' "$TMPFILE" > "$OUT_PATH"

echo "Wrote token response to $OUT_PATH"
