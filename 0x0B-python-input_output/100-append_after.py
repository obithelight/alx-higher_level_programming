#!/usr/bin/python3
''' A Python Module '''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text to a file,
    after each line containing a specific string.
    '''

    # Open the input file for reading
    with open(filename, 'r') as f:
        lines = f.readlines()  # Read all lines into a list

    # Open a new file for writing
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
