#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$SCRIPT_DIR"
LAB_DIR="${LAB_DIR:-$PROJECT_DIR/.lab}"

fail() { printf 'FAIL: %s\n' "$*" >&2; exit 1; }

command -v bash >/dev/null 2>&1 || fail "bash no está disponible"
command -v python3 >/dev/null 2>&1 || fail "python3 no está disponible"

mkdir -p "$LAB_DIR/workspace" "$LAB_DIR/logs" "$LAB_DIR/backups"

if [[ ! -f "$LAB_DIR/workspace/current-payload.json" ]]; then
    cp "$PROJECT_DIR/fixtures/sample-payload.json" "$LAB_DIR/workspace/current-payload.json"
fi

if [[ ! -f "$LAB_DIR/workspace/previous-payload.json" ]]; then
    cp "$PROJECT_DIR/fixtures/sample-payload.json" "$LAB_DIR/workspace/previous-payload.json"
fi

printf 'OK: Proyecto final preparado en %s\n' "$LAB_DIR"
