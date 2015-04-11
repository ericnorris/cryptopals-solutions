import base64
from common import recover_xor_key

def main(data):
    line_scores = {
        score: text for _, score, text in [
            recover_xor_key(base64.b16decode(line.rstrip(), True))
            for line in data
        ]
    }

    best_score = min(line_scores)

    return line_scores[best_score]
