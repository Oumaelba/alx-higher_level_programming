#!/usr/bin/python3
"""
This script defines a function add_integer that adds two integers.
"""

def add_integer(a, b=98):
	"""
	The function adds two parameters:
	
	Parameters:
	a: an integer or float
	b: an integer or float

	Returns:
	int: The function returns the sum of the two parameters as an integer.
	"""
	if isinstance(a, (int,float)):
		a = int(a)
	else:
		raise TypeError("a must be an integer")
	if isinstance(b, (int, float)):
		b = int(b)
	else:
		raise TypeError("b must be an integer")
	
	return a + b
