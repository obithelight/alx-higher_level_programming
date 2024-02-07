#!/usr/bin/python3
'''
    A script that adds all arguments to a Python list
    and saves them to a JSON file
'''
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

    f = 'add_item.json'

    # Check if the file exists, if not create an empty list
    try:
        items = load_from_json_file(f)
    except FileNotFoundError:
        items = []

    # Add the new arguments to the list
    items.extend(sys.argv[1:])

    # Save the updated list to the file
    save_to_json_file(items, f)
