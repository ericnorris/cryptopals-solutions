import base64
from cryptopals.set1.common import recover_xor_key

def main(hex_string):
    decoded = base64.b16decode(hex_string, True)

    key, score, text = recover_xor_key(decoded)

    return text
