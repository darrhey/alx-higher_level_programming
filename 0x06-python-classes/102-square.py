#!/usr/bin/python3
"""Square generation module for 0x06
"""
class Square:
    def __init__(self, size=0):
        self.__size = size

        
    def area(self):
        return self.__size**2


    @property
    def size(self):
        return self.__size


    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")


    def __lt__(self, other):
        return self.area() < other.area()


    def __le__(self, other):
        return self.area() <= other.area()


    def __eq__(self, other):
        return self.area() == other.area()


    def __ne__(self, other):
        return self.area() != other.area()


    def __gt__(self, other):
        return self.area() > other.area()


    def __ge__(self, other):
        return self.area() >= other.area()
