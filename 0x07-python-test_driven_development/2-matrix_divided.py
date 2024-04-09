#!/usr/bin/python3
"""
This script defines a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
	"""
	Divide each element of a matrix by a divisor.
	
	Parameters:
		matrix (list of lists of int/float): the matrix to divide
		div (int/float): the number to divide by
	Raises:
		TypeError: If the matrix is not a list of lists of integers or floats,
		or if div is not a number.
		TypeError: If each row of the matrix does not have the same size.
		ZeroDivisionError: If div is equal to 0.
	Returns:
	a new matrix
	"""
	if not isinstance(matrix, list) or \
		any(not isinstance(row, list) for row in matrix):
		raise TypeError("matrix must be a matrix \
			(list of lists) of integers/floats")

	if not isinstance(div, (int, float)):
		raise TypeError("div must be a number")

	if div == 0:
		raise ZeroDivisionError("division by zero")

	row_sizes = set(len(row) for row in matrix)
	if len(row_sizes) > 1:
		raise TypeError("Each row of the matrix must have the same size")

	new_matrix = []
	for row in matrix:
		new_row = [round(element / div, 2) for element in row]
		new_matrix.append(new_row)

	return new_matrix
