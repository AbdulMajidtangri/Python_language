"""NumPy lesson 2: understanding an array's properties."""

import numpy as np


# The values below form 2 rows and 3 columns, so the shape is (2, 3).
scores = np.array([[78, 85, 92], [88, 76, 95]])
print("scores:\n", scores)
print("Python type:", type(scores))
print("ndim:", scores.ndim, "(number of axes)")
print("shape:", scores.shape, "(rows, columns)")
print("size:", scores.size, "(total values)")
print("dtype:", scores.dtype, "(type used by every value)")

# dtype can be selected when precision or memory usage matters.
decimal_scores = np.array([1.5, 2.5, 3.5], dtype=np.float32)
print("\nDecimal values:", decimal_scores)
print("Decimal dtype:", decimal_scores.dtype)

# A regular array normally contains one compatible dtype.  Mixing numbers and
# text causes NumPy to choose a common type, often converting numbers to text.
mixed = np.array([10, "twenty", 30])
print("Mixed values:", mixed)
print("Mixed dtype:", mixed.dtype)
