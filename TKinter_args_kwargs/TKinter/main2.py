# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)
# adding padding to all the components
window.config(padx= 200, pady = 200)

# Any widget create without pack() place() or gird() will not be represented in output screen
# grid() it is imagined that the entire program is  grid of any number of rows and columns
# grid is relative to other components

# label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
my_label.config(text = "New Text")
my_label.grid(column = 0, row = 0)
# adding padding to a specific widget
my_label.config(padx = 30, pady = 40)

# Button
button = Button(text = "Click Me", command = button_clicked)
button.grid(column = 1, row = 1)

# Button
new_button = Button(text = "New Click Me", command = button_clicked)
new_button.grid(column = 2, row = 0)

# Entry
input = Entry(width=10)
print(input)
input.grid(column = 3, row = 2)


















# has to at the very end
window.mainloop()