from cryptopals.util.pkcs_7 import pkcs7_pad


def main(plaintext, blocksize):
    return pkcs7_pad(plaintext, blocksize)
