# 1. Create a function that prints your name.
def your_name(name):
    print(f"Wellcome {name}")
your_name("majid") 
# 2. Create a function that takes name and prints welcome message.
yourname = input("Enter your Name : ")
def welcome_message(name):
    print(f"hello {name} how ar eyou feeling")
welcome_message(yourname)
# 3. Create a function that takes two numbers and prints their sum.
num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
def sum_of_two_numbers(num1,num2):
    return num1+num2
result = sum_of_two_numbers(num1,num2)
print(f"THe sum of Two numbers is :{result}")
# 4. Create a function that takes marks and returns pass/fail.

def pass_or_fail(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

marks = int(input("Enter your marks: "))
result = pass_or_fail(marks)
print(result)

# 5. Create a function that takes age and returns child/teenager/adult/senior citizen.
def age_group(age):
    if age < 13:
        print("You are a child.")
    elif age < 20:
        print("You are a teenager.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

age = int(input("Enter your age: "))
age_group(age)
# 6. Create a function that takes a number and prints its table.
def print_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

number = int(input("Enter a number to print its table: "))
print_table(number)


# 7. Create a function that takes list of marks and returns average.
def average_marks(marks_list):
    total = sum(marks_list)
    average = total / len(marks_list)
    return average

marks_list = []
for i in range(5):
    mark = int(input(f"Enter mark {i + 1}: "))
    marks_list.append(mark)
avg = average_marks(marks_list)
print(f"The average marks are: {avg}")


# 8. Create a function that takes username and password and checks login.
def check_login(username, password):
    # For demonstration purposes, let's assume the correct username and password are "admin" and "password123"
    correct_username = "admin"
    correct_password = "password123"
    
    if username == correct_username and password == correct_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

result = check_login(username, password)
print(result)

# 9. Create a function that checks even or odd.
def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

number = int(input("Enter a number to check if it's even or odd: "))
result = check_even_odd(number)
print(result)

# 10. Create a function that takes marks and attendance and returns scholarship eligibility.
def check_scholarship_eligibility(marks, attendance):
    if marks >= 85 and attendance >= 75:
        return "You are eligible for scholarship."
    else:
        return "You are not eligible for scholarship."

marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))
result = check_scholarship_eligibility(marks, attendance)
print(result)