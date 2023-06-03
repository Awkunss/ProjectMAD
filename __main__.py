from Group3 import *
import sys

NUMBER_OF_TASKS = 2

tasks = [
    "Convert a number to another base",
    "Do calculations in a given base",
]


def serve_menu():
    """Serve the menu to user"""

    # Print the menu
    print("===OPTIONS TO SELECT===")
    for index, task in enumerate(tasks):
        print(str(index + 1) + ": " + task)

    print("0: Quit")

    match get_option():
        case 1:
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

            match operation:
                case "+":
                    print("The result is " + add(number1, number2, base))

                case "-":
                    ...

                case "*":
                    print("The result is " + multi(number1, number2, base))

                case "/":
                    try:
                        ...
                    except ZeroDivisionError:
                        print("For god's sake you cannot divide by zero.")


def get_number_input(base, prompt=None):
    """Get number input in a given base.
    Args:
        base (int): base of the inputted number
        prompt (str): the prompt to print out
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
    """Get an option from menu"""
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
    """Get an integer from stdin, re-prompt if input is invalid
    Args:
        prompt (str): prompt to print out to user
        lower_bound (int): The lowest valid number that the user can input
        upper_bound (int): The greatest valid number that the user can input
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
