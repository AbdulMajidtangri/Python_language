import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[0:3]) #[start :end] => 0:3  =>output : 1,2,3 and here the end index is exclusive means it will not include the element at index 3 the third is the wall where the slicing will stop and it will not include the element at index 3
print(arr[0:6:2]) #[start :end :step] => 0:6:2  =>output : 1,3,5 and here the end index is exclusive means it will not include the element at index 6 the sixth is the wall where the slicing will stop and it will not include the element at index 6 and step is used to skip the elements in the array
print(arr[::]) #[start :end :step] => ::  =>output : 1,2,3,4,5,6 and here the start index is 0 and end index is 6 and step is 1 means it will include all the elements in the array
print(arr[::-1]) #[start :end :step] => ::-1  =>output : 6,5,4,3,2,1 and here the start index is 0 and end index is 6 and step is -1 means it will include all the elements in the array in reverse order


#2d array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2[0:2,0:3]) #[start-row :end-row , start-column :end-column] => 0:2,0:2  =>output : [[1 2] [4 5]] and here the end index is exclusive means it will not include the element at index 2 the second is the wall where the slicing will stop and it will not include the element at index 2