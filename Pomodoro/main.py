from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)
# taking the size of the image to be used
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)


# Timer
timer_label = Label(text = "Timer", font=(FONT_NAME,50,"bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column = 1)

# Tickmark
tick_label = Label(text = "🗸", font=("Arial",24,"bold"), fg = GREEN, bg = YELLOW)
tick_label.grid(row = 3, column = 1)

# start_button
start_button = Button(text = "START", highlightthickness=0)
start_button.grid(row = 2, column = 0)
start_button.grid

# reset_button
reset_button = Button(text = "RESET", highlightthickness=0)
reset_button.grid(row = 2, column = 2)
reset_button.grid


window.mainloop()