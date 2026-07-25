
"""
env_loader.py
HormigasAIS Secret Loader

Carga secretos desde:
- Variables de entorno
- ~/.hormigas_secrets
"""

from pathlib import Path
import os


def load_termux_secrets():

    secret_file = Path.home() / ".hormigas_secrets"

    if not secret_file.exists():
        return

    for line in secret_file.read_text(
        encoding="utf-8"
    ).splitlines():

        line = line.strip()

        if (
            not line
            or line.startswith("#")
            or "=" not in line
        ):
            continue

        key, value = line.split("=", 1)

        os.environ.setdefault(
            key.strip(),
            value.strip()
            .strip('"')
            .strip("'")
        )
