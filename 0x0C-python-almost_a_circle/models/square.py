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
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
