import random

def rock_paper_scissors():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    # Get user input
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice! Please try again.")
        return

    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")

# Start the game
rock_paper_scissors()
