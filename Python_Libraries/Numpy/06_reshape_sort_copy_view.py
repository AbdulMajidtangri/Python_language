"""NumPy lesson 6: reshape, sort, copy, and view."""

import numpy as np


values = np.array([5, 2, 8, 1, 4, 7])

# Reshape changes the structure, not the number of values.  6 values can
# become 2 x 3, but not 4 x 2 because 8 values would be required.
grid = values.reshape(2, 3)
print("Grid:\n", grid)
print("Sorted values:", np.sort(values))
print("Descending values:", np.sort(values)[::-1])

# copy owns independent data.  Changing it does not change the original.
copied = values.copy()
copied[0] = 999
print("\nOriginal after changing copy:", values)
print("Copy:", copied)

# view shares the original memory.  A change through the view is visible in
# the original array, which is useful but must be done deliberately.
viewed = values.view()
viewed[1] = 222
print("Original after changing view:", values)
print("View:", viewed)

# The base attribute helps reveal whether an array refers to another array's data.
print("Copy owns its data:", copied.base is None)
print("View shares data:", viewed.base is not None)
