from calcerrors import InvalidInputError

def sanitize_input(arg, msg) -> list:
    if len(arg) > 1:
        raise InvalidInputError('Please enclose the statement in ""')
    elif len(arg) == 0:
        raise InvalidInputError(msg)

    return arg[0].split()

def validate(arg, keys) -> None:
    """
    validate that arg is a proper argument for calculation
    """
    if arg in keys:
        return
    
    try:
        val = int(arg, base=10)
    except(ValueError):
        raise InvalidInputError('{0} argument invalid'.format(arg))