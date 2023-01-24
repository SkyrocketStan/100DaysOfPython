with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    letter_text = letter.read()

for name in names:
    name = name.strip()
    new_letter = letter_text.replace("[name]", name)
    filename = f"Output/ReadyToSend/letter_for_{name}.txt"
    with open(filename, mode="x") as file:
        file.write(new_letter)
