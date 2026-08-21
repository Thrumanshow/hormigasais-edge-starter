# Ejercicio 4: Recuperación y rollback

## Desafío

Demuestra que una operación fallida no deja el laboratorio en un estado ambiguo.

## Instrucciones

1. Copia `course/fixtures/sample-payload.json` a `course/.lab/workspace/current-payload.json`.
2. Guarda una copia anterior en `course/.lab/workspace/rollback-payload.json`.
3. Simula un cambio inválido usando un archivo temporal.
4. Ejecuta la validación y registra el fallo.
5. Restaura la copia anterior.
6. Ejecuta nuevamente la validación y registra el estado recuperado.

## Evidencia mínima

El estudiante entrega un log con dos estados: `FAILED_VALIDATION` y `ROLLED_BACK`. El log no debe contener secretos, rutas privadas ni contenido completo de credenciales.

## Criterios

El ejercicio se aprueba si el estado final coincide con la copia anterior, la operación es repetible y el estudiante explica qué habría que respaldar y qué habría que revocar en un entorno remoto real.
