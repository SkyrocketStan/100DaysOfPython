# Take a look inside file1.txt and file2.txt. They each contain a bunch of
# numbers, each number on a new line.
#
# You are going to create a list called result which contains the numbers
# that are common in both files.

def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()
    return [n.strip() for n in lines]


file_1 = read_file("file1.txt")
file_2 = read_file("file2.txt")

result = [int(n) for n in file_1 if n in file_2]
# Write your code above 👆

print(result)
