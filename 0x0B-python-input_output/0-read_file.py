#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r', encoding="UTF8") as file:
        rd_file = file.read()
        for line in rd_file:
            print(line, end="")
