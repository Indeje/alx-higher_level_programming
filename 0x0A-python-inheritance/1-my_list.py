#!/usr/bin/python3

"""
Module that contains class 'MyList'
"""


class MyList(list):

	"""
	Class that inherits properties of inbuilt 'list' class
	"""

	def print_sorted(self):
		print(list.sort(reverse=True))
