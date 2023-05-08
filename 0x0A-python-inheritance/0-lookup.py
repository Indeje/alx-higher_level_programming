#!/usr/bin/python3

"""
	Module that contains 'lookup' function
"""

def lookup(obj):

	"""
		Function that finds available attributes and methods of an object
		Args:
			obj: Object
		Returns:
			list of object attributes and methods
	"""

	return dir(obj)
