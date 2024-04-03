# import tkinter
from tkinter import *

def miles_to_km():
    print("I got clicked")
    miles =  float(miles_ip.get())
    print(miles)
    km = round(miles * 1.60934, 2)
    km_cal_label.config(text = f"{km}")


window = Tk()
window.title("Miles to Km")
window.minsize(width=100, height=100)

# so many labels are just to get the grid layout
# label
my_label = Label(text = "", font=("Arial",24,"bold"))
# my_label.config(text = "New Text")
my_label.grid(row = 0, column = 0)

my_label = Label(text = "Is Equal to ", font=("Arial",24,"bold"))
# my_label.config(text = "New Text")
my_label.grid(row = 1, column = 0)

my_label = Label(text = "", font=("Arial",24,"bold"))
# my_label.config(text = "New Text")
my_label.grid(row = 2, column = 0)

miles_label = Label(text = "Miles", font=("Arial",14))
# my_label.config(text = "New Text")
miles_label.grid(row = 0, column = 2)

km_label = Label(text = "Kilometer", font=("Arial",14))
# my_label.config(text = "New Text")
km_label.grid(row = 1, column = 2)

my_label = Label(text = "", font=("Arial",24,"bold"))
# my_label.config(text = "New Text")
my_label.grid(row = 2, column = 2)

km_cal_label = Label(text = "", font=("Arial",14))
km_cal_label.grid(row = 1, column = 1)


# Entries
miles_ip = Entry(width=15)
# Add some text to begin with
miles_ip.insert(END, string="0")
# Gets text in entry
print(miles_ip.get())
miles_ip.grid(row = 0, column = 1)

# Button
button = Button(text = "Calculate", command = miles_to_km) # command is name of the function without ()
button.grid(row = 2, column = 1)








# has to at the very end
window.mainloop()
