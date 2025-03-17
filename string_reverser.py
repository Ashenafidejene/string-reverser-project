def reverse_string(s):
    """Reverse the input string."""
    return s[::-1]

import unittest

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("12345"), "54321")
        self.assertEqual(reverse_string(""), "")

if __name__ == '__main__':
    unittest.main()