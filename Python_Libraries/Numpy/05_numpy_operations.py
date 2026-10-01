"""NumPy lesson 5: arithmetic and summary operations."""

import numpy as np


prices = np.array([100, 150, 80, 120])
quantities = np.array([2, 1, 3, 2])

# NumPy applies arithmetic element by element when shapes are compatible.
print("Prices:", prices)
print("Prices after 10% discount:", prices * 0.90)
print("Total for each item:", prices * quantities)
print("Total bill:", np.sum(prices * quantities))

# Comparisons also work element by element and produce a Boolean array.
print("Prices above 100:", prices > 100)
print("Expensive prices:", prices[prices > 100])

# Reduction functions summarize many values into one value.
print("Minimum:", np.min(prices))
print("Maximum:", np.max(prices))
print("Mean:", np.mean(prices))
print("Median:", np.median(prices))
print("Standard deviation:", np.std(prices))
print("Remainders after division by 3:", np.mod(prices, 3))

# Broadcasting lets a scalar interact with every array value.  Compatible
# shapes can also broadcast, but incompatible shapes raise a ValueError.
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("\nMatrix plus 10:\n", matrix + 10)
