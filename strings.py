# Strings and string operation in python

# String in python is like and array of characters
# Strings in python are immutable (the original string value does not changes)

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

print("\n")


# String Mehtods

text = "This is a sample text !!!!"

print(text.upper())  # Converts the whole text to upper case
print(text.lower())  # Converts the whole text to lower case
print(text.replace("text", "sentence"))  # replaces the old string with new one
print(text.capitalize())  # returns the first letter upper case and remaining lower case
print(text.title())  # capitalizes the first letter of each word
print(text.istitle())  # checks is it a title or not & returns bool value

print(text.find("java"))  # finds the given string & returns -1 if not found
# if found it returns the index where it is found
print(text.find("is", 3, 12))  # finds the given string within that index (2:12)

print(text.count("t"))  # counts the string passed to it
print(text.count("s", 2, 10))  # counts the given strign within taht index (2:10)

print(text.endswith("!"))  # whether the text ends with given string returns boo"lean
print(text.endswith("is", 2, 12))  # checks the ending string within the index (2:12)

print(text.startswith("This"))  # returns true if the text starts with passed string
print(text.startswith("is", 4, 12))  # checks for the given indes range only

text = "apple, banana, guava, mango, cherry"

print(text.split(","))  # splits text by finding the passed string & returns list
print(text.split(" "))  # splitting by finding the whitespace & retunrs list


name = "Sarvesh"
usn = "1CS24DG052"
age = "24"

print(usn.isalnum())  # Returns True if all characters are letters or numbers
print(age.isdigit())  # # Returns True if all characters only digits
print(name.isalpha())  # Returns True if all characters in the string are letters.
