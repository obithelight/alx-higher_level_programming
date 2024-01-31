#!/usr/bin/python3
'''Module Representing a Locked Class'''


class LockedClass:
    '''
    Defines a locked class that prevents the user
    from dynamically creating new instance attributes
    except if the new instance is called "first_name."
    '''

    __slots__ = 'first_name'
