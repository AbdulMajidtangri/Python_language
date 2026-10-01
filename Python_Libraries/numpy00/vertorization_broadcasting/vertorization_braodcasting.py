import numpy as np;
arr = np.array([[1,2,3],[4,5,6]])
#vectorization in numpy is the process of performing operations on entire arrays rather than individual elements. This allows for more efficient and faster computations.
print(f"Add 2 to each element of the array: {arr + 2}") #add 2 to each element of the array
print(f"Multiply each element of the array by 2: {arr * 2}") #multiply each element of the array by 2
print(f"Subtract 2 from each element of the array: {arr - 2}") #subtract 2 from each element of the array
print(f"Divide each element of the array by 2: {arr / 2}") #divide each element of the array by 2

#braodcasting in numpy is the process of performing operations on arrays of different shapes and sizes. This allows for more efficient and faster computations.
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([1,2,3])
print(f"Add arr2 to arr: {arr2 + arr3}") #add arr2 to arr
