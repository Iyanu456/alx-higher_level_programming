#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """class BaseGeometry"""

    def integer_validator(self, name, value):
        """Validates if value is an integer greater than 0"""

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")

        if value <= 0:
            raise ValueError("<name> must be graeter than 0")

    def area(self):
        """area not implemented"""

        raise Exception("area() is not implemented")
