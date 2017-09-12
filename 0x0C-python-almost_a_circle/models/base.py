#!/usr/bin/python3
""" Module holding class Base """
import json


class Base:
    """ class Base  """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization for id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON representation of an object (string)"""
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        new_list = []
        filename = cls.__name__ + ".json"

        # convert each object in list_objs into dictionary
        for each in list_objs:
            # to_dictionary created in rectangle. access with cls.to_dictionary
            add_to_dict = cls.to_dictionary(each)

            # append each dictionary to a list
            new_list.append(add_to_dict)

            # to_jason converts list of dicts to string
            json_list = cls.to_json_string(new_list)

        with open(filename, 'w') as file:
            file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """ deserializes and returns json_string(list of JSON string)"""
        if json_string is None:
            return[]
        return json.loads(json_string)
