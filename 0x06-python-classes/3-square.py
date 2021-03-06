#!/usr/bin/python3
class Square:
    """ Square class """
    def __init__(self, size=0):
        """ size of square(private) """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ finds area """
        return self.__size**2
