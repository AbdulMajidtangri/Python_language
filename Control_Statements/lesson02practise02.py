# 1. Take marks and print grade.
marks3 = int(input("Enter your marks : "))
if marks3 >= 90 and marks3 >=100 : 
    print("You have got grade A1 in you class")
elif marks3 <90 and marks3 >=80:
     print("You have got grade A in you class")
elif marks3 <80 and marks3 >=70:
     print("You have got grade B+ in you class")
elif marks3 <70 and marks3 >=65:
     print("You have got grade B in you class")
elif marks3 <65 and marks3 >=60:
     print("You have got grade C+ in you class")
elif marks3 < 60 and marks3 >=50:
     print("You have got grade C in you class")
else :
    print("you are faileddddd!!")
# 2. Take age and check:
#    age < 13       → Child
#    age 13 to 19   → Teenager
#    age 20 to 59   → Adult
#    age >= 60      → Senior citizen

age = int(input("Enter you age : "))
if age < 13 and age >=0 : 
     print("you are child")
elif age >=13 and age <=19:
     print("teenager")
elif age >19 and age <=59:
     print("Adult")
elif age >=60:
     print("senior citizen")
else:
     print("invalid age")
# 3. Take username and password.
#    If both correct, print Login Successful.
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
# 4. Take day number 1 to 7 and print day name using match case.
day = int(input("Enter the day the no : "))
match day:
     case 1:
          print("monday")
     case 2:
          print("tuesday")
     case 3:
          print("Wednesday")
     case 4:
          print("Thursday")
     case 5:
          print("Friday")
     case 6:
          print("saturday")
     case 7:
          print("Sunday")
     case _:
          print("invalid input")
# 5. Take user role:

roles = input("Enter you role")
match roles:
     case "admin":
          print("admin dashboard")
     case "doctor":
          print("doctor dashboard")
     case "patient":
          print("patient dashboard")
     case _:
          print("invalid role")
#    admin  → Show admin dashboard
#    doctor → Show doctor dashboard
#    patient → Show patient dashboard
#    other → Invalid role