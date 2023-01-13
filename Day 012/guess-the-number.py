# Number Guessing Game Objectives:
import random

# Include an ASCII art logo. Allow the player to submit a guess for a number
# between 1 and 100. Check user's guess against actual answer. Print "Too
# high." or "Too low." depending on the user's answer. If they got the answer
# correct, show the actual answer to the player. Track the number of turns
# remaining. If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode,
# only 5 guesses in hard mode).

print(""""
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")
player_win = False
in_game = True
while in_game:
    attempts = 0
    number = random.randint(1, 100)
    print(f"DEBUG: {number}")
    difficulty_level = input(
        "Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 10 if difficulty_level == "easy" else 5
    guess = 0

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            player_win = True
            in_game = False
            break
        if guess > number or guess < number:
            stake = "high" if guess > number else "low"
            print(f"Too {stake}.")
            attempts -= 1
            if attempts > 0:
                print("Guess again.")
            else:
                in_game = False

if not player_win:
    print("You've run out of guesses, you lose.")
