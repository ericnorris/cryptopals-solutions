from Crypto.Cipher import AES
from cryptopals.set2.challenge_9 import pkcs7_pad

# This challenge requires the use of the PyCrypto module
# https://github.com/dlitz/pycrypto

def fixed_xor(str1, str2):
    """Return the result of str1 ^ str2."""
    return ''.join([chr(ord(a) ^ ord(b)) for a, b in zip(str1, str2)])

def block_iterator(text, block_size):
    """Group text into a set of block_size blocks."""
    return [''.join(block) for block in zip(*([iter(text)] * block_size))]

def encrypt_aes_cbc(plaintext, key, IV):
    """Encrypt the given plaintext using AES with CBC."""

    # Set up the cipher
    cipher = AES.new(key, AES.MODE_ECB)

    # Block size
    block_size = 16

    # Pad the plaintext
    plaintext = pkcs7_pad(plaintext, block_size)

    # Use the IV
    previous_block = IV

    ciphertext = ""

    for plain_block in block_iterator(plaintext, block_size):
        # XOR the block with the previous block and encrypt it
        cipher_block = cipher.encrypt(fixed_xor(plain_block, previous_block))
        ciphertext += cipher_block

        previous_block = cipher_block

    return ciphertext

def decrypt_aes_cbc(ciphertext, key, IV):
    """Decrypt the given ciphertext using AES with CBC."""

    # Set up the cipher
    cipher = AES.new(key, AES.MODE_ECB)

    # Block size
    block_size = 16

    # Use the IV
    previous_block = IV

    plaintext = ""

    for cipher_block in block_iterator(ciphertext, block_size):
        # Decrypt the block and XOR it with the previous block
        plaintext += fixed_xor(cipher.decrypt(cipher_block), previous_block)

        previous_block = cipher_block

    # Strip the padding
    padding_length = ord(plaintext[-1])
    plaintext = plaintext[:-padding_length]

    return plaintext

def main(ciphertext, key, IV):
    """Decrypt the ciphertext, and then encrypt with the same key/IV."""
    decrypted = decrypt_aes_cbc(ciphertext, key, IV)
    encrypted = encrypt_aes_cbc(decrypted, key, IV)

    return (decrypted, encrypted)