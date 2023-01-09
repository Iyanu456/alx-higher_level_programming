#!/usr/bin/python3
"""
Function to check if an object is an instance of a class

"""


def is_same_class(obj, a_class):
    """
    checks if an object is an instance of a class

    @param: obj (any): The object to check
    @param: a_class (type): The class to match the type  of object to

    """

    if type(obj) == a_class:
        return True
    return False
