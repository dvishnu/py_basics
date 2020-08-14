# Strings ,String functions and strings manipulations

# Display a string

print("Hyderabad")

# declare a string and print it

text = "Hello Hyderabad"
print("The above string is " + text )
print("The above string is {} ".format(text))

# Access the values in the strings
print(text[1:]) #prints the characters from the second index
print(text[1:5]) #prints the characters between 1 and 5 (1st character is excluded and last one is included)
print(text[-5:-2]) # prints the characters from position -5 (included) to -2 i.e -5.-4,-3 indexes
print(text[::-1]) # This reverses the string and it will start from the end of the string and increments by -1
print(text[::-2])# This reverses the string and it will start from the end of the string and increments by -2

#String functions and inbuilt methods

# length of the string
print(len(text))
#Strip is an inbuilt method and it should be used as string.strip() removes the extra white spaces
print(text.strip())
# lower and upper methods
print(text.lower())
print(text.upper())
# Replace method (replaces the string )
print(text.replace('H','V')) #(replcaes every occurence of H with V)
#split splits the string into substring based upon the field seperator which we provide ex: , " " :
print(text.split(" "))
#Checking the occurence of a strings using 'in' and 'not in' keywords
a = "Hello" in text
print(a)
b = "Hero" not in text
print(b)
#String concatenation
x ="Hello"
y ="How are you"
print(x + " " + y)
print("Hi my name is vishnu and " + y)
#string format takes arguments and places with respective placeholders
name = "pk"
city = "Hyderabad"
place = "Gachibowli"
print("Hi my name is {} and i stay in {} located in {}".format(name,place,city))
print("Hi my name is {0} and i stay in {1} located in {2}".format(name,place,city))# can use with index numbers
#Escape characters
print("Hello world this is \"Robo2.0\" ")
print("Hello world this is \'Robo2.0\' ")
print('It\'s always like that')
print(" Hi my name is {0} \n and i stay in {1} \n located in {2}".format(name,place,city))  # newline
print(" Hi my name is {0} \t and i stay in {1} \t located in {2}".format(name,place,city)) # tabspace

# Some other important string methods
# center
print(text.center(50)) # takes thespace of 50 char and prints text between the spaces
print(text.center(50,'1')) #replaces the spaces with 1
#count
print(text.count('Hello')) #returns the count of strings
print(text.find('l'))
