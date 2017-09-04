#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ returns whether object is instance inherited from specified class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
