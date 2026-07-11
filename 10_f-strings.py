# Formatted string literals
# simply adding the letter f or F directly brofre a string's opening quote
# enables user to inject variables directly inside {}

name = "Sarvesh"
country = "India"
print(f"My name is {name} and I am form {country}")


# f-string accepts formatting syntax inside { } by appending a colon
# followed by format specifior like :.2f
# we can control decimal precision and rounding automatically

price = 54.59978
txt = f"The current price of item in stock is {price:.2f} rupees."
print(txt)

# if in condition where we literally need to print { } we wrap them in another one like {{}}

print(f"We are learning f-strings like: {{name}}")  # considers {name} a part of string

print(f"We are learning f-strings like: {{{name}}}")  # considers {name} as variable


# Inline Evacuation : f-strings can compile any valid expression at run time
#  we can process math operations,methods,conditional stmts inside the {}

print(f"Math : {2*3}")
print(f"Transform : {'test' .upper()}")


# Docstrings(Document Strings) in python
# Docstrings are string literals that are used to document fumctions, classes, parameters and returns
# They describe technical purpose of the block.
# Note: There is a strict condition that, the string literal should be just below the function/class ('def' line) definition
# not even a single line of code should be between string literal and the function definition not even comments


def square(num):
    """This function takes a number num,and squares it"""
    print(num**2)


square(5)
print(square.__doc__)


def sum(a, b):
    print(a, b)
    """This function does the sum of two numbers"""
    return a + b


print(sum(5, 8))
print(sum.__doc__)
# will print NONE because the print line is between the fun definition and docstring
