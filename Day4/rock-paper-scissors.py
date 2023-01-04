import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


# Write your code below this line 👇

def print_figure(fig):
    if fig == 0:
        print(rock)
    elif fig == 1:
        print(paper)
    elif fig == 2:
        print(scissors)


rps_player = int(input("Rock - 0, Paper - 1, Scissors - 2: "))
rps_computer = random.randint(0, 2)

print("Player choice:", end="")
print_figure(rps_player)
print("Computer choice:", end="")
print_figure(rps_computer)

if rps_computer == rps_player:
    print("Tie")
elif (rps_player == 0 and rps_computer != 1) or \
        (rps_player == 1 and rps_computer != 2) or \
        (rps_player == 2 and rps_computer != 0):
    print("Player win!")
else:
    print("Computer win")
