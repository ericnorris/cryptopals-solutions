import base64
from common import recover_xor_key

def main(hex_string):
    decoded = base64.b16decode(hex_string, True)

    key, text = recover_xor_key(decoded)

    return text
