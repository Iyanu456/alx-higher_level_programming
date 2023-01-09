#!/usr/bin/python3
"""Checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class

    @param: obj (any): object to be checked
    @param: a_class (type): class type to match object with

    """

    return (isinstance(obj, a_class))
