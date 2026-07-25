def decode_packet(frame):
    return {
        "header":frame[:8],
        "type_code":frame[8:16],
        "length":int(frame[16:24],16),
        "payload":bytes.fromhex(frame[24:]).decode()
    }
