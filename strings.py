# Strings and string operation in python

# String in python is like and array of characters

name = "Sarvesh"
print("My name is :", name)

# as strings are like arrays we can access the characters using indexing

print(name[0])  # 0th index of varriable name
print(name[1])  # 1st index of varriable name
print(name[2])  # 2nd index of varriable name


print(len(name))  # len() function returns the len of the string

print(name[0:4])  # slices the characters form index 0th to 3rd (excludes the 4th one)
print(name[:4])  # same as the above line it adds automatically 0th index

print(name[len(name) - 3 : len(name) - 1])  # this is called negative slicicng
print(name[-3:-1])  # similar to the above line
