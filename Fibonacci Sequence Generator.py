def fibonacci_sequence(n):
    # Initialize the first two terms of the sequence
    fib_sequence = [0, 1]
    
    # Generate the sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)

    return fib_sequence[:n]

# Input from the user
num_terms = int(input("Enter the number of terms in the Fibonacci sequence: "))

# Generate and display the Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print("Fibonacci sequence up to 1 term: [0]")
else:
    print(f"Fibonacci sequence up to {num_terms} terms: {fibonacci_sequence(num_terms)}")
