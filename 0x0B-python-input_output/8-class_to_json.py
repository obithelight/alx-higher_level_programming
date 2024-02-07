#!/usr/bin/python3
''' A Python Module '''


def class_to_json(obj):
    '''
    Returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean)
    '''
    # Check if the object has a method or attribute, convert to a dictionary
    if hasattr(obj, 'to_dict'):
        return obj.to_dict()

    # If the object doesn't have a specific method,
    # attempt a generic conversion.
    try:
        return obj.__dict__
    except AttributeError:
        # If no method or attribute is found,
        # raise an error or handle the case accordingly.
        raise ValueError("Object cannot be converted to JSON")
