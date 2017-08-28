#!/usr/bin/python3


class Rectangle:
    """ rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width to given value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height to given value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ returns area of rectangle """
        return self.__width*self.__height

    def perimeter(self):
        """ returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width*2) + (self.__height*2)

    def __str__(self):
        """ returns string format of perimeter in '#'  """
        if self.__height == 0 or self.__width == 0:
            return ("")

        str = ''.join(('#' * self.__width + '\n') * self.__height)

        return str

    def __repr__(self):
        """ return a string representation of the rectangle"""
        return("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """del instance of rectangle"""
        print("Bye rectangle...")
