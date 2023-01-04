# You are going to write a virtual coin toss program. It will randomly tell
# the user "Heads" or "Tails".

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲

# Write the rest of your code below this line 👇

import random

print("Heads" if random.randint(0, 1) == 1 else "Tails")
