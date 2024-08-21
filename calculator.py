import Addition

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

    # elif operation = 1, 2, 3

    elif ((operation == 4) or (operation not in [0, 1, 2, 3])):
        break