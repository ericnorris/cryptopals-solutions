import unittest
from os import path, chdir
from set1 import *

test_directory = path.dirname(path.realpath(__file__))

class TestSet1(unittest.TestCase):

    def test_challenge_1(self):
        input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b" \
                       "65206120706f69736f6e6f7573206d757368726f6f6d"

        expected_output_string = (
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        )

        output_string = challenge_1.main(input_string)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_2(self):
        input_strings = [
            "1c0111001f010100061a024b53535009181c",
            "686974207468652062756c6c277320657965"
        ]

        expected_output_string = "746865206b696420646f6e277420706c6179"

        output_string = challenge_2.main(*input_strings)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_3(self):
        input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78" \
                       "373e783a393b3736"

        expected_output_string = "Cooking MC's like a pound of bacon"

        output_string = challenge_3.main(input_string)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_4(self):
        input_file = open(test_directory + "/data/challenge-4-data.txt")

        expected_output_string = "Now that the party is jumping\n"

        output_string = challenge_4.main(input_file)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_5(self):
        text = "Burning 'em, if you ain't quick and nimble\n" \
               "I go crazy when I hear a cymbal"

        key = "ICE"

        expected_output_string = "0b3637272a2b2e63622c2e69692a23693a2a3c6324" \
                                 "202d623d63343c2a26226324272765272a282b2f20" \
                                 "430a652e2c652a3124333a653e2b2027630c692b20" \
                                 "283165286326302e27282f"

        output_string = challenge_5.main(text, key)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_6(self):
        input_file = open(test_directory + "/data/challenge-6-data.txt").read()
        ciphertext = input_file.decode("base64")

        expected_output_string = "Terminator X: Bring the noise"

        output_string = challenge_6.main(ciphertext)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_7(self):
        input_file = open(test_directory + "/data/challenge-7-data.txt").read()

        ciphertext = input_file.decode("base64")
        key = b'YELLOW SUBMARINE'

        output_file = test_directory + "/output/challenge-7-output.txt"
        expected_output_string = open(output_file).read()

        output_string = challenge_7.main(ciphertext, key)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_8(self):
        input_file = open(test_directory + "/data/challenge-8-data.txt")

        expected_output = 1

        output = challenge_8.main(input_file)

        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
