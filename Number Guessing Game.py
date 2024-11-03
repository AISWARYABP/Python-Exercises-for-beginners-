import random

def number_guessing_game():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100
    target_number = random.randint(lower_bound, upper_bound)

    print(f"Welcome to the Number Guessing Game!")
    print(f"I have selected a number between {lower_bound} and {upper_bound}. Try to guess it!")

    attempts = 0
    while True:
        # User input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break

# Start the game
number_guessing_game()
