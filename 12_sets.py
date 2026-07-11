# A set in python is defined as an unordered collection of unique items enclosed within {}
# Auto-De-duplication : if you try to feed multiple duplicate entries into a set literal python
# drops the repeating elements and retains exactly one unique instance.
# Unordered Execution : Sets do not maintain insertion order.
# the position of items is completely unstable and random.

s = {2, 3, 5, 7, 8, 9, 2, 3, 7, 8}
print(s)  # items are unordered in the output and not repeated items

info = {True, 19, "Mishra", 5.9, 19}
print(info)  # repeated items are removed and are unordered


# Indexing Restrictions: because items are randomly placed in memory sets do not support indexing or slicing expressions
# if you try to access the items of sets it returns an error
# Note : The dictionary and set both uses {} brackets for storing literals so ,
# empty set created using {} is considered as empty dictionary not set
# if you want to create empty set use set() function

info = {}
print(type(info))  # returns the data type of info (dictionary)

info = set()
print(type(info))  # not info is an empty set


print("\n")
# if we ever want to go throught the set items we need to loop through the set

set = {
    "mishra",
    True,
    "banana",
    34,
    23.4,
}
for value in set:
    print(value)

