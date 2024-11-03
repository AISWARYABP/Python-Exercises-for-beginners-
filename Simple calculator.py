# Simple Calculator

# Function to perform the chosen operation
def calculator():
    # Take input from the user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display available operations
    print("Choose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take the choice of operation from the user
    choice = input("Enter your choice (1/2/3/4): ")

    # Perform the operation based on user's choice
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator function
calculator()
