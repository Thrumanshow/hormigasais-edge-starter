#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

echo "== Ejecutando validación integral del curso =="

python3 "$SCRIPT_DIR/scripts/check-environment.py"
bash "$SCRIPT_DIR/scripts/verify-no-secrets.sh"

test -f "$SCRIPT_DIR/bootstrap-course.sh"
test -f "$SCRIPT_DIR/README.md"
test -f "$SCRIPT_DIR/project/rubric.md"

echo "OK: Curso totalmente reproducible y validado correctamente."
