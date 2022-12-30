#!/usr/bin/python3
"""
Module that contains the print_square function

print_square functions prints a square wit the `#` character
"""


def print_square(size):
    """
    Prints a square of size ```size```

    :param size: size of square (int)

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print(" ")
        return

    for i in range(size):
        print("#" * size)

    return
