#!/usr/bin/env bash
set -Eeuo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || {
  echo "FAIL: ejecuta este script desde un clon Git del repositorio." >&2
  exit 1
}

SOURCE="$REPO_ROOT/course/project/starter"
TARGET="${TARGET_DIR:-$REPO_ROOT/packages/hormigasais-edge-starter}"

[[ -d "$SOURCE" ]] || {
  echo "FAIL: no existe $SOURCE" >&2
  exit 1
}

if [[ -e "$TARGET" && "${FORCE:-0}" != "1" ]]; then
  echo "FAIL: el destino ya existe: $TARGET" >&2
  exit 1
fi

rm -rf "$TARGET"
mkdir -p "$TARGET/bin" "$TARGET/runtime/scripts" "$TARGET/runtime/fixtures"

cp "$SOURCE/bootstrap-project.sh" "$TARGET/runtime/bootstrap-project.sh"
cp "$SOURCE/validate-project.sh" "$TARGET/runtime/validate-project.sh"
cp "$SOURCE/scripts/verify-project.py" "$TARGET/runtime/scripts/verify-project.py"
cp "$SOURCE/fixtures/sample-payload.json" "$TARGET/runtime/fixtures/sample-payload.json"
chmod +x "$TARGET/runtime/bootstrap-project.sh" "$TARGET/runtime/validate-project.sh" "$TARGET/runtime/scripts/verify-project.py"

cat > "$TARGET/bin/hormigasais-edge.js" <<'NODE'
#!/usr/bin/env node
'use strict';

const path = require('node:path');
const { spawnSync } = require('node:child_process');

const runtime = path.resolve(__dirname, '..', 'runtime');
const labDir = process.env.LAB_DIR || path.resolve(process.cwd(), '.hormigasais-edge-lab');
const command = process.argv[2] || 'validate';
const commands = {
  bootstrap: ['bootstrap-project.sh'],
  validate: ['validate-project.sh'],
};

if (command === 'help' || command === '--help' || command === '-h') {
  console.log('Uso: hormigasais-edge <bootstrap|validate|help>');
  process.exit(0);
}

if (!commands[command]) {
  console.error(`FAIL: comando no reconocido: ${command}`);
  process.exit(2);
}

const result = spawnSync('bash', [path.join(runtime, commands[command][0])], {
  cwd: runtime,
  env: { ...process.env, LAB_DIR: labDir },
  stdio: 'inherit',
});

if (result.error) {
  console.error(`FAIL: no se pudo ejecutar bash: ${result.error.message}`);
  process.exit(1);
}
process.exit(result.status ?? 1);
NODE
chmod +x "$TARGET/bin/hormigasais-edge.js"

cat > "$TARGET/package.json" <<'JSON'
{
  "name": "@hormigasais/edge-starter",
  "version": "0.1.0",
  "description": "Offline-first Edge starter CLI for Termux and Linux, using public fixtures only.",
  "keywords": ["hormigasais", "edge", "termux", "linux", "devops", "security-lab"],
  "homepage": "https://github.com/Thrumanshow/hormigasais-edge-starter",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Thrumanshow/hormigasais-edge-starter.git"
  },
  "bugs": {
    "url": "https://github.com/Thrumanshow/hormigasais-edge-starter/issues"
  },
  "license": "Apache-2.0",
  "engines": {
    "node": ">=18"
  },
  "bin": {
    "hormigasais-edge": "bin/hormigasais-edge.js"
  },
  "files": ["bin", "runtime", "README.md", "LICENSE"],
  "scripts": {
    "test": "node bin/hormigasais-edge.js validate",
    "pack:check": "npm pack --dry-run --json"
  }
}
JSON

cat > "$TARGET/README.md" <<'MD'
# @hormigasais/edge-starter

CLI reproducible para preparar y validar un laboratorio Edge offline-first desde Termux o Linux. El paquete contiene únicamente scripts, fixtures públicos y una interfaz CLI; no contiene secretos reales ni el contenido completo del curso.

## Requisitos

Se requiere Node.js 18 o posterior, Bash, Python 3 y Git. El paquete está orientado a entornos POSIX, especialmente Termux y Linux.

## Uso local

    npm install
    npm test
    npm run pack:check
    node bin/hormigasais-edge.js bootstrap
    node bin/hormigasais-edge.js validate

Por defecto, el laboratorio se crea en .hormigasais-edge-lab/ dentro del directorio desde el que se ejecuta el comando. Puedes cambiarlo mediante LAB_DIR=/ruta/segura.

## Licencia

Apache License 2.0. Ver el archivo LICENSE para el texto completo.

## Seguridad

Usa únicamente fixtures ficticios. No introduzcas tokens de Cloudflare, claves SSH, archivos .env, logs privados o configuraciones reales en el paquete.

El contenido educativo completo permanece en course/ en el repositorio principal y no se distribuye automáticamente con este paquete.
MD

if [[ -f "$REPO_ROOT/LICENSE" ]]; then
  cp "$REPO_ROOT/LICENSE" "$TARGET/LICENSE"
else
  curl -s "https://www.apache.org/licenses/LICENSE-2.0.txt" -o "$TARGET/LICENSE"
fi

cat > "$TARGET/.npmignore" <<'EOF'
.hormigasais-edge-lab/
.env
*.log
*.tmp
*.key
*.pem
course/
.git/
EOF

printf 'OK: paquete generado en %s\n' "$TARGET"
printf 'NEXT: revisa package.json, LICENSE y ejecuta npm pack --dry-run dentro del paquete.\n'
