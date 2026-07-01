# List in Python:
# A list is used to store multiple values in a single variable.
# It is mutable, which means we can change, add, and remove values after creating it.
# List is ordered and indexed.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1. Print complete list
print(numbers)
# 2. Find length of list
print(len(numbers))
# 3. Access list values using index
print(numbers[0])     # First element
print(numbers[-1])    # Last element
# 4. Add element at the end
numbers.append(10)
print(numbers)
# 5. Add element at specific index
numbers.insert(0, 112)
print(numbers)
# 6. Remove specific value
numbers.remove(3)
print(numbers)
# 7. Remove last element
numbers.pop()
print(numbers)
# 8. Sort list in ascending order
numbers.sort()
print(numbers)
# 9. Sort list in descending order
numbers.sort(reverse=True)
print(numbers)
# 10. Reverse list order
numbers.reverse()
print(numbers)
# 11. Loop through list
for number in numbers:
    print(number)
# 12. Sum of list values
print(sum(numbers))
# 13. Maximum value
print(max(numbers))
# 14. Minimum value
print(min(numbers))