# File handling is used to create, read, write, update, and delete files in Python.

# 1. Create and write file
import os # importing the os module to use the remove() function to delete files.


filehandle = open("new_file.txt", "w")
# "w" mode creates the file if it does not exist.
# If the file already exists, it removes old data and writes new data.

filehandle.write("Hello World\n")
filehandle.write("I am learning Python file handling\n")

filehandle.close()


# 2. Read file
filehandle = open("new_file.txt", "r")
# "r" mode is used to read data from the file.

content = filehandle.read()
print(content)

filehandle.close()


# 3. Append/update file
filehandle = open("new_file.txt", "a")
# "a" mode is used to add new data at the end of the file.
# It does not delete old data.

filehandle.write("This line is added using append mode\n")

filehandle.close()


# 4. Read file again after append
filehandle = open("new_file.txt", "r")
print(filehandle.read())
filehandle.close()


# 5. Delete file
os.remove("new_file.txt")

