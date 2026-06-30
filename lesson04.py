#function are reusalbe blocks of code that can be called multiple times throughout a program.
#without function we need to write the same code again anad agin for the different value so there function make it easier as make a single function and call whenever we need it.
#so function are created using def keyword and function name with parenthesis and colon at the end on the line 
def my_function():
    print("hello world")
my_function() #function call

# there are the type of functions parameter and without parameter function
def function_with_parameter(name):
    print(f"helllllllllllo {name}")
function_with_parameter("musawer") #function call with parameter

#return staement in function is used to return the value from the function to where it called and we can use that value in our program
def sum(a,b):
    return a+b
result = sum(5,10) #function call with parameter and return value
print(result)
