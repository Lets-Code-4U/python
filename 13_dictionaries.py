# Dictionaries
# A highly powerful built in type used to store data as key value pairs
# Dictionaries officially maintain their insertion order
# Key Rule: Key must be unique and immutable(like strings,integers,tuples)
# Values can be duplicated and hold any mutable object type like list

employees = {"23AI": "sarvesh", "24AI": "mishra", "25AI": "gagan", "26AI": "mohan"}
print(employees["23AI"])  # accessing keys

# Accessing Elements (using [] vs .get())
# Bracket method dict[key] : will crach error if the key is missing
# The dict.get(key) method exists cleanly and returns None if the key is missing

# print(employees["29AI"])   # will catch error
print(employees.get("29AI"))  # retunrs none


# Component Extraction : keys,values,items
# dict.keys() : returns the sequence holding all unique index keys
# dict.values() : returns all associated values
# dict.items() : returns a sequence of (key,value) tuples,unlocking native structural unpacking

print(employees.keys())
print(employees.values())
print(employees.items())

# Accessing the items of dictionary using loop
for key, value in employees.items():
    print(f"The key is {key} and value is {value}")

print("\n")
# list() function is used to get the list of keys, values and items of dictionary
print(list[employees.keys()])
print(list[employees.values()])
print(list[employees])  # returns the list of items of dictionary

# looks for the given key in the dictionary if found returns True if not then False
print("29AI" in employees)

# del vs clear()
# clear() : wipes out the dictionary but leaves the empty dictionary with variable name
# del() : completely erases the dictionary form the memory
# dict.del[key] : only deletes the specific key form the dictionary

dict = {"name": "msihra", "age": 23, "status": "active"}
del dict["age"]
print(dict)
dict.clear()  # cleans the dictionary and it remains empty
print(dict)
del dict
print(dict)  # prints the empty dictionary


print("\n")
# the dict() constructor
# the dict() constructor provides a way to build dictionaries dynamically from other data structures
# like tuples lists or keyword Arguments instead of typing literal {}

# Using keyword arguments
# if key are simple strings we can pass them directly as keyword parameters

user = dict(name="sarvesh", age="23", sex="male", status="active")
print(user)

# Converting a list or tuple of two item sequence
# if data arrives as list of tuples or a tuple of lists where each inner item contains exactly tow elements 
# the constructor maps directly into key value pair

# Here data is list of tuples (the process is same for tuple of lists)
data = [("id", 123), ("name", "mishra"), ("status", "active"), ("zone", "A")]
system = dict(data)
print(system)

# zipping two seprate lists: if we have one sequence of keys and a matching sequence of values 
# we can use built in zip() function inside dict() constructor to pari them 
employee_id = [101, 102, 103, 104]
employee_names = ["mohan", "sohan", "rohan", "rohit"]
record = dict(zip(employee_id, employee_names))
print(record)