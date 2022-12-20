#!/usr/bin/python3
# a class with private instance attribute
"""
    we are not allowed to import any module
"""


class Square:
    """ a class with private instance attribute of size """
    def __init__(self, size):
        """ instantiation of class """
        self.__size = size
