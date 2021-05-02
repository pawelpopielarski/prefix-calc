import unittest
import flask
import json

from CalcService import index, help, infix, prefix

class CalcService(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask('test')

    def test_index(self):
        with self.app.test_request_context():
            ret = index()
            self.assertEqual('GET /calc/v1 for detailed API description', ret)
    
    def test_help(self):
        with self.app.test_request_context():
            ret = help()
            self.assertTrue(ret.startswith('POST /calc/v1/infix'))
    
    def helper_no_json(self, ret):
        self.assertEqual(400, ret.status_code)
        val = json.loads(ret.response[0])
        self.assertEqual('no json', val['error'])

    def helper_invalid_json(self, ret):
        self.assertEqual(400, ret.status_code)
        val = json.loads(ret.response[0])
        self.assertEqual('statement field missing in json', val['error'])

    def test_validate_no_json(self):
        with self.app.test_request_context():
            self.helper_no_json(infix())
        
        with self.app.test_request_context():
            self.helper_no_json(prefix())

    def test_validate_invalid_json(self):
        invalid = '{"some":"param"}'
        with self.app.test_request_context(json=invalid):
            self.helper_invalid_json(infix())
        
        with self.app.test_request_context(json=invalid):
            self.helper_invalid_json(prefix())

    def helper_calc_positive(self, ret, result):
        self.assertEqual(200, ret.status_code)
        val = json.loads(ret.response[0])
        self.assertEqual(result, val['result'])

    def test_prefix_positive(self):
        with self.app.test_request_context(json={'statement': '- / 10 + 1 1 * 1 2'}):
            self.helper_calc_positive(prefix(), '3.0')

    def test_infix_positive(self):
        with self.app.test_request_context(json={'statement': '( ( 1 * 2 ) + 3 )'}):
            self.helper_calc_positive(infix(), '5')

    def helper_invalid_statement(self, ret, msg):
        self.assertEqual(400, ret.status_code)
        val = json.loads(ret.response[0])
        self.assertEqual(msg, val['error'])

    def test_prefix_negative(self):
        with self.app.test_request_context(json={'statement': '- / 10 + 1 1 * * 1 2'}):
            self.helper_invalid_statement(prefix(), 'Too many operations for given operands')

    def test_prefix_negative(self):
        with self.app.test_request_context(json={'statement': '( ( 1 * 2 ) + 3 ) )'}):
            self.helper_invalid_statement(infix(), 'Parentheses mismatch')

if __name__ == '__main__':
    unittest.main()