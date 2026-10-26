# 🐜 HormigasAIS Edge Starter

Starter oficial para desplegar un **nodo soberano** de HormigasAIS con agentes LBH.

> "Soberanía digital en el edge"

## 🚀 Instalación

### Opción 1 — Starter CLI vía npm (recomendado)

El starter técnico se distribuye como paquete npm independiente, sin el contenido pedagógico completo:

    npm install -g @hormigasais/edge-starter
    hormigasais-edge --help
    hormigasais-edge bootstrap
    hormigasais-edge validate

Por defecto, el laboratorio se crea en .hormigasais-edge-lab/ en el directorio actual. Puedes cambiar la ubicación con LAB_DIR:

    LAB_DIR="$HOME/hormigasais-edge-lab" hormigasais-edge bootstrap

Paquete: [@hormigasais/edge-starter](https://www.npmjs.com/package/@hormigasais/edge-starter)

### Opción 2 — Clonar el repositorio completo (incluye el curso)

    git clone https://github.com/Thrumanshow/hormigasais-edge-starter.git
    cd hormigasais-edge-starter
    bash bootstrap.sh
    python3 generator.py

Usa esta opción si además del starter quieres acceso al curso práctico completo (./course/).

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

## Curso Práctico

El directorio [`course/`](./course/) contiene un laboratorio educativo aislado para aprender administración Edge y protocolos LBH desde Android/Termux. Sus scripts utilizan fixtures y no requieren secretos reales. Consulta [`course/README.md`](./course/README.md) para comenzar.

---

## 📄 Componentes y Enlaces del Ecosistema

| Repo | Descripción |
| :--- | :--- |
| **LBH-Net** | Red soberana P2P :9199/:9200 |
| **Institucionalidad** | Foundation & Governance |

---

### Arquitectura y Ecosistema HormigasAIS
* **Red P2P Base:** [LBH-Net](https://github.com/HormigasAIS/LBH-Net) — Red soberana distribuida basada en Protocolo LBH (Termux / UDP :9199 / TCP :9200 / SQLite / Ed25519).
* **Vitrina Oficial:** [hormigasais.com](https://hormigasais.com)
* **Documentación Técnica:** [docs.hormigasais.com](https://docs.hormigasais.com)
* **Fundador:** CLHQ — Cristhiam Leonardo Hernández Quiñonez | El Salvador 2026 | DOI: 10.5281/zenodo.17767205

## Licencia

HormigasAIS Source-Available License v1.0 (ver `LICENSE`). Puedes leer y estudiar el código, e instalar el paquete para generar y probar un nodo propio con fines personales no comerciales. El uso en producción, la redistribución y el uso comercial requieren autorización de CLHQ.

Las versiones 0.1.0 a 0.1.2 se publicaron declarando MIT; desde la 0.1.3 rige esta licencia.
