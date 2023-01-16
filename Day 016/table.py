from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
table.align = "l"
print(table)
