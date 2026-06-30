# String is the data type that used to represent the text in the python,
#the string is imutable data type that means we cannot change the value of the string once it is created,
name = "majid" #the name is the variable that stores the string value
print(name)
#String operation
#f-string is a string function used to print the varaible in the text
print(f"your name is: {name}")
print(len(name)) #len() function is used to find the length of the string
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.replace("majid","Abdul Majid"))
print(name)
print(name[0])
print(name[::-1]) #print the string in reverse order
print(name[0:6:2]) #print the string from index 0 to 6 with step 2
print(name.split("j")) #split() function is used to split the string into list of strings