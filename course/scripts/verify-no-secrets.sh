#!/usr/bin/env bash
set -Eeuo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
COURSE_DIR="$(cd -- "$SCRIPT_DIR/.." && pwd)"

# El propio validador contiene patrones de búsqueda y debe excluirse.
# Los fixtures educativos también se excluyen porque usan valores ficticios.
if grep -RInE \
    --exclude-dir=".lab" \
    --exclude-dir=".git" \
    --exclude=".env.example" \
    --exclude="sample.env" \
    --exclude="verify-no-secrets.sh" \
    'Bearer[[:space:]]+[A-Za-z0-9._-]{20,}|CF_API_TOKEN=[A-Za-z0-9._-]{20,}' \
    "$COURSE_DIR"; then
    echo "ERROR: Se detectaron posibles secretos expuestos en course/." >&2
    exit 1
fi

echo "OK: Verificación de higiene de secretos completada sin hallazgos."
