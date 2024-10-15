#!/usr/bin/python3
"""Adds all command line arguments to a Python list,
and then save them to a file
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"
args = argv[1:]
json_string = []

try:
    json_string = list(load_from_json_file(filename))
except FileNotFoundError:
    save_to_json_file(args, filename)

json_string += args
save_to_json_file(json_string, filename)
