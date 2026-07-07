# Conditional statements are used to perform the task based on the condition is true or false
# if
# if-else
# if-elif


# if statement
age = int(input("Enter the age : "))
if age >= 18:
    print("You can vote")


# if-else statement
if age >= 18:
    print("Adult")
else:
    print("Minor")


# if-elif-else statement
score = int(input("\nEnter the score : "))
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Fail")


# Combining Conditions (Logical Operators)
# Can check multiple things at once inside a single if statement using and, or, and not.
print("\n")

is_ticket = True
is_id = True
if is_ticket and is_id:
    print("Welcome to the show")
else:
    print("You can not enter")


is_weekend = True
is_holiday = False
if is_weekend or is_holiday:
    print("Hurray !!")


# Short hand or Ternary operator

result = "Adult" if age >= 18 else "Minor"
# result will be adult if age>= 18 else it will be minor
print(result)



# Match case
# it looks to the variable and matches it to the case it fits

# day is the variable and 1,2,3 are cases to matched with the day
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")  # This is the one that will execute!
    case _:
        print("Invalid day number")

# case_  is the default case
import random

device_list = ["iphone14", "samsungs24", "vivo23", "iphone13"]
device = device_list[random.randint(0, 3)]

match device:
    case "iphone14" | "iphone13":
        operating_system = "ios"
    case "samsungs24" | "vivo23":
        operating_system = "android"
    case _:
        operating_system = "unknown"
print(f"The operating for the {device} is {operating_system}")


