#!/usr/bin/env bash
cd ~/hormigasais-edge-starter

echo "🐜 Actualizando agents_generator.py y contracts_generator.py..."

# agents_generator.py
cat << 'AGENT' > generators/agents_generator.py
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
AGENT

# contracts_generator.py
cat << 'CONTRACT' > generators/contracts_generator.py
"""
contracts_generator.py
HormigasAIS Edge Starter
"""

from pathlib import Path
import datetime

def write_if_missing(path: Path, content: str):
    if path.exists():
        print(f"  └── {path.name} ya existe")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"  └── {path.name} creado")

def generate(root: Path):
    print("[LOAD] contracts_generator")
    protocols_dir = root / "protocols"
    protocols_dir.mkdir(exist_ok=True)

    fecha = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    contract_content = f"""\
==============================================================================
.human GOVERNANCE CONTRACT — HormigasAIS Edge Starter
==============================================================================
NODE:       A16
OWNER:      Cristhiam Leonardo Hernández Quiñonez
CREATED:    {fecha}
SOVEREIGNTY DECLARATION:
This node operates under full digital sovereignty.
CERT::LBH-HUMAN-STARTER-V1-CLHQ
==============================================================================
"""
    contract_path = protocols_dir / "human_contract.lbh"
    write_if_missing(contract_path, contract_content)
    print("[ OK ] contracts_generator")
CONTRACT

echo "✅ Generadores actualizados"

python3 generator.py
echo "✅ agents y contracts actualizados correctamente."
