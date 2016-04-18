import unittest
from broken import process_single, process

class Tests(unittest.TestCase):
    def test_single(self):
        (working_keys, text) = ( 5, "This can't be solved by brute force" )
        self.assertEqual( process_single(working_keys, text), 7)

    def test_chrs(self):
        self.assertEqual( process_single(3, "abcabcdef"), 6)

    def test_provided_input(self):
        sample_input = (
            "5\n"
            "This can't be solved by brute force.\n"
            "1\n"
            "Mississippi\n"
            "0\n"
            )
        expected_output = (
            "7\n"
            "2\n"
            )
        actual_output = process(sample_input)

        self.assertEqual(expected_output, actual_output)

if __name__=="__main__":
    unittest.main()


