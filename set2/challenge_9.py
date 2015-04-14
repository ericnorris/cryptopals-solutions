def pkcs7_pad(plaintext, blocksize):
    """Pad the given plaintext to a multiple of the blocksize per PKCS #7."""
    padding = blocksize - (len(plaintext) % blocksize)

    return plaintext + (chr(padding) * padding)

def main(plaintext, blocksize):
    return pkcs7_pad(plaintext, blocksize)
