#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) < 97:
            print("{:s}".format(chr(ord(i) + 32)))
        else:
            print("{:s}".format(i))
