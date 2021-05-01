import unittest

import InfixCalculator, calcerrors

class TestInfixCalculator(unittest.TestCase):
    def setUp(self):
        self.target = InfixCalculator.InfixCalculator()

    def test_calculate_positive(self):
        self.assertEqual(3, self.target.calculate(list('(1+2)')))
        self.assertEqual(7, self.target.calculate(list('(1+(2*3))')))
        self.assertEqual(5, self.target.calculate(list('((1*2)+3)')))
        self.assertEqual(-1.8, self.target.calculate(['(', '(', '(', '1', '+', '1', ')', '/', '10', ')', '-', '(', '1', '*', '2', ')', ')']))
        self.assertEqual(231, self.target.calculate(['16','-','(','3','*','(','4','-','8',')','/','(','5','-','3',')','*','(','16','+','20',')',')','-','1']))

    def test_calculate_negative(self):
        with self.assertRaises(calcerrors.InvalidInputError):
            self.target.calculate(list('(((1*2)+3)'))
        with self.assertRaises(calcerrors.InvalidInputError):
            self.target.calculate(list('1*2)+3)'))

if __name__ == '__main__':
    unittest.main()