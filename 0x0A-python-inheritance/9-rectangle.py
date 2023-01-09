#!/usr/bin/python3
"""Rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Implements a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """Calculates the area of the rectangle"""

        return (self.__width * self.__height)

    def __str__(self):
        """print"""

        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
