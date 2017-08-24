#!/usr/bin/python3

def add_integer(a, b):
	""" Returns sum of 2 integers """
	if type(a) != int and type(a) != float:
		raise TypeError("a must be an integer")
	if type(b) != int and type(b) != float:
		raise TypeError("b must be an integer")
	if type(a) == float or type(b) == float:
		return int(a) + int(b)
	else:
		return a + b
