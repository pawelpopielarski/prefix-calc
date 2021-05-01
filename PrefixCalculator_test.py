import unittest
import PrefixCalculator

class TestPrefixCalculator(unittest.TestCase):
    def setUp(self):
        self.target = PrefixCalculator.PrefixCalculator()

    def test_init(self):
        self.assertEqual(0, len(self.target.stack))

    def test_calculate_negative(self):
        with self.assertRaises(PrefixCalculator.InvalidInputError):
            self.target.calculate(['0','0'])
        with self.assertRaises(PrefixCalculator.InvalidInputError):    
            self.target.calculate(['0','0','*','0'])
        with self.assertRaises(PrefixCalculator.InvalidInputError):    
            self.target.calculate(['*','*','0','0'])
        with self.assertRaises(PrefixCalculator.InvalidInputError):    
            self.target.calculate(['0','0','*'])

    def test_state_clear_after_invalid_input(self):
        with self.assertRaises(PrefixCalculator.InvalidInputError):
            self.target.calculate(['0','0'])

        self.assertEqual(1, self.target.calculate(['-','3','2']))
        
    def test_calculate_positive(self):
        self.assertEqual(0, self.target.calculate([]))
        self.assertEqual(-3, self.target.calculate(['-','0','3']))
        self.assertEqual(7, self.target.calculate(['+','1','*','2','3']))
        self.assertEqual(-1, self.target.calculate(['-','2','3']))
        self.assertEqual(1, self.target.calculate(['-','3','2']))
        self.assertEqual(3, self.target.calculate(['+','2','1']))
        self.assertEqual(5, self.target.calculate(['+', '*', '1', '2', '3']))
        self.assertEqual(3, self.target.calculate(['-', '/', '10', '+', '1', '1', '*', '1', '2']))
        self.assertEqual(1.5, self.target.calculate(['/','3','2']))

if __name__ == '__main__':
    unittest.main()