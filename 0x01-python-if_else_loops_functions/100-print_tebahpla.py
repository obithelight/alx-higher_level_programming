#!/usr/bin/python3
for element in range(ord('z'), ord('a') - 1, -2):
    print("{}{}".format(chr(element), chr(element - 33)), end="")
