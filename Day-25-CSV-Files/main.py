import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(len(data[data["Primary Fur Color"] == "Gray"]))
new_data_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [len(data[data["Primary Fur Color"] == "Gray"]),
              len(data[data["Primary Fur Color"] == "Cinnamon"]),
              len(data[data["Primary Fur Color"] == "Black"])]
}
df = pandas.DataFrame(new_data_dict)
print(df)
df.to_csv("squirrel_count.csv") # Creating new CSV file