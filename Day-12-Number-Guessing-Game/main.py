#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)
#print(f"Pssst, the correct answer is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    turns = 10
else:
    turns = 5

continue_game = True
is_number_guessed = False
while continue_game:
    print(f"You have {turns} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    turns -= 1
    if guess == random_number:
        continue_game = False
        is_number_guessed = True
    else:
        if guess > random_number:
            print("Too high.")
        else:
            print("Too low.")

        if turns == 0:
            continue_game = False
        else:
            print("Guess again.")

if is_number_guessed:
    print(f"You got it! The answer was {random_number}.")
else:
    print("You've run out of guesses, you lose.")
