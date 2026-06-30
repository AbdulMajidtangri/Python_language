#set is like the list but allow us to store unique value only and it is mutalbe data tyep that mean the data can be changed once it is created 
set = {1,2,2,3,4,5,6}
# here i have added the dublicate value 2 but it will not be added in the set because set only allow unique value
print(set) #output will be {1,2,3,4,5,6}
set.add(7) #add() function is used to add the element in the set
print(set)
print(set[2]) #set is unindexed data type that means we cannot access the element of the set by index