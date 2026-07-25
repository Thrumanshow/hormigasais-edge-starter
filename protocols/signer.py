import hashlib
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
