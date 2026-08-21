# Curso práctico: Gobernanza Edge desde Android

Este laboratorio acompaña el repositorio `hormigasais-edge-starter` y enseña a preparar y validar un entorno Edge desde Android/Termux usando herramientas POSIX, Git, Python y fixtures de laboratorio.

> El curso utiliza un entorno educativo aislado. No requiere tokens reales, claves privadas ni credenciales de Cloudflare para completar la ruta principal.

## Resultado de aprendizaje

Al terminar, el estudiante podrá preparar un laboratorio reproducible desde Termux, separar código de configuración, detectar posibles secretos antes de publicar, validar una operación local y documentar un flujo Edge con controles de mínimo privilegio y recuperación.

El curso usa HormigasAIS y LBH como **caso de estudio experimental**. No presenta LBH como un estándar universal ni afirma que una demostración local constituya una auditoría de seguridad independiente.

## Requisitos

El estudiante necesita un dispositivo Android con Termux o un sistema Linux equivalente, Bash, Python 3, Git y acceso a Internet para clonar el repositorio. La ruta principal funciona offline después de descargar el proyecto. El módulo Cloudflare es opcional y debe ejecutarse únicamente en un entorno de prueba.

## Recorrido

| Etapa | Tema | Evidencia |
|---|---|---|
| 1 | Preparación del entorno | El validador detecta Bash, Python y Git. |
| 2 | Identidades y Git/SSH | El estudiante distingue clave privada, clave pública y remoto. |
| 3 | Configuración segura | Los fixtures no contienen credenciales reales. |
| 4 | Firmas y payloads | Se valida un mensaje de laboratorio. |
| 5 | Worker sandbox | Se entiende el flujo remoto sin usar secretos productivos. |
| 6 | Validación | El curso produce resultados esperados. |
| 7 | Rollback | El estudiante restaura un estado anterior y documenta la recuperación. |

## Inicio rápido

Desde la raíz de `hormigasais-edge-starter`:

```bash
cd course
bash bootstrap-course.sh
bash validate-course.sh
```

Después comienza con [`lessons/01-environment/README.md`](lessons/01-environment/README.md) y ejecuta el ejercicio de [`exercises/01-environment-check/README.md`](exercises/01-environment-check/README.md).

## Reglas de seguridad

Nunca introduzcas en este directorio tokens reales, claves privadas, archivos `.pem`, credenciales de Cloudflare ni datos personales. Usa únicamente los valores de `fixtures/` y el archivo local `course/.lab/.env`, que está excluido por `.gitignore`. Si una práctica necesita un servicio externo, utiliza una cuenta de sandbox o una simulación local y revoca cualquier credencial de prueba al terminar.

## Proyecto final

El proyecto final consiste en crear un flujo de laboratorio que prepara un nodo, valida un payload, registra un resultado no sensible y demuestra una recuperación. La especificación está en [`project/README.md`](project/README.md) y la evaluación en [`project/rubric.md`](project/rubric.md).

## Limitaciones

La ejecución en Android/Termux demuestra portabilidad del plano de control para este laboratorio; no demuestra que todos los dispositivos Android sean equivalentes ni elimina la dependencia de conectividad cuando se invoca un servicio remoto. Las métricas y afirmaciones deben acompañarse de versión, dispositivo, fecha y comandos reproducibles.

## Licencia y atribución

Consulta la licencia del repositorio raíz. El material del curso debe conservar la atribución de HormigasAIS y distinguir claramente entre código del starter, fixtures educativos y aportes del estudiante.
