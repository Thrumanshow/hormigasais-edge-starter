from .constants import TYPE_CODES

def make_header(node_id="A16", version="00"):
    return (
        node_id.encode().hex()[:4].ljust(4,"0") +
        version.encode().hex()[:4].ljust(4,"0")
    )

def encode_packet(header, type_code, payload):
    payload_hex = payload.encode().hex()
    length = format(len(payload_hex)//2,"08x")
    return f"{header}{type_code}{length}{payload_hex}"
