#!/usr/bin/python3
""" 3-main """


import sys
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)



from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
