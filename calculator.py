import Addition
import Multiplication
import Subtraction
import Division
import sys

try:
    while True:
        print("Let's perform a calculation!")
        print("Addition (0)")
        print("Multiplication (1)")
        print("Subtraction (2)")
        print("Division (3)")
        print("Quit (4)")

        try:
            operation = int(input("Enter the operation you would like to perform (0, 1, 2, 3, 4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 4.\n")
            continue

        if operation == 0:
            try:
                user_input = list(map(int, input("Enter numbers you want to add (space-separated): ").split()))
                add_value = Addition.addition(user_input)
                print(f'The result of addition of {user_input} is: {add_value} \n')
            except ValueError:
                print("Invalid input. Please enter space-separated integers.\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")

        elif operation == 1:
            try:
                user_input = list(map(int, input("Enter numbers you want to multiply (space-separated): ").split()))
                multiply_value = Multiplication.multiply(user_input)
                print(f'The result of multiplication of {user_input} is: {multiply_value} \n')
            except ValueError:
                print("Invalid input. Please enter space-separated integers.\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")

        elif operation == 2:
            try:
                user_input = list(map(int, input("Enter two numbers you want to subtract (space-separated): ").split()))
                if len(user_input) != 2:
                    raise ValueError("Subtraction requires exactly two numbers.")
                sub_value = Subtraction.subtract(user_input[0], user_input[1])
                print(f'The result of subtraction of {user_input[0]} and {user_input[1]} is: {sub_value} \n')
            except ValueError as ve:
                print(f"Invalid input: {ve}\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")

        elif operation == 3:
            try:
                user_input = list(map(int, input("Enter two numbers you want to divide (space-separated): ").split()))
                if len(user_input) != 2:
                    raise ValueError("Division requires exactly two numbers.")
                div_value = Division.divide(user_input[0], user_input[1])
                print(f'The result of division of {user_input[0]} and {user_input[1]} is: {div_value} \n')
            except ZeroDivisionError:
                print("Division by zero is not allowed.\n")
            except ValueError as ve:
                print(f"Invalid input: {ve}\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")

        elif operation == 4:
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid operation (0, 1, 2, 3, or 4).\n")

except KeyboardInterrupt:
    print("\n\nProgram interrupted. Exiting gracefully. Goodbye!")
    sys.exit(0)

except Exception as e:
    print(f"An unexpected error occurred: {e}. Exiting now.")
    sys.exit(1)
