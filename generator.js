#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const targetName = process.argv[2] || 'mi-colonia';
const targetDir = path.join(process.cwd(), targetName);

console.log(`🐜 [HormigasAIS] Desplegando nodo soberano en edge: ${targetName}...`);

if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
}

// Estructura de directorios
const subdirs = ['agents', 'protocols', 'scripts', '.hormigasais'];
subdirs.forEach(dir => {
    const p = path.join(targetDir, dir);
    if (!fs.existsSync(p)) fs.mkdirSync(p, { recursive: true });
});

// Copiar o generar archivos base en el directorio destino
const fecha = new Date().toISOString();

const config = {
    "node_id": "NODE-" + Math.random().toString(36).substring(2, 8).toUpperCase(),
    "node_name": targetName,
    "protocol": "LBH_BINARY_V1",
    "version": "2.0",
    "owner": "Cristhiam Leonardo Hernández Quiñonez",
    "location": "San Miguel, El Salvador",
    "nodo_maestro": "A16-SanMiguel-SV",
    "created": fecha,
    "agents": ["hormiga_centinela", "hormiga_relevo"],
    "cert": "SELLADO-SOBERANO-LBH"
};

fs.writeFileSync(path.join(targetDir, '.hormigasais', 'node_config.json'), JSON.stringify(config, null, 2));

console.log(`✅ Nodo configurado en ${targetDir}`);
console.log(`
Siguiente paso:\n  cd ${targetName}\n  ./scripts/ignicion.sh`);
