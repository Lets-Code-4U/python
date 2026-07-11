# The way of calling a function in the function it self is called recurssion

# function to get factorial of a number


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


user_input = int(input("Enter the n to get factorial of it : "))

print(factorial(user_input))


# Function to get fibonacci sequence
def fibonacci(n):
    """Returns the Fibonacci sequence value at index n."""

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(12))
