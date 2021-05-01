import sys
from collections import deque

#move to another file
class InvalidInputError(Exception):
    pass

"""
> 3
3
> + 1 2
3
> + 1 * 2 3
7
> + * 1 2 3
5
> - / 10 + 1 1 * 1 2
3
> - 0 3
-3
> / 3 2
1 (or 1.5)
"""
class PrefixCalculator(object):
    operations = {
        '+': lambda a,b: a+b,
        '-': lambda a,b: a-b,
        '*': lambda a,b: a*b,
        '/': lambda a,b: a/b,
    }

    def __init__(self):
        self.stack = deque()

    def validate(self, arg) -> None:
        """
        validate that arg is a proper argument for calculation
        i.e. it is either an integer or {+, -, *, /}
        """
        if arg in self.operations.keys():
            return
        
        try:
            val = int(arg, base=10)
        except(ValueError):
            raise InvalidInputError('{0} argument invalid'.format(arg))

    def calculate(self, args) -> int:
        """
        args support the operators {+, -, *, /} and integers
        """
        if not len(args):
            return 0
        
        while len(args):
            arg = args.pop()
            self.validate(arg)
            self.__step(arg)

        if len(self.stack) > 1:
            raise InvalidInputError('Not enough operations to perform calculation')

        return self.stack.pop()

    def __step(self, arg) -> None:
        if not arg in self.operations.keys():
            self.stack.append(int(arg))
            return

        if len(self.stack) < 2:
            raise InvalidInputError('Too many operations for given operands')

        top = self.stack.pop()
        bottom = self.stack.pop()
        val = self.operations[arg](top, bottom)
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

