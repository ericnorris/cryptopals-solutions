import unittest
from os import path, chdir
from set2 import *

class TestSet2(unittest.TestCase):

    def test_challenge_9(self):
        input_string = "YELLOW SUBMARINE"
        block_size = 20

        expected_output_string = "YELLOW SUBMARINE\x04\x04\x04\x04"

        output_string = challenge_9.main(input_string, block_size)

        self.assertEqual(output_string, expected_output_string)
