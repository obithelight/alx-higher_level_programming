#!/usr/bin/python3
''' A Python Module '''

import json


class Base:
    ''' Defines the base class '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initializes the base class '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Converts a list of dictionaries to a JSON string representation

        Args:
            list_dictionaries (list): A list of dictionaries
        '''

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Write the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances

        Returns:
            None
        '''
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
            f.write(json_string)
