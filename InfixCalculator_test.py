import unittest

import InfixCalculator

class TestInfixCalculator(unittest.TestCase):
    def setUp(self):
        self.target = InfixCalculator.InfixCalculator()

    def test_calculate(self):
        self.assertEqual(3, self.target.calculate(list('(1+2)')))
        self.assertEqual(7, self.target.calculate(list('(1+(2*3))')))
        self.assertEqual(5, self.target.calculate(list('((1*2)+3)')))
        self.assertEqual(-2, self.target.calculate(['(', '(', '(', '1', '+', '1', ')', '/', '10', ')', '-', '(', '1', '*', '2', ')', ')']))
        """
        > ( 1 + 2 )
        3
        > ( 1 + ( 2 * 3 ) )
        7
        > ( ( 1 * 2 ) + 3 )
        5
        > ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
        -2 (or -1.8)
        """

if __name__ == '__main__':
    unittest.main()