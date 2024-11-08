import random

# Initialize the attempt counter
attempt = 1

# Generate a random number between 1 and 20
target = random.randint(1, 20)

# Loop to allow the player 7 attempts to guess the number
while attempt <= 7:
    # Prompt the user to guess the number
    guess = int(input("Enter your guess (between 1 and 20): "))

    # Display the attempt number and guessed number
    print(f"Attempt {attempt}: You guessed {guess}")

    # Check if the guess is correct
    if guess == target:
        print("Congratulations! You've won the game.")
        break
    else:
        print("Incorrect guess. Please try again.")

    # Increment the attempt counter
    attempt += 1

# If the player has used all attempts, they lose the game
if attempt > 7:
    print(f"Sorry, you've lost the game. The correct number was {target}. Better luck next time!")
