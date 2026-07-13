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


# Set methods
# Combining sets (union vs update)
# union() : it merges two sets and returns a new set object.Both the sets remains untouched
# update() : changes the target set in place by inserting all unique elements from the incoming set

s1 = {"banana", "guava", "grapes", "orange", "apple", "onion", "cucumber", "carrot"}
s2 = {"onion", "banana", "orange", "apple", "pumpkin", "cabbage"}

print(s1.union(s2))  # combines all unique elements of both sets in new set
print(s1)  # original set remains untouched

s1.update(s2)
print(s1)  # original s1 set has been changed

#  Commonalities (Intersetion vs intersection update)
# intersection() : returns a new set with the common elements of both the sets.Both sets remains untouched
# intersection_update() : changes the caller set to keep only common elements. deletes the remaining items
s1 = {1, 2, 3, 4, 5, 6, 6, 5, 4, 23}
s2 = {1, 2, 3, 6, 7, 3, 2}

print(s1.intersection(s2))  # print common elements of both sets
print(s1)  # original sets remains untouched


s1.intersection_update(s2)
print(s1)  # original set has changed and contains the common elements of both sets


print("\n")
# isdisjoint() : Returns True if both sets have zero common elements
# issuperset() : Returns True if target set contains all elements of incoming set.
# issubset() : Returns True if all elements of target set exixts inside the incoming set
# add() : inserts a single element into the set
# remove() : removes element from set. Thorows keyerror if element not found
# discard() : removes element but ignores the failure if element not found in the set

set1 = {"ram", "shyam", "mohan", "sohan"}
set2 = {1, 2, 3, 4, 5, 5, 7, 3, 2, 1}

print(set1.isdisjoint(set2))
print(set1.issuperset(set2))
print(set1.issubset(set2))
set1.add("sarvesh")
print(set1)
set1.remove("ram")
print(set1)
set1.discard("gagan")
