import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

result = [nato_dic[letter] for letter in word]
print(result)
