#!/usr/bin/python3
"""Rectangle module for 0x08
"""
class Rectangle:
    """class defined for calculating area or perimeter
of Rectangle
"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self._height) * 2

    def _draw_rectangle(self):
        str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                str += '#'
            if self.__width != 0 and i < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        return self._draw_rectangle()
