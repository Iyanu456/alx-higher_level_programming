#!/usr/bin/python3
"""
Module that contains the say_my_name function

say_my_name: prints a name

"""


def say_my_name(first_name, last_name=""):
    """
    Prints a name in the format:
    My name is <first_name> <last_name>

    :param a: <first_name> (str)
    :param b: <last_name> (str)
    :return: None

    >>> say_my_name("Abraham", "Lincoln")
    My name is Abraham Lincoln

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

    return
