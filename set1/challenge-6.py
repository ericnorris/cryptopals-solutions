from __future__ import division
import base64
import math
from sys import maxint

# Imported (with heavy modification) from challenge 4
# TODO refactor out into util module of some sort
import collections
import string

expected_frequency = collections.defaultdict(int, {
    ' ': .1217,
    'a': .0609,
    'b': .0105,
    'c': .0284,
    'd': .0292,
    'e': .1136,
    'f': .0179,
    'g': .0138,
    'h': .0341,
    'i': .0544,
    'j': .0024,
    'k': .0041,
    'l': .0292,
    'm': .0276,
    'n': .0544,
    'o': .0600,
    'p': .0195,
    'q': .0024,
    'r': .0495,
    's': .0568,
    't': .0803,
    'u': .0243,
    'v': .0097,
    'w': .0138,
    'x': .0024,
    'y': .0130,
    'z': .0003,
    '_': .0657,
})

def recover_xor_key(cipher_text):
    xor_text_map = {
        char: single_byte_xor(cipher_text, char) for char in string.printable
    }

    scores = {
        char: score_text(text) for char, text in xor_text_map.items()
    }

    return min(scores, key = scores.get)


def single_byte_xor(string, character):
    return ''.join([chr(ord(a) ^ ord(character)) for a in string])

def score_text(text):
    counter = collections.Counter([
        char.lower() if char not in string.punctuation else '_'
        for char in text
    ])

    total = len(text)

    return sum([
        math.pow(abs(expected_frequency[char] - (count / total)), 2)
        if char in string.printable else 1
        for char, count in counter.items()
    ])

### End of import

def hamming_distance(s1, s2):
    return sum([
        bin(ord(ch1) ^ ord(ch2)).count("1")
        for ch1, ch2 in zip(s1, s2)
    ])

def guess_keysize(text, start, end, blocks):
    keysize_scores = list()
    for keysize in range(start, end):
        block_iter = (item for item in zip(*[iter(text)]*keysize))

        score = sum([
            hamming_distance(block_iter.next(), block_iter.next()) / keysize
            for i in range(0, blocks * 2)
        ]) / blocks

        keysize_scores.append((keysize, score))

    return sorted(keysize_scores, key = lambda pair: pair[1])

def blockify(text, block_size):
    text_length = int(len(text) / block_size) * block_size
    return [text[i:i + block_size] for i in range(0, text_length, block_size)]

def transpose(blocks):
    return [''.join(block) for block in zip(*blocks)]

def repeating_xor_decrypt(text, key):
    padded_key = key * int(math.ceil(len(text) / len(key)))

    decrypted = [chr(ord(a) ^ ord(b)) for a, b in zip(text, padded_key)]

    return ''.join(decrypted)

if __name__ == '__main__':
    data_file = open("challenge-6-data.txt")
    decoded = base64.b64decode(data_file.read())

    keysize_scores = guess_keysize(decoded, 2, 40, 3)

    # Try the top 3 keys
    best_key = None
    best_result = None
    best_score = maxint
    for keysize, score in keysize_scores[:3]:
        xor_blocks = transpose(blockify(decoded, keysize))
        key = ''.join([recover_xor_key(block) for block in xor_blocks])

        decrypted = repeating_xor_decrypt(decoded, key)
        decryption_score = score_text(decrypted)

        if (decryption_score < best_score):
            best_key = key
            best_result = decrypted
            best_score = decryption_score

    print "key: ", best_key
    print "result: ", best_result
