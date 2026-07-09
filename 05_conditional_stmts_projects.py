# Basic Projects to understand the logic of conditional statements

# Project 01
# Ask the user for the weight of their package in kg.
# Determine the base cost using these rules:
# Under 2 kg: $5.00
# 2 kg to 6 kg: $8.50
# Over 6 kg to 10 kg: $12.00
# Over 10 kg: Print "Package too heavy for standard shipping."
# Ask if they want Express Delivery (adds a flat $5.00 to the total).
# Print the final shipping cost.

weight = int(input("\nEnter the weight (in kg): "))
delivery_input = input("Do you want express delivery (yes/no): ").strip().lower()

# will check delivery_input is equal to "yes" if found it returns True else False and stores in delivery_type variable
delivery_type = delivery_input == "yes"

# We initialize cost as None to handle the "too heavy" or invalid edge cases
cost = None

# Cleaner ranges: since they evaluate top-to-bottom, we don't need 'and'
if weight <= 0:
    print("Enter a valid weight.")
elif weight <= 2:
    cost = 50 * weight
elif weight <= 6:
    cost = 80 * weight
elif weight <= 10:
    cost = 120 * weight
else:
    print("Package is too heavy for standard shipping.")

# Only calculate final cost if a valid base cost was assigned
if cost is not None:
    final_cost = cost + 50 if delivery_type else cost
    print("\nThe final delivery cost is: ", final_cost)


print("\n")
# Project 02

# Rock, Paper, Scissors
# Create a game where the user plays Rock, Paper, Scissors against the computer.
# Import the random module to let the computer choose randomly from a list: ["rock", "paper", "scissors"].
# Take the user's input.
# Use conditional statements to check who won.
# Tip: First check if it's a tie (user_choice == computer_choice). Then check all the ways the user could win.
#  Use else to cover the computer winning.


import random  # this module will generate random numbers within in range

# list of choices for computer
computer_list = ["rock", "paper", "scissors"]

# indexing random list items using random module
computer_choice = computer_list[random.randint(0, 2)]

user_choice = input("Enter you choice(rock,paper,scissors) : ").strip().lower()

# checking user input is valid or not by using the list of valid choices
if user_choice not in computer_list:
    print("Error! Invalid choice")
    exit()
else:
    print(f"Your choice is :{user_choice}")

result = None

if user_choice == computer_choice:
    result = "This is tie!"
elif user_choice == "rock" and computer_choice == "paper":
    result = 1
elif user_choice == "rock" and computer_choice == "scissors":
    result = 0
elif user_choice == "paper" and computer_choice == "rock":
    result = 0
elif user_choice == "paper" and computer_choice == "scissors":
    result = 1
elif user_choice == "scissors" and computer_choice == "rock":
    result = 1
elif user_choice == "scissors" and computer_choice == "paper":
    result = 0

if result is not None:
    if result == "This is tie!":
        print(result)
    elif result == 1:
        print("Computer won the match!")
        print("Better luck next time!")
    elif result == 0:
        print("Congratulations! You won")
