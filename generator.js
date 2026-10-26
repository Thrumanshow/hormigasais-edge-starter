#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const targetName = process.argv[2] || 'mi-colonia';
const targetDir = path.join(process.cwd(), targetName);

console.log(`🐜 [HormigasAIS] Creando nodo: ${targetName}...`);

for (const dir of ['agents', 'protocols', 'scripts', '.hormigasais']) {
  fs.mkdirSync(path.join(targetDir, dir), { recursive: true });
}

const configFile = path.join(targetDir, '.hormigasais', 'node_config.json');

if (fs.existsSync(configFile)) {
  console.log('  node_config.json ya existe, no se sobrescribe.');
} else {
  const config = {
    schema: 'LBH_NODE_CONFIG_V1',
    node_id: 'NODE-' + Math.random().toString(36).substring(2, 8).toUpperCase(),
    node_name: targetName,
    protocol: 'LBH_BINARY_V2',
    version: '2.0.0',
    owner: { name: 'YOUR-NAME', email: 'YOUR-EMAIL' },
    location: { country: 'YOUR-COUNTRY', city: 'YOUR-CITY' },
    created_at: new Date().toISOString(),
    status: 'INITIALIZED',
    agents: ['hormiga_centinela', 'hormiga_relevo'],
    certificate: 'PENDING'
  };
  fs.writeFileSync(configFile, JSON.stringify(config, null, 2) + '\n');
}

console.log(`✅ Nodo creado en ${targetDir}`);
console.log(`Siguiente paso: cd ${targetName} y completa .hormigasais/node_config.json`);
