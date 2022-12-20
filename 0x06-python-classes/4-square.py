#!/usr/bin/python3
# updating private instance attribute
"""
    we will use getter and setter
"""


class Square:
    """ updating a privare instance attribute """
    def __init__(self, size=0):
        """ instantiation of class square """
        self.__size = size
    
    @property
    def size(self):
        """ getter for size """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ setter for size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__self = value
    
    def area(self):
        """ return an area of square """
        return (self.__size * self.__size)
