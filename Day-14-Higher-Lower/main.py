import art
import random
from game_data import data
from replit import clear


def is_user_correct(guess, a_count, b_count):
    if a_count > b_count:
        return guess == "A"
    else:
        return guess == "B"

def generate_b(data, a):
    b = random.choice(data)
    while b == a:
        b = random.choice(data)
    return b

def get_formatted_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def game():
    print(art.logo)
    current_score = 0
    continue_game = True
    compare_a = random.choice(data)
    while continue_game:
        print(f"Compare A: {get_formatted_data(compare_a)}")
        print(art.vs)
        compare_b = generate_b(data, compare_a)
        print(f"Against B: {get_formatted_data(compare_b)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear()
        print(art.logo)
        if is_user_correct(guess, compare_a["follower_count"], compare_b["follower_count"]):
            current_score += 1
            print(f"You're right! Current score: {current_score}")
            compare_a = compare_b
        else:
            continue_game = False

    print(f"Sorry, that's wrong. Final score: {current_score}")


game()
