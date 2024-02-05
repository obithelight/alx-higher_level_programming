#!/usr/bin/python3
''' A Module for Python Inheritance '''


def is_kind_of_class(obj, a_class):
    ''' Defines a function is-kind-of-class '''

    if isinstance(obj, a_class):
        return True
    return False
