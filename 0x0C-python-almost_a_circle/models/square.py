#!/usr/bin/python3
""" class inherited from Rectangle """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square inherited from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """" inheriting attributes from Rectangle """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """updating __str__"""
        return("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width))

    @property
    def size(self):
        """ getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns/upsates class square attributes """
        if len(args):
            for i, val in enumerate(args):
                if i == 0:
                    self.id = val
                elif i == 1:
                    self.size = val
                elif i == 2:
                    self.x = val
                elif i == 3:
                    self.y = val
        else:
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
        """Returns the dictionary representation of a Square """
        dict_key = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dict_key
