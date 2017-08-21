#!/usr/bin/python3

def text_indentation(text):
    """ prints a text with 2 new lines after
    each of those characters: ., ? and :"""

    chars = ".,?"

    for i in range(len(text)-1):

        for j in chars:
            if text[i] == j:
                print(j)
                print()
                i+=1
        print(text[i], end="")
