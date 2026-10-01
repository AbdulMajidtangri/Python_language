"""Practice: Python loops and loop-control statements.

Read each example, predict its output, and then run this file.  After that,
change the values and conditions to test your understanding.
"""

# 1. A for loop repeats once for every value produced by range.
print("Counting from 1 to 5:")
for number in range(1, 6):
	print(number)

# 2. A while loop continues while its condition is True.  Updating the
# counter is essential; without it, the loop would never finish.
print("\nWhile-loop countdown:")
countdown = 3
while countdown > 0:
	print(countdown)
	countdown -= 1
print("Go!")

# 3. break stops the nearest loop immediately.
print("\nStop when the value reaches 4:")
for number in range(1, 8):
	if number == 4:
		break
	print(number)

# 4. continue skips only the current iteration and then starts the next one.
print("\nPrint only odd numbers:")
for number in range(1, 8):
	if number % 2 == 0:
		continue
	print(number)

# 5. Nested loops are useful for tables and grids.  The inner loop completes
# all of its repetitions for each one repetition of the outer loop.
print("\nA small multiplication table:")
for row in range(1, 4):
	for column in range(1, 4):
		print(row * column, end=" ")
	print()

# 6. pass is a placeholder: it does nothing.  It is useful temporarily when
# a block is required syntactically but the logic has not been written yet.
for number in range(1, 4):
	if number == 2:
		pass
	print("pass example:", number)
