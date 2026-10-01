"""NumPy lesson 7: joining arrays and stacking along an axis."""

import numpy as np


morning = np.array([1, 2, 3])
evening = np.array([4, 5, 6])

# concatenate extends an existing axis.  For 1D arrays it makes one longer row.
print("Concatenated:", np.concatenate((morning, evening)))

# stack creates a new axis.  axis=0 makes rows; axis=1 makes columns.
print("Stacked as rows:\n", np.stack((morning, evening), axis=0))
print("Stacked as columns:\n", np.stack((morning, evening), axis=1))

first = np.array([[1, 2], [3, 4]])
second = np.array([[5, 6], [7, 8]])
print("\nVertical join:\n", np.vstack((first, second)))
print("Horizontal join:\n", np.hstack((first, second)))

# Arrays joined along an axis must have compatible dimensions on the other axes.
print("Depth stack shape:", np.stack((first, second), axis=2).shape)
