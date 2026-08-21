# Objetivos y mapa pedagógico

## Objetivo general

Construir y validar un laboratorio Edge reproducible desde Android/Termux, aplicando separación de identidades, higiene de secretos, validación de payloads, registro seguro y recuperación controlada.

## Objetivos específicos

Al finalizar, el estudiante podrá:

1. Comprobar la disponibilidad de Bash, Python 3 y Git desde Termux o Linux.
2. Explicar la diferencia entre una clave SSH pública, una clave privada, un token de API y una variable de configuración.
3. Mantener secretos fuera del repositorio y detectar patrones de exposición antes de publicar.
4. Ejecutar un flujo local idempotente con fixtures y resultados esperados.
5. Describir la separación entre plano de control local y plano de ejecución remoto.
6. Validar un payload de laboratorio y registrar solo metadatos no sensibles.
7. Diseñar un rollback y demostrarlo en un escenario controlado.
8. Documentar las decisiones, limitaciones y pasos de reproducción.

## Evidencias de dominio

El estudiante entrega un repositorio o carpeta de proyecto que contiene un README, un script de preparación, un validador, fixtures ficticios, pruebas, un registro sanitizado y una sección de recuperación. El proyecto debe ejecutarse sin credenciales reales y debe explicar qué partes son locales, cuáles son remotas y qué dependencias permanecen.

## Niveles

| Nivel | Descripción |
|---|---|
| Inicial | Puede preparar el entorno y ejecutar validaciones básicas. |
| Operativo | Puede separar configuración, ejecutar fixtures y detectar exposición. |
| Integrador | Puede diseñar un flujo Edge sandbox, pruebas y rollback. |

## Método de trabajo

Cada lección sigue el ciclo: leer el objetivo, ejecutar un comando pequeño, comparar con el resultado esperado, registrar el hallazgo y explicar qué cambiaría en producción. La reproducibilidad importa tanto como que el comando termine con éxito.
