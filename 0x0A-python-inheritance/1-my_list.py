#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """ includes method to print sorted list """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints sorted list """
        print(sorted(self))
