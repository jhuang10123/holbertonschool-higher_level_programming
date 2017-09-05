#!/usr/bin/python3
class BaseGeometry():
    """ BaseGeometry class """
    def area(self):
        """ raise exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ class inherited from BaseGeometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return("[Rectangle] {}/{}".format(self.__width, self.__height))

    def print(self):
        return self.area

class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        return self.__size**2

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
