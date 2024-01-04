#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for element in str:
        if ord(element) >= 97 and ord(element) <= 122:
            upper = chr(ord(element) - 32)
        else:
            upper = element
        print("{}".format(upper), end='')
    print()
