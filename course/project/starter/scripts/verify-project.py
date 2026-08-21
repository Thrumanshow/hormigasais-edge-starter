#!/usr/bin/env python3
"""Verificador offline del proyecto final de HormigasAIS."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SECRET_PATTERNS = (
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}"),
    re.compile(r"(?:CF_API_TOKEN|CLOUDFLARE_API_TOKEN)=[A-Za-z0-9._-]{20,}"),
    re.compile(r"-----BEGIN (?:RSA|OPENSSH|EC|DSA) PRIVATE KEY-----"),
)


def fail(message: str) -> int:
    print(f"FAIL: {message}", file=sys.stderr)
    return 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Valida el proyecto final offline")
    parser.add_argument("--project-dir", type=Path, required=True)
    parser.add_argument("--lab-dir", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    project_dir = args.project_dir.resolve()
    lab_dir = args.lab_dir.resolve()

    fixture = project_dir / "fixtures" / "sample-payload.json"
    current = lab_dir / "workspace" / "current-payload.json"
    previous = lab_dir / "workspace" / "previous-payload.json"

    for path in (fixture, current, previous):
        if not path.is_file():
            return fail(f"Falta archivo requerido: {path.name}")

    try:
        payload = json.loads(fixture.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"Fixture JSON inválido: {exc}")

    required_keys = {"operation", "node", "mode", "payload", "signature"}
    missing = required_keys.difference(payload)
    extra = set(payload).difference(required_keys)
    if missing:
        return fail(f"Faltan claves del fixture: {', '.join(sorted(missing))}")
    if extra:
        return fail(f"Claves no permitidas en el fixture: {', '.join(sorted(extra))}")

    expected_values = {
        "operation": "LAB_VALIDATE",
        "node": "nodo-estudiante-01",
        "mode": "offline",
        "payload": "LBH://COURSE/FINAL-PROJECT",
        "signature": "fixture-only-not-a-real-signature",
    }
    for key, expected in expected_values.items():
        if not isinstance(payload.get(key), str) or payload[key] != expected:
            return fail(f"Valor inválido para {key}")

    for workspace_path in (current, previous):
        try:
            workspace_payload = json.loads(workspace_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            return fail(f"Workspace JSON inválido en {workspace_path.name}: {exc}")
        if workspace_payload != expected_values:
            return fail(f"Payload de workspace inválido: {workspace_path.name}")

    scan_roots = (project_dir / "fixtures", project_dir / "scripts")
    for root in scan_roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError as exc:
                return fail(f"No se pudo leer {path.name}: {exc}")
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    return fail(f"Posible secreto en {path.relative_to(project_dir)}")

    private_markers = ("/home/", "/data/data/", "/sdcard/", "C:\\Users\\")
    for path in (project_dir / "README.md",):
        if path.is_file():
            text = path.read_text(encoding="utf-8", errors="replace")
            if any(marker in text for marker in private_markers):
                return fail(f"Ruta privada detectada en {path.name}")

    if current.read_bytes() != previous.read_bytes():
        print("INFO: current-payload.json difiere de previous-payload.json; rollback disponible.")

    print("OK: Fixture, workspace, higiene y estructura verificados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
