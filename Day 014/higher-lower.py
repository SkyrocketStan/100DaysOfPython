import random

from art import logo, vs
from game_data import data

print(logo)


def get_competitors():
    return random.sample(data, 2)


def print_competitor(letter, thing: dict):
    name = thing.get("name")
    desc = thing.get("description")
    country = thing.get("country")
    print(f"Compare {letter}: {name}, a {desc}, "
          f"from {country}.")


def print_competitors(first, second):
    # here be first
    print_competitor("A", first)
    # print art
    print(vs)
    # here be the second
    print_competitor("B", second)


def get_choice():
    return input("Who has more followers? Type 'A' or 'B': ").upper()


def print_win_score(score):
    print(f"You're right! Current score: {score}.")


def print_lose_score(score):
    print(f"Sorry, that's wrong. Final score: {score}")


def get_second_competitor(old_choice: dict) -> dict:
    while True:
        new_choice = random.choice(data)
        if new_choice != old_choice:
            return new_choice


def game():
    game_over = False
    score = 0
    competitors = get_competitors()
    the_first: dict = competitors[0]
    the_second: dict = competitors[1]

    while not game_over:
        if score > 0:
            the_first = the_second
            the_second = get_second_competitor(the_first)

        # print competitors
        print_competitors(the_first, the_second)

        # get scores
        first_score = the_first.get("follower_count")
        second_score = the_second.get("follower_count")

        # get the winner
        winner = "A" if first_score > second_score else "B"

        # if wint print the win score
        if get_choice() == winner:
            score += 1
            print_win_score(score)
            continue
        else:  # else drop the game and print lose score
            game_over = True
            print_lose_score(score)


game()
