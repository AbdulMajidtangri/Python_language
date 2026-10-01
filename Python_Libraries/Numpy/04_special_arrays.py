"""NumPy lesson 4: creating useful arrays without listing every value."""

import numpy as np


# zeros and ones are useful for initialization, placeholders, and masks.
print("Zeros:\n", np.zeros((2, 3)))
print("Ones:\n", np.ones((2, 3), dtype=int))

# full fills every position with one chosen value.
print("Filled with 7:\n", np.full((2, 3), 7))

# arange behaves like range: start is included, stop is excluded.
print("Values 0 to 8:", np.arange(0, 10, 2))

# linspace creates a requested number of evenly spaced values.  Unlike
# arange, its third argument is a count, not a step size.
print("Five evenly spaced values:", np.linspace(0, 1, 5))

# eye creates an identity matrix: ones on the main diagonal and zeros elsewhere.
print("Identity matrix:\n", np.eye(3, dtype=int))

# Random values are useful for experiments.  A seed makes this lesson
# repeatable, so every student sees the same output on each run.
rng = np.random.default_rng(42)
print("Random integers:\n", rng.integers(1, 10, size=(2, 3)))
