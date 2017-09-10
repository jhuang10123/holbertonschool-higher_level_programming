#!/usr/bin/python3
""" adds all arguments to a Python list, and then save them to a file """
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

# try open file - if file exists. if exist, set list to content ofile
try:
    alist = load_from_json_file(filename)  # returns python object or error

# except-> if file doesnt exist, set empty list
except BaseException:
    alist = []

# list from content will be json formatted so convert to python to edit/append

# start at 2nd argument, append args to alist
for arg in sys.argv[1:]:
    alist.append(arg)

# save updated list back to json format
new_list = save_to_json_file(alist, filename)
