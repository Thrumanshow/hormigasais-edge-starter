# Ejercicio 3: API sandbox

## Desafío

Modela una operación remota sin exponer credenciales ni depender de un entorno productivo.

## Modo offline

Usa `course/fixtures/sample-payload.json` y registra el resultado esperado en `course/.lab/logs/api-sandbox.log`. El log debe contener fecha, tipo de operación, estado y código de resultado, pero nunca un token ni una cabecera de autorización.

## Modo remoto opcional

Si utilizas Cloudflare u otro proveedor, emplea una cuenta de laboratorio, permisos mínimos y valores que puedan revocarse. No pegues el token en archivos del repositorio, capturas, logs ni mensajes de commit. Documenta el proveedor, el entorno y el método de revocación sin publicar identificadores sensibles.

## Criterios

El ejercicio se aprueba si existe una variante offline, el resultado es reproducible, el log está sanitizado y el estudiante puede señalar con claridad qué parte pertenece al plano de control local y cuál al plano remoto.
