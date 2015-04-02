import base64

def detect_ecb(ciphertext):
    # Look for repeating blocks
    block_size = 16
    blocks = [ciphertext[i:i+block_size]
              for i in range(0, len(ciphertext), block_size)]

    return len(blocks) != len(set(blocks))

if __name__ == '__main__':
    data_file = open("challenge-8-data.txt")
    line_number = 0

    for line in data_file:
        ciphertext = base64.b16decode(line.rstrip(), True)

        if (detect_ecb(ciphertext)):
            print "ecb detected on line", line_number

        line_number += 1
