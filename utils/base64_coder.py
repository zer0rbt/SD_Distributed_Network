import base64

def binary_to_base64(binary_bytes: bytes):
    return base64.b64encode(binary_bytes).decode('utf-8')

def base64_to_binary(base64_str: str):
    return base64.b64decode(base64_str.encode('utf-8'))