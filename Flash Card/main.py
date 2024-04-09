from tkinter import *
import random
import pandas as pd

# ---------------------------- CONSTANTS ------------------------------- #
# FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
to_learn = {}
# ------------------------------ WORDS --------------------------------- #

try:

    words_df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = words_df.to_dict(orient ="records")


# -------------------------- READING FILES ----------------------------- #
def new_word():
    """
    Giving new word each time player correctly or incorrectly identifies a word
    :return:
    """
    global current_card, flip_wait
    window.after_cancel(flip_wait)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text = "French", fill = "black")
    canvas.itemconfig(word, text = current_card["French"], fill = "black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_wait = window.after(3000, func=card_flip)

# ---------------------------- CARD FLIP ------------------------------- #
def card_flip():
    """
    Card to flip to english translations to let the user check uts answer
    :return:
    """
    canvas.itemconfig(canvas_image, image = back_img)
    canvas.itemconfig(title, text="English",  fill = "white")
    canvas.itemconfig(word, text = current_card["English"],  fill = "white")

# ---------------------------- LEARNING -------------------------------- #
# remove the card from the list of words to learn
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index = False)
    new_word()

# ---------------------------- UI SETUP -------------------------------- #
window = Tk()
window.title("Language Learner")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_wait = window.after(3000, func = card_flip)

# Setting up canvas
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)

# Canvas - Images
front_img = PhotoImage(file = "./images/card_front.png")
back_img = PhotoImage(file = "./images/card_back.png")

# Canvas
canvas_image = canvas.create_image(400, 263, image = front_img)
title = canvas.create_text(400, 150, text = "", fill = "black", font = (FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 263, text = "", fill = "black", font = (FONT_NAME, 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)

# Wrong Button
wrong_img = PhotoImage(file = "./images/wrong.png")
wrong_button = Button(text = "", width = 100, height = 99, image = wrong_img, highlightthickness=0, command = new_word)
wrong_button.grid(row = 1, column = 1)

# Correct Button
correct_img = PhotoImage(file = "./images/right.png")
correct_button = Button(text = "", width = 100, height = 99, image = correct_img, highlightthickness=0, command = is_known)
correct_button.grid(row = 1, column = 0)

# Calling new word to generate the first word
new_word()



window.mainloop()