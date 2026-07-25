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
