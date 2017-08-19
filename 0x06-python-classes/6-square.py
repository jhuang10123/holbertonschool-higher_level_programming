#!/usr/bin/python3
class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """ size and position of square(private) """
        if type(size) == int:
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__position = position

    def area(self):
        """ finds area of square """
        return self.__size**2

    @property
    def size(self):
        """ property for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set value for size if follow conditions """
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        return self.__size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ returns position"""
        if type(value) != tuple or len(value) != 2\
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """ prints the square of size in '#' and position in ' ' """
        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            print('#' * self.__size)
