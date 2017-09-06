#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
alist = []
if len(sys.argv) > 1:
    alist = [item for item in sys.argv]
new_list = load_from_json_file(alist)
save_to_json_file(new_list, filename)
