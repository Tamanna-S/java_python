#Using just file methods
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    # print(data)

#Using csv library

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row_ka_1st_index in data:
        if row_ka_1st_index[1] != "temp":
            temperatures.append(int(row_ka_1st_index[1]))
    # print(temperatures)

# Using the pandas library
import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

# Get Data in Row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Get Row data value
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp)
#convert it into farenheit
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_from_scartch = pandas.DataFrame(data_dict)
naya_data = data_from_scartch.to_csv("new_data.csv")           # ab ye new_data.csv ek nayi file bn chuki hai isi folder main

print(data_dict)





