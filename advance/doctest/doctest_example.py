# run with pytest --doctest-modules

def something():
    """ a doctest in a docstring
    >>> something()
    42
    """
    return 42


def get_something():
    """ a doctest in a docstring
    >>> get_something()
    42
    """
    return 31
