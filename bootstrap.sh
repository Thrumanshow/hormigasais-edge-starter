#!/usr/bin/env bash
# HormigasAIS Edge Starter — bootstrap.sh
# Prepara el entorno antes de ejecutar generator.py

set -Eeuo pipefail

echo "🐜 HormigasAIS Edge Starter — Bootstrap"
echo "========================================"

# 1. Validar Python3
if ! command -v python3 >/dev/null 2>&1; then
  echo "❌ python3 no encontrado. Instálalo antes de continuar."
  exit 1
fi
echo "✅ python3: $(python3 --version)"

# 2. Validar Node (opcional, solo si se usará generator.js)
if command -v node >/dev/null 2>&1; then
  echo "✅ node: $(node --version)"
else
  echo "⚠️ node no encontrado (opcional, solo necesario para generator.js)"
fi

# 3. Crear directorios base si no existen
mkdir -p logs generators .hormigasais
echo "✅ Directorios base verificados: logs/, generators/, .hormigasais/"

# 4. Instalar dependencias npm solo si existe package.json y node/npm disponibles
if [ -f package.json ] && command -v npm >/dev/null 2>&1; then
  echo "📦 Instalando dependencias npm..."
  npm install --omit=dev
else
  echo "⚠️ Saltando npm install (sin package.json o sin npm)"
fi

echo "========================================"
echo "✅ Bootstrap completado. Siguiente paso:"
echo "   python3 generator.py"
