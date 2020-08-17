# Dictionaries in Python

# unorderdered and indexed and have keyvalue pairs

d1 = {
"name": "robo",
"city": "Hyderabad",
"State": "Telengana"
}

print(d1)
# access the items from the Dictionaries

print(d1["name"]) # access the value from the key
print(d1["city"])

d1["name"] = "Alibaba" # changing the value in the dict
print(d1["name"])

# loops

for i in d1:
    print(i)

for i in d1:
    print(d1[i]) # print all the values for the keys one by one

for i in d1.values():
    print("key values are " + i) #printing the items using the values method

for i,j in d1.items(): # using items method to display both key and values
    print(i,j)

for i in d1.values():
    if "Hyderabad" in i:
        print("yes")
    else:
        print("no")
#or
if "name" in d1:
    print("name exists")
else:
    print("name do not exists")
# length of the Dictionaries

print(len(d1))
# Add items to Dictionaries

d1["pincode"] = "500047"
print(d1)

# Remove the items
print(d1.pop("pincode"))
print(d1)
# or
#d1.pop("pincode")
# Using the delete keyword
del d1["name"]
print(d1)

# copy one dict to other Dictionaries

d2 = d1.copy()
print(d2)
# other way to copy using dict method
d3 = dict(d2)
print(d3)

# Nested dicts:
college = {
"student1": {
"name": "VD",
"city": "Chennai"
},
"student2":{
"name": "pk",
"city": "chennai"
}
}
print(college)

# Creating the dict which contains the nested Dictionaries
