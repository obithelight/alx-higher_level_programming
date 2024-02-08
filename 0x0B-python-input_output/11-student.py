#!/usr/bin/python3
''' A Python Module '''


class Student:
    ''' Defines a student class '''

    def __init__(self, first_name, last_name, age):
        ''' Initialises a new student '''

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Gets a dictionary representation of the student '''

        if (type(attrs) is list and
                all(type(items) is str for items in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        ''' Replaces all attributes of the student instance '''

        for key, value in json.items():
            setattr(self, key, value)
