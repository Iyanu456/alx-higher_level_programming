#!/usr/bin/python3
"""Square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """instantiation with size"""

        self.integer_validator(self)
        self.__size = size
        super().__init__(self.__size, self.__size)
