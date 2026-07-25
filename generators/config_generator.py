"""
config_generator.py
HormigasAIS Edge Starter

Genera la configuración inicial del nodo.
No sobrescribe configuraciones existentes.
"""

from pathlib import Path
import json
import datetime
import getpass
import socket


def generate(root: Path):

    config_dir = root / ".hormigasais"
    config_dir.mkdir(exist_ok=True)

    config_file = config_dir / "node_config.json"

    if config_file.exists():
        print("  └── node_config.json ya existe")
        return

    now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")

    hostname = socket.gethostname()

    if hostname == "localhost":
        hostname = "A16"

    config = {
        "schema": "LBH_NODE_CONFIG_V1",
        "node_id": f"{hostname}-{getpass.getuser()}",
        "node_name": "mi-colonia",
        "protocol": "LBH_BINARY_V2",
        "version": "2.0.0",
        "owner": {
            "name": "YOUR-NAME",
            "email": "YOUR-EMAIL"
        },
        "location": {
            "country": "SV",
            "city": "San Miguel"
        },
        "master_node": "A16-SanMiguel-SV",
        "created_at": now,
        "status": "INITIALIZED",
        "agents": [
            "hormiga_centinela",
            "hormiga_relevo"
        ],
        "security": {
            "hmac_required": True,
            "algorithm": "HMAC-SHA256"
        },
        "certificate": "PENDING"
    }

    with open(config_file, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("  └── node_config.json creado")
