import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 9

    while True:
        try:
            user_guess = int(input("Enter the number "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please enter a number within the valid range (1-100).")
                continue

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number correctly.")
                print(f"It took you {attempts} attempts to guess the number.")
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Start the game
number_guessing_game()
