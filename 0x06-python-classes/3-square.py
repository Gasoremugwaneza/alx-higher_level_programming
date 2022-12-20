#!/usr/bin/python3
# defining area of square
"""
    including an area method
"""


class Square:
    """ creating class square """
    def __init__(self, size=0):
        """ instantiation of class square """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ defining area of square """
        return self.__size * self.__size
