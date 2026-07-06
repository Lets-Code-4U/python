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