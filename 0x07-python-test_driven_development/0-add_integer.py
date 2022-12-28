#!/usr/bin/python3
"""Defines an integer addition function

:param a: int/float
:param b: int/float
"""


def add_integer(a, b=98):
    """Adds tow integers/floats together

    :return: int"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
