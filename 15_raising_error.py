# The raise keyword: Sometimes, letting a program continue running with invalid parameters is far more dangerous than
# stopping it immediately.raise keyword is used to flag these anomalies instantly, stopping corrupt operations

user_input = int(input("Enter a number between 2 and 6: "))
if user_input <= 2 or user_input >= 6:
    raise ValueError("Invalid entry detected!")

# program that handles decimal checks, string validations, and exits when the user types "quit" in any case format:


def validate_user_input():
    user_input = (
        input("Enter a value between 5 and 9 (or 'quit' to exit): ").strip().lower()
    )

    # termination check
    if user_input == "quit":
        print("Exiting application gracefully...")
        return

    try:
        # Step 1: Check if it can be converted to a numeric type
        num = float(user_input)
    except ValueError:
        # Step 2: If it's not a number (and not 'quit'), raise a ValueError
        raise ValueError(f"Invalid input: '{user_input}' is not a valid number!")

    # Step 3: Check bounds
    if num < 5 or num > 9:
        raise ValueError(f"Out of bounds! Value {num} is not between 5 and 9.")

    print(f"Success! Your validated value is: {num}")


# --- Test Executions ---
try:
    validate_user_input()
except ValueError as error:
    print(f"Caught Raised Error -> {error}")
