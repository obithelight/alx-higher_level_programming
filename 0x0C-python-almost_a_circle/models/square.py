#!/usr/bin/python3
''' A Python Module Representing A Square'''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Defines a Square Class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' Initializes the square class '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Informal string representation of square class '''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                               self.x,
                                               self.y,
                                               self.width)
