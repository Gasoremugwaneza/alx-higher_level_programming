#!/usr/bin/pyhton3
# printing a square with # character
"""
    we are not allowed to import any module
"""


class Square:
    ''' defining a class square '''
    def __init__(self, size=0):
        """ instantiation of class """
        self.size = size

    @property
    def size(self):
        """ getter of size """
        return self.__size
    
    @size.setter
    def size(self, value):
        """ setter of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must >= 0")
        self.__size = value
    
    def area(self):
        """ return an area of square """
        return (self.__size * self.__size)
    
    def my_print(self):
        """ printing a square with # character """
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
