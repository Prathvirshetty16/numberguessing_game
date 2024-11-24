import random

# Function to start the guessing game
def number_guessing_game():
    # Generate a random number between 1 and 200
    number_to_guess = random.randint(1, 200)
    
    # Variable to track the number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Your goal is to guess the number.")
    
    # Loop to allow the user to keep guessing
    while True:
        # Take user input for their guess
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        # Increment the attempt counter
        attempts += 1
        
        # Check if the guess is correct, too high, or too low
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break  # Exit the loop if the guess is correct

# Call the function to start the game
number_guessing_game()
