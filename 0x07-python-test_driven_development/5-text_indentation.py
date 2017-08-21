#!/usr/bin/python3

def text_indentation(text):
    """ prints a text with 2 new lines after
    each of those characters: ., ? and :"""

    chars = ".,?"

    for i in text:
        for j in chars:
            if i == j:
                print()
        print(i, end="")
