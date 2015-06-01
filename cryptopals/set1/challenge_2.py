import base64

def fixed_xor(str1, str2):
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)])

def main(hex_a, hex_b):
    decoded_a = hex_a.decode('hex')
    decoded_b = hex_b.decode('hex')

    result = fixed_xor(decoded_a, decoded_b)

    return base64.b16encode(result).lower()
