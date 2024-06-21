import random

def guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None
    
    print("Welcome to the Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Can you guess what it is?")
    
    # Loop until the user guesses the correct number
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    guessing_game()
