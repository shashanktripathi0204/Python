import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
print(data["Primary Fur Color"].unique())
Gray = len(data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"].to_list())
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"]["Primary Fur Color"].to_list())
Black = len(data[data["Primary Fur Color"] == "Black"]["Primary Fur Color"].to_list())
color_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[int(f"{Gray}"),int(f"{Cinnamon}"),int(f"{Black}")]
}
print(color_dict)
squirrel_count = pd.DataFrame(color_dict)
squirrel_count.to_csv("squirrel_count")
