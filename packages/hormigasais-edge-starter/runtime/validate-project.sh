#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="${LAB_DIR:-$SCRIPT_DIR/.lab}"

fail() { printf 'FAIL: %s\n' "$*" >&2; exit 1; }

printf '%s\n' '== Validando proyecto final =='

[[ -f "$SCRIPT_DIR/bootstrap-project.sh" ]] || fail "Falta bootstrap-project.sh"
[[ -f "$SCRIPT_DIR/fixtures/sample-payload.json" ]] || fail "Falta fixture principal"
[[ -f "$SCRIPT_DIR/scripts/verify-project.py" ]] || fail "Falta verify-project.py"

bash "$SCRIPT_DIR/bootstrap-project.sh"
python3 "$SCRIPT_DIR/scripts/verify-project.py" \
    --project-dir "$SCRIPT_DIR" \
    --lab-dir "$LAB_DIR"

printf '%s\n' 'OK: Proyecto final validado correctamente.'
