#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
	"""computes the square value of all integers of a matrix."""
	if not matrix:
		return None
	
	return [[x**2 for x in i] for i in matrix]

