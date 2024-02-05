#!/usr/bin/python3
''' A Python Module for Inheritance '''


def is_same_class(obj, a_class):
    ''' This function returns True for Exact Same Objects '''
    if type(obj) == a_class:
        return True
    return False
