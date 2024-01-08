#!/usr/bin/python3

def no_c(my_string):
    if my_string[:]:
        first_str = my_string.translate({ord("C"): None})
        second_str = first_str.translate({ord("c"): None})
        return second_str
    return my_string
