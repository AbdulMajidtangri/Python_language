# Tuple in Python:
# A tuple is an immutable data type used to store multiple values.
# Immutable means we cannot change, add, or remove values after creating it.
# Tuple values are ordered and indexed.
tuple1 = (1, 2, 3, 4, 5)
tuple2 = 1, 2, 3, 4, 5

print(tuple1)
print(tuple2)

#single value tuple
x = (5,)
print(type(x))

numbers = (112, 3, 4, 33, 45, 456, 67, 87)

# Print tuple
print(numbers)

# Access values
print(numbers[0])
print(numbers[2])

# Slicing
print(numbers[1:5])

# Length
print(len(numbers))

# Count method
values = (1, 2, 2, 3, 4, 2)
print(values.count(2))

# Index method
print(values.index(3))

# Loop through tuple
for number in numbers:
    print(number)

# Tuple can contain mutable list
student_data = ([80, 90, 70], "Majid")

student_data[0].append(85)
print(student_data)


