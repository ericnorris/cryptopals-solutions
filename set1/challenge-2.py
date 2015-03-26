import base64

def fixed_xor(hex_a, hex_b):
    decoded_a = base64.b16decode(hex_a, True)
    decoded_b = base64.b16decode(hex_b, True)
    xor_result = [chr(ord(a) ^ ord(b)) for a, b in zip(decoded_a, decoded_b)]

    return base64.b16encode(''.join(xor_result))

if __name__ == '__main__':
    hex_a = raw_input("hex_a> ")
    hex_b = raw_input("hex_b> ")

    print fixed_xor(hex_a, hex_b)
