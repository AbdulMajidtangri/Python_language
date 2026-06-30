# print('hello i am learning python')
# # the python is a programming language that lets you work quickly and integrate systems more effectively. It is easy to learn and has a simple syntax.  
# #these comment in the program help us to understand the code better and also help us to remember what the code is doing when we come back to it after a long time.
# # the varaible is the named contanier that is used to store data in the memory. The variable can be of different types like integer, float, string, list, tuple, dictionary etc. The variable can be assigned a value using the assignment operator (=). The variable can be used to perform various operations like arithmetic operations, logical operations, comparison operations etc. The variable can also be used to store the result of an operation.
# name = "majid"
# #datatype is the type of data that is stored in the varaible, the datatype can be of different types like the integer,,float,string,tuples,and dictionary.
# age = 30 #this vage varaible can store the integer value
# room_temprature = 20.5 #this room_temperature varaible can store the float value
# print(name)
# print(age)
# print(room_temprature)
# #type() function is used to cheak the datatype of the varaible,it return the datatype of the varaible.
# print(type(name))
# print(type(age))
# print(type(room_temprature))

# #input()  function is used to take input from the user, it takes the value fro m the user and store it in the varaible adn input()  default return the value in the string format, if we want to take the input in the integer format we have to use the int() function to convert the string value into the integer value.
# # user_name = input("enter your name: ")
# # user_age = int(input("enter your age: "))
# # print("your name is: ", user_name)
# # print("your age is: ", user_age)

# # #f-string is a string function used to print the varaible in the text
# # print(f"your name is: {user_name} and your age is: {user_age}")

# # text = 0
# # print(string(text[0])) #this will print the first character of the string its throughing an error just because string cannot be convert to the integer 

# # Arithmetic operators
# # Assignment operators
# # Comparison operators
# # Logical operators
# # Membership operators
# # Identity operators
# # Operator precedence

# # these operators contain the operator which used to perfrom the operation in the program 
# #arthmetic operators (+,-,/,*,%,**) its perfrom three operation like addition,subtraction,multiplication,division,modulas,and power
# a = 2
# b = 2
# print(a+b)
# tex = "hello"
# tex2 = "world"
# print(tex+" "+tex2)

# #assignmenet operators used to store values in varaibles
# increase = 18
# decrease = 9
# print(increase)
# print(decrease)
# increase //=decrease 
# print(increase)
# #Comparison operators used to compare values and retrun true or false 
# #operators ==,>=,<=,>,<,!=
# var = 50
# var2 =51
# print(f"variable 1 is : {var} and the varailbe 2 is : {var2}")
# if var > var2 : 
#     print(f'the varaible one value is greatere then values : {var}')
# elif var2 > var :
#     print(f'the varaible two var2 value is greatere then values : {var2}')
# else: 
#     print('these both values are same')

# a = 10
# b = 0

# print(a == b)
# print(a != b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# #logical operators used to combined conditions at the single time 
# #and,or,not
# if a and b :
#     print("both truthy value")
# else:
#     print('one of them is falsy')

# #membership operator used to cheak if the value is present in the sequence or not
# #in,not in
# sequence = [1, 2, 3, 4, 5]
# print("membership operator: in,not in")
# print(3 in sequence)
# print(3 not in sequence)

# #identity operator used to cheak if the two refers to same object or not, it return true if both refers to the same object otherwise it return false
# #is,is not
# x= 5
# y=5
# arr = [1,2,3,4]
# arr2 = [1,2,3,4]
# print("identity operator: is,is not")
# # print(x is y)
# print(arr is arr2)
# print(arr is not arr2)