#!/usr/bin/python3
def uppercase(str):
    for element in str:
        if ord(element) <= 122 and ord(element) >= 97:
            upper = (chr(ord(element) - 32))
        print(f"{upper}, end=''")
    print()
