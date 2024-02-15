#!/usr/bin/python3
''' A Python Module '''

import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        '''
        Converts a JSON string representation to a list of dictionaries

        Args:
            json_string (str): A JSON string representation
        '''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Creates an instance with all attributes already set

        Args:
            **dictionary: A dictionary containing attribute values

        Return:
            obj: An instance of the class with attributes set
        '''
        if dictionary or dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy_instance = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy_instance = cls(1)

            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        Load instances from a JSON file and returns a list of instances

        Returns:
            list: A list of instances loaded from the JSON file
        '''

        filename = cls.__name__ + ".json"

        try:
            with open(filename, "r") as file:
                # Read the contents of the file
                json_str = file.read()

                # Convert the JSON string to a list of dictionaries
                list_dict = cls.from_json_string(json_str)

                # Initialize an empty list to store instances
                instances = []

                # Create an instance for each dictionary and
                # append it to the list
                for item in list_dict:
                    instances.append(cls.create(**item))

                # Return the list of instances
                return instances
        except FileNotFoundError:
            # if file doesn't exist, return an empty list
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''
        Serialize a list of instances to a CSV file

        Args:
            list_objs (list): A list of instances

         Returns:
            None
        '''
        filename = cls.__name__ + ".csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file and return a list of instances.

        Returns:
            list: A list of instances loaded from the CSV file.
        """
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        id, width, height, x, y = map(int, row)
                        instances.append(cls(id, width, height, x, y))
                    elif cls.__name__ == 'Square':
                        id, size, x, y = map(int, row)
                        instances.append(cls(id, size, x, y))
        except FileNotFoundError:
            pass

        return instances
