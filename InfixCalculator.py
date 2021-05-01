import sys
from collections import deque

import PrefixCalculator
from calcerrors import InvalidInputError
import validation, operations

class InfixCalculator(object):
    ops = operations.get()

    def calculate(self, args) -> int:
        """
        args support parentheses, operators {+, -, *, /} and integers
        """
        if not len(args):
            return 0

        result = self.__transform(args)
        print(result)
        result.reverse()
        print(result)
        calc = PrefixCalculator.PrefixCalculator()
        return calc.calculate(result)

    def __transform(self, args) -> list:
        output = deque()
        operators = deque()
        symbols_allowed = ['(',')']
        for op in self.ops.keys():
            symbols_allowed.append(op)
        
        for arg in args:
            validation.validate(arg, symbols_allowed)

            if arg == '(':
                operators.append(arg)
            elif arg == ')':
                found = False
                while len(operators):
                    val = operators.pop()
                    if val == '(':
                        found = True
                        break
                    output.append(val)

                if not found:
                    raise InvalidInputError('Parentheses mismatch')

            elif arg in self.ops.keys():
                while len(operators):
                    var = operators.pop()
                    if var == '(':
                        operators.append('(')
                        break
                    output.append(var)
                
                operators.append(arg)

            else:
                output.append(arg)

        while len(operators):
            val = operators.pop()
            if not val in self.ops.keys():
                raise InvalidInputError('Parentheses mismatch')

            output.push(val)
        
        return output

def main():
    args = sys.argv[1:]
    try:
        calc = InfixCalculator()
        print(calc.calculate(args))
    except(InvalidInputError) as e:
        print(e)

if __name__ == "__main__":
    main()