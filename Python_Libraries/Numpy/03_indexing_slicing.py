"""NumPy lesson 3: indexing and slicing without losing your place."""

import numpy as np


temperatures = np.array([18, 21, 24, 27, 30, 33])
print("temperatures:", temperatures)

# Indexes start at zero.  Negative indexes count from the end.
print("First:", temperatures[0])
print("Third:", temperatures[2])
print("Last:", temperatures[-1])

# Slicing uses [start:stop:step].  The stop position is excluded.
print("Indexes 1 through 3:", temperatures[1:4])
print("Every second value:", temperatures[::2])
print("Reversed:", temperatures[::-1])

table = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\nTable:\n", table)
print("Row 1:", table[1])
print("Row 1, column 2:", table[1, 2])
print("First column:", table[:, 0])
print("Last two columns:\n", table[:, 1:])

# Boolean indexing keeps only values where the condition is True.
print("Values greater than 50:", table[table > 50])
