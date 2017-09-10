#!/usr/bin/python3


class Student():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        self_dict = self.__dict__.copy
        new = {}
        if attrs == None:
            return self.__dict__
        for i in attrs:
            if i == self_dict[i]:
                new.append(i)
        return new.__dict__
