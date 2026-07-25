"""
scripts_generator.py
HormigasAIS Edge Starter

Genera scripts auxiliares del starter.

Fase:
- utils/env_loader.py
- scripts/verify_sdk.py (POST del SDK LBH)
"""

from pathlib import Path


def write_if_missing(path: Path, content: str):
    if path.exists():
        print(f"  └── {path.name} ya existe")
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  └── {path.name} creado")


def generate(root: Path):

    print("[LOAD] scripts_generator")

    # ============================================================
    # utils/env_loader.py
    # ============================================================

    utils = root / "utils"
    utils.mkdir(exist_ok=True)

    env_loader = r'''
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
'''

    write_if_missing(
        utils / "env_loader.py",
        env_loader
    )


    # ============================================================
    # scripts/verify_sdk.py
    # ============================================================

    scripts = root / "scripts"
    scripts.mkdir(exist_ok=True)


    verify_sdk = r'''#!/usr/bin/env python3

"""
verify_sdk.py
HormigasAIS LBH SDK Power-On Self Test (POST)
"""

import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(
    0,
    str(ROOT)
)


from utils.env_loader import load_termux_secrets

load_termux_secrets()


print("========================================")
print("🐜 HormigasAIS :: SDK POST")
print("========================================")


try:

    from protocols.encoder import (
        make_header,
        encode_packet
    )

    from protocols.decoder import (
        decode_packet
    )

    from protocols.constants import (
        TYPE_CODES
    )

    from protocols.signer import (
        seal_action
    )

    from protocols.verifier import (
        verify_signature
    )


except Exception as e:

    print("[FAIL] Importación del SDK")
    print(e)
    sys.exit(1)


print("[ OK ] Importación del SDK")


secret = os.environ.get(
    "LBH_SECRET"
)


if not secret:

    print(
        "[FAIL] LBH_SECRET no definido"
    )

    print(
        "Configure ~/.hormigas_secrets"
    )

    sys.exit(1)


print(
    "[ OK ] LBH_SECRET disponible"
)


payload = json.dumps(
    {
        "action": "sdk_post",
        "node": "SELFTEST"
    }
)


frame = encode_packet(
    make_header(
        "A16",
        "00"
    ),
    TYPE_CODES["FUEL"],
    payload
)


print(
    "[ OK ] Codificación LBH"
)


decoded = decode_packet(frame)


if decoded["payload"] != payload:

    print(
        "[FAIL] Decodificación"
    )

    sys.exit(1)


print(
    "[ OK ] Decodificación"
)


seal = seal_action(
    payload,
    "SELFTEST"
)


print(
    "[ OK ] Firma HMAC"
)


valid = verify_signature(
    payload,
    seal["firma"],
    seal["owner"],
    seal["timestamp"]
)


if not valid:

    print(
        "[FAIL] Verificación HMAC"
    )

    sys.exit(1)


print(
    "[ OK ] Verificación HMAC"
)


print("")

print(
    "========================================"
)

print(
    "SDK LBH OPERATIVO"
)

print(
    "========================================"
)
'''


    verify = scripts / "verify_sdk.py"

    write_if_missing(
        verify,
        verify_sdk
    )

    verify.chmod(0o755)


    print("[ OK ] scripts_generator")


