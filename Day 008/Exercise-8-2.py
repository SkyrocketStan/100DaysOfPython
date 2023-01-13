# Write your code below this line 👇
import math


def prime_checker(number):
    if (number == 1) or (number > 2 and number % 2 == 0):
        print("It's not a prime number.")
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            print("It's not a prime number.")
            return False
    print("It's a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
