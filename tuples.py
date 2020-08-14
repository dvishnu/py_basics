# Basics of tuples in Python
# immutable and cannot be changed or edited
basic_tuple = ("english" , "hindi" , "telugu", "kannada")
print(basic_tuple)

print(basic_tuple[::])
print(basic_tuple[1:3])
print(basic_tuple[::-1])

# to change the tuple convert the tuple into a list append it and convert back to tuples

l1 = list(basic_tuple)
l1.append("Tamil")
print(l1)
l2 = tuple(l1)
print(l1)
# loops with tuples
for i in basic_tuple:
    print(i)

if "telugu" in basic_tuple:
    print("yes its present")
else:
    print("Not present")

t1 = ("school")
print(type(t1)) # This prints the type as String

t2 = ("school",)
print(type(t2)) # This prints the type as Tuple which includes comma after an element

thistuple = ("apple", "banana", "cherry")
print(thistuple)
