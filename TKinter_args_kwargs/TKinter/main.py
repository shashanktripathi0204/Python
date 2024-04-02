import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text = "I am a label", font=("Arial",24,"bold"))
my_label.pack() # without this it will not be visible on the screen, it packs the label to be represented in the screen
















# has to at the very end
window.mainloop()