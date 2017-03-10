import unittest

from app.main import multiples


class TestStatementCoverage(unittest.TestCase):
    """Test cases for the multiples function"""

    def test_correct_multiples(self):
        self.assertFalse(multiples(3, 4))

    def test_incorrect_multiples(self):
        self.assertTrue(multiples(2, 4))

    def test_same_number_as_multiple(self):
        with self.assertRaises(Exception) as context:
            multiples(2, 2)
        self.assertEqual(str(context.exception),
                         'Numbers should not be the same.')

    def test_zero_multiple(self):
        with self.assertRaises(Exception) as context:
            multiples(0, 2)
        self.assertEqual(str(context.exception),
                         '0 is not valid.')

    def test_noninteger_multiples(self):
        with self.assertRaises(Exception) as context:
            multiples(1.2, 2)
        self.assertEqual(str(context.exception),
                         'Values must be integers.')

    def test_noninteger_multiple2(self):
        with self.assertRaises(Exception) as context:
            multiples(1.2, 2.4)
        self.assertEqual(str(context.exception),
                         'Values must be integers.')

    def test_impossible_multiples(self):
        with self.assertRaises(Exception) as context:
            multiples(4, 2)
        self.assertEqual(str(context.exception),
                         "Error! 2 isn't greater than 4.")

if __name__ == '__main__':
    unittest.main()