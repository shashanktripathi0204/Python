from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 # will keep track of timers
timer = None
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text = "Timer", fg = GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    global reps
    reps = 0
    tick_label.config(text = "")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps > 8:
        return

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text = "Break", fg = RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", fg = GREEN)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg = PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # finding the min and seconds value
    count_min = math.floor(count/60)
    count_sec = count % 60
    # making the starting as mm:00
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    # print(count)
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_Sessions = math.floor(reps/2)
        for _ in range(work_Sessions):
            marks += "✔"
        tick_label.config(text = marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# taking the size of the image to be used
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column = 1)

# Timer
timer_label = Label(text = "Timer", font=(FONT_NAME,50,"bold"), fg = GREEN, bg = YELLOW)
timer_label.grid(row = 0, column = 1)

# Tickmark
tick_label = Label(font=("Arial",24,"bold"), fg = GREEN, bg = YELLOW)
tick_label.grid(row = 3, column = 1)

# start_button
start_button = Button(text = "START", highlightthickness=0, command = start_timer)
start_button.grid(row = 2, column = 0)
start_button.grid

# reset_button
reset_button = Button(text = "RESET", highlightthickness=0, command = reset_timer)
reset_button.grid(row = 2, column = 2)
reset_button.grid


window.mainloop()