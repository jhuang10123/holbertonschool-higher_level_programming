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









        # if self.integer_validator("width", self.__width):
        #     self.__width = width
        # if self.integer_validator("height", self.__height):
        #     self.__height = height


"""
width and height must be private.
must be positive integers, validated by integer_validator
no getter / setter """
