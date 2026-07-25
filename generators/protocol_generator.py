"""
protocol_generator.py
HormigasAIS Edge Starter

Genera el paquete protocols/ modular del SDK LBH.
No sobrescribe archivos existentes.
"""

from pathlib import Path


def write_if_missing(path: Path, content: str):
    if path.exists():
        print(f"  └── {path.name} ya existe")
        return
    path.write_text(content, encoding="utf-8")
    print(f"  └── {path.name} creado")


def generate(root: Path):

    protocols = root / "protocols"
    protocols.mkdir(exist_ok=True)

    write_if_missing(
        protocols / "__init__.py",
        '''"""
LBH Protocol SDK
"""

from .constants import TYPE_CODES
from .encoder import encode_packet
from .decoder import decode_packet
from .signer import seal_action
from .verifier import verify_signature
'''
    )

    write_if_missing(
        protocols / "constants.py",
        '''"""
Constantes oficiales LBH
"""

TYPE_CODES = {
    "SEAL":"5345414c",
    "VERI":"56455249",
    "SYNC":"53594e43",
    "PING":"50494e47",
    "FUEL":"4655454c",
    "ACKK":"41434b4b",
    "ERRR":"45525252",
}
'''
    )

    write_if_missing(
        protocols / "encoder.py",
        '''from .constants import TYPE_CODES

def make_header(node_id="A16", version="00"):
    return (
        node_id.encode().hex()[:4].ljust(4,"0") +
        version.encode().hex()[:4].ljust(4,"0")
    )

def encode_packet(header, type_code, payload):
    payload_hex = payload.encode().hex()
    length = format(len(payload_hex)//2,"08x")
    return f"{header}{type_code}{length}{payload_hex}"
'''
    )

    write_if_missing(
        protocols / "decoder.py",
        '''def decode_packet(frame):
    return {
        "header":frame[:8],
        "type_code":frame[8:16],
        "length":int(frame[16:24],16),
        "payload":bytes.fromhex(frame[24:]).decode()
    }
'''
    )

    write_if_missing(
        protocols / "signer.py",
        '''import hashlib
import hmac
import os
import time

def seal_action(content, owner):

    secret = os.environ.get("LBH_SECRET")

    if not secret:
        raise RuntimeError(
            "LBH_SECRET no definido."
        )

    sha = hashlib.sha256(content.encode()).hexdigest()

    ts = int(time.time())

    payload = f"{sha}|{owner}|{ts}"

    sig = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return {
        "sha256":sha,
        "firma":sig,
        "timestamp":ts,
        "owner":owner
    }
'''
    )

    write_if_missing(
        protocols / "verifier.py",
        '''import hashlib
import hmac
import os

def verify_signature(content, signature, owner, timestamp):

    secret = os.environ.get("LBH_SECRET")

    if not secret:
        return False

    sha = hashlib.sha256(content.encode()).hexdigest()

    payload = f"{sha}|{owner}|{timestamp}"

    expected = hmac.new(
        secret.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()

    return hmac.compare_digest(
        expected,
        signature
    )
'''
    )

    write_if_missing(
        protocols / "lbh_core.py",
        '''"""
Compatibilidad con versiones anteriores.

Importa automáticamente todos los módulos del SDK.
"""

from .constants import *
from .encoder import *
from .decoder import *
from .signer import *
from .verifier import *
'''
    )
