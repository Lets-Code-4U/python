# The basic hello world statement in python
print("Hello world")

# comments in python (any line starting with "#" is a comment in python)

print("this line could be the comment")  # To make this comment add # at the begining

# Multiline comment

""" This is a multi line comment 
 used in python in order to 
 define something """

# Characters Escapes in python
""" \n is for new line
    \" is to apply double quotes in any string
    \' is for single quotes """

print("Hii! \nSarvesh Mishra \nHow are you?")
print('I am fine "Mr. Aanand" ')


# Varriables and data types in python
""" The basic data types are :
    Numerical : int,float,complex
    String (characters and sentences)
    Boolean: True,False
    Sequence: list,tuple
    Mapped: dictionary (a key is matched to a value)"""

a = 12 + 46  # int data type
b = "Sarvesh Mishra"  # string data type
c = True  # boolean data type
d = None
print(f"the income earned by {b} is {a}L")

list = [
    4,
    6,
    "hello",
    True,
    ["Guave", "Banana"],
]  # list is a collection of different data types they are mutable
tuple = [
    "Banana",
    "Guava",
    "Apple",
    "Cucumber",
]  # tuples are similar to list but tuples are immutable
print(list)
print(tuple)

dict = {"name": "Sarvesh Mishra", "roll": 52, "marks": 96, "result": True}
print(dict)


print("\n")

# Type casting in python
# The convedrsion of data type form one to another is termed as typecasting
# There are two types: Explicit(Done by user manually) and Implicit(Done by python interpreter automatically

a = "5"
b = "7"
c = 3
d = 4.6
print(a + b)  # a and b are considered as string and they are treated as string
print(int(a) + int(b))  # both a and b are converted to int (Explicit Typecasting)
print(
    c + d
)  # c is int and d is float so c is also converted to float (Implicit Typecasting)


# Taking user input in python
# input() function is used to take user input


name = input("\nEnter you name : ")
print("\nMy name is : ", name)

# The input() function stores the entered value in the form of string
# so we need to typecast if we need any other data type

first = input("Enter the first number :")
second = input("Enter the second number :")

print(first + second)  # here both the variable are treated as strings
print(int(first) + int(second))  # here it is typecasted to integer
