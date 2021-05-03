import unittest, random
from string import ascii_lowercase

import validation
import calcerrors

class TestValidation(unittest.TestCase):
    def setUp(self):
        self.keys = ['+','-','*','/']

    def test_sanitize_input_too_many_args(self):
        with self.assertRaises(calcerrors.InvalidInputError) as ctx:
            validation.sanitize_input(['1', '2'], "msg")
        
        self.assertTrue(str(ctx.exception).startswith('Please enclose'))

    def test_sanitize_input_zero_args(self):
        msg = 'msg'
        with self.assertRaises(calcerrors.InvalidInputError) as ctx:
            validation.sanitize_input([], msg)
        
        self.assertEqual(msg, str(ctx.exception))

    def test_sanitize_input(self):
        arg = 'statement'
        ret = validation.sanitize_input([arg], 'nothing')
        self.assertEqual(arg.split(), ret)

    def test_validate_correct_operators(self):
        for op in self.keys:
            validation.validate(op, self.keys)

    def test_validate_correct_simple_numbers(self):
        for i in range(1000):
            val = str(i)
            validation.validate(val, self.keys)

    def test_validate_correct_random_numbers(self):
        for i in range(1000):
            rand = str(random.randint(0, 10000000))
            validation.validate(rand, self.keys)

    def test_validate_incorrect_input(self):
        for op in ascii_lowercase:
            with self.assertRaises(calcerrors.InvalidInputError):
                validation.validate(op, self.keys)

if __name__ == '__main__':
    unittest.main()