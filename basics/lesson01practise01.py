# 1. Take two numbers and print addition, subtraction, multiplication, and division.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
    print(f"Floor Division: {num1 // num2}")
else:
    print("Division by zero is not allowed")


# 2. Take one number and check if it is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("This is even number")
else:
    print("This is odd number")
# 3. Take marks and check if student is pass or fail.

marks = int(input("Enter your marks: "))

if marks >= 50:
    print("You are pass")
else:
    print("You are fail")


# 4. Take age and check if person is eligible for CNIC. Age should be 18 or above.

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible for CNIC")
else:
    print("You are not eligible for CNIC")


# 5. Take username and password. If both are correct, print Login Successful.

correct_username = "majuu123"
correct_password = "majid123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
elif username != correct_username and password == correct_password:
    print("Username is incorrect and password is correct")
elif username == correct_username and password != correct_password:
    print("Username is correct and password is incorrect")
else:
    print("Username and password both are incorrect")


# 6. Take a list of cities and check if "Hyderabad" exists in the list.

cities = ["karachi", "hyderabad", "lahore", "islamabad"]

city = input("Which city do you want to search: ").lower()

if city in cities:
    print("City exists in the list")
else:
    print("City does not exist in the list")


# 7. Take three numbers and find which one is greater.

numm1 = int(input("Enter first number: "))
numm2 = int(input("Enter second number: "))
numm3 = int(input("Enter third number: "))

if numm1 >= numm2 and numm1 >= numm3:
    print(f"{numm1} is greatest")
elif numm2 >= numm1 and numm2 >= numm3:
    print(f"{numm2} is greatest")
else:
    print(f"{numm3} is greatest")


# 8. Calculate this expression: 10 + 5 * 2 ** 2

print(10 + 5 * 2 ** 2)


# 9. Use assignment operator.

x = 10
x += 5
x *= 2
x -= 4

print(x)


# 10. Check if a student is eligible for scholarship.

marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance: "))

if marks > 80 and attendance > 75:
    eligible = True
else:
    eligible = False

print(f"The student is eligible: {eligible}")