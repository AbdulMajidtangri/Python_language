#Error handling is a mechanism to handle the error that may occur during the execution of a program.
#it allows the program to continue its execution even if an error occurs.
# using try and except block  we can handle the error in python.
import os
try:
    num1 = int(input("enter First number: "))
    num2 = int(input("Enter Second Number : "))
    result = num1/num2
    print(f"Results are {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
finally:
    print("Execution completed.")


# filehandling = open("new_file.txt","w")
# filehandling.write("Hello World\n")
# filehandling.close()
try:
   os.remove("new_file.txt")
except FileNotFoundError:
    print("Error: File not found.")

  
age = input("Enter your age: ")
try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Your age is {age}")
except ValueError as e:
    print(f"Error: {e}")