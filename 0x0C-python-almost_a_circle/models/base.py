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
        """returns the JSON representation of an object (string)"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        new_list = []
        filename = cls.__name__ + ".json"

        # convert each object in list_objs into dictionary
        if list_objs is not None:
            for each in list_objs:
                # to_dictionary created in rectangle. access with
                # cls.to_dictionary
                add_to_dict = cls.to_dictionary(each)

                # append each dictionary to a list
                new_list.append(add_to_dict)

            # to_jason converts list of dicts to string
            new_list = cls.to_json_string(new_list)

        with open(filename, 'w') as file:
            file.write(new_list)

    @staticmethod
    def from_json_string(json_string):
        """deserializes and returns json_string(list of JSON string)"""
        if json_string is None:
            return[]
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ updating a class' attributes """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        new_list = []
        filename = cls.__name__ + ".json"
# attempt to open file, read content, and deserialize content
        try:
            with open(filename, 'w') as file:
                content = file.read()
                file = cls.from_json_string(content)
        except BaseException:
            return []

# update each element, add to list
        for elem in file:
            new_list.append(cls, **elem)
        return new_list
