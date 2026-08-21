# Ejercicio 2: Higiene de secretos

## Desafío

Identifica qué archivos pueden publicarse y cuáles deben permanecer locales.

## Instrucciones

Ejecuta:

```bash
bash course/scripts/verify-no-secrets.sh
git status --short
```

Revisa `course/.env.example` y `course/fixtures/sample.env`. Ambos deben contener valores ficticios. Crea una copia local en `course/.lab/` y confirma que Git la ignora.

## Criterios

El ejercicio se aprueba si el validador devuelve cero, `course/.lab/.env` no aparece en `git status --short` y el estudiante puede explicar por qué un `.env.example` no es un almacén de secretos.

## Pregunta de reflexión

Explica la diferencia entre ocultar un archivo con `.gitignore` y revocar una credencial que ya fue publicada. La respuesta debe indicar por qué `.gitignore` no corrige una exposición histórica.
