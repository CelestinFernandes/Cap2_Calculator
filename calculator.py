import Addition
import Multiplication
import Subtraction
import Division

while True:
    print("Let's perform a calculation!")
    print("Addition (0)")
    print("Multiplication (1)")
    print("Subtraction (2)")
    print("Division (3)")
    print("Quit (4)")

    operation = int(input("Enter the operation you would like to perform (0, 1, 2, 3, 4): "))

    if operation == 0:
        try: 
            user_input = list(map(int, input("Enter numbers you want to add (space-separated): ").split()))
        except ValueError:
            print("Wrong input, recheck input")
            continue
        add_value = Addition.addition(user_input)
        print(f'The result of addition of {user_input} is: {add_value} \n')

    elif operation == 1:
        try: 
            user_input = list(map(int, input("Enter numbers you want to multiply (space-separated): ").split()))
        except ValueError:
            print("Wrong input, recheck input")
            continue
        multiply_value = Multiplication.multiply(user_input)
        print(f'The result of multiplication of {user_input} is: {multiply_value} \n')

    elif operation == 2:
        try:
            user_input = list(map(int, input("Enter two numbers you want to subtract (space-separated): ").split()))
        except ValueError:
            print("Wrong input, recheck input")
            continue
        sub_value = Subtraction.subtract(user_input[0], user_input[1])
        print(f'The result of subtraction of {user_input[0]} and {user_input[1]} is: {sub_value} \n')

    elif operation  == 3:
        try:
            user_input = list(map(int, input("Enter two numbers you want to divide (space-separated): ").split()))
        except ValueError:
            print("Wrong input, recheck input")
            continue
        div_value = Division.divide(user_input[0], user_input[1])
        print(f'The result of division of {user_input[0]} and {user_input[1]} is: {div_value} \n')

    elif ((operation == 4) or (operation not in [0, 1, 2, 3])):
        break