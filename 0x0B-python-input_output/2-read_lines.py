#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding="UTF8") as file:
        if nb_lines <= 0:
            print("{:s}".format(file.read(), end=""))

        for i in range(nb_lines):
            print("{}".format(file.readline()))

"""
need to handle when out of range
"""
