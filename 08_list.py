# Lists in python contain mixed datatypes simultaneously
# Lists are mutable, we can alter,delete,or replace its elements dynamically after creation in the memory
#  it has zero based indexing
# for list of lenght n the positive index range form 0 to n-1
# negative indexing: it queries items from right to left means -1 is for last element
# positive index = length of list +(Negative index)
# if the len(list)=5 and negative index is -3 then positive index = 5+(-3)=2 means list[2]=list[-3]


marks = [35, 46, 67, "Sarvesh", "pass"]
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])


# slicing and jumping
# list[1:6:1] means start form index 1 got till 5(last or end limit is excluded) by skipping 1 index

animals = ["cat", "bat", "rat", "cow", "pig", "dog", "goat", "sheep"]

print(animals[1:6:1])
# means start from index 1 print till index 5 by jumping 1 index or element


# The "in" keyword : scans the list to check the item availability and returns boolean

print("cat" in animals)  # checks for cat in animals list

if "cow" in animals:
    print("\nThe cow is pet animal")
else:
    print("not found")

if "monkey" in animals:
    print("Found in the list")
else:
    print("not found")


# List comprehension or list short hand
# first for loop is countered and then the body of loop i*i
list1 = [i * i for i in range(5)]
print(list1)


# here after for loop the if statement is executed and then the task i*i
list2 = [i * i for i in range(12) if i % 2 == 0]
print(list2)


