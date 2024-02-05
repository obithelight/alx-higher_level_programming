#!/usr/bin/python3
''' Represents a Geometry Module '''


class BaseGeometry:
    ''' Defines a Geometry Class '''

    def area(self):
        ''' Public Instance Method '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Validate a parameter as an integer '''

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
