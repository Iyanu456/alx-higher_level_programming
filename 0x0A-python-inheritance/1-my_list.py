#!/usr/bin/python3
"""
Class module that inherits from the list object

"""


class MyList(list):
    """ MyList class """

    def print_sorted(self):
        """ Prints the kist but sorted """

        print(sorted(self))
