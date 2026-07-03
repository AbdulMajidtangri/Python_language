#The Numpy is the python library which is used to erform the mathematicla calcualtion using the arrqay and its widely used in the data science and machine learning.
import numpy as np
#1. Create a numpy array using the list
first_arr = np.array([1,2,3,4,5])
print(first_arr)
#looping over the array
for i in range(len(first_arr)):
    print(first_arr[i])
#creating 2D Array
second_arr = np.array([[2,3],[5,6]])
print(second_arr)
#loopin over 2d array in the numpy
for i in range(len(second_arr)):
    for j in range(len(second_arr)):
        print(second_arr[i][j])
#methods of numpy 
#1. Checking the type
print(type(first_arr))
print(type(second_arr))
#2.checking the dimension of the array 
print(first_arr.ndim)
print(second_arr.ndim)
#3. the shape check the number of item within row nad columns for the 1d array it only shwo the no of elemement with in single row and for the 2d array it describe the number of element within the row nad column in the parenthesis (2,2) two elemeent in the rwo and two elemenet in the column
print(first_arr.shape)
print(second_arr.shape)
third_array = np.array([[1,2,3],[3,2,1],[9,8,7]])
print(third_array.shape)

#3 size define the total number of elemeent in array 
print(first_arr.size)

#4 dtype is used to chdck the data type of the array 
print(first_arr.dtype)
fourth_array = np.array([["apple","oragne"],["grapes","berries"]])
print(fourth_array.dtype)
fivth_array = np.array([["apple",23],["grapes","berries"]])
print(fivth_array.dtype)

#5 Array slicing

print(first_arr)
print(first_arr[0:2])
numberss = np.array([1,2,3,4,5,6,7,8,9,10])
print(first_arr[5:6])

#array types

#zeros : the zeros create the array which filled with zeros only so the array can be 1d,2d and other

oned_zeros_array = np.zeros(5) 
print(oned_zeros_array)
twod_zero_array = np.zeros((3,3))
print(twod_zero_array)

#ones : this creates new array filed with ones only and only

oned_ones_array = np.ones(5)
print(oned_ones_array)

#arrange work like the range aray but create new numpy array with ragne from start to end 
range_array = np.arange(1,6)
print(range_array)
#steps
range_array2 = np.arange(1,6,3)
print(range_array2)
#linspace() this create the new array with specific gap like for this array the gap that i hvae only those no of elemenet added in the array 

linespacee = np.linspace(1,10,2)
print(linespacee)


#perform arthmetic operations in the numpy array
arr1 = np.array([1,2,3,4])
print(arr1)
print(arr1+5)
print(arr1-1)
print(arr1*2)
print(arr1/2)

#perform the arthmetic operation between two array
arr2 = np.array([4,3,2,1])
print(arr1+arr2)  
#perfrom the arthmetic operation between two array with different shape it will give the error because the shape of the array is not same
arr3 = np.array([[1,2,3],[4,5,6]])
#print(arr1+arr3) #shwos error because the shape of the array is not same
#perfrom the statistical operation in the numpy array
print(np.sum(arr1)) 
print(np.max(arr1))
print(np.min(arr1))
print(np.mean(arr1))
print(np.median(arr1))
print(np.std(arr1))
print(np.mod(arr1,2)) #this will give the remainder of the array when divided by 2


#reshape is used to change the shape of the array but the total number of element should be same in the new shape and old shape
reshaped_array = arr1.reshape(2,2)
print(reshaped_array)


print(np.sort(arr1)) #this will sort the array in ascending order
# decending order
print(np.sort(arr1)[::-1])
#COPY AND VIEW
#copy is used to create the new array with the same data but the new array is independent when any changes made to copy array will not effect the original array vice versa
#view is used t o create the new array with the same data but the new array is dependent when any changes made to view array will effect the original array vice versa
copy_array = arr1.copy()
view_array = arr1.view()    
arr1[0] = 10
print(arr1)
copy_array[0] = 20
print(copy_array)
print(view_array) #this will show the change made in the original array because the view is dependent on the original array


#slicing 
#slicing is used to get the specific element from the array or to get the specific range of the array
#We can also define the step, like this: [start:end:step].
#::-> are the slicing operator which is used to get the specific range of the array

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  # Get elements from index 1 to 4
print(arr[::2])  # Get every second element
print(arr[1::2]) # Get every second element starting from index 1


#joining means putting the content of two or more arrays in a single array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
#joining two arrays
print(np.concatenate((arr1, arr2)))  # Output: [1 2 3 4 5 6]

print(np.stack((arr1, arr2), axis=0))  # Stack along the first axis
print(np.stack((arr1, arr2), axis=1))  # Stack along the second axis

twodarr = np.array([[1, 2], [3, 4]])
twodarr2 = np.array([[5,6], [7,8]])

print(twodarr)
print(np.stack((twodarr, twodarr2), axis=0))  # Stack along the first axis

