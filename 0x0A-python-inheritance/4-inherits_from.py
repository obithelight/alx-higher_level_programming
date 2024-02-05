#!/usr/bin/python3
''' A Module for Python Inheritance '''


def inherits_from(obj, a_class):
    ''' Returns True if obj is an instance of a subclass of a_class '''

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
