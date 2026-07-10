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
