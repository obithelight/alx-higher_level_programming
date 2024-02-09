#!/usr/bin/python3
''' A Python Module '''


def append_after(filename="", search_string="", new_string=""):
    '''
    Inserts a line of text to a file,
    after each line containing a specific string.
    '''

    text = ''

    # Open the input file for reading
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string

    # Open a new file for writing
    with open(filename, 'w') as w:
        w.write(text)
