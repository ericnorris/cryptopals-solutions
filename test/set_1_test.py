import unittest
from set1 import challenge_1
from set1 import challenge_2

class TestSet1(unittest.TestCase):

    def test_challenge_1(self):
        input_string = ''.join([
            "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f6",
            "9736f6e6f7573206d757368726f6f6d"
        ])

        expected_output_string = ''.join([
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        ])

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

if __name__ == '__main__':
    unittest.main()
