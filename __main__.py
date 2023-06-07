"""A CLI for converting numbers between different bases and performing calculations in a given base.

Usage: python main.py

The user is presented with a menu that allows them to select between two options:
converting a number to another base, or doing calculations in a given base. 
The module provides helper functions for getting user input and performing calculations in a given base.
"""


from Group3 import *
import sys

# Define the number of tasks in the menu
NUMBER_OF_TASKS = 2

# Define the tasks in the menu
tasks = [
    "Convert a number to another base",
    "Do calculations in a given base",
]


def serve_menu():
    """Print a menu with two options and handle user input.

    The function prints a menu with two options: converting a number to another base, or doing calculations in a given base.
    It then prompts the user to select an option and handles their input accordingly.
    """

    # Print the menu
    print("=========OPTIONS TO SELECT=========")
    for index, task in enumerate(tasks):
        print(str(index + 1) + ") " + task)

    print("0) Quit")

    # Handle user input
    match get_option():
        case 1:
            # Convert a number to another base
            input_base = get_int(
                "Enter base to input [2..16]: ", lower_bound=2, upper_bound=16
            )
            output_base = get_int(
                "Enter base to output [2..16]: ", lower_bound=2, upper_bound=16
            )
            number_in = get_number_input(input_base)

            print(
                "The result is "
                + dec_to_out_base(inp_base_to_dec(number_in, input_base), output_base)
            )

        case 2:
            # Do calculations in a given base
            operation: str
            while True:
                operation = input("Choose an operation [+, -, *, /]: ").strip()
                if operation in "+-*/":
                    break

            base = get_int(
                "Enter base to calculate [2..16]: ", lower_bound=2, upper_bound=16
            )

            print("\nCalculating a " + operation + " b in base " + str(base) + ".")
            number1 = get_number_input(
                prompt="Input number a in base " + str(base) + ": ", base=base
            )
            number2 = get_number_input(
                prompt="Input number b in base " + str(base) + ": ", base=base
            )

            while operation == "/" and inp_base_to_dec(number2, base) == 0:
                print("Cannot divide by zero. Please input another denominator.")
                number2 = get_number_input(
                    prompt="Input number b in base " + str(base) + ": ", base=base
                )

            while operation == "/" and inp_base_to_dec(number2, base) >= base:
                print(
                    "This feature (dividing by a number larger or equals than base) has not been implemented yet."
                )
                number2 = get_number_input(
                    prompt="Input number b in base " + str(base) + ": ", base=base
                )

            while operation == "-" and inp_base_to_dec(number1, base) < inp_base_to_dec(
                number2, base
            ):
                print(
                    "The function of subtraction with subzero result has not been implemented. Please try again with a > b."
                )
                number1 = get_number_input(
                    prompt="Input number a in base " + str(base) + ": ", base=base
                )
                number2 = get_number_input(
                    prompt="Input number b in base " + str(base) + ": ", base=base
                )

            # Perform the calculation
            match operation:
                case "+":
                    print("The result is " + add(number1, number2, base))

                case "-":
                    print("The result is " + minus(number1, number2, base))

                case "*":
                    print("The result is " + multi(number1, number2, base))

                case "/":
                    print("The result is " + div(number1, number2, base), end="")
                    modulo = mod(number1, number2, base)
                    if inp_base_to_dec(modulo, base) > 0:
                        print(", mod " + modulo)
                    print()


def get_number_input(base, prompt=None):
    """Prompt the user to enter a number in a given base and return it as a string.

    Args:
        base (int): The base of the inputted number.
        prompt (str, optional): The prompt to display to the user. Defaults to None.

    Returns:
        str: The user's input as a string.

    The function prompts the user to enter a number in the given base and returns it as a string. If the user enters an invalid input (i.e. a character that is not a valid digit in the given base), the function prints an error message and prompts the user to enter the number again. The function supports bases from 2 to 16, using the digits 0-9 and the letters A-F to represent values 10-15.
    """

    if not prompt:
        prompt = "Enter a number in base " + str(base) + ": "

    tmp = input(prompt).strip().upper()

    for c in tmp:
        if "0" <= c <= "9":
            digit = int(c)
        elif "A" <= c <= "F":
            digit = ord(c) - 65 + 10
        else:
            print("Invalid input: not a valid base " + str(base) + " number.")
            return get_number_input(base, prompt)

        if digit > base - 1:
            print("Invalid input: not a valid base " + str(base) + " number.")
            return get_number_input(base, prompt)

    return tmp


def get_option():
    """Prompt the user to enter an option from the menu and return it as an integer.

    Returns:
        int: The user's selected option as an integer.

    The function prints a prompt to the user to enter an option from the menu and returns the user's input as an integer. The function validates the user's input to ensure that it is within the range of valid options (0 to NUMBER_OF_TASKS). If the user enters an invalid input, the function prints an error message and prompts the user to enter the option again. If the user enters 0, the function prints "Quit" and exits the program.
    """
    print()
    option = get_int(
        "Enter your choice [0.." + str(NUMBER_OF_TASKS) + "]: ",
        lower_bound=0,
        upper_bound=NUMBER_OF_TASKS,
    )
    if option == 0:
        print("Quit")
        sys.exit(0)
    return option


def get_int(prompt, lower_bound=None, upper_bound=None):
    """Get an integer from stdin, re-prompt if input is invalid.

    Args:
        prompt (str): The prompt to display to the user.
        lower_bound (int, optional): The lowest valid number that the user can input. Defaults to None.
        upper_bound (int, optional): The greatest valid number that the user can input. Defaults to None.

    Returns:
        int: The user's input as an integer.

    The function prompts the user to enter an integer and returns it. If the user enters an invalid input (i.e. a non-integer), the function prints an error message and prompts the user to enter the number again. If `lower_bound` or `upper_bound` are specified, the function checks that the user's input is within the specified range and re-prompts the user if it is not. If the user enters a valid input, the function returns it as an integer.
    """
    while True:
        try:
            tmp = int(input(prompt))
        except ValueError:
            print("Invalid input: input is not a number.")
        else:
            if lower_bound is not None and tmp < lower_bound:
                print("Invalid input: The number inputted is below", lower_bound)
                continue

            if upper_bound is not None and tmp > upper_bound:
                print("Invalid input: The number inputted is above", upper_bound)
                continue

            return tmp


if __name__ == "__main__":
    while True:
        serve_menu()
        input("Press Enter to continue...")
        print()
