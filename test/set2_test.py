import unittest
from os import path, chdir
from set2 import *

test_directory = path.dirname(path.realpath(__file__))

class TestSet2(unittest.TestCase):

    def test_challenge_9(self):
        input_string = "YELLOW SUBMARINE"
        block_size = 20

        expected_output_string = "YELLOW SUBMARINE\x04\x04\x04\x04"

        output_string = challenge_9.main(input_string, block_size)

        self.assertEqual(output_string, expected_output_string)

    def test_challenge_10(self):
        input_file = open(test_directory +
                          "/data/challenge-10-data.txt").read()

        ciphertext = input_file.decode("base64")
        key = b'YELLOW SUBMARINE'
        IV = "\x00" * 16

        output_file = test_directory + "/output/challenge-10-output.txt"
        expected_output_string = open(output_file).read()

        decrypted, encrypted = challenge_10.main(ciphertext, key, IV)

        self.assertEqual(decrypted, expected_output_string)
        self.assertEqual(encrypted, ciphertext)

    def test_challenge_11(self):
        # Test five times
        self.assertTrue(challenge_11.main())
        self.assertTrue(challenge_11.main())
        self.assertTrue(challenge_11.main())
        self.assertTrue(challenge_11.main())
        self.assertTrue(challenge_11.main())

    def test_challenge_12(self):
        input_file = open(test_directory +
                          "/data/challenge-12-data.txt").read()

        plaintext = input_file.decode('base64')

        output = challenge_12.main(plaintext)

        self.assertEqual(plaintext, output)

    def test_challenge_13(self):
        admin_profile = challenge_13.main()

        self.assertIn('role', admin_profile)
        self.assertEqual(admin_profile['role'], 'admin')

    def test_challenge_14(self):
        input_file = open(test_directory +
                          "/data/challenge-14-data.txt").read()

        plaintext = input_file.decode('base64')

        output = challenge_14.main(plaintext)

        self.assertEqual(plaintext, output)

    def test_challenge_15(self):
        good_input = "ICE ICE BABY\x04\x04\x04\x04"

        expected_output_string = "ICE ICE BABY"

        output_string = challenge_15.main(good_input)

        self.assertEqual(output_string, expected_output_string)

        bad_input1 = "ICE ICE BABY\x05\x05\x05\x05"

        self.assertRaises(Exception, challenge_15.main, bad_input1)

        bad_input2 = "ICE ICE BABY\x01\x02\x03\x04"

        self.assertRaises(Exception, challenge_15.main, bad_input2)

    def test_challenge_16(self):
        self.assertTrue(challenge_16.main())
