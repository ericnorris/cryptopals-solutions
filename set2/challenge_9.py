def pkcs7_pad(plaintext, blocksize):
    padding = blocksize - (len(plaintext) % blocksize)

    return plaintext + (chr(padding) * padding)

def main(plaintext, blocksize):
    return pkcs7_pad(plaintext, blocksize)
