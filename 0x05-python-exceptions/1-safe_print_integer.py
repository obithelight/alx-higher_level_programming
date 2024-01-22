#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{}".format(value), end="\n")
            return True
    except ValueError:
        print("{}".format(value), end="\n")
        return False
