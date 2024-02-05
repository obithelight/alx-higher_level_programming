#!/usr/bin/python3
''' A Python Module for Inheritance '''


class MyList(list):
    ''' This class inherits from another function '''

    def print_sorted(self):
        ''' Defines and prints the list '''

        sorted_list = sorted(self)
        print(sorted_list)
