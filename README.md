# 🐜 HormigasAIS Edge Starter

Starter oficial para desplegar un **nodo soberano** de HormigasAIS con agentes LBH.

> "Soberanía digital en el edge"

## 🚀 Instalación Rápida

```bash
git clone https://github.com/Thrumanshow/hormigasais-edge-starter.git
cd hormigasais-edge-starter
bash bootstrap.sh
python3 generator.py
```

> ⚠️ El comando `npx create-hormigas-node` aún no está publicado en npm. Usa el método manual mostrado arriba.

## ¿Qué incluye?

- **Bootstrap automático** del entorno en Termux
- **SDK LBH completo** (encoder, decoder, signer, verifier)
- **Agentes autónomos**: \`hormiga_centinela\` y \`hormiga_relevo\`
- **Generadores modulares** (config, protocols, scripts, agents, contracts)
- **Verificación POST** del SDK (\`verify_sdk.py\`)

## Comandos útiles

\`\`\`bash
./bootstrap.sh                    # Preparar entorno
python3 generator.py              # Ejecutar generadores
python3 scripts/verify_sdk.py     # Test completo del SDK LBH
\`\`\`

## Estructura del proyecto

\`\`\`
hormigasais-edge-starter/
├── bootstrap.sh
├── generator.py
├── package.json
├── protocols/          # SDK LBH
├── agents/             # Agentes autónomos
├── scripts/            # Scripts de verificación
├── utils/              # Utilidades
├── .hormigasais/       # Configuración del nodo
└── logs/
\`\`\`

---

**Made with ❤️ for digital sovereignty**
Author: Cristhiam Leonardo Hernández Quiñonez (CLHQ)
© HormigasAIS • Lenguaje Binario HormigasAIS (LBH)

[hormigasais.com](https://hormigasais.com) | [@Thrumanshow](https://github.com/Thrumanshow)
