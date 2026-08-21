# Lección 1: Comprobar el entorno

## Objetivo

Comprobar que el laboratorio puede ejecutarse con las herramientas mínimas y aprender a distinguir una salida válida de un error de entorno.

## Contexto

Un nodo Edge reproducible empieza por declarar sus dependencias. El curso no presupone que Android, Termux y Linux tengan exactamente la misma configuración; por eso la primera práctica registra qué herramientas están disponibles.

## Ejecución

Desde la raíz del repositorio:

```bash
python3 course/scripts/check-environment.py
```

También puedes ejecutarlo desde el directorio del curso:

```bash
cd course
python3 scripts/check-environment.py
```

## Resultado esperado

La salida debe contener:

```text
OK: Entorno de laboratorio compatible (Bash, Python3, Git detectados).
```

El código de salida debe ser `0`. Puedes comprobarlo con:

```bash
echo $?
```

## Interpretación

Si aparece `FAIL`, el script no está afirmando que el dispositivo sea inseguro; únicamente indica que falta una herramienta necesaria para esta práctica. Instala la dependencia desde una fuente confiable o ejecuta el laboratorio en un entorno Linux compatible. No continúes ocultando el error ni sustituyas una herramienta por un binario desconocido.

## Registro del estudiante

Completa una nota local con la fecha, versión de Python, versión de Git y sistema operativo. No registres rutas que revelen información sensible ni pegues variables de entorno.

```bash
python3 --version
git --version
uname -a
```

## Criterio de finalización

La lección está completa cuando el validador devuelve `0`, el estudiante puede explicar qué comprueba cada herramienta y existe una nota de entorno reproducible sin secretos.

## Extensión opcional

Ejecuta el mismo comprobador desde un directorio temporal y explica por qué el resultado no debería depender del directorio actual. Si el script se comporta de manera diferente, abre una incidencia educativa en lugar de corregirla ocultando el problema.
