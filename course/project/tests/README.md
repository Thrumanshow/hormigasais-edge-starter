# Pruebas del proyecto final

Las pruebas deben ejecutarse desde la raíz del repositorio y no deben requerir credenciales. Como mínimo, deben comprobar que `bootstrap-project.sh` puede ejecutarse dos veces, que `validate-project.sh` devuelve cero con fixtures válidos, que devuelve un código distinto de cero con un payload inválido y que el rollback restaura el estado anterior.

La salida debe utilizar estados estables, por ejemplo `PASS`, `FAIL` y `ROLLED_BACK`. No incluyas timestamps completos, rutas privadas ni valores de variables de entorno si no son necesarios para reproducir el resultado.

Una prueba mínima debe dejar el árbol limpio fuera de `course/.lab/` y producir un informe sanitizado en el directorio temporal del proyecto.
