#dictionary is like list but it store the data in key value pair and it is mutable data type that means we can change the value of the dictionary once it is created
user = {
    "name":"Abdul Majid",
    "age":22,
    "lastname": "Tangri",
    "phone":123456789
}
print(user) #print the dictionary
print(user["name"]) #print the value of the key "name"
print(user["age"]) #print the value of the key "age"
print(user["lastname"]) #print the value of the key "lastname"
print(user["phone"]) #print the value of the key "phone"

user["name"] = "kareem" #change the value of the key "name"
print(user) #print the dictionary after changing the value of the key "name"
user['address'] = "Pakistan" #add the new key value pair in the dictionary
print(user) #print the dictionary after adding the new key value pair
print(len(user)) #len() function is used to find the length of the dictionary
print(user['address'])
print(user.keys())
user.pop('address') #pop() function is used to remove the key value pair from the dictionary
print(user) #print the dictionary after removing the key value pair
for i,h in user.items():
    print(i,h) #print the key value pair of the dictionary
 
 