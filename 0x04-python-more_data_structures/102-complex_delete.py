#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_keys = list(a_dictionary.keys())

    for key in my_keys:
        if value == a_dictionary[key]:
            del a_dictionary[key]

    return (a_dictionary)
