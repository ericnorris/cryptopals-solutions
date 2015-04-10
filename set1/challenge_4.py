from __future__ import division
import base64
import collections
import string

expected_frequency = {
    'e': .12702,
    't': .9056,
    'a': .8167,
    'o': .7507,
    'i': .6966,
    'n': .6749,
    's': .6327,
    'h': .6094,
    'r': .5987,
    'd': .4253,
    'l': .4025,
    'c': .2782,
    'u': .2758,
    'm': .2406,
    'w': .2360,
    'f': .2228,
    'g': .2015,
    'y': .1974,
    'p': .1929,
    'b': .1492,
    'v': .0978,
    'k': .0772,
    'j': .0153,
    'x': .0150,
    'q': .0095,
    'z': .0074
}

def decrypt_message(hex_string):
    decoded = base64.b16decode(hex_string, True)

    xor_text_map = {
        char: single_byte_xor(decoded, char) for char in string.printable
    }

    scores = {
        char: score_text(text) for char, text in xor_text_map.items()
    }

    best_result = max(scores, key = scores.get)

    return (scores[best_result], xor_text_map[best_result])


def single_byte_xor(string, character):
    return ''.join([chr(ord(a) ^ ord(character)) for a in string])

def score_text(text):
    counter = collections.Counter(text.lower())
    total = sum(counter.values())

    return sum([
        (expected_frequency[char] if char in expected_frequency else 0)
        - (count / total)
        for char, count in counter.items()
    ])

if __name__ == '__main__':
    data_file = open("challenge-4-data.txt")

    best_score = 0
    best_string = None

    for line in data_file:
        score, text = decrypt_message(line.rstrip())

        if (score > best_score):
            best_score = score
            best_string = text

    print best_string,
