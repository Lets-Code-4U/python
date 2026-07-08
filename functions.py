# Functions are block of code logic that we can reuse it without rewriting th same line over and over
# The Syntax Rule:write 'def' keyword followed by the function name, set of parentheses (), and a colon : at the end


def calculate_gmean(a, b):
    gmean = (a * b) / (a + b)
    print(gmean)


# calling a function
calculate_gmean(8, 9)
calculate_gmean(7, 3)


# if we have planned to use a function called addition in future,
#  but we have not build the logic for it so we can not leave it blank
# if it is left blank it will crash an error
# so we use "pass" keyword to leave it empty


def addition():
    pass


# Define a function called check_number that takes one argument named num.
# Inside the function, if num is greater than 0, print "Positive".
# If num is less than 0, print "Negative".
# If num is exactly 0, just use the pass statement (do nothing).
# Call your function at the bottom with a number like 5 or -3.


def check_number(num):
    if num == 0:
        pass
    elif num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")


check_number(5)
check_number(-3)
check_number(0)


print("\n")
# Create a function called find_total_spend.
# It should accept one argument called expenses (which will be a list of numbers).
# Inside the function, create a variable called total = 0.
# Use a for loop to iterate through the list and add each expense to total.
# Use the return keyword to return the final total.
# Outside the function, create a list of mock numbers: my_expenses = [120, 50, 300, 45]
# Call your function, pass my_expenses into it, save the result in a variable, and print it.


def find_total_spend(expenses):
    total = 0
    for item in expenses:
        total = total + item
    return total


my_expenses = [120, 234, 300, 46]
total_expenses = find_total_spend(my_expenses)
print(total_expenses)
print("\n")


# Write a function called remove_zeros that takes a list called data.
# Inside, create an empty list called clean_data = [].
# Loop through data. If an item is not equal to 0 (using != 0), append it to clean_data.
# Return clean_data.
# Test it with test_list = [10, 0, 25, 0, 42] and print the returned result.


def remove_zeros(data):
    clean_data = []
    for data in data:
        if data != 0:
            clean_data.append(data)
    return clean_data


test_list = [10, 0, 25, 0, 42]
print(remove_zeros(test_list))
