#!/usr/bin/python3
""" 6-main """

import sys
import os



# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to the Python path
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

sys.path.append(parent_dir)

from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()
