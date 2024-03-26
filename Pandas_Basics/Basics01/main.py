# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# sum = 0
# for i in temp_list:
#     sum = sum + int(i)
# print(f"avg = {sum/len(temp_list)}")

# printing row
# print(data[data.day == "Tuesday"])
#
# # printing row with max temp
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print((monday.temp[0])*9/5 + 32)

# creating data frame from strach

data_dict = {
    "students" : ["Amy", "Raj", "Penny"],
    "Scores" : [99,100,40]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("data.csv")