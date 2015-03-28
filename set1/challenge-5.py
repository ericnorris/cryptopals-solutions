from __future__ import division
import math
import base64

def repeating_xor_encrypt(text, key):
    padded_key = key * int(math.ceil(len(text) / len(key)))

    encrypted = [chr(ord(a) ^ ord(b)) for a, b in zip(text, padded_key)]

    return base64.b16encode(''.join(encrypted))

if __name__ == '__main__':
    text = ("Burning 'em, if you ain't quick and nimble\n"
           "I go crazy when I hear a cymbal")
    key = "ICE"

    print repeating_xor_encrypt(text, key).lower()
