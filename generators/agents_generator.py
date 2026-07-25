"""
agents_generator.py
HormigasAIS Edge Starter
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
    print("[LOAD] agents_generator")
    agents_dir = root / "agents"
    agents_dir.mkdir(exist_ok=True)

    centinela_code = '''#!/usr/bin/env python3
"""
hormiga_centinela.py
"""
import time
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from utils.env_loader import load_termux_secrets
load_termux_secrets()

from protocols.encoder import make_header, encode_packet
from protocols.constants import TYPE_CODES
from protocols.signer import seal_action

NODE_ID = "A16"
OWNER = "Cristhiam Leonardo Hernández Quiñonez"
INTERVAL = 30

def emit_pulse():
    payload = json.dumps({
        "agent": "hormiga_centinela",
        "status": "ACTIVE",
        "node": NODE_ID,
        "ts": int(time.time())
    })
    header = make_header(NODE_ID[:3], "00")
    frame = encode_packet(header, TYPE_CODES["FUEL"], payload)
    seal = seal_action(payload, OWNER)
    print("[CENTINELA] FUEL pulse emitido")
    return frame

if __name__ == "__main__":
    print(f"[CENTINELA] Iniciando en nodo {NODE_ID}")
    while True:
        emit_pulse()
        time.sleep(INTERVAL)
'''

    c_path = agents_dir / "hormiga_centinela.py"
    write_if_missing(c_path, centinela_code)
    c_path.chmod(0o755)

    print("[ OK ] agents_generator")
