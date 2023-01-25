import pandas

data = pandas.read_csv("weather_data.csv")

temp_list = data["temp"].to_list()


def avg(lst):
    return sum(lst) / len(lst)


# find average
print(avg(temp_list))
print(data["temp"].mean())

# find max temp
print(data["temp"].max())

# print dta of max temp
print(data[data.temp == data.temp.max()])
