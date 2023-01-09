import os

from art import logo


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# HINT: You can call clear() to clear the output in the console.
# clear()

print(logo)
bids = {}

while True:
    name = input("name: ")
    price = int(input("price: "))
    bids[name] = price
    next_person = input("Is there another person (Yes/No)").lower()
    if next_person == "yes":
        clear()
        continue
    else:
        break

winner = ""
for key in bids:
    max_price = 0
    if bids[key] > max_price:
        winner = key
else:
    print(f"The winner is {winner} and bid is {bids[winner]}")
