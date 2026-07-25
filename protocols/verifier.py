import hashlib
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
