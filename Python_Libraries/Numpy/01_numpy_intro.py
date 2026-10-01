"""NumPy lesson 1: arrays and the basic NumPy vocabulary.

Run this file from the terminal with:
	python 01_numpy_intro.py

NumPy (Numerical Python) is designed for fast numerical work.  Its main
object is the ``ndarray``: a collection of values with a fixed shape and a
single data type.  The examples below are intentionally small so that a
student can predict the output before running the file.
"""

import numpy as np


# A Python list stores values as a general-purpose container.
numbers_list = [1, 2, 3]
print("Python list multiplied by 2:", numbers_list * 2)

# np.array converts the list into a numerical array.  Arithmetic is then
# applied element by element (this is called vectorized arithmetic).
numbers = np.array(numbers_list)
print("NumPy array multiplied by 2:", numbers * 2)
print("NumPy array plus 10:", numbers + 10)


# A 1D array is a single sequence of values.  Indexing starts at zero.
one_dimensional = np.array([10, 20, 30, 40])
print("\n1D array:", one_dimensional)
print("First value:", one_dimensional[0])
print("Last value:", one_dimensional[-1])

# A 2D array is a table: the outer list contains rows and each inner list
# contains the columns in that row.
two_dimensional = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D array:\n", two_dimensional)
print("Value at row 1, column 2:", two_dimensional[1, 2])


# These properties describe the array without changing its values.
print("\nType:", type(two_dimensional))  # numpy.ndarray means NumPy array.
print("Number of dimensions:", two_dimensional.ndim)  # 2: rows and columns.
print("Shape (rows, columns):", two_dimensional.shape)  # (2, 3)
print("Total number of values:", two_dimensional.size)  # 2 * 3 = 6.
print("Data type of each value:", two_dimensional.dtype)


# A loop can still visit values one at a time, although NumPy operations are
# usually clearer and faster when they can be written without explicit loops.
print("\nValues in the 2D array:")
for row in two_dimensional:
	for value in row:
		print(value)
