#!/usr/bin/python3
''' A Python Module '''


def read_file(filename=""):
    ''' Reads a text file (UTF8) and prints it to stdout '''
    with open(filename, encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end="")
