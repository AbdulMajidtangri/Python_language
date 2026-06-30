#Tuples are like list but they are immutable data type that means we cannot change the value of the tuple once it is created
tuple = [112,3,4,33,45,456,67,87]
tuple1 = (1,2,3,4,5,6)
tuple3 = 1,2,3,4
print(tuple)
print(tuple1)
print(tuple3)
tuple.sort() #sort() function is used to sort the tuple in ascending order
print(tuple)
print(tuple.pop())
print(tuple)
tuple.append(100) #append() function is used to add the element at the end of the tuple
print(tuple)
print(tuple.remove(33))
print(tuple)

#values within the tuple cannot be changed but we can change the values of the list within the tuple
t = ([1,2,3],[6,7,8])
list1 = t[0]
list1.append(4)
print(t)
print(list1)
list1[1] = 5
print(list1)
