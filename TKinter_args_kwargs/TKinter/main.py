# import tkinter
from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text)

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text = "I am a label", font=("Arial",24,"bold"))
my_label.config(text = "New Text")
my_label.pack() # without this it will not be visible on the screen, it packs the label to be represented in the screen

# my_label["text"] = "New Text" # my_label.config(text = "yay")

# Button
button = Button(text = "Click Me", command = button_clicked) # command is name of the function without ()
button.pack()


# Entry
input = Entry(width=10)
print(input.get())
input.pack()


















# has to at the very end
window.mainloop()