# 1. Getting data with inbuilt libraries
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# 2. Getting data with csv library
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)  # printing CSV file data
# print(type(data)) # printing object type. In this case is a DataFrame class
# print(data["temp"])  # printing temperature data
# print(type(data["temp"]))  # printing object type. In this case is a Series class

data_dict = data.to_dict()  # converting data to dictionary
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

average_temp = sum(temp_list) / len(temp_list)
print(f"Average temperature is {average_temp}")
# or
print(data["temp"].mean())

max_temperature = data["temp"].max()
print(f"Maximum temperature is {max_temperature}")

print(data["temp"]) #  Getting COLUMN data in "temp" Column

print(data[data["day"] == "Monday"]) # Getting ROW data where day = Monday
print(data[data["temp"] == data["temp"].max()]) # Getting ROW data which has maximum temperature

monday = data[data.day == "Monday"]
print(monday.condition[0])
print(monday.temp[0] * 1.8 + 32) #fahrenheit = (1.8 * celsius) + 32.

# ----------------------------------------------------------------
# Create a Dataframe and CSV file
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv") # Creating new CSV file
