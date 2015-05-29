def pkcs7_strip(plaintext):
    """Strip PKCS#7 padding from plaintext, or raise exception if invalid."""
    padding_size = ord(plaintext[-1])
    padding = plaintext[-padding_size:]

    expected_padding = ''.join([
        chr(padding_size) for i in xrange(0, padding_size)
    ])

    if padding != expected_padding or padding_size == 0:
        raise Exception('Invalid PKCS#7 padding')

    return plaintext[:-padding_size]

def main(plaintext):
    return pkcs7_strip(plaintext)
