#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    strlength = len(argv) - 1
    if strlength < 1:
        print("{} arguments.".format(strlength))
    elif strlength > 1:
        print("{} arguments:".format(strlength))
    else:
        print("{} argument:".format(strlength))

    for i in range(strlength):
        print("{}: {:s}".format(i + 1, argv[i + 1]))
