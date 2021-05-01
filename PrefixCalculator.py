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
    def __init__(self):
        self.valid_operations = ['+','-','*','/']

    def is_valid(self, arg) -> bool:
        """
        validate that arg is a proper argument for calculation
        """
        if arg in self.valid_operations:
            return True
        
        try:
            return int(arg, base=10) >= 0
        except(ValueError):
            return False

    def calculate(self, args) -> int:
        """
        args support the operators {+, -, *, /} and positive integers
        """
        if not len(args):
            return 0
        
        stack = deque()

        while len(args):
            arg = args.pop()
            if not self.is_valid(arg):
                raise InvalidInputError()

        return 0

def main():
    args = sys.argv[1:]
    print(args)
    try:
        calc = PrefixCalculator()
        print(calc.calculate(args))
    except(InvalidInputError):
        print("Invalid input")

if __name__ == "__main__":
    main()

