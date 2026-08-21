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
