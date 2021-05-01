import sys
from collections import deque

from calcerrors import InvalidInputError
import validation, operations

class PrefixCalculator(object):
    ops = operations.get()

    def __init__(self):
        self.stack = deque()

    def calculate(self, args) -> int:
        """
        args support operators {+, -, *, /} and integers
        """
        if not len(args):
            return 0

        self.stack.clear()
        
        while len(args):
            arg = args.pop()
            validation.validate(arg, self.ops.keys())
            self.__step(arg)

        if len(self.stack) > 1:
            raise InvalidInputError('Not enough operations to perform calculation')

        return self.stack.pop()

    def __step(self, arg) -> None:
        if not arg in self.ops.keys():
            self.stack.append(int(arg))
            return

        if len(self.stack) < 2:
            raise InvalidInputError('Too many operations for given operands')

        top = self.stack.pop()
        bottom = self.stack.pop()
        val = self.ops[arg](top, bottom)
        self.stack.append(val)

def main():
    args = sys.argv[1:]
    try:
        calc = PrefixCalculator()
        print(calc.calculate(args))
    except(InvalidInputError) as e:
        print(e)

if __name__ == "__main__":
    main()

