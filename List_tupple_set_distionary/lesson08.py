# Set is used to store unique values only.
# It is mutable, which means we can add and remove values after creating it.
# Set is unordered and unindexed, so we cannot access values using index.

numbers = {1, 2, 2, 3, 4, 5, 6}

# 1. Print set
# Duplicate value 2 will be removed automatically.
print(numbers)


# 2. Add single value
numbers.add(7)
print(numbers)


# 3. Add multiple values
numbers.update([8, 9, 10])
print(numbers)


# 4. Find length of set
print(len(numbers))


# 5. Check value exists or not
if 5 in numbers:
    print("5 exists in the set")
else:
    print("5 does not exist in the set")


# 6. Remove value using remove()
numbers.remove(3)
print(numbers)


# 7. Remove value using discard()
numbers.discard(4)
print(numbers)


# 8. Loop through set
for number in numbers:
    print(number)