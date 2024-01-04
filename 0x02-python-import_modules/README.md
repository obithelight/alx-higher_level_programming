# 0x02. Python - import & modules

## Learning Objectives

### Why Python programming is awesome:
- Python is known for its simplicity and readability. It has a large standard library and an active community. Python supports multiple programming paradigms, making it versatile for various applications.

### How to import functions from another file:
- You can import functions from another file using the import statement. Suppose you have a file named my_module.py with a function called my_function. You can import it in another script using:
python
Copy code
from my_module import my_function

### How to use imported functions:
- Once imported, you can use the functions from the module as if they were defined in your current script:
python
Copy code
result = my_function()

### How to create a module:
- To create a module, you write a Python script with functions or variables and save it as a .py file. For example, create a file named my_module.py with your functions or variables.

### How to use the built-in function dir():
- The dir() function is used to get a list of names in the current local scope or to get attributes of an object. For example:
python
Copy code
print(dir())  # List names in the current scope

### How to prevent code in your script from being executed when imported:
- Use the if __name__ == "__main__": construct. Code within this block will only be executed if the script is run directly, not when imported as a module. For example:
python
Copy code
if __name__ == "__main__":
    # Your main code here

### How to use command line arguments with your Python programs:
- You can use the sys.argv list from the sys module to access command-line arguments. Alternatively, you can use the argparse module for more advanced argument parsing. Here's a simple example with sys.argv:
python
Copy code
import sys

if len(sys.argv) > 1:
    print("Argument passed:", sys.argv[1])
