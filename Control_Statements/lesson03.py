# loops are used to print the code again and again....
print("printing the loop")
for i in range(1,6):
    print(i)

# Types of Loops in Python
# 1. for loop
#for loop is used when we know the no of iteration while repaeting the block of code
print("for loop")
#for loop is used iterator over the no of the ranges
for i in range(1,5):
    print("hello world!!!!!!!!")
#for is uised to iterate over the list of the elements
arr = ["local","premium","business"]
for i in arr:
    print(i)
# 2. while loop
print("while loop")
# while is used when we don't know the no of iteration while repaeting the block of code,we only have condition according to that condition our loop repeats the code
while len(arr) > 0:
    print(arr.pop())
# 3. nested loop
#nested loop means the loop within the loop 
for i in range(1,6):
    for j in range(1,5):
        print(i,j)

# 4. loop control statements
#    - break : breaks statement is used to stop loop  we use any condition if that condition got true the stop its execution 
for i in range(1,6):
    if i == 4:
        break
    print(i)
#    - continue : continue is used to skip current execution of the loop and move to another execution
for i in range(1,6):
    if i == 4:
        continue
    print(i)
#    - pass :pass statement is simple mean do nothing its used when i dont want to write the logic jsut leave empty space
for i in range(1,6):
    if i == 4:
        pass
    print(i)
  
#print the patterns

# *
# **
# ***
# ****
# *****
# ******
# *******
for i in range(1,8):
    print("*" * i)

for i in range(8,0,-1):
    print("*" * i)

