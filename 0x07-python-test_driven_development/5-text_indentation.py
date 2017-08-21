#!/usr/bin/python3

def text_indentation(text):
    """ prints a text with 2 new lines after
    each of those characters: ., ? and :"""

    if type(text) != str:
        raise TypeError("text must be a string")


    text = text.replace(".", ".\n\n")
    text = text.replace(",", ",\n\n")
    text = text.replace("?", "?\n\n")

    print(text)

    # chars = ['.', ',', '?']



    # splited_str = text.split(".,?")
