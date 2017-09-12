#!/usr/bin/python3
""" class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ inherited from class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization of rectangle attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value


"""
    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__y):
            print()

        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            print('#' * self.__width)

    def __str__(self):
        return ("[Rectangle] {} {}/{} - {}/{}".format(self.id, self.__x,
                                                      self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        # assigns argument to attributes
        for idx, arg in enumerate(args):
            if idx == 0:
                self.id = arg
            elif idx == 1:
                self.width = arg
            elif idx == 2:
                self.height = arg
            elif idx == 3:
                self.x = arg
            elif idx == 4:
                self.y = arg

        for key, val in kwargs.items():
            if key == "id":
                self.id = val
            elif key == "width":
                self.width = val
            elif key == "height":
                self.height = val
            elif key == "x":
                self.x = val
            elif key == "y":
                self.y = val

    def to_dictionary(self):
        dict_key = {"id": self.id, "width": self.width,
                    "height": self.height, "x": self.x, "y": self.y}
        return dict_key

"""
"""
for **kwargs:
should work, theoretially:
        keydict={}
        for key, val in kwargs.items():
            keydict[key] = val
        self.__dict__.update(keydict)
"""
