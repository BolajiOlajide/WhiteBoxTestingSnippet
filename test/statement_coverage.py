import unittest

from app.main import multiples


class TestStatementCoverage(unittest.TestCase):
    """Test cases for the multiples function"""

    def test_correct_multiples(self):
        self.assertTrue(multiples(2, 4))

    def test_incorrect_multiples(self):
        self.assertFalse(multiples(3, 4))

    def test_same_number_as_multiple(self):
        with self.assertRaises(Exception) as context:
            multiples(2, 2)
        self.assertEqual(str(context.exception),
                         'Numbers should not be the same.')

if __name__ == '__main__':
    unittest.main()