from itertools import cycle

def repeating_xor_encrypt(text, key):
    return ''.join([chr(ord(a) ^ ord(k)) for a, k in zip(text, cycle(key))])

def main(text, key):
    return repeating_xor_encrypt(text, key).encode("hex")
