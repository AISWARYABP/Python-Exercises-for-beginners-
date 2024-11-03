def multiplication_table(number, range_limit):
    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, range_limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Input from the user
try:
    num = int(input("Enter a number to generate its multiplication table: "))
    limit = int(input("Enter the range for the multiplication table: "))
    
    multiplication_table(num, limit)
except ValueError:
    print("Please enter valid integers.")
