# Issue
# We've got some buggy code. Try running the code. The code will crash and
# give you an IndexError. This is because we're looking through the list of
# fruits for an index that is out of range.

# Instructions
# Use what you've learnt about exception handling to prevent the program from
# crashing. If the user enters something that is out of range just print a
# default output of "Fruit pie".

# Hint
# You'll need to catch the IndexError exception.
# You'll need the try, except and else keywords.

fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
