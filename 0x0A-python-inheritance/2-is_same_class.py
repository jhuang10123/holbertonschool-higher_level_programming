#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ returns whether object is exactly an instance of the specified class """
    return type(obj) is a_class
#    return isinstance(obj, a_class)
