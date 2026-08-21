# Proyecto final: Nodo Edge de laboratorio reproducible

## Descripción

Construye un flujo educativo que pueda ejecutarse desde Termux o Linux y que demuestre preparación, validación, higiene de secretos, registro seguro y recuperación. El proyecto debe trabajar offline con fixtures y puede añadir una integración remota opcional en sandbox.

## Entregable

El estudiante debe entregar dentro de `course/project/starter/`:

```text
README.md
bootstrap-project.sh
validate-project.sh
fixtures/sample-payload.json
scripts/verify-project.py
logs/example-sanitized.log
```

También debe incluir una nota de arquitectura que explique el plano de control local, el plano de ejecución opcional, las dependencias y los límites del laboratorio.

## Requisitos funcionales

El proyecto debe preparar un directorio de trabajo sin sobrescribir datos existentes, cargar únicamente configuración ficticia, validar un payload, escribir un log sanitizado y demostrar un rollback. Las operaciones deben ser idempotentes: ejecutarlas dos veces no debe duplicar ni destruir información.

## Requisitos de seguridad

No se aceptan tokens reales, claves privadas, archivos `.pem`, credenciales de proveedores, datos personales ni identificadores de cuenta. El validador debe fallar si encuentra patrones de credenciales o rutas absolutas del autor. El proyecto debe declarar qué acciones serían diferentes en producción.

## Requisitos de documentación

El README del proyecto debe incluir objetivo, requisitos, instalación, uso, salida esperada, manejo de errores, rollback, limitaciones y licencia. Debe incluir una tabla que distinga datos públicos, fixtures y secretos que nunca deben aparecer en Git.

## Variantes

La variante mínima es completamente offline. La variante avanzada puede invocar un endpoint de sandbox usando permisos mínimos, pero la evaluación se basa en la reproducibilidad y la seguridad, no en tener una cuenta de proveedor.

## Preguntas de defensa

El estudiante debe explicar qué ocurre si falla la red, qué ocurre si el secreto se filtra, cómo se revoca una credencial, cómo se restaura el último estado válido y qué evidencia permitiría a otra persona reproducir el experimento.
