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
