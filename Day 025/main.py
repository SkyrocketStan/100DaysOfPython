import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    temps = []
    for x in data:
        if x[1] != "temp":
            temps.append(int(x[1]))
print(temps)
