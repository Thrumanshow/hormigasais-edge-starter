#!/usr/bin/env python3
"""
verify_sdk.py
LBH SDK Power-On Self Test (POST)
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

print("========================================")
print("🐜 HormigasAIS :: SDK POST")
print("========================================")

try:
    from protocols.encoder import make_header, encode_packet
    from protocols.decoder import decode_packet
    from protocols.constants import TYPE_CODES
    from protocols.signer import seal_action
    from protocols.verifier import verify_signature
except Exception as e:
    print("[FAIL] Importación del SDK")
    print(e)
    sys.exit(1)

print("[ OK ] Importación del SDK")

secret = os.environ.get("LBH_SECRET")

if not secret:
    print("[FAIL] LBH_SECRET no definido")
    sys.exit(1)

print("[ OK ] LBH_SECRET disponible")

payload = json.dumps({
    "action":"sdk_post",
    "node":"SELFTEST"
})

frame = encode_packet(
    make_header("A16","00"),
    TYPE_CODES["FUEL"],
    payload
)

print("[ OK ] Codificación LBH")

decoded = decode_packet(frame)

if decoded["payload"] != payload:
    print("[FAIL] Decodificación")
    sys.exit(1)

print("[ OK ] Decodificación")

seal = seal_action(
    payload,
    "SELFTEST"
)

print("[ OK ] Firma HMAC")

valid = verify_signature(
    payload,
    seal["firma"],
    seal["owner"],
    seal["timestamp"]
)

if not valid:
    print("[FAIL] Verificación HMAC")
    sys.exit(1)

print("[ OK ] Verificación HMAC")

print("")
print("========================================")
print("SDK LBH OPERATIVO")
print("========================================")
