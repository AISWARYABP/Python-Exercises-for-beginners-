import math
from sympy import symbols, Eq, solve

# Scientific Calculator Function
def scientific_calculator():
    print("Welcome to the Scientific Calculator!")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")
    print("11. Solve Equation")

    # Get user's choice
    choice = input("Enter your choice (1-11): ")

    # Basic arithmetic operations
    if choice in ['1', '2', '3', '4', '6']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            print(f"The result of {num1} + {num2} is: {num1 + num2}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is: {num1 - num2}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is: {num1 * num2}")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"The result of {num1} / {num2} is: {num1 / num2}")
        elif choice == '6':
            print(f"The result of {num1} ^ {num2} is: {num1 ** num2}")
    
    # Square root
    elif choice == '5':
        num = float(input("Enter a number: "))
        if num < 0:
            print("Error: Square root of a negative number is not allowed.")
        else:
            print(f"The square root of {num} is: {math.sqrt(num)}")
    
    # Trigonometric functions
    elif choice == '7':
        angle = float(input("Enter the angle in degrees: "))
        print(f"The sine of {angle} degrees is: {math.sin(math.radians(angle))}")
    elif choice == '8':
        angle = float(input("Enter the angle in degrees: "))
        print(f"The cosine of {angle} degrees is: {math.cos(math.radians(angle))}")
    elif choice == '9':
        angle = float(input("Enter the angle in degrees: "))
        print(f"The tangent of {angle} degrees is: {math.tan(math.radians(angle))}")

    # Logarithmic function
    elif choice == '10':
        num = float(input("Enter the number: "))
        base = float(input("Enter the base (default is e): ") or math.e)
        if num <= 0 or base <= 0:
            print("Error: Logarithm of zero or negative number is not allowed.")
        else:
            print(f"The logarithm of {num} with base {base} is: {math.log(num, base)}")
    
    # Equation solving
    elif choice == '11':
        print("Equation solving (e.g., enter 'x + 2 - 3 = 0')")
        equation_input = input("Enter the equation: ")
        x = symbols('x')  # Define the variable
        equation = Eq(eval(equation_input.replace('=', '==')))
        solutions = solve(equation, x)
        print(f"The solution(s) for the equation is/are: {solutions}")

    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator function
scientific_calculator()
