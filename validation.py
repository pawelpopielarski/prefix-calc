from calcerrors import InvalidInputError

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