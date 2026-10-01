# Numpy is the python library used for efficiently representing and maniulating mathematical data in the form of arrays. It is widely used in data science and machine learning for numerical computations. 
#numpy is the python library used to handle mathematical data in the form of arrays,
import numpy as np
arr = np.array([[1,22,3],[4,4.5,6]])
arr2 = np.array(
    [
       [
        [1,2,3],
        [4,5,6] 
        ] ,
         [
           [7,8,9],
           [10,11,12]
           ]
    ]
)

#1.ndim define the directions of the array
print(arr.ndim) 
print(arr2.ndim) 

#2.shape define the shape of the array in the form of tuple (rows,columns)
print(arr.shape)
print(arr2.shape) #2,2,3 => 2 blocks, 2 rows, 3 columns

#3.size define the size of the array (number of elements) the size is calculated by multiplying the shape of the array
print(arr.size) #2,3 => 2 rows, 3 columns
print(arr2.size) #2,2,3 => 2 blocks, 2 rows, 3 columns 

#4.dtype deifgne the type of the array int,float,complex,bool etc 32 or 64 => 32 or 64 bit
print(arr.dtype) #int32
print(arr2.dtype) #float64

#5.indexing  of the array
#indexing is used to access the elements of the array using the index of the array
#2D array
print(arr[0][1]) #22
print(arr[0][0]) #1
#3d array
print(arr2[0][1][2]) #6
print(arr2[0][0][0]) #1

#6.slicing of the array
#slicing is used to acces the elements of the array using the index of the array
#2D array
print(arr[0:2,0:3]) #[[ 1.  22.   3.] [ 4.   4.5  6. ]]
print(arr[0:2,0:2]) #[[ 1.  22.] [ 4.   4.5]]
#3D array       
# print(arr3[0:2,0:2,0:2]) #[[ 1.  2.] [ 4.   4.5]]


#Aggregate functions in numpy are used to perform mathematical operations on the array like sum,mean,median,std,min,max etc
print(f"Sum of the array: {np.sum(arr)}")
print(f"Mean of the array: {np.mean(arr)}")
print(f"Median of the array: {np.median(arr)}")
print(f"Standard deviation of the array: {np.std(arr)}")
print(f"Minimum value in the array: {np.min(arr)}")
print(f"Maximum value in the array: {np.max(arr)}")


#copy of the array in numpy is used to create a new array with the same data as the original array. The copy of the array is independent of the original array and any changes made to the copy will not affect the original array.
arr_copy = arr.copy()
print(f"Original array: {arr}")
print(f"Copy of the array: {arr_copy+9}")
print(f"Original array after changing the copy: {arr}")
#view of the array in numpy is used to create a new array with the same data as the original array. The view of the array is dependent on the original array and any changes made to the view will affect the original array.
#it just creat ethe view of the array and any changes made to the view will affect the original array.
arr_view = arr.view()
print(f"Original array: {arr}")
arr_view += 9
print(f"View of the array: {arr_view}")
print(f"Original array after changing the view: {arr}") # the original array is changed because the view of the array is dependent on the original array and any changes made to the view will affect the original array.