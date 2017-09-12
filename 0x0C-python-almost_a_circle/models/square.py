#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width))

"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        for idx, val in enumerate(args):
            if idx == 0:
                self.id = val
            if idx == 1:
                self.size = val
            if idx == 2:
                self.x == val
            if idx == 3:
                self.y == val

        for key, val in kwargs.items():
            if key == "id":
                self.id = val
            if key == "size":
                self.size = val
            if key == "x":
                self.x = val
            if key == "y":
                self.y = val

    def to_dictionary(self):
        dict_key = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dict_key
"""
