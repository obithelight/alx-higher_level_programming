#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    allnames = dir()
    for i in range(len(allnames)):
        if allnames[i][:2] != "__":
            print("{:s}".format(allnames[i]))
