# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# Any widget create without pack() place() or gird() will not be represented in output screen
# place() is for precise positioning, we place at x and y value-> downside is that it is very specific

# label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
my_label.config(text = "New Text")
# these x and y value depend on width and height provided
my_label.place(x = 130, y = 50)

# Button
button = Button(text = "Click Me", command = button_clicked)


# Entry
input = Entry(width=10)
print(input.get())


















# has to at the very end
window.mainloop()