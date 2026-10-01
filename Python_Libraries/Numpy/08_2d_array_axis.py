"""NumPy lesson 8: rows, columns, and the meaning of axis."""

import numpy as np


sales = np.array([[10, 20, 30], [15, 25, 35]])
print("Sales:\n", sales)

# axis=0 moves down rows, so each column is reduced independently.
print("Column totals (axis=0):", np.sum(sales, axis=0))

# axis=1 moves across columns, so each row is reduced independently.
print("Row totals (axis=1):", np.sum(sales, axis=1))
print("Column averages:", np.mean(sales, axis=0))
print("Row maximums:", np.max(sales, axis=1))

# Keep dimensions when the result will be combined with the original array.
column_totals = np.sum(sales, axis=0, keepdims=True)
print("Totals with dimensions preserved:\n", column_totals)
print("Totals shape:", column_totals.shape)

# Broadcasting subtracts each column's average from that entire column.
column_averages = np.mean(sales, axis=0)
centered = sales - column_averages
print("Sales centered around each column average:\n", centered)
