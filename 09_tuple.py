# Tupes in Python
# A tuple is an ordered immutable collection of elements enclosed in ()

tup = (1, 2, 3, 4, "Sarvesh", "Good")
print(type(tup), tup)  # prints the datatype of tup and literals of tup

# as tuple is immutable you can not add or remove or modify the elements of tuple once it is saved in memory
# Indexing of tuples: positive and negative indexing

print(tup[3])  # element at index 3
print(tup[-2])  # element at index 4 (len(tup)+(negative index) 6-2=4)

# 'in' keyword: checks an element availability in the tuple and returns boolean

print("Good" in tup)

if 1 in tup:
    print("Found")

# Tuple slicing: tup[start:end]   end is excluded

print(tup[1:5])  # prints values form indices 1 to 4 (4th index is excluded)

#  Indirect Tupe Modification : we can not modify tuple directly so
#  we convert tuple to list using list()
#  apply the list operation and methods and convert the list back to tuple using tuple()

countries = ("india", "germany", "spain", "russia", "italy")
print(countries)
temp = list(countries)  # converting tuple to list and storing in temp
temp.append("England")  # appending to the list temp
temp.pop(4)  # removing the index 4 element 4 from list
temp[2] = "France"  # adding element at index 2
countries = tuple(temp)  # converting list back to tuple
print(countries)


# Tuple concatenation : two tuples can be merged using "+" operator
# Both the tuples remain untouched in their original form

food1 = ("paneer", "tofu", "peanuts", "chickpea")
food2 = ("vegetables", "fruits", "legumes")
dish = food1 + food2
print(dish)


# .count() and .index() methods
# .count(value) conunts how many times an item appears in the collection
# .index(value,start,end) within the given range scans for the first occuring of the value and retruns the +ve index w
#  start and end are optional
#  if the value is not found in the tuple or within the given range it crashes a ValueError

tuple = (1, 2, 3, 4, 5, 6, 2, 3, 3, 5, 4, 2, 6, 1)
print(tuple.count(3))  # counts the 3 in tuple and returns int
print(tuple.index(3))  # returns the index of first occuring of 3
print(tuple.index(3, 1, 7))
# scans for 3 in the index range 1 to 7 and returns the index of 3
