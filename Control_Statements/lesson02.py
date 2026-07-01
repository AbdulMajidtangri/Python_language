#control statement is used to control the execution of the program in the python while python execution the code line by line
#there are two type of the control statement 1.conditional statemenets and 2.loop statements
#in the conditiona statement we have if,else,and elif statement to print the block of as per the condition when we have two possible outcome we have if ,else statement and elif is used when we have more the two possible outcomes 
#used only if condition
marks  = 50
if marks >= 50 :
    print("you are pass")
#use if ,and else both conditions
marks2  = 50

if marks2 >= 50 : 
    print("You are Pass!")
else :
    print("you are faileddddd!!")
#elif will be used when we have more two possibilities 
marks3 = 45
if marks3 >= 90 : 
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
# the logical operator are usually more used in the if,elif statement to cheak more condition at a same time 

# lets use the switch statement in the program which ususaly used over the if,elif statements
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

     
     