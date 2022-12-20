#!/usr/bin/python3
# a class that define a square
"""
    we are not allowed to import any module
"""


class Square:
    """ a class that define square """
    def __init__(self, size=0):
        """ instantiation of square class """
        if not isinstance(size, int):
            raise TypeError("size must an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self__size = size
