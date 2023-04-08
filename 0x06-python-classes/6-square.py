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

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

        
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


    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for y in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(type(i) != int for i in value) or any(j < 0 for j in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
