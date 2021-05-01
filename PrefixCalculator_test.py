import unittest, random
from string import ascii_lowercase

import PrefixCalculator

class TestPrefixCalculator(unittest.TestCase):
    def setUp(self):
        self.target = PrefixCalculator.PrefixCalculator()

    def test_calculate(self):
        self.assertEqual(0, self.target.calculate([]))

    def test_calculate(self):
        self.assertEqual(7, self.target.calculate(['+','1','*','2','3']))
        self.assertEqual(-1, self.target.calculate(['-','2','3']))
        self.assertEqual(1, self.target.calculate(['-','3','2']))
        self.assertEqual(3, self.target.calculate(['+','2','1']))
        self.assertEqual(5, self.target.calculate(['+', '*', '1', '2', '3']))
        self.assertEqual(3, self.target.calculate(['-', '/', '10', '+', '1', '1', '*', '1', '2']))
        self.assertEqual(1.5, self.target.calculate(['/','3','2']))

    def test_validate_correct_operators(self):
        for op in ['+','-','*','/']:
            self.target.validate(op)

    def test_validate_correct_simple_numbers(self):
        for i in range(1000):
            val = str(i)
            self.target.validate(val)

    def test_validate_correct_random_numbers(self):
        for i in range(1000):
            rand = str(random.randint(0, 10000000))
            self.target.validate(rand)

    def test_validate_incorrect_input(self):
        for op in ascii_lowercase:
            with self.assertRaises(PrefixCalculator.InvalidInputError):
                self.target.validate(op)

if __name__ == '__main__':
    unittest.main()