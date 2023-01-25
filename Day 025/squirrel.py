import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_sq = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sq, cinnamon_sq, black_sq]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")