#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        elements = my_list[:x]
        print(*elements, sep="", end="")
        print()
        count = 0
        for i in elements:
            count = count + 1
        return count
    except:
        print(elements, sep="", end="")
        print()
