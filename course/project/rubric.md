# Rúbrica del proyecto final

La calificación total es de 100 puntos. El proyecto se considera aprobado con 70 puntos o más y sin incumplimientos críticos de seguridad.

| Criterio | Puntos | Evidencia |
|---|---:|---|
| Preparación del entorno | 10 | Bootstrap ejecutable e idempotente. |
| Arquitectura | 15 | Diagrama o explicación clara de control local y ejecución remota. |
| Separación de configuración | 15 | Fixtures públicos y secretos ausentes del repositorio. |
| Validación funcional | 15 | Payload válido, payload inválido y códigos de salida correctos. |
| Registro seguro | 10 | Log útil sin tokens, claves ni datos personales. |
| Manejo de errores | 10 | El flujo falla de forma explícita y recuperable. |
| Rollback | 15 | Restauración demostrada y documentada. |
| Reproducibilidad | 5 | Otra persona puede ejecutar el proyecto con las instrucciones. |
| Documentación | 5 | README completo, límites y decisiones explicadas. |

## Incumplimientos críticos

El proyecto no se aprueba si incluye una clave privada, un token real, una credencial de proveedor, datos personales o una instrucción que solicite publicar secretos. Tampoco se aprueba si el validador afirma éxito cuando una dependencia esencial falta.

## Niveles de desempeño

| Nivel | Rango | Descripción |
|---|---:|---|
| Insuficiente | 0–59 | Flujo incompleto o no reproducible. |
| Básico | 60–69 | Funciona parcialmente, pero necesita correcciones importantes. |
| Competente | 70–84 | Cumple los requisitos y mantiene higiene básica. |
| Avanzado | 85–94 | Incluye buenas pruebas, rollback y documentación sólida. |
| Excelente | 95–100 | Es reproducible, pedagógico, seguro y fácil de extender. |

## Revisión entre pares

Una revisión externa debe ejecutar el bootstrap en un directorio limpio, leer el README, comprobar los resultados esperados y señalar cualquier dependencia oculta. El autor debe responder a las observaciones sin solicitar credenciales ni datos privados.
