# Ejercicio 1: Environment Check

## Desafío

Demuestra que tu entorno puede ejecutar el laboratorio sin modificar el núcleo del starter.

## Instrucciones

Ejecuta:

```bash
python3 course/scripts/check-environment.py
printf 'exit_code=%s\n' "$?"
```

Guarda en tu solución la versión de Python, la versión de Git y el código de salida. No incluyas el contenido completo de tu entorno ni variables sensibles.

## Entrega

Crea `course/.lab/student-environment.txt` con una salida sanitizada que contenga:

```text
python=3.x
 git=2.x
status=compatible
```

El espacio inicial antes de `git` es solo ilustrativo; utiliza una línea limpia en tu archivo.

## Criterios

El ejercicio se aprueba si el comando devuelve cero, la salida contiene `OK`, el archivo de entrega no contiene tokens y no se modifican archivos fuera de `course/.lab/`.

## Pregunta de reflexión

¿Por qué un script de bootstrap debe comprobar dependencias antes de intentar generar agentes o desplegar cambios? Responde en dos o tres párrafos y relaciona la respuesta con reproducibilidad y manejo de errores.
