"""

    New elements are to be added in the following way:
        1) Function itself in Function Definition Section
        2) Adding new element in Program Design section, in the list "menu".
            New elements are added before last element (before Quit).
        3) Function Calling Section - New condition option following the sequence.

    You select operation from the list

"""


#   Function Definition Section
def addition(a: float, b: float):
    result = a + b
    print(f"Result = {result}")


def subtraction(a: float, b: float):
    result = a - b
    print(f"Result = {result}")


def multiplication(a: float, b: float):
    result = a * b
    print(f"Result = {result}")


def division(a: float, b: float):
    if b == 0:
        print(f"{a} can not be divided by {b}")
        return
    else:
        result = a / b
    print(f"result = {result}")


# Program Design
print("Python Calculator")
menu = list("Menu: Addition Subtraction Multiplication Division Quit".split())

while True:
    print()
    for index in range(len(menu)):
        if index == 0:
            print(f"{menu[index]}")
        else:
            print(f"{index}. {menu[index]}")
    print()

    command = input(f"Select option from Menu, in range [1,{len(menu) - 1}] ")
    if command == str(len(menu) - 1):
        print("Goodbye!")
        break
    else:
        if not command.isdigit():
            print("\nSelect Valid option!\n")
            continue
        else:
            command_int = int(command)
            if len(menu) - 1 <= command_int > 0:
                print(f"\nSelect valid Option from Menu, in range [1,{len(menu) - 1}] ")
                continue
            operation = menu[command_int]
            while True:
                number_1 = input("Enter the first number: ")
                if not (all(char.isdigit() or char == '.' or (char == '-' and i == 0) for i, char in enumerate(number_1.strip()))):
                    print(f"\nYou selected '{operation}' from the menu.")
                    print("Select a valid value for the first number!\n")
                    continue
                break
            while True:
                number_2 = input("Enter the second number: ")

                if not (all(char.isdigit() or char == '.' or (char == '-' and i == 0) for i, char in enumerate(number_2.strip()))):
                    print(f"\nYou selected '{operation}' from the menu.")
                    print(f"First number = {number_1}")
                    print("Select a valid value for the second number!\n")
                    continue
                break
            number_1_digit = float(number_1)
            number_2_digit = float(number_2)
            print(f"\nOperation = {operation}")
            print(f"First number = {number_1}")
            print(f"Second number = {number_2}")

            # Function Calling section
            if command_int == 1:
                addition(number_1_digit, number_2_digit)
            elif command_int == 2:
                subtraction(number_1_digit, number_2_digit)
            elif command_int == 3:
                multiplication(number_1_digit, number_2_digit)
            elif command_int == 4:
                division(number_1_digit, number_2_digit)
