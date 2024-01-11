#!/usr/bin/python3

def uniq_add(my_list=[]):
    add_unique = set(my_list)
    sum = 0
    for i in add_unique:
        sum = sum + i
    return sum
