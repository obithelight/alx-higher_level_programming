#!/usr/bin/python3
''' A Python Module '''

import json
import csv
import turtle


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
        """
        Write the CSV serialization of a list of objects to a file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)

        with open(file_name, "w") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=field_names)

            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return a list of classes instantiated from a CSV file.
        """
        # corrected the name of the file extension from .json to .csv
        file_name = "{}.csv".format(cls.__name__)
        try:
            with open(file_name, "r") as csvfile:
                if cls.__name__ == "Rectangle":
                    filednames = ["id", "width", "height", "x", "y"]
                else:
                    filednames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=filednames)

                new_list_dict = []

                converted_dict = {}

                for d in list_dicts:
                    for key, value in d.items():
                        converted_dict[key] = int(value)

                    new_list_dict.append(converted_dict)

                list_dicts = new_list_dict

                list_of_instances = []

                for d in list_dicts:
                    list_of_instances.append(cls.create(**d))

                return list_of_instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles,
        and Squares using the turtle module.
        """
        turt = turtle.Turtle()

        turt.screen.bgcolor("#3399FF")

        turt.pensize(4)

        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()

            turt.up()

            turt.goto(rect.x, rect.y)

            turt.down()

            for _ in range(2):
                turt.forward(rect.width)

                turt.left(90)

                turt.forward(rect.height)

                turt.left(90)

            turt.hideturtle()

        turt.color("#FFFF00")

        for sq in list_squares:
            turt.showturtle()

            turt.up()

            turt.goto(sq.x, sq.y)

            turt.down()

            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)

                turt.forward(sq.height)

                turt.left(90)

            turt.hideturtle()

        turtle.exitonclick()
