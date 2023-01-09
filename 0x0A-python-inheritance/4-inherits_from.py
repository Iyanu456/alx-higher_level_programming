#!/usr/bin/python3
"""
Returns true if the object is an instance of a
class that inherited(directly or indirectly)

"""


def inherits_from(obj, a_class):
    """
    Checks if an object inherits from a class

    @params: obj (any): object to be checked
    @params: a_class (type): object type to match object with

    """

    return (type(obj) != a_class and isinstance(obj, a_class))
