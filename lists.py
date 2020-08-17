# basics of arrays and lists in python

fruits = ["apple","mango","banana","orange"]
print(fruits[0]) #accessing the list
print(fruits[1:])
print(fruits[::-1]) # reverse view of the list
print(fruits[-1]) #negative index
print(fruits[1:3]) #includes index 1 and excludes index 3 and prints values from index 1,2
print(fruits[:2]) # prints indexes till 2 (0,1)
print(fruits[2:])# prints indexes from 2 to ending of the list
print(fruits[-3:-2]) # count starts from reverse order

# change the values in the list
fruits[2] = "pineapple"
print(fruits)

# loops through the lists
for i in fruits:
    print(i)
# check if the given item exists in the list

if "orange" in fruits:
    print("yes")
else:
    print("The above fruit is not present")

# length of the lists

print(len(fruits)) # gives the number/length of items in the list

# add items to the lists (append function will add /update the items to the lists)
fruits.append("watermelon")
print(fruits)
# Inserting an element using insert methods at the specific indexes
fruits.insert(5,"kiwi")
print(fruits)
# Removing the items from the lists
fruits.remove("kiwi")
print(fruits) # kiwi will be removed from the lists

#removing using pop method
fruits.pop() # removes the last item if index is not mentioned
print(fruits)
fruits.pop(1) # removes the item from the index:1
print(fruits)

# To remove the list completely
cars = ["maruti","hyundai","tata"]
print(cars)
#del cars # this deletes the entire lists

# copy a list from an other lists
new_fruits = fruits[::] # copy method seems to be not working in python2 and 3 versions
print(new_fruits)

# we can copy using the list methods
extra_fruits = list(fruits)
print(extra_fruits)

# add the lists
join = fruits + cars
print(join)

# Add the lists using the loops
for x in fruits:
    cars.append(x)
    print(cars)

# extend method to add the elements at the ending
l1 = ["A" , "B", "C"]
l2 = ["x" , "y", "z"]
l1.extend(l2)
print(l1)

# in built methods
fruits.reverse()
print(fruits)

#fruits.clear() # present in python3 version
fruits.sort()
print("sorted list {}".format(fruits))


i = 1
while i <= 10:
    j = 5 * i
    print("5 * {} = {}".format(i,j))
    i += 1
