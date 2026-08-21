#!/usr/bin/env bash
set -Eeuo pipefail

TEST_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
STARTER_DIR="$(cd -- "$TEST_DIR/../starter" && pwd)"
TEST_LAB="$(mktemp -d)"
trap 'rm -rf "$TEST_LAB"' EXIT

export LAB_DIR="$TEST_LAB/.lab"

bash "$STARTER_DIR/bootstrap-project.sh"
bash "$STARTER_DIR/bootstrap-project.sh"
bash "$STARTER_DIR/validate-project.sh"

[[ -f "$LAB_DIR/workspace/current-payload.json" ]]
[[ -f "$LAB_DIR/workspace/previous-payload.json" ]]

cp "$LAB_DIR/workspace/current-payload.json" "$TEST_LAB/before.json"
printf '%s\n' '{"invalid":true}' > "$LAB_DIR/workspace/current-payload.json"
if python3 "$STARTER_DIR/scripts/verify-project.py" \
    --project-dir "$STARTER_DIR" \
    --lab-dir "$LAB_DIR" >/dev/null 2>&1; then
    echo "FAIL: El payload inválido fue aceptado" >&2
    exit 1
fi

cp "$LAB_DIR/workspace/previous-payload.json" "$LAB_DIR/workspace/current-payload.json"
python3 "$STARTER_DIR/scripts/verify-project.py" \
    --project-dir "$STARTER_DIR" \
    --lab-dir "$LAB_DIR"

cmp -s "$LAB_DIR/workspace/current-payload.json" "$LAB_DIR/workspace/previous-payload.json"
echo "OK: Pruebas de idempotencia, validación y rollback completadas."
