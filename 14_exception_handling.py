# when an error occurs in the normal pyhton script the interpreter halts the execution immediately and crashes
# To bypass this program haltion we use try-except structure to catch error cleanly and continue the program
# The 'try' block : addressed the code block that have the chance of failing at runtime
# (like user input,fetching data from server,opening files...)
# 'except' block : act as a safety net if any exception occurs under try block, this block is executed to
# continue the program or application running

user_input = "mishra"
try:
    num = int(user_input)
    print("Here is an error, trying to parse the string to integer.")
except:
    print("There is an exception in the try block so this block is executiog.")

print("Still there is an exception error, the application continues.")


# using 'except' block we can target specific exception types to treat different errors uniquily
# ValueError: Triggers when a function receives an argument of the correct type but an invalid value
# IndexError: Triggers when trying to access a sequence index that is out of range
# ZeroDivisionError: Triggers when the denominator in a division operation is zero.

try:
    a = [10, 20]
    index = int(input("Enter index: "))
    print(a[index])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index error occurred. Out of range.")

# when error happens in the try block it looks for a matching exception block
# If a matching exception type is found, control moves to that block and execution resumes normally
# If the exception type does not match any blocks, it crashes the program

data = [10, 5, 0]

try:
    idx = int("2")  # string converted to integer
    val = data[idx]  # val stores the 2nd index value (0)
    result = 100 / val  # here 100/0  encounters an error (zeroDivisionError)
    print("Calculated:", result)

except ValueError:
    print("Caught a ValueError")

except IndexError:
    print("Caught an IndexError")

except ZeroDivisionError:
    print("Caught a ZeroDivisionError")

print("System Check Complete")


print("\n")
# The 'finally' keyword
# The code inside a finally block is guaranteed to execute,
# regardless of whether an error was thrown or handled successfully

try:
    list = [1, 2, 3, 4, 5]
    user_input = int(input("Enter the index : "))
    print(list[user_input])
except:
    print("Some error occured!")
finally:
    print("This block execution is completed,")

print("\n")
# even if we write a normal print statement outside the try-except block it will behave the same way as finally,
# but , the finally keyword plays a vital inside function
"""python rule says that as soon as a function encounters a return statement, it terminates immediately, 
and ignores all subsequent code lines in its block
However, the finally clause overrides this rule. 
Even if Python hits a return statement inside the try block or the except block, 
it forces the system to pause, execute the code inside the finally block first, 
and only then return the value out of the function"""


def func():
    try:
        list = [1, 2, 3, 4, 5]
        user_input = int(input("Enter the index : "))
        print(list[user_input])
        return 1
    except:
        print("Some error occured!")
        return 0
    finally:
        print("This block execution is completed,")


x = func()
print(x)



