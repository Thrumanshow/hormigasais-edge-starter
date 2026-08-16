#!/usr/bin/env python3
"""
HormigasAIS Edge Starter
generator.py

Orquestador principal del starter.

Responsabilidades:
- Crear la estructura base.
- Ejecutar cada generador especializado.
- No sobrescribir archivos existentes salvo indicación explícita.
"""

from pathlib import Path
import importlib
import sys

ROOT = Path(__file__).resolve().parent
GENERATORS = ROOT / "generators"

sys.path.insert(0, str(ROOT))

MODULES = [
    "config_generator",
    "protocol_generator",
    "contracts_generator",
    "agents_generator",
    "scripts_generator",
]


def main():

    GENERATORS.mkdir(exist_ok=True)

    init = GENERATORS / "__init__.py"

    if not init.exists():
        init.write_text(
            "# HormigasAIS Generators Package\n",
            encoding="utf-8"
        )

    print("============================================")
    print("🐜 HormigasAIS Generator")
    print("============================================")

    fallos = []
    faltantes = []

    for module_name in MODULES:

        print(f"[LOAD] {module_name}")

        try:

            module = importlib.import_module(
                f"generators.{module_name}"
            )

            if hasattr(module, "generate"):

                module.generate(ROOT)

                print(f"[ OK ] {module_name}")

            else:

                print(f"[SKIP] {module_name} (sin generate())")

        except ModuleNotFoundError:

            print(f"[FALTA] {module_name} no existe — módulo obligatorio")
            faltantes.append(module_name)

        except Exception as e:

            print(f"[FAIL] {module_name}")
            print(e)
            fallos.append(module_name)

    print("")

    if faltantes or fallos:
        print("❌ Proceso terminado CON ERRORES.")
        if faltantes:
            print(f"   Módulos faltantes: {", ".join(faltantes)}")
        if fallos:
            print(f"   Módulos con fallo: {", ".join(fallos)}")
        print("============================================")
        sys.exit(1)

    print("✅ Proceso terminado correctamente.")
    print("============================================")


if __name__ == "__main__":
    main()
