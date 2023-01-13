
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

big_name = name1.lower() + name2.lower()

true_numbers = 0
love_numbers = 0

for letter in "true":
    true_numbers += big_name.count(letter)

for letter in "love":
    love_numbers += big_name.count(letter)

score = int(str(true_numbers) + str(love_numbers))

print(f"Your score is {score}", end="")
if score < 10 or score > 90:
    print(", you go together like coke and mentos.")
elif 40 <= score <= 50:
    print(", you are alright together.")
else:
    print(".")
