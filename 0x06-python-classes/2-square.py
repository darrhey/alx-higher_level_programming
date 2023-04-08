#!/usr/bin/python3
"""Square generation module for 0x06
"""
class Square:
    """class defined for square generation
"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
