import unittest, random
from string import ascii_lowercase

import PrefixCalculator

class TestPrefixCalculator(unittest.TestCase):
    def setUp(self):
        self.target = PrefixCalculator.PrefixCalculator()

    def test_calculate(self):
        self.assertEqual(0, self.target.calculate([]))

    def test_validate_correct_operators(self):
        for op in ['+','-','*','/']:
            self.assertTrue(self.target.is_valid(op))

    def test_validate_correct_simple_numbers(self):
        for i in range(1000):
            val = str(i)
            self.assertTrue(self.target.is_valid(val))

    def test_validate_correct_random_numbers(self):
        for i in range(1000):
            rand = str(random.randint(0, 10000000))
            self.assertTrue(self.target.is_valid(rand), '{0} is not valid'.format(rand))

    def test_validate_incorrect_input(self):
        for op in ascii_lowercase:
            self.assertFalse(self.target.is_valid(op), '{0} is not valid'.format(op))

        for i in range(1000):
            rand = str(random.randint(-10000000, -1))
            self.assertFalse(self.target.is_valid(rand), '{0} is not valid'.format(rand))

if __name__ == '__main__':
    unittest.main()