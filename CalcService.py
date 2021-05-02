from flask import Flask, request, make_response, jsonify

import PrefixCalculator, InfixCalculator
import calcerrors

app = Flask(__name__)

def handle_calc(req, calc):
    try:
        result = calc.calculate(req.json['statement'].split())
        return make_response(jsonify({'result': '{}'.format(result)}), 200)
    except(calcerrors.InvalidInputError) as e:
        return make_response(jsonify({'error': '{}'.format(str(e))}), 400)

def validate(r):
    if not r.data or not r.json:
        return False, make_response(jsonify({'error': 'no json'}), 400)
    if not 'statement' in r.json:
        return False, make_response(jsonify({'error': 'statement field missing in json'}), 400)
    return True, None

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return "GET /calc/v1 for detailed API description"

@app.route('/calc/v1', methods=['GET'])
def help():
    return "POST /calc/v1/infix\nPOST /calc/v1/prefix\nexample json for prefix:" + '{"statement":"- / 10 + 1 1 * 1 2"}'

@app.route('/calc/v1/infix', methods=['POST'])
def infix():
    valid, reply = validate(request)
    if not valid:
        return reply
    return handle_calc(request, InfixCalculator.InfixCalculator())

@app.route('/calc/v1/prefix', methods=['POST'])
def prefix():
    valid, reply = validate(request)
    if not valid:
        return reply
    return handle_calc(request, PrefixCalculator.PrefixCalculator())

if __name__ == "__main__":
    app.run(debug=True)