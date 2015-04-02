import base64
from Crypto.Cipher import AES

# This challenge requires the use of the PyCrypto module
# https://github.com/dlitz/pycrypto

def decrypt_aes_ecb(key, ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    padding_length = ord(padded_plaintext[-1])
    plaintext = padded_plaintext[:-padding_length]

    return plaintext

if __name__ == '__main__':
    data_file = open("challenge-7-data.txt")

    decoded = base64.b64decode(data_file.read())

    print decrypt_aes_ecb(b'YELLOW SUBMARINE', decoded)
