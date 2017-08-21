#!/usr/bin/python3

def text_indentation(text):
    """ prints a text with 2 new lines after
    each of those characters: ., ? and :"""

    if type(text) != str:
        raise TypeError("text must be a string")
    count = 0
    chars=[',', '.', '?']
    for i in text:
        if i in chars:
            count+=1

    for i in text:

    # chars = ",.?"

    # for i in range(len(text)-1):
    #     for j in chars:
    #         if text[i] == chars:
    #             print (chars)
    #             text = text.split(chars)
    # print (text.split(",.?"))



    # text = text.replace(".", ".\n\n")
    # text = text.replace(",", ",\n\n")
    # text = text.replace("?", "?\n\n")


    # print("\n\n".join(text.split(".,?"), end=""))
