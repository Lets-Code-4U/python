# the mechanism for importing functions, classes, and variables from both built-in Python libraries and external files
#  into our active script is done by using "import" keyword

# The base method brings the entire module into current file context under its own namespace (import module_name)

import math

# Call Syntax: Accessing items requires using the dot notation (module.function)

a = math.sqrt(25)
print(a)


# Selective Importing (from module import item)
# Extracts specific functions or values out of a module and maps them directly into script's base namespace layer

from math import sqrt, pi

a = math.sqrt(49) * pi
print(a)


# (as keyword)
# Renames imported modules or specific functions locally to shorten long package definitions (e.g., TensorFlow or Pandas)

import math as mt

a = mt.sqrt(4)
print(a)

from math import pi as p

print(p)


# . Local File Importing
# You can import custom scripts located within the same folder space using the import keyword

import import_demo as demo

print(demo.welcome())
print(demo.addition(10, 9))
print(demo.substraction(99, 34))
