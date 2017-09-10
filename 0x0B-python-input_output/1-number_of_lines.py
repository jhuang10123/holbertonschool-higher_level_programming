#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r', encoding="UTF8") as file:
        count = 0
        for line in file:
            count += 1
    return count
