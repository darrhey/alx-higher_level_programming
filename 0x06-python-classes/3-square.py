#!/usr/bin/python3
"""Square generation module for 0x06
"""
class Square:
    """class defined for square generation
Args:
size(int): length of one side of square
Attributees:
__size(int): length of one side of square
Raises:
TypeError: if size is not an integer
ValueError: if size is less than 0
"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        
    def area(self):
        return self.__size**2
