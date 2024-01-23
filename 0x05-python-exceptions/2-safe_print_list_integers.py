#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    try:
        box = []
        count = 0
        for item in my_list:
            if isinstance(item, int):
                box.append(item)
                count += 1
                if count == x:
                    break
        print(" ".join("{:d}".format(i) for i in box), end="\n")
        return count
    except IndexError:
        print("list index out of range")
