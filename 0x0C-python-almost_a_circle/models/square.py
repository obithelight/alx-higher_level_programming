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

    @property
    def size(self):
        ''' Retrieves the size of the square '''
        return self.width

    @size.setter
    def size(self, value):
        ''' Sets the size of the square '''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        ''' assigns key word attributes to square class '''
        if args:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                    self.height = arg
                elif index == 2:
                    self.x == arg
                elif index == 3:
                    self.y = arg
                else:
                    continue

        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    continue
