#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
LAB_DIR="$SCRIPT_DIR/.lab"

echo "== Preparando laboratorio de aprendizaje =="

mkdir -p "$LAB_DIR/logs" "$LAB_DIR/workspace"
cp -n "$SCRIPT_DIR/fixtures/sample.env" "$LAB_DIR/.env" 2>/dev/null || true

python3 "$SCRIPT_DIR/scripts/check-environment.py"

echo "OK: Laboratorio inicializado con éxito en $LAB_DIR"
