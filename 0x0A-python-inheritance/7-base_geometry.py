#!/usr/bin/python3
''' Represents a Geometry Module '''


class BaseGeometry:
    ''' Defines a Geometry Class '''

    def area(self):
        ''' Public Instance Method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Public Instance Method '''
        self.name = name

        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
