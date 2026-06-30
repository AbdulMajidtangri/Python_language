#List is used to more than one value in a single variable and it is mutable data type that means we can change the value of the list once it is created,
list1 = [1,2,3,4,5,6,7,8,9]
print(list1)
print(len(list1)) #len() function is used to find the length of the list
print(list1[0]) #print the first element of the list
print(list1[-1]) #print the last element of the list
list1.append(10) #append() function is used to add the element at the end of the list
print(list1)
list1.insert(0, 112) #insert() function is used to add the element at the specified index
print(list1)
list1.remove(3) #remove() function is used to remove the element from the list
print(list1)
list1.pop() # pop() function is used to the remvoe the elememet from the end of the list
print(list1)
list1.sort() #sort() function is used to sort the list in ascending order
print(list1)
list1.sort(reverse=True) #sort() function is used to sort the list in descending order
print(list1)
list1.reverse() #reverse() function is used to reverse the list
print(list1)


for i in list1: #for loop is used to iterate the list
    print(i)