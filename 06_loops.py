# match case statement
# it contains keyword to match with the case clauses

x = 4
match x:
    case 0:
        print("X is zero")
    case 4:
        print("X is four")
    case _:
        print(x)

# case _: is the default case if none of the case matched it will come forward
print("\n")


# For loops
# loops are used to perform the task are continuous or has a pattern

# loop iteration on string to print all the characters
name = "Mishra"
for i in name:
    print(i)


# iteration over the list to print the list items
colors = ["red", "green", "blue", "yellow"]
for color in colors:
    print(color)


# if we want to iterate for a specific number of times we use range keyword

# we want to run this loop for 5 times and print numbers from 0 to 4
for i in range(5):
    print(i)

# this loop will print the numbers from 2 to 8
for l in range(2, 9):
    print(l)

# break: It tells the program to completely exit the loop immediately
# continue: It skips the remaining code only for that specific iteration and jumps straight to the next loop cycle


# as soon as the counter hits 6 it will immediately stop the loop cycle
for i in range(11):
    if i == 7:
        break
    print(i)

print("\n")
# as the counter hits 7 it will skip the current loop cycle and also the code below the continue and will enter the next cycle
for i in range(11):
    if i == 7:
        continue
    print(i)


# Write a Python loop that goes from 1 to 10.
# If the number is 5, skip it (don't print it).
# If the number hits 8, stop the loop entirely.

for i in range(1, 11):
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
