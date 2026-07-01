# Dictionary is used to store data in key-value pairs.
# It is mutable, which means we can change, add, and remove values after creating it.

user = {
    "name": "Abdul Majid",
    "age": 22,
    "lastname": "Tangri",
    "phone": 123456789
}

# 1. Print complete dictionary
print(user)


# 2. Access values using keys
print(user["name"])
print(user["age"])
print(user["lastname"])
print(user["phone"])


# 3. Change/update value
user["name"] = "Kareem"
print(user)


# 4. Add new key-value pair
user["address"] = "Pakistan"
print(user)


# 5. Find length of dictionary
print(len(user))


# 6. Access newly added value
print(user["address"])


# 7. Get all keys
print(user.keys())


# 8. Get all values
print(user.values())


# 9. Get all key-value pairs
print(user.items())


# 10. Remove key-value pair using pop()
user.pop("address")
print(user)


# 11. Loop through dictionary keys and values
for key, value in user.items():
    print(key, value)