import random
import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# This is a function to take input from the user to understand whether the user wants to play on easy mode or hard mode
def choose_difficulty():
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty_level == "hard":
        return HARD_LEVEL_TURNS

# This function checks if the answer is correct, too high or too low and also reduces the number of turns if we guessed it wrong
def check_answer(user_guess, num, turns):
    if user_guess > num:
        print("Too High\nGuess Again")
        return turns - 1
    elif user_guess < num:
        print("Too Low\nGuess Again")
        return turns - 1
    else:
        print(f"You got it! The answer was {num}")

# This is the main algorithm for our game
def num_guess_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = random.randint(1, 100) # assigning a random number to the variable

    num_attempts = choose_difficulty()

    user_guess = 0
    while user_guess != random_number:
        print(f"You have {num_attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        num_attempts = check_answer(user_guess, random_number, num_attempts)

        if num_attempts == 0:
            print(f"You've run out of guesses, you lose.\nThe correct answer was {random_number}")
            return # this will stop the program in case we don't have anymore attempts left

num_guess_game()