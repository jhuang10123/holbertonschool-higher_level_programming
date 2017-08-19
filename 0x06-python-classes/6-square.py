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


    def my_print(self):
        """ prints the square of size in '#' and position in ' '  """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)


    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ returns position"""
        if type(position) == tuple and len(position) is 2:
            if position[0] >= 0 and position[1] >= 0:
                return self.__position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
